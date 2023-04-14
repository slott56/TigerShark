"""
Base definitions for X12 message constructs:

- Element -- the atomic base value

- Composite -- a sequence of Elements

- Segment -- a sequence of [Composite | Element] with a prefix code (e.g., "ISA", "IEA")

- Loop -- a sequence of [Loop | Segment]

- Message -- a sequence of Loop

Each of these has overall attributes defined in a ``Schema`` class definition.
This class has a number of individual attribute values:

-   ``json``, has a JSONSchema object.

-   For Segments, the ``segment_name`` has the prefix code for the segment.

-   For Elements, the ``datatype`` is a reusable JSONSchema object from the ``common`` module.

-   For Elements, the ``codes`` is either a set of codes from the ``common`` module
    or the list of codes provided in the message schema.

Design
======

The top-level (Message, Loop, Segment) structures all have a :meth:`parse` method
to parse a :meth:`Source` instance. This consumes whole segments.

The bottom-level (Composite, Element) structures have a :meth:`build` method that
consumes oen or more fields of a segment. Composite will consume multiple element values.
Element will consume a single element value.
"""
from collections.abc import Iterator
import datetime
from decimal import Decimal
import logging
import sys
from types import GenericAlias, UnionType, NoneType
from typing import Any, get_type_hints, get_args, assert_type, Union


logger = logging.getLogger("x12.base")


class Source:
    """
    The source text used to parse a message in "Exchange format."

    High-level client's :meth:`parse` method will consume an entire segment, up to the segment separator.
    This applies to :class:`Method`, :class:`Loop`, and :class:`Segment`.
    The :meth:`next_segment` method lets a client peek at the prefix to the next segment.

    Low-level client's :meth:`build` method will consume element values from a segment.
    The :meth:`elements` method decomposes the current segment, and advances to the next segment.

    State invariant: ``self.text[self.pos]`` is the start of a segment.

    When parsing the initial ISA segment; there's no defined ``element_sep``.
    During parsing the ISA, the ``element_sep`` and ``segment_sep`` can be located,
    and used for all following segments.

    In some rare cases, the ISA is already compressed. The element and segment
    separation characters must be provided separately.

    TODO: Consider str | TextIO | Path as ``text`` parameter type.

    TODO: Consider how to read multiple complete messages from a single file.
        Is this appropriate?
    """
    def __init__(self, text: str, element_sep: str = "", segment_sep: str = "") -> None:
        self.text = text
        self.element_sep = element_sep  # Often "|", might be "*".
        self.segment_sep = segment_sep  # Often "~".
        self.pos: int = 0

    def elements(self) -> list[str]:
        """
        Unpack a Segment's into a list of potential Element values.
        This consumes whitespace.
        It consumes the segment up to (and including) the segment_sep character.

        Note the initial ISA segment is fixed length, not compressed. Separators aren't defined yet.
        The initial ISA segment's text is returned as a single string for parsing by the segment.
        """
        if not self.segment_sep:
            raise RuntimeError("no element or segment separators set")
        # Consume whitespace.
        while self.pos != len(self.text) and self.text[self.pos].isspace():
            self.pos += 1
        start = self.pos
        while self.pos != len(self.text) and self.text[self.pos] != self.segment_sep:
            self.pos += 1
        if self.pos != len(self.text):
            self.pos += 1
        return self.text[start:self.pos-1].rstrip().split(self.element_sep)

    def peek(self, size: int = 106) -> str:
        """
        Peek ahead a fixed number of characters. This also consumes leading whitespace.
        The default peek is 106 to read a non-compressed ISA segment.
        """
        # Consume whitespace.
        while self.pos != len(self.text) and self.text[self.pos].isspace():
            self.pos += 1
        # Handle the weird case of segment separator preceeded by whitespace.
        end = self.pos + size
        segment = self.text[self.pos: end].rstrip()
        while (
                len(segment) != size and
                end != len(self.text)
        ):
            logger.debug("Source: Whitespace before segment separator")
            if not self.text[end].isspace():
                segment += self.text[end]
            end += 1
        return segment

    def next_segment(self) -> str:
        """Peek at upcoming segment's header. This consumes leading whitespace."""
        # Consume whitespace.
        while self.pos != len(self.text) and self.text[self.pos].isspace():
            self.pos += 1
        if not self.element_sep:
            # Assume 3-char prefix until we have a separator
            return self.text[self.pos: self.pos+3]
        start = end = self.pos
        while end != len(self.text) and self.text[end] != self.element_sep:
            end += 1
        return self.text[start: end]

    def __repr__(self) -> str:
        return f"{self.element_sep=} {self.segment_sep=} text={self.text[:self.pos]!r} && {self.text[self.pos:]!r}"


