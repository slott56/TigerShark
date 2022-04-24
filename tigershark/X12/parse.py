#!/usr/bin/env python
"""X12.parse defines classes to build an X12 message parser.

An :class:`X12.parse.Parser` object participates in several use cases.

    1.  It is used to unmarshall X12 message text and create a message
        instance, :class:`X12.message.X12Message` structures, from that text.

    2.  It can help marshall an X12 message, since it
        contains some important structural information.  As a
        practical matter, the :mod:`X12.message` module does
        this by itself, since marshalling is a relatively simple
        matter of assembling the :class:`X12.message.X12Segment` data
        in the right order.

    3.  It also describes a message's structure.  It can
        describe the message structure in a variety of notations.
        All of these are essentially metadata about the message.
        Not the message instance itself.

The :mod:`X12.map` package provides a number of mappings
that convert a :class:`Message` structure definition to other notations.  These
include Python source, SQL, SQLAlchemy and Django definitions.

Unmarshall/Parsing
==================

The typical usage is something like the following::

    from tigershark import X12
    import x278

    ... read some text into txt ...
    x12Msg= x278.x278_message.unmarshall( txt )
    ... process the resulting x12Msg structure.

In unusual cases, you may have a stream of messages of multiple types.
In this case, you'll might want to scan the message's headers before
attempting to parse.  The :func:`preParse` function helps do this.

The alternative is to attempt parsing with various
message definitions.  Since each contains a built-in compliance check,
a failure to parse means that the input is not a match fot the given
message structure.  This is relatively slow.

Marshalling
===========

An :class:`X12.message.X12Message` has a marshall method that emits the X12
text.

Structure Description
=====================

There are several languages used to emit message structure.  Each of these
is module in :mod:`X12.map`.  These are based on a subclass of
:class:`StructureVisitor` that does the dirty work of emitting
proper text for each piece of the overall message structure.

    - Python, :mod:`X12.map.source`

    - Django ORM, :mod:`X12.map.dj`

    - SQL DDL, :mod:`X12.map.SQL`

    - SQLAlchemy ORM, XXX - Future

These are all prepared by a number of **Visitor** pattern class definitions.
Each subclass of :class:`StructureVisitor` emits a different representation of the
parser.

Definitions In This Module
==========================

An X12 Parser is built as a collection of parsers for each part of a message. It
includes an overall Message parser, plus a Loop parser and a Segment parser.
These components are structured to reflect the message they are designed to
parse.

The following classes define the structure of an X12 message. A Message object
is a parser for a given structure.

    - :class:`Parser`. Superclass for elements of an X12 Parser.

        - :class:`Segment`. Definition of a segment, builds an :class:`X12.message.X12Segment`
          object when parsing input.  Segments consist of Elements and Composites.

        - :class:`Loop`. Parse a Loop, builds an :class:`X12.message.X12Loop` object.
          Loops consist of Segments and Loops.

        - :class:`Message`. Parse a complete message, building an :class:`X12.message.X12Message`
          for the overall message.  A Message consists of Loops.

        - :class:`Element`. A bottom-level, atomic, leaf data element. The individual
          Elements aren't parsed -- they're available within the
          :class:`X12.message.X12Segment` based on their positions.

        - :class:`Composite`.  A composite of two or more Elements.  Composites
          are broken down with further parsing rules.  The ISA16 field
          (Subelement Separator) defines the punctuation that separates
          subelements of a Composite.

    - :class:`Properties`.  A flexible container for properties of any
      of the above structures.

    - :class:`SegmentToken`.  A list-like object that extends the built-in
      list type so that it returns :samp:`None` past the end of the list,
      rather than an exception.

Each sub-structure of a Loop (Segment and Loop) is effectively a type (the Loop name
or Segment name) and requires an instance number, as well as a sequential position
in the original message.

We must use at least the lead-off Segment to recognize the beginning of each
kind of Loop. This is a "look-ahead" match. For the match to be true,
a Loop has to delegate matching to the Segments or subLoops it contains.
Eventually any nested subLoops would bottom-out at a Segment that could actually
perform the match.  [Apparently, the X12 standard begins each Loop with one or
more Segments, so the recursive matching doesn't actually occur.]

A convenience function, :func:`scan`, examines the message to get some basic
identification.  This can save matching the message against each possible
alternative definition to see what parses.

Exceptions defined in this module.

    - :class:`ParseError`. The input message doesn't have the expected structure.

    - :class:`StructureError`.  You're attempting to build a parser with an illegal
      structure.  Usually, you're trying to put something inside
      an Element.

The object definition syntax in Python enfoces some style conventions
on how we want our message structure declaration to look.

The X12 Parsing Algorithm
=========================

    1.  Examine the ISA segment.

        ISA is followed by the field-level punctuation mark.
        Pick apart the ISA record to find a number of fields, including the
        definitions of the other punctuation marks which are used.
        Last characters in this segment (:samp:`~` or :samp:`~\\n`) define the segment punct.

    2.  Examine the GS, ST segments, also.  This completes the header.

    3.  A message is a sequence of LOOPS, defined by the
        transaction type in the ST header.

        In some cases, there may be an
        additional segment along with ST that defines a transaction subtype.

            - Each Loop will have a series of Segments and SubLoops.

                - Each Segment will have a fixed sequence of Elements
                  and Composites.
                  Composites have SubElements.

    4.  End with SE, GE and IEA segments which bracket the ST, GS and ISA.

Building a Parser
=================

Here's a top-level Message declaration::

    nameParser= Message( "name", Properties(desc="description"), ... )

Where *name* is the X12N name, and *description* is the descriptive text.

The remaining argument values must be Loop instances.  For small messages
these can be right in the constructor.  For most messages, however, these
must be separate sub-parser constructors.

They look like this::

    loop_2010A= Loop( "name", Properties(...), ... )

Where *name* is the X12N name. The remaining argument values must be Segment and Loop instances.

Simple, obvious indentation is very helpful.

X12 Codes
=========

X12 is filled with odd codes.  Here are some.

Formatting:

    - "D8"  Date CCYYMMDD
    - "D6"  Date YYMMDD
    - "RD8"  Date Range CCYYMMDD-CCYYMMDD
    - "TM"  Time HHMM

Syntax:

    - pattern built from (E|L|P|C|R)([0-9]{2}){2,20}  Example L040203.

Data Types:

    - "N", "N0", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9" - Numeric
    - "R" - Decimal
    - "ID" - An ID
    - "AN" - Alphanumeric
    - "DT" - Date
    - "TM" - Time
    - "B" - Binary?

Class Definitions
==================

..  autoclass:: SegmentToken
    :members:

..  autoclass:: StopDescent
    :members:

..  autoclass:: StructureVisitor
    :members:

..  autoclass:: ParseError
    :members:

..  autoclass:: StructureError
    :members:

..  autoclass:: Properties
    :members:

..  autoclass:: Parser
    :members:

..  autoclass:: Element
    :members:

..  autoclass:: Composite
    :members:

..  autoclass:: Segment
    :members:

..  autoclass:: Loop
    :members:

..  autoclass:: Message
    :members:

..  autofunction:: scan

..  autofunction:: preParse
"""
from __future__ import print_function
import logging

