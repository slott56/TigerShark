#####################################
How Validation Works
######################################

The validation happens in the :py:class:`Segment` and :py:class:`Composite`
classes. The :py:meth:`__init__`  methods validate each
individual field's value.

The :py:meth:`Segment.parse` and :py:meth:`Composite.parse` methods
are class methods, inherited by each :py:class:`Segment`
and :py:class:`Composite` subclass. These do three things:

1. Build "helper" objects for the individual elements.

2. Create a dictionary of validation exceptions.

3. Invoke the helper to validate the field. This uses a ``try:`` block and ValueError exceptions can be silenced.

The ``skip_validation`` parameter is a list of strings,
each one provides a pattern for Segment names, field names,
and annotations that can be skippped.

For example ``*_ISA:*:MinLen`` will bypass the MinLen annotation
for all elements of segments named "ISA".

The Leading ``*_`` for the segment is used because segments
can be reused in multiple loop contexts.
The **xml_extract** tool creates these long names.

The :py:meth:`Message.parse`  and :py:meth:`Loop.parse` methods
get the ``skip_validateion`` value (e.g., ``["*_ISA:*:MinLen"]``).
They filter the list and pass the
relevant subset down to :py:class:`Segment` subclasses that
match the first part of the name.
The rules are cached at the segment level by the :py:meth:`Segment.save_validation` method.
The rules are *applied* by both the segment and composite classes,
but the name matching is at the segment level for any
fields in a composite inside a segment.

Common Practice
===============

 Handle compressed ISA header by skipping validation.

::

     compressed_headers = ["*_ISA:*:MinLen"]
