..  _context:

##########################
Context: Use Cases
##########################

C4 suggests we look at Context, Container, Component, Code.
(See https://c4model.com).

This section defines the context by describing the `Actors`_
and their `Use Case Scenarios`_.

The `Data Model`_ section provides an overview of some of the key data entities.

For details on the Containers and Components, see :ref:`architecture`.

Fore more about Code, see :ref:`design`.

Actors
^^^^^^

There are two actors.

-   Developer

    This person creates and modifies definitions of X12 transactions (e.g.,
    270 Eligibility) as Python class definitions.

    They can then build EDI applications which depend on the X12 message
    structures.

-   EDI Application

    An EDI application will import the class definitions.
    These definitions are used to deserialize X12 messages for analysis or processing.
    The application can use the message class definitions to serialize messages in EDI exchange format.

Use Case Scenarios
^^^^^^^^^^^^^^^^^^^^^

The following use cases are explored in detail:

    - `Define An X12 Structure`_

    - `Deserialize A Message`_ (Also called "parsing" or "loading")

    - `Serialize A Message`_ (Also called "unparsing" or "dumping")

Other use cases are combinations of these. For example,
deserializing a message to change the date and serializing the resulting message.

Define An X12 Structure
=================================

Actor locates the IG (Implementation Guide) that describes a message.
This has the loops, segments, composites, and data elements
that comprise the message.
It has the various data element definitions, syntax, and usage
rules, as well as the repetition factors that are permitted.

The PyX12 project has XML files built from from IG's.
For example, :file:`270.4010.X092.A1.xml`.
This file is paired with data element definitions and code definitions.
See https://github.com/azoner/pyx12/tree/master/pyx12/map

TigerShark tools can build JSONSchema and
Python Modules from the XML definitions.
Alternatively, the Python classes can be defined manually from the details in the IG.

Because of the reuse of segment and element names,
each loop definition becomes an important namespace for disambiguating
reused segment names. A specific example is the ``HL``
segment, which appears in many loops, sometimes with
slightly different element names, based on the loop context.

..  _`unmarshall`:

Deserialize A Message
=====================

An application imports a module with message
definition classes.

The application uses the class definitions
to parse a message, creating an instance
of the class.

..  doctest::

    >>> from x12 import msg_271_4010_X092_A1, Source
    >>> from pathlib import Path

    >>> source_path = Path.cwd().parent / "tests" / "271-example.txt"
    >>> source = Source(source_path.read_text())
    >>> msg = msg_271_4010_X092_A1.MSG271.parse(source)

The resulting ``msg`` object is an instance of a subclass of ``Message``
with attributes based on the loop/segment/composite/element structure of the specific message type.

..  _`marshall`:

Serialize A Message
====================

An application imports the module with message
definition classes.

The application creates the message object.

..  doctest::

    >>> from x12.msg_270_4010_X092_A1 import *

    >>> msg = MSG270(
    ...    isa_loop=[
    ...         ISA_LOOP(
    ...             isa=ISA_LOOP_ISA(
    ...                 isa01=ISA_LOOP_ISA01('00'),
    ...                 # etc. for this segment ...
    ...                 isa16=ISA_LOOP_ISA16(':'),
    ...             ),
    ...             gs_loop=[
    ...             # etc. for this loop of segments...
    ...             ],
    ...             st_loop=[
    ...                 ST_LOOP(
    ...                     st=ST_LOOP_ST(
    ...                         st01=ST_LOOP_ST01("271"), st02=ST_LOOP_ST02("0001")
    ...                     ),
    ...                     header=[
    ...                         HEADER(
    ...                             bht=HEADER_BHT(
    ...                                 bht01=HEADER_BHT01("0022"),
    ...                                 bht02=HEADER_BHT02("11"),
    ...                                 bht03=HEADER_BHT03("11111"),
    ...                                 bht04=HEADER_BHT04("20120605"),
    ...                                 bht05=HEADER_BHT05("232423"),
    ...                             )
    ...                         )
    ...                     ],
    ...                     # etc.
    ...                )
    ...             ],
    ...         )
    ...     ]
    ... )

When testing healthcare applications,
EDI messages are oten tweaked to change the date of submission.

..  doctest::

    >>> msg.isa_loop[0].st_loop[0].header[0].bht04 = "20230223"

The intent is to locate instances of the various nested loops, and
then change element values of segments within a loop.
Loops repeat and require indexing.

The application can then dump the message in X12 ("exchange") notation.

..  doctest::

    >>> source_path = Path.cwd() / "changed_for_today.txt"
    >>> with source_path.open('w') as destination:
    ...     msg.dump(destination)

The message can also be dumped in JSON notation.

..  doctest::

    >>> print(msg.json())

The :py:meth:`json` method is similar to the one
offered by the **pydantic** class definitions.
        
Data Model
^^^^^^^^^^

An X12 Message contains Loops.
Each Loop is a recursive structure that contains Loops and Segments.
An Segment contains Composites (groups of Elements) and atomic Elements.

Here's the structure:

..  uml::

    class Message

    class Loop

    class Segment {
        name: string
    }

    Message --> Loop

    Loop --> Loop
    Loop --> Segment

    class Composite

    class Element {
        value: Any
    }

    Segment --> Composite
    Segment --> Element
    Composite --> Element


It's important to note that only segments
have names, and only elements have values.

Further, segment names are reused by loops.
This leads to the following -- more realistic -- depiction
of the structure.


..  uml::

    class Message

    package Loop1 {
        class SegmentX {
            name: string = "X"
        }

        class Composite

        class Element {
            value: Any
        }

        SegmentX --> Composite
        SegmentX --> Element
        Composite --> Element
    }

    package Loop2 {
        class SegmentX {
            name: string = "X"
        }
        class Composite

        class Element {
            value: Any
        }

        SegmentX --> Composite
        SegmentX --> Element
        Composite --> Element
    }

    Message --> Loop1
    Message --> Loop2

The :class:`SegmentX` segment definition is repeated
in each loop, often with small but significant differences,
based on the distinct context.

This leads to the following data model consideration:

    A Loop is a namespace

This then leads to questions on how best to implement
this "loop-as-namespace". This is the topic of the :ref:`design.loop_namespace` design note.
