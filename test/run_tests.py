#!/usr/bin/env python
"""Test Driver runs all discoverable unit tests.

Synopsis
========

:samp:`python -m test.run_tests`

Description
===========

    Traverses the directory structure looking for test modules.
    All Django tests are descendants of the :mod:`web` subdirectory.
    All POP and WS tests are descendants of the :mod:`test` subdirectory.

Options
=======

    None.

Environment Variables
=====================

    :envvar:`PYTHONPATH` must encompass the entire TigerShark directory tree.

    :envvar:`DJANGO_SETTINGS_MODULE` points to `web.settings`.


Notes
=====

There are three kinds of tests:

    -   Django unit tests.  These must be run with :samp:`manage.py test`
        or equivalent.  This driver does not spawn subprocesses for testing
        (it probably should) but uses :func:`call_command`.

    -   Plain Old Python (POP) unit tests.  These can be run with the
        standard test runner.  Some will require the Django DB environment,
        which will be set up and torn down as needed.

    -   Web Services tests.  These require that the WS be started and stopped.
        These tests will spawn the Django test server.

The suites of tests reuse a single database.  A tearDown to remove
rows is important.

"""
import os
from django.core.management import call_command
import fnmatch
import unittest
import logging, sys
import glob

logger= logging.getLogger( __name__ )

def djangoRunner( rootDir ):
    """Locates and runs all Django applications with tests."""
    def modules():
        for mod_name in "tests.py", "models.py":
            for full_name in glob.glob( os.path.join( "web","*","tests.py") ):
                path_app, module = os.path.split( full_name )
                path, app = os.path.split( path_app )
                yield app
    app_list= list(sorted(set(modules())))
    logger.info( "manage.py test {0}".format( ' '.join(app_list) ) )
    call_command( 'test', *app_list )

def popRunner( rootDir ):
    """Locates and runs all Plain-Old Python tests.

    For Python 2.6, this doesn't properly process the test_wsClaims
    module.  That can be tested manually.
    """
    testRoot= os.path.join( rootDir, "test" )
    topSuite= unittest.TestSuite()
    for path,dirList,fileList in os.walk( testRoot, topdown=True ):
        for f in fileList:
            if fnmatch.fnmatch( f, "test_*.py" ):
                logger.info( "python %s", f )
                name, ext = os.path.splitext( f )
                suite= unittest.defaultTestLoader.loadTestsFromName( "test.%s" % (name,) )
                topSuite.addTest( suite )
    testRunner = unittest.TextTestRunner()
    result = testRunner.run(topSuite)

if __name__ == "__main__":
    rootDir= "."
    logging.basicConfig( stream=sys.stderr, level=logging.INFO )
    djangoRunner( rootDir )
    popRunner( rootDir )
    logging.shutdown()