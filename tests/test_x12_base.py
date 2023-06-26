"""
Test x12/base
"""
import datetime
from decimal import Decimal
from typing import Annotated, get_type_hints, TypeAlias

from pytest import fixture, CaptureFixture, mark, raises

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


def test_schema():
    class SomeSegment(base.Segment):
        """
        SomeSegment
        """
        a: Annotated[str, MinLen(1)]
        BItem: TypeAlias = Annotated[str, MinLen(2)]
        b: list[BItem, MaxItems(2)]
        c: Annotated[int, Title("c")] | None
        d: Annotated[float, Title("d")]
        e: Annotated[datetime.date, Title("e")]
        f: Annotated[datetime.time, Title("f")]
        g: Annotated[Decimal, Title("g"), Scale(2)]
    assert base.schema(SomeSegment) == {
        'class_name': 'SomeSegment',
        'description': 'SomeSegment',
        'properties': {
                    'a': {'minLength': 1, 'type': 'string'},
                    'b': {'items': {'minLength': 2, 'type': 'string'},
                          'maxItems': 2,
                          'type': 'array'},
                    'c': {'any': [{'title': 'c', 'type': 'integer'},
                                  {'type': 'null'}]},
                    'd': {'title': 'd', 'type': 'number'},
                    'e': {'convert': 'datetime.date',
                          'pyformat': '%Y%m%d',
                          'title': 'e',
                          'type': 'string'},
                    'f': {'convert': 'datetime.time',
                          'pyformat': '%h%m',
                          'title': 'f',
                          'type': 'string'},
                    'g': {'convert': 'Decimal',
                          'scale': '?',
                          'title': 'g',
                          'type': 'string',
                          'x-scale': 2}
        },
        'type': 'object'
    }


def test_composite_padding_annotations():
    class SomeComposite(base.Composite):
        se: Annotated[str, Title("Some Element"), MinLen(2), MaxLen(2)]
    class SomeSegment(base.Segment):
        c: SomeComposite
    class SomeLoop(base.Loop):
        s: SomeSegment
    class SomeMessage(base.Message):
        l: SomeLoop

    p = base.X12Parser(SomeMessage)
    c = p.composite_build(SomeComposite, ["01"])
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


def test_composite_build_2():
    class SomeComposite(base.Composite):
        se: Annotated[str, Title("Some Element"), MinLen(2), MaxLen(2)] | None
        be: int
    class SomeSegment(base.Segment):
        c: SomeComposite
    class SomeLoop(base.Loop):
        s: SomeSegment
    class SomeMessage(base.Message):
        l: SomeLoop

    p = base.X12Parser(SomeMessage)
    c = p.composite_build(SomeComposite, ["01", "42"])

    assert repr(c) == "SomeComposite(se='01', be=42)"
    assert c.se == "01"
    assert c.be == 42
    assert c.elements() == ['01', 42]
    assert base.asdict(c) == {'_kind': 'Composite', '_name': 'SomeComposite', 'se': '01', 'be': 42}

    assert base.schema(SomeComposite) == {
        'class_name': 'SomeComposite',
        'description': None,
        'properties': {
            'se': {
                'any': [
                    {'maxLength': 2,
                     'minLength': 2,
                     'title': 'Some Element',
                     'type': 'string'},
                    {'type': 'null'}
                ]
            },
            'be': {'type': 'integer'},
        },
        'type': 'object'
    }


def test_composite_validation():
    class SomeComposite(base.Composite):
        se: Annotated[str, Title("Some Element"), MinLen(2), MaxLen(2), Enumerated("WX", "YZ")]
    class SomeSegment(base.Segment):
        c: SomeComposite
    class SomeLoop(base.Loop):
        s: SomeSegment
    class SomeMessage(base.Message):
        l: SomeLoop

    p = base.X12Parser(SomeMessage)
    with raises(ValueError) as info:
        c = p.composite_build(SomeComposite, ["AB"])
    assert info.value.args == ("invalid SomeComposite.se: typing.Annotated[str, Title('Some Element'), "
         'MinLen(2), MaxLen(2), Enumerated(\'WX\', \'YZ\')] ("invalid value for '
         '\'AB\', not in (\'WX\', \'YZ\')", \'Enumerated\')',)

