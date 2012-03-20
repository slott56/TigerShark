#!/usr/bin/env python
"""Defines an insurance Claim from a business perspective,
mapping to underlying X12 structures.

There are two parts to this module.

-   A **Facade** over :mod:`X12.message` structures.
    See `Facade Use Cases`_ and `Facade Implementation`_.

-   A mapping of a Claim, using the **Facade** elements.
    See `Claim Mapping`_.

Facade Use Cases
================

The :class:`X12LoopBridge` will associate a Python class with an X12 Loop definition.
Each attribute of Python class is a **Descriptor** that references an X12 Element
in  a Segment instance within the overall Loop.

It's a **Bridge** between a Python class and an X12 Loop.

Repeating copies of a Loop create multiple object instances.

Repeating copies of a Segment within a Loop lead to a
somewhat more complex definition.  These segments are "unwrapped" by the
containing Loop.

A Python **Descriptor** gives us an implicit get/set/del protocol around the
attribute. Syntactically, an application simply references the attribute name.
Python will use the get and set methods from the Descriptor to access the
attribute.

The attribute Descriptor has several use cases, depending
on the attribute's type and how that value is accessed from the X12 Segment.

    -   Single simple value, identified by position within a Segment of the top-level Loop.
        This is a direct reference to an Element, and is only appropriate when the
        Segment doesn't repeat.

    -   Single simple value, one of a number of alternative positions within a Segment.
        This is a
        direct reference to an Element, and is appropriate when the Segment
        doesn't repeat.  The Element is one of a number of
        candidates, which are defined by a sequence of
        :samp:`(qualifier,value)` position tuples.  If the Element value in the qualifier
        position is equal to a given qualifier value, the Element in the value
        position is the desired Element. This is required to pick values out of
        the :samp:`PER` segment.

    -   Sequence of simple values, with the value identified a fixed position in multiple
        occurrences of a Segment.  This is used for :samp:`NTE` segments.

    -   Single simple value, identified by a position in a Composite.  This is a direct reference
        to a sub-element of a Composite.  This is used to pick apart the various
        composites that occur in :samp:`HI` segments when a single value is required.

    -   Single complex value, identified by a Composite.

    -   Sequence of simple values, with the value identified by a fixed position in
        multiple occurrences of a Composite.  This is used to pick apart the various
        composites that occur in :samp:`HI` segments when a sequence of values is required.

    -   Sequence of complex values, with the value identified by a recurring
        Segment.  This is used to define a nested object.  This is used to pick apart the :samp:`PWK`
        Segments, which occur multiple times within the 2300 and 2400 loops.

XXX - Can Composite and Element be refactored to have a common superclass?
Do all Composites have a type identifier in the initial position?

There are several dimensions to the above cases:

    -   Source Type:  Segment (which has an underlying Segment Token) and
        Composite (which is just a string).  This distinction applies to
        some of the following dimensions.

    -   Source Objects:

        -   Segment or Segments that match simple qualifications.

        -   Composite or Composites that match simple Criteria, but are found in multiple Segments.

    -   Element Selection:

        -   Fixed position within each Segment, OneOf a Number of Positions
            within a Segment.  This creates a sequence of strings values.

        -   Fixed position(s) within a Composite, Sequence of Positions
            within a Composite (usually positions [1:]).  This creates a sequence
            of string values.

        -   The whole Segment.

    -   Conversion: No conversion, single-element conversion, multi-element conversion.
        At this point, we don't care whether the data was from a Composite or Segment
        since it's now a sequence of strings.

    -   Result Stucture: single occurance vs. the complete sequence.

There are several conversion protocols.

    -   Single-element string value is the native X12 source data types.
        No conversion is done.

    -   Single-element non-string value is done through a simple conversion
        protocol.  A class with two static methods (x12_to_python and python_to_x12)
        is used by the Descriptor to make the value usable.

    -   Multiple-element all-string values are can be handled as simple Python lists of
        strings.

    -   Multiple-element, non-String values use the same basic conversion
        protocol, starting from a list of strings instead of a single string Element
        value.

Facade Implementation
============================

The :class:`X12LoopBridge` handles the high-level mapping between a Python class
and an instance of an :class:`X12.message.X12Loop`. Each bridge has a few
high-level methods, and a long sequence of attribute definitions. Each attribute
is defined using an instance of the :class:`ElementAccess` class.

The :class:`ElementAccess` class is a **Lightweight** class that has parameters
and a reference to the underlying :class:`X12.message.X12Loop` structure. It is
a Python **Descriptor**, and implements the get/set protocol for the attribute
value.

..  autoclass:: X12LoopBridge

..  autoclass:: X12SegmentBridge

Element Access
--------------

The essential feature of Element Access is to provide a two-way mapping between
a named attribute and Elements within a Segment.  This is done through two
parallel multi-step alogithms for locating the element and either getting
or setting the value.

The element access get algorithm has the following steps:

    1.  **Source Segments**. Accumulate the source X12Segment instances from
        the Loop. Filtering is a feature of the :class:`X12LoopBridge`.

    2.  If doing whole Segments:

        -   Repackage the Segment as a list of strings for step 5.

    3.  If doing Elements from Segments (via :class:`ElementAccess`):

        -   **Element Selection**. Locate actual positions of Element values
            within each Segment. This uses a sequence of X12Segment instances.
            There are several
            segment Position algorithms: simple value position, qualified
            position.  Package as list of strings for step 5.

    4.  Elif doing Elements from Composites (via :class:`CompositeAccess`):

        -   **Source Composites**. Accumulate the source Composite sequences.
            Composite filtering is a feature an {CompositeAccess} object, it
            leverages the source segment list.

        -   **Element Selection**. Accumulate the sequence of Element values.
            This is done by a :class:`CompositePosition` object.  There are two
            composite positions algorithms: single value position and range of positions.
            Package as a list of strings for step 5.

    5.  **Conversion**. Apply x12_to_python type conversion to sequences of Element values.
        Ths various :class:`Conversion` subclasses handle this.

    6.  **Result Structure**. Pick the first value or the whole list of values.
        The :class:`ElementAccess` class handles this final selection.

The set algorithm is the approximate inverse of this.

    1.  **Conversion**.  Apply python_to_x12 type conversion to build sequences
        of Element values.

    2.  Then the **Source Objects** and **Element Selection** steps are done to
        locate through the applicable source element(s).

..  autoclass:: SegmentSequenceAccess

..  autoclass:: ElementAccess

..  autoclass:: ElementSequenceAccess

Segment Position
-----------------

Element values are located by "position".  In the majority of cases, the
position is a single, fixed position within a Segment.  The position can
be defined numerically.

When creating an :class:`ElementAccess` attribute definition, a numeric position
is implicitly translated to an instance of :class:`Position`, the simplest kind
of position definition.

There are several kinds of Position definitions.

    -   :class:`Position` defines a single, fixed Element position as the value
        for an attribute.

    -   :class:`OneOf` is used to implement attributes of the :samp:`PER` Segment, which
        are defined by a series of (qualifer,value) pairs.  The Element's position
        isn't fixed, but is determined by examining a number of alterantives.

    -   :class:`SequenceOf` is used to implement attributes which are a simple sequence
        of values picked from the Elements of the Segment.

..  autoclass:: Position

..  autoclass:: OneOf

..  autoclass:: SequenceOf

Composite Position
------------------

Element values are located by "position".  Positions are either a single,
fixed position within a Composite or a range of positions.

..  autoclass:: CompositePosition

..  autoclass:: CompositeAccess

# XXX - Refactor CompositeAccess and CompositeSequenceAccess to be much simpler.

..  autoclass:: CompositeSequenceAccess

Conversion
----------

Each data conversion is a static class definition with two methods:

    -   x12_to_python.  This method converts an X12 string or sequence
        of strings into a Python object.  The sequence of strings is used
        to convert Composites as well as converting whole Segments into distinct
        Python objects.

    -   python_to_x12.  This method converts a Python object into an
        X12 string or a sequence of strings.

..  autoclass:: Conversion
..  autoclass:: D8
..  autoclass:: DR
..  autoclass:: SegmentConversion


Exceptions
-------------

..  autoclass:: MissingSegment

Claim Mapping
===============

**Patient** - Loop 2000C

..  autoclass:: Patient
..  autoclass:: Instutitional_Patient
..  autoclass:: Institutional_Inpatient
..  autoclass:: Institutional_Outpatient
..  autoclass:: Professional_Patient

**Provider** - Loop 2000A (a/k/a BillingProvider)

..  autoclass:: Provider

**Submitter** - Loop 1000A

..  autoclass:: Submitter

**Subscriber** - Loop 2000B

..  autoclass:: Subscriber

**Paperwork** -

..  autoclass:: Paperwork

**ClaimDetails** - Superclass for portions of Loop 2300, including embedded paperwork
  and various "HI" composite objects.

..  autoclass:: ClaimDetails

**Institutional_ClaimDetails**

..  autoclass:: Institutional_ClaimDetails

**Professional_ClaimDetails**

..  autoclass:: Professional_ClaimDetails

**ServiceLine**

..  autoclass:: ServiceLine
..  autoclass:: Institutional_ServiceLine
..  autoclass:: Professional_ServiceLine
..  autoclass:: ServiceLineAdj

Top-Level **Claim**.

..  autoclass:: Claim

"""
from __future__ import print_function
import datetime
from X12.message import X12Message

