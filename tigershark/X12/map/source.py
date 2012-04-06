#!/usr/bin/env python
"""The X12.map.source module emits Python source definitions from an :mod:`X12.parse` structure.

There are two flavors of Python source that can be produced:

    -   :class:`PythonVisitor` creates a single definition.
        A single Python constructor defines the entire message.

    -   :class:`FlatPythonVisitor` builds a flat definition.
        A number of individual constructors are assembled
        into a workable parser.

See :ref:`traversal` for notes on the **Visitor** design pattern.

..  autoclass:: PythonVisitor
    :members:

..  autoclass:: FlatPythonDetails
    :members:

..  autoclass:: FlatPythonVisitor
    :members:
"""

from tigershark.X12.parse import StructureVisitor
from tigershark.X12.parse import StopDescent

class PythonVisitor( StructureVisitor ):
    """Builds a single, huge definition.  Not very practical except
    for TINY messages.  Or if you set :py:data:`skipElement`
    to True, the resulting structure might be useful.

    :ivar skipElement: normally False, you can set this to True
        to produce a Segment-level message summary.
    """
    def __init__( self, varName, *args, **kw ):
        """Create a Python Visitor.
        :param varName: the name of the Python variable we'll product.
        """
        super( PythonVisitor, self ).__init__( *args, **kw )
        self.result= []
        self.varName= varName
        self.skipElement= False # change to True to prune tree, skipping elements
    def preMessage( self, msg, indent=0 ):
        self.result.append( "from tigershark.X12.parse import Message, Loop, Segment, Composite, Element, Properties" )
        if self.varName is None: self.varName= "x%s" % ( msg.name, )
        self.result.append( "%s = Message( %r, %r, " % ( self.varName, msg.name, msg.props ) )
    def postMessage( self, msg, indent=0 ):
        self.result.append( ")" )
    def preLoop( self, aLoop, indent=0 ):
        """Report this Loop.
        :param aLoop: a :class:`X12.parse.Loop` structure.
        :param indent: the indentation level.
        """
        self.result.append( indent*'  ' + "Loop( %r, %r, " % (aLoop.name, aLoop.props,) )
    def postLoop( self, aLoop, indent=0 ):
        self.result.append( indent*'  ' + ")," )
    def preSegment( self, aSegment, indent=0 ):
        """Report this Segment."""
        self.result.append( indent*'  ' + "Segment( %r, %r," % (aSegment.name, aSegment.props,) )
    def postSegment( self, aSegment, indent=0 ):
        self.result.append( indent*'  ' + ")," )
    def preComposite( self, aComposite, indent=0 ):
        """Report this Composite.  Configured by the :py:data:`skipElement` variable."""
        if self.skipElement:
            return
        self.result.append( indent*'  ' + "Composite( %r, %r," % (
            aComposite.name, aComposite.props ) )
    def postComposite( self, aComposite, indent=0 ):
        """Report this Composite.  Configured by the :py:data:`skipElement` variable."""
        if self.skipElement:
            return
        self.result.append( indent*'  ' + ")," )
    def postElement( self, anElement, indent=0 ):
        """Report this Element.  Configured by the :py:data:`skipElement` variable."""
        if self.skipElement:
            return
        elt= anElement
        self.result.append( indent*'  ' + "Element( %r, Properties(desc=%r, req_sit=%r, data_type=(%r,%r,%r), position=%d," % (
            elt.name, elt.desc, elt.req_sit, elt.type_name, elt.min_len, elt.max_len, elt.position ) )
        self.result.append( indent*'  ' + "  codes=%r ) )," % (
            elt.codes, ) )
    def getSource( self ):
        return "\n".join( self.result )

class FlatPythonDetails( PythonVisitor ):
    """Definitions, of Segment, Composite and Element.
    Messages and Loops are silently ignored.  They're handled by
    another visitor that scans the "top" of the structure.
    This Visitor is only used within a Loop or Message.
    """
    def preMessage( self, msg, indent= 0 ):
        pass
    def postMessage( self, msg, indent= 0 ):
        pass
    def preLoop( self, loop, indent=0 ):
        self.result.append( "%s_%s," % ( self.varName, loop.name, ) )
        raise StopDescent # prevent expansion of the Loop we just referenced
    def postLoop( self, loop, indent=0 ):
        pass

class FlatPythonVisitor( StructureVisitor ):
    """Decompose ALL Loops into separate definitions which can be referenced.
    This Visitor doesn't process Segments, Composites and Elements.
    It only looks at Messages and Loops.
    """
    def __init__( self, varName, *args, **kw ):
        super( FlatPythonVisitor, self ).__init__( *args, **kw )
        self.result= []
        self.varName= varName
    def preMessage( self, msg, indent=0 ):
        self.result.append( "from tigershark.X12.parse import Message, Loop, Segment, Composite, Element, Properties" )
    def postMessage( self, msg, indent=0 ):
        if self.varName is None: self.varName= "x%s" % ( msg.name, )
        self.result.append( "%s = Message( %r, %r, " % ( self.varName, msg.name, msg.props ) )
        for s in msg.structure:
            details= FlatPythonDetails( self.varName )
            # for Segment, Composites, etc., this involves a full pre-/post- visit
            # for Loops, however, it's a reference to a previous post- definition
            s.visit( details )
            self.result.extend( details.result )
        self.result.append( ")" )
    def preLoop( self, aLoop, indent=0 ):
        pass
    def postLoop( self, aLoop, indent=0 ):
        """Loop with References to stuff defined during pre-processing."""
        self.result.append( "%s_%s = Loop( %r, %r, " % ( self.varName, aLoop.name, aLoop.name, aLoop.props ) )
        for s in aLoop.structure:
            details= FlatPythonDetails( self.varName )
            s.visit( details )
            self.result.extend( details.result )
        self.result.append( ")" )
    def getSource( self ):
        return "\n".join( self.result )
