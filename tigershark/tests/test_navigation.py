#!/usr/bin/env python
"""Test :mod:`X12.message` Xpath-like navigation.

The :mod:`X12.message` Factory is used to build one set of objects.  This works
in a stand-alone mode.
"""
import unittest
import logging, sys
from tigershark import X12


class TestNavigationX12( unittest.TestCase ):
    """Test XPath-like Navigation methods."""
    factory= X12.message.Factory
    def setUp( self ):
        factory= self.factory
        self.message= factory.makeMessage( "278" )
        loop_isa= factory.makeLoop( "ISA" )
        self.message.addChild( loop_isa )
        isaSegToken= X12.parse.SegmentToken( ["ISA", "21", "blah", "blah", "blah"] )
        loop_isa.addChild( factory.makeSegment( isaSegToken ) )
        loop_gs= factory.makeLoop( "GS" )
        loop_isa.addChild( loop_gs )
        gsSegToken= X12.parse.SegmentToken( ["GS", "HI", "blah", "blah", "blah"] )
        loop_gs.addChild( factory.makeSegment( gsSegToken ) )
        geSegToken= X12.parse.SegmentToken( ["GE", "hi", "there"] )
        loop_gs.addChild( factory.makeSegment( geSegToken ) )
        ieaSegToken= X12.parse.SegmentToken( ["IEA", "xx", "yy"] )
        loop_isa.addChild( factory.makeSegment( ieaSegToken ) )
    def testChild( self ):
        loops= self.message.child( "LOOP" )
        self.assertEquals( 1, len(loops) )
        segs= self.message.child( "SEGMENT" )
        self.assertEquals( 0, len(segs) )
        isaList= self.message.child( "LOOP", name="ISA" )
        self.assertEquals( 1, len(isaList) )
        ieaList= isaList[0].child( "SEGMENT", name="IEA" )
        self.assertEquals( 1, len(ieaList) )
    def testDescendant( self ):
        geList= self.message.descendant( "SEGMENT", name="GE" )
        self.assertEquals( 1, len(geList) )
    def testParent( self ):
        geList= self.message.descendant( "SEGMENT", name="GE" )
        self.assertEquals( 1, len(geList) )
        ge= geList[0]
        self.assertEquals( 0, len(ge.parent("SEGMENT")) )
        parentList= ge.parent( "LOOP" )
        self.assertEquals( 1, len(parentList) )
        self.assertEquals( "GS", parentList[0].name )
    def testAncestor( self ):
        geList= self.message.descendant( "SEGMENT", name="GE" )
        self.assertEquals( 1, len(geList) )
        ge= geList[0]
        isaList= ge.ancestor( "LOOP", name="ISA" )
        self.assertEquals( 1, len(isaList) )

if __name__ == '__main__':
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.DEBUG,
    )
    unittest.main()