def test_composite_skipvalidation_ok():
    class SomeComposite(base.Composite):
        se: Annotated[str, Title("Some Element"), MinLen(2), MaxLen(2), Enumerated("WX", "YZ")]
    class SomeSegment(base.Segment):
        c: SomeComposite
    class SomeLoop(base.Loop):
        s: SomeSegment
    class SomeMessage(base.Message):
        l: SomeLoop

    p = base.X12Parser(SomeMessage, skip_validation=["SomeSegment:se:Enumerated"])
    c = p.composite_build(SomeComposite, ["AB"])
    assert c.se == "AB"

def test_composite_skipvalidation_notok():
    class SomeComposite(base.Composite):
        se: Annotated[str, Title("Some Element"), MinLen(2), MaxLen(2), Enumerated("WX", "YZ")]
    class SomeSegment(base.Segment):
        c: SomeComposite
    class SomeLoop(base.Loop):
        s: SomeSegment
    class SomeMessage(base.Message):
        l: SomeLoop

    p = base.X12Parser(SomeMessage, skip_validation=["SomeSegment:se:MinLen"])
    with raises(ValueError) as info:
        c = p.composite_build(SomeComposite, ["AB"])
    assert info.value.args == ("invalid SomeComposite.se: typing.Annotated[str, Title('Some Element'), "
         'MinLen(2), MaxLen(2), Enumerated(\'WX\', \'YZ\')] ("invalid value for '
         '\'AB\', not in (\'WX\', \'YZ\')", \'Enumerated\')',)

def test_segment_annotated():
    # Given
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
        e02: Annotated[str, Title("I02"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="AN")]
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("SS|01|02|:~", element_sep="|", array_sep=":", segment_sep="~")
    # When
    # s = SomeSegment.parse(src)
    p = base.X12Parser(SomeMsg)
    s = p.segment_parse(SomeSegment, src)
    # Then
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

def test_segment_validation():
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
        e02: Annotated[str, Title("I02"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="AN")]
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("SS|01tooLong|x|:~", element_sep="|", array_sep=":", segment_sep="~")

    # SomeSegment.configure([])
    p = base.X12Parser(SomeMsg)
    with raises(ValueError) as info:
        # s = SomeSegment.parse(src)
        s = p.segment_parse(SomeSegment, src)
    assert info.value.args == ("invalid SomeSegment.e01: typing.Annotated[str, Title('I01'), MinLen(2), "
         'MaxLen(2), OtherMeta(data_type_code=\'ID\')] ("invalid length for '
         '\'01tooLong\', greater than than 2", \'MaxLen\')',)


def test_segment_skipvalidation_ok():
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
        e02: Annotated[str, Title("I02"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="AN")]
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("SS|01tooLong|x|:~", element_sep="|", array_sep=":", segment_sep="~")
    skip_validation = ["SomeSegment:e01:MaxLen", "SomeSegment:e02:MinLen"]

    # SomeSegment.configure(skip_validation)
    p = base.X12Parser(SomeMsg, skip_validation)
    # s = SomeSegment.parse(src)
    s = p.segment_parse(SomeSegment, src)

    assert s.e01 == "01tooLong"
    assert s.e02 == "x"

def test_segment_skipvalidation_notok():
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
        e02: Annotated[str, Title("I02"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="AN")]
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("SS|01tooLong|x|:~", element_sep="|", array_sep=":", segment_sep="~")
    skip_validation = ["SomeSegment:e01:Enumerated", "SomeSegment:e02:Enumerated"]

    # SomeSegment.configure(skip_validation)
    p = base.X12Parser(SomeMsg, skip_validation)
    with raises(ValueError) as info:
        # s = SomeSegment.parse(src)
        s = p.segment_parse(SomeSegment, src)
    assert info.value.args == ("invalid SomeSegment.e01: typing.Annotated[str, Title('I01'), MinLen(2), "
         'MaxLen(2), OtherMeta(data_type_code=\'ID\')] ("invalid length for '
         '\'01tooLong\', greater than than 2", \'MaxLen\')',)