class MissingSegment( Exception ):
    """This exception is raised if the target Segment cannot be found
    within the Loop.
    """
    pass

class X12LoopBridge( object ):
    """Bridge between a user-focused class/attribute definition and an :class:`X12.message.X12Loop`.

    This wrapper implements a simple search for Segments within a Loop.
    It leverates the essential XPath like "descendant" search capability,
    and either returns a sequence of Segments or a single Segment which matches
    certain qualifying criteria.

    This is an abstract superclass definition.  A subclass will contain a number
    of attributes, defined using the :class:`ElementAccess` class or any of its
    subclasses.
    """
    def __init__( self, aLoop ):
        """Named loop within a specific message.
        
        :param aLoop: the loop identifier to pick out of the X12Message.
        """
        self.loop= aLoop
    def __str__( self ):
        return str(self.loop)
    def _filteredList( self, name, qualifierPos=None, inList=None, notInList=None ):
        """Return a all matching X12Segments of the X12Loop.
        If no qualifier, then all segments with the given name are returned.
        If a qualifier position is provided, then the element at that position in the
        segment is checked for a value in the :meth:`inList` or not in the :meth:`notInList`
        values.
        
        :param name: name of the segment
        :param qualifierPos: optional qualifier position in the Segment.
        if omitted, all matching segments are returned.
        :param inList: optional qualification values.  Only used if the qualiferPosition
        is provided.  This the positive list of values segments must have.
        :param notInList: optional qualification values.  Only used if the qualiferPosition
        is provided.  This the negatuve list of values segments must not have.
        :returns: list of all :class:`X12.message.X12Segment` instances within this Loop.
        """
        segList= [ s for s in self.loop.descendant( "segment", name ) ]
        if qualifierPos:
            if inList:
                filtered= [ seg for seg in segList if seg.getByPos(qualifierPos) in inList ]
            elif notInList:
                filtered= [ seg for seg in segList if seg.getByPos(qualifierPos) not in notInList ]
            else:
                raise TypeError( "QualifierPos requires inList or notInList")
        else:
            filtered= segList
        return filtered
    def segList( self, name, qualifierPos=None, inList=None, notInList=None ):
        """Return a all matching X12Segments of the X12Loop.
        If no qualifier, then all segments with the given name are returned.
        If a qualifier position is provided, then the element at that position in the
        segment is checked for a value in the :meth:`inList` or not in the :meth:`notInList`
        values.
        
        :param name: name of the segment
        :param qualifierPos: optional qualifier position in the Segment.
        if omitted, all matching segments are returned.
        :param inList: optional qualification values.  Only used if the qualiferPosition
        is provided.  This the positive list of values segments must have.
        :param notInList: optional qualification values.  Only used if the qualiferPosition
        is provided.  This the negatuve list of values segments must not have.
        :returns: list of all :class:`X12.message.X12Segment` instances within this Loop.
        """
        return [ X12SegmentBridge(s) for s in self._filteredList(name,qualifierPos,inList,notInList) ]
    def segment( self, name, qualifierPosition=None, inList=None, notInList=None ):
        """Return a specific X12Segment of the X12Loop.
        If no qualifier, then the first segment with the given name is returned.
        If there's one instance of a segment within a loop, this default
        picks the only instance.
        If a qualifier position is provided, then the element at that position in the
        segment is checked for a value in the list of values.
        
        :param name: name of the segment
        :param qualifierPosition: optional qualification position.
        if omitted, the first matching segment is returned.
        :param inList: optional qualification values.  Only used if the qualifier
        is provided to specify the position to check.
        :param notInList: optional negative list of values to exclude from qualification.
        Only used if the qualifier
        is provided to specify the position to check.
        :returns: :class:`X12.message.X12Segment` instance within this Loop.
        """
        matches= self._filteredList(name,qualifierPosition,inList,notInList)
        if len(matches) == 0: return None
        return X12SegmentBridge( matches[0] )

