#!/usr/bin/env python
"""Convert pyx12 configuration files from XML to Python.

The Python X12 module contains a number of XML files which
define X12 message structures.  They need to be converted into the syntax for the
:mod:`X12.parse` parser.

Note that the pyx12 module defines Loops, Segments, Composites and individual Elements.
It also defines selected data element types and sizes.  Since it provides
complete code values, it provides Segment parsing clues and compliance
checking values.

Definitions
===========

There are two principle classes in this module.

..  autoclass:: XMLParser

    This reads XML files and creates
    :mod:`xml.dom` structures for the codes, data elements and message
    structures.

..  autoclass:: ParserBuilder

    This emits a Python :mod:`X12.parse` constructor
    that matches the given :file:`.CF` file.

There are two convenience functions.

..  autofunction:: convertFilePath

..  autofunction:: convertFile

..  autofunction:: convertAll


Warnings
========

The following default warnings configuration is used.

    -   :class:`XMLWarning` are elevated to Errors to cause this module to stop.
        In the case of suspicious XML, it is possible to downgrade these
        errors and keep processing.

    -   :class:`EmptyLoopWarning` is always reported, but is merely a warning.

    -   :class:`UnknownElementWarning` is always reported, but is merely a warning.

    -   :class:`Extension` is reported once so that it's clear that the XML contains
        features which were not parsed.

XML Source Structure
====================

The pyx12 package provides a :mod:`pyx12.maps.xsd` that provides a bit
of guidance on parsing the XML documents.
The :file:`README` provides some additional hints.

The following elements are
used in the message xml definitions.

    - usage
        Implementation Guide Usage field. S=Situational, N=Not Used, R=Required

    - pos
        Segment position number -- obvious from the XML document, but provided anyway

    - id
        Implementation Guide id

    - name
        Implementation Guide name

    - data_ele
        Data Element id

    - valid_codes
        List of valid codes for the element or the name.
        Could be a separate list document, via attribute external="".
        See codes.xml for the complete set of codes.

    - refdes
        reference designator for a Composite item

    - syntax
        STD syntax dependency string for a segment, optional

The :mod:`pyx12.maps.xsd` provides a schema for the various message definitions.

Data Element Definitions
========================

The following are used in the data element definitions.

    - data_ele
        Data Element ID

    - name
        IG name

    - data_type
        STD type

    - min_len/max_len
        STD

Analysis reveals the following DTD for the message definitions::

    <!ELEMENT data_elements ( data_ele )*>

    <!ELEMENT data_ele #PCDATA>
    <!ATTLIST data_ele
        ele_num   CDATA #REQUIRED
        data_type (ID|R|AN|DT|TM|N0) #REQUIRED
        min_len   CDATA #REQUIRED
        max_len   CDATA #REQUIRED
        name      CDATA #REQUIRED>

"""
from __future__ import print_function
import xml.dom.minidom as DOM
import argparse
from datetime import datetime
import os.path, logging, sys, fnmatch
import warnings
from tigershark.X12.parse import Composite
from tigershark.X12.parse import Element
from tigershark.X12.parse import Loop
from tigershark.X12.parse import Message
from tigershark.X12.parse import Properties
from tigershark.X12.parse import Segment
from tigershark.X12.map.source import FlatPythonVisitor
from tigershark.X12.map.source import PythonVisitor

class XMLWarning( UserWarning ):
    """A superclass for a number of warnings regarding the XML definition."""
    pass

class EmptyLoopWarning( UserWarning ):
    """A Loop definition had no subloops or Segments."""
    pass

class UnknownElementWarning( UserWarning ):
    """An Element had a dataele= reference to an unkown name."""
    pass

class Extension( UserWarning ):
    """This feature of the XML is an extension to the current implementation."""
    pass

