"""
Test x12/base
"""
import datetime
from decimal import Decimal
from typing import Annotated

from pytest import fixture, CaptureFixture, mark

from x12 import base
from x12.annotations import *

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


def test_composite_padding_annotations():
    class SomeComposite(base.Composite):
        se: Annotated[str, Title("Some Element"), MinLen(2), MaxLen(2)]

    c = SomeComposite.build(["01"])
    assert repr(c) == "SomeComposite(se='01')"
    assert c.se == "01"
    assert c.elements() == ['01']
    assert base.asdict(c) == {'_kind': 'Composite', '_name': 'SomeComposite', 'se': '01'}

    assert base.schema(SomeComposite) == {
        'class_name': 'SomeComposite',
        'description': None,
        'properties': {
            'se': {
                'maxLength': 2,
                'minLength': 2,
                'title': 'Some Element',
                'type': 'string'}
            },
        'type': 'object'
    }


def test_segment_annotated():
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
        e02: Annotated[str, Title("I02"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="AN")]

    src = base.Source("SS|01|02|:~", element_sep="|", array_sep=":", segment_sep="~")
    s = SomeSegment.parse(src)
    assert s.e01 == "01"
    assert s.e02 == "02"
    assert s.elements() == ['01', '02']
    assert repr(s) == "SomeSegment(e01='01', e02='02')"
    assert base.asdict(s) == {'_kind': 'Segment', '_name': 'SomeSegment', 'e01': '01', 'e02': '02'}

    assert base.schema(SomeSegment) == {
        'class_name': 'SomeSegment',
        'description': 'Some Segment',
        'type': 'object',
        'properties': {
            'e01': {'title': 'I01', 'type': 'string', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2},
            'e02': {'title': 'I02', 'type': 'string', 'data_type_code': 'AN', 'minLength': 2, 'maxLength': 2}
        }
    }

def test_segment_schema_annotated():
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")] | None
        e08: Annotated[datetime.date, Title("I08"), MinLen(6), MaxLen(6), OtherMeta(data_type_code="DT")]
        e16: Annotated[Decimal, Scale(0), Title("I16"), MinLen(1), MaxLen(6), OtherMeta(data_type_code="N0")]

    assert base.schema(SomeSegment) == {
        'class_name': 'SomeSegment',
        'description': 'Some Segment',
        'type': 'object',
        'properties': {
            'e01': {
                'any': [
                    {
                        'data_type_code': 'ID',
                        'maxLength': 2,
                         'minLength': 2,
                         'title': 'I01',
                         'type': 'string'
                    },
                    {'type': 'null'}
                ]
            },
            'e08': {'convert': 'datetime.date',
                    'data_type_code': 'DT',
                    'maxLength': 6,
                    'minLength': 6,
                    'pyformat': '%Y%m%d',
                    'title': 'I08',
                    'type': 'string'},
            'e16': {'convert': 'Decimal',
                    'data_type_code': 'N0',
                    'maxLength': 6,
                    'minLength': 1,
                    'scale': '?',
                    'title': 'I16',
                    'type': 'string',
                    'x-scale': 0}
        }
    }


def test_loop_annotated():
    class SomeSegment(base.Segment):
        """Some Segment"""
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
    class SomeLoop(base.Loop):
        """Some Loop"""
        some_segment: SomeSegment

    src = base.Source("SS|01|:~", element_sep="|", array_sep=":", segment_sep="~")
    l = SomeLoop.parse(src)
    assert l.some_segment.e01 == "01"
    assert list(l.segment_iter()) == [['SS', '01'], ]
    assert repr(l) == "SomeLoop(some_segment=SomeSegment(e01='01'))"
    assert base.asdict(l) ==  {'_kind': 'Loop', '_name': 'SomeLoop', 'some_segment': {'_kind': 'Segment', '_name': 'SomeSegment', 'e01': '01'}}

    assert base.schema(SomeLoop) == {
        'class_name': 'SomeLoop',
        'description': 'Some Loop',
        'properties': {
            'some_segment': {
                'class_name': 'SomeSegment',
                'description': 'Some Segment',
                'properties': {
                    'e01': {
                        'data_type_code': 'ID',
                        'maxLength': 2,
                        'minLength': 2,
                        'title': 'I01',
                        'type': 'string'}
                },
                'type': 'object'}
        },
        'type': 'object'
    }

