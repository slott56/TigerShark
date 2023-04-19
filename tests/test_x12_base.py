"""
Test x12/base
"""
import datetime
from decimal import Decimal
from unittest.mock import sentinel, Mock, call

from pytest import fixture, CaptureFixture

from x12 import base

def test_source_typical():
    s = base.Source("\r\rISA|00|01|02|:~   \r  SEG|03|04|05~\r")
    assert s.peek(3) == "ISA"
    s.element_sep = "|"
    s.array_sep = ":"
    s.segment_sep = "~"
    assert s.next_segment() == "ISA"
    assert s.elements() == ["ISA", "00", "01", "02", ":"]
    assert s.peek(3) == "SEG"
    assert s.next_segment() == "SEG"
    assert s.elements() == ["SEG", "03", "04", "05"]

def test_source_edge():
    """A typical use without peeking."""
    s = base.Source("\n\n\nISA|00|01|02|:~   \n  SEG|03|04|05~\n\n", element_sep = "|", segment_sep = "~")
    assert s.elements() == ["ISA", "00", "01", "02", ":"]
    assert repr(s) == "self.element_sep='|' self.segment_sep='~' text='\\n\\n\\nISA|00|01|02|:~' && '   \\n  SEG|03|04|05~\\n\\n'"

def test_type_factory_defined():
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2

    dt = base.type_factory(Schema)
    assert isinstance(dt, base.IDType)
    assert dt.min_len == 2
    assert dt.scale is None

def test_type_factory_undefined():
    class Schema:
        pass

    dt = base.type_factory(Schema)
    assert isinstance(dt, base.ANType)
    assert dt.min_len is None
    assert dt.scale is None

    e = Mock(name="mock Element", source="42")
    class Schema:
        datatype = {'type': 'string', 'title': 'I01'}

    assert dt.to_py(e) == "42"
    assert dt.to_str(42) == "42"

def test_antype():
    e = Mock(name="mock Element", source="01")
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2
    dt = base.ANType(Schema.min_len)
    assert dt.to_py(e) == "01"
    assert dt.to_str('1') == "1 "

def test_btype():
    e = Mock(name="mock Element", source="01")
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2
    dt = base.BType(Schema.min_len)
    assert dt.to_py(e) == "01"
    assert dt.to_str('1') == "1 "

def test_dttype():
    e = Mock(name="mock Element", source="20230203")
    class Schema:
        datatype = {'type': 'string', 'format': '\\d\\d\\d\\d\\d\\d\\d\\d', 'title': 'I08', 'data_type_code': 'DT', 'minLength': 6, 'maxLength': 6}
        min_len = 6
        max_len = 6
    dt = base.DTType(Schema.min_len)
    assert dt.to_py(e) == datetime.date(2023, 2, 3)
    assert dt.to_str(datetime.date(2023, 2, 3)) == "20230203"

def test_idtype():
    e = Mock(name="mock Element", source="1")
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
        min_len = 2
        max_len = 2
    dt = base.IDType(Schema.min_len)
    assert dt.to_py(e) == "1"
    assert dt.to_str(1) == "01"

def test_idtype_nominlen():
    e = Mock(name="mock Element", source="1")
    class Schema:
        datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID'}
        min_len = None
        max_len = None
    dt = base.IDType(Schema.min_len)
    assert dt.to_py(e) == "1"
    assert dt.to_str(1) == "1"


def test_rtype():
    e = Mock(name="mock Element", source="42")
    class Schema:
        datatype = {'type': 'number', 'title': 'Rate', 'data_type_code': 'R', 'minLength': 1, 'maxLength': 9}
        min_len = 1
        max_len = 9
    dt = base.RType(Schema.min_len)
    assert dt.to_py(e) == 42.0
    assert dt.to_str(42.0) == "42.000000"

def test_rtype_nominlen():
    e = Mock(name="mock Element", source="42")
    class Schema:
        datatype = {'type': 'number', 'title': 'Rate', 'data_type_code': 'R'}
        min_len = None
        max_len = None
    dt = base.RType(Schema.min_len)
    assert dt.to_py(e) == 42.0
    assert dt.to_str(42.0) == "42.0"


def test_tmtype():
    e = Mock(name="mock Element", source="1317")
    class Schema:
        datatype = {'type': 'string', 'format': '\\d\\d\\d\\d', 'title': 'I09', 'data_type_code': 'TM', 'minLength': 4, 'maxLength': 4}
        min_len = 4
        max_len = 4
    dt = base.TMType(Schema.min_len)
    assert dt.to_py(e) == datetime.time(13, 17)
    assert dt.to_str(datetime.time(13, 17)) == "1317"

