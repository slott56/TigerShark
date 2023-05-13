import datetime
from decimal import Decimal
from unittest.mock import sentinel, Mock, call

from pytest import fixture

from x12 import base

def test_type_factory_defined():
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2

    gen_type = base.type_factory(Schema)
    assert isinstance(gen_type, base.IDType)
    assert gen_type.min_len == 2
    assert gen_type.scale == 0

def test_type_factory_undefined():
    class Schema:
        pass

    str_type = base.type_factory(Schema)
    assert isinstance(str_type, base.ANType)
    assert str_type.min_len is None
    assert str_type.scale == 0

    assert str_type.to_py("42") == "42"
    assert str_type.to_str(42) == "42"

def test_antype():
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2
    an = base.ANType(Schema.min_len)
    assert an.to_py("01") == "01"
    assert an.to_str('1') == "1 "
    assert an.to_str('1') == "1 "

def test_btype():
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2
    b = base.BType(Schema.min_len)
    assert b.to_py("01") == "01"
    assert b.to_str('1') == "1 "

def test_dttype():
    class Schema:
        datatype = {'type': 'string', 'format': '\\d\\d\\d\\d\\d\\d\\d\\d', 'title': 'I08', 'data_type_code': 'DT', 'minLength': 6, 'maxLength': 6}
        min_len = 8
        max_len = 8
    dt = base.DTType(Schema.min_len)
    assert dt.to_py("20230203") == datetime.date(2023, 2, 3)
    assert dt.to_str(datetime.date(2023, 2, 3)) == "20230203"

    assert dt.to_py(None) is None

def test_idtype():
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2
    id_obj = base.IDType(Schema.min_len)
    assert id_obj.to_py("1") == "1"
    assert id_obj.to_str(1) == "01"

def test_idtype_nominlen():
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID'}
        min_len = None
        max_len = None
    id_obj = base.IDType(Schema.min_len)
    assert id_obj.to_py("1") == "1"
    assert id_obj.to_str(1) == "1"


def test_rtype():
    class Schema:
        datatype = {'type': 'number', 'title': 'Rate', 'data_type_code': 'R', 'minLength': 1, 'maxLength': 9}
        min_len = 1
        max_len = 9
    r = base.RType(Schema.min_len)
    assert r.to_py("42") == 42.0
    assert r.to_str(42.0) == "42"

    assert r.to_py(None) is None

def test_rtype_nominlen():
    class Schema:
        datatype = {'type': 'number', 'title': 'Rate', 'data_type_code': 'R'}
        min_len = None
        max_len = None
    r = base.RType(Schema.min_len)
    assert r.to_py("42") == 42.0
    assert r.to_str(42.0) == "42"


def test_tmtype():
    class Schema:
        datatype = {'type': 'string', 'format': '\\d\\d\\d\\d', 'title': 'I09', 'data_type_code': 'TM', 'minLength': 4, 'maxLength': 4}
        min_len = 4
        max_len = 4
    tm = base.TMType(Schema.min_len)
    assert tm.to_py("1317") == datetime.time(13, 17)
    assert tm.to_str(datetime.time(13, 17)) == "1317"

    assert tm.to_py(None) is None

def test_ntype():
    e = Mock(name="mock Element", source="42")
    class Schema:
        datatype = {'type': 'number', 'title': 'I12', 'data_type_code': 'N', 'minLength': 9, 'maxLength': 9}
        min_len = 9
        max_len = 9
    dt = base.NType(Schema.min_len)
    assert dt.to_py(e.source) == Decimal('42')
    assert dt.to_str(42) == "000000042"

def test_ntype_nominlen():
    e = Mock(name="mock Element", source="42")
    class Schema:
        datatype = {'type': 'number', 'title': 'I12', 'data_type_code': 'N'}
        min_len = None
        max_len = None
    n = base.NType(Schema.min_len)
    assert n.to_py(e.source) == Decimal('42')
    assert n.to_str(42) == "42"

    assert n.to_py(None) is None


def test_n0type():
    e = Mock(name="mock Element", source="42", value=Decimal('42'))
    class Schema:
        datatype = {'type': 'number', 'scale': 0, 'title': 'I12', 'data_type_code': 'N0', 'minLength': 9, 'maxLength': 9}
        min_len = 9
        max_len = 9
    dt = base.NType(Schema.min_len)
    assert dt.to_py(e.source) == Decimal('42')
    assert dt.to_str(Decimal(42)) == "000000042"


def test_n2type():
    e = Mock(name="mock Element", source="4200")
    class Schema:
        datatype = {'type': 'number', 'scale': 2, 'title': 'Amount', 'data_type_code': 'N2', 'minLength': 1, 'maxLength': 15}
        min_len = 1
        max_len = 15
    dt = base.NType(Schema.min_len, scale=Schema.datatype.get('scale', 0))
    assert dt.to_py(e.source) == Decimal('42')
    assert dt.to_str(Decimal('42.00')) == "4200"