def test_message_annotated_1():
    class SomeSegment(base.Segment):
        """Some Segment"""
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
    class SomeLoop(base.Loop):
        """Some Loop"""
        some_segment: SomeSegment
    class AnotherSegment(base.Segment):
        """Another Segment"""
        _segment_name = "AS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
    class AnotherLoop(base.Loop):
        """Another Loop"""
        another_segment: AnotherSegment
    class TheMessage(base.Message):
        """The Message"""
        some_loop: list[SomeLoop]
        another_loop: AnotherLoop

    src = base.Source("SS|01~\nAS|02~\n", element_sep="|", array_sep=":", segment_sep="~")
    m = TheMessage.parse(src)
    assert m
    assert m.some_loop[0].some_segment.e01 == "01"
    assert list(m.segment_iter()) == [['SS', '01'], ['AS', '02']]
    assert repr(m) == "TheMessage(some_loop=[SomeLoop(some_segment=SomeSegment(e01='01'))], another_loop=AnotherLoop(another_segment=AnotherSegment(e01='02')))"
    assert base.asdict(m) == {
        '_kind': 'Message',
        '_name': 'TheMessage',
        'another_loop': {'_kind': 'Loop',
                      '_name': 'AnotherLoop',
                      'another_segment': {'_kind': 'Segment',
                                       '_name': 'AnotherSegment',
                                       'e01': '02'}},
        'some_loop': [{'_kind': 'Loop',
                    '_name': 'SomeLoop',
                    'some_segment': {'_kind': 'Segment',
                                     '_name': 'SomeSegment',
                                     'e01': '01'}}]}
    assert m.json() == '{"_kind": "Message", "_name": "TheMessage", "some_loop": [{"_kind": "Loop", "_name": "SomeLoop", "some_segment": {"_kind": "Segment", "_name": "SomeSegment", "e01": "01"}}], "another_loop": {"_kind": "Loop", "_name": "AnotherLoop", "another_segment": {"_kind": "Segment", "_name": "AnotherSegment", "e01": "02"}}}'

    assert base.schema(TheMessage) == {
        'class_name': 'TheMessage',
        'description': "The Message",
        'properties': {
            'another_loop': {
                'class_name': 'AnotherLoop',
                 'description': "Another Loop",
                 'properties': {
                     'another_segment': {
                         'class_name': 'AnotherSegment',
                         'description': "Another Segment",
                         'properties': {
                             'e01': {
                                 'data_type_code': 'ID',
                                'maxLength': 2,
                                'minLength': 2,
                                'title': 'I01',
                                'type': 'string'}
                         },
                         'type': 'object'}
                 },
                 'type': 'object'},
            'some_loop': {
                'items': {
                    'class_name': 'SomeLoop',
                    'description': "Some Loop",
                    'properties': {
                        'some_segment': {
                            'class_name': 'SomeSegment',
                            'description': "Some Segment",
                            'properties': {
                                'e01': {
                                    'data_type_code': 'ID',
                                   'maxLength': 2,
                                   'minLength': 2,
                                   'title': 'I01',
                                   'type': 'string'}},
                            'type': 'object'}},
                    'type': 'object'},
                'type': 'array'}
        },
        'type': 'object'
    }

def test_demo(capsys: CaptureFixture) -> None:
    """An integration test for many features of the base module."""
    base.demo()
    output, _ = capsys.readouterr()
    assert output.splitlines() == [
        "MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01='00', isa16=':'))])",
        "MSG(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01='00', isa16=':'))])",
    ]
