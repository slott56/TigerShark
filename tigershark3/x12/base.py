"""
Base definitions for X12 message constructs:

- Element -- the atomic base value -- A python object -- str, int, float, Decimal

- Composite -- a sequence of Elements

- Segment -- a sequence of [Composite | Element] with a prefix code (e.g., "ISA", "IEA")

- Loop -- a sequence of [Loop | Segment]

- Message -- a sequence of Loop

The :py:class:`Source` class defines a parser
for the message in "Exchange" format.

-   Elements have an element separator (often "|")

-   Composites have a component separator (varies widely, but ":" is common)

-   Segments have a segment separator (often "~")

The various X12 structures are subclasses of :py:class:`Message`,
:py:class:`Loop`, :py:class:`Segment`, and :py:class:`Composite`.
The details of each element are implemented as ``Annotated[...]``
type hints.

Parsing
=======

The top-level (Message, Loop, Segment) structures all have a :meth:`parse` method
to parse a :meth:`Source` instance. This consumes whole segments.

The bottom-level (Composite) structure has a :meth:`build` method that
consumes one or more field values from a parsed segment.

JSON Schema
===========

The :py:func:`schema` function will
emit a class definition as JSON Schema.
This can be used with :func:`json.dumps` to present
a JSON dump of a schema.

JSON Output
===========

The :py:func:`asdict` function will
emit an object as a dictionary.
This can be used with :func:`json.dumps` to present
a JSON dump of a message.

The :py:meth:`Message.json` method does this
for a message.

Message Segments
================

The :py:meth:`Message.segment_iter` method
yields the sequence of segments.
This is similar to exchange format for a message.

"""
from collections import defaultdict
from collections.abc import Iterator, Callable, Hashable
import datetime
from decimal import Decimal
import fnmatch
from functools import wraps, cache
import json
import logging
import sys
from textwrap import dedent
from types import GenericAlias, UnionType, NoneType, FunctionType
from typing import (  # type: ignore [attr-defined]
    Any, cast, Protocol, overload,
    Union, TypeAlias, Annotated, Optional, DefaultDict,
    get_type_hints, get_origin, get_args, assert_type,
    _SpecialForm,
    _UnionGenericAlias,
)
from typing_extensions import _AnnotatedAlias
import warnings

from .annotations import *

logger = logging.getLogger("x12.base")


class Source:
    """
    The Source class consumes the text used to parse a message in "Exchange format."

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
    logger = logging.getLogger("x12.base.Source")  #: Logger for this class

    def __init__(self, text: str, element_sep: str = "", segment_sep: str = "", array_sep: str = "") -> None:
        """
        Build a Source to be used for parsing a message.

        :param text: the Exchange-format document
        :param element_sep: Optional element separator character. This can be deduced by parsing the ISA segment.
        :param segment_sep: Optional segment separator character. This can be deduced by parsing the ISA segment.
        :param array_sep: Optional component separator character. This is generally found in the ISA16 element of the ISA segment.
        """
        self.text = text
        self.element_sep = element_sep  # Often "|", might be "*".
        self.segment_sep = segment_sep  # Often "~".
        # The Component_Separator is the value of ISA16. It is not, generally, set in advance.
        self.array_sep = array_sep  # Often ":". Sometimes "^".
        self.pos: int = 0

    def consume_whitespace(self) -> None:
        """
        Moves ``self.pos`` past any leading whitespace.
        """
        while self.pos != len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

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

        ..  todo:: re.search() might be faster at finding segment separators than the ``while`` loop.
        """
        if not self.segment_sep:
            raise RuntimeError("no element or segment separators set")  # pragma: no cover
        self.consume_whitespace()
        # TODO: re.search() might be faster at finding the next segment separator
        start = self.pos
        while self.pos != len(self.text) and self.text[self.pos] != self.segment_sep:
            self.pos += 1
        # assert self.text[self.pos] == self.segment_sep
        if self.pos != len(self.text):
            self.pos += 1
        elements = self.text[start:self.pos-1].rstrip().split(self.element_sep)
        # ISA segment? Do NOT subdivide ISA16 field's value -- it would vanish into ``["", ""]``.
        # TODO: Alternative design is for ``Segment`` ISA parser can replace ISA16 ``["", ""]`` value with the parsed array_sep value.
        if elements[0].upper() == "ISA":
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
        self.consume_whitespace()
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
        self.consume_whitespace()
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

class ConversionCallable(Protocol):
    """A protocol for verious kinds of conversions."""
    @overload
    def __call__(self, value: str, format: str) -> Any: ...
    @overload
    def __call__(self, value: str, scale: int) -> Any: ...
    @overload
    def __call__(self, value: str | None = None, extra: str | None = None) -> Any: ...

Conversion: TypeAlias = ConversionCallable | type[Any]

Formatter: TypeAlias = Callable[["X12ElementHelper", Any], str]


