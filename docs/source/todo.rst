#############
The TODO List
#############

Central to making this (somewhat) simpler is
to replace **all** the JSON Schema hooks with Annotations.

See :ref:`design.annotations`.

This breaks down into several steps.

1.  Parallel Annotations with "iterim" Schema.
    A :meth:`Schema` property interrogates the annotations
    to build a valid JSON Schema ``dict[str, Any]`` object.

2.  Replace the :py:class:`x12.base.X12DataType` with a variant
    that works with Annotations instead of JSON Schema.
    (The :meth:`Schema` property, however, makes the interim solution work.)

Actually write integration test cases for the JSON Schema
to be sure (1) a validator can be built, and (2) it validates
the JSON output.

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