def test_ntype():
    e = Mock(name="mock Element", source="42")
    class Schema:
        datatype = {'type': 'number', 'title': 'I12', 'data_type_code': 'N', 'minLength': 9, 'maxLength': 9}
        min_len = 9
        max_len = 9
    dt = base.NType(Schema.min_len)
    assert dt.to_py(e) == Decimal('42')
    assert dt.to_str(42) == "000000042"

def test_ntype_nominlen():
    e = Mock(name="mock Element", source="42")
    class Schema:
        datatype = {'type': 'number', 'title': 'I12', 'data_type_code': 'N'}
        min_len = None
        max_len = None
    dt = base.NType(Schema.min_len)
    assert dt.to_py(e) == Decimal('42')
    assert dt.to_str(42) == "42"


def test_n0type():
    e = Mock(name="mock Element", source="42", value=Decimal('42'))
    class Schema:
        datatype = {'type': 'number', 'scale': 0, 'title': 'I12', 'data_type_code': 'N0', 'minLength': 9, 'maxLength': 9}
        min_len = 9
        max_len = 9
    dt = base.NType(Schema.min_len)
    assert dt.to_py(e) == Decimal('42')
    assert dt.to_str(Decimal(42)) == "000000042"


def test_n2type():
    e = Mock(name="mock Element", source="4200")
    class Schema:
        datatype = {'type': 'number', 'scale': 2, 'title': 'Amount', 'data_type_code': 'N2', 'minLength': 1, 'maxLength': 15}
        min_len = 1
        max_len = 15
    dt = base.NType(Schema.min_len, scale=Schema.datatype.get('scale', 0))
    assert dt.to_py(e) == Decimal('42')
    assert dt.to_str(Decimal('42.00')) == "4200"


def test_element():
    class SomeElement(base.Element):
        class Schema:
            datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
            min_len = 2
            max_len = 2

    e = SomeElement.build("01")
    assert e.source == "01"
    assert e.value == "01"
    assert repr(e) == "SomeElement('01')"
    e.value = "02"
    assert repr(e) == "SomeElement('02')"
    assert e.asdict() == '02'

def test_composite():
    # We *should* provide a Mock instead of an actual Element instance.
    class SomeElement(base.Element):
        class Schema:
            json = {"title": "Some Element"}
            datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
            min_len = 2
            max_len = 2

    class SomeComposite(base.Composite):
        class Schema:
            json = {"title": "Some Composite"}
        se: SomeElement

    c = SomeComposite.build(["01"])
    assert repr(c) == "SomeComposite(se=SomeElement('01'))"
    assert c.se.source == "01"
    assert c.se.value == "01"
    assert c.source == ["01"]
    assert c.asdict() == {'_kind': 'Composite', '_name': 'SomeComposite', 'se': '01'}


def test_segment():
    # We *should* provide Mocks instead of an actual Element instances.
    class OneElement(base.Element):
        class Schema:
            json = {"title": "Some Element"}
            datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
            min_len = 2
            max_len = 2
    class AnotherElement(base.Element):
        class Schema:
            json = {"title": "Some Element"}
            datatype = {'type': 'string', 'title': 'I02', 'data_type_code': 'AN', 'minLength': 2, 'maxLength': 2}
            min_len = 2
            max_len = 2
    class SomeSegment(base.Segment):
        class Schema:
            json = {"Title": "Some Segment"}
            segment_name = "SS"
        e01: OneElement
        e02: AnotherElement

    src = base.Source("SS|01|02|:~", element_sep="|", array_sep=":", segment_sep="~")
    s = SomeSegment.parse(src)
    assert s.e01.source == "01"
    assert s.e02.source == "02"
    assert s.elements() == ['01', '02']
    assert repr(s) == "SomeSegment(e01=OneElement('01'), e02=AnotherElement('02'))"
    assert s.asdict() == {'_kind': 'Segment', '_name': 'SomeSegment', 'e01': '01', 'e02': '02'}

