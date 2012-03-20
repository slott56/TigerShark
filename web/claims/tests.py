#!/usr/bin/env python
"""Test basic features of the core web.claims application.

Create Segments.  Create Loops with Segments.  Create Messages with Loops and
Segments.

"""
from __future__ import print_function
from  django.test import TestCase
import os.path

from X12.parse import SegmentToken
from web.claims.models import Factory, X12Segment, X12Loop, X12Message
from web.claims.models import ClaimGroup, GroupStatus
import extras.standardSegment
from web.claims.parse import parser
import json

class SegmentTest(TestCase):
    """Builds Segment and assures that various getters and setters work."""
    def setUp( self ):
        segText= "ISA*03*gjohnson2 *01*0000000000*ZZ*0000000Eliginet*ZZ*BLUECROSS BLUES*071015*0903*U*00401*000242835*0*P*:"
        segToken= SegmentToken( segText.split("*") )
        self.isa= Factory.makeSegment( segToken )
        self.isa.save()
        self.id= self.isa.id
    def tearDown( self ):
        X12Segment.objects.all().delete()
        X12Loop.objects.all().delete()
        X12Message.objects.all().delete()
    def testPositionalContent( self ):
        #print( "testPositionalContent" )
        #print( self.isa )
        self.assertEquals( "ISA", self.isa.getByPos(0) )
        self.assertEquals( "03", self.isa.getByPos(1) )
        self.assertEquals( ":", self.isa.getByPos(16) )
    def testNamedContent( self ):
        self.isa.bind( extras.standardSegment.isa )
        self.assertEquals( "03", self.isa.getByName( "ISA01" ))
        self.assertEquals( "000242835", self.isa.getByName( "ISA13"))
    def testSetter( self ):
        isa= X12Segment.objects.get( pk=self.id )
        isa.setByPos( 1, "ZZ" )
        isa.save()
        reFetch= X12Segment.objects.get( pk=self.id )
        self.assertEquals( "ZZ", reFetch.getByPos(1) )

class LoopTest( TestCase ):
    """Builds Loop and Segment.  Loop consists of mixed Segments and Loops."""
    def setUp( self ):
        isaText= "ISA*03*gjohnson2 *01*0000000000*ZZ*0000000Eliginet*ZZ*BLUECROSS BLUES*071015*0903*U*00401*000242835*0*P*:"
        isaToken= SegmentToken( isaText.split("*") )
        ieaText= "IEA*1*000242835"
        ieaToken= SegmentToken( ieaText.split("*") )
        self.isa= Factory.makeSegment( isaToken )
        self.iea= Factory.makeSegment( ieaToken )
        self.gs_loop= Factory.makeLoop( "GS_LOOP" )
        self.isa_loop= Factory.makeLoop( "ISA_LOOP", self.isa, self.gs_loop, self.iea)
        self.id= self.isa_loop.id
    def tearDown( self ):
        X12Segment.objects.all().delete()
        X12Loop.objects.all().delete()
        X12Message.objects.all().delete()
    def testLoop( self ):
        #print( "testLoop" )
        # Get the test loop from the DB
        isa_loop= X12Loop.objects.get(pk=self.id)
        #print( isa_loop )
        for loop in isa_loop.subloop_set.all():
            #print( loop.name, loop.kind, loop.thePosition, loop.theParent.name )
            pass
        children= isa_loop.children()
        self.assertEquals( 3, len(children) )
        self.assertEquals( self.isa, children[0] )
        self.assertEquals( self.gs_loop, children[1] )
        self.assertEquals( self.iea, children[2] )

