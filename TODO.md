# TODO: 2023-05-21
[x] Rewrite `test_x12_base.py` to remove all `Schema`. 

[x] Mark `Schema` references in `base` and `tools` as deprecated. 

[x] Add `skip_validation` parameter to `Message.parse()`, `Segment.parse()` and `Composite.parse()`.

[x] Test with these skips

   a. Skip *_ISA:*:MinLen check  -- This is Universal -- Always needed.
   
   b. Skip *_N1:n101:Enumerated check -- This is a debugging special case.
   
   c. Skip *_HL:hl03:Enumerated check -- This is a debugging special case.

[x] Move skip_validation OUT of annotation and composite and keep it in Segment. Change Exception raised in Annotation to include Annotation class name.

[x] Create "class_fields" function (with @cache decorator) to provide the list of fields with _SpecialForm's removed.

[ ] Remove Schema Interim solution.

[ ] Add new annotation-based features


