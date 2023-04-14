..  _`design.element`:

####################
Element Class Design
####################

Currently, the :mod:`x12.base.Element` class defines individual, atomic elements.
Is this necessary? Or can we approach it without the added overhead of these classes?

We have two considerations:

-   Providing a complete JSON Schema definition for an Element of a Message.

-   Converting between serialized text and native Python values.

The schema details include the following:

-   Text without further specifications; ``'data_type_code': 'AN'`` or ``'data_type_code': 'ID'``.
    The ``str`` type needs length information in addition to the base type.
    This is ``typing.Annotated[str, MinLen(x), MaxLen(y)]``.

-   Text with a list of values.
    The ``Literal["value", ...]`` type could be used, or ``typing.Annotated[str, MinLen(2), MaxLen(2), Allowed("value", "value")]``.

-   Text with a format specification; ``'data_type_code': 'DT'`` and ``'data_type_code': 'TM'``.
    The ``str`` type needs format information in addition to the base type.
    This could be ``typing.Annotated[str, MinLen(4), MaxLen(4), Format(r'\d\d\d\d')]``.
    The conversion to ``datetime.date`` or ``datetime.time``, however, is implied, not stated by a ``str``\ -focused type annotation.
    This should be ``typing.Annotated[datetime.time, Format('%H%M')]`` or ``typing.Annotated[datetime.date, Format('%Y%m%d')]``.
    In the exotic cases of 6- or 8-position dates, ``typing.Annotated[datetime.date, Format('%Y%m%d'), Format('%y%m%d')]`` might be workable.

-   "Real" numbers; ``'data_type_code': 'R'``.
    The ``float`` type with additional sizing information.
    This is ``typing.Annotated[float, MinLen(4), MaxLen(4)]``.

-   Numbers; ``'data_type_code': 'N'``.
    The ``int`` type with additional sizing information.
    This is ``typing.Annotated[int, MinLen(4), MaxLen(4)]``.

-   Decimal numbers; any of the various ``'data_type_code': 'Nx'`` options.
    The ``Decimal`` type with additional sizing information.
    For ``'data_type_code': 'N2'``, this is ``typing.Annotated[decimal.Decimal, MinLen(4), MaxLen(4), Scale(2)]``.

The above annotation design supports conversion to JSON Schema. This eliminates the need for a ``Schema`` internal class definition.

Using annotations almost eliminates the need for a separate class definition for each element.
The nuanced details of a title introduces a tiny complication that's not trivially available.
A ``Title("Number of Included Functional Groups")`` as part of the annotations provides a way
to include this information in a JSON Schema document.

To an extent, common type definitions can become first-class ``TypeAlias`` definitions that can be re-used in segment definitions.
These can lead to complex annotations.

Further, the source data can be validated by these detailed annotations.

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