class MessageTest( TestCase ):
    """Builds Message of Loops and Segments."""
    def setUp( self ):
        self.sample_278="ISA*03*gjohnson2 *01*0000000000*ZZ*0000000Eliginet*ZZ*BLUECROSS BLUES*071015*0903*U*00401*000242835*0*P*:~GS*HI*0000000Eliginet*BLUECROSS BLUES*20071015*0903*241935*X*004010X094A1~ST*278*242835~BHT*0078*13*GXEDWLXQYKII*20071015*0903~HL*1**20*1~NM1*X3*2*BLUECROSS BLUESHIELD OF WESTERN NEW*****PI*55204~HL*2*1*21*1~NM1*1P*1*SHEIKH*ZIA****24*161590688~REF*ZH*000524454008~N3*4039 ROUTE 219*SUITE 102~N4*SALAMANCA*NY*14779~HL*3*2*22*1~HI*BF:706.1~NM1*IL*1*burton*amanda****MI*yjw88034076701~DMG*D8*19900815*U~HL*4*3*19*1~NM1*SJ*1*JAREMKO*WILLIAM****24*161482964~REF*ZH*000511127003~N3*2646 WEST STATE STREET*SUITE 405~N4*OLEAN*NY*147600000~HL*5*4*SS*0~TRN*1*1*9999955204~UM*SC*I*******Y~DTP*472*RD8*20071015-20080415~HSD*VS*30~SE*24*242835~GE*1*241935~IEA*1*000242835~"
        segments= [ SegmentToken(s.split('*')) for s in self.sample_278.split("~") ]

        self.msg= Factory.makeMessage( "278" )
        self.loop_isa= Factory.makeLoop( "LOOP_ISA" )
        self.loop_isa.addChild( Factory.makeSegment( segments[0] ) )
        self.loop_gs= Factory.makeLoop( "LOOP_GS" )
        self.loop_gs.addChild( Factory.makeSegment( segments[1] ) )
        self.loop_st= Factory.makeLoop( "LOOP_ST" )
        self.loop_st.addChild( Factory.makeSegment( segments[2] ) )
        self.loop_st.addChild( Factory.makeSegment( segments[3] ) )
        self.loop_st.addChild( Factory.makeSegment( segments[-4] ) )
        self.loop_gs.addChild( self.loop_st )
        self.loop_gs.addChild( Factory.makeSegment( segments[-3] ) )
        self.loop_isa.addChild( self.loop_gs )
        self.loop_isa.addChild( Factory.makeSegment( segments[-2] ) )
        self.msg.addChild( self.loop_isa )
    def tearDown( self ):
        X12Segment.objects.all().delete()
        X12Loop.objects.all().delete()
        X12Message.objects.all().delete()
    def testMessage( self ):
        #print( self.msg )
        self.assertEquals( "278", self.msg.name )
        self.assertEquals( 1, self.msg.x12loop_set.count() )
    def testSegments( self ):
        segs= self.msg.segs()
        self.assertEquals( 7, len(segs) )
        self.assertEquals( "ISA", segs[0].getByPos(0) )
        self.assertEquals( "GS", segs[1].getByPos(0) )
        self.assertEquals( "ST", segs[2].getByPos(0) )
        self.assertEquals( "BHT", segs[3].getByPos(0) )
        self.assertEquals( "SE", segs[4].getByPos(0) )
        self.assertEquals( "GE", segs[5].getByPos(0) )
        self.assertEquals( "IEA", segs[6].getByPos(0) )
    def testMarshall( self ):
        txt= self.msg.marshall()
        start, mid, end = txt.partition( "~SE" )
        self.assertTrue( self.sample_278.startswith( start+"~" ) )
        self.assertTrue( self.sample_278.endswith( "SE"+end ) )

class ParseTest( TestCase ):
    """Uses the manually-build :samp:`278` parser to parse and persist a complete message."""
    def setUp( self ):
        import os
        #print( "Working Dir", os.getcwd() )
        # The example_278.py builds parse_278
        # execfile("../tests/example_278.py")
        from test.example_278 import parse_278
        self.parser= parse_278
        self.mssgs= []
    def tearDown( self ):
        self.gs.delete()
        self.group.delete()
        X12Segment.objects.all().delete()
        X12Loop.objects.all().delete()
        X12Message.objects.all().delete()
    def testParseToSave( self ):
        self.gs, _ = GroupStatus.objects.get_or_create( name='Base' )
        self.group, status = ClaimGroup.objects.get_or_create(
            name= "Test Group",
            description= "Sample Claims",
            status= GroupStatus.objects.get( name='Base' ),
            owner= "me" )
        count= 0
        source= {}
        with open( os.path.join("test","TEST 278_13 TXNS.txt"),"r") as example:
            for msg in example:
                msg= msg.strip()
                if len(msg) == 0: continue
                x12msg= self.parser.unmarshall( msg, Factory )
                x12msg.name= "MSG %d" % ( count, )
                x12msg.group= self.group
                x12msg.save()
                source[ x12msg.id ]= msg
                count += 1
                self.mssgs.append( x12msg )
        for msgId, msgTxt in source.items():
            dbMsg= X12Message.objects.get( pk=msgId )
            self.assertEquals( msgTxt, dbMsg.marshall() )
            # Locate unique id's (ISA13)
            isaLoop= dbMsg.x12loop_set.get( name="ISA" )
            isaSeg= isaLoop.child("segment","ISA")[0]
            self.assertTrue( isaSeg.getByPos(13) in ( '000032679','000242835','000242836','000032674','000242839' ), "Not %r" % ( isaSeg.getByPos(13) , ) )
            # XXX - should look at structure more closely, but source definition
            # for the 278 parser is not structured well.
        x12msg= X12Message.objects.get( name="MSG 0" )
        print( x12msg )


class TestWS( TestCase ):
    def setUp( self ):
        sample= os.path.join("test","837-example.txt")
        with open( sample, "rU" ) as claims:
            self.claimText= "".join(x.strip() for x in claims)
        msg= parser.unmarshall( self.claimText, Factory )
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
        response= self.client.post( "/claim/load/", params )
        #print( response.content )
        self.assertEquals( 201, response.status_code )
        object= json.loads( response.content )
        self.assertEqual( "test_load", object['claim_id'] )
        self.assertEqual( self.claimText, object['claim'] )
    def test_fetch( self ):
        response= self.client.get( "/claim/837_example/" )
        self.assertEquals( 200, response.status_code )
        object= json.loads( response.content )
        self.assertEqual( "837_example", object['claim_id'] )
        self.assertIsNone( object['message'] )
        self.assertEqual( self.claimText, object['claim'] )
        
from test.test_navigation import TestNavigationX12
import web.claims.models

class TestNavigationClaims( TestNavigationX12 ):
    """Test message structure navigation using :mod:`web.claims` class definitions
    instead of the X12 package class definitions.
    
    This plugs in the :class:`web.claims.models.Factory`.
    """
    factory= web.claims.models.Factory
