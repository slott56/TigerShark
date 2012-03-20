#!/usr/bin/env python
"""Test :mod:`X12.parse`.

Manually build a 278 parser, :py:data:`parse_278`.  Exercise that manually-built parser.

Test the Python output from the 278 parser.

Test the SQL output from the 278 parser.

Test the Django output from the 278 parser.

:parse_278: Manually built parser for :samp:`278` messages.
"""
from __future__ import print_function
import unittest
import logging, sys
import os.path

import X12
from X12.parse import Message, Loop, Segment, Element, Properties
import X12.map.SQL
import X12.map.source
import X12.map.dj

logger= logging.getLogger( __name__ )

# THE MANUALLY-BUILT PARSER:
from example_278 import parse_278, loop2000F, loop2000A

class TestStructure(unittest.TestCase):
    """Test Message Structure."""
    def testBadLoop( self ):
        """Can't include a Message within a Loop."""
        self.assertRaises( X12.parse.StructureError,
            Loop, "name", Properties(desc="desc", req_sit="R", repeat="1"), Message("bad",Properties(desc="bad") ) )
    def testMessage( self ):
        self.assertEquals( parse_278, loop2000F.message  )
        self.assertEquals( "278", loop2000A.message.name )

class TestSegmentMatch(unittest.TestCase):
    """Test Segment match."""
    def setUp( self ):
        self.segments1= [ ['ST', '278', '242835'] ]
        self.segments2= [ ['ST', '279', '242835'] ]
        self.parserQual= Segment( "ST", Properties( qual=(1,"278"), desc="ST", req_sit="R" ),
            Element( "ST01", Properties(position=1,codes=["278"]) ),
            )
        self.parserNonQual= Segment( "ST", Properties( desc="ST", req_sit="R" ) )
    def testQual( self ):
        self.assertTrue( self.parserQual.match( self.segments1[0] ) )
        self.assertFalse( self.parserQual.match( self.segments2[0] ) )
    def testNonQual( self ):
        self.assertTrue( self.parserNonQual.match( self.segments1[0] ))
        self.assertTrue( self.parserNonQual.match( self.segments2[0] ))

class TestParse278_13(unittest.TestCase):
    """Test the hand-build 278 parser."""
    def setUp( self ):
        # a 278-13 response
        self.msg1="""ISA*03*gjohnson2 *01*0000000000*ZZ*0000000Eliginet*ZZ*BLUECROSS BLUES*071015*0903*U*00401*000242835*0*P*:~GS*HI*0000000Eliginet*BLUECROSS BLUES*20071015*0903*241935*X*004010X094A1~ST*278*242835~BHT*0078*13*GXEDWLXQYKII*20071015*0903~HL*1**20*1~NM1*X3*2*BLUECROSS BLUESHIELD OF WESTERN NEW*****PI*55204~HL*2*1*21*1~NM1*1P*1*SHEIKH*ZIA****24*161590688~REF*ZH*000524454008~N3*4039 ROUTE 219*SUITE 102~N4*SALAMANCA*NY*14779~HL*3*2*22*1~HI*BF:706.1~NM1*IL*1*burton*amanda****MI*yjw88034076701~DMG*D8*19900815*U~HL*4*3*19*1~NM1*SJ*1*JAREMKO*WILLIAM****24*161482964~REF*ZH*000511127003~N3*2646 WEST STATE STREET*SUITE 405~N4*OLEAN*NY*147600000~HL*5*4*SS*0~TRN*1*1*9999955204~UM*SC*I*******Y~DTP*472*RD8*20071015-20080415~HSD*VS*30~SE*24*242835~GE*1*241935~IEA*1*000242835~"""

    def testTokenize( self ):
        _, _, _, tokens= parse_278.tokenize( self.msg1 )
        self.assertEquals( 28, len(tokens) )
        self.assertEquals( 17, len(tokens[0])) # The ISA Segment
        self.assertEquals( "ISA", tokens[0][0] )
        self.assertEquals( "GS", tokens[1][0] )
        self.assertEquals( "ST", tokens[2][0] )
        self.assertEquals( "SE", tokens[-3][0] )
        self.assertEquals( "GE", tokens[-2][0] )
        self.assertEquals( "IEA", tokens[-1][0] )

    def testISAMatch( self ):
        _, _, _, tokens= parse_278.tokenize( self.msg1 )
        isaTokens= tokens[0]
        isa= parse_278.structure[0]
        self.assertTrue( isa.match(isaTokens) )

    def testParse( self ):
        message= parse_278.unmarshall( self.msg1 )
        self.assertEquals( self.msg1, message.marshall() )
        #print( message )

