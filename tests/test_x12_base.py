"""
Test x12/base
"""

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
    assert e.schema() == {
        'data_type_code': 'ID',
        'maxLength': 2,
        'minLength': 2,
        'title': 'I01',
        'type': 'string'
    }

def test_composite_padding():
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
    assert c.schema() == {
        'properties': {
            'se': {
                'data_type_code': 'ID',
                'maxLength': 2,
                'minLength': 2,
                'title': 'I01',
                'type': 'string'}},
        'title': 'Some Composite'
    }


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
            json = {"title": "Some Segment"}
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
    assert s.schema() == {
        'title': 'Some Segment', 'properties': {
            'e01': {'title': 'I01', 'type': 'string', 'data_type_code': 'ID', 'minLength': 2, 'maxLength': 2},
            'e02': {'title': 'I02', 'type': 'string', 'data_type_code': 'AN', 'minLength': 2, 'maxLength': 2}}
    }

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
    assert l.schema() == {
        'properties': {
            'some_segment': {
                'properties': {
                    'e01': {
                        'data_type_code': 'ID',
                        'maxLength': 2,
                        'minLength': 2,
                        'title': 'I01',
                        'type': 'string'}},
                'title': 'Some Segment'
            }
        },
        'title': 'Some Loop'
    }


def test_message_complete_1():
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
