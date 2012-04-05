#!/usr/bin/env python
"""Survey PyX12 Segment Definitions.

Read ALL pyx12 message definitions, accumulate all Segment definitions.

"""
from __future__ import print_function
import xml.dom.minidom as DOM
import os, glob

segmentTypes= {}
segmentUse= {}
def getDef( aFile ):
    """Get the Segment Definitions from an XML file."""
    msgDef= DOM.parse( aFile )
    theDoc= msgDef.documentElement
    msgName= theDoc.attributes['xid'].value
    for segment in msgDef.getElementsByTagName( "segment"):
        xid= segment.attributes['xid'].value
        for n in segment.childNodes:
            if n.nodeType == DOM.Node.ELEMENT_NODE and n.nodeName == "name":
                segName= " ".join( [ c.nodeValue for c in n.childNodes ] )
        segmentUse.setdefault( xid, set() )
        segmentUse[xid].add( msgName )
        segmentTypes.setdefault( xid, set() )
        segmentTypes[xid].add( segName )

def survey( pattern ):
    """Survey an entire directory, using a wild-card pattern."""
    for f in glob.glob( pattern ):
        getDef( f )
    segs= segmentTypes.keys()
    segs.sort()
    format1 = "+%-8s+%-128s+"
    format2 = "|%-8s|%-128s|"
    print( format1 % ( 8*'-', 128*'-' ) )
    for k in segs:
        v= list( segmentTypes[k] )
        print( format2 % ( "``%s``" % k, v[0] ) )
        for m in v[1:]:
            print( format2 % ( '', ", "+m ) )
        print( format1 % ( 8*'-', 128*'-' ) )

if __name__ == "__main__":
    baseDir= r"C:\Python25\share\pyx12\map"
    #survey( os.path.join( baseDir, "[0-9]*.xml" ) )
    survey( os.path.join( baseDir, "837*.xml" ) )
