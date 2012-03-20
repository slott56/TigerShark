from X12.parse import Message, Loop, Segment, Composite, Element, Properties

class AnySegment( Segment ):
    def match( self, candidate ):
        return True

class AnyLoop( Loop ):
    valid_types = ( AnySegment, )
    def match( self, candidate ):
        return True

class AnyMessage( Message ):
    valid_types = ( AnyLoop, )

parser= AnyMessage( 'any', Properties(desc='any'),
    AnyLoop( '*', Properties(desc='*'),
        AnySegment( '*', Properties(desc='*') ) ) )