def test_segment_make_helpers_annotated():
    class SomeComposite(base.Composite):
        c01: Annotated[int, Title("C01")]
        c02: Annotated[int, Title("C02")]

    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")] | None
        e08: Annotated[datetime.date, Title("I08"), MinLen(6), MaxLen(6), OtherMeta(data_type_code="DT")]
        e16: Annotated[Decimal, Scale(0), Title("I16"), MinLen(1), MaxLen(6), OtherMeta(data_type_code="N0")]
        SomeItem: TypeAlias = Annotated[str, Title("Repeating")]
        e99: Annotated[list[SomeItem], MaxItems(2)]
        e98: int
        e97: SomeComposite
        e96: list[int]
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop

    # SomeSegment.configure([])
    p = base.X12Parser(SomeMsg)

    assert list(SomeSegment._helpers.keys()) == ['e01', 'e08', 'e16', 'e99', 'e98', 'e97', 'e96']

def test_segment_attr_build_union():
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")] | None
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("SS|01~", element_sep="|", array_sep=":", segment_sep="~")

    # SomeSegment.configure([])
    p = base.X12Parser(SomeMsg)

    # s = SomeSegment.parse(src)
    s = p.segment_parse(SomeSegment, src)
    assert s.e01 == "01"


def test_segment_attr_build_union_empty():
    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")] | None
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop

    # SomeSegment.configure([])
    p = base.X12Parser(SomeMsg)

    # values = [
    #     SomeSegment.attr_build(field_type, [])
    #     for name, field_type in base.class_fields(SomeSegment)
    # ]
    values = [
        p.segment_attr_build(SomeSegment, name, field_type, [])
        for name, field_type in base.class_fields(SomeSegment)
    ]
    assert values == [None]

def test_segment_attr_build_composite():
    class SomeComposite(base.Composite):
        c01: Annotated[str, Title("C01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")] | None

    class SomeSegment(base.Segment):
        """
        Some Segment
        """
        _segment_name = "SS"
        comp: SomeComposite
        e02: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")] | None
    class SomeLoop(base.Loop):
        s01: SomeSegment
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("SS|01|02~", element_sep="|", array_sep=":", segment_sep="~")

    # SomeSegment.configure([])
    p = base.X12Parser(SomeMsg)

    # s = SomeSegment.parse(src)
    s = p.segment_parse(SomeSegment, src)
    assert s.e02 == "02"
    assert s.comp.c01 == "01"


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
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("SS|01|:~", element_sep="|", array_sep=":", segment_sep="~")

    p = base.X12Parser(SomeMsg)

    # l = SomeLoop.parse(src)
    l = p.loop_parse(SomeLoop, src)

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

def test_loop_attr_build_union():
    class OptSegment1(base.Segment):
        """Optional Segment"""
        _segment_name = "OS1"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
    class OptSegment2(base.Segment):
        """Another Optional Segment"""
        _segment_name = "OS2"
        e01: Annotated[str, Title("I01"), MinLen(2), MaxLen(2), OtherMeta(data_type_code="ID")]
    class SomeLoop(base.Loop):
        """Some Loop"""
        opt_seg_1: OptSegment1 | None
        opt_seg_2: Annotated[OptSegment2, Title("Opt2")] | None
    class SomeMsg(base.Message):
        l01: SomeLoop
    src = base.Source("OS1|01~\nOS2|02~\n", element_sep="|", segment_sep="~", array_sep="^")

    p = base.X12Parser(SomeMsg)
    # SomeLoop.configure([])

    assert OptSegment1._helpers
    assert OptSegment2._helpers
    # loop = SomeLoop.parse(source)
    l = p.loop_parse(SomeLoop, src)
    assert l.opt_seg_1
    assert l.opt_seg_2
    assert list(l.segment_iter()) ==  [['OS1', '01'], ['OS2', '02']]

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
        another_loop: AnotherLoop | None

    src = base.Source("SS|01~\nAS|02~\n", element_sep="|", array_sep=":", segment_sep="~")
    p = base.X12Parser(TheMessage)
    # m = TheMessage.parse(src)
    m = p.parse(src)
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
                'any': [
                    {
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
                         'type': 'object'
                    },
                    {"type": "null"}
                ]
            },
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
