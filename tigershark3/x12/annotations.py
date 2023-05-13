"""
Base annotations used to decorate types
with X12 Schema attributes.

These seem to overlap (to an extent) with JSON Schema.

There are distinctive annotations, unique to X12,
which must be provided as JSONSchema extensions.
"""
import re
import decimal
from typing import Any, get_origin, get_args, cast
from typing_extensions import _AnnotatedAlias
from types import GenericAlias, UnionType

class X12Annotation:
    def __init__(self, *parameters: Any) -> None:
        self.params = parameters

    def __repr__(self) -> str:
        match len(self.params):
            case 0:
                return f"{self.__class__.__name__}()"
            case 1:
                return f"{self.__class__.__name__}({self.params[0]!r})"
            case _:
                return f"{self.__class__.__name__}({', '.join(repr(p) for p in self.params)})"

    def __eq__(self, other: Any):
        if not isinstance(other, self.__class__):
            return NotImplemented
        else:
            return self.params == other.params

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return cast(dict[str, Any], {})

class Format(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"format": self.params[0]}

class Scale(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-scale": self.params[0]}

class MinLen(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"minLength": self.params[0]}

class MaxLen(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"maxLength": self.params[0]}

class Enumerated(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"enum": list(self.params)}

class Title(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"title": self.params}

class Usage(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-usage": self.params}

class Position(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-position": self.params}

class Syntax(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-syntax": self.params}

class Required(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        if self.params:
            return {"x-required": self.params[0]}
        return {"x-required": True}

class MinItems(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"min Items": self.params[0]}

class MaxItems(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"maxItems": self.params[0]}

class OtherMeta(X12Annotation):
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {self.params[0]: self.params[1]}


def json_schema(type_hint: type) -> dict[str, Any]:
    """
    Given a type hint (from ``typing.get_type_hints()``)
    return an equivalent JSON Schema.

    ..  todo:: Handle Union[T | None].
    """
    # if type_hint *is* an unannotated type, get_args() will fail.
    try:
        base, *annotations = get_args(type_hint)
    except ValueError:
        base = type_hint
        annotations = []
    # print(base, type(base), annotations)
    match base:
        case _ if isinstance(base, _AnnotatedAlias):
            # Descending into something like list[Annotated[str, ...]]
            schema = json_schema(base)
        case GenericAlias():
            origin = get_origin(base)
            if origin == list:
                item_type, *error = get_args(base)
                assert error == []
                schema = {"type": "array", "items": json_schema(item_type)}
            elif origin == dict:
                # Not sure what this might mean in JSON Schema.
                # Without further advice on values for propertyNames. we can't do much.
                schema = {"type": "object"}
            else:
                raise ValueError(f"Unsupported generic: {base!r}")
                # schema = {"x-unsupported": repr(base)}
        case _ if issubclass(base, str):
            schema = {"type": "string"}
        case _ if issubclass(base, int):
            schema = {"type": "integer"}
        case _ if issubclass(base, float):
            schema = {"type": "float"}
        case _ if issubclass(base, decimal.Decimal):
            schema = {"type": "string", "_class": "Decimal"}
        case _:
            raise ValueError(f"Unsupported type: {base!r}")
            schema = {"x-unsupported": repr(base)}
    for ann in annotations:
        match ann:
            case X12Annotation():
                schema |= ann.JSONSchema
    return schema
