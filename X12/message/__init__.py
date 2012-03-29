#!/usr/bin/env python
"""X12.message contains classes that are the default definitions of parts of
an X12 message instance.

An X12 message instance is a recursive construction of Loops, sub-Loops and Segments.
The leaf elements are always Segments.  For transmission, the Segment
leaves are flattened out; the loop structure is lost.

An X12 message instance is built by :mod:`X12.parse`.

Navigation
==========

The X12 message structure is a deeply nested collection of Loops and Segments.
Consquently, XPath-like functionality is helpful.  Literal XPath is a pain to
parse and process. However, a Pythonic set of methods and keyword arguments
can provide XPath-like features.

Each class, therefore has the following methods that correspond to XPath
axes: parent, child, ancestor, descendant.  [Optional: methods like following, preceding,
following_sibling, preceding_sibling, self, ancestor_or_self, descendent_or_self.]

Each method accepts a "node test" as a positional parameter.  Values are
simply the node type name, either Loop or Segment.

Each method has optional keywords which contains basically one expression.
the name="X" keyword is like :samp:`[@name=X]` in XPath.  The pos=n keyword is like :samp:`[n]`
in XPath.

Implementations
===============

Note that there are several alternative implementations:

-   This module, :mod:`X12.message`, which is pure Python.

-   The :mod:`web.claims.models` implementation, which is built using the
    Django ORM.

-   The :mod:`web.claims_837.models` implementation which has a
    complete set of X12Segments
    that reflect the various actual segment types used in :samp:`837`.

An :mod:`X12.message.sa` module could provde SQLAlchemy
mappings for the pure Python class definitions.

Consequently, a :class:`Factory` object is essential for building the correct
objects each alternative implementation.

Module Content
==============

This module contains the following class definitions.

    - :class:`Factory`.  Factory which builds object instances.

    - :class:`X12Structure`. Superclass for the resulting X12 message structure.

        - :class:`X12Message`.  The overall message -- a collection of Loops.

        - :class:`X12Loop`. A Loop is a collection of Segments and sub-Loops.

        - :class:`X12Segment`. A Segment is a collection of Elements and Composites.
          Segments names are essentially a type name; segments can be reused
          in a single Loop with different semantics.

        - X12Composite.  A Composite is a collection of Elements.  This is
          not actually implemented.

        - X12Element.  An atomic piece of data.  These are identified
          positionally within a segment's source text.

The generic definition of :class:`X12Segment` depends on having the :mod:`X12.parse`
definitions of the Segment,
Composite and Element available to interpret the strings of data associated
with each X12Segment.

If we want a more sophisticated, admin-friendly implementation, we have
to subclass :class:`X12Segment` for each unique kind of segment found in the X12
message definitions.  This is done in the Django and SQLAlchemy versions.

Since a Loop is just a kind of PK and sequence number
used to marshall a Message (and interpret the meaning of Segments), we
don't need to subclass Loop.

It's simplest to persist at the Segment level, with enough FK's and Occurance
identifiers to reconstruct a Loop from a sequence of Segments.

Details
=============

..  autoclass:: Factory
    :members:

..  autoclass:: X12Structure
    :members:

..  autoclass:: X12Loop
    :members:

..  autoclass:: X12Segment
    :members:

..  autoclass:: X12Message
    :members:
    
SQL Alchemy module
===========================

..  automodule:: X12.message.sa
"""