class ParserBuilder( object ):
    """Build a :mod:`X12.parse` Parser from an XML message specification.

    This makes use of an :class:`XMLParser` instance which has been populated
    with three separate XML documents.

        1. The data element definitions were parsed with :meth:`XMLParser.data`.

        2. The external code definitions were parsed with :meth:`XMLParser.codes`.

        3. The message structure was parsed via :meth:`XMLParser.read`.

    Once this is complete, then the :meth:`build` method can be given the
    :class:`XMLParser` to emit the desired :class:`X12.parse.Message` object.

    This creates the :class:`X12.parse.Message` object, inserts the various
    Loop and Segment components.  The resulting object can be used to
    parse X12 messages.

    The resulting object can also be used to emit Python source,
    as well as SQL DDL.

    The :samp:`<transaction>` contains :samp:`<loop>`'s.
    The :samp:`<loop>`'s contain :samp:`<segment>`'s and :samp:`<loop>`'s.
    The :samp:`<segment>`'s contain :samp:`<element>`'s and :samp:`<composite>`'s.

    :ivar dataDictionary: a dictionary of :samp:`<data_ele>` definitions.
    """
    def __init__( self ):
        """Creates a new, uninitialized ParserBuilder."""
        self.log= logging.getLogger( "tools.convertPyX12.ParserBuilder" )
        self.log2= logging.getLogger( "tools.convertPyX12.ParserBuilder.buildElement" )
        self.dataDictionary= {}
    def buildDataElementDef( self, aNode ):
        """Load the data dictionary with the definition from a :samp:`<data_ele>` node.
        The key is the data element name.
        The value in the dictionary is a tuple of ( data_type, min_len and max_len ).

        :param aNode: a :mod:`xml.dom` Element with a name of :samp:`data_ele`
        """
        assert aNode.nodeType == DOM.Node.ELEMENT_NODE and aNode.nodeName == "data_ele"
        # ele_num="100" data_type="ID" min_len="3" max_len="3" name
        ele_num= aNode.getAttribute('ele_num')
        data_type= aNode.getAttribute('data_type')
        min_len= aNode.getAttribute('min_len')
        max_len= aNode.getAttribute('max_len')
        name= aNode.getAttribute('name')
        self.dataDictionary[ele_num]= ( name, (data_type, min_len, max_len) )
    def dataElements( self, xmlDoc ):
        """Load the data dictionary with the definitions from the :samp:`<data_elements>` node.

        :param xmlDoc: a :class:`XMLParser` which has parsed the data document
        """
        doc= xmlDoc.dataeleDoc.documentElement
        assert doc.nodeType == DOM.Node.ELEMENT_NODE and doc.nodeName == "data_elements"
        for c in doc.childNodes:
            if c.nodeType != DOM.Node.ELEMENT_NODE: continue
            if c.nodeName == "data_ele":
                self.buildDataElementDef( c )
            else:
                warnings.warn( XMLWarning("Unexpected %r" % (c,) ) )
                self.log.warning( "*** Unexpected %r", c )
    def codes( self, xmlDoc ):
        """Load external code file.

        ..  todo:: XXX - Finish load external code file.

        :param xmlDoc: a :class:`XMLParser` which has parsed the codes document
        """
        pass
    def getValidCodes( self, aNode ):
        """Parse a :samp:`<valid_codes>` node, building a list of valid codes
        for an Element.  This will examine only :samp:`<code>` elements found
        under the :samp:`<valid_codes>` element.
        
        :param aNode: a :mod:`xml.dom` Element with a name of :samp:`valid_codes`
        :returns: list of code values
        """
        assert aNode.nodeType == DOM.Node.ELEMENT_NODE and aNode.nodeName == "valid_codes"
        codes= []
        for c in aNode.childNodes:
            if c.nodeType != DOM.Node.ELEMENT_NODE: continue
            if c.nodeName == "code":
                for n in c.childNodes:
                    codes.append( n.nodeValue )
            else:
                warnings.warn( XMLWarning("Unexpected %r" % (c,) ) )
                self.log.warning( "*** Unexpected %r", c )
        return codes
    def buildComposite( self, compositeNode, context, nesting=0 ):
        """Build a Composite from a list of sub-Elements.

        Note that the ISA segment provides the Component Element Separator in ISA16.

        Composites are tricky.  We have two choices.

            1.  Treat them as just a sequence of Elements -- which they
                are for RDBMS purposes.  However, this makes compliance
                checking hard, since we have to look inside the composite.
                We have to turn off "match" for each Element of the Composite,
                otherwise, we won't be able to look into the segment data
                properly.

            2.  Treat them as a subclass of Elements -- which is a lot of
                fooling around to support a few compliance checks.  We have to
                provide a composite match function and we have to make use
                of punctuation in the ISA segment for sub-parsing each Composite when we
                finally figure out what the Segment and Elements.

        :param compositeNode: a :mod:`xml.dom` Element with a name of :samp:`composite`
        :param context: The Segment which contains this Composite
        :param nesting: The current nesting level used to indent the log messages.
        """
        assert compositeNode.nodeType == DOM.Node.ELEMENT_NODE and compositeNode.nodeName == "composite"
        name= self.getChildTextValue( compositeNode, "name" )
        usage= self.getChildTextValue( compositeNode, "usage" )
        seq= self.getChildTextValue( compositeNode, "seq" )
        data_ele= self.getChildTextValue( compositeNode, "data_ele" )
        refdes= self.getChildTextValue( compositeNode, "refdes" )
        self.log.debug( "%*sComposite name %r usage %r seq %r data_ele %r refdes %r",
                       nesting*2, '', name, usage, seq, data_ele, refdes )
        theComposite= Composite(
            data_ele,
            Properties( desc=name, req_sit=usage, seq=seq, refdes=refdes ) )
        for c in compositeNode.childNodes:
            # Want to preserve the original XML order of <element>
            if c.nodeType != DOM.Node.ELEMENT_NODE: continue
            if c.nodeName == "element":
                self.buildElement( c, theComposite, nesting+1 )
            elif c.nodeName in ( "name", "usage", "seq", "data_ele", 'refdes',):
                pass # already consumed
            else:
                warnings.warn( XMLWarning("Unexpected %r" % (c,) ) )
                self.log.warning( "*** Unexpected %r", c )
        context.append( theComposite )
    def buildElement( self, elementNode, context, nesting=0 ):
        """Element is the fundamental piece of data in a Segment or Composite.
        Elements can have code definitions or can reference external code
        definitions.
        
        ..  todo:: XXX - Use external code definitions.
        
        :param elementNode: a :mod:`xml.dom` Element with a name of :samp:`element`
        :param context: The Segment or Composite which contains this Element
        :param nesting: The current nesting level used to indent the log messages.
        """
        assert elementNode.nodeType == DOM.Node.ELEMENT_NODE and elementNode.nodeName == "element"
        eltXid= elementNode.getAttribute('xid')
        name= self.getChildTextValue( elementNode, "name" )
        usage= self.getChildTextValue( elementNode, "usage" )
        seq= self.getChildTextValue( elementNode, "seq" )
        data_ele= self.getChildTextValue( elementNode, "data_ele" )
        self.log.debug( "%*sElement id %r name %r usage %r seq %r data_ele %r",
                       nesting*2, '', eltXid, name, usage, seq, data_ele )
        if not self.dataDictionary.has_key( data_ele ):
            warnings.warn( UnknownElementWarning("No Data Element %r %r %r" % ( eltXid, data_ele, name ,) ) )
            data_type_tuple= (None,None,None)
        else:
            name, data_type_tuple = self.dataDictionary[data_ele]

        codes= []
        for c in elementNode.childNodes:
            if c.nodeType != DOM.Node.ELEMENT_NODE: continue
            if c.nodeName == "valid_codes":
                if c.getAttribute("external") != "":
                    pass # reference to codes.xml codes
                    # XXX - Handle external code list
                    warnings.warn( Extension("External Codes Not Implemented") )
                else:
                    codes= self.getValidCodes( c )
            elif c.nodeName in ( "name", "usage", "seq", "data_ele", ):
                pass # already consumed
            else:
                warnings.warn( XMLWarning("Unexpected %r" % (c,) ) )
                self.log.warning( "*** Unexpected %r", c )

        theElement= Element(
            eltXid,
            Properties(desc=name, req_sit=usage, seq=seq, data_ele=data_ele,
                       data_type=data_type_tuple, codes=codes, )
            )

        if self.dataDictionary.has_key( data_ele ) and len(codes) != 0:
            #self.log2.debug( "Segment Qual Parameter? %r %r", self.dataDictionary[data_ele], codes )
            pass

        context.append( theElement )
    def buildSegment( self, segmentNode, context, nesting=0 ):
        """Segment contains Elements and Composites.
        
        :param segmentNode: a :mod:`xml.dom` Element with a name of :samp:`segment`
        :param context: The Loop which contains this Segment.
        :param nesting: The current nesting level used to indent the log messages.
        """
        assert segmentNode.nodeType == DOM.Node.ELEMENT_NODE and segmentNode.nodeName == "segment"
        segXid= segmentNode.getAttribute('xid')
        name= self.getChildTextValue( segmentNode, "name" )
        usage= self.getChildTextValue( segmentNode, "usage" )
        pos= self.getChildTextValue( segmentNode, "pos" )
        max_use= self.getChildTextValue( segmentNode, "max_use" )
        syntax= self.getChildTextValue( segmentNode, "syntax" )
        self.log.debug( "%*sSegment xid %r: name %r usage %r pos %r max_use %r syntax %r",
                       nesting*2, '', segXid, name, usage, pos, max_use, syntax )
        theSegment= Segment(
            segXid,
            Properties(desc=name,req_sit=usage,pos=pos,repeat=max_use,syntax=syntax),
            )

        for c in segmentNode.childNodes:
            # Want to preserve the original XML order of <element> and <composite>
            if c.nodeType != DOM.Node.ELEMENT_NODE: continue
            if c.nodeName == "element":
                self.buildElement( c, theSegment, nesting+1 )
            elif c.nodeName == "composite":
                self.buildComposite( c, theSegment, nesting+1 )
            elif c.nodeName in ( "name", "usage", "pos", "max_use", "syntax", ):
                pass # already consumed
            else:
                warnings.warn( XMLWarning("Unexpected %r" % (c,) ) )
                self.log.warning( "*** Unexpected %r", c )
        context.append( theSegment )
    def buildLoop( self, loopNode, context, nesting=0 ):
        """Loop contains Segments and Loops.
        Empty Loops create a warning, and are dropped.
        
        :param loopNode: a :mod:`xml.dom` Element with a name of :samp:`loop`
        :param context: The Loop which contains this Loop or Segment.
        :param nesting: The current nesting level used to indent the log messages.
        """
        assert loopNode.nodeType == DOM.Node.ELEMENT_NODE and loopNode.nodeName == "loop"
        loopXid= loopNode.getAttribute('xid')
        loopType= loopNode.getAttribute('type')
        name= self.getChildTextValue( loopNode, "name" )
        usage= self.getChildTextValue( loopNode, "usage" )
        pos= self.getChildTextValue( loopNode, "pos" )
        repeat= self.getChildTextValue( loopNode, "repeat" )
        self.log.debug( "%*sLoop xid %r type %r: name %r usage %r pos %r repear %r",
                       nesting*2, '', loopXid, loopType, name, usage, pos, repeat )
        theLoop= Loop(
            loopXid,
            Properties(desc=name,req_sit=usage,pos=pos,repeat=repeat,looptype=loopType),
            )

        for c in loopNode.childNodes:
            # Want to preserve the original XML order of <loop> and <segment>
            if c.nodeType != DOM.Node.ELEMENT_NODE: continue
            if c.nodeName == "loop":
                self.buildLoop( c, theLoop, nesting+1 )
            elif c.nodeName == "segment":
                self.buildSegment( c, theLoop, nesting+1 )
            elif c.nodeName in ( "name", "usage", "pos", "repeat", ):
                pass # already consumed
            else:
                warnings.warn( XMLWarning("Unexpected %r" % (c,) ) )
                self.log.warning( "*** Unexpected %r", c )
        if len(theLoop.structure) == 0:
            warnings.warn( EmptyLoopWarning("Empty Loop %r" % (theLoop,) ) )
            # optimize this out of existence
        else:
            context.append( theLoop )
    def build( self, xmlDoc, name=None ):
        """Build the overall :class:`X12.parse.Message` parser.
        
        :param xmlDoc: a :class:`XMLParser` which has parsed the data, codes and message
            structure documents.
        :param name: Optional name of the Message to build; this will use
            the xid attribute provided in the XML if no overriding name is provided here.
        :returns: :class:`X12.parse.Message` parser.
        """
        self.dataElements( xmlDoc )
        self.codes( xmlDoc )
        doc= xmlDoc.doc.documentElement
        assert doc.nodeType == DOM.Node.ELEMENT_NODE and doc.nodeName == "transaction"
        xid= doc.getAttribute('xid')
        desc= self.getChildTextValue( doc, "name" )
        if name is None: name= xid
        self.log.info( "Message %s: xid=%s desc=%s", name, xid, desc )
        self.top= Message( name, Properties(desc=desc) )
        for c in doc.childNodes:
            # Want to preserve the original XML order of <loop> and <segment>
            if c.nodeType != DOM.Node.ELEMENT_NODE: continue
            if c.nodeName == "loop":
                self.buildLoop( c, self.top )
            elif c.nodeName in ( "name", ):
                pass # Already consumed this
            else:
                warnings.warn( XMLWarning("Unexpected %r" % (c,) ) )
                self.log.warning( "*** Unexpected %r", c )
        return self.top
    def getChildTextValue( self, aNode, name ):
        """Examines all children with the given name
        and extracts the text nodes for those children.
        It accumulates the nodeValues for those text nodes.
        
        :param aNode: an :mod:`xml.dom` Element.
        :param name: a node name underneath the given node.
        """
        childElements = [ n for n in aNode.childNodes if n.nodeType == DOM.Node.ELEMENT_NODE and n.nodeName == name ]
        textNodes = [ n for c in childElements for n in c.childNodes if n.nodeType in ( DOM.Node.TEXT_NODE, DOM.Node.CDATA_SECTION_NODE ) ]
        text = [ n.nodeValue for n in textNodes ]
        return " ".join( text )

