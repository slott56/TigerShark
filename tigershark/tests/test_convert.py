#!/usr/bin/env python
"""Test :mod:`tools.convertPyX12`.

Each TestCase is reasonably similar to the following.

    1.  Use the ParserBuilder to read the source and build an :mod:`X12.parse` object.
    2.  Emit SQL.  Use the SQL to build a SQLite database.
    3.  Emit Python Source.  Evaluate the Python source to create a parser.
        Parse a sample message with that parser.
"""
from __future__ import print_function
import unittest, logging, sys
import os.path
from tigershark import tools
from tigershark import X12
import cStringIO
import sqlite3.dbapi2 as sqlite
import zipfile
from tigershark.X12.parse import Message
from tigershark.X12.parse import Properties

logger= logging.getLogger( __name__ )

class TestConvertPyx12(unittest.TestCase):
    """Test conversion of PyX12 source XML definitions.
    
    ..  note::
    
        The ORIGINAL 278.4010.X094.A1.xml definition was improperly nested.
        The 2000A, 2000B, 2000C, 2000D, 2000E, 2000F Loop structure was not flat;
        a failure to match the Situational 2000D segment means that are
        no more segments were available to match.  Why no more?  2000E and 2000F are
        nested within 2010D - inexplicably.
    """
    def setUp( self ):
        # a 278-13 - I think this is a referral response
        self.msg1="""ISA*03*gjohnson2 *01*0000000000*ZZ*0000000Eliginet*ZZ*BLUECROSS BLUES*071015*0903*U*00401*000242835*0*P*:~GS*HI*0000000Eliginet*BLUECROSS BLUES*20071015*0903*241935*X*004010X094A1~ST*278*242835~BHT*0078*13*GXEDWLXQYKII*20071015*0903~HL*1**20*1~NM1*X3*2*BLUECROSS BLUESHIELD OF WESTERN NEW*****PI*55204~HL*2*1*21*1~NM1*1P*1*SHEIKH*ZIA****24*161590688~REF*ZH*000524454008~N3*4039 ROUTE 219*SUITE 102~N4*SALAMANCA*NY*14779~HL*3*2*22*1~HI*BF:706.1~NM1*IL*1*burton*amanda****MI*yjw88034076701~DMG*D8*19900815*U~HL*4*3*19*1~NM1*SJ*1*JAREMKO*WILLIAM****24*161482964~REF*ZH*000511127003~N3*2646 WEST STATE STREET*SUITE 405~N4*OLEAN*NY*147600000~HL*5*4*SS*0~TRN*1*1*9999955204~UM*SC*I*******Y~DTP*472*RD8*20071015-20080415~HSD*VS*30~SE*24*242835~GE*1*241935~IEA*1*000242835~"""

        bldParser= tools.convertPyX12.ParserBuilder()

        baseDir= r"C:\Python25\share\pyx12\map"
        zipSource= os.path.join( "Downloads", "pyx12-1.5.0.zip" )
        zip= zipfile.ZipFile( zipSource )

        xml= tools.convertPyX12.XMLParser()
        xml.data( zip.open("pyx12-1.5.0/map/dataele.xml") )
        xml.codes( zip.open("pyx12-1.5.0/map/codes.xml") )
        #The 278 definition doesn't have the correct nested LOOP structure to parse
        #xml.read( zip.open("pyx12-1.5.0/map/278.4010.X094.A1.xml") )
        #This 278 definition seems to parse better.
        xml.read( os.path.join( "test", "278.4010.X094.A1.xml" ) )
        self.x12p= bldParser.build( xml )

        sql= X12.map.SQL.SQLTableVisitor( )
        self.x12p.visit( sql )
        self.sqlCode= sql.getSource()

        python= X12.map.source.FlatPythonVisitor( "parse_278" )
        self.x12p.visit( python )
        self.pyCode= python.getSource()
    def testPythonOut( self ):
        try:
            # Creates response parser, parse_278
            exec self.pyCode
        except Exception, ex:
            logger.exception( self.pyCode )
        try:
            x12mssg= parse_278.unmarshall( self.msg1 )
        except Exception, ex:
            logger.exception( self.pyCode )
            eltPunct, compPunct, segPunct, segments= Message.tokenize(self.msg1)
            logger.error( segments )
            raise
        # TODO: Assert something...
        print( "result" )
        print( x12mssg )
        #print( self.pyCode )
    def testSQL( self ):
        db= sqlite.connect( ":memory:")
        try:
            for stmt in self.sqlCode.split( '\n;\n' ):
                db.execute( stmt )
        except sqlite.OperationalError, e:
            logger.exception( stmt )
            raise
        db.close()

if __name__ == '__main__':
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.DEBUG,
    )
    unittest.main()
