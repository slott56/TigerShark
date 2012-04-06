#!/usr/bin/env python
"""The X12.map.SQL module emits SQL table definitions from an :mod:`X12.parse` structure.

These table definitions are minimized by flattening Segments into their
parent Loop structures.

See :ref:`traversal` for notes on the **Visitor** design pattern.

..  autoclass:: SQLDetailsVisitor
    :members:

..  autoclass:: SQLTableVisitor
    :members:
"""
from tigershark.X12.parse import StructureVisitor
from tigershark.X12.parse import StopDescent

class SQLDetailsVisitor( StructureVisitor ):
    """Details means, effectively, column definitions, which are X12.parse.Elements.
    However, a Segments are murky.
    A Segment with a repeat of "1" can be expanded inline.
    A Segment with a repeat of ">1" or some specific number, has to be a separate
    table (or we have to generate a design not in 1NF).

    Similarly, a Loop which repeats exactly once can be expanded in-line.
    Loops which repeat, on the other hand, require distinct tables.  This is
    not as interesting, so we trust the other Visitor to allocate all Loops
    to separate tables.

    This visitor merely emits the in-line Segments, in-line Loops and Elements.
    Composites are little more than a comment, effectively an in-line sub-Segment.
    """
    typeMap= {
        'ID': 'VARCHAR2',
        'R':  'DECIMAL',
        'AN': 'VARCHAR2',
        'DT': 'CHAR', # Date, really
        'TM': 'CHAR', # Time, really
        'N0': 'NUMERIC',
        'N':  'NUMERIC',
        'B':  'NUMERIC', # Binary?
    }
    def __init__( self, *arg, **kw ):
        super( SQLDetailsVisitor, self, ).__init__( *arg, **kw )
        self.result= []
    def postElement( self, anElement, indent ):
        if anElement.req_sit == "S":
            nullable= "         "
        else:
            nullable= "NOT  NULL"
        # Some Segments are repeated.
        if anElement.parent.total_occurs != 1:
            qual= anElement.parent.occurance
        else:
            qual= ""
        typeStr= "%s(%s)" % ( self.typeMap.get(anElement.type_name,None), anElement.max_len )
        self.result.append( "    %s%s %s %s, -- %s" % (
            anElement.sqlName, qual, typeStr, nullable, anElement.desc ) )
    def preComposite( self, aComposite, indent ):
        self.result.append( "    -- Composite %s %s" % ( aComposite.name, aComposite.desc, ))
    def preSegment( self, aSegment, indent ):
        """Repeats?  If so, we need a separate table."""
        if aSegment.repeat == "1":
            self.result.append( "    -- In-line Segment %s %s" % (aSegment.name, aSegment.desc,) )
        else:
            self.result.append( "    -- FK reference from X%s_%s_%s -- %s" % (aSegment.message.name, aSegment.parent.name, aSegment.name, aSegment.desc,))
            raise StopDescent # already in a separate table definition
    def preLoop( self, aLoop, indent ):
        self.result.append( "    -- FK reference from X%s_%s -- %s" % (aLoop.message.name, aLoop.name, aLoop.desc,))
        raise StopDescent # already in a separate table definition

class SQLTableVisitor( StructureVisitor ):
    def __init__( self, *arg, **kw ):
        super( SQLTableVisitor, self ).__init__( *arg, **kw )
        self.result= []
    def preMessage( self, aMessage, indent ):
        """Table definitions of a Message."""
        self.result.append( "-- %s" % ( aMessage.desc,) )
        self.result.append( "CREATE TABLE X%s_%s(" % ( aMessage.message.name, aMessage.name ) )
        self.result.append( "    id INTEGER PRIMARY KEY AUTOINCREMENT," )
        for s in aMessage.structure:
            details= SQLDetailsVisitor( )
            s.visit( details )
            self.result.extend( details.result )
        self.result.append( "    xtra CHAR(8) -- placeholder")
        self.result.append( ") -- %s" % ( aMessage.name, ) )
        self.result.append( ";")
    def preLoop( self, aLoop, indent ):
        """Table definitions of a Loop."""
        self.result.append( "-- %s" % ( aLoop.desc,) )
        self.result.append( "CREATE TABLE X%s_%s(" % ( aLoop.message.name, aLoop.name ) )
        self.result.append( "    id INTEGER PRIMARY KEY AUTOINCREMENT," )
        self.result.append( "    loop INTEGER NOT NULL REFERENCES X%s_%s(id)," % ( aLoop.message.name, aLoop.parent.name) )
        for s in aLoop.structure:
            details= SQLDetailsVisitor( )
            s.visit( details )
            self.result.extend( details.result )
        self.result.append( "    xtra CHAR(8) -- placeholder")
        self.result.append( ") -- %s" % ( aLoop.name, ) )
        self.result.append( ";" )
    def preSegment( self, aSegment, indent ):
        if aSegment.repeat != "1":
            # Another table with an FK to this Segment
            name= "X%s_%s_%s%d" % ( aSegment.message.name, aSegment.parent.name, aSegment.name, aSegment.occurance )
            self.result.append( "-- %s" % ( aSegment.desc,) )
            self.result.append( "-- %r" % ( aSegment.props, ) )
            self.result.append( "CREATE TABLE %s(" % ( name, ) )
            self.result.append( "    id INTEGER PRIMARY KEY AUTOINCREMENT," )
            self.result.append( "    loop INTEGER NOT NULL REFERENCES X%s_%s(id)," % ( aSegment.message.name, aSegment.parent.name) )
            for s in aSegment.structure:
                details= SQLDetailsVisitor( )
                s.visit( details )
                self.result.extend( details.result )
            self.result.append( "    xtra CHAR(8) -- placeholder")
            self.result.append( ") -- %s" % ( aSegment.name, ) )
            self.result.append( ";" )
    def getSource( self ):
        return "\n".join( self.result )
