#!/usr/bin/env python
"""Batch Load Claims Messages associated with Classification plus Automod Parameters.

Synopsis
========

:samp:`load.py {description.csv}...`

Description
===========

Reads the CSV-format descriptions, either from stdin or files supplied as command-line
arguments.  Each file contains rows which provide three separate things:

    - name of a file with claim(s) to parse (or the claim itself),

    - classification parameters for the claims,

    - automod constraints for the claims *[XXX this may be derivable from the claim]*.

This program calls the claim load service, and writes a log of success
and failures.

Before this program can be run, an extract must be used to get the X12N claims
out of the source application's HIPAA gateway.  The extract process uses a
request ``.csv`` file, and writes the X12N files, plus the description ``.csv`` file.

The typical use case for this loader is as follows::

    claimExtract request.csv | load.py

Options
=======

    :file:`*description.csv`* a CSV-format files which identifies claims to load.
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

    -   :samp:`BENEFIT` The Benefit ID to assign to this claim.  This is checked against the
        TOS/Benefit list.

    -   :samp:`TYPE-OF-SERVICE` The Type of Service ID to assign to this claim.  This is checked against the
        TOS/Benefit list.

    -   :samp:`LOCATION` The codes are ALB, BUF, CE and CW.
        Descriptions are Albany, Buffalo, Central NY West, and Central NY East.

    -   :samp:`TYPE` The codes are I, P, O or D.
        Descriptions are In-Patient, Professional, Out-Patient and Dental.

    -   :samp:`SECONDARY`  The codes are M and R.
        Descriptions are Medicare and Regular.

    -   :samp:`GENDER` This is used to define an automod constraint.
        Codes are M, F and U.

    -   :samp:`AGE-FROM` This is used to define an automod constraint.

    -   :samp:`AGE-TO` This is used to define an automod constraint.

    -   :samp:`CLAIM-FILE` If present, this is the file that contains the X12 message for this claim.
        If omitted, the `CLAIM-TEXT` column must be used to provide
        the actual X12N message.

    -   :samp:`CLAIM-TEXT` If present, this is the text of the X12 message for this claim.
        If omitted, the `CLAIM-FILE` column must be used to provide the
        name of a file with the actual X12N message.

Other columns are permitted in this file.  They are ignored. For example, the following
additional column is often used.

    -   :samp:`GWID`  This is the HIPAA Gateway Transaction ID for the claim, used to retrieve it
        from FACETS.
"""
import X12.file
import logging, sys
import xmlrpclib
import csv

wsClaims= xmlrpclib.ServerProxy( "http://slott:slott@localhost:18000/RPC2/claim", allow_none=True )

def loadClaims( claimIter, claimId, properties=None, constraints=None ):
    """Load a collection of claims, all of which have a common set of properties
    and automod constraints.
    
    :param claimIter: An iterator over some claims, a list or a file will work.
        Often an :mod:`X12.file` is used because it streamlines the file reading.
    :param claimId: The base claim id.  If multiple claims are loaded, then
        claims after the first will have "-*n*" appended to the claim id string.
    :param properties: A dict with Claim Properties.
    :param constraints: A dict with Automod constraints.
    """
    log= logging.getLogger( "web.claims_837.loadClaims" )
    count= 0
    good= 0
    error= 0
    id= claimId
    for claim in claimIter:
        count += 1
        log.info( "Parsing claim %d", count )
        try:
            status= wsClaims.load( claim, id, properties, constraints )
            if status[0] == "OK":
                good += 1
            else:
                log.error( status )
                error += 1
        except xmlrpclib.ProtocolError, e:
            log.error( str(e) )
            error += 1
        id= "%s-%d" % ( claimId, count )
    log.info( "Count %d", count )
    log.info( "Good  %d", good )
    log.info( "Error %d", error )

def loadClaimAndDescription( csvFile ):
    """Load a set of claims provided in a CSV-format file.
    Each row of the CSV file describes one (rarely multiple) claim.
    It provides a complete set of Properties and AutomodConstraints for
    the claim.

    :param csvFile: an open file (or file-like object) that can be used
        by csv.DictReader to get claims, properties and constraints.
    """
    log= logging.getLogger( "web.claims_837.loadClaimAndDescription" )
    csvReader= csv.DictReader( csvFile )
    for row in csvReader:
        # If Claim Text: put this in a simple list
        if row.has_key("CLAIM-TEXT") and row["CLAIM-TEXT"] is not None:
            claims= [ row["CLAIM-TEXT"] ]
        # elif Claim File: use X12.file to read the file
        elif row.has_key("CLAIM-FILE") and row["CLAIM-FILE"] is not None:
            claims= X12.file.genClaims( row["CLAIM-FILE"] )
        # else: log a warning -- no claim present
        else:
            log.warning( "Row %r has no claim" % ( row, ) )
            continue
        # Build Properties dict
        propCols= ( "BENEFIT", "TYPE-OF-SERVICE", "LOCATION", "TYPE", "SECONDARY" )
        properties= dict( [ (k,row[k]) for k in propCols ] )
        # Build Constraints dict
        consCols= ( "GENDER", "AGE-FROM", "AGE-TO" )
        constraints= dict( [ (k,row[k]) for k in consCols ] )
        # load claims
        claimId= row["CLAIM-ID"]
        loadClaims( claims, claimId, properties, constraints )

if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr, level=logging.INFO )
    #loadClaims( X12.file.genClaims(r"..\..\test\837-example.txt") )
    #loadClaims( X12.file.genClaims(r"..\..\test\837I-Examples.txt") )
    with open(r"..\..\test\test_description.csv","rb") as claims:
        loadClaimAndDescription( claims )
