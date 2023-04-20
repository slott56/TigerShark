..  _architecture:

########################################
Architecture and Design
########################################

This document provides an `Architecture Summary`_ with an overview of the
architectural principles.

The `Database Design Alternatives`_ chapter describes alternative database design
strategies.

The `Component Model`_ chapter provides an overview of the package structure
underlying the application software.

The `Processing Model`_ chapter provides an overview of the various kinds of processing that occur.

`Appendix I`_ contains the 57 distinct segment types.

Requirements: :ref:`UseCase`.

Architecture Summary
^^^^^^^^^^^^^^^^^^^^

There are two distinct "levels" or "views".

-   Meta-Level processing. This is the developer's view.  It is used to
    generate the message class definitions. This is a preliminary step
    to transform X12
    message format definitions into Plain Old Python
    Object (POPO) class definitions.

-   Application-Level processing. This is an application's view.  A message
    is implemented as a
    module that can be imported.  The module is used to unmarshall and marshall
    X12 messages.

Meta-Level Processing
=====================

The simplest, standard format for claims is the X12 ("EDI" or "HIPAA") message
format. EDI applications will have an X12 interchange or
"gateway" for handling messages in X12 format.

X12 Background
--------------

An X12 message can have a tremendous number of individual loops, segments,
and elements, making it difficult to create meaningful data definitions
manually. Generally, the X12 standard is defined via :file:`.SEF` files; additional
meta-definitions are used to manage the complexity.

There are several layers of interpretation of a message.

    -   X12 Message in exchange format, a big block of text.
        This is rather difficult to manipulate since it must be
        unmarshalled for processing.

    -   X12 Segments. It's relatively easy to decompose an X12 message into
        a sequence of segments of known types. This is a purely lexical analysis,
        so we can call this tokenizing a message into
        segment tokens. This is also a convenient form for persisting a message,
        since it is generally fixed by the X12 standard. See `Database Design
        Alternatives`_.

    -   X12 Loops. Loops are closer to the "meaning" of a message. Loops
        are not present in the source text; a semantic analysis of the content
        of individual segment tokens is required to determine the loops present
        in a given message. This is somewhat more flexibly defined, since an X12
        Implementation Guide may alter the "Required", "Situational" and "Not
        Used" status of a loop or segment.

    -   Claim or Eligibility Request. A Claim or Eligibility Request
        is an interpretation of the loops and segments in an X12
        message. This is most convenient for application processing.

X12 Message Definitions
-----------------------

X12N message definitions are rather complex, and defining a the necessary
class definitions and message unmarshaller
by hand is challenging. X12N messages are defined by Standards as well as a
vendor's unique Implementation Guide. This means that message unmarshalling
and compliance checking has to be performed using customized code for each
vendor (payer or provider).

Rather than write unmarshallers by hand, TigerShark includes tools for
generating a parser ("unmarshaller") and a set of class definitions.
These tools don't generate a complete, working application or complete
application components. They generate 80% of the needed code; some manual
tweaking is usually required to completely integrate the generated code into a
working application.

The unmarshaller parses an X12 message and locates Segments and Loops within
that message. This is used to build Plain Old Python Objects (POPO)
from the message.  Given a message as a POPO, processing is quite simple.

Also, the Segments can be persisted.  This requires that the message class
definitions must be part of an Object-Relational Mapping (ORM).

There are three sources for X12 message definitions, in addition to the
customer's Implementation Guide.

    -   The Python-based `PyX12`_ package. This package defines X12N messages using
        .xml files that are reasonably complete.

    ..  _`PyX12`: http://pyx12.sourceforge.net

    -   A Perl-based `X12-0.08`_ package. This package defines X12N messages
        using :file:`.cf` files, which have a format similar to :file:`.ini`
        files. These files provide just enough information to minimally parse a message.

    .. _`X12-0.08`: http://search.cpan.org/~prasad/X12-0.08/

    -   The SEF files, published by DISA. These files are the
        operating standard. However, they're hard to make direct use of.

