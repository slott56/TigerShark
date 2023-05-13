"""
Base definitions for X12 message constructs:

- Element -- the atomic base value

- Composite -- a sequence of Elements

- Segment -- a sequence of [Composite | Element] with a prefix code (e.g., "ISA", "IEA")

- Loop -- a sequence of [Loop | Segment]

- Message -- a sequence of Loop

Elements have an element separator (often "|")

Composites seem to have a component separator (varies widely, but ":" is common)

Segments have a segment separator (often "~")

For now, each of these classes has overall attributes defined in a ``Schema`` class definition.
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
import json
import logging
import sys
from types import GenericAlias, UnionType, NoneType
from typing import (
    Any, cast, get_type_hints, get_origin, get_args, assert_type, Union, TypeAlias,
    Annotated, Sequence
)
from .annotations import *

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

    When parsing the initial ISA segment, there's no defined ``element_sep``.
    During parsing the ISA, the ``element_sep`` and ``segment_sep`` can be located,
    and used for all following segments. The ``array_sep`` (or component separator) is explicitly
    provided in the ISA segment; this is used to decompose composites.

    In some rare cases, the ISA is already compressed. The element and segment
    separation characters must be provided separately.

    ..  todo:: Consider str | TextIO | Path as ``text`` parameter types.
    """
    logger = logging.getLogger("x12.base.Source")

    def __init__(self, text: str, element_sep: str = "", segment_sep: str = "", array_sep: str = "") -> None:
        self.text = text
        self.element_sep = element_sep  # Often "|", might be "*".
        self.segment_sep = segment_sep  # Often "~".
        # The Component_Separator is the value of ISA16. It is not, generally, set in advance.
        self.array_sep = array_sep  # Often ":". Sometimes "^".
        self.pos: int = 0

    def elements(self) -> list[str | list[str]]:
        """
        Unpack a Segment into a list of potential Element values.
        This consumes whitespace.
        It consumes the segment up to (and including) the segment_sep character.

        Note the initial ISA segment is fixed length, not compressed. Separators aren't defined yet.
        The initial ISA segment's text is returned as a single string for parsing by the segment.

        Most elements are atomic with two notable exceptions:

        -   There array array-like elements that leverage
            the ISA16 Component Separator character, called the
            ``array_sep`` here.

        -   Composites are punctuated by the ISA16 Component Separator character.

        We choose to parse these non-atomic elements here by looking at the values
        and splitting any that have the separator character.

        Conceptually:

            >>> source = "field|comp:osite|field~"
            >>> segments = source.split("~")
            >>> fields = segments[0].split("|")
            >>> fields = [v.split(":") if ":" in v else v for v in fields]
            >>> fields
            ['field', ['comp', 'osite'], 'field']

        ..  todo:: Optimize the field and composite splitting to avoid creating multiple lists.
        """
        if not self.segment_sep:
            raise RuntimeError("no element or segment separators set")  # pragma: no cover
        # Consume whitespace.
        while self.pos != len(self.text) and self.text[self.pos].isspace():
            self.pos += 1
        # TODO: re.search() might be faster at finding the next segment separator
        start = self.pos
        while self.pos != len(self.text) and self.text[self.pos] != self.segment_sep:
            self.pos += 1
        # assert self.text[self.pos] == self.segment_sep
        if self.pos != len(self.text):
            self.pos += 1
        elements = self.text[start:self.pos-1].rstrip().split(self.element_sep)
        # ISA segment? Do NOT subdivide ISA16 field's value -- it vanishes into ``["", ""]``.
        # TODO: Segment ISA parser can replace ISA16 ``["", ""]`` value with the parsed array_sep value.
        if elements[0] == "ISA":
            return cast(list[str | list[str]], elements)
        return [
            val.split(self.array_sep) if self.array_sep in val else val
            for val in elements
        ]

    def peek(self, size: int = 106) -> str:
        """
        Peek ahead a fixed number of characters. This also consumes leading whitespace.
        The default peek is 106 to read a non-compressed ISA segment.
        """
        # Consume whitespace.
        while self.pos != len(self.text) and self.text[self.pos].isspace():
            self.pos += 1
        # Handle the weird case of segment separator **preceeded** by whitespace.
        end = self.pos + size
        segment = self.text[self.pos: end].rstrip()
        while (
                len(segment) != size and
                end != len(self.text)
        ):
            self.logger.debug("Whitespace before segment separator")
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
            # Assume a 3-char prefix until we have a separator
            return self.text[self.pos: self.pos+3]
        # TODO: re.search() might be faster at finding the next element separator
        start = end = self.pos
        while end != len(self.text) and self.text[end] != self.element_sep:
            end += 1
        return self.text[start: end]

    def __repr__(self) -> str:
        return f"{self.element_sep=} {self.segment_sep=} text={self.text[:self.pos]!r} && {self.text[self.pos:]!r}"