class X12ElementHelper:
    """
    An X12ElementHelper
    provides methos to convert element values from source text
    to Python objects, and Python back to source text.

    Don't create an :py:mod:`X12ElementHelper` directly. Use the :py:meth:`X12ElementHelper.annotated` method.

    For example::

        hints = get_type_hints(SomeSegment, include_extras=True)
        some_helper = base.X12ElementHelper.annotated(hints['some_element'])


    The :py:meth:`X12ElementHelper.validate` method raises a :exc:`ValueError`
    exception  with two parameters:

    -   The usual message.

    -   The Annotation class name that failed validation.

    ..  TODO: A hierarchy of classes can handle primitive formatting methods better.

        The "format" feature should be subclasses not method plug-ins.
    """
    @staticmethod
    def _date(source: str, format: str) -> Any:
        return datetime.datetime.strptime(source, format).date()

    @staticmethod
    def _time(source: str, format: str) -> Any:
        return datetime.datetime.strptime(source, format).time()

    @classmethod
    def annotated(cls, type_hint: type[Any]) -> Union["X12ElementHelper", None]:
        """
        Build an :py:class:`X12ElementHelper` instance to convert an element's text to Python objects,
        and python objects back to text.

        This does *not* handle List[X] and Union[X, None].
        """
        # Wrapped classes: list[X], X | None, Annotated[X, ...]
        base: type[Any]
        aspects: list[X12Annotation]
        match type_hint:
            case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                return None
            case GenericAlias() if get_origin(type_hint) is list:
                return None
            case _AnnotatedAlias():  # type: ignore[misc]
                # An "Annotated[X]" -- extract the annotation aspects
                base, *aspects = get_args(type_hint)
                # Continues in second match step, below.
            case type():
                # A bare "X" -- work with what we have
                base = type_hint
                aspects = []
                # Continues in a second match step, below.
            case _:  # pragma: no cover
                raise TypeError(f"invalid {type_hint}")  # pragma: no cover

        # For Annotated[X] or bare X, create a helper
        # These don't seem to work well with ``match``.
        if issubclass(base, datetime.date):
            # TODO: Make this sensisitve to MinLen() and MaxLen()
            return X12ElementHelper(
                cast(Conversion, cls._date),
                *aspects,
                parse_formats=["%y%m%d", "%Y%m%d", ],
                formatter=cls.dttm_fmt
            )
        elif issubclass(base, datetime.time):
            # TODO: Make this sensisitve to MinLen() and MaxLen()
            return X12ElementHelper(
                cast(Conversion, cls._time),
                *aspects,
                parse_formats=["%H%M", "%H%M%S", ],
                formatter=cls.dttm_fmt
            )
        else:
            match base():
                case Composite():  # type() if issubclass(base, Composite):
                    return X12ElementHelper(cast(Conversion, lambda x: x), *aspects)
                case str():  # type() if base == str:
                    return X12ElementHelper(cast(Conversion, str), *aspects, formatter=cls.str_fmt)
                case int():  # type() if base == int:
                    return X12ElementHelper(cast(Conversion, int), *aspects, formatter=cls.int_fmt)
                case float():  # type() if base == float:
                    return X12ElementHelper(cast(Conversion, float), *aspects, formatter=cls.float_fmt)
                case Decimal():  # type() if base == Decimal:
                    scale_aspect = [a for a in aspects if isinstance(a, Scale)]
                    if scale_aspect:
                        scale = int(scale_aspect[0].params[0])
                    else:  # pragma: no cover
                        scale = 0
                    # Bind scale into a decimal conversion function
                    decimal_conversion_partial: Conversion = cast(
                            Conversion,
                            lambda to_decimal=None, scale=scale: (Decimal(to_decimal) if to_decimal else Decimal()).scaleb(-scale)
                    )
                    return X12ElementHelper(
                        decimal_conversion_partial,
                        *aspects,
                        formatter=cls.dec_fmt
                    )

        # Silently tolerate other structures.
        return None

    def __init__(self, conversion: Conversion, *aspects: X12Annotation, parse_formats: list[str] | None = None, formatter: Formatter | None = None) -> None:
        """
        Build an X12ElementHelper.

        :param conversion: The conversion from text to Python function.
        :param aspects: The X12Annotations from the Annotated type.
        :param parse_formats: A sequence of formats for parsing dates and times.
        :param formatter: The conversion from Python back to text. :py:func:`str` is the default.
        """
        self.conversion = conversion  # the to-python conversion function
        self.formatter = formatter or cast(Formatter, str)  # the to-text formatter function
        self.aspects = aspects  # The annotations that will be checked.
        # TODO: Seems to be a silly optimization.
        self.validation = [
            a
            for a in self.aspects
            if a.validation
        ]  # Subset of annotations that can be validated.
        self.optional = (
            any(
                a.params[0] in {"N", "S"} for a in self.aspects
                if isinstance(a, (Usage,))
            ) or any(
                not a.params[0] for a in self.aspects
                if isinstance(a, (Required,))
            )
        )  # Interpret X12 rules to see if this is optional
        self.parse_formats: list[str] = parse_formats or []  # Alternative date/time formats.
        self.dttm_format: str | None = None  # Set to the preferred cormat for dates or times.
        self.max_len = self._value_for(MaxLen) or 99
        self.min_len = self._value_for(MinLen) or 0
        self.scale = self._value_for(Scale)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.conversion}, *{self.aspects}, parse_formats={self.parse_formats or None}, formatter={self.formatter})"

    def _value_for(self, annotation_class: type[X12Annotation]) -> Any:
        """Find the last value set for a specific annotation class."""
        instances = [a for a in self.aspects if isinstance(a, annotation_class)]
        if instances:
            return instances[-1].params[0]
        else:
            return None

    def validate(self, source: str) -> None:
        if self.optional and (source == '' or source is None):
            return
        for a in self.validation:
            if msg := a.invalid(source):
                raise ValueError(msg, a.__class__.__name__)

    def to_py(self, source: str) -> Any:
        if source is None:
            # TODO: Check ``Usage`` and ``Required`` annotations
            return None
        conv_func = self.conversion
        if self.parse_formats:
            # Date/Time with multiple formats.
            for fmt in self.parse_formats:
                try:
                    v = conv_func(source, fmt)
                    self.dttm_format = fmt
                    return v
                except ValueError:
                    pass
            raise ValueError(f"invalid {source!r} formats {self.parse_formats}")  # pragma: no cover
        else:
            # Other types without format alternatives.
            if source == "":
                # Assume the conversion is a type, str, int, float, Decimal
                try:
                    return cast(type[Any], conv_func())
                except TypeError as ex:  # pragma: no cover
                    # Rare issue with conversion function being used improperly.
                    raise TypeError(f"{conv_func} {self.aspects} {ex}")
            else:
                return conv_func(source)

    def to_str(self, value: Any) -> str:
        # print(f"in {self!r}, to_str({value=}) with {self.formatter=}")
        return self.formatter(self, value)

    def str_fmt(self, value: Any) -> str:
        return f"{value:{self.min_len}s}"

    def int_fmt(self, value: Any) -> str:
        return f"{value:0>{self.min_len}d}"

    def float_fmt(self, value: Any) -> str:
        return f"{value:0>{self.min_len}.0f}"

    def dec_fmt(self, value: Any) -> str:
        base_text = f"{value:.{self.scale}f}".replace(".", "")
        return f"{base_text:0>{self.min_len}s}"

    def dttm_fmt(self, value: Any) -> str:
        if not self.dttm_format:
            self.dttm_format = self.parse_formats[0]
        return f"{value:{self.dttm_format}}"


SegmentText: TypeAlias = list[str | None | list[str | None]]