Application-Level Processing
=============================

An X12 Message is what the application uses.  It's a collection
of X12 Segments.  The X12 Segments are
defined by the X12 standard and truly universal.

This leads to the following kind of architecture layers within the data model.

-   Application classes: these rely on access to X12Message objects.

-   X12Message classes: A message is a collection of Segment tokens;
    it can also be a container for loops, segments, composites and elements.

-   Segment Token: tokenized X12 text; this will contain composites and
    elements.

..  _`Database Design Alternatives`:

Database Design Alternatives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The database model should reflect a relatively complete view
of an X12 message.

Persistence Choices
======================

There are a number of choices for ways to create the relational database model.
These are based on the level of intepretation imposed by the database. The least
interpretation is persisting messages as Flat Text. A mid-level of
intepretation imposed by Segment-type Persistence. The most user-oriented design is
some kind of Application-based Persistence (i.e. Claim, Elgibility Request, etc.)

..  _`Metadata-based Design`:

Flat-Text Persistence
----------------------

One view is a flat list of the segements -- as text. The flat view
permits very easy unmarshalling, persistence and marshalling of messages.
However, a "flat list of segments" limits the changes that can be made
to a message. A flat structure means that the Loops are unknown; this means that
segments can't easily be added or removed.

The flat-text persistence requires extensive metadata to interpret
the text. That design stores Message identification and a flat list of
Segments in a single message table.

A metadata-based design, has a relatively simple data model with a few tables
that are heavily reused.

    -   Data Tables include ``X12Message``, ``X12Loop``, ``X12Segment`` which contain an
        instance of a message, and tie to the proper metadata elements to
        interpret the data.

    -   Metadata includes ``Message``, ``Loop``, ``Segment``, ``Composite`` and ``Element``
        definitions. These definitions allow us to unmarshall messages into
        database objects and unmarshall database objects into a working message.

A message Unmarshall and Load requires a message parser to unmarshall the source
message into a structure. The unmarshalled structure is then persisted with FK
references to the message definition.

All access and manipulation require that the ``Segment``, ``Composite`` and ``Element``
metadata be present to understand the content of a particular ``X12Element``. For
exammple finding the ``Element`` position from an element name requires the list of
``Elements`` in a ``Segment`` definition.

Marshalling a message requires the metadata definition -- to determine the order
of the ``Loop``\ s and ``Segment``\ s -- and then retrieving all of the related ``X12Message``,
``X12Loop`` and ``X12Segment`` objects. The objects can then be marshalled into a final
X12 output string.

The upside is that this is trivial to implement. It is independent of any
specific message or segment definition.

The downside of this is that the automatic Django Admin pages won't work. They
won't have field-by-field definitions of the Segments. It won't be possible to
provide interactive "touch-up" of an object (i.e. a Claim) without dynamically building pages
from the Segment definitions.

..  _`Segment-type Design`:

Segment-type Persistence
------------------------

A Segment-type design has a somewhat more complex data model with a larger
number of tables that are specific to each type of Segment.

    -   Generic Tables include ``X12Message``, ``X12Loop``, ``X12Segment`` will contain an
        instance of a message, and tie to the proper metadata elements to
        interpret the data. The ``X12Segment`` contains the original segment token,
        not the interpreted elements.

    -   Segment-type tables for all 57 types of segments. These type-specific
        segments are linked to the generic segment information, and provide the
        standard interpretation of the segment data.

The downside is that this is more complex to implement. It is requires
generating a large number of class definitions that match the segment-type
definitions. Howsever, these segment type definitions are standardized, and easy
to create with metadata tools.

The upside of this is that the automatic Django Admin pages work. They will have
field-by-field definitions of the Segments. However, the definitions will be
standards-based and not specific to a given customer.

Further, this design allows us to some flexibility customize the X12N messages
based on a customer's Implementation Guide.

Application-Based Persistence
------------------------------

An Application-Based design has tables with directly reflect the definition
of a application objects (e.g., Claim or Eligibility Request).

