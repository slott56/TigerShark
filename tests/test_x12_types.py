"""
Test base X12ElementHelper
and the various Annotations that are used.
"""
import datetime
from decimal import Decimal
from typing import Annotated, get_type_hints, TypeAlias

from unittest.mock import sentinel, Mock, call
from pytest import fixture, raises, mark

import x12
from x12 import base


def test_type_factory_annotated():
    ID: TypeAlias = Annotated[str, base.Format(r"\d+")]

    class SomeSegment:
        some_element: Annotated[ID, base.Title('some_element'), base.MinLen(2), base.MaxLen(2)]
        another_element: str
        optional_element: Annotated[ID, base.Title('optional_element'), base.MinLen(2), base.MaxLen(2)] | None
        list_element: list[str]

    hints = get_type_hints(SomeSegment, include_extras=True)

    gen_type_some = base.X12ElementHelper.annotated(hints['some_element'])
    assert isinstance(gen_type_some, base.X12ElementHelper)

    assert gen_type_some.validate('12') is None
    with raises(ValueError):
        gen_type_some.validate('ab')
    with raises(ValueError):
        gen_type_some.validate('123')
    with raises(ValueError):
        gen_type_some.validate('1')

    gen_type_another = base.X12ElementHelper.annotated(hints['another_element'])
    assert isinstance(gen_type_another, base.X12ElementHelper)

    assert gen_type_another.validate('12') is None

    gen_type_optional = base.X12ElementHelper.annotated(hints['optional_element'])
    assert gen_type_optional is None

    get_type_list_str = base.X12ElementHelper.annotated(hints['list_element'])
    assert get_type_list_str is None


def test_annotated_antype():
    AN: TypeAlias = str
    class SomeSegment:
        an_element: Annotated[AN, base.Title('an_element'), base.MinLen(2), base.MaxLen(2)]
    hints = get_type_hints(SomeSegment, include_extras=True)

    an = base.X12ElementHelper.annotated(hints['an_element'])
    assert an.to_py("01") == "01"
    assert an.to_str('1') == "1 "


def test_annotated_btype():
    B: TypeAlias = str
    class SomeSegment:
        b_element: Annotated[B, base.Title('b_element'), base.MinLen(2), base.MaxLen(2)]
    hints = get_type_hints(SomeSegment, include_extras=True)

    b = base.X12ElementHelper.annotated(hints['b_element'])
    assert b.to_py("01") == "01"
    assert b.to_str('1') == "1 "


def test_annotated_dttype():
    DT: TypeAlias = datetime.date
    class SomeSegment:
        dt_element: Annotated[DT, base.Title('dt_element'), base.MinLen(8), base.MaxLen(8), base.Format(r"\d{8}")]
    hints = get_type_hints(SomeSegment, include_extras=True)

    dt = base.X12ElementHelper.annotated(hints['dt_element'])
    assert dt.to_py("20230203") == datetime.date(2023, 2, 3)
    assert dt.to_str(datetime.date(2023, 2, 3)) == "20230203"

    assert dt.to_py(None) is None

    # Edge case of no input to provide a preferred format.
    dt2 = base.X12ElementHelper.annotated(hints['dt_element'])
    assert dt2.to_str(datetime.date(2023, 2, 3)) == "230203"


def test_annotated_idtype():
    ID: TypeAlias = str
    class SomeSegment:
        id_element: Annotated[ID, base.Title('id_element'), base.MinLen(2), base.MaxLen(2)]
    hints = get_type_hints(SomeSegment, include_extras=True)

    id_obj = base.X12ElementHelper.annotated(hints['id_element'])
    assert id_obj.to_py("1") == "1"
    assert id_obj.to_str("1") == "1 "


def test_annotated_rtype():
    R: TypeAlias = float
    class SomeSegment:
        r_element: Annotated[R, base.Title('r_element'), base.MinLen(2), base.MaxLen(6)]
    hints = get_type_hints(SomeSegment, include_extras=True)

    r = base.X12ElementHelper.annotated(hints['r_element'])
    assert r.to_py("42") == 42.0
    assert r.to_str(42.0) == "42"

    assert r.to_py(None) is None


def test_annotated_tmtype():
    TM: TypeAlias = datetime.time
    class SomeSegment:
        tm_element: Annotated[TM, base.Title('dt_element'), base.MinLen(4), base.MaxLen(4), base.Format(r"\d{4}")]
    hints = get_type_hints(SomeSegment, include_extras=True)

    tm = base.X12ElementHelper.annotated(hints['tm_element'])
    assert tm.to_py("1317") == datetime.time(13, 17)
    assert tm.to_str(datetime.time(13, 17)) == "1317"

    assert tm.to_py(None) is None


def test_annotated_ntype():
    N: TypeAlias = int
    class SomeSegment:
        n_element: Annotated[N, base.Title('n_element'), base.MinLen(9), base.MaxLen(9)]
    hints = get_type_hints(SomeSegment, include_extras=True)

    n = base.X12ElementHelper.annotated(hints['n_element'])
    assert n.to_py("42") == Decimal('42')
    assert n.to_str(42) == "000000042"


def test_annotated_n0type():
    N0: TypeAlias = Annotated[Decimal, base.Scale(0)]
    class SomeSegment:
        n0_element: Annotated[N0, base.Title('n0_element'), base.MinLen(9), base.MaxLen(9)]
    hints = get_type_hints(SomeSegment, include_extras=True)

    n0 = base.X12ElementHelper.annotated(hints['n0_element'])
    assert n0.to_py("42") == Decimal('42')
    assert n0.to_str(Decimal('42')) == "000000042"


def test_annotated_n2type():
    N2: TypeAlias = Annotated[Decimal, base.Scale(2)]
    class SomeSegment:
        n2_element: Annotated[N2, base.Title('n2_element'), base.MinLen(1), base.MaxLen(15)]
    hints = get_type_hints(SomeSegment, include_extras=True)

    n2 = base.X12ElementHelper.annotated(hints['n2_element'])
    assert n2.to_py("4200") == Decimal('42')
    assert n2.to_str(Decimal('42.00')) == "4200"

