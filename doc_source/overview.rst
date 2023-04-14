##############
Overview
##############

TigerShark handles efficient storage and modification of X12 formatted
data using Python objects.
This can be used for various EDI purposes, including medical claims
(837) and eligibility (270).

This package helps to create Plain Old Python Objects (POPO) which contain
to X12 structures.  No intermediate XML or other notation is used.
This can speed X12 message unmarshalling and
marshalling because the definitions are handled directly as Python objects.
It simplifies processing X12 messages because
XPATH-like segment location is replaced with Python attribute
navigation.

Additionally, JSON Schema definitions are used
to describe the X12 messages. This can provide
a handy non-Python representation for X12 data.
It tends to preserve the Loop/Segment/Composite structure,
by adding some punctuation.
