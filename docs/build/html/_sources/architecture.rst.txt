..  _architecture:

########################################
Architecture: Containers and Components
########################################

C4 suggests we look at Context, Container, Component, Code.
(See https://c4model.com).
For more information on the Context, see :ref:`context`.

This chapter provides Container and Component views.

The `Architecture Summary`_ has an overview of the architectural principles.

The `Container View`_ is pretty small. This is a simple set of applications to run on a desktop computer.

The `Component View`_ section provides an overview of the package structure
underlying the application software.

The `Processing Model`_ section provides an overview of the various kinds of processing that occur.

The `Dependencies`_ section identifies an important implementation dependency: the PyX12 project.

An overview of the Code is covered in :ref:`design`. Details are in :ref:`implementation`.

Architecture Summary
^^^^^^^^^^^^^^^^^^^^

There are two distinct "levels" or "views" to this application.

:Developer:
    These are the tools to create and test the message class definitions.
    This defines X12 message types as Plain Old Python Object (POPO) classes.

:Application:
    A message is implemented as class in a module.
    The class is used to load and dump the text of messages in a variety of formats.
    (Other terms are parse/unparse, deserialize/serialize, unmarshall/marshall.)

The most common use case is loading an  "exchange" format message to create Python objects.
From here, Python to JSON conversions can persist an easy-to-use copy of the message.

Developer's Perspective
=======================

An X12 message has a complicated, nested structure of loops, segments, composites and elements.
There are several layers in the interpretation of a message:

1.  Exchange Format. This is a big block of text, sometimes with additional ``\n`` inserted after each segment separator.

2.  X12 Segment Format. The segment separator can be used to decompose the exchange format into
    a sequence of segments. Each segment is a sequence of element and composite values.
    Note that the loop structure is not an explicit part of this representation.

3.  The application's view of a Message. For example, a Claim or Eligibility Request.
    This is a Python object with the loops, segments, composites, and elements of the message.

The PyX12 project defines common sets of code values,
and common data types outside the messages.
This is reflected in a :py:mod:`x12.common` module with these definitions.

Before we look at the application use of message, we'll look at message definitions in general.

X12 Message Definitions
-----------------------

The X12 standard is defined via :file:`.SEF` files; additional
meta-definitions are used to manage the exchange of messages,
versioning, and other considerations.
These files are proprietary, and not freely available.

Instead, we rely on the Python-based `PyX12`_ package.
This package defines X12 messages using ``.xml`` files that seem to be reasonably complete.

..  _`PyX12`: https://github.com/azoner/pyx12

The TigerShark :py:mod:`tools.xml_extract` tool can transform the ``.xml`` files
into Python class definitions.
A class definition can emit JSON Schema for messages of that class.

Ideally, it would be preferrable to work directly  with the :file:`.SEF` files.

Application Perspective
=============================

An X12 :py:class:`x12.base.Message` object is what an application uses.
It's a collection of X12 Loops, Segments, Composites, and Elements.
The segment names are often reused, meaning
that a segment only has meaning in the context
of a specific Loop.

This leads to a naming convention for classes where a segment name
is prefixed with the loop that uses that segment.
For example ``ISA_LOOP_ISA`` has a loop name of ``ISA_LOOP``,
and a segment name of ``ISA`` in the context of the ISA Loop.
See the :ref:`design.loop_namespace` design note.

Container View
^^^^^^^^^^^^^^^

Any applications are typically single container applications.
For example, the :py:mod:`tools.xml_extract` reads XML definitions and creates
message class definitions.

An application that parses messages is most often going to be
a single container to extract useful content from messages
for deeper analysis.

Component View
^^^^^^^^^^^^^^^

The component packaging breaks into two major areas.

..  uml::

    package x12 {
        package base {
            component Source
            component X12Parser
            component Composite
            component Segment
            component Loop
            component Message
        }
        [common]
        [annotations]
        [msg_xxx_yyyy_zzz]

        msg_xxx_yyyy_zzz --> base
        msg_xxx_yyyy_zzz --> common
        msg_xxx_yyyy_zzz --> annotations
    }

    package your_app {
        [some_app]
    }

    some_app --> msg_xxx_yyyy_zzz


Here are some more details on the Python packages and modules.

-   :mod:`x12`. This is a package for handling the serializing and
    deserializing of X12 messages.

    -   :mod:`x12.annotations`. This has classes that define annotations to collect the details of an Element (or Composite).

    -   :mod:`x12.base`. This has the abstract base class definitions for all messages.
        It also includes the :mod:`x12.base.Source` and :mod:`x12.base.X12Parser` classes used to parse wire-format messages.

    -   :mod:`x12.common`. This has common data element and code definitions. This is built by the :mod:`tools.xml_extract` tool. Touching this is unwise.

    -   ``msg_mmm_vvvv_Xxxx...py`` modules with message definitions. These are built by the :mod:`tools.xml_extract` tool. Touching these is unwise.

-   :mod:`tools`. This package has applications to help define the message classes.

    -   ``xml_extract`` Converts the XML definitions to ``x12/msg_mmm_vvvv_Xxxx...py`` files.


Processing Model
^^^^^^^^^^^^^^^^

There are several kinds of processing that are part of TigerShark.

-   The application processing includes multiple conversions between Exchange (the X12 text format),
    JSON and Python notation.

    -   `Loading`_ extracts useful Python objects from messages in Exchange or JSON format.

    -   An application can modify the Python or JSON message. An application can persist the JSON or Python notation, also.

    -   `Dumping`_ builds a message in Exchange format or JSON from Python objects.

-   `JSON Schema`_ describes the JSON Schema formalization of the structure.
    This is how messages in JSON notation can be described.

Loading
=============

See the :ref:`unmarshall` use case.

There are three ways to load messages:

-   From "exchange format" text.

-   From a JSON dump of the objects.

-   Using Python code to build a message.

Exchange Format Parsing
-----------------------

A :py:class:`base.Message` class has a :meth:`base.Message.parse` method for loading (or deserializing or parsing) text to create Plain Old Python Objects.

This class processes text that's wrapped in the :py:class:`base.Source` class definition.
This wrapper leverages the segment, element, and component separator characters required
to decompose a message.


..  doctest::

    >>> from x12 import msg_271_4010_X092_A1, Source, X12Parser
    >>> from pathlib import Path

    >>> source_path = Path.cwd().parent / "tests" / "271-example.txt"
    >>> source = Source(source_path.read_text())
    >>> parser = X12Parser(msg_271_4010_X092_A1.MSG271)
    >>> msg = parser.parse(source)


JSON Load
---------

Not currently implemented.

Python Code
-----------

A message can be build using ordinary class constructors of the various
Message, Loop, Segment, and Composite classes that define the message.

..  doctest::

    >>> from x12.msg_271_4010_X092_A1 import *

    >>> m = MSG271(
    ...     isa_loop=[
    ...         ISA_LOOP(
    ...             isa=ISA_LOOP_ISA(
    ...                 isa01="00",
    ...                 isa02="          ",
    ...                 isa03="00",
    ...                 isa04="          ",
    ...                 isa05="ZZ",
    ...                 isa06="ZIRMED         ",
    ...                 isa07="ZZ",
    ...                 isa08="12345          ",
    ...                 isa09="120605",
    ...                 isa10="2324",
    ...                 isa11="U",
    ...                 isa12="00401",
    ...                 isa13="000050033",
    ...                 isa14="1",
    ...                 isa15="P",
    ...                 isa16="^",
    ...             ),
    ...             gs_loop=[
    ...             # etc. for all of the various loops inside the GS
    ...             ],
    ...             iea=ISA_LOOP_IEA(
    ...                 iea01="1", iea02="000050033"
    ...             ),
    ...         )
    ...     ]
    ... )

Dumping
===========

See the :ref:`marshall` use case.

An application must load (or build) a message.
It may also tweak the message

This means

..  doctest::

    >>> msg.isa_loop[0].st_loop[0].header[0].bht04 = "20230223"

Each Message object handles serialization into X12 text
or JSON.
A :meth:`dump` method emits the content in X12 "exchange format".
A :meth:`json` method emits the content in JSON notation.


The application can then dump the message.
This can be in X12 ("exchange") notation.

..  doctest::

    >>> source_path = Path.cwd() / "changed_for_today.txt"
    >>> with source_path.open('w') as destination:
    ...     msg.dump(destination)

The message can also be dumped in JSON notation.

..  doctest::

    >>> print(msg.json())

The :py:meth:`json` method is similar to the one
offered by the **pydantic** class definitions.

JSON Schema
===========

See the :ref:`schema` use case.

Conceptually, the JSON Schema description of a message can be defined as

::

    some_message:
        type: object
        properties:
            loop1:
                $ref: #/$loops/loop1
            loop2:
                $ref: #/$loops/loop2

Each loop definition is provided in a ``$loops`` section of the overall schema definition.

A loop definition  needs to refer to segments using a more complex path.

::

    $loops:
        loop1:
            type: object
            properties:
                segmentX:
                    $ref: #/$segments/loop1/segmentX
        loop2:
            type: object
            properties:
                segmentX:
                    $ref: #/$segments/loop2/segmentX

Each segment definition is provided in a ``$segments`` section of the overall schema definition.
The path, however, includes the containing loop.
This permits the distinct definitions of a reused segment in multiple loop contexts.

The JSON Schema representation of the message
definitions is handled via a large number of ``{"$ref": ...}`` references.
This permits a relatively flat structure that parallels the Python class definitions.

The complete message is generally defined as follows:

::

    title: 227
    description: details of the 227 message
    type: object
    properties:
        isa_loop:
            "$ref": "#/$loops/isa_loop"

    "$loops":
        isa_loop:
            type: object
            properties:
                ISA:
                    "$ref": "#/$segments/isa_loop/ISA"
                gs_loop:
                    "$ref": "#/$loops/gs_loop"
                IEA:
                    "$ref": "#/$segments/isa_loop/IEA"

    "$segments":
        isa_loop:
            ISA:
                type: object
                properties:
                    ISA01:
                        "$ref": "#/$elements/isa_loop/ISA01"

    "$elements":
        isa_loop:
            ISA01:
                description: Authorization Information Qualifier
                type:
                    "$ref": "#/$datatype/I01"

    "$datatype":
        I01:
            x12_type: "ID"
            type: string
            minLength: 2
            maxLength: 2

This structure avoids deeply-nested constructs.
It permits reuse of the data types and codes.
It provides a loop namespace to disambiguate segments, and their composites and elements.

Currently, the internal message classes can be turned into JSON Schema.
The :py:func:`x12.base.schema` function does *not* structure
the JSON Schema with the base and common definitions
clearly separated like this. Instead it coughs out
deeply-nested JSON Schema with redudant copies
of base definitions.

However, the :mod:`tools.xml_extract` makes an effort
to provide a flatter structure that reflects the source
definitions in XML. (These, in turn, likely reflect the
original specification files.)


Dependencies
^^^^^^^^^^^^

The tools depend on the PyX12 prohject.
The PyX12 project has XML files built from from IG's.
See https://github.com/azoner/pyx12/tree/master/pyx12/map

This schema repository contains three types of XML files.

-   :file:`270.4010.X092.A1.xml` message definition

-   :file:`codes.xml`

-   :file:`dataele.xml`

-   :file:`maps.xml`