class X12SegmentBridge( object ):
    """Bridge between a user-focused class/attribute definition and an :class:`X12.message.X12Segment`.

    This is a simple wrapper around an X12Segment which can be used to locate Composites
    within the Segment or locate Elements within the Segment.

    XXX - This is only really necessary when extracting Composites.
    Consider not using X12SegmentBridge for ordinary ElementAccess processing.
    """
    def __init__(self, aSegment ):
        self.segment= aSegment
    def __str__( self ):
        return str( self.segment )
    def compositeList( self, *names ):
        sep= self.segment.message.getCompositeSeparator()
        result= []
        pos= 1
        while self.segment.getByPos(pos) is not "":
            composite= self.segment.getByPos( pos )
            # XXX - Seems vaguely icky to parse composites here.
            subElts= composite.split( sep )
            if subElts[0] in names:
                result.append( subElts )
            pos += 1
        return result
    def composite( self, *name ):
        compList= self.compositeList( *name )
        if len(compList) > 0: return compList[0]
        return None # technically redundant to do this.

class SegmentSequenceAccess( object ):
    """Define access to sequence of Segments with a user-friendly attribute name.
    This appears as a sequence of individual object instances.
    This requires a :class:`Conversion` for doing data
    type conversion of the Segment's collection of Elements.

    This class is used to create attribute definitions which are
    mappings to X12Segments in an :class:`X12.message.X12Loop` instance.

    This is a Descriptor, which implements the attribute name via implicit
    getters and setters defined in this class.  These are attached to X12LoopBridge
    objects, so "instance" is always a specific X12LoopBridge, and owner is
    a subclass of X12LoopBridge.

        -   __get__ must locate the Segments and provide lists of string element values
            to a Conversion class.

        -   __set__ must convert objects to lists of strings, then locate the elements and replace their
            values.
    """
    def __init__( self, segment, qualifier=None, x12type=None ):
        """Define an attribute.
        Most attributes are the string values of Elements, simply accessed by position.

        If an attribute has a non-string type, the :py:data:`x12type` parameter can identify
        a :class:`Conversion` class to use.

        If an attribute is on a Segment which can occur multiple times, with a qualified
        value, then the :py:data:`qualifier` parameter is used to provide a tuple with
        the position of the segment used for qualification and the value to test.

        For example: :samp:`segment="REF", qualifier=(2,"SY")` will examine all "REF" segments
        within this loop, looking for one with :samp:`"SY"` in :samp:`REF02`.

        :param segment: Name of the segment that contains the element which has the
        value for this attribute.
        :param qualifier: A qualifier tuple used when there are multiple instances
        of the given segment name and a specific position in the segment must be tested.
        :param x12type: An X12type conversion class name.
        :returns: The element value for this attribute name.
        """
        self.segment= segment
        if qualifier is None:
            self.qualifier= None
        elif isinstance(qualifier, (list,tuple)):
            self.qualifier= qualifier
        else:
            self.qualifier= ( qualifier, )
        self.x12type= x12type
    def __repr__( self ):
        """Provide Documentation for epydoc."""
        typeName = "None" if self.x12type is None else self.x12type.__name__
        return "SegmentSequenceAccess( %r, %r, %r, %s )" % ( self.segment, self.position, self.qualifier, typeName )
    def __get__( self, instance, owner ):
        # XXX - Some are unfiltered...
        if self.qualifier is None:
            segBridgeList= instance.segList( self.segment, )
        else:
            segBridgeList= instance.segList( self.segment, self.qualifier[0], inList=self.qualifier[1:] )
        return [ self.x12type.x12_to_python(segBridge.segment.segmentToken) for segBridge in segBridgeList ]
    def __set__( self, instance, value ):
        raise UnimplementedError( "Can't set segment sequences, yet")

class Position( object ):
    """Sets or gets the value of an Element in a Segment based on a
    single, fixed position.
    """
    def __init__( self, position ):
        """Define a fixed Position for ElementAccess.
        
        :param position: the numeric position of this element.
        """
        self.position= position
    def __repr__( self ):
        return "Position(%d)" % ( self.position, )
    def get( self, aSegment ):
        """Get our defined Element out of the given X12Segment.
        
        :param aSegment: an :class:`X12.message.X12Segment` to examine.
        """
        return aSegment.getByPos( self.position )
    def set( self, aSegment, value ):
        """Set our defined Element within the given X12Segment.
        
        :param aSegment: an :class:`X12.message.X12Segment` to update.
        :param value: the String value to place into the segment.
        """
        aSegment.setByPos( self.position, value )

