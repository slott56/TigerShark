#!/usr/bin/env python
"""Batch Fetch Claims Messages.

Synopsis
========

:samp:`fetch.py {description.csv}...`

Description
===========

Reads the CSV-format descriptions, either from stdin or files supplied as command-line
arguments.  Each file contains rows which provide the claim identifiers.  Other
attributes are silently ignored.

This program calls the claim fetch service, and writes a log of success
and failures.

Options
=======

    :file:`*description.csv`* a CSV-format files which identifies claims to fetch.
    If omitted, :file:`stdin` is read.

Environment Variables
=====================

    :envvar:`DJANGO_SETTINGS_MODULE` is the Django Settings Module that defines the
    database and other runtime environment parameters.

CSV FILE FORMAT
===============

The claim description file has the following format.  Either the columns MUST be in
the following order, or the first row MUST have these column titles.

    -   :samp:`CLAIM-ID`.  This is the unique claim ID which will be assigned.

    Other columns are permitted in this file.  They are ignored. For example, the following
    additional column is often used.

    -   :samp:`GWID`  This is the HIPAA Gateway Transaction ID for the claim, used to retrieve it
        from FACETS.
"""
from __future__ import print_function
import X12.file
import logging, sys
import xmlrpclib
import csv

wsClaims= xmlrpclib.ServerProxy( "http://slott:slott@localhost:18000/RPC2/claim", allow_none=True )
wsAutomod= xmlrpclib.ServerProxy( "http://slott:slott@localhost:18000/RPC2/automod", allow_none=True )

def fetchClaims( csvFile ):
    log= logging.getLogger( "web.claims_837.fetchClaims" )
    csvReader= csv.DictReader( csvFile )
    for row in csvReader:
        claimId= row["CLAIM-ID"]
        try:
            status, claim = wsClaims.fetch( claimId )
            if status == "OK":
                print( claim )
            else:
                print( "***", claim )
        except xmlrpclib.ProtocolError, e:
            print( e )
            print( "*** Could not fetch", claimId )

def getCounts( csvFile ):
    log= logging.getLogger( "web.claims_837.getCounts" )
    csvReader= csv.DictReader( csvFile )
    for row in csvReader:
        status, counts = wsAutomod.getCounts(
            row["LOCATION"], row["TYPE"],
            row["BENEFIT"], row["TYPE-OF-SERVICE"], "Base" )
        if status != "OK":
            print( "***", counts )
            continue
        for prop, count in counts:
            status, claims = wsAutomod.mod( prop, "" )
            print( status, map( str, claims ) )

if __name__ == "__main__":
    with open(r"..\..\test\test_description.csv","rb") as claims:
        #fetchClaims( claims )
        getCounts( claims )
