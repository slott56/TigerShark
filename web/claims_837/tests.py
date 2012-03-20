#!/usr/bin/env python
"""Unit tests for the web.claims_837 application.
"""
from __future__ import print_function
from  django.test import TestCase
import logging, sys
import os.path
import json

from X12.parse import SegmentToken, ParseError
from web.claims.models import X12Segment, X12Loop, X12Message
from web.claims_837.models import Factory
from parse import parse_837p, parse_837d, parse_837i

logging.basicConfig( stream=sys.stderr, level=logging.INFO )

class ParseTest( TestCase ):
    def setUp( self ):
        with open( os.path.join("test","837-example.txt"),"r") as example:
            some837Lines= [ l.strip() for l in example.readlines() ]
        self.some837= "".join( some837Lines )
    def tearDown( self ):
        X12Segment.objects.all().delete()
        X12Loop.objects.all().delete()
        X12Message.objects.all().delete()
    def test837p( self ):
        try:
            msg= parse_837p.unmarshall( self.some837 )
        except ParseError, e:
            print( '***', e )
            self.fail( "Claim is supposed to be 837-Professional")
        st= msg.descendant( 'SEGMENT', 'ST' )
        #print( 'Message Type', map( str, st ) )
        self.assertEquals( "837", st[0].getByPos(1) )
        st_loop= msg.descendant( 'LOOP', 'ST_LOOP' )[0]
        header= st_loop.child( 'LOOP', 'HEADER' )[0]
        bht= header.child( 'SEGMENT', 'BHT' )
        #print( 'Beginning of Hierarchical Transaction', map( str, bht ) )
        ref= header.child( 'SEGMENT', 'REF' )
        #print( 'Transmission Type Identification', map( str, ref ) )
        self.assertEquals( "004010X098A1", ref[0].getByPos(2) )
    def test837i( self ):
        try:
            msg= parse_837i.unmarshall( self.some837 )
            self.fail("Claim wrongly matched 837-Institutional")
        except ParseError, e:
            print( 'Expected:', e )
    def test837d( self ):
        try:
            msg= parse_837d.unmarshall( self.some837 )
            self.fail( "Claim wrongly matched 837-Dental")
        except ParseError, e:
            print( 'Expected:', e )

class PersistTest( TestCase ):
    def setUp( self ):
        with open( os.path.join("test","837-example.txt"),"r") as example:
            some837Lines= [ l.strip() for l in example.readlines() ]
        self.some837= "".join( some837Lines )
    def tearDown( self ):
        X12Segment.objects.all().delete()
        X12Loop.objects.all().delete()
        X12Message.objects.all().delete()
    def testPersist837p( self ):
        try:
            msg= parse_837p.unmarshall( self.some837, Factory )
        except ParseError, e:
            print( '***', e )
            self.fail( "Claim is supposed to be 837-Professional")
        for msg in X12Message.objects.all():
            loop2400List= msg.descendant( 'loop', '2400' )
            self.assertEquals( 2, len(loop2400List) )
            lx1Loop= loop2400List[0]
            lx2Loop= loop2400List[1]
            #print( lx1Loop )
            self.assertEquals( "LX", lx1Loop.child('SEGMENT','LX')[0].name )
            #print( lx2Loop )
            self.assertEquals( "LX", lx2Loop.child('SEGMENT','LX')[0].name )
            self.assertEquals( self.some837, msg.marshall() )


class TestWS( TestCase ):
    def setUp( self ):
        sample= os.path.join("test","837-example.txt")
        with open( sample, "rU" ) as claims:
            self.claimText= "".join(x.strip() for x in claims)
        msg= parse_837p.unmarshall( self.claimText, Factory )
        msg.name= '837_example'
        msg.save()
    def test_load( self ):
        properties = {
            'TYPE': '', # a :class:`ClaimType` 
            'SECONDARY': '', # a :class:`SecondaryCoverage`
            'LOCATION': '', # a :class:`Location`
            'BENEFIT': '', # a :class:`Benefit`
            'TYPE-OF-SERVICE': '', # a :class:`TypeOfService`
        }
        prop_json= json.dumps( properties )
        constraints = {
            'GENDER': '', # 
            'AGE-FROM': 0, # 
            'AGE-TO': 199, # 
        }
        cons_json= json.dumps( constraints )
        params= {'claim':self.claimText, 'claim_id':'test_load',
                    'properties':prop_json, 'constraints':cons_json}
        response= self.client.post( "/claim_837/load/", params )
        self.assertEquals( 201, response.status_code )
        object= json.loads( response.content )
        self.assertEqual( "test_load", object['claim_id'] )
        self.assertEqual( self.claimText, object['claim'] )
    def test_fetch( self ):
        response= self.client.get( "/claim_837/837_example/" )
        self.assertEquals( 200, response.status_code )
        object= json.loads( response.content )
        self.assertEqual( "837_example", object['claim_id'] )
        self.assertIsNone( object['message'] )
        self.assertEqual( self.claimText, object['claim'] )