For example, this could include the following structures present on a Claim.

-    Billing Provider Name
-    Pay-To Provider Name
-    Subscriber Name
-    Patient Name
-    Patient Claim
-    Referring Provider Name
-    Rendering Provider Name
-    Submitter Name
-    Service Line
-    Service Line Adj
-    Service Provider Name
-    Attending Physician Provider
-    Operating Physician Provider

This is highly specific to Claim processing. While handy for
end-users, it requires a fair amount of care to translate between these
structures, ``X12Loops`` and the final, marshalled X12 message.


General Persistence Design
===============================

The best approach is the mid-level `Segment-type Design`_. This allows simple
presentation of details of claims. We have a few implementation decisions as a
consequence of chosing a Segment-type design.

In all cases, each "part" of the X12 message (Segment, Loop, etc.) is mapped to
a SQL table. Additionally, we must provide appropriate keys and occurance values
above and beyond the X12 Segment text.

ORM Details
================

There are several variations on ORM's, each of which has slightly different
implementation consequences.

    -   **Subclassing with Descriptors**. Django ORM is based directly on the Python classes; however,
        Django ORM requires that each persistent Segment-type-specific class be a
        subclass of ``django.db.models.Model``. This precludes other class
        hierarchies being part of the design.

    -   **Explicit Mappings**.  The SQLAlchemy ORM can have a
        Segment-type Python class hierarchy plus explicit mappings to SQL tables.

    -   **Decorators**.  An ORM may also have Python classes with some decorations
        to handle ORM mapping.

A consequence of using Segment-type design is that we have to persist a large
number of different segment types. (See Appendix I for a list of all 57 Segment
types used by ``837`` messages.) This exhaustive list of segment types is difficult
to produce by hand.

The conversion tools, then, must generate two features of an X12 message
processing module.

    -   Class definitions for the X12 message, segment, loop.

    -   Create a generic unmarshall class (and default object) for the given X12 message
        that handles the implied loop structure

    -   Create a template for each customer-specific **Factory** that plugs into
        the generic unmarshall class.

An additional feature is ORM support.  This can be one of the following:

    -   Particular Python class definition style (either subclassing with
        descriptors or decorators).

    -   Additional explicit mapping information.



Component Model
^^^^^^^^^^^^^^^

The component packaging is intended to follow a kind of
Model-Access-Presentation design pattern.
Most of these layers are outside TigerShark and are here to illustrate
the relationships.

    - **User Interface**.  A Web-based GUI, using Django templates, CSS, etc.  To
      an extent, the static content ("media") served by Apache is part of this package, also.

    - **Web Navigation**.  This is built from the Django URL and View components.
      The view functions makes use of the **Web Services** services
      to manipulate the **Domain Model** data.

    - **Web Services**.  Web Services, callable from client-site installed code.  This is built
      on the **Model**.  This is a kind of View of the underlying model.  These
      services are simple WSGI-enabled XML-RPC services.

    - **Access**.  This includes the ORM and RDBMS components that are outside
      a Django application.

    - **Domain Model**. The core objects: X12 structures and any
      application-specific structures
      that interpret those X12 structures.

The **Domain Model** decomposes into a number of packages. Both package trees must be
placed on the PYTHONPATH.

    -   ``X12``. This is a library package for handling the marshalling and
        unmarshalling of X12 messages.

        -   ``X12.parse`` This is the essential X12 parser. It depends on an X12
            message definition module
            which provides definitions of X12 message components.

            This requires a customer-specific **Factory**
            object that handles details of
            emitting proper objects.

        -   ``X12.map`` This is a package of utilities for mapping X12 message
            definitions to other structures like SQL tables.

        -   ``X12.message`` This package defines classes for X12 messages.

            This can be extended to
            include Object-Relational Mapping (ORM) definitions for SQLAlchemy
            or other ORM's, depending on what seems important.


        -   ``X12.tools`` This is a package of handy applications. This includes the
            following.

            -   ``convertPyX12`` Converts the XML definitions to ``X12.parse`` structures.

            -   ``surveyPyX12`` Parses all of the XML definitions to get a complete list
                of Segment types used by the various ``837`` messages.