# This is only to give us access a default Factory.
from tigershark.X12.message import Factory as MessageFactory

class SegmentToken( object ):
    """A list-like object that gracefully handles a Segment with missing elements.

    When parsing an X12 message, each Segment is a discrete token.

    The X12 standard (apparently) permits eliding all empty Elements at the
    end of a Segment.  This eliminates a lot of trailing punctuation.
    It also means that we either need to know the defined length of the Segment,
    or we have to be tolerant of asking for the value of an Element that was
    not explicitly provided.
    """
    def __init__( self, *values ):
        """Build a SegmentToken from individual values.
        The values can either be a list or tuple of values,
        or the complete set of positional arguments will be taken
        as the values int the SegmentToken.
        """
        if len(values) == 1 and type(values) in (list, tuple):
            self.elements= values[0]
        else:
            self.elements= values
    def __getitem__( self, position ):
        """Return the requested item or ''."""
        return self.elt(position)
    def elt( self, position ):
        """Return the requested item or ''."""
        return self.elements[position] if position < len(self.elements) else ''
    def subElt( self, position, punct, subPos ):
        if position < len(self.elements):
            compElements= self.elements[position].split(punct)
            if subPos < len(compElements):
                return compElements[subPos]
        return ''
    def __iter__( self ):
        return iter(self.elements)
    def __len__( self ):
        return len(self.elements)
    def __repr__( self ):
        return "[%s]" % ( ", ".join( map(repr,self.elements)))
    def __str__( self ):
        return str( self.elements )

