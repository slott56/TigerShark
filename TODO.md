# TODO: 2023-05-21
[x] Rewrite `test_x12_base.py` to remove all `Schema`. 

[x] Mark `Schema` references in `base` and `tools` as deprecated. 

[ ] Add `skip_validation` parameter to `Message.parse()`, `Segment.parse()` and `Composite.parse()`.

[ ] Test with these skips

   a. Skip *_ISA:*:MinLen check  -- This is Universal -- Always needed.
   
   b. Skip *_N1:n101:Enumerated check -- This is a debugging special case.
   
   c. Skip *_HL:hl03:Enumerated check -- This is a debugging special case.

[ ] Add new annotation-based features


# How validation overrides are injected

The validation happens 
in `Segment.parse()` and `Composite.parse()` methods.
These tailor the helpers used by the `__init__()` methods.

The `Message.parse()`  and `Loop.parse()` get `["*_ISA:*:MinLen"]`.
They passe `[":*:MinLen"]` to Segments
with names matching `'*_ISA'`. The `Segment.parse()` passes 
this down to `Composite.parse()`.

`SomeSegment.parse(text, skip_validation=[":*:MinLen", etc.])`

The generic `Segment.parse()` and `Composite.parse()` methods
can uses the name and skip option with the named field's
helper object construction.

The `__init__()` will then have the proper special-cases.

