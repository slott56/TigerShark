.. Tiger documentation master file, created by
   sphinx-quickstart on Wed Dec 07 18:25:14 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tiger Shark X12 Tools
=================================

TigerShark handles semantically rich storage and modification of X12 formatted
data using Python objects.
This can be used for various EDI purposes, including medical claims
(837) and eligibility (270).

This package helps to create Plain Old Python Objects (POPO) which contain
X12 structures.  No intermediate XML or other notation is used.
This can simplify X12 message parsing because the resulting structure is a Python object.

Additionally, JSON Schema definitions can be created
to describe the X12 messages for processing outside EDI software.
This can provide a handy representation for X12 data that can be processed by a wide variety of tools.

..  toctree::
    :maxdepth: 2

    operation
    usecase
    architecture
    design/index
    implementation/index
    todo
    
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

