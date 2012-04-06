#!/usr/bin/env python
"""X12.message.sa contains a SQLAlchemy mapping for :mod:`X12.message`
classes.

An X12 message instance is a recursive construction of Loops, sub-Loops and Segments.
The leaf elements are always Segments.  For transmission, the segment
leaves are flattened out; the loop structure is lost.

An X12 message instance is built by :mod:`X12.parse`.

This module inherits mappings for the following class definitions.

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
          
..  autoclass:: Factory
    :members:
"""
import sqlalchemy as sa
from tigershark.X12.message import Factory
from tigershark.X12.message import X12Loop
from tigershark.X12.message import X12Message
from tigershark.X12.message import X12Segment

# Get some settings to define the SA engine dynamically.
# This allows us to have Django-like run-time binding to a specific database.

# Define the database metadata.

# Define the sa.mapper between X12.message structures
# and database metadata.

class Factory( Factory ):
    """A Factory for this module's version of X12Message structures."""
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
        Ideally, all Segments exist as classes, defined in a module
        that imports this one, and is built by some conversion utility.
        However, we may be parsing some oddball message, or we may
        have specifically elected to ignore some segments and treat
        them as "generic".

        :param segmentToken: the :class:`X12.parse.SegmentToken` created by the parser.
        :param compositeSep: Composite internal separator from the ISA segment.
        :param segmentType: an instance of :class:`X12.parse.Segment` which defines
            the Elements and Composites of this Segment.
        :returns: X12Segment instance
        """
        name= "X12Segment_%s" % segmentToken[0]
        try:
            theClass= eval(name)
        except NameError:
            theClass= X12Segment
        return theClass( segmentToken, segmentType )
