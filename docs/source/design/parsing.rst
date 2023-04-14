..  _`design.parsing`:

##################################
Parsing An Exchange-Format Message
##################################

An exchange-format X12 EDI message is a sequence of segments.
Each segment has an identifier of 2 or 3 characters, and a sequence of element values.

..  uml::

    class MessageText

    class SegmentText

    class Identifier

    class Value

    MessageText *--> "n" SegmentText

    SegmentText *--> "1" Identifier

    SegmentText *--> "v" Value

For example, the following segment uses "|" as an element separator and "~" as a segment separator.

::

    ST|271|0001~

This segment can be viewed as three string values, "ST", "271", and "0001".
The first string value is the segment identifier.

Alternatively, this segment can be viewed as an identifier and separator, "ST|",
followed by two string values, "271" and "0001".

We generally choose the former view, which permits simple use of the :meth:`string.split()` method
to split the segment into fields.
The first field is the identifier, used for parsing the structure of a message and the loops.
The remaining values are assigned to elements and composites of the segment.

Conceptually, the parsing uses approach similar to the following:

::

    identifier, *fields = segment_text.split(separator)
    segment_class[identifier].build_attrs(fields)

Pragmatically, it's a bit more complicated for two reasons:

1.  Loops are not present in the text representation.
    A loop contains one or more segments, defining an expected sequence of segments.

2.  Composites are not present in the text representation.
    A composite contains a number of elements; it's a kind of sub-segment.

This means we have the following relationships.

..  uml::

    class Message

    class MessageText

    Message -- MessageText : Represented By >

    class Loop

    Message *--> "n" Loop

    class Segment

    Loop *--> "n" Segment
    Loop *--> "n" Loop

    class SegmentText

    Segment -- SegmentText : Represented By >

    MessageText *--> "n" SegmentText

    class Composite
    class Element

    Segment *--> Composite
    Segment *--> Element
    Composite *--> Element

    class Value

    SegmentText *--> Value
    Element -- Value : Represented By >

The essential algorithm works by consuming the segments to locate the loops within a message.
A source lexical scanner can "peek" at the heading of the next segment.
The loop parser can use the heading to decide if it should consume the next segment or if it is finished consuming segments.

Consuming a segment means locating the elements and composites (sequences of elements) within the segment, and assigning text
values to those elements and composites. This is slightly different from consuming segments because there are fewer choices
to be made. The process has two layers: each element consumes one value; each composite consumes a sequence of values.