When integrating this into a Django project, there will be
a number of applications.
Each application would have a ``models`` module with the Django version of
``X12.message``.
This would define the persistent DB structures for messages.

Processing Model
^^^^^^^^^^^^^^^^

There are several kinds of processing that are part of TigerShark.

-   `Manipulations`_ describes the application processing that is the end-user's view
    of the data.

-   `Meta-data`_ describes the developer's view; this is how messages are customized
    for each undividual customer.

Manipulations
=============

A number of use cases involve loading X12 messages, modifying X12 messages, and downloading
messages for further processing.

-   **Loading** decomposes into `Unmarshalling`_ the details from a text
    file, and then `Persisting`_ each segment of the message.

-   **Modifying** decomposes into `Presenting`_ a message, and
    `Persisting`_ those GUI changes into the database.

-   **Downloading** decomposes into `Querying`_ messages from the database,
    and then `Marshalling`_ those messages into a text file for the actual
    further processing.

Unmarshalling
-------------

See :ref:`unmarshall`.

An ``X12.parse.Message`` object handles unmarshalling text. The object is built from a Python
declaration.

The Python declaration itself can be persisted one of two ways:

    -   Stored in a Python module that imports ``X12.parse`` and builds the
        ``X12.parse.Message`` object.

    -   Stored in the database, by providing ORM definitions for ``X12.parse``
        objects.

Persisting
----------

See `Database Design Alternatives`_ for the global choices.

Having type-specific segments permits completely automatic generation of forms
for presentation.

Some bookkeeping is required to identify each instance of a message, and the
Segment instances which belong to the message. Since our goal is to leverage the
ORM layer, we include enough PK and FK information to locate the Message as a
whole, each Loop's position within the message, and each Segment's position
within a Loop.

Presenting
----------

A complex message (like a claim, ``837``) can't easily be presented.
Rather than attempt to present all Loops and Segments within a message, it might
be slightly simpler to present an indented outline of the Loop structure, with
each Segment containing an ``[Edit]`` and ``[Remove]`` button to alter the message
structure. Similarly, optional or repeating segments can have a ``[Add]``
placeholder inserted to permit adding segments.

::

    MSG ``837`` - Unique ID# - Test Case Id
    ISA LOOP
        ISA Segment           [edit]
        GS LOOP
            GS Segment        [edit]
            ST LOOP
                ST Segment    [edit]
                BHT Segment   [edit]
                Header
                Detail
                    LOOP 2000A
                        NM1   [edit]
                        N3    [edit]
                        N4    [edit]
                        HI    [add]
                Trailer
                SE Segment    [edit]
            GE Segment        [edit]
        IEA Segment           [edit]

The individual segments, on the other hand, are simple presentations of the
Elements in the segment mapped to HTML forms in the most direct manner.

Querying
--------

Generally, the common queries will be for collections of Messages based on test
cases, scenarios, versions, etc. Other use cases define a number of ways of
organizing messages.

Once a message collection has been identified, what remains is to find all
messages in that collection. Each message, in turn, is a collection of Loops and
Segments, based on the ``X12.message`` structures.

Marshalling
-----------

See :ref:`marshall`.

An ``X12.message.X12Message`` object handles marshalling. The structure is managed as
Message-Loop-Segment, with lower levels of detail collapsed into the Segment.
Each of these classes cooperates to produce a flat list of Segments in the
proper order. The Message's marshall method uses a simple recursive descent to
assemble a flat list of Segments which are encoded and emitted.

Meta-data
=========

There are two layers to the structure of an ``X12.parse`` object.

    -   The Message-Loop layer which shows the Message-Loop-Segment
        relationships. This is generic meta-data and applies to all messages of
        a given type. The top-level X12Message and X12Loop class definitions are
        adequate to persist this information.

    -   The Segment-Composite-Element layer which provides the data for each
        Segment of a message. There are a large number of subclasses of
        X12Segment, each of which has a unique combination of Elements.

