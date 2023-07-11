"""Test the x12.annotations"""
from decimal import Decimal
from typing import Annotated, get_type_hints, get_origin, get_args
from x12.annotations import *

def test_format():
    class X:
        some_var: Annotated[str, Format(r"\d+")]
    th = get_type_hints(X, include_extras=True)
    assert get_args(th['some_var']) == (str, Format(r"\d+"))
    assert repr(th['some_var']) == "typing.Annotated[str, Format('\\\\d+')]"
    assert json_schema(th['some_var']) == {'format': '\\d+', 'type': 'string'}

def test_scale():
    class X:
        some_var: Annotated[Decimal, Scale(2)]
    th = get_type_hints(X, include_extras=True)
    assert get_args(th['some_var']) == (Decimal, Scale(2))
    # print(repr(th['some_var']))
    assert repr(th['some_var']) == "typing.Annotated[decimal.Decimal, Scale(2)]"
    assert json_schema(th['some_var']) == {'_class': 'Decimal', 'type': 'string', 'x-scale': 2}


def test_minlen_maxlen():
    class X:
        some_var: Annotated[str, MinLen(2), MaxLen(4)]
    th = get_type_hints(X, include_extras=True)
    assert get_args(th['some_var']) == (str, MinLen(2), MaxLen(4))
    # print(repr(th['some_var']))
    assert repr(th['some_var']) == "typing.Annotated[str, MinLen(2), MaxLen(4)]"
    assert json_schema(th['some_var']) == {'maxLength': 4, 'minLength': 2, 'type': 'string'}


def test_enumerated():
    class X:
        some_var: Annotated[str, Enumerated("This", "That")]
    th = get_type_hints(X, include_extras=True)
    assert get_args(th['some_var']) == (str, Enumerated("This", "That"))
    # print(repr(th['some_var']))
    assert repr(th['some_var']) == "typing.Annotated[str, Enumerated('This', 'That')]"
    assert json_schema(th['some_var']) == {'enum': ['This', 'That'], 'type': 'string'}


def test_title_usage_position_syntax():
    class X:
        some_var: Annotated[str, Title("Title"), Usage("R"), Position("1"), Syntax(["P2P3"])]
    th = get_type_hints(X, include_extras=True)
    assert get_args(th['some_var']) == (str, Title("Title"), Usage("R"), Position("1"), Syntax(("P2P3",)))
    # print(repr(th['some_var']))
    assert repr(th['some_var']) == "typing.Annotated[str, Title('Title'), Usage('R'), Position('1'), Syntax(('P2P3',))]"
    assert json_schema(th['some_var']) == {'title': 'Title', 'type': 'string', 'x-position': '1', 'x-syntax': [('P2P3',)], 'x-usage': 'R'}


def test_required_maxItems():
    class X:
        some_var: Annotated[list[str], Required(), MaxItems(2)]
    th = get_type_hints(X, include_extras=True)
    assert get_args(th['some_var']) == (list[str], Required(), MaxItems(2))
    ann = get_args(th['some_var'])[0]
    assert get_args(ann) == (str,)
    # print(repr(th['some_var']))
    assert repr(th['some_var']) == "typing.Annotated[list[str], Required(), MaxItems(2)]"
    assert json_schema(th['some_var']) == {'maxItems': 2, 'type': 'array', 'items': {'type': 'string'}, 'x-required': True}

def test_title_otherMeta():
    class X:
        some_var: Annotated[str, OtherMeta(name="value")]
    th = get_type_hints(X, include_extras=True)
    assert get_args(th['some_var']) == (str, OtherMeta(name="value"))
    # print(repr(th['some_var']))
    assert repr(th['some_var']) == "typing.Annotated[str, OtherMeta(name='value')]"
    assert json_schema(th['some_var']) == {'name': 'value', 'type': 'string'}