class X12DataType:
    fill = " "

    def __init__(self, min_len: int | None = None, max_len: int | None = None, scale: int = 0) -> None:
        self.min_len = min_len
        self.max_len = max_len
        self.scale = scale

    def to_py(self, source: str | None) -> Any:
        return source

    def to_str(self, value: Any) -> str | None:
        """Apply right fill char to get to min_len, if provided."""
        if value:
            if self.min_len:
                return f"{value:{self.fill}<{self.min_len}s}"
            return f"{value}"
        # Rewrite zero-len strings as None.
        return f"{value}"


## TODO: Replace these with annotations.
## TODO: Refactor the features into Segment and Composite
## - element_parse(type, str) -> Any:
## - element_str(type, Any) -> str:

class ANType(X12DataType):
    pass


class BType(X12DataType):
    pass


class DTType(X12DataType):
    def __init__(self, min_len: int | None = None, max_len: int | None = None, scale: int = 0) -> None:
        super().__init__(min_len, max_len, scale)
        if self.min_len == 6 and self.max_len == 6:
            self.date_formats = ["%y%m%d"]
        elif self.min_len == 8 and self.max_len == 8:
            self.date_formats = ["%Y%m%d"]
        else:
            self.date_formats = ["%Y%m%d", "%y%m%d"]

    def to_py(self, source: str | None) -> Any:
        if source:
            for d_format in self.date_formats:
                try:
                    return datetime.datetime.strptime(source, d_format).date()
                except ValueError:  # pragma: no cover
                    pass
            raise ValueError(f"could not parse DT {source=} with formats {self.date_formats}")  # pragma: no cover
        return None

    def to_str(self, value: Any) -> str:
        # print(f"DTType.to_str({value=}) {self.min_len=} {self.max_len=} {self.date_formats[0]=}")
        return value.strftime(self.date_formats[0])


class IDType(X12DataType):
    fill = "0"
    def to_str(self, value: Any) -> str | None:
        """Apply left fill char to get to min_len, if provided."""
        # print(f"IDType.to_str({value=}) {self.min_len=} {self.max_len=}")
        if value:
            if self.min_len:
                return f"{str(value):{self.fill}>{self.min_len}s}"
            else:
                return f"{value}"
        # Tends to rewrite zero-len strings as None.
        return None


class RType(X12DataType):
    fill = "0"
    def to_py(self, source: str | None) -> Any:
        if source:
            return float(source)
        return None

    def to_str(self, value: Any) -> str:
        """
        Apply left fill char to get to min_len, if provided.
        Remove trailing zeroes. If it was a whole number, remove the dot, too.
        """
        if value is not None:
            if self.min_len:
                return f"{value:{self.fill}>{self.min_len}f}".rstrip("0").rstrip(".")
            else:
                return f"{value}".rstrip("0").rstrip(".")
        else:
            return ""  # pragma: no cover


