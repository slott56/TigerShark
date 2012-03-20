"""This sample web site shows an approach to integrating X12 message
processing with Django applications.

web.claims
============

This application uses an application-specific claim definition.
The definition is entirely developed "by hand" and represents some
specific use cases.

..  automodule:: web.claims
    :members:
    
web.claims_837
==============

This application uses an 837 parser built by :mod:`tools.convertPyX12`.
This conversion creates the Django models so that more generic claims
processing can be performed.

..  automodule:: web.claims_837
    :members:
    
web.make837
=============

Converts the :samp:`837` claim message definitions into Python parsers
and Django ORM structures to define the :mod:`web.claims_837.models`
classes.

..  automodule:: web.make837
    :members:

"""