class X12DataType:
    fill = " "

    def __init__(self, min_len: int = 0, scale: int = 0) -> None:
        self.min_len = min_len
        self.scale = scale

    def to_py(self, element: "Element") -> Any:
        return element.source

    def to_str(self, element: "Element") -> str:
        """Apply right fill char to get to min_len, if provided."""
        if self.min_len:
            return f"{element.value:{self.fill}<{self.min_len}s}"
        else:
            return f"{element.value}"


class ANType(X12DataType):
    pass


class BType(X12DataType):
    pass


class DTType(X12DataType):
    def to_py(self, element: "Element") -> Any:
        return datetime.datetime.strptime(element.source, "%Y%m%d").date()

    def to_str(self, element: "Element") -> str:
        return element.value.strftime("%Y%m%d")


class IDType(X12DataType):
    fill = "0"
    def to_str(self, element: "Element") -> str:
        """Apply left fill char to get to min_len, if provided."""
        if self.min_len:
            return f"{str(element.value):{self.fill}>{self.min_len}s}"
        else:
            return f"{element.value}"


class RType(X12DataType):
    fill = "0"
    def to_py(self, element: "Element") -> Any:
        return float(element.source)

    def to_str(self, element: "Element") -> str:
        """Apply left fill char to get to min_len, if provided."""
        if self.min_len:
            return f"{element.value:{self.fill}>{self.min_len}f}"
        else:
            return f"{element.value}"


class TMType(X12DataType):
    def to_py(self, element: "Element") -> Any:
        return datetime.datetime.strptime(element.source, "%H%M").time()

    def to_str(self, element: "Element") -> str:
        return element.value.strftime("%H%M")


class NType(X12DataType):
    fill = "0"
    def to_py(self, element: "Element") -> Any:
        return Decimal(element.source)

    def to_str(self, element: "Element") -> str:
        """Apply left fill char to get to min_len, if provided."""
        if self.min_len:
            base_text = str(element.value).replace(".", "")
            return f"{base_text:{self.fill}>{self.min_len}s}"
        else:
            return f"{element.value}".strip()


TYPE_CLASS_MAP = {
    "AN": ANType,
    "B": BType,
    "DT": DTType,
    "ID": IDType,
    "R": RType,
    "TM": TMType,
    "N": NType,
    "N0": NType,  # 0 decimal places, i.e. integer.
    "N1": NType,
    "N2": NType,  # 2 decimal places, i.e. currency.
    "N3": NType,
    "N4": NType,
    "N5": NType,
    "N6": NType,
    "N7": NType,
    "N8": NType,
    "N9": NType,
}


class SchemaType:
    """An abstraction for the Schema embedded in a class."""
    json: dict[str, Any]
    datatype: dict[str, Any] | None
    codes: list[str] | None
    min_len: int | None
    max_len: int | None
    segment_name: str | None


def type_factory(schema: type(SchemaType)) -> X12DataType:
    if hasattr(schema, "datatype"):
        type_code = schema.datatype['data_type_code']
        scale = schema.datatype.get('scale', None)
    else:
        # Defaults if the data type was never defined
        type_code = "AN"
        scale = None
    cls = TYPE_CLASS_MAP[type_code]
    min_len = getattr(schema, "min_len") if hasattr(schema, "min_len") else None
    helper = cls(min_len=min_len, scale=scale)
    return helper


class Element:
    """
    An atomic element.

    This has a value attribute, schema attribute, and a datatype.
    """
    def __init__(self, source: str | None = None) -> None:
        self.source = source
        assert_type(self.__class__.Schema, SchemaType)
        if hasattr(self.__class__.Schema, "codes"):
            self.codes = self.__class__.Schema.codes
        else:
            self.code = None
        self.type_helper = type_factory(self.__class__.Schema)

    @classmethod
    def fields(cls: type("Element")) -> int:
        return 1

    @classmethod
    def build(cls: type("Element"), source_value: str) -> "Element":
        logger.debug("Element.build %s with %r", cls.__name__, source_value)
        return cls(source_value)

    @property
    def value(self) -> Any:
        """Apply any conversion based on the datatype information"""
        return self.type_helper.to_py(self)

    @value.setter
    def value(self, value: Any) -> None:
        """Validate this value before applying the change."""
        # TODO: Validate self.type_helper.to_str(value).
        self.source = self.type_helper.to_str(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.source!r})"

    def json(self) -> dict[str, Any]:
        return self.source

