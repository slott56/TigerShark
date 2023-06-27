..  _`design.class`:

################################
Message Schema as Class
################################

A message definition has the following structure:

::

    from .base import *
    from .common import *


    class ISA_LOOP_ISA(Segment):
        """Interchange Control Header"""
        _segment_name = 'ISA'

        isa01: Annotated[I01, Title('Authorization Information Qualifier'), Usage('R'), Position(1), Enumerated(*['00', '03'])]

        isa02: Annotated[I02, Title('Authorization Information'), Usage('R'), Position(2)]

        isa03: Annotated[I03, Title('Security Information Qualifier'), Usage('R'), Position(3), Enumerated(*['00', '01'])]

        isa04: Annotated[I04, Title('Security Information'), Usage('R'), Position(4)]

        isa05: Annotated[I05, Title('Interchange ID Qualifier'), Usage('R'), Position(5), Enumerated(*['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ'])]

        isa06: Annotated[I06, Title('Interchange Sender ID'), Usage('R'), Position(6)]

        isa07: Annotated[I05, Title('Interchange ID Qualifier'), Usage('R'), Position(7), Enumerated(*['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ'])]

        isa08: Annotated[I07, Title('Interchange Receiver ID'), Usage('R'), Position(8)]

        isa09: Annotated[I08, Title('Interchange Date'), Usage('R'), Position(9)]

        isa10: Annotated[I09, Title('Interchange Time'), Usage('R'), Position(10)]

        isa11: Annotated[I10, Title('Interchange Control Standards Identifier'), Usage('R'), Position(11), Enumerated(*['U'])]

        isa12: Annotated[I11, Title('Interchange Control Version Number'), Usage('R'), Position(12), Enumerated(*['00401'])]

        isa13: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(13)]

        isa14: Annotated[I13, Title('Acknowledgment Requested'), Usage('R'), Position(14), Enumerated(*['0', '1'])]

        isa15: Annotated[I14, Title('Usage Indicator'), Usage('R'), Position(15), Enumerated(*['P', 'T'])]

        isa16: Annotated[I15, Title('Component Element Separator'), Usage('R'), Position(16)]


    # Additional loops, segments, and composites omitted.


    class ISA_LOOP(Loop):
        isa: Annotated[ISA_LOOP_ISA, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]

        ItemGs_Loop: TypeAlias = Annotated[GS_LOOP, Title('Functional Group Header'), Usage('R'), Position(20), Required(True)]
        gs_loop: Annotated[list[ItemGs_Loop], MinItems(1)]

        ta1: Annotated[ISA_LOOP_TA1, Title('Interchange Acknowledgement'), Usage('S'), Position(20), Required(True)]

        iea: Annotated[ISA_LOOP_IEA, Title('Interchange Control Trailer'), Usage('R'), Position(30), Required(True)]


    class MSG270(Message):
        """HIPAA Health Care Eligibility Inquiry X092A1-270"""
        ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
        isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]

The content of each level of the Message/Loop/Segment/Composite/Element structure is
defined through type annotations.

The :mod:`x12.base` module provides class definitions on which the other defintions depend.

The  :mod:`x12.common` module has type aliases taken from the X12 definitions. It includes the following:

::

    ID: TypeAlias = str
    # The other foundational definitions like AN, DT, TM, R, N, etc.

    I01: TypeAlias = Annotated[ID, MinLen(2), MaxLen(2)]
    # Many, many others, built on the foundational definitions

The built-in :mod:`inspect` module provides a handy :func:`get_annotations`
function that examines the attributes of the class
to locate the annotations for the component loops, composites, segments, and elements.

The :mod:`typing` module include :func:`get_type_hints()` which is more
useful becuase it works on a class as a whole.

Note that a ``Segment`` description can be reused in multiple ``Loop`` definitions.
For more on this, see :ref:`design.loop_namespace`.

For the atomic ``Element`` definition, a full class seems to be a bit much. Each element is a primitive Python object.
The types are ``Annotated[Foundation_, ...]`` definitions to extend the foundation with additional constraints.
