#!/usr/bin/env python
"""Create the Claims fixture from sample claim messages.

The :file:`test...` file contains sample claims to populate
the database.

This is used to create the :file:`claims/fixtures/example837.json` file.
"""
import logging
import sys
import os.path

from django.core.management import call_command

from web.claims_837.models import Factory
from web.claims_837.parse import parse_837p

def make_fixture():
    call_command("syncdb", interactive=False, database='wstest')

    sample= os.path.join("test","837-example.txt")
    with open( sample, "rU" ) as claims:
        claimText= "".join( x.strip() for x in claims )
    msg= parse_837p.unmarshall( claimText, Factory )
    msg.name= '837_example'
    msg.save( using='wstest' )

    result= os.path.join('web','claims_837','fixtures','example837.json')
    with open(result,'w') as target:
        sys.stdout= target
        call_command("dumpdata", "claims", "claims_837", indent=2, database='wstest')
        sys.stdout= sys.__stdout__

if __name__ == "__main__":
    make_fixture()