class Composite:
    """
    A composite of atomic elements.

    These are not visible in the exchange format.
    These are flattened out into a sequence of element values.
    """
    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def n_fields(cls: type("Element")) -> int:
        fields = get_type_hints(cls)
        return len(fields)

    @classmethod
    def attr_build(cls, field_type: type, source_values: list[str]):
        """May pop source_values."""
        match field_type:
            case UnionType():
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")
                return alternatives[0].build(source_values.pop(0))
            case _ if issubclass(field_type, Element):
                return field_type.build(source_values.pop(0))
            case _:
                raise TypeError(f"unexpected type {field_type} {type(field_type)}")

    @classmethod
    def build(cls: type("Composite"), source_values: list[str]) -> "Composite":
        fields = get_type_hints(cls)
        logger.debug("Composite.build %s with %s", cls.__name__, fields)
        if len(fields) != len(source_values):
            raise ValueError(
                f"wrong number of values {cls.__name__} needs {len(fields)} provided {len(source_values)}"
            )
        arg_dict = {}
        for name, field_type in fields.items():
            arg_dict[name] = cls.attr_build(field_type, source_values)
        return cls(**arg_dict)

    @property
    def source(self) -> list[str]:
        fields = get_type_hints(self)
        return [getattr(self, name).source for name in fields]

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)!r}" for name in fields)
        return f"{self.__class__.__name__}({text})"

    def json(self) -> dict[str, Any]:
        fields = get_type_hints(self.__class__)
        return {"__kind__": "composite", "__name__": self.__class__.__name__} | {
            name: getattr(self, name)
            for name in fields
            if getattr(self, name) is not None
        }

class Segment:
    """
    A Segment is a collection of ``Elements | Composite]``.

    Composites are flattened into a sequence of values.
    This means the exchange format parser transforms
    the flat sequence of element values into
    a structure that includes composites.

    The ISA Segment is special. It's generally fixed-length, and it defines the element and segment separators
    used everywhere else.

    If parsing ISA, we handle this as a distinct special case.
    """
    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def attr_build(cls, field_type: type, source_values: list[str]):
        """
        Walks type structure to create Elements and Composites.

        May pop source_values.
        """
        logger.debug("Segment.attr_build %s from %r", field_type, source_values)
        match field_type:
            case GenericAlias():  # list[Something]
                repeating_type = get_args(field_type)[0]
                logger.debug("  parse list[%s]", repeating_type.__name__)
                values: list[Segment] = []
                next_value = cls.attr_build(repeating_type, source_values)  # repeating_type.parse(source_values)
                values.append(next_value)
                while source_values:
                    next_value = cls.attr_build(repeating_type, source_values)  # repeating_type.parse(source_values)
                    values.append(next_value)
                return values
            case UnionType():  # list[Something] | None OR Something | None
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")
                if source_values:
                    return cls.attr_build(alternatives[0], source_values)
                return cls.attr_build(alternatives[0], [None])
            case _ if issubclass(field_type, Element):
                # Consume a single value from the elements of this segment.
                if source_values:
                    return field_type.build(source_values.pop(0))
                else:
                    return field_type.build(None)
            case _ if issubclass(field_type, Composite):
                # Consume multiple values from the elements of this segment.
                composite_values = source_values[:field_type.n_fields()]
                if len(composite_values) < field_type.n_fields():
                    composite_values.extend([None]*(field_type.n_fields() - len(composite_values)))
                del source_values[:field_type.n_fields()]
                return field_type.build(composite_values)
            case _:
                raise TypeError(f"unexpected type {field_type} {type(field_type)}")

    @classmethod
    def parse(cls: type("Segment"), source: Source) -> Union["Segment", None]:
        """
        Parses segments in general.

        Handles ISA segments specially to extract element and segment separators.
        """
        fields = get_type_hints(cls)
        logger.debug("Segment.parse %s with %s", cls.__name__, fields)
        assert_type(cls.Schema, SchemaType)
        segment_name = cls.Schema.segment_name
        if source.next_segment() != segment_name:
            return None

        # Special case: the ISA segment can update the ``Source`` parsing state.
        # Used in the general case when ISA header not compressed.
        if segment_name == "ISA" and not source.element_sep:
            # Sum of field size + separator for each field.
            # + 3 for header "ISA".
            size = sum(f.Schema.max_len + 1 for f in fields.values()) + 2
            logger.debug("ISA: source.element_sep=%r, source.segment_sep=%r", source.element_sep, source.segment_sep)
            logger.debug("ISA: size=%s", size)  # Should be 107??
            raw_text = source.peek(size)
            logger.debug("ISA: text=%r, separators text[-3:]=%r", raw_text, raw_text[-3:])
            # ISA16 (positions 103, 104 and 105) has three separator characters: element, something?, and segment.
            source.element_sep = raw_text[-3]
            source.segment_sep = raw_text[-1]

        flat_values = source.elements()[1:]  # Drops the segment name from the values.
        logger.debug("SEGMENT %s: fields %s values %r", cls.__name__, fields, flat_values)

        arg_dict: dict[str, Element | Composite] = {}
        for name, field_type in fields.items():
            arg_dict[name] = cls.attr_build(field_type, flat_values)

        # TODO: ISA16 Element has three characters: element_sep, ":", segment_sep

        obj = cls(**arg_dict)
        return obj

    def elements(self) -> list[str]:
        """
        The segment as a list of Element source values.
        The segment text is the basis for the exchange format: a sequence of Segments.
        """
        fields = get_type_hints(self.__class__)
        values: list[str] = []
        for name in fields:
            field = getattr(self, name)
            match field:
                case list():
                    for instance in field:
                        values.extend(instance.source)
                case _ if isinstance(field, Element):
                    values.append(field.source)
                case _ if isinstance(field, Composite):
                    values.extend(field.source)
                case _:
                    raise TypeError(f"unexpected {name}: {fields[name]} {field=}")
        return values

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)}" for name in fields)
        return f"{self.__class__.__name__}({text})"

    def json(self) -> dict[str, Any]:
        fields = get_type_hints(self.__class__)
        return {"__kind__": "segment", "__name__": self.__class__.__name__} | {
            name: getattr(self, name)
            for name in fields
            if getattr(self, name) is not None
        }

