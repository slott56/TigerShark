#!/usr/bin/env python2.6
"""
Unit test of web.claims application as a complete Django WSGI web service.
"""
from __future__ import print_function
import unittest
import httplib
import urllib2, urllib
import logging, sys
import os.path
import datetime
import base64
import subprocess, time
import json

logger= logging.getLogger( __file__ )

class TestWS( unittest.TestCase ):
    """Exercise load and fetch operations.

    The tests must be run in order to force the expected behavior.
    """
    def setUp( self ):
        self.claimDict= {
            'GWID':'06E266185200',
            'CLAIM-ID':'22559311',
            'BENEFIT':'CHRC',
            'TYPE-OF-SERVICE':'CI',
            'LOCATION':'ALB',
            'TYPE':'P',
            'SECONDARY':'M',
            'GENDER':'U',
            'AGE-FROM':'0',
            'AGE-TO':'125',
            'CLAIM-FILE': os.path.join("test","837-example.txt"),
        }
        with open( self.claimDict['CLAIM-FILE'],"rU" ) as claims:
            self.claimText= "".join(x.strip() for x in claims)
        self.headers={'Authorization':'BASIC '+base64.encodestring("admin:admin")[:-1]}
        self.client= httplib.HTTPConnection( 'localhost', 18000 )
    def test_01_Load( self ):
        # Build Properties dict
        row= self.claimDict
        propCols= ( "BENEFIT", "TYPE-OF-SERVICE", "LOCATION", "TYPE", "SECONDARY" )
        properties= dict( [ (k,row[k]) for k in propCols ] )
        prop_json= json.dumps( properties )
        # Build Constraints dict
        consCols= ( "GENDER", "AGE-FROM", "AGE-TO" )
        constraints= dict( [ (k,row[k]) for k in consCols ] )
        cons_json= json.dumps( constraints )
        # load claims
        claimId= row["CLAIM-ID"]
        params= urllib.urlencode({'claim':self.claimText, 'claim_id':claimId,
                    'properties':prop_json, 'constraints':cons_json})
        self.client.request( 'POST', "/claim/load/", body=params, headers=self.headers)
        response= self.client.getresponse()
        result= response.read()
        #print( result )
        self.client.close()
        self.assertEquals( "CREATED", response.reason )
        object= json.loads(result)
        self.assertEquals( claimId, object['claim_id'] )
    def test_02_Fetch( self ):
        claimId= self.claimDict["CLAIM-ID"]
        self.client.request( 'GET', "/claim/{0}/".format(claimId), headers=self.headers )
        response= self.client.getresponse()
        result= response.read()
        self.client.close()
        object= json.loads(result)
        self.assertEquals( "OK", response.reason )
        self.assertEquals( self.claimText, object['claim'] )
    def test_03_Fetch( self ):
        claimId= '837_example'
        self.client.request( 'GET', "/claim_837/{0}/".format(claimId), headers=self.headers )
        response= self.client.getresponse()
        result= response.read()
        self.client.close()
        object= json.loads(result)
        #print( result )
        self.assertEquals( "OK", response.reason )
        print( object['claim'] )

def setUpModule():
    """Spawn the test server process.
    This should build a test database, load fixtures, and then provide
    the Django-based services.
    """
    global the_proc, the_log, the_err

    command= ["/Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6", "-m", "web.manage", "testserver",
              '--addrport=18000', '--settings=web.settings',
              '--noinput', '--verbosity=1',
              'example837.json',
              ]
    log_file= 'testserver.log'
    err_file= 'testserver.err'

    logger.info( '{0} >{1} 2>{2}'.format( ' '.join( command ), log_file, err_file ) )
    the_log= open( log_file, 'w', 0 )
    the_err= open( err_file, 'w', 0 )
    the_proc = subprocess.Popen(command, shell=False, stdout=the_log, stderr=the_err)
    time.sleep(6) # Wait for fixtures to load
    status= the_proc.poll()
    logger.info( 'PID %d, status %r', the_proc.pid, status )

    logger.info( datetime.datetime.now() )

def tearDownModule():
    """Kill the server process."""
    global the_proc
    logger.info( "Stopping server" )
    the_proc.kill()
    logger.debug( "Waiting for %d to finally exit", the_proc.pid )
    the_proc.wait()
    logger.info( "PID %d, status %r", the_proc.pid, the_proc.returncode )
    the_log.close()
    the_err.close()
    for f, p in (the_log, 'log>'), (the_err, 'err>'):
        print()
        with open( f.name, 'r' ) as source:
            for line in source:
                print( p, line, end='' )
        print()

if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.DEBUG,
    )
    
    if sys.version_info[:2] <= ( 2, 6 ):
        #Python2.6 work-around
        setUpModule()
        tests= unittest.defaultTestLoader.loadTestsFromModule(__import__('__main__'))
        result= unittest.TextTestRunner().run( tests )
        tearDownModule()
        sys.exit(not result.wasSuccessful())

    #Python2.7
    unittest.main()