class StopDescent( Exception ):
    "Not an error -- like Stop Iteration, it interrupts visiting."
    pass

class StructureVisitor( object ):
    """A **Visitor** which can traverse the Message structure,
    and emit appropriate messages with each piece of the structure.
    Subclasses produce python source, SQL DDL, SQLAlchemy ORM,
    and Django ORM from the message structure.

    We have the following combinations.

        - pre\ *class* methods are lead-ins to definitions.
          In some cases, this can iterate through children producing
          child definitions which this object will reference.

        - post\ *class* methods are completion of definitions.
          In some cases, these are references to previous definitions.
    """
    def preMessage( self, aMessage, indent ):
        pass
    def postMessage( self, aMessage, indent ):
        pass
    def preLoop( self, aLoop, indent ):
        pass
    def postLoop( self, aLoop, indent ):
        pass
    def preSegment( self, aSegment, indent ):
        pass
    def postSegment( self, aSegment, indent ):
        pass
    def preElement( self, anElement, indent ):
        pass
    def postElement( self, anElement, indent ):
        pass
    def preComposite( self, aComposite, indent ):
        pass
    def postComposite( self, aComposite, indent ):
        pass

class ParseError( Exception ):
    """Error found while unmarshalling a message instance."""
    def __init__( self, text, **details ):
        super( ParseError, self ).__init__( text )
        self.details= details
    def log( self, aLog ):
        aLog.error( "--- Parse Error ---")
        aLog.error( "Message: %s", self.args[0] )
        for k in self.details:
            aLog.error( "%s: %r", k, self.details[k] )
        aLog.error( "-------------------")

class StructureError( Exception ):
    """Error found while attempting to define a Parser."""
    pass

class Properties( object ):
    """A flexible dictionary-like collection of property values.
    Each property becomes an attibute of the resulting object.
    """
    def __init__( self, **kw ):
        self.repr= ",".join( [ "%s=%r" % (k,v,) for k,v in kw.items() ] )
        self.__dict__.update( kw )
    def __repr__( self ):
        return "%s(%s)" % (self.__class__.__name__, self.repr,)
    def __getattr__( self, name ):
        return None

