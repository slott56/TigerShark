..  _`design.annotations`:

#############################
Element Types and Annotations
#############################

Currently, the :mod:`x12.base.Element` class defines individual, atomic elements.
Is this necessary? Or can we approach it without the added overhead of these classes?
Can we replace them with type annotations and focus on the
collections (i.e. Composites and Segments)?

We have the following considerations:

-   Providing a complete JSON Schema definition for an Element of a Message.

-   Using the Annotation information to convert between serialized text and native Python values.

-   Updating ``tools/xml_extract.py`` application.

Essential Schema Details
========================

The XML source files have the definitionof the schema.
These appear to be derived from the
source .SEF files, which we don't have.

The schema details in the XML source files include the following:

:Text without further specifications:
    ``'data_type_code': 'AN'`` or ``'data_type_code': 'ID'``.

    The ``str`` type needs length information in addition to the base type.
    This should become ``typing.Annotated[str, MinLen(x), MaxLen(y)]``.

    The annotation becomes JSONSchema ``{"type": "string", "minLength": x, "maxLength": y}``

:Text with a list of values:
    ``'data_type_code': 'AN'`` or ``'data_type_code': 'ID'``.

    The ``Literal["value", ...]`` type could be used for this; it has the advantage of being supported directly by **mypy**.
    An alternative is ``typing.Annotated[str, MinLen(2), MaxLen(2), Enumerated("value", "value")]``;
    while somewhat more internally consistent, it bypasses **mypy**.

    The annotation becomes JSONSchema ``{"type": "string", "minLength": x, "maxLength": y, "enum": [values, ...]}``

:Text with a format specification:
    ``'data_type_code': 'DT'`` or ``'data_type_code': 'TM'``.

    The Python ``str`` type needs format information in addition to the base type.
    This could be ``typing.Annotated[str, MinLen(4), MaxLen(4), Format(r'\d\d\d\d')]``.
    The conversion to ``datetime.date`` or ``datetime.time``, however, omitted when using a ``str``\ -focused type annotation.

    This should be ``typing.Annotated[datetime.time, Format('%H%M')]`` or ``typing.Annotated[datetime.date, Format('%Y%m%d')]``.
    In the exotic cases of permitting either 6- or 8-position dates, ``typing.Annotated[datetime.date, Format('%Y%m%d'), Format('%y%m%d')]`` might be workable.

    Preserving the length information (to be consistent with other annotations)
    is redundant, but possibly helpful. Consider ``typing.Annotated[datetime.time, MinLen(4), MaxLen(4), Format('%H%M')]``.

    The annotation becomes JSONSchema ``{"type": "string", "minLength": x, "maxLength": y, "format": "\d\d\d\d", "conversion": "date"}``.
    An extension attribute, "conversion", is required to clarify the need for a conversion when serializing or deserializing.

:"Real" numbers:
    ``'data_type_code': 'R'``.

    The ``float`` type with additional sizing information to describe the source text.
    This is ``typing.Annotated[float, MinLen(4), MaxLen(4)]``.

    The annotation becomes JSONSchema ``{"type": "number", "minLength": x, "maxLength": y, "format": "\d\d\d\d", "conversion": "date"}``.

:Numbers:
    ``'data_type_code': 'N'``.

    The ``int`` type with additional sizing information to describe the source text.
    This is ``typing.Annotated[int, MinLen(4), MaxLen(4)]``.

    The annotation becomes JSONSchema ``{"type": "integer", "minLength": x, "maxLength": y, "format": "\d\d\d\d", "conversion": "date"}``.
    This uses the common extension of "integer" instead of "number".

:Decimal numbers:
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

This permits type definitions to become first-class ``TypeAlias`` definitions.
These can be properly re-used in segment definitions.

Data Validation
===============

The source data can be validated by these detailed annotations.

There are two tiers to validation:

-   **Structural**. The ``parse()`` methods all gather source text and apply the overall
    Message, Loop, or Segment class to build an instance.
    The structural type hints of ``x : SomeClass``, ``y: list[SomeClass]``,
    are exploited to understand the structure of message and loop.

-   **Elemental**. For Composites and Elements, the ``build()`` method is used to construct
    these foundational objects. At this level,
    ``x: SomeTypeAlias`` becomes important for converting the text source
    into a Python object.

The Segment parsing is -- of course -- the most complicated because it's a
mix of structural and elemental. Overall, the segment is structural: it's a sequence of individual elements or composites.
However, each element has elemental validation and conversion rules.

..  important:: Source Text and Python Objects

    The ``Element`` class currenly keeps both source text and converted value.

    This is handy for tracking down a parsing problem.
    It permits displaying a Segment that has an invalid element to provide debugging context.

    Eliminating the ``Element`` objects *also* means tracking the parsing
    state to provide ample context for invalid data.

The ``parse()`` methods have a ``match`` statement for the various
type hints. Currently, there are ``case _ if issubclass(field_type, Element):``
and ``case _ if issubclass(field_type, Composite):`` clauses that must be replaced
with ``case _AnnotatedAlias() as p:`` to examine the annotations in detail.

It seems easiest to have a generic ``convert(annotation: _AnnotatedAlias, source: str) -> Any``
function. However, the first parameter of an annotation is a base type,
permitting a ``match get_args(p)[0]:`` statement to use type-specific
converters: ``str_convert(annotation: _AnnotatedAlias, source: str) -> str``, etc,
for the supported ``str``, ``int``, ``float``, ``datetime.date``, ``datetime.time``, ``Decimal`` types.

Additional Schema Details
=========================

It's not perfectly clear where supplemental data like the Segment identifier string and the "position" information
should be carried. Should this be part of the docstring? Or should it be a separate attribute-like feature
of the class? Or should it be an internal class stripped down to these two features?

Here's a potential segment definition with no reuse of type information.

::

    class ISA_LOOP_IEA(Segment):
        """
        Interchange Control Trailer
        """
        class Schema:
            segment_name = "IEA"
            position = 30

        iea01: Annotated[Decimal, MinLen(1), MaxLen(5), Scale(0), Title("Number of Included Functional Groups")]
        iea02: Annotated[Decimal, MinLen(9), MaxLen(9), Scale(0), Title("Interchange Control Number")]

Here's a potential segment definition with reuse.

::

    N0: TypeAlias = Annotated[Decimal, Scale(0)]
    I16: TypeAlias = Annotated[N0, MinLen(1), MaxLen(5)]
    I12: TypeAlias = Annotated[N0, MinLen(9), MaxLen(9)]

    class ISA_LOOP_IEA(Segment):
        """
        Interchange Control Trailer
        """
        class Schema:
            segment_name = "IEA"
            position = 30

        iea01: Annotated[I16, Title("Number of Included Functional Groups")]
        iea02: Annotated[I12, Title("Interchange Control Number")]

This form (with reuse) may better preserve the source document definitions.
This may make changes somewhat simpler because definitions are not repeated.
