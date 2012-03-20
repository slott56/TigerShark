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

There is a preparation step where Python class definitions and a Factory
are built from X12 message definition XML's.  This is the only use for XML.

Once the Python class definitions are built for a message,
the Factory is used to populate instances of the class definitions
from an X12 message.
This is the unmarshalling process.  The factory is also used to marshall
a Python structure into an X12 message.
