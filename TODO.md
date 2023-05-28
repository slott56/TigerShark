# TODO: 2023-05-21
[x] Rewrite `test_x12_base.py` to remove all `Schema`. 

[x] Create "class_fields" function (with @cache decorator) to provide the list of fields with _SpecialForm's removed.

[x] Revise `test_x12_types` to remove all `Schema`.

[x] Remove "Interim Explicit Schema" solution from `base`.

[ ] Unify the various "Peel the Onion" algorithms.

Option 1: a common `TypeVisitor` class.

```python

class TypeVisitor:
    """Post-order traversal of structures."""
    def __init__(self) -> None:
        pass
    def visit(self, name: str, field_type: type[Any]) -> None:
        match field_type:
            case _GenericAlias() if get_origin(loop_type) is list:
                repeating_type = get_args(loop_type)[0]
                self.visit(name, repeating_type)
                self.do_list_wrapper(name, field_type)
            case _AnnotatedAlias():
                base_type = get_args(loop_type)[0]
                self.visit(name, base_type)
                self.do_annotated_wrapper(name, field_type)
            case UnionType():
                # find non-None alternatives.
                alternatives = get_args(field_type)
                for alt in alternatives:
                    if alt is not None:
                        self.visit(alt)
                self.do_union_wrapper(name, field_type)
            case type() if issubclass(field_type, Segment):
                for name, seg_field_tp in class_fields(field_type):
                    self.visit(name, seg_field_tp)
                self.do_segment(name, field_type)
            case type() if issubclass(field_type, Composite):
                for name, comp_field_tp in class_fields(field_type):
                    self.visit(name, comp_field_tp)
                self.do_composite(name, field_type)
            case type() if issubclass(field_type, Loop):
                for name, loop_field_tp in class_fields(field_type):
                    self.visit(name, loop_field_tp)
                self.do_loop(name, field_type)
            case type() if issubclass(field_type, Message):
                for name, msg_field_tp in class_fields(field_type):
                    self.visit(name, msg_field_tp)
                self.do_message(name, field_type)
            case type() is issubclass(field_type, (str, int, float, Decimal, datetime.date, datetime.time));
                self.do_primitive(name, field_type)
```

Option 2: a common higher-order function for type walking.
This has a large list of kwarg functions that
are called for each piece of the structure.

```python`
def type_walker(name: str, field_type: type[Any], **kwargs: Callback) -> None:
    match field_type:
        case _GenericAlias() if get_origin(loop_type) is list:
            repeating_type = get_args(loop_type)[0]
            type_walker(name, repeating_type, **kwargs)
            kwargs["list_wrapper"](name, field_type)
        # and etc.
```
