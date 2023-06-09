"""
Base annotations used to decorate types
with X12 Schema attributes.

The X12 requirements overlap with JSON Schema, and
the :py:func:`json_schema` function emits
an annotation into JSON Schema format.

This is not a complete set of annotations
for all possible JSON Schema features.
This is the minimum set of anntations that
seem required for X12 message definitions.

::

    >>> from x12.annotations import *
    >>> from typing import Annotated

    >>> class XY:
    ...     x: Annotated[str, MinLen(2), MaxLen(3)]
    ...     y: Annotated[str, Format(r"\d+{2,3}")]

    >>> from typing import get_type_hints
    >>> hints = get_type_hints(XY, include_extras=True)
    >>> json_schema(hints['x'])
    {'type': 'string', 'minLength': 2, 'maxLength': 3}
    >>> json_schema(hints['y'])
    {'type': 'string', 'format': '\\\\d+{2,3}'}

"""
import re
from decimal import Decimal
import sys
from typing import Any, get_origin, get_args, cast
from typing_extensions import _AnnotatedAlias
from types import GenericAlias, UnionType

class X12Annotation:
    """
    Superclass for X12 annotations.
    Each Annotation instance is part of the ``Annotated[]`` definition in the :py:mod:`typing` module.
    """
    validation = False  #: Should this be used for validation?

    def __init__(self, *parameters: Any) -> None:
        self.params = tuple(parameters)

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

    def __hash__(self) -> int:
        return (hash(self.__class__) + hash(self.params))  % sys.hash_info.modulus

    @property
    def JSONSchema(self) -> dict[str, Any]:
        """Emits the JSON Schema for this annnotation."""
        return cast(dict[str, Any], {})

    def invalid(self, source: str) -> str | None:
        """
        Returns None if valid (i.e., not invalid).
        Returns message for ValueError if invalid.
        ::

            if msg := ann.invalid(text):
                raise ValueError(msg)

        Or. Accumulate a list of problems.
        ::

            errors = list(filter(None, (ann.invalid(text) for ann in annotations))
            if errors:
                raise ValueError('; '.join(errors))
        """
        return None

class Format(X12Annotation):
    """
    The Format(...) annotation. The parameter is a regular expression that is checked.
    """
    validation = True

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"format": self.params[0]}

    def invalid(self, source: str) -> str | None:
        if re.match(self.params[0], source) is None:
            return f"invalid format for {source!r}, not {self.params[0]}"
        return None

class Scale(X12Annotation):
    """
    The Scale(...) annotation for decimal numbers.
    The parameter is the number of decimal places to impose on a string of digits.

    ::

        x: Annnotated[Decimal, Scale(2)]

    Will convert ``'4200'`` to ``Decimal('42.00')``.
    """

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-scale": self.params[0]}

class MinLen(X12Annotation):
    """
    The MinLen(...) nnotation for strings.
    """
    validation = True

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"minLength": self.params[0]}

    def invalid(self, source: str) -> str | None:
        if source is None:
            return None
        if len(source) < self.params[0]:
            return f"invalid length for {source!r}, less than {self.params[0]}"
        return None

class MaxLen(X12Annotation):
    """
    The MaxLen(...) annotation for strings.
    """
    validation = True

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"maxLength": self.params[0]}

    def invalid(self, source: str) -> str | None:
        if source is None:
            return None
        if len(source) > self.params[0]:
            return f"invalid length for {source!r}, greater than than {self.params[0]}"
        return None

class Enumerated(X12Annotation):
    """
    The Enumerated(...) annotation for strings.

    This is similar to ``typing.Literal[]``.
    """
    validation = True

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"enum": list(self.params)}

    def invalid(self, source: str) -> str | None:
        if source is None:
            return None
        if source not in self.params:
            return f"invalid value for {source!r}, not in {self.params}"
        return None

class Title(X12Annotation):
    """
    A Title("Name of the field") annotation.
    """

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"title": self.params[0]}

class Usage(X12Annotation):
    """
    A Usage("R"|"S"|"N") annotation.
    """

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-usage": self.params[0]}

class Position(X12Annotation):
    """
    A Position(n) annotation.
    """
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-position": self.params[0]}

class Syntax(X12Annotation):
    """
    A Syntax() annotation with a collection of
    strings to define some more complex validation rules.
    """
    def __init__(self, *parameters: Any) -> None:
        self.params = tuple(tuple(p) for p in parameters)

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"x-syntax": list(self.params)}

class Required(X12Annotation):
    """
    A Reqired(True | False) annotation.

    This repeats the :py:class:`Usage` annotation.
    It's often a derived value.
    """
    @property
    def JSONSchema(self) -> dict[str, Any]:
        if self.params:
            return {"x-required": self.params[0]}
        return {"x-required": True}

class MinItems(X12Annotation):
    """
    The MinItems(...) annotation for arrays.
    """
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"min Items": self.params[0]}

class MaxItems(X12Annotation):
    """
    The MaxItems(...) annotation for arrays.
    """
    @property
    def JSONSchema(self) -> dict[str, Any]:
        return {"maxItems": self.params[0]}

class OtherMeta(X12Annotation):
    """
    A placeholder for additional JSON Schema
    attributes.
    """
    def __init__(self, **parameters: Any) -> None:
        self.meta_params = parameters
        self.params = tuple(self.meta_params.items())

    @property
    def JSONSchema(self) -> dict[str, Any]:
        return self.meta_params

    def __repr__(self) -> str:
        nv_text = ", ".join(
            f"{name}={value!r}"
            for name, value in self.meta_params.items()
        )
        return f"{self.__class__.__name__}({nv_text})"

def json_schema(type_hint: type) -> dict[str, Any]:
    """
    Given a type hint (from ``typing.get_type_hints()``)
    return an equivalent JSON Schema.

    :param type_hint: the type hint to expand into JSON Schema notation.
    :returns: a dictionary with the JSON Schema for the given hint.

    ..  todo:: Handle Union[T | None].
    """
    # if type_hint *is* an unannotated type, get_args() will fail.
    try:
        base, *annotations = get_args(type_hint)
    except ValueError:
        base = type_hint
        annotations = []
    # print(base, type(base), annotations)
    match base():
        case _AnnotatedAlias():  # type: ignore[misc]
            # Descending into something like list[Annotated[str, ...]]
            schema = json_schema(base)
        case []:
            origin = get_origin(base)
            item_type, *error = get_args(base)
            assert error == []
            schema = {"type": "array", "items": json_schema(item_type)}
        case {}:
            # Not clear where the details might be for this.
            schema = {"type": "object"}
        case str():
            schema = {"type": "string"}
        case int():
            schema = {"type": "integer"}
        case float():
            schema = {"type": "float"}
        case Decimal():
            schema = {"type": "string", "_class": "Decimal"}
        case _:
            raise ValueError(f"unsupported type: {base!r}")
            schema = {"x-unsupported": repr(base)}
    for ann in annotations:
        match ann:
            case X12Annotation():
                schema |= ann.JSONSchema
    return schema
