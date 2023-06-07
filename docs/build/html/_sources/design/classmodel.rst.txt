..  _`design.class`:

################################
Class Model
################################

The objective is to have a definition somewhat like the following:

::

    from .base import *
    from . import common

    class ISA_LOOP_ISA(Segment):
        """Interchange Control Header"""
        _segment_name = "ISA"
        isa01: common.I01
        isa02: common.I02
        isa03: common.I03
        isa04: common.I04
        isa05: common.I05
        isa06: common.I06
        isa07: common.I07
        isa08: common.I08
        isa09: common.I09
        isa10: common.I10
        isa11: common.I11
        isa12: common.I12
        isa13: common.I13
        isa14: common.I14
        isa15: common.I15
        isa16: common.I16

    class ISA_LOOP(Loop):
        """Interchange Control Header"""
        isa_loop_isa: ISA_LOOP_ISA
        gs_loop: list[GS_LOOP]
        isa_loop_ta1: ISA_LOOP_TA1
        isa_loop_iea: ISA_LOOP_IEA

    class MSG270(Message):
        """HIPAA Health Care Eligibility Inquiry X092A1-270"""
        isa_loop: list[ISA_LOOP]

The content of each level of the Message/Loop/Segment/Composite/Element structure is
defined through type annotations.

The :mod:`x12.base` module provides class definitions on which the other defintions depend.

The  :mod:`x12.common` module has type aliases. It would include the following:

::

    I01: TypeAlias = Annotated[str, Title("I01"), MinLen(2), MaxLen(2)]

The built-in :mod:`inspect` module provides a handy :func:`get_annotations`
function that examines the attributes of the class
to locate the annotations for the component loops, composites, segments, and elements.

The :mod:`typing` module include :func:`get_type_hints()` which is more
useful becuase it works on a class as a whole.

Note that a ``Segment`` description can be reused in multiple ``Loop`` definitions.
For more on this, see :ref:`design.loop_namespace`.

For the ``Element`` definition, a class seems to be a bit much, since each element is a primitive Python object.
See :ref:`design.element`.