def test_loop():
    # We *should* provide Mocks instead of an actual Element and Segment instances.
    class OneElement(base.Element):
        class Schema:
            json = {"title": "Some Element"}
            datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
            min_len = 2
            max_len = 2
    class SomeSegment(base.Segment):
        class Schema:
            json = {"title": "Some Segment"}
            segment_name = "SS"
        e01: OneElement
    class SomeLoop(base.Loop):
        class Schema:
            json = {"title": "Some Loop"}
        some_segment: SomeSegment

    src = base.Source("SS|01|:~", element_sep="|", array_sep=":", segment_sep="~")
    l = SomeLoop.parse(src)
    assert l.some_segment.e01.source == "01"
    assert list(l.segment_iter()) == [['SS', '01'], ]
    assert repr(l) == "SomeLoop(some_segment=SomeSegment(e01=OneElement('01')))"
    assert l.asdict() ==  {'_kind': 'Loop', '_name': 'SomeLoop', 'some_segment': {'_kind': 'Segment', '_name': 'SomeSegment', 'e01': '01'}}


def test_message():
    # We *should* provide Mocks instead of an actual Element, Segment, and Loop instances.
    class OneElement(base.Element):
        class Schema:
            json = {"title": "Some Element"}
            datatype = {'type': 'string', 'title': 'I01', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2}
            min_len = 2
            max_len = 2
    class SomeSegment(base.Segment):
        class Schema:
            json = {"title": "Some Segment"}
            segment_name = "SS"
        e01: OneElement
    class SomeLoop(base.Loop):
        class Schema:
            json = {"title": "Some Loop"}
        some_segment: SomeSegment
    class AnotherSegment(base.Segment):
        class Schema:
            json = {"title": "Another Segment"}
            segment_name = "AS"
        e01: OneElement
    class AnotherLoop(base.Loop):
        class Schema:
            json = {"title": "Another Loop"}
        some_segment: AnotherSegment
    class TheMessage(base.Message):
        class Schema:
            json = {"title": "The Message"}
        some_loop: list[SomeLoop]
        another_loop: AnotherLoop

    src = base.Source("SS|01~\nAS|02~\n", element_sep="|", array_sep=":", segment_sep="~")
    m = TheMessage.parse(src)
    assert m
    assert m.some_loop[0].some_segment.e01.source == "01"
    assert list(m.segment_iter()) == [['SS', '01'], ['AS', '02']]
    assert repr(m) == "TheMessage(some_loop=[SomeLoop(some_segment=SomeSegment(e01=OneElement('01')))], another_loop=AnotherLoop(some_segment=AnotherSegment(e01=OneElement('02'))))"
    assert m.asdict() == {
        '_kind': 'Message',
        '_name': 'TheMessage',
        'another_loop': {'_kind': 'Loop',
                      '_name': 'AnotherLoop',
                      'some_segment': {'_kind': 'Segment',
                                       '_name': 'AnotherSegment',
                                       'e01': '02'}},
        'some_loop': [{'_kind': 'Loop',
                    '_name': 'SomeLoop',
                    'some_segment': {'_kind': 'Segment',
                                     '_name': 'SomeSegment',
                                     'e01': '01'}}]}
    assert m.json() == '{"_kind": "Message", "_name": "TheMessage", "some_loop": [{"_kind": "Loop", "_name": "SomeLoop", "some_segment": {"_kind": "Segment", "_name": "SomeSegment", "e01": "01"}}], "another_loop": {"_kind": "Loop", "_name": "AnotherLoop", "some_segment": {"_kind": "Segment", "_name": "AnotherSegment", "e01": "02"}}}'
    assert m.schema() == {
        'properties': {'another_loop': {'properties': {'some_segment': {'properties': {'e01': {'data_type_code': 'ID',
                                                                                                'maxLength': 2,
                                                                                                'minLength': 2,
                                                                                                'title': 'I01',
                                                                                                'type': 'string'}},
                                                                         'title': 'Another '
                                                                                  'Segment'}},
                                         'title': 'Another Loop'},
                        'some_loop': {'properties': {'some_segment': {'properties': {'e01': {'data_type_code': 'ID',
                                                                                             'maxLength': 2,
                                                                                             'minLength': 2,
                                                                                             'title': 'I01',
                                                                                             'type': 'string'}},
                                                                      'title': 'Some '
                                                                               'Segment'}},
                                      'title': 'Some Loop'}},
         'title': 'The Message'
    }

def test_demo(capsys: CaptureFixture) -> None:
    """More of an integration test."""
    base.demo()
    output, _ = capsys.readouterr()
    assert output.splitlines() == [
        "MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01=ISA_LOOP_ISA01('00'), isa16=ISA_LOOP_ISA16(':')))])",
        "MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01=ISA_LOOP_ISA01('00'), isa16=ISA_LOOP_ISA16(':')))])",
    ]
