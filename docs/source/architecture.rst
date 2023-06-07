..  _architecture:

########################################
Architecture and Design
########################################

C4 suggests we look at Context, Container, Component, Code.
(See https://c4model.com).
For more information on the Context, see :ref:`context`.

This chapter provides an `Architecture Summary`_ with an overview of the
architectural principles.

The `Container View`_ is pretty small. This is a simple set of applications to run on a desktop computer.

The `Component View`_ section provides an overview of the package structure
underlying the application software.

The `Processing Model`_ section provides an overview of the various kinds of processing that occur.

The `Dependencies`_ section identifies an important implementation dependency: the PyX12 project.

`Appendix: Segments`_ contains the 57 distinct segment types.

The details of Code are covered in :ref:`design`.

Architecture Summary
^^^^^^^^^^^^^^^^^^^^

There are two distinct "levels" or "views" to this application.

:Developer:
    These are the tools to create and test the message class definitions.
    This defines X12 message types as Plain Old Python Object (POPO) classes.

:Application:
    A message is implemented as class in a module.
    The class is used to load and dump (other terms are parse/unparse, deserialize/serialize, unmarshall/marshall) the text of messages in a variety of formats.

The most common use case is loading an  "exchange" format message to create Python objects.
From here, Python to JSON conversions can persist an easy-to-use copy of the message.

Developer's Perspective
=======================

An X12 message has a complicated structure of loops, segments, composites and elements.
This is reflected in the message type definition,
which depends on loop, segment, and composite definitions.

There are several layers in the interpretation of a message:

1.  Exchange Format. This is a big block of text, sometimes with additional ``\n`` inserted after each segment separator.

2.  X12 Segment Format. The segment separator can be used to decompose the exchange format into
    a sequence of segments. Each segment is a sequence of element and composite values.
    Note that the loop structure is not an explicit part of this representation.

3.  The application's view of a Message that may be a Claim or Eligibility Request.
    This is a Python object definition that reflects the
    loops, segments, composites, and elements of the message.

It's common practice to define common sets of code values,
and common data types outside the messages. This is reflected
in a :py:mod:`x12.common` module with these definitions.

See :ref:`design.class` and :ref:`design.parsing` for more on solutions.

X12 Message Definitions
-----------------------

The X12 standard is defined via :file:`.SEF` files; additional
meta-definitions are used to manage the exchange of messages,
versioning, and other considerations.
These files are proprietary, and not freely available.

There are two sources for X12 message definitions, in addition to the
customer's Implementation Guide.

-   The Python-based `PyX12`_ package. This package defines X12 messages using
    ``.xml`` files that seem to be reasonably complete.

..  _`PyX12`: https://github.com/azoner/pyx12

-   The .SEF files. These seem to be a proprietary product of TIBCO.

The TigerShark :py:mod:`tools.xml_extract` tool can transform the ``.xml`` files
into Python class definitions.
A class definition can emit JSON Schema for messages of that class.


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

Container View
^^^^^^^^^^^^^^^

The applications are more-or-less a single container applications.
The :py:mod:`tools.xml_extract` reads XML definitions and creates
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

See :ref:`unmarshall`.

An message class has a :meth:`parse` method for loading (or deserializing or parsing) text to create Plain Old Python Objects.

Dumping
===========

See :ref:`marshall`.

Each Message object handles serialization into X12 text
or JSON.
A :meth:`dump` method emits the content in X12 "exchange format".
A :meth:`json` method emits the content in JSON notation.

JSON Schema
===========

The ``tools/xml_extract.py`` application, specifically,
reads XML files from the PyX12 project and creates modules with Python class definitions.
The Python can be used to build JSON Schema definitions.

The JSON Schema description of a message can be defined as

::

    some_message:
        type: object
        properties:
            loop1:
                $ref: #/$loops/loop1
            loop2:
                $ref: #/$loops/loop2

A loop can refer to segments using a more complex path

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

The ordinary nesting of referenced elements assures
the distinct definitions of a reused segment.

The JSON Schema representation of the message
definitions is handled via a large number of "$ref" references
from the overall structure to the definitions of loops, segements,
composites, elements, codes, and data element definitions.

The idea is that an overall message is generally
defined as follows:

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
It provides a loop namespace to disambiguate segments,
and their composites and elements.

Currently, the internal message classes
can be turned into JSON Schema.
The :py:func:`base.schema` function does *not* structure
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

Appendix: Segments
^^^^^^^^^^^^^^^^^^^

The following table identifies the 57 distinct segment ID's and how they are
used. When a segment ID has a list of segment types that indicates that the
segment appears in a number of distinct loops, often within a single message.

The worst case is the ``REF`` segment, which is used in a vast number of distinct loops and messages.

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