class Loop:
    """
    A Loop is a collection of ``Loop | Segment``.

    Loops and Segments can repeat, and may be optional.

    We need to examine the loop's structure of segments
    and sub-loops to match the segment prefix.
    """
    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def attr_build(cls, field_type: type, source: Source) -> Segment | list[Segment] | None:
        """
        Walks type structure to create sub-loops and segments.

        May consume source segments.
        """
        logger.debug("Loop.attr_build %s", field_type)
        match field_type:
            case GenericAlias():  # list[Something]
                repeating_type = get_args(field_type)[0]
                logger.debug("  parse list[%s]", repeating_type.__name__)
                values: list[Segment] = []
                next_value = repeating_type.parse(source)
                while next_value:
                    values.append(next_value)
                    next_value = repeating_type.parse(source)
                return values
            case UnionType():  # Something | None OR list[Something] | None
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")
                alt_type = alternatives[0]
                return cls.attr_build(alt_type, source)
            case _ if issubclass(field_type, Segment):
                seg_name = source.next_segment()
                if seg_name == "":
                    return None
                if field_type.Schema.segment_name != seg_name:
                    # TODO: segment with usage == "R"? Error
                    #  Else move on to next potential segment of Loop?
                    logger.debug("Loop expected field segment_name %r != next segment %r", field_type.Schema.segment_name, seg_name)
                    return None
                return field_type.parse(source)
            case _ if issubclass(field_type, Loop):
                raise RuntimeError("unexpected nested Loop: {field_type} inside {cls.__name__}")
                # Alternative is to parse it...
                # return field_type.parse(source)
            case _:
                raise TypeError(f"unexpected {field_type} {type(field_type)}")

    @classmethod
    def parse(cls: type("Loop"), source: Source) -> Union["Loop", None]:
        fields = get_type_hints(cls)
        logger.debug("Loop.parse %s with %s", cls.__name__, fields)
        arg_dict = {}
        for name, field_type in fields.items():
            loop_value = cls.attr_build(field_type, source)
            if loop_value:
                arg_dict[name] = loop_value
        if arg_dict:
            return cls(**arg_dict)
        else:
            return None

    def segment_iter(self) -> Iterator[Segment]:
        """
        A flat sequence of segments in this Loop and all sub Loops.
        This is the basis for the exchange format.

        This **also** does an ``attr_build()`` style type walk.
        """
        fields = get_type_hints(self.__class__)
        logger.debug("Loop.segment_iter() fields=%r", fields)
        for name in fields:
            if not hasattr(self, name):
                continue
            field = getattr(self, name)
            logger.debug("Loop.segment_iter() name=%s field=%s", name, field)
            match field:
                case list():  # list[Something]
                    for instance in field:
                        if isinstance(instance, Loop):
                            yield from instance.segment_iter()
                        elif isinstance(instance, Segment):
                            yield [instance.Schema.segment_name] + instance.elements()
                        else:
                            raise TypeError(f"unexpected {name}: {fields[name]} instance {instance=}")
                case _ if isinstance(field, Loop):
                    yield from field.segment_iter()
                case _ if isinstance(field, Segment):
                    yield [field.Schema.segment_name] + field.elements()
                case _:
                    raise TypeError(f"unexpected {name}: {fields[name]} {field=}")

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)}" for name in fields if hasattr(self, name))
        return f"{self.__class__.__name__}({text})"

    def json(self) -> dict[str, Any]:
        fields = get_type_hints(self.__class__)
        return {"__kind__": "loop", "__name__": self.__class__.__name__} | {
            name: getattr(self, name)
            for name in fields
            if getattr(self, name) is not None
        }