class Factory( object ):
    """Create the generic X12Message structures.

    This object is used by an :mod:`X12.parse` to unmarshall message
    text and create generic Python objects.

    Subclasses include

        - :class:`X12.message.sa` creates SQLAlchemy objects; these have endless
          subclasses for X12Segment.

        - :mod:`web.claims.models` creates Django objects.  The generic
          claims application uses a generic X12Segment implementation.

        - XXX future: :mod:`web.claims_837.models` will create Django objects;
          this version will have endless peer classes for X12Segment that
          carry the detailed element definitions.

    The "subclasses" are entirely a theoretical construct.  We don't *need*
    a properly polymorphic class hierarchy.
    """
    @staticmethod
    def makeMessage( name, *structure ):
        """Create a new X12Message object.
        :param name: name of this Message
        :param structure: the various Loops of this Message
        :returns: X12Message instance
        """
        return X12Message( name, *structure )
    @staticmethod
    def makeLoop( name, *structure ):
        """Create a new X12Loop object.
        :param name: name of this Loop
        :param structure: the various sub-Loops and Segments of this Loop
        :returns: X12Loop instance
        """
        return X12Loop( name, *structure )
    @staticmethod
    def makeSegment( segmentToken, compositeSep=":", segmentType=None ):
        """Create a new X12Segment object.
        :param segmentToken: the :class:`X12.parse.SegmentToken` created by the parser.
        :param compositeSep: Composite internal separator from the ISA segment.
        :param segmentType: an instance of :class:`X12.parse.Segment` which defines
        the Elements and Composites of this Segment.
        :returns: X12Segment instance
        """
        return X12Segment( segmentToken, segmentType )

class X12Structure( object ):
    """A piece of an X12 message structure.  This is the common superclass
    for X12Loop and X12Segment, allowing a recursive structure.

    :ivar name: name of this structure.
    :ivar thePosition: relative position within the parent.
    :ivar theParent: parent structure.
    :ivar occurrence: occurrence number for Loops or Segments which repeat.
    """
    def __init__( self, name ):
        self.name= name
        self.thePosition= 0
        self.theParent= None
        self.occurrence= 0
        self.theMessage= None
    def segs( self ):
        """Returns a flat list of Segments under this structure."""
        return NotImplemented
    def getMessage( self ):
        return self.theMessage
    def setMessage( self, aMessage ):
        self.theMessage= aMessage
    message= property( getMessage, setMessage )
    def matches( self, test, name=None, pos= None ):
        """The Xpath :samp:`self` axis"""
        testType= _test2type[test.lower()]
        if isinstance(self, testType ):
            c1, c2 = True, True
            if name is not None:
                c1= self.name == name
            if pos is not None:
                c2= self.thePosition == pos
            return c1 and c2
        return False
    def child( self, test, name=None, pos=None ):
        return NotImplemented
    def descendant( self, test, name=None, pos=None ):
        return NotImplemented
    def parent( self, test, name=None, pos=None ):
        """Examine the immediate parent of this node."""
        result= []
        if self.theParent.matches( test, name, pos ):
          result.append( self.theParent )
        return result
    def ancestor( self, test, name=None, pos=None ):
        """Examine nay ancestor of this node."""
        result= []
        if self.theParent:
            if self.theParent.matches( test, name, pos ):
                result.append( self.theParent )
            result.extend( self.theParent.ancestor(test,name,pos) )
        return result

class X12Loop( X12Structure ):
    """A Loop in an X12 message; it contains subloops and segments.
    This also the superclass for a Message, which includes Loops
    (but no Segments.)
    :ivar parts: sequence of component parts (subLoops or Segments)
    """
    def __init__( self, name, *parts ):
        """Create an X12Loop with a given name and list of X12Structure parts.
        :param name: name of this loop
        :param parts: (optional) list of parts to attach to this loop.
        """
        super(X12Loop,self).__init__( name )
        self.parts= []
        for p in parts:
            self.addChild( p )
    def __str__( self ):
        return "%s(%s)" % (
            self.name,
            ", ".join(map(str,self.parts)) )
    def getMessage( self ):
        return self.theMessage
    def setMessage( self, aMessage ):
        self.theMessage= aMessage
        for p in self.parts:
            p.message= aMessage
    message= property( getMessage, setMessage )
    def segs( self ):
        """Create a flat list of Segments under this Loop."""
        segList= []
        for p in self.parts:
            segList.extend( p.segs() )
        return segList
    def addChild( self, aPart ):
        """Add a child Loop or Segment to this Loop.
        Under some circumstances, we may need to propagate the message
        definition down into the lower levels of this structure.

        Note that this sets the message of the parts to the message
        associated with this Loop.  The message setting is recursive
        and assures that all subloops are also correctly associated with
        this message.
        """
        aPart.message= self.message
        aPart.theParent= self
        aPart.thePosition= len(self.parts) + 1
        self.parts.append( aPart )
    def child( self, test, name=None, pos=None ):
        """Examine immediate children of this node."""
        result= []
        for part in self.parts:
            if part.matches( test, name, pos ):
                result.append( part )
        return result
    def descendant( self, test, name=None, pos=None ):
        """Examine descendents of this node."""
        result= []
        for part in self.parts:
            if part.matches( test, name, pos ):
                result.append( part )
            result.extend( part.descendant(test,name,pos) )
        return result