class TestVisitor1(unittest.TestCase):
    """Test the generic visitor."""
    def testPythonVisitor( self ):
        python= X12.map.source.PythonVisitor( "parse_278" )
        parse_278.visit( python )
        text= python.getSource()
        sample="""from X12.parse import Message, Loop, Segment, Composite, Element, Properties
parse_278 = Message( '278', Properties(desc='HIPAA Health Care Services Review: Request X094A1-278'),
  Loop( 'ISA', Properties(req_sit='R',repeat='1',desc='ISA'),
    Segment( 'ISA', Properties(),
    ),
    Loop( 'GS', Properties(req_sit='R',repeat='1',desc='GS'),
      Segment( 'GS', Properties(),
      ),
      Loop( 'ST', Properties(req_sit='R',repeat='1',desc='ST'),
        Segment( 'ST', Properties(qual=(1, '278'),req_sit='R',repeat='1',desc='Transaction Set Header'),
          Element( 'ST01', Properties(desc=None, req_sit=None, data_type=(None,None,None), position=1,
            codes=['278'] ) ),
        ),
        Segment( 'BHT', Properties(req_sit='R',repeat='1',desc='Beginning of Hierarchical Transaction'),
        ),
        Loop( '2000A', Properties(req_sit='R',repeat='1',desc='2000A'),
          Segment( 'HL', Properties(qual=(3, '20'),req_sit='R',repeat='1',desc='Utilization Management Organization (UMO) Level'),
            Element( 'HL03', Properties(desc=None, req_sit=None, data_type=(None,None,None), position=3,
              codes=['20'] ) ),
          ),
          Loop( '2010A', Properties(req_sit='R',repeat='>1',desc='2010A'),
            Segment( 'NM1', Properties(qual=(1, 'X3'),req_sit='R',repeat='1',desc='Utilization Management Organization (UMO) Name'),
              Element( 'NM101', Properties(desc=None, req_sit=None, data_type=(None,None,None), position=1,
                codes=['X3'] ) ),
            ),
          ),"""
        tLines= text.splitlines()
        sLines= sample.splitlines()
        for i in range(len(sLines)):
            self.assertEqual( tLines[i].rstrip(), sLines[i].rstrip() )

class TestPythonVisitor(unittest.TestCase):
    """Does it compile?

    Does it actually parse the message?"""
    def setUp( self ):
        # a 278-13 response
        self.msg1="""ISA*03*gjohnson2 *01*0000000000*ZZ*0000000Eliginet*ZZ*BLUECROSS BLUES*071015*0903*U*00401*000242835*0*P*:~GS*HI*0000000Eliginet*BLUECROSS BLUES*20071015*0903*241935*X*004010X094A1~ST*278*242835~BHT*0078*13*GXEDWLXQYKII*20071015*0903~HL*1**20*1~NM1*X3*2*BLUECROSS BLUESHIELD OF WESTERN NEW*****PI*55204~HL*2*1*21*1~NM1*1P*1*SHEIKH*ZIA****24*161590688~REF*ZH*000524454008~N3*4039 ROUTE 219*SUITE 102~N4*SALAMANCA*NY*14779~HL*3*2*22*1~HI*BF:706.1~NM1*IL*1*burton*amanda****MI*yjw88034076701~DMG*D8*19900815*U~HL*4*3*19*1~NM1*SJ*1*JAREMKO*WILLIAM****24*161482964~REF*ZH*000511127003~N3*2646 WEST STATE STREET*SUITE 405~N4*OLEAN*NY*147600000~HL*5*4*SS*0~TRN*1*1*9999955204~UM*SC*I*******Y~DTP*472*RD8*20071015-20080415~HSD*VS*30~SE*24*242835~GE*1*241935~IEA*1*000242835~"""
    def testPythonVisitorCompile( self ):
        python= X12.map.source.FlatPythonVisitor( "parse_278" )
        parse_278.visit( python )
        text= python.getSource()
        #print( "***Manual Inspection" )
        #print( text )
        exec text

    def testPythonVisitorWorks( self ):
        python= X12.map.source.FlatPythonVisitor( "parse_278" )
        parse_278.visit( python )
        text= python.getSource()
        exec text
        self.assertEqual( type(parse_278), X12.parse.Message )
        msg= parse_278.unmarshall( self.msg1 )
        # XXX - check the resulting structure
        self.assertEquals( self.msg1, msg.marshall() )