def schema(some_type: type[Any]) -> dict[str, Any]:
    """
    Expands an annotated type or any of the X12 structures into a JSON Schema.

    This is very similar to the pydantic function :py:func:`schema_of`.

    :param some_type: Any kind of type. A subclass of :py:class:`Message` is typical.
    :returns: JSON Schema.
    """

    def x12_class_base_schema(some_type: type[Any]) -> dict[str, Any]:
        properties = {
            name: schema(field_type)
            for name, field_type in class_fields(some_type)
        }
        json_schema = {
            "description": dedent(some_type.__doc__.strip()) if some_type.__doc__ else None,
            "class_name": some_type.__name__ if isinstance(some_type, type) else some_type.__class__.__name__,
            "type": "object",
            "properties": properties,
        }
        return json_schema

    annotations: list[X12Annotation] = []
    match some_type:
        case GenericAlias() if get_origin(some_type) is list:
            repeating_type, *annotations = get_args(some_type)
            json_schema = {
                "type": "array",
                "items": schema(repeating_type),
            }
        case _AnnotatedAlias():  # type: ignore [misc]
            base_type, *annotations = get_args(some_type)
            json_schema = schema(base_type)
        case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
            alternatives = get_args(some_type)
            json_schema = {
                "any": [schema(alt) for alt in alternatives]
            }
        case _:
            if issubclass(some_type, datetime.date):
                # TODO: X12ElementHelper has formats.
                json_schema = {"type": "string", "convert": "datetime.date", "pyformat": "%Y%m%d"}
            elif issubclass(some_type, datetime.time):
                json_schema = {"type": "string", "convert": "datetime.time", "pyformat": "%h%m"}
            else:
                match some_type():
                    case Composite() | Segment() | Loop() | Message():
                        json_schema = x12_class_base_schema(some_type)
                    # Classes with built-in primitive schema.
                    case str():
                        json_schema = {"type": "string"}
                    case int():
                        json_schema = {"type": "integer"}
                    case float():
                        json_schema = {"type": "number"}
                    case Decimal():
                        json_schema = {"type": "string", "convert": "Decimal", "scale": "?"}
                    case None:
                        json_schema = {"type": "null"}
                    case _:  # pragma: no cover
                        raise ValueError(f"can't make schema for {some_type} ({type(some_type)})")
    # Effectively a reduce(set.union, (ann.JSONSchema for ann in annotations if hasattr(ann, "JSONSchema")))
    for ann in annotations:
        if hasattr(ann, "JSONSchema"):
            json_schema |= ann.JSONSchema
    return json_schema

X12Structure: TypeAlias = Union[
    "Composite", "Segment", "Loop", "Message",
    str, int, float, Decimal, datetime.date, datetime.time,
    None
]

def asdict(x12_obj: X12Structure) -> dict[str, Any] | Any:
    """
    Given an X12 object (i.e., Message, Loop, Segment, Composite), emit a dictionary.

    :param x12_obj: Any X12 structure.
    :returns: a dictionary, suitable for JSON output.
    """
    match x12_obj:
        case Composite() | Segment() | Loop() | Message():
            fields = {
                name: getattr(x12_obj, name, None)
                for name, hint in class_fields(x12_obj.__class__)
            }
            non_null_fields = {
                name: asdict(value)
                for name, value in fields.items()
                if value is not None
            }
            parent = x12_obj.__class__
            return {
                '_kind': x12_obj.__class__.__mro__[1].__name__,
                '_name': x12_obj.__class__.__name__,
            } | non_null_fields
        case str() | int() | float():
            return x12_obj
        case Decimal():
            return str(x12_obj)
        case datetime.date():
            format = "%Y%m%d"
            return {"date": x12_obj.strftime(format), "_format": format}
        case datetime.time():
            format = "%H%M"
            return {"time": x12_obj.strftime(format), "_format": format}
        case list(some_items):
            return [
                asdict(item) for item in some_items
            ]
        case _:  # pragma: no cover
            raise ValueError(f"can't create value for {x12_obj} ({type(x12_obj)})")


class FieldInspector:
    """
    A ``FieldInspector`` walks the definition of fields in an X12 structure,
    providing those not excluded by a few rules:

    -   Excludes "Schema" as a special attribute name.

    -   Excludes all names starting with "_".

    -   Excludes any ``TypeAlias`` lines in the class.

    The result of scanning a structure is a list of (name, hint) tuples.

    The :py:func:`class_fields` function is the useful instance of this class.
    """
    def __init__(self) -> None:
        self.cache: dict[type[Any], list[tuple[str, type[Any]]]] = {}

    def field_iter(self, cls: type[Any]) -> Iterator[tuple[str, type[Any]]]:
        fields = get_type_hints(cls, include_extras=True)
        # Exclude "Schema" and names starting with _
        x_schema_hidden = (
            (name, field_type)
            for name, field_type in fields.items()
            if not (name in {"Schema"} or name.startswith("_"))
        )
        # Exclude the TypeAlias special form.
        x_special = (
            (name, field_type)
            for name, field_type in x_schema_hidden
            if not (isinstance(field_type, _SpecialForm) and field_type._name == "TypeAlias")  # type: ignore[attr-defined]
        )
        return x_special

    def field_list(self, cls: type[Any]) -> list[tuple[str, type[Any]]]:
        if cls not in self.cache:
            self.cache[cls] = list(self.field_iter(cls))
        return self.cache[cls]

cached_field_inspector = FieldInspector()

class_fields = cached_field_inspector.field_list  #: Function to use a :py:class:`FieldInspector` on a class, returns all non-excluded fields.


