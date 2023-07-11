.. Tiger documentation master file, created by
   sphinx-quickstart on Wed Dec 07 18:25:14 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tiger Shark X12 Tools
=================================

TigerShark handles semantically rich storage and processing of X12 formatted
data by converting wire format message text to Python objects.
This can be used for various EDI purposes, including gathering
data on medical claims (837) and eligibility (270).

This package helps to create Plain Old Python Objects (POPO) from X12 messages.
No intermediate XML or other notation is used.
This can simplify X12 message processing.

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
    appendices/index
    
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

