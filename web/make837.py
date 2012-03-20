#!/usr/bin/env python
"""Build 837 parsers and 837 Segment definitions from XML Configuration.

Synopsis
========

:samp:`make837.py -p {python} -d {django} -b {baseDir} {name=source}...`

Description
===========

Reads the PyX12 source files (in .XML) and writes a Python parser module
for unmarshalling messages as well as a Django model for persisting the
message instances.

Prior to this step you must initialize the application directory
structure with :samp:`manage.py startapp {newApp}`.

After this step, you must update :file:`settings.py` to include the new application.

Then you must sync the database with the following command before you can start
using the parser, factory and Django persistent class definitions you've created.

:samp:`manage.py syncdb --pythonpath=".."`

Options
=======

    :samp:`-p {python}` writes the Python module for unmarshalling the given messages.

    :samp:`-d {django}` writes two Django modules for persisting the given message instances.
        This will be :samp:`{django}/models.py` and :samp:`{django}/admin.py`.

    :samp:`-b {baseDir}` is the base directory for the various source files.

    :samp:`name={source}` a list of parser names and message definitions.
    The name is the Python variable name; the source is the PyX12 XML source file.

Notes
=====

An X12 parser is defined to use a Factory object to emit message instance objects.
This Factory object is a run-time binding between a parser and some message instance module.
Generic message instance modules include :mod:`X12.message` and :mod:`web.claims.models`.

This application builds a specific message instance module, with specific message types.
In order for an :mod:`X12.parse` module to make use of the Django message instance module,
a Factory is required to instantiate the Django objects as well as the generic
X12Segment object defined in :mod:`web.claims.models`.
"""
from __future__ import print_function
import optparse
import tools.convertPyX12
import os
import logging
import sys
import datetime
import X12.map.source
import X12.map.dj

class ApplicationBuilder( object ):
    """Build the core parser and message persistence modules for
    an application.

    Generally, given a base directly, we'll load a number of XML files
    which will define X12N message parsers.  We have to emit a Python
    source module for each individual message type, since they have unique
    compliance rules.

    After seeing all of those XML files, we'll also know the various
    segments defined and can emit a peristence model for the unique
    kinds of segments.

    Note that the Django Visitor *accumulates* the various definitions.
    Only the last output from the Django Visitor is particularly useful.
    """
    def __init__( self, baseDir=None ):
        """Initialize the ApplicationBuilder with a base directory."""
        self.baseDir= baseDir if baseDir is not None else "."
        self.log= logging.getLogger( "make837.LoadXMLDefs")
        self.bldParser= tools.convertPyX12.ParserBuilder()
        # Accumulate Django definitions until after all messages have been examined
        self.djMap= X12.map.dj.DjangoModelVisitor( )
        self.djAdm= X12.map.dh.DjangoAdminVisitor( )
        self.x12p= None
    def load( self, xmlDef ):
        """Load another message definition.  This will also accumulate
        Django Segment definitions.
        """
        try:
            xml= tools.convertPyX12.XMLParser()
            xml.data( os.path.join( self.baseDir, "dataele.xml") )
            xml.codes( os.path.join( self.baseDir, "codes.xml") )
            xml.read( os.path.join( self.baseDir, xmlDef) )

            self.x12p= self.bldParser.build( xml )
        except Warning, w:
            log.warning( '*** WARNING IN %s', xmlDef )
            self.x12p= None
            raise
        self.pyCode= None
        self.x12p.visit( self.djMap )
        self.x12p.visit( self.djAdm )
        return self.x12p
    @property
    def getParser( self ):
        """Return the current message's parser object."""
        return self.x12p
    def getPython( self, name ):
        """Return Python source for the current message."""
        pyMap= X12.map.source.FlatPythonVisitor( name )
        self.x12p.visit( pyMap )
        self.pyCode= pyMap.getSource()
        return self.pyCode
    def getDjangoModel( self ):
        """Emit the Django model code built so far."""
        self.djangoModel= self.djMap.getSource()
        return self.djangoModel
    def getDjangoAdmin( self, appname='claims_837'):
        """Emit the Django Admin code built so far."""
        self.djangoAdmin= self.djAdm.getSource(appname)
        return self.djangoAdmin