class Parser( object ):
    """Superclass for definition of X12 Structure-Driven Parsers.

    There are several subclasses to parse elements of the X12 message structure:

        - :class:`Element` matches an element's value to support recognition of the
          Segment.

        - :class:`Composite` contains sub-Element's; matches a collection of
          sub-Element values to support recognition of the Segment.

        - :class:`Segment` contains Elements and Composites; is matched; creates
          an :class:`X12.message.X12Segment` in the resulting message structure.

        - :class:`Loop` contains Segments and sub-Loops; relies in Segment matching
          to recognize which Loop is being parsed; creates an :class:`X12.message.X12Loop`
          in the resulting message structure.

        - :class:`Message` contains Loops; relies on Loop parsing (which relies
          Segment match); creates an :class:`X12.message.X12Message` structure.

    Message parsing breaks the source message down into
    a flat list of segment tokens.  Then the structure defined
    by Segment, Element and Loop is imposed on those segment tokens.
    to build the X12Message from X12Loop and X12Segment.

    There are several properties:

        - path - the Path to this structure within the Message

        - message - the top-most Message

        - factory - the Factory used to generate X12Message instances

    :cvar valid_types: the list of valid types for the sub-structure
        within this structure.  For example a Message has valid types
        of Loop.  Loop has valid types of Loop and Segment.

    :ivar name: X12 ID for this structure.

    :ivar props: Properties.  Varies with the type.  Usually contains
        description, required/situational/not used, repeat count, etc.

    :ivar structure:  Structure.  A sequence of sub-structure declarations.

    :ivar occurance:  An occurance count within the parent of segments with
        the same type.  Some Segment types are reused.

    :ivar parent: The parent structure.  For Messages, this is None.

    :ivar position: the position within the parent.  Generally, this is inferred
        from the structure of loops and segments.  However, it can be forced in when
        we are missing Element definitions and just need one to identify a Segment.

    :ivar theFactory: the Factory used to generate X12Message instances.
    """
    valid_types = ()
    segmentHeader= 1
    def __init__( self, name, properties=None, *parts ):
        """Build a simple structure of sub-elements.
        
        :param name: the X12 ID for this structure (Message, Loop, Segment, Element)
        :param properties: a Properties object with the description, etc.
        :param parts: Sub-Parsers that belong to this Parser.
        """
        self.name= name
        self.props= properties if properties else Properties(desc=name)
        self.structure= []
        self.occurance= None
        self.position= self.props.position
        self.parent= None
        self.theFactory= None
        if type(name) not in ( str, unicode, None ):
            raise StructureError( "Possible missing parameter: name")
        if type(properties) != Properties:
            raise StructureError( "Possible missing parameter: properties")
        for part in parts:
            if type(part) not in self.valid_types:
                raise StructureError( "Unexpected %r inside %r" % ( part, self.__class__.__name__ ) )
            self.append( part )
    def getMessage( self ):
        if self.parent:
            return self.parent.getMessage()
        return self
    message= property( fget= getMessage, doc="The top-most Message" )
    def getPath( self ):
        p= [ self.name ]
        top= self
        while top.parent is not None:
            top= top.parent
            p.insert( 0, top.name )
        return "/".join( p )
    path= property( fget= getPath, doc="Path from message to this structure")
    def getFactory( self ):
        return self.theFactory
    def setFactory( self, aFactory ):
        self.theFactory= aFactory
        for s in self.structure:
            s.factory= aFactory
    factory= property( fget=getFactory, fset=setFactory, doc="Factory to create message instances")
    def isLast( self ):
        if self.parent is None: return False
        return self == self.parent.structure[-1]
    def append( self, aChild ):
        """Append a child to this Parser's structure.
        :param aChild: a sub-structure parser.
        """
        aChild.parent= self
        if aChild.position == None:
            aChild.position= self.segmentHeader+len(self.structure)
        previous = [ p for p in self.structure if p.name == aChild.name ]
        aChild.occurance= len(previous)
        aChild.total_occurs= 1+len(previous)
        self.structure.append( aChild )
        for p in previous:
            p.total_occurs= 1+len(previous)
    def getParts( self, segments, theLoop ):
        """Get the parts of the current structure we're parsing.
        For each piece of our structure, evalute the :meth:`parse()` method to see if
        it can be parsed.  If so, append the part.

        This is inherited by Loop, Message and Segment.
        It is overridden by Element, since it has no parts.

        To handle repeating Loops, we must repeatedly call the parser until it fails, and
        keep track of the sequence of Loops.

        This repeat factor also applies
        to Segments which can repeat within a Loop.

        :param segments: list of SegmentToken instances
        :param theLoop: X12.message.X12Loop structure we're building.
        """
        for part in self.structure:
            count= 0
            for subloop in part.parse( segments ):
                subloop.occurrence= count
                theLoop.addChild( subloop )
                count += 1
    def visit( self, visitor, indent=0 ):
        """Iterate through the components."""
        try:
            self.preVisit( visitor, indent )
        except StopDescent, s:
            return
        for s in self.structure:
            s.visit( visitor, indent+1 )
        self.postVisit( visitor, indent )
    def preVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        raise NotImplementedError
    def postVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        raise NotImplementedError