class X12Segment( X12Structure ):
    """A segment in an X12 message, created by a parser from a segmentToken.
    :ivar elements: an instance of :class:`X12.parse.SegmentToken` which contains
    the individual Element values.
    :ivar segType: An optional instance of :class:`X12.parse.Segment` that provides
    names, data type properties for each Element of the Segment.
    """
    def __init__( self, segmentToken, segmentType=None ):
        """Create a Segment from a SegmentToken and a X12.parse.Segment definition.
        :param segmentToken: An :class:`X12.parse.SegmentToken` instance:
        a list-like collection of Element values.  It turns out that a simple
        list of values may also work, if it does NOT have trailing empty
        items omitted.  Real Segment Tokens can have trailing empty items
        omitted.
        :param segmentType: An :class:`X12.parse.Segment` instance, which
        defines the Elements and Composites of this X12Segment.
        """
        super(X12Segment,self).__init__( segmentToken[0] )
        self.elements= segmentToken
        self.segType= segmentType
    def __str__( self ):
        return str( self.elements )
    def bind( self, segment ):
        """Bind an :class:`X12.parse.Segment` to this data.
        :param segment: An :class:`X12.parse.Segment` instance
        """
        self.segType= segment
    def segs( self ):
        """Return this segment as a flat list of segments."""
        return [ self ]
    def getByPos( self, position ):
        """Get an element from this segment, by position.
        Positions appear to be numbered from 1.  Position 0 is
        the segment's name.
        :param position: the position of the element.
        :returns: string value in this position.  No type conversion is done.
        """
        return self.elements[int(position)]
    def setByPos( self, position, value ):
        """Set an element of this segment, by position.
        Positions appear to be numbered from 1.  Position 0 is
        the segment's name.
        :param position: the position of the element.
        :param value: String value to assign.  No type conversion is done.
        """
        while len(self.elements) <= int(position):
            self.elements.append("")
        self.elements[int(position)]= str(value)
    def positionOf( self, name ):
        """Locate the position of an element by name.
        :param name: name of the element.
        :returns: numberic position.
        """
        if self.segType is None:
            raise NotImplementedError( "No Segment bound to this data." )
        for en in range(len(self.segType.structure)):
            if name == self.segType.structure[en].name:
                return en+1
        raise ValueError( "Name %s Is Unknown in Segment %s" % ( name, self.name ))
    def getByName( self, name ):
        """Get an element from this segment, by name.
        :param name: the name of the element.
        :returns: string value in the element's position.  No type conversion is done.
        """
        return self.getByPos(self.positionOf(name))
    def child( self, test, name=None, pos=None ):
        """Examine immediate children of this node;
        segments have no children; the result is an empty list."""
        return []
    def descendant( self, test, name=None, pos=None ):
        """Examine all descendants of this node;
        segments have no children; the result is an empty list."""
        return []

class X12Message( X12Loop ):
    """An overall X12 Message: essentially a collection of Loops."""
    def __init__( self, *args ):
        super( X12Message, self ).__init__( *args )
        self.message= self
    def marshall( self, segSep="~", eltSep="*" ):
        """Marshall this message into an X12 string.
        :param segSep: (optional) Segment Terminator, usually :samp:`~`
        :param eltSep: (optional) Element Separator, usually :samp:`*`
        :returns: String with this X12 message marshalled
        """
        segments= self.segs()
        return segSep.join( [ eltSep.join( s.elements ) for s in segments ] ) + segSep
    def getCompositeSeparator( self ):
        """Returns the composite separator in :samp:`ISA16`.
        :returns: string value of the composite separator, often a :samp:`:`.
        """
        isaLoop= self.descendant( "segment", "ISA" )[0]
        return isaLoop.getByPos(16)

_test2type = { "loop" : X12Loop, "segment" : X12Segment, "message" : X12Message }