class TMType(X12DataType):
    def __init__(self, min_len: int | None = None, max_len: int | None = None, scale: int = 0) -> None:
        super().__init__(min_len, max_len, scale)
        if self.min_len == 4 and self.max_len == 4:
            self.time_formats = ["%H%M"]
        elif self.min_len == 4 and self.max_len == 8:
            # Some length annotations is min 4 to max 8. Unclear what the remaining 4 digits might be.
            self.time_formats = ["%H%M", "%H%M%S",]
        elif self.min_len == 6 and self.max_len == 6:
            # Makes sense logically. No examples, though.
            self.time_formats = ["%H%M%S"]  # pragma: no cover
        else:
            self.time_formats = ["%H%M", "%H%M%S", ]

    def to_py(self, source: str | None) -> Any:
        # print(f"TMType.to_py({source=}) {self.time_formats=}")
        if source:
            for t_format in self.time_formats:
                try:
                    tm = datetime.datetime.strptime(source, t_format).time()
                    self.time_formats = [t_format]
                    # print(f"TMType.to_py({source=}) {self.time_formats=} {tm=}")
                    return tm
                except ValueError:
                    pass
            raise ValueError(f"could not parse TM {source=} with formats {self.time_formats}")  # pragma: no cover
        return None

    def to_str(self, value: Any) -> str:
        # print(f"TMType.to_str({value=}) {self.min_len=} {self.max_len=} {self.time_formats[0]=}")
        if value is not None:
            return value.strftime(self.time_formats[0])
        return ""  # pragma: no cover


class NType(X12DataType):
    fill = "0"
    def to_py(self, source: str | None) -> Any:
        if source is not None:
            if source == "":
                return Decimal("0").scaleb(-self.scale)  # pragma: no cover
            return Decimal(source).scaleb(-self.scale)
        return None

    def to_str(self, value: Any) -> str:
        """Apply left fill char to get to min_len, if provided."""
        base_text = str(value).replace(".", "")
        if self.min_len:
            return f"{base_text:{self.fill}>{self.min_len}s}"
        else:
            return base_text


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
    """
    An abstraction for the Schema embedded in a class.

    .. todo: Replace this structure with an annotation.

    ::

        element: Annotation[int | str | float | decimal, details...]

    The datatype values become the details. ``MinLen()``, ``MaxLen()``, ``Format()``, ``Scale()``, etc.

    The codes become a detail with ``Literal[...]``

    The segment name is tricky. This becomes a ``_segment_name: Literal["NAME"]`` that **must be first**.
    """
    json: dict[str, Any]
    datatype: dict[str, Any] | None
    codes: list[str] | None
    min_len: int | None
    max_len: int | None
    segment_name: str | None

def type_factory(schema: type[SchemaType]) -> X12DataType:
    """
    This version works with Schema and is the interim solution.
    With Annotations, this is replaced by a generic conversion.
    """
    if hasattr(schema, "datatype") and schema.datatype:
        type_code: str = schema.datatype['data_type_code']
        min_len: int | None = schema.datatype.get('minLength', None)
        max_len: int | None = schema.datatype.get('maxLength', None)
        scale: int | None = schema.datatype.get('scale', None)
    else:
        # Defaults if the data type was never defined
        type_code = "AN"
        min_len = None
        max_len = None
        scale = None
    cls = TYPE_CLASS_MAP[type_code]
    # Any overrides to the base definition?
    if hasattr(schema, "min_len"):
        if (v := getattr(schema, "min_len")) > 0:
            min_len = v
    if hasattr(schema, "max_len"):
        if (v := getattr(schema, "max_len")) > 0:
            max_len = v
    helper = cls(min_len=min_len, max_len=max_len, scale=scale or 0)
    return helper


SegmentText: TypeAlias = list[str | None | list[str | None]]