class Element( Parser ):
    """An Element within a Segment.
    There's no internal structure, just a name and Properties.
    """
    def __init__( self, name, properties,):
        super( Element, self ).__init__( name, properties )
        self.desc= self.props.desc
        self.req_sit= self.props.req_sit # ( Required, Situational, Not Used )
        if self.props.data_type:
            self.type_name, self.min_len, self.max_len = self.props.data_type
        else:
            self.type_name, self.min_len, self.max_len = None, None, None
        self.codes= self.props.codes
        self.sqlName= self.name.replace("-","_")
    def __repr__( self ):
        return "Element( %r, Properties(desc=%r, req_sit=%r, data_type=(%r,%r,%r), position=%r, codes=%r))" % (
            self.name, self.desc, self.req_sit,
            self.type_name, self.min_len, self.max_len,
            self.position, self.codes, )
    def append( self, value ):
        raise StructureError( "Can't append to an Element")
    def getParts( self, segments, theLoop ):
        """When asked to get parts of an Element, nothing happens."""
        pass
    def match( self, candidate ):
        """Does this Element match the candidate SegmentToken's element?"""
        if self.req_sit in ( 'S', 'N' ): return True
        if len(self.codes) == 1:
            return candidate[self.position] in self.codes
        # Respecting valid_codes causes me nothign but headaches!
        return True
    def logMatch( self, candidate ):
        return "%s in %r" % ( candidate[self.position], self.codes )
    def preVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.preElement( self, indent )
    def postVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.postElement( self, indent )

class Composite( Parser ):
    """A Composite contains one or more sub-Elements.
    Composites require a punctuation mark to further decompose the data
    for their consituent Elements.
    The extra punctuation comes from the Messaage's ISA Segment, Element
    ISA16.  We can be allocated this tidbit by a parser (or manual construction),
    or search back up through the Message structure to find it.
    """
    valid_types = (Element,)
    segmentHeader = 0 # Unlike a full Segment, Composites have no header Element
    def __init__( self, name, properties, *elements ):
        super( Composite, self ).__init__( name, properties, *elements )
        self.desc= self.props.desc
        self.req_sit= self.props.req_sit
        self.seq= self.props.seq
        self.sqlName= self.name.replace("-","_")
        self.log= logging.getLogger( "X12.parse.Composite" )
    def getCodes( self ):
        return [ s.codes for s in self.structure ]
    codes= property( fget= getCodes, doc="Union of all codes in all subelements")
    def __repr__( self ):
        structure= ", ".join( map(repr,self.structure) )
        return "Composite( %r, Properties(desc=%r, req_sit=%r, seq=%r, position=%d,), %s )" % (
            self.name, self.desc, self.req_sit, self.seq, self.position, structure )
    def getCompositePunct( self ):
        return self.getMessage().compPunct
    def match( self, candidate ):
        """Check the individual Elements that make up this Composite."""
        if self.req_sit in ( 'S', 'N' ): return True
        if candidate[self.position] == '' and len(self.structure) == 0:
            return True # special case of empty Composite definition.
        punct= self.getCompositePunct()
        compositeData= SegmentToken( candidate[self.position].split( punct ) )
        self.log.debug( "Match Composite %s: %s", self.path,
            " and ".join(
                [se.logMatch(compositeData) for se in self.structure] ) )
        m= all( [se.match(compositeData) for se in self.structure] )
        # TODO return m?
        return True
    def logMatch( self, candidate ):
        if candidate[self.position] is None:
            return "seg[%s] None" % ( self.position, )
        punct= self.getCompositePunct()
        compositeData= SegmentToken( candidate[self.position].split( punct ) )
        return "%r matches %r" % ( compositeData, [ e.name for e in self.structure ] )
    def preVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.preComposite( self, indent )
    def postVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.postComposite( self, indent )

