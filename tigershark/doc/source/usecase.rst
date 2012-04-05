..  _usecase:

##########################
Use Cases
##########################

This document provides a `Actors`_ with an overview
of the actors.

The `Use Case Scenarios`_ chapter describes the individual use cases.

The `Data Model`_ chapter provides an overview of the key data entities.

Architecture: :ref:`architecture`


Actors
^^^^^^

There are two actors.

-   Developer

    This person transforms XML definitions of X12 transactions (e.g.,
    270 Eligibility) into Python class definitions.  This includes
    the structure definitions, plus an unmarshalling Factory.
    
    They may tweak or adjust the XML or the Python based on specific
    source or target implementation details.
    
    They will then build EDI applications which depend on the X12 message
    structures.

-   EDI Application

    An EDI application will import the class definitions and the
    unmarshalling Factory.  The Factory is used to unmarshall X12 messages.
    The application can use the parsed message and marshall a resulting
    message.

Use Case Scenarios
^^^^^^^^^^^^^^^^^^^^^

The following use cases are defined:

    - `Create A Structure and Factory`_

    - `Unmarshall A Message`_
    
    - `Synthesize A Message`_

    - `Marshall A Message`_

Create A Structure and Factory
=================================

Actor locates an XML file that describes a message, for example,
:file:`pyx12-1.5.0\map\270.4010.X092.A1.xml`
in the :file:`pyx12-1.5.0.zip` archive.

Actor runs the X12.MakePython converter.  System creates a module
of Python classes plus an unmarshalling Factory class, for example
:mod:`M270_4010_X092_A1`.

..  _`unmarshall`:

Unmarshall A Message
====================

An application imports the module with message
definition classes and unmarshalling
Factory class. 

The application creates a Factory object.

The application uses the object
to unmarshall a message.

::

    import M270_4010_X092_A1
    u = M270_4010_X092_A1.Unmarshaller()
    with open('a_file','r') as source:
        msg= u.parse( source )

..  _`synthesize`:

Synthesize A Message
=====================

An application imports the module with message
definition classes.

The application creates the message object.

::

    import M270_4010_X092_A1
    msg = M270_4010_X092_A1.M270()

..  _`marshall`:

Marshall A Message
====================

An application imports the module with message definition classes and marshalling
Factory class. 

The application develops a message and a Factory object.  Perhaps
through the `Unmarshall a Message`_ use case.  Perhaps through
a `Synthesize a Message`_ use case.

It uses
the Factory object to marshall the message.

::

    import M270_4010_X092_A1
    m = M270_4010_X092_A1.Marshaller()
    with open('a_file','w') as destination:
        m.dump( msg, destination )
        
Data Model
^^^^^^^^^^

There are three subject areas:

-   `Message Schema and Factory`_.  The message structure and the
    marshall/unmarshall Factory class.
    This is the essential X12 message structure
    xreated
    
-   `Module Builder`_.  This is a module which transforms the XML
    schema definition into a module with POPO's and a Factory.

-   `XML Schema`_.  The master definition of the X12 message.


Message Schema and Factory
=====================================

An X12Message contains X12Loops.
Each X12Loop is a recursive structure that contains X12Loops and X12Segments.
An X12Segment contains Composite Elements and Atomic Elements.

The standard technique for recursive structures involves a polymorphic design,
as shown in `Figure 1`_.

.. figure:: usecaseclaim.png

    _`Figure 1`.

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