class Element:
    """
    An atomic element.

    This has a ``value`` attribute with the value.

    Two kinds of subclasses are possible.

    -   Those defined with a ``Schema`` attribute with the JSONSchema definition.
        These have a ``source`` attribute has the source text.
        And a ``type_helper`` attribte with an ``X12DataType`` type definition.

    -   Those defined with a ``value`` attribute with an annotated type.

    This may raise ValueError exceptions for invalid data.
    """
    Schema: type[SchemaType]
    logger = logging.getLogger("x12.base.Element")

    def __init__(self, source: str | None = None) -> None:
        schema = self.__class__.Schema
        # if hasattr(schema, "codes"):
        #     self.codes = schema.codes
        # else:
        #     self.codes = None
        self.type_helper = type_factory(schema)
        self.value = self.type_helper.to_py(source)

    @property
    def source(self) -> str | None:
        if self.value is not None:
            return self.type_helper.to_str(self.value)
        else:
            return None

    @classmethod
    def schema(cls: type["Element"]) -> dict[str, Any]:
        if not hasattr(cls, "Schema"):
            raise TypeError(f"{cls} has no Schema attribute")  # pragma: no cover
        return getattr(cls.Schema, 'json', {}) | getattr(cls.Schema, 'datatype', {})

    @classmethod
    def build(cls: type["Element"], source_value: str | None) -> "Element":
        cls.logger.debug("build %s with %r", cls.__name__, source_value)
        return cls(source_value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.source!r})"

    def asdict(self) -> dict[str, Any] | str | None:
        return self.source

class Composite:
    """
    A composite of values separated the "array_sep".

    Souce may have ``value|comp:osite|value``
    where the composite will be parsed into ``["comp", "osite"]``

    ..  todo:: Develop a better way to exclude "Schema" from type hints. OR. Do away with Schema.
    """
    Schema: type[SchemaType]
    logger = logging.getLogger("x12.base.Composite")

    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def schema(cls: type["Composite"]) -> dict[str, Any]:
        if not hasattr(cls, "Schema"):
            raise TypeError(f"{cls} has no Schema attribute")  # pragma: no cover
        assert_type(cls.Schema, type[SchemaType])
        fields = get_type_hints(cls)
        return cls.Schema.json | {
            "properties": {
                name: get_args(field_type)[0].schema() if isinstance(field_type, GenericAlias) else field_type.schema()
                for name, field_type in fields.items()
                if name not in {'Schema',}
            }
        }

    @classmethod
    def attr_build(cls, field_type: type, source_value: str | None) -> "Element":
        """Populate Element or Element | None field value"""
        match field_type:
            case UnionType():
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")  # pragma: no cover
                return alternatives[0].build(source_value)
            case _ if issubclass(field_type, Element):
                return field_type.build(source_value)
        raise TypeError(f"unexpected type {field_type}")  # pragma: no cover

    @classmethod
    def build(cls: type["Composite"], source_value: str | None | list[str | None]) -> "Composite":
        fields = get_type_hints(cls)
        cls.logger.debug("build %s with %s", cls.__name__, fields)
        if not isinstance(source_value, list):
            source_value = [source_value]
        num_fields = sum(1 for name in fields if name != 'Schema')
        if num_fields < len(source_value):
            # Too many values for the fields of this composite.
            raise ValueError(
                f"wrong number of values {cls.__name__} needs {num_fields} provided {len(source_value)}"
            )  # pragma: no cover
        elif num_fields > len(source_value):
            source_value.extend([None] * (num_fields - len(source_value)))
        else:
            # num_fields == len(source_value)
            pass
        arg_dict = {}
        for name, field_type in fields.items():
            if name == "Schema":
                continue
            arg_dict[name] = cls.attr_build(field_type, source_value.pop(0))
        return cls(**arg_dict)

    @property
    def source(self) -> list[str | None]:
        fields = get_type_hints(self)
        return [getattr(self, name).source for name in fields if name != 'Schema']

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)!r}" for name in fields if name != 'Schema')
        return f"{self.__class__.__name__}({text})"

    def asdict(self) -> dict[str, Any] | str:
        self.logger.debug("asdict(%r)", self)
        fields = get_type_hints(self.__class__)
        name_value = ((name, getattr(self, name)) for name in fields if name != 'Schema')
        non_none_name_value = ((name, value) for name, value in name_value if value is not None)
        return {"_kind": "Composite", "_name": self.__class__.__name__} | {
            name: [e.asdict() for e in value] if isinstance(value, list) else value.asdict()
            for name, value in non_none_name_value
        }