class Segment( Parser ):
    """Structure of an individual Segment of a message."""
    valid_types = (Element,Composite,)
    def __init__( self, name, properties, *elements ):
        """Build a Segment Definition.
        A segment contains one or more Elements.
        Some elements are required to positively identify the Segment/Loop
        structure of a message.  These elements act qualifiers.  The qual
        property is a kind of short-hand for specifying this special-purpose
        Element within the Segment.

        :param name: The X12 name for this segment.
        :param properties:  The following properties:
        qual=None, desc=None, req_sit="R", repeat=None
        :param elements: The Elements or Composites within this Segment
        """
        super( Segment, self ).__init__( name, properties, *elements )
        self.log= logging.getLogger( "X12.parse.Segment" )
        self.desc= self.props.desc
        self.required= self.props.req_sit == 'R'
        self.situational= self.props.req_sit == 'S'
        self.notused= self.props.req_sit == 'N'
        self.repeat= self.props.repeat if self.props.repeat is not None else "1"
    def __repr__( self ):
        structure= ""
        if self.structure:
            structure= ", ".join( map(repr,self.structure) )
        return "%s(%r, %r, %s)" % ( self.__class__.__name__, self.name, self.props, structure )
    def genMatchElements( self ):
        for s in self.structure:
            if len(s.codes) > 0:
                yield s
    def getOptionality( self ):
        if self.required:
            return "REQUIRED"
        else:
            return "OPTIONAL"
    optionality= property( getOptionality )
    def match( self, candidate ):
        """Does this segment match the candidate segment in the input?
        Two parts: does the name match and do the data elements match?
        """
        matchName= candidate[0] == self.name
        self.log.debug( "Match %s: %s", self.path,
            " and ".join(
                [me.logMatch(candidate) for me in self.genMatchElements()] ) )
        matchData= all( [me.match(candidate) for me in self.genMatchElements()] )
        return matchName and matchData
    def parse( self, segments ):
        """If this segment matches the next segment token in the input,
        create the X12Segment object.
        :param segments: list of SegmentTokens for the current message.
        :returns: yields a single parsed Segment or raises StopIteration
        """
        try:
            if self.repeat.startswith(">"):
                repeat = 999
            else:
                repeat = int(self.repeat)
        except:
            repeat = 1
        for i in range(repeat):
            if self.match( segments[0] ):
                compPunct= self.getMessage().compPunct
                theSegment= self.theFactory.makeSegment( segments.pop(0), compPunct, self )
                yield theSegment
            elif self.situational or self.notused:
                raise StopIteration
            else:
                error= ParseError(
                    "Could not unmarshall {seg_name} Segment, "\
                        "{ele_name} Element. Got {segment}".format(
                            seg_name=self.name,
                            ele_name=segments[0][0],
                            segment=segments[0]),
                    description=self.message.desc, parser=self, segments=segments )
                raise error
    def preVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.preSegment( self, indent )
    def postVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.postSegment( self, indent )

class Loop( Parser ):
    """Structure of a Loop: a sequence of Segments and sub-Loops."""
    def __init__( self, name, properties, *segments ):
        """Build a Loop Definition.
        :param name: The X12 name for this loop.
        :param properties:  The following properties:
        desc=None, req_sit="R", repeat=None
        :param segments: The Segments within this Loop
        """
        super( Loop, self ).__init__( name, properties, *segments )
        self.log= logging.getLogger( "X12.parse.Loop" )
        self.desc= self.props.desc
        self.required= self.props.req_sit == 'R'
        self.situational= self.props.req_sit == 'S'
        self.notused= self.props.req_sit == 'N'
        self.repeat= self.props.repeat
    def __repr__( self ):
        structure= ", ".join( map(repr,self.structure) )
        return "%s(%r, %r, %s)" % ( self.__class__.__name__, self.name, self.props, structure, )
    def parse( self, segments ):
        """Parse the current Loop.
        Append each part.  Return the parsed Loop.
        Note that loops may repeat (the property will have a "usage" of "R"
        and a repeat count > 1).

        To handle repeating Loops:
        This is a generator that yields multiple values; it will keep yielding
        loops until a segment no longer matches.

        :param segments: list of SegmentToken instances
        :returns: Yields the next X12.message.X12Loop structure or raises StopIteration
        """
        # Confirm match between this loop and a segment of the structure
        i = 0
        while len(segments) > 0 and i < len(self.structure):
            self.log.debug("Check {path}: {structure} {segments}".format(
                path=self.path,
                structure=self.structure[i].name,
                segments=segments[0]))
            if self.structure[i].match(segments[0]):
                self.log.debug("Consume {path}: {structure}".format(
                    path=self.path,
                    structure=[s.name for s in self.structure]))
                theLoop = self.theFactory.makeLoop(self.name)
                self.getParts(segments, theLoop)
                yield theLoop
            elif self.structure[i].situational and \
                    segments[0][0] in [s.name for s in self.structure]:
                # Absence of a situational segment shouldn't exit
                # Can't pop because it destroys the structures before they
                # get used
                i += 1
            else:
                # Nothing left to check, so stop the iteration
                raise StopIteration

    def match( self, candidate ):
        return self.structure[0].match( candidate )
    def preVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.preLoop( self, indent )
    def postVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.postLoop( self, indent )

# To support recursion, this must be set outside the class
# definition.
Loop.valid_types = ( Loop, Segment )