class Composite:
    """
    A Composite is a collection of elements.

    In the exchange format, they're separated the "array_sep".
    For example, the ``array_sep=":"`` and
    The :py:class:`Source` may have text ``value|comp:osite|value``.
    The composite will be parsed into ``["comp", "osite"]``

    Composites are often defined as follows.

    ::

        class Loop_Seg_Comp(Composite):
            field_2_1: Annotated[...]
            field_2_2: Annotated[...]
            etc.

        class Loop_Seg(Segment):
            field_1: Annotated[...]
            field_2: Loop_Seg_Comp
            etc.

    A Composite is generally built using the :py:meth:`composite.build` method and sequence of values.
    """
    _composite_name: str  #: Name of the composite
    _helpers: dict[str, X12ElementHelper | None]  #: X12ElementHelpers for element conversion and validation
    _skip_validation: DefaultDict[str, list[str]]  #: Elements not to be validated
    # No type hint: invisible to get_type_hints() introspection
    logger = logging.getLogger("x12.base.Composite")  #: Class Logger

    def __init__(self, **arg_dict) -> None:
        """
        Create a Composite instance by providing keyword argument values
        for each field.

        This will validate each value provided.
        """
        fields = get_type_hints(self.__class__, include_extras=True)
        unknowns = arg_dict.keys() - fields.keys()
        if unknowns:
            raise TypeError(f"unknown fields: {unknowns}")  # pragma: no cover
        self.__class__.make_helpers(fields)

        # Ideally, all missing names are also not required.
        for name, hint in class_fields(self.__class__):
            source: str = cast(str, arg_dict.get(name))
            value: Any
            if self._helpers[name] is not None:
                helper: X12ElementHelper = cast(X12ElementHelper, self._helpers[name])
                # Validate (possibly raising ValueError)
                try:
                    helper.validate(source)
                except ValueError as ex:
                    if not (name in self._skip_validation and len(ex.args) == 2):
                        raise ValueError(f"invalid {self.__class__.__name__}.{name}: {hint} {ex}") from ex
                    msg, annotation = ex.args
                    if annotation not in self._skip_validation[name]:
                        raise ValueError(f"invalid {self.__class__.__name__}.{name}: {hint} {ex}") from ex
                # Build the attribute value
                value = helper.to_py(source)
            else:
                value = source
            setattr(self, name, value)

    @classmethod
    def make_helpers(cls, fields: dict[str, type[Any]]) -> None:
        """
        Build the element ``_helpers`` for this Composite.

        Used like this::

            class XYZ(Composite):
                x01: float
                x02: float

            fields = get_type_hints(XYZ, include_extras=True)
            XYZ.make_helpers(fields)

        This updates the class with detailed helpers for each field.
        """
        if hasattr(cls, '_helpers'):
            return

        # Assume it contains *only* elements.
        cls._helpers = {
            name: X12ElementHelper.annotated(hint)
            for name, hint in class_fields(cls)
        }

    @classmethod
    def composite_configure(cls, skip_validation : DefaultDict[str, list[str]], segment_rules: list[tuple[str, str]], composite_name: str) -> None:
        """
        Provide the skip_validation configuration to the elements of this Composite.
        """
        cls._skip_validation = skip_validation
        fields = get_type_hints(cls, include_extras=True)
        cls.make_helpers(fields)
        for name, helper in cls._helpers.items():
            for field_match, annotation_name in segment_rules:
                if fnmatch.fnmatch(name, field_match):
                    cls._skip_validation[name].append(annotation_name)

    def elements(self) -> list[str | None | list[str | None | list[str | None]]]:
        """
        Returns the list of values for this composite.

        ..  note:: Confusing overlap of this elements() method with :py:class:`Source.elements` method.

            This is **not** the same concept at all.
        """
        fields = get_type_hints(self)
        return [getattr(self, name) for name, type_hint in class_fields(self.__class__)]

    def __repr__(self) -> str:
        good_names = (name for name, field_type in class_fields(self.__class__))
        text = ", ".join(f"{name}={getattr(self, name)!r}" for name in good_names)
        return f"{self.__class__.__name__}({text})"


