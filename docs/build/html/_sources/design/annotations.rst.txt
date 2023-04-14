..  _`design.annotations`:

################
Type Hints
################

The message/loop/segment/composite structure is defined with type hints.
Individual elements don't rely on type annotations, but instead rely on JSON Schema details provided separately.

We'll explore this with a series of examples.

-   `Messages`_. These are collections of Loops.

-   `Loops`_. These are collections of Segments and Sub-Loops.

-   `Segments`_. These are collections of Elements and Composites.

-   `Elements`_. These are atomic.

-   `Composites`_. These are collections of Elements.

The objective is to provide a pure-Python definition of the X12 EDI structure.
This can make it easier to examine and analyze messages.
It can also make it somewhat easier to define alternative syntax for messages
to further facilitate analysis and processing.

..  important:: The JSON Schema is a work in progress

    The JSON Schema seems reasonable, but has not really been implemented fully.

..  important:: The IG compliance is indirect

    These definitions are based on the PyX12 project and may have introduced
    additional bugs or complications.

The JSON Schema **should** be more tightly integrated into the Python definitions.
An explicit ``Schema`` internal class should be removed.

Messages
=========

Here's an example of a Message definition.

::

    class MSG270(Message):
        """HIPAA Health Care Eligibility Inquiry X092A1-270"""
        class Schema:
            json = {'title': 'HIPAA Health Care Eligibility Inquiry X092A1-270',
             'description': 'xid=270 name=HIPAA Health Care Eligibility Inquiry X092A1-270',
             'type': 'object',
             'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
             'required': ['isa_loop']}
        isa_loop: list[ISA_LOOP]

The message contains a single attribute.

:isa_loop:
    This is defined by the ``list[ISA_LOOP]`` type annotation to be a list of ``ISA_LOOP`` instances.
    A parsed message will always have an ``isa_loop`` attribute, and it will be a list.
    An application will use ``msg.isa_loop[0]`` to refer to the first ISA loop of a given message.

Additional information is provided in an internal class definition, always named ``Schema``, providing JSON Schema
details. These come from the source XML (and the original IG) and represent aspects of a defintion that
aren't **easily** incorporated into a class definition.

..  important:: The JSON Schema values should be deduced from pure Python.

    Here are schema attributes and how they could be defined.

    :title:
        Should be first line of the docstring

    :description:
        Should be the docstring with the first line removed

    :type:
        Is always ``object`` for Messages, Loops, Segments, and Composites.

    :properties:
        Is a template that can be built from the attribute type annotations.

    :required:
        This isn't obvious from Python, but can be deduced from the ``| None`` annotations used for the attributes.

    ..  todo:: Reduce reliance on a ``Schema`` class for ``Message`` subclasses. ``Schema`` should be a property.


Loops
=========

A Loop a collection of segments (and sub-loops). It is also a namespace to distinguish reused references
to a common segment definition. See :ref:`design.loop_namespace`.

The loop-as-namespace is implemented by using the loop name as a qualifier for segments that are part of the loop.

Here's an example of a Loop definition.

::

    class ISA_LOOP(Loop):
        class Schema:
            json = {'type': 'array',
             'items': {'title': 'Interchange Control Header',
                       'usage': 'R',
                       'description': 'xid=ISA_LOOP name=Interchange Control Header '
                                      'type=explicit',
                       'position': 1,
                       'type': 'object',
                       'properties': {'isa': {'$ref': '#/$segments/ISA_LOOP_ISA'},
                                      'gs_loop': {'$ref': '#/$segments/GS_LOOP'},
                                      'ta1': {'$ref': '#/$segments/ISA_LOOP_TA1'},
                                      'iea': {'$ref': '#/$segments/ISA_LOOP_IEA'}},
                       'required': ['isa', 'gs_loop', 'iea']}}
        isa: ISA_LOOP_ISA
        gs_loop: list[GS_LOOP]
        ta1: ISA_LOOP_TA1 | None
        iea: ISA_LOOP_IEA

This Loop has four attributes.

:isa:
    An instance of the ISA_LOOP's ``ISA`` segment.

:gs_loop:
    A sequence of GS_LOOP instances.

:ta1:
    An optional instance of the  ISA_LOOP's ``TA1`` segment.

:iea:
    An instance of the ISA_LOOP's ``IEA`` segment.

Additional information is provided in an internal class definition, always named ``Schema``, providing JSON Schema
details. These come from the source XML (and the original IG) and represent aspects of a defintion that
aren't **easily** incorporated into a class definition.
For example, the ``'usage': 'R'`` means this loop is required; this is properly an aspect of the parent message.

..  important:: The JSON Schema values should be deduced from pure Python.

    Note that the description includes values taken from the XML schema (and the IG) that don't seem to be useful,
    but are sill preserved here.

    ..  todo:: Reduce reliance on a ``Schema`` class for ``Message`` subclasses. ``Schema`` should be a property.

Segments
=========

Here's an example of a Segment definition.