class Message( Parser ):
    """Structure of an entire message.

    :ivar desc: descriptions

    :ivar eltPunct: Found Element punctuation, usually :samp:`*`
        This is found after the "ISA" in the first segment of the message.

    :ivar segPunct: Found Segment punctuation, usually :samp:`~`
        This is found at the end of element 16 of the first, ISA, segment of
        the message.

    :ivar compPunc: Defined Composite punctuation, usually :samp:`:`.
        This is defined in field 16 (ISA16) in the first, ISA, segment of
        the message.

    :ivar segments: Working list of SegmentTokens for this message.
        When we're done parsing, this is an empty list.
    """
    valid_types= ( Loop, )
    def __init__( self, name, properties, *loops ):
        """Build a parser for a given X12 message structure.
        
        :param name: Name of this message.
        :param properties: instance of :class:`X12.parse.Properties` with Message
            properties.  Currently, only the :samp:`desc` property is used.
        :param loops: sequence of individual :class:`X12.parse.Loop` definitions
        :raises StructureError: if the attempted message structure is invalid.
        """
        super(Message,self).__init__( name, properties, *loops )
        self.log = logging.getLogger("X12.parse.Message")
        self.desc= self.props.desc
    def __repr__( self ):
        structure= ",\n".join( map(repr,self.structure) )
        return "%s( %r, %r, %s )" % ( self.__class__.__name__, self.name, self.props, structure, )
    @staticmethod
    def tokenize( msg ):
        """Decompose the message into a flat list of segment tokens.
        Note that most ISA's are 105 characters long; effectively
        a fixed-length header.
        """
        if msg[:3] != "ISA":
            raise ParseError( "Missing ISA Segment in Header", )
        eltPunct= msg[3]
        fields= msg.split(eltPunct)[:17] # 16 ISA fields
        #print( fields )
        compPunct= fields[16][0] # Composite Elements
        segPunct= fields[16][1:-2] # This will tend to de-wrap messages, too
        nextField= fields[16][-2:]
        if nextField != "GS":
            raise ParseError(
                "Missing GS Segment (can't reason out punctuation)", )
        return eltPunct, compPunct, segPunct, [
            SegmentToken( seg.split(eltPunct) )
                for seg in msg.split( segPunct )
                    if len(seg) > 0]
    def unmarshall( self, message, factory=MessageFactory ):
        """Unmarshall the text version of an X12 message
        into a structure defined by the given factory.
        
        :param message: X12 source text
        :param factory: A message instance Factory, by default :class:`X12.message.Factory`.
        :returns: :class:`X12.message.X12Message` structure
        :raises ParseError: if the message does not fit this parser's structure.
        """
        self.factory= factory
        try:
            self.eltPunct, self.compPunct, self.segPunct, self.segmentTokens= self.tokenize(message)
        except ParseError, ex:
            ex.details= dict(
                description= self.desc,
                parser= self,
                message= None
            )
            raise ex
        theMssg= self.factory.makeMessage( self.name )
        self.getParts( self.segmentTokens, theMssg )
        if len(self.segmentTokens) != 0:
            names= ", ".join( s[0] for s in self.segmentTokens )
            raise ParseError(
                "Extra segments {0!r}".format( names ),
                description=self.desc, parser=self, segments=self.segmentTokens )
        return theMssg
    def preVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.preMessage( self, indent )
    def postVisit( self, visitor, indent ):
        """Call class-specific method of visitor."""
        visitor.postMessage( self, indent )

def scan( msg ):
    """Overview of a message.
    returns a dict with the wrapper fields,
    plus a list of all segments as flat lists of stings.
    """
    m= Message( '*', Properties(desc='*') )
    segments= m.tokenize( msg )
    # locate the wrappers: ISA, GS, ST (and BHT if present)
    wrappers= { }
    for s in segments:
        if s[0] in ( "ISA", "GS", "ST", "SE", "GE", "IEA", "BHT" ):
            wrappers.setdefault(s[0], s)
    return wrappers, segments

def preParse( msg ):
    wrapper, segments = scan(msg)
    for w in wrapper:
        print( w, wrapper[w] )
    print( "trans=",wrapper["ST"][1] )
    for s in segments:
        print( s )