class Segment:
    """
    A Segment is a collection of ``Elements | Composite``.

    Composites have array_sep separators.
    The lexical scanner turns these into sub-lists of the element value list.
    So ``element1|comp:osite|element3`` is three element
    values: ``["element1", ["comp", "osite"], "element3"]``.

    The ISA Segment is special. It's generally fixed-length, and it defines the element and segment separators
    used everywhere else.

    When parsing ISA, we handle this as a distinct special case.

    ..`todo:: IndexError: pop from empty list often means wrong separators.
    """
    Schema: type[SchemaType]
    logger = logging.getLogger("x12.base.Segment")

    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def schema(cls: type["Segment"]) -> dict[str, Any]:
        if not hasattr(cls, "Schema"):
            raise TypeError(f"{cls} has no Schema attribute")  # pragma: no cover
        assert_type(cls.Schema, type[SchemaType])
        fields = get_type_hints(cls)
        return cls.Schema.json | {
            "properties": {
                name: get_args(field_type)[0].schema() if isinstance(field_type, GenericAlias) else field_type.schema()
                for name, field_type in fields.items()
                if name not in {'Schema',}
            }
        }

    @classmethod
    def attr_build(cls, field_type: type, source_values: list[str | None | list[str | None]]):
        """
        Walks type structure to create Elements and Composites.

        May pop source_values.

        ..  todo:: Implement array -- this is a feature of an 834 message (only)

            Get the PyX12 834 example with the ":"-separated value of 2100A or 2100B DMG05.
        """
        cls.logger.debug("attr_build %s from %r", field_type, source_values)
        match field_type:
            case GenericAlias():  # list[Something]
                assert get_origin(field_type) is list
                # COMPOSITE-LIKE PROCESSING for elements that are list[Element]
                repeating_type = get_args(field_type)[0]
                cls.logger.debug("  parse array list[%s]", repeating_type.__name__)
                source_array = cast(list[str], source_values.pop(0))
                values = [repeating_type.build(item) for item in source_array]
                return values
            case UnionType():  # list[Something] | None OR Something | None
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")  # pragma: no cover
                if source_values:
                    return cls.attr_build(alternatives[0], source_values)
                return cls.attr_build(alternatives[0], [None])
            case _ if issubclass(field_type, Element):
                # Consume a single value from the elements of this segment.
                value: str = cast(str, source_values.pop(0))
                return field_type.build(value)
            case _ if issubclass(field_type, Composite):
                # Next value in this segment *should* be a list.
                # If it didn't have the component separator, we make single-element list.
                composite_value: list[str | None]
                if source_values:
                    composite_value = cast(list[str | None], source_values.pop(0))
                else:
                    composite_value = []
                return field_type.build(composite_value)
        raise TypeError(f"unexpected type {field_type} {field_type.mro()}")  # pragma: no cover

    @classmethod
    def parse(cls: type["Segment"], source: Source) -> Union["Segment", None]:
        """
        Parses segments in general.

        Handles ISA segments specially to extract element and segment separators.
        """
        fields = get_type_hints(cls)
        cls.logger.debug("parse %s with %s", cls.__name__, fields)
        if not hasattr(cls, "Schema"):
            raise TypeError(f"{cls} has no Schema attribute")  # pragma: no cover
        assert_type(cls.Schema, type[SchemaType])
        segment_name = cls.Schema.segment_name
        if source.next_segment() != segment_name:
            return None

        # Special case: the ISA segment can update the ``Source`` parsing state.
        # Used in the general case when ISA header not compressed.
        if segment_name == "ISA" and not source.element_sep:
            # Sum of field size + separator for each field.
            # + 3 for header "ISA"
            # + 1 for final segment separator
            size = sum(field_type.Schema.max_len + 1 for name, field_type in fields.items() if name != 'Schema') + 4
            cls.logger.debug("ISA: source.element_sep=%r, source.segment_sep=%r", source.element_sep, source.segment_sep)
            cls.logger.debug("ISA: size=%s", size)  # Should be 106 to include segment separator
            raw_text = source.peek(size)
            cls.logger.debug("ISA: text=%r, separators text[-3:]=%r", raw_text, raw_text[-3:])
            # ISA16 has the composite separator.
            # It's preceeded by an element separator and followed by the segment separator.
            source.element_sep = raw_text[-3]
            source.array_sep = raw_text[-2]
            source.segment_sep = raw_text[-1]

        flat_values = cast(list[str | None | list[str | None]], source.elements())[1:]  # Drops the segment name from the values.
        cls.logger.debug("SEGMENT %s: fields %s values %r", cls.__name__, fields, flat_values)

        arg_dict: dict[str, Element | Composite] = {}
        for name, field_type in fields.items():
            if name == "Schema":
                continue
            arg_dict[name] = cls.attr_build(field_type, flat_values)

        obj = cls(**arg_dict)
        return obj

    def elements(self) -> list[str | None | list[str | None]]:
        """
        The segment as a list of Element source values.
        The segment text is the basis for the exchange format: a sequence of Segments.

        .. note:: Confusing overlap of names with the Source class.

            This is **not** the same concept at all.

        ..  todo:: Rename this.
        """
        fields = get_type_hints(self.__class__)
        values: list[str | None | list[str | None]] = []
        for name in fields:
            if name == "Schema":
                continue
            field: Element | Composite | list[Composite] = getattr(self, name)
            match field:
                case list():
                    values.append(
                        [cast(str | None, instance.source) for instance in field]
                    )
                case _ if isinstance(field, Element):
                    self.logger.debug(f"{name}: {field} {field.type_helper.__class__.__name__} {field.schema()=} {field.source=}")
                    values.append(field.source)
                case _ if isinstance(field, Composite):
                    values.append(field.source)
                case _:  # pragma: no cover
                    raise TypeError(f"unexpected {name}: {fields[name]} {field=}")
        return values

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)}" for name in fields if name != 'Schema')
        return f"{self.__class__.__name__}({text})"

    def asdict(self) -> dict[str, Any] | str:
        self.logger.debug("asdict(%r)", self)
        fields = get_type_hints(self.__class__)
        name_value = ((name, getattr(self, name)) for name in fields if name != 'Schema')
        non_none_name_value = ((name, value) for name, value in name_value if value is not None)
        return {"_kind": "Segment", "_name": self.__class__.__name__} | {
            name: [e.asdict() for e in value] if isinstance(value, list) else value.asdict()
            for name, value in non_none_name_value
        }

