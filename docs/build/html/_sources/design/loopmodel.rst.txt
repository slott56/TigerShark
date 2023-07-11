..  _`design.loop_namespace`:

###################
Loops as Namespace
###################

Within a message, a number of loops can reuse
segment names, providing alternative definitions for the segment.
Each segment definition is unique to a loop,
making the loop definition a kind of namespace
for the segments, composites, and elements that are part of the loop.

Using a Loop definition as a namespace presents a
potential complication.
There are several potential ways to implement a namespace.

1.  `Packages and modules`_. A message can be a package, each loop can be a module within the package.

2.  `Nested class definitions`_. A loop's ``class`` can contain nested classes for Segments, Composits, and Elements.

3.  `Qualified name prefixes`_. A loop's name can be a prefix for a Segment, Composite, and Element name.
    This is the current solution.

A more radical approach is to discard the idea of
Python class, and rely on JSON Schema as a way to describe
message structure. This seems to defeat the design objective
of using Plain Old Python Objects for the various segments
and elements of each message. With this, the schema is required
at all levels to make sense of the exchange message text.

This design uses the `Qualified name prefixes`_ tecchnique.
Names like ``L2000_HL`` and ``L2100_HL`` define two ``HL`` segments that are part of two distinct loops,
``L2000`` and ``L2100``.


Packages and modules
====================

The idea is to have the following structure

-   ``msg_xxx``

    -   ``__init__.py``

        ::

            from base import Message,Loop,Segment,Composite,Element
            import isa_loop

            class Msg_xxx(Message):
                isa_loop: isa_loop.ISA_Loop

    -   ``isa_loop``

        -   ``__init__.py``

            ::

                from base import Message,Loop,Segment,Composite,Element

                class ISA(Segment):
                    etc.
                class IEA(Segment):
                    etc.
                class ISA_Loop(Loop):
                    isa: ISA
                    iea: IEA

This tends to bury the meaningful content deep within
a directory hierarchy where it can be difficult to find.

This seems to break the Zen of Python advice that flat is better than nested.
This will create very deeply nested structures.


Nested class definitions
========================

The idea is to have the following structure

-   ``msg_xxx.py``

    ::

        from base import Message,Loop,Segment,Composite,Element
        import common

        class ISA_Loop(Loop):
            class ISA(Segment):
                isa01: common.I01
                etc.

            class IEA(Segment):
                iea01: common.I01
                etc.

            isa: ISA
            iea: IEA

        class Msg_xxx:
            isa_loop: ISA_Loop


The message is contained within a single file.

With some care, very deeply-nested
structures can be avoided.
Each Loop can be declared at the top level of
the module. The level of nesting
should be limited to elements, segments and composites
within a containing loop.

Loop names are unique and reflect the loop nesting.
A sequence of loop definitions can be used by
containing loops and the overall message.

Qualified name prefixes
=======================


The idea is to have the following structure

-   ``msg_xxx.py``

    ::

        from base import Message,Loop,Segment,Composite,Element
        import common

        class ISA_Loop_ISA(Segment):
            isa01: common.I01
            etc.

        class ISA_Loop_IEA(Segment):
            iea01: common.I01
            etc.

        class ISA_Loop(Loop):
            isa: ISA_Loop_ISA
            iea: ISA_Loop_IEA

        class Msg_xxx:
            isa_loop: ISA_Loop

The message is contained within a single file.

Nested structures are avoided.
The loop now has two aspects:

-   A prefix for segment, composite, and element names.

-   A class definition.

A sequence of class definitions can be used as needed
to build composites, segments, loops, and the overall message.

Loop names are unique and reflect the loop nesting.
For example, Loop 2100 is a sub-loop of Loop 2000.
The prefix of ``Loop_2100_`` is sufficient to express
the reuse of a segment within separate loops.
Longer prefixes are not required.
