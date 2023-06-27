..  _`design.type_hints`:

##########################
Type Hints and JSON Schema
##########################

The essential message/loop/segment/composite structure is defined with type hints.
This, however, doesn't capture all the details of the source
XML (and presumably the source SEF on which the XML is based.)

We'll explore the type hints with a series of examples.

-   `Messages`_. These are collections of Loops.

-   `Loops`_. These are collections of Segments and Sub-Loops.

-   `Segments`_. These are collections of Elements and Composites.

-   `Composites`_. These are collections of Elements.

-   `Elements`_. These are atomic, and can be treated as Python objects.

The objective is to provide a pure-Python definition of the X12 EDI structure.
This can make it easier to examine and analyze messages.
It can also make it somewhat easier to define alternative syntax for messages
to further facilitate analysis and processing.

..   note:: The JSON Schema is a work in progress

..  important:: The IG compliance is indirect

    These definitions are based on the PyX12 project.
    TigerShark may have introduced bugs or complications.

Messages
=========

Here's an example of a Message definition.

::


    class MSG270(Message):
        """HIPAA Health Care Eligibility Inquiry X092A1-270"""
        ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
        isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]

The message contains a type alias and single attribute.

:ItemIsa_Loop:
    A TypeAlias used to provide the essential item definition for a repeating list of items.
    This provides the details for each item in a list.

:isa_loop:
    A list of ``ItemIsa_Loop`` instances.
    A parsed message will always have an ``isa_loop`` attribute, and it will be a list.
    The annotations describe the list as a whole.

An application will use ``msg.isa_loop[0]`` to refer to the first ISA loop of a given message.

The type alias provides a number of XML (and presumably SEF) attribute details.
These are annotations used to validate input values.

Loops
=========

A Loop a collection of segments (and sub-loops). It is also a namespace to distinguish reused references
to a common segment definition. See :ref:`design.loop_namespace`.

The loop-as-namespace is implemented by using the loop name as a qualifier for segments that are part of the loop.

Here's an example of a Loop definition.

::


    class ISA_LOOP(Loop):

        isa: Annotated[ISA_LOOP_ISA, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
        ItemGs_Loop: TypeAlias = Annotated[GS_LOOP, Title('Functional Group Header'), Usage('R'), Position(20), Required(True)]
        gs_loop: Annotated[list[ItemGs_Loop], MinItems(1)]

        ta1: Annotated[ISA_LOOP_TA1, Title('Interchange Acknowledgement'), Usage('S'), Position(20), Required(True)]

        iea: Annotated[ISA_LOOP_IEA, Title('Interchange Control Trailer'), Usage('R'), Position(30), Required(True)]


This Loop has four attributes:

:isa:
    An instance of the ISA_LOOP's ``ISA`` segment.

:gs_loop:
    A sequence of ``ItemGs_Loop`` instances. A separate ``TypeAlias`` provides the definition for each item in the collection.

:ta1:
    An optional instance of the  ISA_LOOP's ``TA1`` segment.

:iea:
    An instance of the ISA_LOOP's ``IEA`` segment.

Segments
=========

Here's an example of a Segment definition.

::

    class ISA_LOOP_IEA(Segment):
        """Interchange Control Trailer"""
        _segment_name = 'IEA'

        iea01: Annotated[I16, Title('Number of Included Functional Groups'), Usage('R'), Position(1)]

        iea02: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(2)]


This Segment has two attributes related to message content,
and a "hidden" attribute used for message loading.

:_segment_name:
    The literal ``'IEA'`` to identify this segment when parsing.
    This is not considered part of the value of the segment
    and is not part of the dictionary or JSON representation.

:iea01:
    An instance of the ISA_LOOP's ``IEA01`` element.
    The common definitions provide the needed ``I16`` base type.

:iea02:
    An instance of the ISA_LOOP's ``IEA02`` element
    The common definitions provide the needed ``I12`` base type.

The annotations here build in the common definitions of two reusable type definitions, ``I16`` and ``I12``.
We'll look at these next.

Elements
=========

Here are somes examples of an common elements defined via ``TypeAlias``.

::

    I12: TypeAlias = Annotated[N0, MinLen(9), MaxLen(9)]
    I13: TypeAlias = Annotated[ID, MinLen(1), MaxLen(1)]
    I14: TypeAlias = Annotated[ID, MinLen(1), MaxLen(1)]
    I15: TypeAlias = Annotated[AN, MinLen(1), MaxLen(1)]
    I16: TypeAlias = Annotated[N0, MinLen(1), MaxLen(5)]

These depend on other foundational X12 data types like ``N0``, ``ID``, and ``AN``.

::

    AN: TypeAlias = str
    ID: TypeAlias = str
    N0: TypeAlias = Annotated[Decimal, Scale(0)]

This stack of type aliases seems to parallel the XML (and .SEF)
definitions.

Composites
==========

Here's the definition of a Composite.

::

    class L2110D_C003(Composite):
        """Composite Medical Procedure Identifier"""

        eq02_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ'])]

        eq02_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]

        eq02_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]

        eq02_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]

        eq02_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]

        eq02_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]

        eq02_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]



This defines six attributes; the first two are required.
Four, with ``Usage('S')`` are "situational", one (with ``Usage('N')``) is not used.

The name, ``L2110D_C003``, uses the loop ``2210D`` as a namespace for composite ``C003``.