class XMLParser( object ):
    """Parse a related set of XML docs to get codes, data element definitions
    and the overall Message structure.

    The ParserBuilder will need some combination of these related XML documents
    to define the :mod:`X12.parse` parser.
    """
    def __init__( self ):
        """Creates an empty XMLParser instance."""
        self.dataeleDoc= None
        self.codesDoc= None
        self.doc= None
    def data( self, name_or_file ):
        """Parses the data element definition XML file.
        
        :param fileName: name of the data element file, usually :file:`dataele.xml`
        """
        self.dataeleDoc= DOM.parse( name_or_file )
    def codes( self, name_or_file ):
        """Parses the external codes definition XML file.
        
        :param fileName: name of the external codes file, usually :file:`codes.xml`
        """
        self.codesDoc= DOM.parse( name_or_file )
    def read( self, name_or_file ):
        """Parses the message structure XML file.
        
        :param fileName: the name of a message structure file.
        """
        self.doc= DOM.parse( name_or_file )
    def dump( self, aDoc ):
        """Prints a dump of an XML document to stdout.
        
        :param aDoc: an :mod:`xml.dom` Node (usually the top-level Document).
        """
        nodeNames= set()
        def walk( node, depth=0 ):
            if node.nodeType in ( DOM.Node.TEXT_NODE, DOM.Node.CDATA_SECTION_NODE ):
                if len(node.nodeValue.strip()) == 0:
                    # Disposable whitespace node
                    return
            if node.nodeType == DOM.Node.COMMENT_NODE:
                return
            print( depth*' ', node.nodeName, repr(node.nodeValue) )
            if node.attributes is not None and len(node.attributes.keys()) > 0:
                print( depth*'  ', '(', ", ".join([ "%s=%r" % (k,v) for k,v in node.attributes.items() ]), ')' )
            nodeNames.add( node.nodeName )
            for c in node.childNodes:
                walk( c, depth+1 )
        walk( aDoc )

