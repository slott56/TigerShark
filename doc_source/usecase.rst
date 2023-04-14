..  _usecase:

##########################
Use Cases
##########################

This chapter describes the `Actors`_
and their `Use Case Scenarios`_.

The `Data Model`_ section provides an overview of the key data entities.

For details on the architecture, see :ref:`architecture`.


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
    These definitions are used to unmarshall X12 messages.
    The application can use the parsed message and marshall a resulting
    message.

Use Case Scenarios
^^^^^^^^^^^^^^^^^^^^^

The following use cases are defined:

    - `Create An X12 Structure`_

    - `Unmarshall A Message`_

    - `Marshall A Message`_

Create A Structure and Factory
=================================

Actor locates the IG (Implementation Guide) that describes a message.
This has the loops, segments, composites, and data elements
that comprise the message.
It has the various data element definitions, syntax, and usage
rules, as well as the repetition factors that are permitted.

The PyX12 project has XML files built from from IG's.
For example, :file:`270.4010.X092.A1.xml`.
This is paired with data element definitions and code definitions.
See https://github.com/azoner/pyx12/tree/master/pyx12/map

A tool in this project can help to build JSONSchema and
Python Modules from the XML definitions.

Because of the reuse of segment and element names,
the loop becomes an important namespace for disambiguating
reused segment names. A specific example is the ``HL``
segment, which appears in many loops, sometimes with
slightly different element names.

..  _`unmarshall`:

Unmarshall A Message
====================

An application imports a module with message
definition classes.

The application uses the class definitions
to unmarshall a message, creating an instance
of the class

::

    from x12.msg_270_4010_X092_A1 import MSG270
    with open('a_file', 'r') as source:
        msg = MSG270.parse(source)

..  _`marshall`:

Marshall A Message
====================

An application imports the module with message
definition classes.

The application creates the message object.

::

    from x12.msg_270_4010_X092_A1 import MSG270
    msg = MSG270(
        ISA_LOOP(
            ISA_LOOP_ISA(
                isa01=...,
                isa02=...,
            )
        )
    )

When testing healthcare applications,
EDI messages are oten tweaked to change the date of submission.

::

    msg.find("SOME_LOOP")[0].segment.s01 = "20230223"

The intent is to locate a deeply-nested loop, and
then change attributes of segments within that specific loop.
Loops that may repeat will require indexing.
Loops that do not repeat do not require indexing.

The application can then dump the message in X12 notation.

::

    with open('a_file', 'w') as destination:
        msg.dump(destination)

The message can also be dumped in JSON notation.

::

    print(msg.json())

The :py:meth:`json` method is similar to the one
offered by the **pydantic** class definitions.
        
Data Model
^^^^^^^^^^

An X12 Message contains Loops.
Each Loop is a recursive structure that contains Loops and Segments.
An Segment contains Composites (groups of Elements) and atomic Elements.

Here's the structure:

..  startuml::

    class Message

    class Loop

    class Segment

    Message --> Loop

    Loop --> Loop
    Loop --> Segment

    class Composite

    class Element

    Segment --> Composite
    Segment --> Element
    Composite --> Element



An X12Message is an X12Structure, and contains X12Structure elements.
An X12Loop, similarly, is an X12Structure and contains X12Structure elements.
This allows a loop to contain subloops as well as segments.  An X12Segment
is an X12Structure (and contained within an X12Loop), but is not a container
of other elements.

X12Element and X12Composite contain the attributes of an X12Segment.

For implementation notes, see :ref:`Recursive Structures`.

Module  Builder
=====================

Transform XML definitions of X12 messages into POPO and marshall/unmarshall
factory class.

Generally, this is an XML parser which creates DOM objects,
and a suite of Visitors to emit Python class definitions which
reflect the X12 message structure.

Other visitors can be defined wich will emit Django model definitions
or, perhaps, SQLAlchemy model definitions.

XML Schema
================================

This is the definition of X12 messages.  We borrow these from the Py12
package which provides definitions of X12 messages.

The schema repository contains three types of XML files.

-   :file:`270.4010.X092.A1.xml` message definition

-   :file:`codes.xml`

-   :file:`dataele.xml`

-   :file:`maps.xml`
