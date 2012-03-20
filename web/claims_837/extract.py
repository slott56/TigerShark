#!/usr/bin/env python
"""Extract Claims Messages.

Synopsis
========

:samp:`extract.py {description.csv}...`

Description
===========

Options
=======

Environment Variables
=====================

    :samp:`DJANGO_SETTINGS_MODULE` is the Django Settings Module that defines the
    database and other runtime environment parameters.
"""
from __future__ import print_function
from web.claims.models import X12Message
import logging, sys

def fetchClaims( ):
    for claim in X12Message.objects.all():
        print( claim.marshall() )
        print()

if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr, level=logging.INFO )
    fetchClaims( )