def convertFilePath( baseDir, aFile, dataeleFile="dataele.xml",
        codesFile="codes.xml" ):
    """Converts a single message file from XML to :mod:`X12.parse`."""
    return convertFile(open(os.path.join(baseDir, aFile)),
            open(os.path.join(baseDir, dataeleFile)),
            open(os.path.join(baseDir, codesFile)))


def convertFile(xml_file, data_ele_file, codes_file):
    log = logging.getLogger("tools.convertPyX12.convertFile")
    bp = ParserBuilder()
    try:
        xml = XMLParser()
        xml.data(data_ele_file)
        xml.codes(codes_file)
        xml.read(xml_file)
        return bp.build(xml)
    except Exception as e:
        log.error("Failed to convert %s: %s" % (xml_file.name, e))
        raise


def convertAll( baseDir ):
    """Convert all :file:`nnn*.4010.X*.xml` files in the given directory.
    
    :param baseDir: Directory with message definition, dataele and codes files.
    """
    for path,dirs,names in os.walk(baseDir):
        for fn in names:
            if fnmatch.fnmatch( fn, "[0-9][0-9][0-9]*.4010.X*.xml"):
                convertFilePath( path, fn )

def writeFile(aFile, name, x12, structure="flat"):
    """Write the x12 python module to a file.
    
    :param aFile: Filename of destination file.
    :type aFile: String
    :param name: The name of the generated class.
    :type name: String
    :param x12: The `X12.parse.Message` object to write.
    :type x12: `X12.parse.Message`
    """
    if structure == "nested":
        pyMap= PythonVisitor( name )
    else:
        pyMap= FlatPythonVisitor( name )
    x12.visit( pyMap )
    pySrc= pyMap.getSource()
    with open(aFile, 'w') as f:
        f.write("#\n# Generated by TigerShark.tools.convertPyX12 on %s\n#\n" % 
                datetime.now())
        f.write( pySrc )
        f.write( '\n\n' )