class Loop:
    """
    A Loop is a collection of ``Loop | Segment``.

    Loops and Segments can repeat, and may be optional.

    We need to examine the loop's structure of segments
    and sub-loops to match the segment prefix.
    """
    Schema: type[SchemaType]
    logger = logging.getLogger("x12.base.Loop")

    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def schema(cls: type["Loop"]) -> dict[str, Any]:
        fields = get_type_hints(cls)
        return cls.Schema.json | {
            "properties": {
                name: get_args(field_type)[0].schema() if isinstance(field_type, GenericAlias) else field_type.schema()
                for name, field_type in fields.items()
                if name not in {'Schema',}
            }
        }

    @classmethod
    def attr_build(cls, field_type: type, source: Source) -> Segment | list[Segment] | None:
        """
        Walks type structure to create sub-loops and segments.

        May consume source segments.
        """
        cls.logger.debug("attr_build %s", field_type)
        match field_type:
            case GenericAlias():  # list[Something]
                assert get_origin(field_type) is list
                repeating_type = get_args(field_type)[0]
                cls.logger.debug("  parse list[%s]", repeating_type.__name__)
                values: list[Segment] = []
                next_value = repeating_type.parse(source)
                while next_value:
                    values.append(next_value)
                    next_value = repeating_type.parse(source)
                return values
            case UnionType():  # Something | None OR list[Something] | None
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")  # pragma: no cover
                alt_type = alternatives[0]
                return cls.attr_build(alt_type, source)
            case _ if issubclass(field_type, Segment):
                seg_name = source.next_segment()
                if seg_name == "":
                    return None
                if field_type.Schema.segment_name != seg_name:
                    # TODO: segment with usage == "R"? Error
                    #  Else move on to next potential segment of Loop?
                    cls.logger.debug("expected field segment_name %r != next segment %r", field_type.Schema.segment_name, seg_name)
                    return None
                return field_type.parse(source)
            case _ if issubclass(field_type, Loop):  # pragma: no cover
                raise RuntimeError("unexpected nested Loop: {field_type} inside {cls.__name__}")
                # Alternative is to parse it...
                # return field_type.parse(source)
        raise TypeError(f"unexpected {field_type} {type(field_type)}")  # pragma: no cover

    @classmethod
    def parse(cls: type["Loop"], source: Source) -> Union["Loop", None]:
        fields = get_type_hints(cls)
        cls.logger.debug("parse %s with %s", cls.__name__, fields)
        arg_dict = {}
        for name, field_type in fields.items():
            if name == "Schema":
                continue
            loop_value = cls.attr_build(field_type, source)
            if loop_value:
                arg_dict[name] = loop_value
        if arg_dict:
            return cls(**arg_dict)
        else:
            return None

    def segment_iter(self) -> Iterator[list[str | None | list[str | None]]]:
        """
        A flat sequence of segment values in this Loop and all sub Loops.
        This is the basis for the exchange format.

        This **also** does an ``attr_build()`` style type walk.
        """
        fields = get_type_hints(self.__class__)
        self.logger.debug("segment_iter() fields=%r", fields)
        for name in fields:
            if name == "Schema" or not hasattr(self, name):
                continue
            field = getattr(self, name)
            self.logger.debug("segment_iter() name=%s field=%s", name, field)
            match field:
                case list():  # list[Something]
                    for instance in field:
                        if isinstance(instance, Loop):
                            yield from instance.segment_iter()
                        elif isinstance(instance, Segment):
                            yield cast(list[str | None | list[str | None]], [instance.Schema.segment_name]) + instance.elements()
                        else:
                            raise TypeError(f"unexpected {name}: {fields[name]} instance {instance=}")  # pragma: no cover
                case _ if isinstance(field, Loop):
                    # This doesn't seem to arise in practice.
                    yield from field.segment_iter()  # pragma: no cover
                case _ if isinstance(field, Segment):
                    yield cast(list[str | None | list[str | None]], [field.Schema.segment_name]) + field.elements()
                case _:  # pragma: no cover
                    raise TypeError(f"unexpected {name}: {fields[name]} {field=}")

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)}" for name in fields if name != 'Schema' and hasattr(self, name))
        return f"{self.__class__.__name__}({text})"

    def asdict(self) -> dict[str, Any] | str:
        self.logger.debug("asdict(%r)", self)
        fields = get_type_hints(self.__class__)
        name_value = ((name, getattr(self, name)) for name in fields if name != 'Schema' and hasattr(self, name))
        non_none_name_value = ((name, value) for name, value in name_value if value is not None)
        return {"_kind": "Loop", "_name": self.__class__.__name__} | {
            name: [e.asdict() for e in value] if isinstance(value, list) else value.asdict()
            for name, value in non_none_name_value
        }

