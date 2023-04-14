..  _`design.class`:

################################
Class Model
################################

The objective is to have a definition somewhat like the following:

::

    from .base import *
    from . import common

    class ISA01(Element):
        """Authorization Information Qualifier"""
        class Schema:
            datatype = common.I01

    class ISA_LOOP_ISA(Segment):
        """Interchange Control Header"""
        isa01: ISA01
        isa02: ISA02
        isa03: ISA03
        isa04: ISA04
        isa05: ISA05
        isa06: ISA06
        isa07: ISA07
        isa08: ISA08
        isa09: ISA09
        isa10: ISA10
        isa11: ISA11
        isa12: ISA12
        isa13: ISA13
        isa14: ISA14
        isa15: ISA15
        isa16: ISA16

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

The  :mod:`x12.common` module would include the following:

::

    I01 = {
        'type': 'string',
        'description': 'name=I01 ele_num=I01 data_type=ID',
        'minLength': 2,
        'maxLength': 2
    }

This :mod:`x12.common` module has the JSON Schema definitions for the data elements.
It doesn't use class definitions, since these are only reusable attributes of an :mod:`x12.base.Element` subclass.

The built-in :mod:`inspect` module provides a handy :func:`get_annotations`
function that examines the attributes of the class
to locate the annotations for the component loops, composites, segments, and elements.

In the case of the element, the class uses a special
internal class, :class:`Schema` to carry some details
of the schema definition.
The class methods use the value of ``self.Schema.datatype``
to interpret the text provided as a Python object.
For data types like "DT", "TM", "R", and the various "Nx", conversions
are applied.

Note that segments are often reused in multiple loops.
For more on this, see :ref:`design.loop_namespace`.

For the Element definition, a class seems to be a bit much, since it's also primitive Python object.
See :ref:`design.element`.