# Raise an XML warning to an error level.  This will spot extra tags.
warnings.simplefilter( "error", XMLWarning, 0 )
# Report empty loop warnings.  This will spot Loops with no Segments.
warnings.simplefilter( "always", EmptyLoopWarning, 0 )
# Report unknown data elements.
warnings.simplefilter( "always", UnknownElementWarning, 0 )
# Report extensions that aren't implemented yet.
warnings.simplefilter( "once", Extension, 0 )

if __name__ == "__main__":
    logging.basicConfig( stream=sys.stdout, level=logging.DEBUG )
    parser = argparse.ArgumentParser(
        description="Convert a PyX12 XML file to a python module.")
    parser.add_argument('x12_file', help="The x12 xml file to convert")
    parser.add_argument('py_file', help="The destination file.")
    parser.add_argument('-b', '--base_dir', dest="base_dir", default='.',
            help="Base directory containing the X12 xml, dataele.xml, and "\
                    "codes.xml files.")
    parser.add_argument('-s', '--structure', choices=['flat', 'nested'],
            default="flat", help="The structure of the resulting python "\
                    "class. Nested is easier to read, but may not compile "\
                    "due to too many object instantiations in a single "\
                    "call.")
    parser.add_argument('-n', '--name', help="The name of the generated "\
            "class. Defaults to the py_file argument, minus the filetype.")
    args = parser.parse_args()
    x12 = convertFilePath( args.base_dir, args.x12_file)
    if args.name is not None:
        name = args.name
    else:
        name = args.py_file.rsplit('/', 1)[1]
        name = name.split('.', 1)[0]
    writeFile(args.base_dir, args.py_file, name, x12, args.structure)