class Segment:
    """
    A Segment is a collection of ``Elements | Composite``.

    Segments have the element_sep separators;
    any contained composites use the array_sep separtors.

    The lexical scanner turns these into sub-lists of the element value list.
    So ``seg|element1|comp:osite|element3`` will become the following list of
    values: ``["seg", "element1", ["comp", "osite"], "element3"]``.

    The ISA Segment is special. It's generally fixed-length, and it defines the element and segment separators
    used everywhere else.

    Segments are defined as a list of elements.

    ::

        class Loop_Segment(Segment):
            field_1: Annotated[str, MinLen(2), MaxLen(2)]
            field_2: Annotated[Decimal, Scale(2)]
            etc.

    When parsing the ISA segment, we handle this as a distinct special case.

    ..   note:: IndexError: pop from empty list

        often means wrong separators.
    """
    _segment_name: str  #: String name to match to parse this segment
    _helpers: dict[str, X12ElementHelper | None]  #: X12ElementHelper for field conversion and validation
    _skip_validation: DefaultDict[str, list[str]]  #: Elements not to be validated
    # No type hint: invisible to get_type_hints() introspection
    logger = logging.getLogger("x12.base.Segment")  #: Class Logger

    def __init__(self, **arg_dict) -> None:
        """
        Create a Segment instance by providing keyword argument values
        for each field.

        This will validate each value provided.
        """
        fields = get_type_hints(self.__class__, include_extras=True)
        unknowns = arg_dict.keys() - fields.keys()
        if unknowns:
            raise TypeError(f"unknown fields: {unknowns}")  # pragma: no cover
        self.__class__.make_helpers(fields)

        # Ideally all missing names are also not required.
        for name, hint in class_fields(self.__class__):
            ## TODO: Replace `None` with a "do nothing" X12ElementHelper instance.
            source: str = cast(str, arg_dict.get(name))
            value: Any
            if self._helpers[name] is not None:
                helper: X12ElementHelper = cast(X12ElementHelper, self._helpers[name])
                # Validate (possibly raising ValueError)
                try:
                    helper.validate(source)
                except ValueError as ex:
                    if not (name in self._skip_validation and len(ex.args) == 2):
                        # print(f"{self.__class__.__name__} {self._skip_validation=} {name=} {ex.args=}")
                        raise ValueError(f"invalid {self.__class__.__name__}.{name}: {hint} {ex}") from ex
                    msg, annotation = ex.args
                    if annotation not in self._skip_validation[name]:
                        # print(f"{self.__class__.__name__} {self._skip_validation=}")
                        raise ValueError(f"invalid {self.__class__.__name__}.{name}: {hint} {ex}") from ex
                # Convert
                value = helper.to_py(source)
            else:
                # No helper? Use the value without further ado (it's likely a Composite or a list[X])
                value = source
            setattr(self, name, value)

    @classmethod
    def make_helpers(cls, fields: dict[str, type[Any]]) -> None:
        """
        Build the element ``_helpers`` for this Segment.

        Used like this:

        ::

            fields = get_type_hints(SomeSegment, include_extras=True)
            SomeSegment.make_helpers(fields)
        """
        if hasattr(cls, '_helpers'):
            return
        cls._helpers = {}
        for name, hint in class_fields(cls):
            cls._helpers[name] = cls._make_helper(name, hint)

    @classmethod
    def _make_helper(cls, name: str, hint: type[Any]) -> X12ElementHelper | None:
        """
        This class creates helper wrappers for List[X] and Union[X, None].
        Otherwise, use :py:class:`X12ElementHelper` for primitives.
        """
        match hint:
            case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                # # TODO: Create a X | Y | None to_py construct.
                # # If a validate() works, that's the result, None.
                # # If none of the validate()'s work, and there's a None, that's it.
                # # Otherwise, a ValueError exception from a failing validate.

                alternatives = list(filter(lambda t: t is not NoneType, get_args(hint)))
                if len(alternatives) != 1:
                    raise NotImplementedError(
                        f"not supported {hint}; too many {alternatives}")  # pragma: no cover
                base = alternatives[0]
                # TODO: make X12UnionHelper.annotated(base); return X12UnionHelper(hint) instance
                # Instead, we quietly ignore the Union.
                return cls._make_helper(name, base)
            case GenericAlias() if get_origin(hint) == list:
                repeating, *aspects = get_args(hint)
                item_helper = X12ElementHelper.annotated(repeating)
                # TODO: Create A "list[X]" to_py that checks MaxItems (and MinItems)
                list_conversion: Conversion = cast(
                    Conversion,
                    lambda some_list: [item_helper.to_py(v) for v in some_list]
                )
                return X12ElementHelper(list_conversion, *aspects)
            case _AnnotatedAlias():  # type: ignore[misc]
                # Annotated. Create a helper
                helper = X12ElementHelper.annotated(hint)
                if helper is None:
                    # Something more elaborate than a primitive.
                    # usually Annotated[list[Annotated[base, etc.], etc.]
                    # base is list[Annotated]
                    base, *annotations = get_args(hint)
                    # TODO: Build AnnotatedListHelper.
                    return cls._make_helper(name, base)
                else:
                    return helper
            case type() if issubclass(hint, Composite):
                hint.make_helpers(get_type_hints(hint, include_extras=True))
                # TODO: Return an X12CompositeHelper() that does nothing.
                return None
            case type():
                # Primitive
                return X12ElementHelper.annotated(hint)
        raise ValueError(f"unexpected {name}: {hint} {type(hint)=} {get_origin(hint)=} in {cls}")  # pragma: no cover

    @classmethod
    def configure(cls, skip_validation : list[str]) -> None:
        """
        Provide the skip_validation configuration to the elements of this Segment.
        """
        fields = get_type_hints(cls, include_extras=True)
        cls.make_helpers(fields)
        all_rules = (
            rule.split(":")
            for rule in skip_validation
        )
        try:
            segment_rules = [
                (field_match, annotation_name)
                for class_match, field_match, annotation_name in all_rules
                if fnmatch.fnmatch(cls.__name__, class_match)
            ]
        except ValueError:  # pragma: no cover
            raise ValueError(f"invalid skip_validation rule in {skip_validation}")
        cls.logger.debug("Skip Validation: %s", segment_rules)

        cls._skip_validation = defaultdict(list)

        for field_match, annotation_name in segment_rules:
            # Does this match any names in the class?
            # print(f"configure {field_match=} {annotation_name=} in {cls.__name__}")
            for name, helper in cls._helpers.items():
                if fnmatch.fnmatch(name, field_match):
                    cls._skip_validation[name].append(annotation_name)

        # Propogate down to composites.
        for name, field_type in class_fields(cls):
            # TODO: PEEL THE ONION
            while type(field_type) is not type:
                match field_type:
                    case _AnnotatedAlias():  # type: ignore[misc]
                        # Annotated[f, ...]
                        field_type = get_args(field_type)[0]
                    case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                        # f | None
                        alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                        if len(alternatives) != 1:
                            raise NotImplementedError(
                                f"not supported {field_type}; too many {alternatives}")  # pragma: no cover
                        field_type = alternatives[0]
                    case GenericAlias() if get_origin(field_type) is list:
                        # List[f]
                        field_type = get_args(field_type)[0]
                    case _:  # pragma: no cover
                        raise ValueError(f"unexpected {name}: {field_type} {type(field_type)=} {get_origin(field_type)=} in {cls}")
            # print(f"configure {field_type}, {type(field_type)}")
            if issubclass(field_type, Composite):
                field_type.composite_configure(cls._skip_validation, segment_rules, name)

    def elements(self) -> SegmentText:
        """
        The segment as a list of Element source values.
        The segment text is the basis for the exchange format: a sequence of Segments.

        ..  note:: Confusing overlap of this elements() method with :py:class:`Source.elements` method.

            This is **not** the same concept at all.

        ..  todo:: Rename this to not conflict with semantics of `Source`.
        """
        values: SegmentText = []
        for name, hint in class_fields(self.__class__):
            field: Composite | list[Composite] = getattr(self, name)
            match field:
                case list():
                    values.append(cast(list[str | None], [v.elements() for v in field]))
                case Composite():
                    values.append(cast(list[str | None], field.elements()))
                case _:
                    # Annotated fields
                    self.logger.debug(f"{name}: {field} {self._helpers[name]} {getattr(self, name)=}")
                    values.append(getattr(self, name))
        return values

    def __repr__(self) -> str:
        good_names = (name for name, hint in class_fields(self.__class__))
        text = ", ".join(f"{name}={getattr(self, name)!r}" for name in good_names)
        return f"{self.__class__.__name__}({text})"


