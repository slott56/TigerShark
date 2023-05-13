#############
The TODO List
#############

Annotations
===========

Central to making this (somewhat) simpler is
to replace **all** the JSON Schema hooks with Annotations.

See :ref:`design.type_hints` and :ref:`design.annotations`.

This breaks down into several steps.

1.  Expand Annotations to replace the "iterim" ``Schema`` internal class.
    A :meth:`Schema` property interrogates the annotations
    to build a valid JSON Schema ``dict[str, Any]`` object
    from the type Annotations.

2.  Replace the :py:class:`x12.base.X12DataType` with a variant
    that works with Annotations instead of JSON Schema.
    (The :meth:`Schema` property, however, permits the interim solution to continue to work.)

    This means an ``Element`` subclass will have one
    mandatory field, ``value`` with an annotated type.
    This replaces the ``Schema`` and the implied pair of fields,
    ``value`` and ``source``.

    In the long run, this Element wrapper is not needed.

3.  Write an integration test cases for the JSON Schema
    to be sure (1) a validator can be built, and (2) it validates
    the JSON output.

4.  Expand the ``tools/xml_extract.py`` application to emit annotations from the XML-defined schema.

5.  Rebuild all the message definitions.

This is the highest priority. Some other things to do
are captured in these documents, and annotated in the code.

Remove Element class
=============================

The ``Element`` class is needless overhead.
It wraps up data conversion functionality
that is better handled by ``Segment`` and ``Composite``
parsing and dumping.

From the Documentation
======================

Things to do, from the documentation.

..  todolist::

From the code
=============

tools/xml_extract.py:        # TODO: DRY issue. The segment_walker (above) is given the class_name value from the Loop class (below).

tools/xml_extract.py:    # TODO: Emit the mapping objects.

x12/base.py:    TODO: Consider str | TextIO | Path as ``text`` parameter type.

x12/base.py:        # TODO: re.search() might be faster at finding the next segment separator

x12/base.py:        # TODO: re.search() might be faster at finding the next element separator

x12/base.py:## TODO: Replace these with annotations.

x12/base.py:## TODO: Refactor to_py(Element, type hint with annotation)

x12/base.py:## TODO: Refactor to_str(object, type hint with annotation)

x12/base.py:    TODO: Replace this with pure annotations.

x12/base.py:        # TODO: Validate with self.type_helper...

x12/base.py:                    # TODO: segment with usage == "R"? Error

