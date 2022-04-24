"""
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
"""
import datetime
from decimal import Decimal


class Facade(object):
    def loops(self, theClass, anX12Message, *args, **kwargs):
        return [theClass(loop, *args, **kwargs) for loop in
                anX12Message.descendant("loop", theClass.loopName)]


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
        """Return all matching X12Segments that are children of the X12Loop.
        Do not check descendants, only check immediate children.
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
        segList= [ s for s in self.loop.child( "segment", name ) ]
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


class SegmentAccess( object ):
    """Used to get a single segment.

    Best used in Conjunction with X12SegmentBridge, eg:
        class NamedEntity(X12SegmentBridge):
            last_name = ElementAccess("NM1", 3)

        class InformationSource(X12LoopBridge):
            loopName = "1000"
            entity_details = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))

        class InformationReceiver(X12LoopBridge):
            loopName = "2000"
            entity_details = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))

    """
    def __init__( self, segment, qualifier=None, x12type=None ):
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
        return "SegmentAccess( %r, %r, %s )" % ( self.segment, self.qualifier, typeName )

    def __get__( self, instance, owner ):
        """Get the requested Segment and convert it, if applicable.

        :param instance: An X12LoopBridge object.
        """
        if self.qualifier is None:
            segBridge = instance.segment( self.segment, )
        else:
            segBridge = instance.segment( self.segment, self.qualifier[0], inList=self.qualifier[1:] )
        if segBridge is None:
            return None
        return self.x12type.x12_to_python(segBridge.segment)

    def __set__( self, instance, value ):
        raise UnimplementedError( "Can't set segment sequences, yet")


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
        return "SegmentSequenceAccess( %r, %r, %s )" % ( self.segment, self.qualifier, typeName )
    def __get__( self, instance, owner ):
        # XXX - Some are unfiltered...
        if self.qualifier is None:
            segBridgeList= instance.segList( self.segment, )
        else:
            segBridgeList= instance.segList( self.segment, self.qualifier[0], inList=self.qualifier[1:] )
        return [ self.x12type.x12_to_python(segBridge.segment) for segBridge in segBridgeList ]
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

    The instance object that has ElementAccess attribtues may influence the
    default qualifier used. For example:

        class Person(X12LoopBridge):
            first_name = ElementAccess("NM1", 4)
            last_name = ElementAccess("NM1", 3, qualifier=(1, "IL"))

            def __init__(self, aLoop):
                self.qualifier = (1, "QC")
                super(Person, self).__init__(aLoop)

    When you instantiate this Person class, the resulting object will have a
    first_name ElementAccess attributes that uses (1, "QC") as its qualifier,
    and a last_name ElementAccess that uses (1, "IL"). This is pretty awful,
    and I do apologize for the weird behavior but I have a deadline to meet.
    At least I left behind this helpful comment...

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

    def get_qualifier(self, instance, owner):
        """ Allow instance to influence the qualifier.
        
        This is a huge, regrettable hack. This will cause bugs that will take
        you hours to track down. I'm so sorry.

        I promise I'll come back some day and make all of this more reasonable,
        but I need to get this running asap.
        """
        if self.qualifier is None or self.qualifier == (None,):
            if hasattr(instance, 'qualifier'):
                return instance.qualifier
        else:
            return self.qualifier
        return (None,)

    def __get__( self, instance, owner ):
        qualifier = self.get_qualifier(instance, owner)
        if isinstance(instance, X12LoopBridge):
            segBridge= instance.segment( self.segment, qualifier[0], inList=qualifier[1:] )
        else:
            # ElementAccess works on a Segment which doesn't include qualifier
            # info, so make sure the current Segment has the qualifier 
            if qualifier[0] is None or \
                    instance.segment.getByPos(qualifier[0]) == qualifier[1]:
                segBridge = instance
            else:
                segBridge = None
        if segBridge is None:
            raw = None
        else:
            raw = self.position.get( segBridge.segment )
        if self.x12type is not None:
            return self.x12type.x12_to_python( raw )
        else:
            return raw
    def __set__( self, instance, value ):
        qualifier = self.get_qualifier(instance, owner)
        if x12type is not None:
            raw= self.x12type.python_to_x12( value )
        else:
            raw= value
        segBridge= instance.segment( self.segment, qualifier[0], inList=qualifier[1:] )
        if segBridge is None:
            raise MissingSegment( "Segment %s (%r) Not Found" % ( self.segment, qualifier ) )
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
        return "ElementSequenceAccess( %r, %r, %r, %s )" % ( self.segment, self.position, self.qualPos, typeName )
    def __get__( self, instance, owner ):
        segs= instance.segList( self.segment, self.qualPos, self.inList, self.notInList )
        raw_list = [ s.segment.getByPos(self.position) for s in segs ]
        if self.x12type is not None:
            return [self.x12type.x12_to_python( raw ) for raw in raw_list]
        else:
            return raw_list
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


class TM(Conversion):
    """Convert between TM format time to proper datetime.time objects."""
    @staticmethod
    def x12_to_python(raw):
        if raw is None or raw == "":
            return raw
        if len(raw) < 4:
            return ""
        hh, mm = int(raw[0:2]), int(raw[2:4])
        ss = 0
        dd = 0  # hundredths of a second / centiseconds
        if len(raw) >= 6:
            ss = int(raw[4:6])
        if len(raw) >= 7:
            dd = int(raw[6:])
        dd = dd * 10  # milliseconds
        dd = dd * 100  # microseconds
        return datetime.time(hh, mm, ss, dd, None)

    @staticmethod
    def python_to_x12(value):
        if value is None:
            return ""
        return "{time}{centiseconds}".format(
                time=value.strftime("%H%M%S"),
                centiseconds=int(value.microsecond / 10000))


class D8( Conversion ):
    """Convert between D8 format dates to proper DateTime objects."""
    @staticmethod
    def x12_to_python( raw ):
        if raw is None:
            return raw
        yy,mm,dd = int(raw[0:4]), int(raw[4:6]), int(raw[6:8])
        return datetime.date( yy,mm,dd )
    @staticmethod
    def python_to_x12( value ):
        if value is None:
            return ""
        return value.strftime( "%4Y%2m%2d" )


class DR( Conversion ):
    """Convert between DR format dates to proper DateTime objects."""
    @staticmethod
    def x12_to_python( raw ):
        if raw is None or raw == "":
            return None
        d1, punct, d2 = raw.partition('-')
        if d1 is None or d2 is None or d1 == "" or d2 == "":
            return None
        yy1,mm1,dd1 = int(d1[0:4]), int(d1[4:6]), int(d1[6:8])
        yy2,mm2,dd2 = int(d2[0:4]), int(d2[4:6]), int(d2[6:8])
        return datetime.date( yy1,mm1,dd1 ), datetime.date( yy2,mm2,dd2 )
    @staticmethod
    def python_to_x12( value ):
        if value is None:
            return ""
        d1, d2 = value
        return "%s-%s" % ( d1.strftime( "%4Y%2m%2d" ), d2.strftime( "%4Y%2m%2d" ) )


class SegmentConversion( Conversion ):
    __name__ = "SegmentConversion"
    """Convert between an X12Segment and a proper Python object."""
    def __init__( self, someClass ):
        self.someClass= someClass

    def x12_to_python( self, raw ):
        return self.someClass( raw )

    def python_to_x12( self, value ):
        return value.segment


class XDecimal(Conversion):
    @staticmethod
    def x12_to_python(raw):
        if raw == "" or raw is None:
            return Decimal(0.0)
        if "(" in raw:
            raw = raw.replace("(", "-").replace(")", "")
        return Decimal(raw)

    @staticmethod
    def python_to_x12(value):
        if isinstance(value, str):
            return value
        return "{}".format(value)


class Money(XDecimal):
    @staticmethod
    def python_to_x12(value):
        if isinstance(value, str):
            return value
        return "{:.2f}".format(value)


def enum(options, raw_unknowns=False):
    """Translate abbreviations or codes into descriptions.

    :param options: A dictionary of code:description
    :type options: dict
    :param raw_unknowns: Whether or not to return the raw value if it's not
    in the options dict.
    :type raw_unknowns: boolean

    For example:

    class Header(X12LoopBridge):
        loopName = "HEADER"
        type = ElementAccess("BPR", 1, x12type=enum(
            {"C": "Payment accompanies remittance advice",
             "D": "Make payment only",
             "H": "Notification only",
             "I": "Remittance information only",
             "P": "Prenotification of future transfers",
             "U": "Split payment and remittance",
             "X": "Handling party's option to split payment and remittance."},
             raw_unknowns=True))
    header.type -> ("C", "Payment accompanies remittance advice")

    # Or an unknown type, say "Z":
    header.type -> "Z"
    """
    class Enum(Conversion):
        @staticmethod
        def x12_to_python(raw):
            if raw == "" or raw is None:
                return None
            elif raw in options:
                return (raw, options[raw])
            elif raw_unknowns:
                return raw
            return None

        @staticmethod
        def python_to_x12(value):
            if value is None or value == "":
                return ""
            elif value in options:
                return value
            else:
                for (k,v) in options.iteritems():
                    if value == v:
                        return k
            if raw_unknowns:
                return value
            return ""
    return Enum


def boolean(match):
    """ True if the field matches match. Match must be a string. """
    class Boolean(Conversion):
        @staticmethod
        def x12_to_python(raw):
            return raw == match

        @staticmethod
        def python_to_x12(value):
            return match
    return Boolean