factory='''
import web.claims.models
class Factory( web.claims.models.Factory ):
    """Factory for a generated application."""
    @staticmethod
    def makeSegment( segmentToken, compositeSep, segmentType=None ):
        """Create a Segment from a SegmentToken and an Segment definition.

        :param segmentToken: An :class:`X12.parse.SegmentToken` instance:
        a list-like collection of Element values.  It turns out that a simple
        list of values may also work, if it does NOT have trailing empty
        items omitted.  Real Segment Tokens can have trailing empty items
        omitted.
        :param compositeSep: Composite internal separator from the ISA segment.
        :param segmentType: An :class:`X12.parse.Segment` instance, which
        defines the Elements and Composites of this X12Segment.
        :returns: X12Segment instance
        """
        seg= web.claims.models.Factory.makeSegment( segmentToken, compositeSep, segmentType )
        appSegClass= eval( "Segment_%s" % ( segmentToken[0], ) )
        appSeg= appSegClass( segment= seg )
        appSeg.unmarshall( segmentToken, compositeSep )
        appSeg.save()
        return seg
'''

def process( baseDir=r"C:\Python25\share\pyx12\map" ):
    convertList= [
        ("parse_837i", "837.4010.x096.A1.xml"),
        ("parse_837d", "837.4010.x097.A1.xml"),
        ("parse_839p", "837.4010.x098.A1.xml"),
    ]
    # Load messages, generating Python as we go
    builder= ApplicationBuilder( baseDir )
    for parserName, fileName in convertList:
        builder.load( fileName )
        pySrc= builder.getPython( parserName )
        print( pySrc )
    # Write Django all in one final 'models' file
    print( factory )
    builder.getDjangoModel()
    print( builder.djangoModel )
    builder.getDjangoAdmin( 'claims_837' )
    print( builder.djangoAdmin )

def main():
    # Parse command-line options
    cmdParse= optparse.OptionParser(version="0.1")
    cmdParse.add_option( "-p", "--python", dest="python", default=None )
    cmdParse.add_option( "-d", "--django", dest="django", default=None )
    cmdParse.add_option( "-b", "--basedir", dest="baseDir", default="." )
    options, args = cmdParse.parse_args()
    now= datetime.datetime.now()
    builder= ApplicationBuilder( options.baseDir )
    if options.python is not None:
        with open(options.python, "w" ) as pFile:
            pFile.write( '#!/usr/bin/env python\n' )
            pFile.write( '"""Generated by make837.py on %s"""\n' % (now,) )
            for argText in args:
                parserName, punct, fileName = argText.partition( "=" )
                builder.load( fileName )
                if options.python is not None:
                    pySrc= builder.getPython( parserName )
                    pFile.write( "# %s/%s\n" % ( options.baseDir, fileName ) )
                    pFile.write( pySrc )
                    pFile.write( '\n\n' )
    if options.django is not None:
        with open( os.path.join(options.django,"models.py"), "w" ) as dFile:
            dFile.write( '#!/usr/bin/env python\n' )
            dFile.write( '"""Generated by make837.py on %s"""\n' % ( now,) )
            dFile.write( factory )
            dFile.write( '\n\n' )
            djSrc= builder.getDjangoModel( options.django )
            dFile.write( djSrc )
            dFile.write( '\n\n' )
        with open( os.path.join(options.django,"admin.py"), "w" ) as dFile:
            dFile.write( '#!/usr/bin/env python\n' )
            dFile.write( '"""Generated by make837.py on %s"""\n' % ( now,) )
            djSrc= builder.getDjangoAdmin( options.django )
            dFile.write( djSrc )
            dFile.write( '\n\n' )

if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.DEBUG,
    )
    logging.getLogger("tools.convertPyX12.BuildParser").setLevel(logging.INFO)
    #process()
    main()