class OneOf( Position ):
    """Sets or Gets the value of an Element by searching through a sequence
    of alternative Element pairs using a qualifier value.
    This subclsas of Position is initialized with a sequence (qualifier,value) position pairs and
    a qualifier value.  If the qualifier value matches the element
    in the qualifier position, then the element in the value position
    is used.
    """
    def __init__( self, value, *posPairSeq ):
        """Define a qualifier value and a sequence of (qualifier,value) positions ElementAccess.
        
        :param value: the qualifier value used to match the Element in one of the qualifier positions.
        :param posPairSeq: sequence of (qualifierPosition, valuePosition)
        """
        self.value= value
        self.posPairSeq= posPairSeq
    def __repr__( self ):
        return "OneOf(%r,%r)" % ( self.value, self.posPairSeq, )
    def get( self, aSegment ):
        """Get our defined element out of the given segment.
        If the qualifier value cannot be found, return None.
        
        :param aSegment: an :class:`X12.message.X12Segment` to examine.
        """
        for qualPos, valPos in self.posPairSeq:
            if aSegment.getByPos( qualPos ) == self.value:
                return aSegment.getByPos( valPos )
        return None
    def set( self, aSegment, value ):
        """Set our defined element within the given segment.
        If the qualifier value cannot be found, raise a NotImplementedError.
        
        XXX - Implement the ability to add qualifiers and values to a segment.
        
        :param aSegment: an :class:`X12.message.X12Segment` to examine.
        :param value: the String value to place into the segment.
        """
        for qualPos, valPos in self.posPairSeq:
            if aSegment.getByPos( qualPos ) == self.value:
                aSegment.setByPos( valPos, value )
                return
        raise NotImplementedError( "Unimplemented: add new OneOf value to this segment" )

class SequenceOf( Position ):
    """Unwind a number of Elements into an sequence of attribute values.
    Often, each value is a Composite element with a qualifier, plus additional values."""
    def __init__( self, start, end ):
        """Define a sequence Position for ElementAccess.
        
        :param start: the first Element position within the Segment.
        :param end: last Element position within the Segment)
        """
        self.start= start
        self.end= end
    def __repr__( self ):
        return "SequenceOf(%d,%d)" % ( self.start, self.end, )
    def get( self, aSegment ):
        elementList= [ aSegment.getByPos(pos) for pos in range(self.start,self.end) if aSegment.getByPos(pos) is not None ]
        return elementList
    def set( self, aSegment, valueList ):
        for pos,val in zip(range(self.start,self.end),valueList):
            aSegment.setByPos(pos,val)
            return
        raise NotImplementedError( "Unimplemented: add new SequenceOf value to this segment" )

class ElementAccess( object ):
    """Define access to Element(s) within a Segment with a user-friendly attribute name.
    This can also bind in a :class:`Position` for finding the specific Element, and
    a :class:`Conversion` for doing data type conversion of the Element.

    This class is used to create attribute definitions which are
    mappings to positional Elements in an :class:`X12.message.X12Segment` instance.

    This is a Descriptor, which implements the attribute name via implicit
    getters and setters defined in this class.  These are attached to X12LoopBridge
    objects, so "instance" is always a specific X12LoopBridge, and owner is
    a subclass of X12LoopBridge.

        -   __get__ must locate the elements and provide string to a Conversion class.

        -   __set__ must convert strings, then locate the elements and replace their
            values.
    """
    def __init__( self, segment, position=None, oneOf=None, qualifier=None, x12type=None ):
        """Define an attribute.
        Most attributes are the string values of Elements, simply accessed by position.

        If an attribute has a non-string type, the :py:data:`x12type` parameter can identify
        a :class:`Conversion` class to use.

        If an attribute is on a Segment which can occur multiple times, with a qualified
        value, then the :py:data:`qualifier` parameter is used to provide a tuple with
        the position of the segment used for qualification and the value to test.

        For example: :samp:`segment="REF", qualifier=(2,"SY")` will examine all "REF" segments
        within this loop, looking for one with :samp:`"SY"` in :samp:`REF02`.

        If an attribute occurs multiple times within a segment, and a qualifying
        element is used, then the :class:`oneOf` parameter is used.  This accepts a sequence
        of values: the first is a test to use, the remaining values are
        pairs of positions.  The first position is used to test, the second position
        is the result.

        For example: :samp:`segment="PER", oneOf=( "EM", (3,4), (5,6), (7,8) )` means that
        if element 3 is "EM", the attribute is element 4; if element 5 is "EM",
        the attribute is element 6; if element 7 is "EM", the attribute is element 8.

        :param segment: Name of the segment that contains the element which has the
        value for this attribute.
        :param position: integer position of the element within the segment; this
        is not used if oneOf is used to pick a position.
        :param oneOf: a sequence with a qualifier and position pairs used to
        examine a qualifier element and a value element.  Example
        :samp:`oneOf=( "EM", (3,4), (5,6), (7,7)`.  If oneOf is used, position is
        meaningless.
        :param qualifier: A qualifier tuple used when there are multiple instances
        of the given segment name and a specific position in the segment must be tested.
        :param x12type: An X12type conversion class name.
        :returns: The element value for this attribute name.
        """
        self.segment= segment
        if isinstance(position, int):
            self.position= Position( position )
        elif isinstance(oneOf, (list,tuple) ):
            self.position= OneOf( *oneOf )
        elif isinstance( position, Position ):
            self.position= position
        else:
            raise TypeError( "position (%r) is an unrecognized type (%s)" % ( position, type(position) ) )
        if isinstance(qualifier, (list,tuple)):
            self.qualifier= qualifier
        else:
            self.qualifier= ( qualifier, )
        self.x12type= x12type
    def __repr__( self ):
        """Provide Documentation for epydoc."""
        typeName = "None" if self.x12type is None else self.x12type.__name__
        return "ElementAccess( %r, %r, %r, %s )" % ( self.segment, self.position, self.qualifier, typeName )
    def __get__( self, instance, owner ):
        segBridge= instance.segment( self.segment, self.qualifier[0], inList=self.qualifier[1:] )
        if segBridge is None: return None
        raw= self.position.get( segBridge.segment )
        if self.x12type is not None: return self.x12type.x12_to_python( raw )
        else: return raw
    def __set__( self, instance, value ):
        if x12type is not None:
            raw= self.x12type.python_to_x12( value )
        else:
            raw= value
        segBridge= instance.segment( self.segment, self.qualifier[0], inList=self.qualifier[1:] )
        if segBridge is None:
            raise MissingSegment( "Segment %s (%r) Not Found" % ( self.segment, self.qualifier ) )
        else:
            self.position.set( segBridge.segment, raw )