class Message:
    """
    A top-level message, a collection of Loop.

    Loops can (and often do) repeat.
    """
    Schema: type[SchemaType]
    logger = logging.getLogger("x12.base.Message")

    def __init__(self, **arg_dict) -> None:
        for k, v in arg_dict.items():
            setattr(self, k, v)

    @classmethod
    def schema(cls: type["Message"]) -> dict[str, Any]:
        fields = get_type_hints(cls)
        return cls.Schema.json | {
            "properties": {
                name: get_args(field_type)[0].schema() if isinstance(field_type, GenericAlias) else field_type.schema()
                for name, field_type in fields.items()
                if name not in {'Schema',}
            }
        }

    @classmethod
    def parse(cls: type["Message"], source: Source) -> "Message":
        fields = get_type_hints(cls)
        cls.logger.debug("parse %s with %s", cls.__name__, fields)
        arg_dict = {}
        for name, loop_type in fields.items():
            if name == "Schema":
                continue
            match loop_type:
                case GenericAlias():
                    assert get_origin(loop_type) is list
                    repeating_type = get_args(loop_type)[0]
                    values = []
                    next_value = repeating_type.parse(source)
                    while next_value:
                        values.append(next_value)
                        next_value = repeating_type.parse(source)
                    arg_dict[name] = values
                case _ if issubclass(loop_type, Loop):
                    # Stand-alone Loop without a list[Loop] framing...
                    arg_dict[name] = loop_type.parse(source)
                case _:  # pragma: no cover
                    raise TypeError(f"unexpected {name}: {loop_type} {type(loop_type)}")
        return cls(**arg_dict)

    def segment_iter(self) -> Iterator[list[str | None | list[str | None]]]:
        """
        A flat sequence of segments in a Message.
        This is the basis for the exchange format.
        """
        fields = get_type_hints(self.__class__)
        for name in fields:
            if not hasattr(self, name) or name == "Schema":
                # Missing entirely? Weird. But. Tolerable.
                continue  # pragma: no cover
            loop = getattr(self, name)
            match loop:
                case list():
                    for instance in getattr(self, name):
                        yield from instance.segment_iter()
                case _ if isinstance(loop, Loop):
                    yield from loop.segment_iter()
                case _:  # pragma: no cover
                    raise TypeError(f"unexpected {name}: {fields[name]} {loop=}")

    def __repr__(self) -> str:
        fields = get_type_hints(self.__class__)
        text = ", ".join(f"{name}={getattr(self, name)}" for name in fields if name != "Schema")
        return f"{self.__class__.__name__}({text})"

    def __bool__(self):
        fields = get_type_hints(self.__class__)
        return any(getattr(self, name) for name in fields if name != "Schema")

    def asdict(self) -> dict[str, Any] | str:
        self.logger.debug("asdict(%r)", self)
        fields = get_type_hints(self.__class__)
        name_value = ((name, getattr(self, name)) for name in fields if name != "Schema")
        non_none_name_value = ((name, value) for name, value in name_value if value is not None)
        return {"_kind": "Message", "_name": self.__class__.__name__} | {
            name: [e.asdict() for e in value] if isinstance(value, list) else value.asdict()
            for name, value in non_none_name_value
        }

    def json(self, indent: int | None = None) -> str:
        return json.dumps(self.asdict(), indent=indent)

def demo() -> None:
    """
    A minimal demonstration of some features of the base classes.

    >>> from x12.base import demo
    >>> demo()
    MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01=ISA_LOOP_ISA01('00'), isa16=ISA_LOOP_ISA16(':')))])
    """
    class ISA_LOOP_ISA01(Element):
        """Authorization Information Qualifier"""
        class Schema:
            json: dict[str, Any] = {}
            datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
            max_len = 2

    class ISA_LOOP_ISA16(Element):
        """Component Element Separator"""
        class Schema:
            json: dict[str, Any] = {}
            datatype = {'type': 'string', 'title': 'I16', 'data_type_code': 'AN', 'minLength': 1, 'maxLength': 1}
            max_len = 1

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
    parsed_m = MSG.parse(Source(text, element_sep="|", segment_sep="~"))
    print(parsed_m)

    built_m = MSG(
        isa_loop=[
            ISA_LOOP(
                isa=ISA_LOOP_ISA(
                    isa01=ISA_LOOP_ISA01('00'),
                    # etc.
                    isa16=ISA_LOOP_ISA16(':')
                )
            )
        ]
    )
    print(built_m)

if __name__ == "__main__":  # pragma: no cover
    logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
    demo()
    logging.shutdown()