class Message:
    """
    A top-level message, a collection of Loop.

    Loops can (and often do) repeat.
    """
    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def parse(cls: type("Message"), source: Source) -> "Message":
        fields = get_type_hints(cls)
        logger.debug("Message.parse %s with %s", cls.__name__, fields)
        arg_dict = {}
        for name, loop_type in fields.items():
            match loop_type:
                case GenericAlias():
                    repeating_type = get_args(loop_type)[0]
                    values = []
                    next_value = repeating_type.parse(source)
                    while next_value:
                        values.append(next_value)
                        next_value = repeating_type.parse(source)
                    arg_dict[name] = values
                case _ if issubclass(loop_type, Loop):
                    arg_dict[name] = loop_type.parse(source)
                case _:
                    raise TypeError(f"unexpected {name}: {loop_type} {type(loop_type)}")
        return cls(**arg_dict)

    def segment_iter(self) -> Iterator[Segment]:
        """
        A flat sequence of segments in a Message.
        This is the basis for the exchange format.
        """
        fields = get_type_hints(self.__class__)
        for name in fields:
            if not hasattr(self, name):
                continue
            loop = getattr(self, name)
            match loop:
                case list():
                    for instance in getattr(self, name):
                        yield from instance.segment_iter()
                case _ if isinstance(loop, Loop):
                    yield from loop.segment_iter()
                case _:
                    raise TypeError(f"unexpected {name}: {fields[name]} {loop=}")

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)}" for name in fields)
        return f"{self.__class__.__name__}({text})"

    def __bool__(self):
        fields = get_type_hints(self.__class__)
        return any(getattr(self, name) for name in fields)

def demo() -> None:
    """
    A minimal demonstration of some features of the base classes.

    >>> from x12.base import demo
    >>> demo()
    MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01=ISA_LOOP_ISA01('00'), isa16=ISA_LOOP_ISA16(':')))])

    ..  todo:: ISA16 should be based on ``Source`` state, and have 3 chars: ``"|:~"``.
    """
    class ISA_LOOP_ISA01(Element):
        """Authorization Information Qualifier"""
        class Schema:
            json = {}
            datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
            max_len = 2

    class ISA_LOOP_ISA16(Element):
        """Component Element Separator"""
        class Schema:
            json = {}
            datatype = {'type': 'string', 'title': 'I16', 'data_type_code': 'ID', 'minLength': 3, 'maxLength': 3}
            max_len = 3

    class ISA_LOOP_ISA(Segment):
        class Schema:
            segment_name = "ISA"
        isa01: ISA_LOOP_ISA01
        isa16: ISA_LOOP_ISA16

    class ISA_LOOP(Loop):
        isa: ISA_LOOP_ISA

    class MSG(Message):
        isa_loop: list[ISA_LOOP]

    text = "ISA|00|:~"
    logger.info("Building from %r", text)
    m = MSG.parse(Source(text, element_sep="|", segment_sep="~"))
    print(m)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
    demo()
    logging.shutdown()