class ElementSequenceAccess( ElementAccess ):
    """Map a user-friendly attribute name to an sequence of Elements that occur in multiple
    copies of a Segment type.  This is used for the "NTE" Segments where
    a sequence of individual instances occur within a 2300 claim details loop.

    This is a Descriptor which implements the attributes name using
    __get__ and __set__ methods.
    """
    def __init__( self, segment, position, qualPos=None, inList=None, notInList=None, x12type=None ):
        """Build Element Access for a sequence of Elements.
        
        :param segment: Name of the segments that contains the elements which are the
        values for this attribute.
        :param position: integer position of the element within the segment.
        :param qualPos: integer position of the qualifier attribute in each segment instance.
        If omitted, all instances of the segment will become the sequence of values.
        If used, either :meth:`inList` or :meth:`notInList` must be provided.
        :param inList: sequence of values to include segments.
        :param notInList: sequence of values to exclude segments.
        :param x12type: An X12type conversion class name.
        :returns: The sequence of element values for this attribute name.
        """
        self.segment= segment
        self.position= position
        self.qualPos= qualPos
        self.inList= inList
        self.notInList= notInList
        self.x12type= x12type
    def __repr__( self ):
        """Provide Documentation for epydoc."""
        typeName = "None" if self.x12type is None else self.x12type.__name__
        return "ElementSequenceAccess( %r, %r, %r, %s )" % ( self.segment, self.position, self.qualifier, typeName )
    def __get__( self, instance, owner ):
        segs= instance.segList( self.segment, self.qualPos, self.inList, self.notInList )
        return [ s.getByPos(self.position) for s in segs ]
    def __set__( self, instance, valueList ):
        segs= instance.segList( self.segment, self.qualPos, self.inList, self.notInList )
        for seg,val in zip(segs, valueList):
            if seg is None or val is None:
                raise NotImplementedError( "Unimplemented: number of values and segments don't match" )
            if x12type is not None:
                raw= self.x12type.python_to_x12( val )
            else:
                raw= val
            seg.setByPos( self.position, raw )

class CompositePosition( object ):
    """Sets or gets the value of an Element in a Composite based on a
    single, fixed position.

    Segments are managed as SegmentToken instances.  Composites, however,
    are simple sequences of strings.
    """
    def __init__( self, *position ):
        self.positions= position
    def get( self, aComposite ):
        return [ aComposite[c] if c < len(aComposite) else None for c in self.positions ]
    def set( self, aComposite, *value ):
        for pos,val in zip(self.positions,value):
            assert pos is not None and val is not None, ValueError("values and composite positions diffent lengths")
            aComposite[pos]= val

class CompositeAccess( ElementAccess ):
    """Map a user-friendly attribute name to an Element of a Composite;
    the composites can be found
    anywhere among the occurances of a given Segment type.
    This is used for the various "HI" Segments where a single value is located in a
    qualified Composite.  This behaves a little bit like the OneOf position
    for an ordinary ElementAccess.

    Generally, a Composite has multiple Elements, the first of which is a qualifier.
    The rest of which are the target values.

    This is a Descriptor which implements the attributes name using
    __get__ and __set__ methods.  This descriptor is associated with a subclass of
    X12LoopBridge, the instance is a specific **Brige** and the owner is
    the subclass of X12LoopBridge.
    """
    def __init__( self, segment, compositeQualifier, compositePosition, x12type=None ):
        """Build Composite Access for an individual Composite.
        
        :param segment: Name of the segments that contains the composites which are the
        values for this attribute.
        :param compositeQualifier: A qualifier string or tuple of strings that identifies
        the composites to collect
        :param compositePosition: The numeric position of the element within the Composite.
        :param x12type: An X12type conversion class name.  This conversion will receive a
        large, complex sequence of values decomposed from a Composite.
        :returns: The sequence of element values for this attribute name.
        """
        self.segment= segment
        if isinstance( compositeQualifier, (list,tuple) ):
            self.qualifier= compositeQualifier
        else:
            self.qualifier= (compositeQualifier,)
        if isinstance( compositePosition, CompositePosition ):
            self.compPosition= compositePosition
        if isinstance( compositePosition, (list,tuple) ):
            self.compPosition= CompositePosition( *compositePosition )
        else:
            self.compPosition= CompositePosition( compositePosition )
        self.x12type= x12type
    def __repr__( self ):
        """Provide Documentation for epydoc."""
        typeName = "None" if self.x12type is None else self.x12type.__name__
        return "CompositeAccess( %r, %r, %r, %s )" % ( self.segment, self.position, self.qualifier, typeName )
    def __get__( self, instance, owner ):
        segList= instance.segList( self.segment )
        compList= []
        for seg in segList:
            compList.extend( seg.compositeList( *self.qualifier ) )
        data= []
        for composite in compList:
            raw= self.compPosition.get( composite )
            if self.x12type is not None:
                data.append( self.x12type.x12_to_python( raw ) )
            else:
                data.append( raw )
        return data[0]
    def __set__( self, instance, value ):
        """XXX - Implement this."""
        raise NotImplementedError( "Unimplemented: can't update Composite" )
        segList= instance.segList( self.segment )
        # need to locate composite in this segList and update it.