class Loop:
    """
    A Loop is a collection of ``Loop | Segment`` instances.

    Loops (and their Segments) can repeat, or may be optional.

    We need to examine the loop's structure of segments
    and sub-loops my matching segment prefixes to see
    which segment can be parsed.
    """
    logger = logging.getLogger("x12.base.Loop")  #: Class Logger

    def __init__(self, **arg_dict) -> None:
        """
        Create a Loop instance by providing keyword argument values
        for each segment or nested loop.

        The Segments and Composites will validate any values provided.
        """
        fields = get_type_hints(self.__class__)
        unknowns = arg_dict.keys() - fields.keys()
        if unknowns:
            raise TypeError(f"unknown fields: {unknowns}")  # pragma: no cover
        # Ideally all missing names are also not required.
        for name, hint in class_fields(self.__class__):
            setattr(self, name, arg_dict.get(name))

    @classmethod
    def configure(cls, skip_validation : list[str]) -> None:
        """
        Provide the skip_validation configuration to the Segments of this Loop.
        """
        for name, field_type in class_fields(cls):
            # TODO: PEEL THE ONION...
            while type(field_type) is not type:
                match field_type:
                    case GenericAlias() if get_origin(field_type) is list:
                        # list[X]
                        field_type = get_args(field_type)[0]
                    case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                        # Something | None OR list[Something] | None
                        alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                        field_type = alternatives[0]
                    case _AnnotatedAlias():  # type: ignore[misc]
                        field_type = get_args(field_type)[0]
                    case _:  # pragma: no cover
                        raise ValueError(f"unexpected {name}: {field_type} {type(field_type)=} {get_origin(field_type)=} in {cls}")
            if issubclass(field_type, Segment):
                field_type.configure(skip_validation)
            elif issubclass(field_type, Loop):
                field_type.configure(skip_validation)
            else:
                raise TypeError(f"unexpected {name}: {field_type} {type(field_type)}")  # pragma: no cover

    def segment_iter(self) -> Iterator[SegmentText]:
        """
        A flat sequence of segment values in this Loop and all sub Loops.
        This is the basis for the exchange format.
        """
        for name, hint in class_fields(self.__class__):
            field = getattr(self, name)
            self.logger.debug("segment_iter() name=%s field=%s", name, field)
            match field:
                case list():  # list[Something]
                    for instance in field:
                        if isinstance(instance, Loop):
                            yield from instance.segment_iter()
                        elif isinstance(instance, Segment):
                            name = cast(Segment, instance)._segment_name
                            yield cast(SegmentText, [name]) + instance.elements()
                        else:
                            raise TypeError(f"unexpected {name}: {hint} instance {instance=}")  # pragma: no cover
                case Loop(): # _ if isinstance(field, Loop):
                    # This doesn't seem to arise in practice.
                    yield from field.segment_iter()  # pragma: no cover
                case Segment(): # _ if isinstance(field, Segment):
                    name = cast(Segment, field)._segment_name
                    yield cast(SegmentText, [name]) + field.elements()
                case None:
                    # TypeAlias will have a value of None.
                    pass
                case _:  # pragma: no cover
                    raise TypeError(f"unexpected {name}: {field}")

    def __repr__(self) -> str:
        good_names = (n for n, h in class_fields(self.__class__))
        text = ", ".join(f"{name}={getattr(self, name)}" for name in good_names if hasattr(self, name))
        return f"{self.__class__.__name__}({text})"


class Message:
    """
    A top-level message, a collection of Loop instances.

    Loops can (and often do) repeat.
    """
    logger = logging.getLogger("x12.base.Message")  #: Class Logger

    def __init__(self, **arg_dict) -> None:
        """
        Create a Message instance by providing keyword argument values
        for each Loop.

        The Segments and Composites will validate any values provided.
        """
        fields = get_type_hints(self.__class__)
        unknowns = arg_dict.keys() - fields.keys()
        if unknowns:
            raise TypeError(f"unknown fields: {unknowns}")  # pragma: no cover
        # Ideally all missing names are also not required.
        for name, hint in class_fields(self.__class__):
            setattr(self, name, arg_dict.get(name))

    @classmethod
    def configure(cls, skip_validation : list[str]) -> None:
        """
        Provide the skip_validation configuration to the Segments of this Loop.
        """
        for name, loop_type in class_fields(cls):
            # TODO: PEEL THE ONION.
            while type(loop_type) is not type:
                match loop_type:
                    case GenericAlias() if get_origin(loop_type) is list:  # type: ignore[misc]
                        loop_type = get_args(loop_type)[0]
                    case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                        # Something | None OR list[Something] | None
                        alternatives = list(filter(lambda t: t is not NoneType, get_args(loop_type)))
                        loop_type = alternatives[0]
                    case _AnnotatedAlias():  # type: ignore[misc]
                        loop_type = get_args(loop_type)[0]
                    case _:  # pragma: no cover
                        raise TypeError(f"unexpected {name}: {loop_type} {type(loop_type)}")  # pragma: no cover
            if issubclass(loop_type, Loop):
                loop_type.configure(skip_validation)
            else:
                raise TypeError(f"unexpected {name}: {loop_type} {type(loop_type)}")  # pragma: no cover

    def segment_iter(self) -> Iterator[list[str | None | list[str | None]]]:
        """
        A flat sequence of segments in a Message.
        This is the basis for the exchange format.
        """
        for name, hint in class_fields(self.__class__):
            loop = getattr(self, name)
            match loop:
                case list():
                    for instance in loop:
                        yield from instance.segment_iter()
                case Loop():
                    yield from loop.segment_iter()
                case _:  # pragma: no cover
                    raise TypeError(f"unexpected {name}: {hint} {loop=}")

    def __repr__(self) -> str:
        good_names = (n for n, h in class_fields(self.__class__))
        text = ", ".join(f"{name}={getattr(self, name)}" for name in good_names)
        return f"{self.__class__.__name__}({text})"

    def __bool__(self):
        return any(getattr(self, name) for name, hint in class_fields(self.__class__))

    def json(self, indent: int | None = None) -> str:
        return json.dumps(asdict(self), indent=indent)

    def asdict(self) -> dict[str, Any]:
        return asdict(self)


