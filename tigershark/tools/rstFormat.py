#!/usr/bin/env python
"""Handy classes to emit RST tables with pleasant column wrapping."""

class Column( object ):
    """Defines a column within a table display.  Can wrap text to fit
    within the column's defined size.
    """
    def __init__( self, name, size ):
        self.name= name
        self.size= size
    def pad( self, value, filler=' ' ):
        return value + (self.size-len(value))*filler
    def wrap( self, value, filler=' ' ):
        value= str(value)
        if len(value) <= self.size:
            return [ self.pad(value,filler), ]
        words= value.split()
        lines= []
        line= ""
        while len(words) != 0:
            nw= words.pop(0)
            if len(line) + len(nw) + 1 > self.size:
                lines.append( line )
                while len(nw) > self.size:
                    lines.append( nw[:self.size] )
                    nw= nw[self.size:]
                line= nw
            else:
                line += nw + " "
        if len(line) > 0:
            lines.append( line )
        return [ self.pad(l,filler) for l in lines ]

class Table( object ):
    def __init__( self, *columns ):
        self.columns= columns
    def _sep( self, filler='-' ):
        row= [ c.pad('',filler=filler) for c in self.columns ]
        return "+".join( [""] + row + [""] )
    def header( self ):
        row= ["Class","Attribute","Segment","Position","source","line"]
        yield self._sep('-')
        yield "|".join( [""] + [ c.pad(c.name) for c in self.columns ] + [""] )
        yield self._sep('=')
    def row( self, *data ):
        colLines = [ col.wrap(data) for col,data in zip(self.columns,data) ]
        sizes= [ len(x) for x in colLines ]
        for i in range(max(sizes)):
            row= []
            for col,data in zip(self.columns,colLines):
                if len(data) != 0:
                    row.append( col.pad( data.pop(0) ) )
                else:
                    row.append( col.pad("") )
            yield "|".join( [""] + row + [""] )
        yield self._sep('-')