class TestSQLVisitor(unittest.TestCase):
    """Does it compile?"""
    def testSQLVisitor( self ):
        sql= X12.map.SQL.SQLTableVisitor( )
        parse_278.visit( sql )
        text= sql.getSource()
        #print( "***Manual Inspection" )
        #print( text )
        sample="""-- HIPAA Health Care Services Review: Request X094A1-278
CREATE TABLE X278_278(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- FK reference from X278_ISA -- ISA
    -- FK reference from X278_IEA -- IEA
    xtra CHAR(8) -- placeholder
) -- 278
;
-- ISA
CREATE TABLE X278_ISA(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    loop INTEGER NOT NULL REFERENCES X278_278(id),
    -- In-line Segment ISA None
    -- FK reference from X278_GS -- GS
    -- FK reference from X278_GE -- GE
    xtra CHAR(8) -- placeholder
) -- ISA
;
-- GS
CREATE TABLE X278_GS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    loop INTEGER NOT NULL REFERENCES X278_ISA(id),
    -- In-line Segment GS None
    -- FK reference from X278_ST -- ST
    -- FK reference from X278_SE -- SE
    xtra CHAR(8) -- placeholder
) -- GS
;
"""
        tLines= text.splitlines()
        sLines= sample.splitlines()
        for i in range(len(sLines)):
            self.assertEqual( tLines[i].rstrip(), sLines[i].rstrip() )

class TestDjangoVisitors(unittest.TestCase):
    """Look at the Django structure emitted"""
    def testDjangoModel( self ):
        dj= X12.map.dj.DjangoModelVisitor( )
        parse_278.visit( dj )
        text= dj.getSource(appname='claims_837')
        #print( "***Manual Inspection" )
        #print( text )
        sample='''\
from web.claims.models import X12Segment
from django.db import models

class Segment_ISA(models.Model):
    """Properties()"""
    segment = models.ForeignKey( X12Segment )
    def unmarshall( self, segmentToken, cs=':' ):

class Segment_GS(models.Model):
    """Properties()"""
    segment = models.ForeignKey( X12Segment )
    def unmarshall( self, segmentToken, cs=':' ):

class Segment_ST(models.Model):
    """Properties(qual=(1, '278'),req_sit='R',repeat='1',desc='Transaction Set Header')"""
    segment = models.ForeignKey( X12Segment )
    ST01 = models.CharField( max_length=16, null=True, blank=True ) # None None
    def unmarshall( self, segmentToken, cs=':' ):
        self.ST01 = segmentToken.elt(1)
'''
        tLines= text.splitlines()
        sLines= sample.splitlines()
        for i in range(len(sLines)):
            self.assertEqual( tLines[i].rstrip(), sLines[i].rstrip() )
    def testDjangoAdmin( self ):
        dj= X12.map.dj.DjangoAdminVisitor( )
        parse_278.visit( dj )
        text= dj.getSource(appname='claims_837')
        #print( "***Manual Inspection" )
        #print( text )
        sample= '''\
from web.claims_837.models import NM1
admin.site.register( NM1 )
from web.claims_837.models import PER
admin.site.register( PER )
from web.claims_837.models import CRC
admin.site.register( CRC )
from web.claims_837.models import ST
admin.site.register( ST )
from web.claims_837.models import HL
admin.site.register( HL )
from web.claims_837.models import MSG
admin.site.register( MSG )
from web.claims_837.models import ISA
admin.site.register( ISA )
from web.claims_837.models import DTP
admin.site.register( DTP )
from web.claims_837.models import REF
admin.site.register( REF )
from web.claims_837.models import HSD
admin.site.register( HSD )
from web.claims_837.models import DMG
admin.site.register( DMG )
from web.claims_837.models import PRV
admin.site.register( PRV )
from web.claims_837.models import CL1
admin.site.register( CL1 )
from web.claims_837.models import GS
admin.site.register( GS )
from web.claims_837.models import TRN
admin.site.register( TRN )
from web.claims_837.models import GE
admin.site.register( GE )
from web.claims_837.models import IEA
admin.site.register( IEA )
from web.claims_837.models import N3
admin.site.register( N3 )
from web.claims_837.models import N4
admin.site.register( N4 )
from web.claims_837.models import CR2
admin.site.register( CR2 )
from web.claims_837.models import CR1
admin.site.register( CR1 )
from web.claims_837.models import CR6
admin.site.register( CR6 )
from web.claims_837.models import CR5
admin.site.register( CR5 )
from web.claims_837.models import INS
admin.site.register( INS )
from web.claims_837.models import UM
admin.site.register( UM )
from web.claims_837.models import HI
admin.site.register( HI )
from web.claims_837.models import BHT
admin.site.register( BHT )
from web.claims_837.models import SE
admin.site.register( SE )
'''
        tLines= text.splitlines()
        sLines= sample.splitlines()
        for i in range(len(sLines)):
            self.assertEqual( tLines[i].rstrip(), sLines[i].rstrip() )

if __name__ == '__main__':
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.DEBUG,
    )
    
    unittest.main()