A message parser object is created by a three-step process.

Parsing the XML version of the message definition to create a Python ``X12.parse``
object. This is done by a a ``ParserBuilder`` object which transforms the XML
message definition into the Python objects to parse an X12 message.

    1. Using the ``X12.map.source`` module to construct source for the message
    parser object. This is a object constructor for the ``X12.parse`` object. It is
    created by a kind of introspection of the message parser built in step (1),
    above.

    2. Using the ``X12.map.sa`` or ``X12.map.django`` module to construct the ``X12Segment``
    subclasses used by this message definition. This is a series of class
    definitions which extend ``X12.message.X12Segment`` and provide specific Element
    definitions. These are created by a kind of introspection of the message
    parser built in step (1), above.

    3. This message parser source built in step 2 becomes live code used to
    unmarshall X12 input files to create an ``X12.message`` object that can be
    persisted, modified, queried and unmarshalled.

The various ``X12Segment`` subclass definitions built in step 3 must be merged into
a composite data model to allow appropriate levels of reuse. Each of the 57
subclasses of ``X12Segment`` is simply a subclass of Segment, with a number of FK
relationships to Loop and some common attributes.

Appendix I
^^^^^^^^^^

The following table identifies the 57 distinct segment types and how they are
used. While this table is rather large, the entire set of Segment types can be
generated automatically as subtypes of ``X12.message.X12Segment``.

