..  _`Recursive Structures`:

########################################
Design Note: Recursive Structures in SQL
########################################

:ref:`architecture`

Problem
=======

Recursive structures, as exemplified by the Loop definition, are a long-standing
problem in SQL.  While pure SQL can -- to an extent -- cope, an ORM mapping of
a class hierarchy makes this more difficult.

Specifically, Django's strongly-typed mapping to SQL is challenging because of the
way it handles superclasses.  Any class with a Model attribute must become
a distinct table.  A superclass must either be "abstract" in that it has no
Model attributes, or "concrete" and allocated to a distinct table.

Forces
======

The standard technique for recursive structures involves a polymorphic design,
as shown in `Figure 1`_.

.. figure:: polymorphic.png

    _`Figure 1`.

This shows the standard object design for recursive structures.  The
superclass (X12Structure) has a number of subclasses.  The X12Loop
class can contain any mixture of X12Structures (X12Loop or X12Segment).

This doesn't work in Django because we don't have polymorphism.
Django forces us to target a specific class, not a polymorphic union of classes.

We have two principle choices.

-   A Loop contains two collections: Subloops and Segments.  A sequence
    number can be used to order the union of Loops and Segments and
    reconstruct the original Loop with the Loops and Segments the correct order.

    In this case, the children method is a fairly complex Union query (which aren't directly
    supported in Django).  We must do two queries, then merge the results
    into a Python list structure.

    When we add Loops or Segments to a Loop they go into their appropriate
    collection with a proper sequence number.

-   A Loop can contain either a collection subLoops or a single Segment.
    Some Loops are the degenerate case
    which contain exactly one Segment and no subLoops.  These degenerate
    SubLoops don't even have names.  Other Loops have a name and subLoops (but no Segment.)

    In this case, we have a ``children`` method which does a ``subloop_set.all()``
    query, then iterates through this result set, replacing degenerate Loops
    with their one-and-only child Segment to create a proper List that contains
    mixed Loops and Segments in their correct order.

    When we append a Segment to a Loop, we have to do a two-step
    operation: append the degenerate Loop, then put the Segment in the degerate
    Loop.

    When we append a Loop to a Loop, we simply append the Loop.

Solution
========

The Django-friendly design is shown in `Figure 2`_.

.. figure:: stronglytyped.png

    _`Figure 2`.

This shows the basic Message - Loop - Segment structure.  It also shows the
constraint imposed on Loops: they either contain subloops or a single Segment.
While it seems appealing to have multiple segments, it isn't practical to keep
the sequence numbering straight.

Consequence
===========

We won't have a simple polymorphic, recursive container.

Either solution requires that we provide navigation methods.
The XPath standard provides guidance on what this navigation should look like.

We need a unique keys for a message (and all loops and segments of that
message) plus we need unique keys for the loops.  See :ref:`Key Generation` for
more information on this issue.