class CompositeSequenceAccess( CompositeAccess ):
    """Map a user-friendly attribute name to a sequence of Composites that occur
    somewhere in the occurances of a given Segment type
    This is used for the various "HI" Segments where a sequence of values is located in a
    qualified Composites.

    Each Composite Element has multiple values, the first of which is a qualifier
    for the Composite.  The rest of which is the target values.

    This is a Descriptor which implements the attributes name using
    __get__ and __set__ methods.
    """
    def __init__( self, segment, compositeQualifier=None, x12type=None ):
        """Build Composite Access for a sequence of Composites.
        
        :param segment: Name of the segments that contains the elements which are the
        values for this attribute.
        :param compositeQualifier: A qualifier string or tuple of strings that identifies
        the composites to collect
        :param x12type: An X12type conversion class name.  This conversion will receive a
        large, complex sequence of values decomposed from a Composite.
        :returns: The sequence of element values for this attribute name.
        """
        self.segment= segment
        if isinstance( compositeQualifier, (list,tuple) ):
            self.qualifier= compositeQualifier
        else:
            self.qualifier= ( compositeQualifier, )
        self.x12type= x12type
    def __repr__( self ):
        """Provide Documentation for epydoc."""
        typeName = "None" if self.x12type is None else self.x12type.__name__
        return "CompositeSequenceAccess( %r, %r, %r, %s )" % ( self.segment, self.position, self.qualifier, typeName )
    def __get__( self, instance, owner ):
        segList= instance.segList( self.segment )
        compList= []
        for seg in segList:
            compList.extend( seg.compositeList( *self.qualifier ) )
        data= []
        for composite in compList:
            raw= composite
            if self.x12type is not None:
                data.append( self.x12type.x12_to_python( raw ) )
            else:
                data.append( raw )
        return data
    def __set__( self, instance, value ):
        """XXX - implement this."""
        raise NotImplementedError( "Unimplemented: can't update Composite" )

class Conversion( object ):
    """Convert between X12 strings and Python objects.
    This is the abstract superclass for all conversions.
    """
    @staticmethod
    def x12_to_python( raw ):
        return NotImplemented
    @staticmethod
    def python_to_x12( value ):
        return NotImplemented

class D8( Conversion ):
    """Convert between D8 format dates to proper DateTime objects."""
    @staticmethod
    def x12_to_python( raw ):
        yy,mm,dd = int(raw[0:4]), int(raw[4:6]), int(raw[6:8])
        return datetime.date( yy,mm,dd )
    @staticmethod
    def python_to_x12( value ):
        return value.strftime( "%4Y%2m%2d" )

class DR( Conversion ):
    """Convert between DR format dates to proper DateTime objects."""
    @staticmethod
    def x12_to_python( raw ):
        d1, punct, d2 = raw.partition('-')
        yy1,mm1,dd1 = int(d1[0:4]), int(d1[4:6]), int(d1[6:8])
        yy2,mm2,dd2 = int(d2[0:4]), int(d2[4:6]), int(d2[6:8])
        return datetime.date( yy1,mm1,dd1 ), datetime.date( yy2,mm2,dd2 )
    @staticmethod
    def python_to_x12( value ):
        d1, d2 = value
        return "%s-%s" % ( d1.strftime( "%4Y%2m%2d" ), d2.strftime( "%4Y%2m%2d" ) )

class SegmentConversion( Conversion ):
    """Convert between an X12Segment and a proper Python object."""
    def __init__( self, someClass ):
        self.someClass= someClass
    def x12_to_python( self, raw ):
        return self.someClass( raw )
    def python_to_x12( self, value ):
        return value.segment

class Patient( X12LoopBridge ):
    """Patient Data from loop 2000C"""
    loopName= "2000C"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    id= ElementAccess( "NM1", 9 )
    addr1= ElementAccess( "N3", 1 )
    addr2= ElementAccess( "N3", 2 )
    city= ElementAccess( "N4", 1 )
    state= ElementAccess( "N4", 2 )
    zip= ElementAccess( "N4", 3 )
    country= ElementAccess( "N4", 4 )
    dob= ElementAccess( "DMG", 2, x12type=D8 )
    sex= ElementAccess( "DMG", 3 )
    ssn= ElementAccess( "REF", 2, qualifier=(1,"SY") )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Instutitional_Patient( Patient ):
    """Patient on an 837I claim."""
    rel= ElementAccess( "PAT", 1 )
    measCode= ElementAccess( "PAT", 7 )
    weight= ElementAccess( "PAT", 8 )
    resp= ElementAccess( "PAT", 9 )

class Institutional_Inpatient( Instutitional_Patient ):
    pass

class Institutional_Outpatient( Instutitional_Patient ):
    pass

class Professional_Patient( Patient ):
    """Patient on an 837P claim."""
    rel= ElementAccess( "PAT", 1 )
    dateFormat= ElementAccess( "PAT", 5 )
    dod= ElementAccess( "PAT", 6 )
    measCode= ElementAccess( "PAT", 7 )
    weight= ElementAccess( "PAT", 8 )
    preg= ElementAccess( "PAT", 9 )

