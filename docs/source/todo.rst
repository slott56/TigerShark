#############
The TODO List
#############

General Design
==============

Refactor parsing to separate it from
the ``Message``, ``Loop``, ``Segment``, ``Composite``
class structure.

Ideally, an instance of ``Parse`` should be able to fill in classes
defined with **Pydantic**.

::

    class X12Parser:
        """
            Walks the structure of the annotated components,
            parses the Segment text blocks.
        """
        def parse(self, cls: type[Message], source: Source, skip_validation : list[str] | None = None) -> Message:
            ...
        def msg_attr_build(self, cls: type[Message], name: str, loop_type: type, source: Source) -> Loop | list[Loop] | None:
            ...
        def loop_parse(self, cls: type[Loop], source: Source) -> Union[Loop, None]:
            ...
        def loop_attr_build(self, cls: type[Loop], name: str, field_type: type, source: Source) -> Segment | list[Segment] | None:
            ...
        def segment_parse(self, cls: type[Segment], source: Source) -> Union[Segment, None]:
            ...
        def segment_attr_build(self, cls: type[Segment], field_type: type, source_values: list[str | None | list[str | None]]) -> Any | list[Any] | Composite | None:
            ...
        def composite_build(self, cls: type[Composite], source_value: str | None | list[str | None]) -> Composite:
            ...
        def composite_attr_build(self, cls: type[Composite], field_type: type, source_value: str | None) -> Any:
            ...

Annotations
===========

1.  Write an integration test cases for the JSON Schema output from a class.
    Confirm (1) a validator can be built, and (2) it validates
    the JSON output from the class.

2.  Unify the various "Peel the Onion" algorithms.

3.  Cleanup type hints to the extent possible.
    A large number of ``type: ignore[misc]`` comments are present.

Some other things to do
are captured in these documents, and annotated in the code.

From the Documentation
======================

Things to do, from the documentation.

..  todolist::

From the code
=============

::

    % find tigershark3 -name '*.py' -exec grep -Hn -i todo {} \;


tigershark3/tools/xml_extract.py:176:.. todo:: This version identification is not implemented

tigershark3/tools/xml_extract.py:886:        ..  todo:: properly flatten the message to emit $loop, $segment, $composite, and $element definitions.

tigershark3/tools/xml_extract.py:1100:        # TODO: DRY issue. The segment_walker (above) is given the class_name value from the Loop class (below).

tigershark3/tools/xml_extract.py:1538:        # TODO: Emit the mapping objects.

tigershark3/tools/xml_extract.py:1552:## TODO: Combine make_message_schema() and  make_jsonschema() into a class

tigershark3/tools/xml_extract.py:1563:    ..  todo:: Include the "$ref" data types and code sets.

tigershark3/x12/annotations.py:183:    ..  todo:: Handle Union[T | None].

tigershark3/x12/base.py:78:    ..  todo:: Consider str | TextIO | Path as ``text`` parameter types.

tigershark3/x12/base.py:126:        ..  todo:: Optimize the field and composite splitting to avoid creating multiple lists.

tigershark3/x12/base.py:131:        # TODO: re.search() might be faster at finding the next segment separator

tigershark3/x12/base.py:140:        # TODO: Segment ISA parser can replace ISA16 ``["", ""]`` value with the parsed array_sep value.

tigershark3/x12/base.py:173:        # TODO: re.search() might be faster at finding the next element separator

tigershark3/x12/base.py:207:    ..  TODO: Should be a  hierarchy of classes.

tigershark3/x12/base.py:222:                # TODO: Create a X | Y | None to_py construct.

tigershark3/x12/base.py:230:                # TODO: Create A "list[X]" to_py that checks MaxItems (and MinItems)

tigershark3/x12/base.py:276:                # TODO: Make this sensisitve to MinLen() and MaxLen()

tigershark3/x12/base.py:284:                # TODO: Make this sensisitve to MinLen() and MaxLen()

tigershark3/x12/base.py:297:        # TODO: Seems to be a silly optimization.

tigershark3/x12/base.py:338:            # TODO: Check ``Usage`` and ``Required`` annotations

tigershark3/x12/base.py:433:            # TODO: X12ElementHelper has formats.

tigershark3/x12/base.py:550:        ..  todo:: Remove ``instance`` parameter

tigershark3/x12/base.py:693:            # TODO: Refactor into recursive walk through type...

tigershark3/x12/base.py:694:            # TODO: PEEL THE ONION...

tigershark3/x12/base.py:744:            # TODO: PEEL THE ONION

tigershark3/x12/base.py:870:        ..  todo:: Rename this to not conflict with semantics of `Source`.

tigershark3/x12/base.py:915:            # TODO: PEEL THE ONION...

tigershark3/x12/base.py:971:                # TODO: segment with usage == "R"? Error

tigershark3/x12/base.py:1060:            # TODO: PEEL THE ONION.

tigershark3/__main__.py:66:    TODO: Output is "json" format.