::

    class ISA_LOOP_IEA(Segment):
        """Interchange Control Trailer"""
        class Schema:
            json = {'title': 'Interchange Control Trailer',
             'usage': 'R',
             'description': 'xid=IEA name=Interchange Control Trailer',
             'position': 30,
             'type': 'object',
             'properties': {'xid': {'literal': 'IEA'},
                            'iea01': {'$ref': '#/$elements/ISA_LOOP_IEA01'},
                            'iea02': {'$ref': '#/$elements/ISA_LOOP_IEA02'}},
             'required': ['iea01', 'iea02']}
            segment_name = 'IEA'
        iea01: ISA_LOOP_IEA01
        iea02: ISA_LOOP_IEA02

This Segment has two attributes and a segment ``xid``.

:xid:
:segment_name:
    The literal ``"IEA"`` to identify this segment. This is defined in the ``Schema`` object.
    It -- perhaps -- could be a ``Literal["IEA"]`` type annotation.
    However, the name is an immutable feature of the segment, not a mutable attribute value.

:iea01:
    An instance of the ISA_LOOP's ``IEA01`` element.

:iea02:
    An instance of the ISA_LOOP's ``IEA02`` element

..  important:: The JSON Schema values should be deduced from pure Python.

    Note that the description includes values taken from the XML schema (and the IG) that don't seem to be useful,
    but are sill preserved here.

    The position attribute seems to be used to sort the definitions into a proper ordering within a loop definition.

    ..  todo:: Reduce reliance on a ``Schema`` class for ``Message`` subclasses. ``Schema`` should be a property.


Elements
=========

Here's an example of an Element definition.

::

    class ISA_LOOP_IEA01(Element):
        """Number of Included Functional Groups"""
        class Schema:
            json = {'title': 'Number of Included Functional Groups',
             'usage': 'R',
             'description': 'xid=IEA01 data_ele=I16',
             'sequence': 1,
             'type': {'$ref': '#/$common/I16'}}
            datatype = common.I16
            min_len = 1
            max_len = 5

There are no attributes of an Element.  (If there were, it wouldn't be atomic, would it?)

The details of the value's type are provided in the XML schema definition.
They can also be provided via a set of common type definitions that are widely reused, as well as being part of the element.

In this case, the I16 definition looks like this:

::

    I16 = {'type': 'number', 'scale': 0, 'title': 'I16', 'data_type_code': 'N0', 'minLength': 1, 'maxLength': 5}

These details were used to build the ``min_len`` and ``max_len`` attributes of the ``Schema`` object.
These features are very important when parsing the ISA segment. The remaining details are helpful for converting source text to a Python value,
and are used by the element's :meth:`x12.base.Element.value` method.

It's not perfectly clear whether or not Element details require a separate class.
See :ref:`design.element`.


Composites
==========

Here's the definition of a Composite.

::

    class L2110D_C003(Composite):
        class Schema:
            json = {'title': 'Composite Medical Procedure Identifier',
             'usage': 'S',
             'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                            'data_ele=C003',
             'sequence': 2,
             'syntax': [],
             'type': 'object',
             'properties': {'eq02_01': {'title': 'Product or Service ID Qualifier',
                                        'usage': 'R',
                                        'description': 'xid=EQ02-01 data_ele=235',
                                        'sequence': 1,
                                        'type': {'allOf': [{'$ref': '#/$common/235'},
                                                           {'enum': ['AD', 'CJ', 'HC', 'ID',
                                                                     'IV', 'N4', 'ZZ']}]}},
                            'eq02_02': {'title': 'Procedure Code',
                                        'usage': 'R',
                                        'description': 'xid=EQ02-02 data_ele=234',
                                        'sequence': 2,
                                        'type': {'$ref': '#/$common/234'}},
                            'eq02_03': {'title': 'Procedure Modifier',
                                        'usage': 'S',
                                        'description': 'xid=EQ02-03 data_ele=1339',
                                        'sequence': 3,
                                        'type': {'$ref': '#/$common/1339'}},
                            'eq02_04': {'title': 'Procedure Modifier',
                                        'usage': 'S',
                                        'description': 'xid=EQ02-04 data_ele=1339',
                                        'sequence': 4,
                                        'type': {'$ref': '#/$common/1339'}},
                            'eq02_05': {'title': 'Procedure Modifier',
                                        'usage': 'S',
                                        'description': 'xid=EQ02-05 data_ele=1339',
                                        'sequence': 5,
                                        'type': {'$ref': '#/$common/1339'}},
                            'eq02_06': {'title': 'Procedure Modifier',
                                        'usage': 'S',
                                        'description': 'xid=EQ02-06 data_ele=1339',
                                        'sequence': 6,
                                        'type': {'$ref': '#/$common/1339'}},
                            'eq02_07': {'title': 'Description',
                                        'usage': 'N',
                                        'description': 'xid=EQ02-07 data_ele=352',
                                        'sequence': 7,
                                        'type': {'$ref': '#/$common/352'}}},
             'required': ['eq02_01', 'eq02_02']}
        eq02_01: L2110D_EQ02_01
        eq02_02: L2110D_EQ02_02
        eq02_03: L2110D_EQ02_03 | None
        eq02_04: L2110D_EQ02_04 | None
        eq02_05: L2110D_EQ02_05 | None
        eq02_06: L2110D_EQ02_06 | None

This defines six attributes; the first two are required, four are "situational", one (with ``'usage': 'N',``) is not used.

The name, ``L2110D_C003``, uses the loop ``2210D`` as a namespace for composite ``C003``.
The composite name seems to haVe been generated as part of the XML, and may not be formally defined in the IG.