class X12Parser:
    """
    Walks the structure of the annotated components in a given class.
    parses the Segment text blocks.

    This handles the various annotation cases supported by X12 messages:

    -   Optional[_T] == Union[_T, None].

    -   list[_T]

    -   Annotated[_T, ...]

    -   _T

    It also honors the nesting structure of messages, loops, segments, composites, and elements.

    """
    def __init__(self, message_class: type[Message], skip_validation : list[str] | None = None) -> None:
        self.cls = message_class
        self.cls.configure(skip_validation or [])
        self.logger = logging.getLogger(self.__class__.__name__)

    def parse(self, source: Source) -> Message:
        """
        Parses the Exchange format text for this Message subclass.

        Locates all Loops; each Loop will consume one or more Segments.
        """
        self.logger.debug("parse(%s, source)", self.cls.__name__)
        arg_dict = {}
        for name, loop_type in class_fields(self.cls):
            self.logger.debug("parse %s: %r %s", name, loop_type, type(loop_type))
            arg_dict[name] = self.msg_attr_build(self.cls, name, loop_type, source)
        return self.cls(**arg_dict)

    def msg_attr_build(self, cls: type[Message], name: str, loop_type: type, source: Source) -> Loop | list[Any] | None:
        """
        Walks type structure to create Message of Loop instances.

        May consume source Segments.

        Return type can be a tricky recursive structure; we use list[Any]
        """
        self.logger.debug("msg_attr_build cls=%s, %s: %s", cls, name, loop_type)
        match loop_type:
            case GenericAlias() if get_origin(loop_type) is list:
                # list[Loop] structure
                repeating_type = get_args(loop_type)[0]
                values: list[Loop | list[Any] | None] = []
                next_value = self.msg_attr_build(cls, name, repeating_type, source)
                while next_value:
                    values.append(next_value)
                    next_value = self.msg_attr_build(cls, name, repeating_type, source)
                return values
            case _AnnotatedAlias():  # type: ignore[misc]
                base_type = get_args(loop_type)[0]
                return self.msg_attr_build(cls, name, base_type, source)
            case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                # Something | None OR list[Something] | None
                alternatives = list(filter(lambda t: t is not NoneType, get_args(loop_type)))
                union_type = alternatives[0]
                return self.msg_attr_build(cls, name, union_type, source)
            case type() if issubclass(loop_type, Loop):
                # Stand-alone Loop without a list[Loop] framing...
                value = self.loop_parse(loop_type, source)
                return value
        raise TypeError(f"unexpected {name}: {loop_type} {type(loop_type)}")  # pragma: no cover

    def loop_parse(self, cls: type[Loop], source: Source) -> Union[Loop, None]:
        """
        Parses the Exchange format text for this Loop subclass.
        """
        self.logger.debug("loop_parse(%s) %s", cls.__name__, cls)
        arg_dict = {}
        for name, field_type in class_fields(cls):
            self.logger.debug("loop_parse %s: %r", name, field_type)
            loop_value = self.loop_attr_build(cls, name, field_type, source)
            # Implicitly treat a loop as "Situational": ignore it if it contains no Segments.
            if loop_value:
                arg_dict[name] = loop_value
        if arg_dict:
            return cls(**arg_dict)
        else:
            self.logger.debug("Skipping empty loop %s", cls)
            return None

    def loop_attr_build(self, cls: type[Loop], name: str, field_type: type, source: Source) -> Loop | Segment | list[Any] | None:
        """
        Walks type structure to create Loop of Loops and Segments.

        May consume source Segments.

        Return type is a tricky recursive structure; we use list[Any]
        """
        self.logger.debug("loop_attr_build %s: %r", name, field_type)
        match field_type:
            case GenericAlias() if get_origin(field_type) is list:
                # list[Something]
                repeating_type = get_args(field_type)[0]
                self.logger.debug("  list[%s] %s", repeating_type.__name__, repeating_type)
                values: list[Loop | Segment | list[Any] | None] = []
                next_value = self.loop_attr_build(cls, name, repeating_type, source)
                while next_value:
                    values.append(next_value)
                    # next_value = self.segment_parse(repeating_type, source)
                    next_value = self.loop_attr_build(cls, name, repeating_type, source)
                return values
            case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                # Something | None OR list[Something] | None
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                # OR. Try each alternative until one works.
                # For None supply a None instance.
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")  # pragma: no cover
                union_type = alternatives[0]
                return self.loop_attr_build(cls, name, union_type, source)
            case _AnnotatedAlias():  # type: ignore[misc]
                # Annotated[base, ...]
                base_type = get_args(field_type)[0]
                return self.loop_attr_build(cls, name, base_type, source)
            case type() if issubclass(field_type, Segment):
                seg_name = source.next_segment()
                if seg_name == "":
                    return None
                # TODO: segment with usage == "R"? Error
                # Else move on to next potential segment of Loop?
                return self.segment_parse(field_type, source)
            case type() if issubclass(field_type, Loop):  # pragma: no cover
                # raise RuntimeError("unexpected nested Loop: {field_type} inside {cls.__name__}")
                # An alternative is to try to parse it...
                return self.loop_parse(field_type, source)
        raise TypeError(f"unexpected {field_type} {type(field_type)}")  # pragma: no cover

    def segment_parse(self, cls: type[Segment], source: Source) -> Union[Segment, None]:
        """
        Parses the Exchange format text for this Segment subclass.

        Handles ISA segments specially to extract element and segment separators.
        If the ISA is uncompressed, then the separator characters for the :py:class`Source` can be deduced;
        this updates the state of the :py:class`Source`, and all subsequent segments can be compressed.
        If the ISA is compressed, then the separator characters must be provided before parsing can start.

        If the next segment in the :py:class:`Source` matches
        this segment's ``_segment_name`` attribute, then the segment
        will be consumed. Each element and composite will be validated.

        If the next segment does not match the ``_segment_name`` attribute,
        this segment's value will be ``None``.
        """
        fields = get_type_hints(cls, include_extras=True)
        self.logger.debug("segment_parse %s with %s", cls.__name__, fields)
        if source.next_segment().upper() != cls._segment_name.upper():
            return None

        # Special case: the ISA segment can update the ``Source`` parsing state.
        # Used in the case when ISA header not compressed.
        # If the ISA header is compressed, the separators must be provided "manually" to the :py:class:`Source` instance.
        if cls._segment_name.upper() == "ISA" and not source.element_sep:
            # Sum of field size + separator for each field.
            # + 3 for header "ISA"
            # + 1 for final segment separator
            args: list[tuple[X12Annotation]] = cast(list[tuple[X12Annotation]], [get_args(hint)[1:] for name, hint in class_fields(cls)])
            max_len_params: list[int] = [
                ann.params[0]
                for arg in args
                if arg
                    for ann in arg
                    if isinstance(ann, MaxLen)
            ]
            # print(f"Segment.parse() {max_len_params}")
            size = sum(p+1 for p in max_len_params) + 4
            self.logger.debug("ISA: source.element_sep=%r, source.segment_sep=%r", source.element_sep, source.segment_sep)
            self.logger.debug("ISA: size=%s", size)  # Should be 106 to include segment separator
            raw_text = source.peek(size)
            self.logger.debug("ISA: text=%r, separators text[-3:]=%r", raw_text, raw_text[-3:])
            # TODO: Rething this hack
            # ISA16 has the composite separator.
            # It's preceeded by an element separator and followed by the segment separator.
            source.element_sep = raw_text[-3]
            source.array_sep = raw_text[-2]
            source.segment_sep = raw_text[-1]

        # Note: Transition from parsing to building.
        # Extract all element values and build the segment.
        flat_values = cast(list[str | None | list[str | None]], source.elements())[1:]  # Drops the segment name from the values.
        self.logger.debug("segment_parse %s: fields %s values %r", cls.__name__, fields, flat_values)
        arg_dict: dict[str, Any] = {
            name: self.segment_attr_build(field_type, name, field_type, flat_values)
            for name, field_type in class_fields(cls)
        }
        obj = cls(**arg_dict)
        return obj

    def segment_attr_build(self, cls: type[Segment], name: str, field_type: type[Segment], source_values: list[str | None | list[str | None]]) -> Any | list[Any] | Composite | None:
        """
        Walks type structure to create Elements and Composites. The Element's are ``Any`` type.

        May pop source_values as part of building the instance.
        """
        self.logger.debug("segment_attr_build %s: %s from %r", name, field_type, source_values)
        match field_type:
            case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                alternatives = list(filter(lambda t: t is not NoneType, get_args(field_type)))
                if len(alternatives) != 1:
                    raise NotImplementedError(f"not supported {field_type}; too many {alternatives}")  # pragma: no cover
                if source_values:
                    return self.segment_attr_build(cls, name, alternatives[0], source_values)
                return self.segment_attr_build(cls, name, alternatives[0], [None])
            case _AnnotatedAlias():  # type: ignore[misc]
                # Consume a single value from the elements of this segment.
                # Either a ``Composite`` or list or some primitive type
                base = get_args(field_type)[0]
                value = self.segment_attr_build(cls, name, base, source_values)
                return value
            case GenericAlias() if get_origin(field_type) is list: # list[Something]
                # COMPOSITE-LIKE PROCESSING for elements that are list[Element]
                repeating_type = get_args(field_type)[0]
                self.logger.debug("  list[%s]", repeating_type.__name__)
                source_array = cast(list[str], source_values.pop(0))
                values = [self.segment_attr_build(cls, name, repeating_type, [item]) for item in source_array]
                return values
            case type() if issubclass(field_type, Composite):
                # Next value in this segment *should* be a list.
                # If it didn't have the component separator, we make single-element list.
                composite_value: list[str | None]
                if source_values:
                    composite_value = cast(list[str | None], source_values.pop(0))
                else:
                    composite_value = []
                # print(f"Segment.attr_build() {field_type} with {composite_value}")
                value = self.composite_build(field_type, composite_value)
                return value
            case type():
                # Atomic elements.
                if source_values:
                    raw_value = cast(str, source_values.pop(0))
                    return raw_value
                return None
        raise TypeError(f"unexpected type {field_type} {type(field_type)} in {cls}")  # pragma: no cover

    def composite_build(self, cls: type[Composite], source_value: str | None | list[str | None]) -> Composite:
        """
        Builds an instance of this Composite using a
        collection of source values extracted from parent Segment's Exchange format text.

        :param cls: the ``Composite`` subclass to build.
        :param source_value: the source values to use.
        :returns: an instance of this ``Composite`` subclass.
        """
        fields = get_type_hints(cls, include_extras=True)
        self.logger.debug("composite_build %s with %s", cls.__name__, fields)
        # Expand single value to a list
        if not isinstance(source_value, list):
            source_value = [source_value]

        # Pad with None instances?
        num_fields = sum(1 for name in class_fields(cls))
        if num_fields < len(source_value):
            # Too many values for the fields of this composite.
            raise ValueError(
                f"wrong number of values {cls.__name__} needs {num_fields} provided {len(source_value)}"
            )  # pragma: no cover
        elif num_fields > len(source_value):
            source_value.extend([None] * (num_fields - len(source_value)))
        else:
            # assert num_fields == len(source_value)
            pass
        # Build the object
        arg_dict = {
            name: self.composite_attr_build(cls, name, field_type, source_value.pop(0))
            for name, field_type in class_fields(cls)
        }
        return cls(**arg_dict)

    def composite_attr_build(self, cls: type[Composite], name: str, field_type: type, source_value: str | None) -> Any:
        """
        Populate Element's field value from a text value.
        """
        match field_type:
            case _AnnotatedAlias():  # type: ignore[misc]
                # Annotated[X, ...]
                return source_value
            case UnionType() | _UnionGenericAlias():  # type: ignore[misc]
                # Usually, X | None
                return source_value
            case type():
                return source_value
        raise TypeError(f"unexpected type {field_type}")  # pragma: no cover