class Provider( X12LoopBridge ):
    """Provider Data on the 2000A loop."""
    loopName= "2000A"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    nm106= ElementAccess( "NM1", 6 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    taxId= ElementAccess( "NM1", 9 )
    npi= ElementAccess( "NM1", 9 )
    nm109= ElementAccess( "NM1", 9 )
    addr1= ElementAccess( "N3", 1 )
    addr2= ElementAccess( "N3", 2 )
    city= ElementAccess( "N4", 1 )
    state= ElementAccess( "N4", 2 )
    zip= ElementAccess( "N4", 3 )
    country= ElementAccess( "N4", 4 )
    contact_name= ElementAccess( "PER", 1 )
    contact_funct= ElementAccess( "PER", 2 )
    # Email, Phone and Fax are all on the same segment in pairs (3,4), (5,6), (7,8)
    # First value is a qualifier: "EM", "TE" or "FX"
    # Second value is the number
    email= ElementAccess( "PER", oneOf=( "EM", (3,4), (5,6), (7,8) ) )
    fax= ElementAccess( "PER", oneOf=( "FX", (3,4), (5,6), (7,8) ) )
    phone= ElementAccess( "PER", oneOf=( "TE", (3,4), (5,6), (7,8) ) )
    provCode= ElementAccess( "PRV", 1 )
    qual= ElementAccess( "PRV", 2 )
    taxonomyCd= ElementAccess( "PRV", 3 )
    BCID= ElementAccess( "REF", 2, qualifier=(1,"1A") )
    BSID= ElementAccess( "REF", 2, qualifier=(1,"1B") )
    medID= ElementAccess( "REF", 2, qualifier=(1,"1C") )
    uPIN= ElementAccess( "REF", 2, qualifier=(1,"1G") )
    commID= ElementAccess( "REF", 2, qualifier=(1,"G2") )
    taxID_sy= ElementAccess( "REF", 2, qualifier=(1,"SY") )
    taxID_ei= ElementAccess( "REF", 2, qualifier=(1,"EI") )
    ITSSpec= ElementAccess( "REF", 2, qualifier=(1,"N5") )
    legacyID= ElementAccess( "REF", 2, qualifier=(1,"X5") )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Submitter( X12LoopBridge ):
    """Submitter Data derived from the 1000A loop."""
    loopName= "1000A"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    nm106= ElementAccess( "NM1", 6 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    id= ElementAccess( "NM1", 9 )
    email= ElementAccess( "PER", oneOf=( "EM", (3,4), (5,6), (7,8) ) )
    fax= ElementAccess( "PER", oneOf=( "FX", (3,4), (5,6), (7,8) ) )
    phone= ElementAccess( "PER", oneOf=( "TE", (3,4), (5,6), (7,8) ) )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Subscriber( X12LoopBridge ):
    """Subscriber Data from the 2000B loop."""
    loopName= "2000B"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    nm106= ElementAccess( "NM1", 6 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    id= ElementAccess( "NM1", 9 )
    addr1= ElementAccess( "N3", 1 )
    addr2= ElementAccess( "N3", 2 )
    city= ElementAccess( "N4", 1 )
    state= ElementAccess( "N4", 2 )
    zip= ElementAccess( "N4", 3 )
    country= ElementAccess( "N4", 4 )
    payerResp= ElementAccess( "SBR", 1 )
    relCode= ElementAccess( "SBR", 2 )
    reference= ElementAccess( "SBR", 3 )
    name= ElementAccess( "SBR", 4 )
    insType= ElementAccess( "SBR", 5 )
    claimCode= ElementAccess( "SBR", 9 )
    rel= ElementAccess( "PAT", 1 )
    dateFormat= ElementAccess( "PAT", 5 )
    dod= ElementAccess( "PAT", 6 )
    measCode= ElementAccess( "PAT", 7 )
    weight= ElementAccess( "PAT", 8 )
    preg= ElementAccess( "PAT", 9 )
    dob= ElementAccess( "DMG", 2, x12type=D8 )
    gender= ElementAccess( "DMG", 3 )
    ssn= ElementAccess( "REF", 2, qualifier=(1,"SY") )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Paperwork( X12SegmentBridge ):
    """Claim Supplemental Information, contained within ClaimDetails."""
    rptType= ElementAccess( "PWK", 1 )
    transCD= ElementAccess( "PWK", 2 )
    AttCtlQual= ElementAccess( "PWK", 6 )
    AttCtl= ElementAccess( "PWK", 7 )

class ClaimDetails( X12LoopBridge ):
    """Claim Details from the 2300 Loop."""
    loopName= "2300"
    patAcct= ElementAccess( "CLM", 1 )
    amount= ElementAccess( "CLM", 2 )
    serviceLoc= ElementAccess( "CLM", 5 )
    respCode1= ElementAccess( "CLM", 6 )
    medAssign= ElementAccess( "CLM", 7 )
    assignBenInd= ElementAccess( "CLM", 8 )
    release= ElementAccess( "CLM", 9 )
    signature= ElementAccess( "CLM", 10 )
    relCauses= ElementAccess( "CLM", 11 )
    progCode= ElementAccess( "CLM", 12 )
    provAgree= ElementAccess( "CLM", 16 )
    respCode2= ElementAccess( "CLM", 18 )
    delayCode= ElementAccess( "CLM", 20 )
    admsType= ElementAccess( "CL1", 1 )
    admsSrc= ElementAccess( "CL1", 2 )
    dischStat= ElementAccess( "CL1", 3 )
    coveredDays= ElementAccess( "QTY", 2, qualifier=(1,"CA") )
    coveredDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"CA") )
    nonCoveredDays= ElementAccess( "QTY", 2, qualifier=(1,"NA") )
    nonCoveredDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"NA") )
    coInsuranceDays= ElementAccess( "QTY", 2, qualifier=(1,"CD") )
    coInsuranceDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"CD") )
    reserveDays= ElementAccess( "QTY", 2, qualifier=(1,"LA") )
    reserveDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"LA") )
    origClaimNo= ElementAccess( "REF", 2, qualifier=(1,"F8") )
    medLRec= ElementAccess( "REF", 2, qualifier=(1,"EA") )
    microID= ElementAccess( "REF", 2, qualifier=(1,"D9") )
    paperwork= SegmentSequenceAccess( "PWK", x12type=SegmentConversion(Paperwork) )

class Institutional_ClaimDetails( ClaimDetails ):
    """Institutional Claim Details from the 2300 Loop."""
    fmt= ElementAccess( "DTP", 2 )
    stmtDts= ElementAccess( "DTP", 3, qualifier=(1,"434") )
    admsDt= ElementAccess( "DTP", 3, qualifier=(1,"435") )
    dischHr= ElementAccess( "DTP", 3, qualifier=(1,"096") )
    billNote= ElementAccess( "NTE", 2, qualifier=(1,"ADD") )
    # Non-"ADD" "NTE" segments are claim notes -- legacy uses an array of up to 10.
    # Only for institutional claims.
    claimNotes= ElementSequenceAccess( "NTE", 2, qualPos=1, notInList=("ADD",) )

    # DR Composite (Diagnosis Related Group (DRG) Information)
    drg= CompositeAccess( "HI", "DR", 1 )
    # BP/BR Composite (Principal Procedure Information)
    prinProcCode= CompositeAccess( "HI", ("BR","BP"), 1 )
    # BF Composite (Diagnosis) can have a number of attributes
    diagCode= CompositeSequenceAccess( "HI", "BF" )
    # BG Composite (Condition Information) can have a number of attributes
    condCode= CompositeSequenceAccess( "HI", "BG" )
    # BK Composite (Principal Diagnosis) is split into two attributes
    prinDiagCode= CompositeAccess( "HI", "BK", 1 )
    admitDiagCd= CompositeAccess( "HI", "BK", 2 )
    # BO/BQ Composite (Other Procedure Information) has a number of attributes
    procCode= CompositeSequenceAccess( "HI", ("BQ","BO") )
    # BH Composite (Occurrence Information) has a number of attributes
    occrCode= CompositeSequenceAccess( "HI", "BH" )
    # BE Composite (Value Information) has a number of attributes
    valueCode= CompositeSequenceAccess( "HI", "BE" )
    # BI Composite (Occurrence Span Information) is not used
    # TC Composite (Treatment Code Information) is not used