=== ==================================================================================
ID  Segment Types
=== ==================================================================================
AMT Patient Estimated Amount Due , Patient Paid Amount , Sales Tax Amount , Coordination of Benefits (COB) Patient Responsibility Amount , Coordination of Benefits (COB) Total Medicare Paid Amount , Coordination of Benefits (COB) Total Denied Amount , Coordination of Benefits (COB) Total Submitted Charges , Coordination of Benefits (COB) Total Allowed Amount , Facility Tax Amount , Coordination of Benefits (COB) Discount Amount , Coordination of Benefits (COB) Medicare B Trust Fund Paid Amount , Postage Claimed Amount , Service Tax Amount , Diagnostic Related Group (DRG) Outlier Amount , Coordination of Benefits (COB) Allowed Amount , Coordination of Benefits (COB) Covered Amount , Payer Prior Payment , Patient Amount Paid , Coordination of Benefits (COB) Medicare A Trust Fund Paid Amount , Coordination of Benefits (COB) Total Non-Covered Amount , Coordination of Benefits (COB) Tax Amount , Coordination of Benefits (COB) Approved Amount , Coordination of Benefits (COB) Patient Paid Amount , Coordination of Benefits (COB) Payer Paid Amount , Coordination of Benefits (COB) Per Day Limit Amount , Payer Estimated Amount Due , Coordination of Benefits (COB) Total Claim Before Taxes Amount , Credit/Debit Card - Maximum Amount , Medicare Paid Amount - 100% , Medicare Paid Amount - 80% , Total Purchased Service Amount , Approved Amount , Credit/Debit Card Maximum Amount
BHT Beginning of Hierarchical Transaction
CAS Claim Adjustment , Claim Level Adjustment , Line Adjustment , Service Line Adjustment , Claim Level Adjustments , Service Adjustment
CL1 Institutional Claim Code
CLM Claim Information
CN1 Contract Information
CR1 Ambulance Transport Information
CR2 Spinal Manipulation Service Information
CR3 Durable Medical Equipment Certification
CR5 Home Oxygen Therapy Information
CR6 Home Health Care Information
CR7 Home Health Care Plan Information
CRC EPSDT Referral , Home Health Activities Permitted , DMERC Condition Indicator , Homebound Indicator , Ambulance Certification , Hospice Employee Indicator , Home Health Functional Limitations , Patient Condition Information: Vision , Home Health Mental Status
CTP Drug Pricing
CUR Foreign Currency Information
DMG Subscriber Demographic Information , Patient Demographic Information , Other Insured Demographic Information , Other Subscriber Demographic Information
DN1 Orthodontic Total Months of Treatment
DN2 Tooth Status
DTP Service Line Date , Date - Onset of Current Symptom/Illness , Assessment Date , Claim Adjudication Date , Date - Last X-Ray , Date - Initial Treatment , Date - Acute Manifestation , Date - Last Certification Date , Date - Last Menstrual Period , Date - Date Last Seen , Date - Disability Begin , Date - Appliance Placement , Date - Test , Date - Assumed and Relinquished Care Dates , Line Adjudication Date , Claim Paid Date , Date - Authorized Return to Work , Date - Last Worked , Date - Oxygen Saturation/Arterial Blood Gas Test , Date - Shipped , Date - Similar Illness/Symptom Onset , Service Adjudication Date , Date - Referral , Date - Service , Date - Service Date , Date - Prior Placement , Date - Disability End , Date - Begin Therapy Date , Date - Replacement , Date - Accident , Date - Discharge , Date - Certification Revision Date , Date - Last X-ray , Statement Dates , Admission Date/Hour , Date - Admission , Date - Hearing and Vision Prescription Date , Date - Onset of Current Illness/Symptom , Discharge Hour
FRM Supporting Documentation
GE  Functional Group Trailer
GS  Functional Group Header
HCP Claim Pricing/Repricing Information , Line Pricing/Repricing Information
HI  Other Diagnosis Information , Value Information , Occurrence Span Information , Health Care Diagnosis Code , Condition Information , Principal, Admitting, E-Code and Patient Reason for Visit Diagnosis Information , Principal Procedure Information , Diagnosis Related Group (DRG) Information , Treatment Code Information , Other Procedure Information , Occurrence Information
HL  Subscriber Hierarchical Level , Patient Hierarchical Level , Billing/Pay-To Provider Hierarchical Level
HSD Health Care Services Delivery
IEA Interchange Control Trailer
ISA Interchange Control Header
K3  File Information
LIN Drug Identification
LQ  Form Identification Code
LX  Service Line , Line Counter , Service Line Number
MEA Test Result
MIA Medicare Inpatient Adjudication Information
MOA Medicare Outpatient Adjudication Information
N3  Other Subscriber Address , Destination Payer Address , Service Facility Address , Responsible Party Address , Ordering Provider Address , Pay-To Provider's Address , Pay-To Provider Address , Other Payer Address , Subscriber Address , Billing Provider Address , Service Facility Location Address , Patient Address , Payer Address
N4  Payer City/State/ZIP Code , Patient City/State/ZIP Code , Billing Provider City/State/ZIP Code , Pay-To Provider City/State/ZIP , Pay-To Provider City/State/ZIP Code , Other Subscriber City/State/ZIP Code , Service Facility Location City/State/ZIP , Service Facility City/State/Zip Code , Responsible Party City/State/ZIP Code , Destination Payer City/State/ZIP Code , Ordering Provider City/State/ZIP Code , Other Payer City/State/ZIP Code , Subscriber City/State/ZIP Code
NM1 Credit/Debit Card Holder Name , Submitter Name , Other Payer Service Facility Location , Ordering Provider Name , Other Subscriber Name , Operating Physician Name , Destination Payer Name , Other Payer Attending Provider , Other Payer Service Facility Provider , Attending Physician Name , Responsible Party Name , Receiver Name , Assistant Surgeon Name , Supervising Provider Name , Pay-To Provider's Name , Service Facility Location , Purchased Service Provider Name , Referring Provider Name , Service Facility Name , Patient Name , Other Payer Other Provider , Subscriber Name , Other Payer Rendering Provider , Other Payer Referring Provider , Other Payer Prior Authorization or Referral Number , Pay-To Provider Name , Other Payer Name , Rendering Provider Name , Billing Provider Name , Other Provider Name , Payer Name , Credit/Debit Card Account Holder Name , Other Payer Supervising Provider , Other Payer Operating Provider , Other Payer Purchased Service Provider , Other Payer Patient Information
NTE Claim Note , Line Note , Billing Note
OI  Other Insurance Coverage Information
PAT Patient Information
PER Ordering Provider Contact Information , Billing Provider Contact Information , Other Payer Contact Information , Submitter Contact Information , Submitter EDI Contact Information
PRV Billing/Pay-To Provider Specialty Information , Service Facility Specialty Information , Referring Provider Specialty Information , Assistant Surgeon Specialty Information , Rendering Provider Specialty Information , Attending Physician Specialty Information , Other Provider Specialty Information , Operating Physician Specialty Information
PS1 Purchased Service Information
PWK Line Supplemental Information , DMERC CMN Indicator , Claim Supplemental Information
QTY Anesthesia Quantity , Claim Quantity
REF Repriced Claim Number , Pay-To Provider Secondary Identification Number , Rendering Provider Secondary Identification , Original Reference Number (ICN/DCN) , Service Facility Location Secondary Identification , Repriced Line Item Reference Number , Mammography Certification Number , Ordering Provider Secondary Identification , Assistant Surgeon Secondary Identification , Other Payer Supervising Provider Identification , Prescription Number , Claim Identification Number For Clearinghouses and Other Transmission Intermediaries , Other Provider Secondary Identification , Other Subscriber Secondary Identification , Payer Secondary Identification Number , Prior Authorization or Referral Number , Other Payer Referring Provider Identification , Investigational Device Exemption Number , Document Identification Code , Service Facility Secondary Identification , Immunization Batch Number , Line Item Control Number , Attending Physician Secondary Identification , Other Payer Patient Identification , Destination Payer Secondary Identification , Property and Casualty Claim Number , Purchased Service Provider Secondary Identification , Other Payer Service Facility Location Identification , Demonstration Project Identifier , Claim Identification Number for Clearing Houses and Other Transmission Intermediaries , Clinical Laboratory Improvement Amendment (CLIA) Identification , Medical Record Number , Billing Provider Secondary Identification Number , Pay-To Provider Secondary Identification , Transmission Type Identification , Other Payer Purchased Service Provider Identification , Referring Clinical Laboratory Improvement Amendment (CLIA) Facility Identification , Mandatory Medicare (Section 4081) Crossover Indicator , Other Payer Rendering Provider Secondary Identification , Adjusted Repriced Claim Number , Operating Physician Secondary Identification , Peer Review Organization (PRO) Approval Number , Supervising Provider Secondary Identification , Transaction Type Identification , Other Payer Operating Provider Identification , Other Payer Rendering Provider Identification , Other Payer Claim Adjustment Indicator , Subscriber Secondary Identification , Ambulatory Patient Group (APG) , Oxygen Flow Rate , Other Subscriber Secondary Information , Other Payer Secondary Identifier , Other Payer Prior Authorization or Referral Number , Other Payer Attending Provider Identification , Other Payer Service Facility Provider Identification , Universal Product Number (UPN) , Service Predetermination Identification , Billing Provider Secondary Identification , Other Payer Secondary Identification and Reference Number , Predetermination Identification , Adjusted Repriced Line Item Reference Number , Credit/Debit Card Billing Information , Referring Provider Secondary Identification , Payer Secondary Identification , Patient Secondary Identification , Claim Identification Number for Clearinghouses and Other Transmission Intermediaries , Other Payer Other Provider Identification , Claim Submitter Credit/Debit Card Information , Other Payer identification Number , Service Authorization Exception Code , Patient Secondary Identification Number , Credit/Debit Card Information , Clinical Laboratory Improvement Amendment (CLIA) Number
SBR Subscriber Information , Other Subscriber Information
SE  Transaction Set Trailer
ST  Transaction Set Header
SV1 Professional Service
SV2 Institutional Service Line
SV3 Dental Service
SV5 Durable Medical Equipment Service
SVD Line Adjudication Information , Service Line Adjudication Information
TA1 Interchange Acknowledgement
TOO Tooth Information
=== ==================================================================================