def demo() -> None:
    """
    A minimal demonstration of some features of the base classes.

    ::

        >>> from x12.base import demo
        >>> demo()
        MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01='00', isa16=':'))])
        MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01='00', isa16=':'))])
    """

    ID: TypeAlias = str
    AN: TypeAlias = str

    class ISA_LOOP_ISA(Segment):
        _segment_name = "ISA"
        isa01: Annotated[ID, Title('I01'), MinLen(2), MaxLen(2)]
        isa16: Annotated[AN, Title('I16'), MinLen(1), MaxLen(1)]

    class ISA_LOOP(Loop):
        isa: ISA_LOOP_ISA

    class MSG(Message):
        """Demonstration Message"""
        isa_loop: list[ISA_LOOP]

    text = "ISA|00|:~"
    logger.info("Building from %r", text)
    source = Source(text, element_sep="|", segment_sep="~")
    parser = X12Parser(MSG)
    parsed_m = parser.parse(source)
    print(parsed_m)

    built_m = MSG(
        isa_loop=[
            ISA_LOOP(
                isa=ISA_LOOP_ISA(
                    isa01='00',
                    # etc.
                    isa16=':',
                )
            )
        ]
    )
    print(built_m)


if __name__ == "__main__":  # pragma: no cover
    logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
    demo()
    logging.shutdown()
