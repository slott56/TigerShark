#!/usr/bin/env python
"""Create the Initial Data fixture from SQL statements.

The :file:`claims/SQL` directory contains the SQL required to populate
the database.

This is used to create the :file:`claims/fixtures/initial_data.json` file.
"""
import logging
import sys
import os.path

from django.core.management import call_command

def make_fixture():
    call_command("syncdb", interactive=False, database='wstest')
    call_command("sqlcustom", "claims", database='wstest')
    result= os.path.join('web','claims','fixtures','initial_data.json')
    with open(result,'w') as target:
        sys.stdout= target
        call_command("dumpdata", "claims", indent=2, database='wstest')
        sys.stdout= sys.__stdout__

if __name__ == "__main__":
    make_fixture()