class Professional_ClaimDetails( ClaimDetails ):
    """Professional Claim Details from the 2300 Loop."""
    fmt= ElementAccess( "DTP", 2 )
    intDt= ElementAccess( "DTP", 3, qualifier=(1,"454") )
    accidentDt= ElementAccess( "DTP", 3, qualifier=(1,"439") )
    onsetDt= ElementAccess( "DTP", 3, qualifier=(1,"431") )
    lmpDt= ElementAccess( "DTP", 3, qualifier=(1,"484") )
    prescDt= ElementAccess( "DTP", 3, qualifier=(1,"471") )

    measCode= ElementAccess("CR1", 1)
    weight= ElementAccess("CR1", 2)
    ambTransCode= ElementAccess("CR1", 3)
    ambTransReason= ElementAccess("CR1", 4)
    ambTransQual= ElementAccess("CR1", 5)
    ambTransQty= ElementAccess("CR1", 6)
    ambDescript= ElementAccess("CR1", 9)
    ambDescript2= ElementAccess("CR1", 10)

    claimNotes= ElementSequenceAccess( "NTE", 2 )

    diagCode= ElementAccess( "HI", SequenceOf(1,8) )
    homeHealthCd= ElementAccess( "CR7", 1 )
    visitsRend= ElementAccess( "CR7", 2 )
    visitsProj= ElementAccess( "CR7", 3 )

    codeCat= ElementAccess("CRC", 1 )
    cond= ElementAccess("CRC", SequenceOf(2,6) )
    ref1Num= ElementAccess( "REF", 2, qualifier=(1,"9F") )
    preAuth= ElementAccess( "REF", 2, qualifier=(1,"G1") )

class ServiceLine( X12LoopBridge ):
    """Service Line from the 2400 Loop."""
    loopName= "2400"
    SrvLNo= ElementAccess( "LX", 1 )
    format= ElementAccess( "DTP", 2 )
    srvDT= ElementAccess( "DTP", 3, qualifier=(1,"472") )
    dmeCode= ElementAccess( "SV5", 1 )
    qualifier= ElementAccess( "SV5", 2 )
    amt1= ElementAccess( "SV5", 3 )
    amt2= ElementAccess( "SV5", 4 )
    amt3= ElementAccess( "SV5", 5 )
    amt4= ElementAccess( "SV5", 6 )

class Institutional_ServiceLine( ServiceLine ):
    """Institutional Service Line from the 2400 Loop."""
    revenueCode= ElementAccess( "SV2", 1 )
    procID= ElementAccess( "SV2", 2 )
    amt= ElementAccess( "SV2", 3 )
    unitsQual= ElementAccess( "SV2", 4 )
    units= ElementAccess( "SV2", 5 )
    unitRate= ElementAccess( "SV2", 6 )
    amtNotCovered= ElementAccess( "SV2", 7 )

class Professional_ServiceLine( ServiceLine ):
    """Professional Service Line from the 2400 Loop."""
    srvID= ElementAccess( "SV1", 1 )
    amt= ElementAccess( "SV1", 2 )
    unitsQual= ElementAccess( "SV1", 3 )
    units= ElementAccess( "SV1", 4 )
    facCode= ElementAccess( "SV1", 5 )
    diagCode= ElementAccess( "SV1", 7 )
    respCode1= ElementAccess( "SV1", 9 )
    respCode2= ElementAccess( "SV1", 11 )
    respCode3= ElementAccess( "SV1", 12 )
    coPay= ElementAccess( "SV1", 15 )

class ServiceLineAdj( X12LoopBridge ):
    """Service Line Adjustment from the 2430 Loop."""
    loopName= "2430"
    idCode= ElementAccess( "SVD", 1 )
    amt= ElementAccess( "SVD", 2 )
    procID= ElementAccess( "SVD", 3 )
    svcID= ElementAccess( "SVD", 4 )
    qty= ElementAccess( "SVD", 5 )
    assNo= ElementAccess( "SVD", 6 )
    format= ElementAccess( "DTP", 2 )
    srvDT= ElementAccess( "DTP", 3, qualifier=(1,"579") )

class Claim( object ):
    """A claim, built from an X12 :samp:`837` message.
    
    :ivar submitter: A sequence of :class:`Submitter` instances from the 1000A loop.
    :ivar provider: A sequence of :class:`Provider` instances from the 2000A loop.
    :ivar subscriber: A sequence of :class:`Subscriber` instances from the 2000B loop.
    :ivar patient: A sequence of :class:`Institutional_Inpatient` instances from the 2000C loop.
    """
    def loops( self, theClass, anX12Message ):
        return [ theClass(loop) for loop in anX12Message.descendant( "loop", theClass.loopName ) ]
    def __init__( self, anX12Message ):
        """Examine the message and extract the relevant Loops."""
        # XXX - determine 837P vs. 837I and Inpatient vs. Outpatient
        self.submitter= self.loops( Submitter, anX12Message )
        print( "Loop 1000A, Submitter", map( str, self.submitter ) )
        self.provider= self.loops( Provider, anX12Message )
        print( "Loop 2000A, Billing Provider", map( str, self.provider ) )
        self.subscriber= self.loops( Subscriber, anX12Message )
        print( "Loop 2000B, Subscriber", map( str, self.subscriber ) )
        self.patient= self.loops( Institutional_Inpatient, anX12Message )
        print( "Loop 2000C, Patient", map( str, self.patient ) )
        # Loop 2300 - Claim Details
        self.claimDetails= self.loops( Institutional_ClaimDetails, anX12Message )
        print( "Loop 2300, Claim Details", map( str, self.claimDetails ) )
        # Loop 2400 - Service Lines
