..  _`design.annotations`:

#############################
Element Types and Annotations
#############################

We have the following considerations:

-   Providing a complete JSON Schema definition for a Message (including the Loop, Segment, Composite classes) and the atomic Elements.

-   Using the Annotation information to convert between serialized text and native Python values.

-   A ``tools/xml_extract.py`` application that creates the message definitions.

We'll start by looking at the schema.

Essential Schema Details
========================

The XML source files have the definition of the schema.
The XML files appear to be derived from the
source .SEF files (which we don't have.)

The schema details in the XML source files describe the following structures:

:Text values without further specifications:
    ``'data_type_code': 'AN'`` or ``'data_type_code': 'ID'``.

    The ``str`` type needs length information in addition to the base type.
    This should become ``Annotated[str, MinLen(x), MaxLen(y)]``.

    The annotation becomes JSONSchema ``{"type": "string", "minLength": x, "maxLength": y}``

:Text values with a list of permitted values:
    ``'data_type_code': 'AN'`` or ``'data_type_code': 'ID'``.

    The ``Literal["value", ...]`` type could be used for this; it has the advantage of being supported directly by **mypy**.
    An alternative is ``Annotated[str, MinLen(2), MaxLen(2), Enumerated("value", "value")]``;
    while somewhat more internally consistent, it bypasses **mypy**.

    The annotation becomes JSONSchema ``{"type": "string", "minLength": x, "maxLength": y, "enum": [values, ...]}``

:Text values with a format specification:
    ``'data_type_code': 'DT'`` or ``'data_type_code': 'TM'``.

    The Python ``str`` type needs format information in addition to the base type.
    This could be ``Annotated[str, MinLen(4), MaxLen(4), Format(r'\d\d\d\d')]``.
    The conversion to ``datetime.date`` or ``datetime.time``, however, omitted when using a ``str``\ -focused type annotation.

    This should be ``Annotated[datetime.time, Format('%H%M')]`` or ``typing.Annotated[datetime.date, Format('%Y%m%d')]``.
    In the exotic cases of permitting either 6- or 8-position dates, ``typing.Annotated[datetime.date, Format('%Y%m%d'), Format('%y%m%d')]`` might be workable.

    Preserving the length information (to be consistent with other annotations)
    is redundant, but possibly helpful. Consider ``Annotated[datetime.time, MinLen(4), MaxLen(4), Format('%H%M')]``.

    The annotation becomes JSONSchema ``{"type": "string", "minLength": x, "maxLength": y, "format": "\d\d\d\d", "conversion": "date"}``.
    An extension attribute, "conversion", is required to clarify the need for a conversion when serializing or deserializing.

:Real number values:
    ``'data_type_code': 'R'``.

    The ``float`` type with additional sizing information to describe the source text.
    This is ``Annotated[float, MinLen(4), MaxLen(4)]``.

    The annotation becomes JSONSchema ``{"type": "number", "minLength": x, "maxLength": y, "format": "\d\d\d\d", "conversion": "date"}``.

:Integer number values:
    ``'data_type_code': 'N'``.

    The ``int`` type with additional sizing information to describe the source text.
    This is ``Annotated[int, MinLen(4), MaxLen(4)]``.

    The annotation becomes JSONSchema ``{"type": "integer", "minLength": x, "maxLength": y, "format": "\d\d\d\d", "conversion": "date"}``.
    This uses the common extension of "integer" instead of "number".

:Decimal number values:
    Any of the various ``'data_type_code': 'Nx'`` options.

    The ``Decimal`` type with additional sizing information to describe the source text.
    Note that decimal points are *not* part of the source representation, and the `scaleb()` method
    must be used.
    A type of ``'data_type_code': 'N2'``, for example, this is ``typing.Annotated[decimal.Decimal, MinLen(4), MaxLen(4), Scale(2)]``.

    The annotation becomes JSONSchema ``{"type": "str", "minLength": x, "maxLength": y, "format": "\d\d\d\d", "conversion": "decimal", "scale": 2}``.
    An extension attributes, "conversion" and "scale", are required to clarify the need for a conversion when serializing or deserializing.

Using annotations almost eliminates the need for a separate class definition for each individual element.
The nuanced details of the title for an element introduces a tiny complication.
Adding ``Title("Number of Included Functional Groups")`` as part of the annotations provides a way
to include this information in a JSON Schema document.

This permits the foundational type definitions to become first-class ``TypeAlias`` definitions.
These can be properly re-used in segment definitions.

There two kinds of repeating or composite objects:

:list[X]:
    These have a repeat count or a Usage of "R".
    These are ``Annotated[list[Annotated[t, etc.], MaxItems(n)]``
    The repeating type is, itself, an annotated type.

    To keep the syntax readable, it's slightly nicer to
    decompose this into two parts::

        ItemType: TypeAlias = Annotated[t, etc.]
        item: Annotatedp[list[ItemType], MaxItems(n)]

:Union[Annotated[t, etc.], None]:
    These are optional items with a Usage or "S" (Situational.)
    This is not (currently) validated.

These two constructs define a hierarchy of validation.
A list, for example, must have each element validated,
then the list -- as a whole -- can be validated.

Data Validation
===============

The source data can be validated by these detailed annotations.

There are two tiers to validation:

-   **Structural**. The :py:meth:`parse` methods all gather source text and apply the overall
    Message, Loop, Segment, or Composite class to build an instance.
    The structural type hints of ``x : SomeClass``, ``y: list[SomeClass]``,
    are exploited to understand the structure of message and loop.

-   **Elemental**. For Composites and Elements, a :py:meth:`build` method is used to construct
    these foundational objects. At this level,
    ``x: SomeTypeAlias`` becomes important for converting the text source
    into a Python object.

The ``Segment`` parsing is -- consequently -- the most complicated because it's a
mix of structural and elemental. Overall, the segment is structural: it's a sequence of individual elements or composites.
However, each element has elemental validation and conversion rules.

The :py:meth:`__init__` methods for ``Segment`` and ``Composite`` contain
the elemental validation. Each element value is touched by methods of
an ``X12ElementHelper`` object. The :py:meth`to_py` method does this conversion.

The ``X12ElementHelper`` has both the :py:meth:`to_py` and :py:meth:`to_str` methods
for each of the primitive types and structures.

In principle, the validators simply stack on top
of each other. The entire message parsing is nothing
more than a stack of validators ``Message(Loop(ListOf(Segment(source))))``.

Because of optional and repeated segments, this is (superficially) tricky
to write as a functional composition that parses a message.
See https://github.com/dabeaz/blog/blob/main/2023/three-problems.md and this https://www.cs.nott.ac.uk/~pszgmh/monparsing.pdf.

The approach is to have each validator return a Monad
with a partial construct and a revised input stream,
or a "Nothing" that indicates the construct cannot be parsed
and something else needs to be tried. If a construct
can be parsed, the tokens are consumed. If a construct cannot
be parsed, the return value is the original sequence of tokens.

This (in turn) requires sequence and conditional construct parsers.
These apply parser functions until the input is consumed.

This is **not** the approach we've chosen. Instead, we have
use the class-level :py:meth:`parse()` and :py:meth:`build()` function that
either returns an instance of the class or None.

For Message, Loop, Segment
the :py:meth:`parse()` method consumes zero or more complete segments
from the input.
For Composite and Element parsing within a segment,
a :py:meth:`build()` method consumes fields from the segment to
build Elements or Composites.

..  important::

    This means the validation is at the element level.

The Segment and Composite implement ``list[X]`` and ``Union[X, None]`` validations
separately from the ``X12ElementHelper`` class.

A class-level :py:meth:`annotated` method builds
type validations for ``Annotated[X, ...]`` constructs.

There are two special cases:

-   An ``Annotated[list[Annotated[X, etc.], MaxItems()]`` gets
    a subclass of :py:class:`X12ElementHelper` to validate lists assuming the primitives
    have already been validated.

-   Similarly, an ``Union[Annotated[X, etc.], None]`` is tricky.
    Most annotations reject invalid values, but this expands the domain of valid values,
    removing a rejection rule.
    The presence of this annotation implies an inverse ``NotAUnion[Annotated[X, etc.]]`` that will
    reject fields with a ``None``.

Additional Schema Details
=========================

It's not perfectly clear where supplemental data like the ``Segment`` identifier string and the "position" information
should be carried. Should this be part of the docstring? Or should it be a separate attribute-like feature
of the class? Or should it be an internal class stripped down to these two features?

Here's the desired segment definition.

::

    # In the common module
    N0: TypeAlias = Annotated[Decimal, Scale(0)]
    I16: TypeAlias = Annotated[N0, MinLen(1), MaxLen(5)]
    I12: TypeAlias = Annotated[N0, MinLen(9), MaxLen(9)]

    # In the message module
    class ISA_LOOP_IEA(Segment):
        """
        Interchange Control Trailer
        """
        _segment_name = "IEA"
        _segment_position = 30

        iea01: Annotated[I16, Title("Number of Included Functional Groups")]
        iea02: Annotated[I12, Title("Interchange Control Number")]

This form (with reuse) can preserve the source document definitions
while relying on Annotations to carry element definitions.
