"""
Test tools/xml

..  todo:: See below in test_xml_convert -- use a visitor to examine the AST.
"""
import ast
from io import StringIO
from unittest.mock import sentinel, Mock, call

from pytest import fixture, CaptureFixture

from tools import xml_extract


def test_codeset() -> None:
    c = xml_extract.Codeset(sentinel.ID, sentinel.DATA_ELE, sentinel.SOURCE, [sentinel.VALUE])
    assert c.label == sentinel.ID
    assert c.jsonschema() == [sentinel.VALUE]

@fixture
def mock_codes_xml() -> StringIO:
    mock_doc = StringIO("""<?xml version="1.0" encoding="UTF-8"?>
    <codesets xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <codeset>
        <id>states</id>
        <name>US State or Province Codes</name>
        <data_ele>156</data_ele>
        <version>
          <code>NC</code>
        </version>
      </codeset>
    </codesets>
    """)
    return mock_doc

def test_code_reader(mock_codes_xml: StringIO) -> None:
    codes = list(xml_extract.code_reader(mock_codes_xml))
    assert len(codes) == 1
    assert codes[0].id == "states"
    assert codes[0].data_ele == "156"
    assert codes[0].values == ["NC"]

def test_dataelement() -> None:
    d = xml_extract.DataElement(sentinel.ELE_NUM, "AN", "3", "5", sentinel.NAME)
    assert d.jsonschema() == {
        "title": sentinel.NAME,
        "type": "string",
        "data_type_code": "AN",
        "minLength": 3,
        "maxLength": 5,
    }

@fixture
def mock_elements_xml() -> StringIO:
    mock_doc = StringIO("""<?xml version="1.0" encoding="UTF-8"?>
    <data_elements>
    <data_ele ele_num="I01" data_type="ID" min_len="2" max_len="2" name="I01"/>
    </data_elements>
    """)
    return mock_doc

def test_element_reader(mock_elements_xml: StringIO) -> None:
    elements = list(xml_extract.element_reader(mock_elements_xml))
    assert len(elements) == 1
    assert elements[0].ele_num == "I01"
    assert elements[0].data_type == "ID"
    assert elements[0].min_len == "2"
    assert elements[0].min_len == "2"
    assert elements[0].name == "I01"

def test_schemamap() -> None:
    s = xml_extract.SchemaMap(sentinel.ICVN, sentinel.VRIIC, sentinel.FIC, sentinel.ABBR, sentinel.DEFINITION)
    assert s.icvn == sentinel.ICVN
    assert s.vriic == sentinel.VRIIC
    assert s.fic == sentinel.FIC
    assert s.abbr == sentinel.ABBR
    assert s.definition == sentinel.DEFINITION

@fixture
def mock_mapping() -> str:
    mock_doc = StringIO("""<?xml version="1.0" encoding="UTF-8"?>
    <maps>
      <version icvn="00400">
        <map vriic="004010" fic="PS" abbr="830">830.4010.PS.xml</map>
      </version>
    </maps>
    """)
    return mock_doc

def test_map_reader(mock_mapping) -> None:
    maps = list(xml_extract.map_reader(mock_mapping))
    assert len(maps) == 1
    assert maps[0].icvn == "00400"
    assert maps[0].vriic == "004010"
    assert maps[0].fic == "PS"
    assert maps[0].abbr == "830"
    assert maps[0].definition == "830.4010.PS.xml"

def test_pythonify() -> None:
    assert xml_extract.pythonify("ISA", "X") == "ISA"
    assert xml_extract.pythonify("ISA01-02", "X") == "ISA01_02"
    assert xml_extract.pythonify("ISA01.02", "X") == "ISA01_02"
    assert xml_extract.pythonify("123", "D") == "D123"

def test_element() -> None:
    e = xml_extract.Element(
        xid="XID-E.1",
        data_ele=sentinel.DATA_ELE,
        name=sentinel.NAME,
        usage=sentinel.USAGE,
        seq="42",
        refdes=sentinel.REFDES,
        repeat="1",
        codes=[sentinel.CODES],
        external=sentinel.EXTERNAL,
        common_def=sentinel.COMMON_DEF,
        loop=sentinel.LOOP
    )
    assert e.attr_name == "XID_E_1".lower()
    assert e.class_name == "sentinel.LOOP_XID_E_1"
    assert e.jsonschema() == {
        'items': {
            'description': 'xid=XID-E.1 data_ele=sentinel.DATA_ELE',
            'sequence': 42,
            'title': sentinel.NAME,
            'type': {'allOf': [{'$ref': '#/$common/sentinel.COMMON_DEF'},
                              {'enum': [sentinel.CODES]}]},
            'usage': sentinel.USAGE},
         'maxItems': 1,
         'type': 'array'} != {'description': 'xid=XID-E.1 data_ele=sentinel.DATA_ELE',
         'maxItems': 1,
         'sequence': 42,
         'title': sentinel.NAME,
         'type': 'array',
         'usage': sentinel.USAGE}

def test_composite() -> None:
    e = Mock(
            name="mock element",
            attr_name=sentinel.ELEMENT,
            usage="R",
            jsonschema=Mock(return_value={"schema": None})
    )
    c = xml_extract.Composite(
        xid="XID-C.1",
        data_ele=sentinel.DATA_ELE,
        name=sentinel.NAME,
        usage=sentinel.USAGE,
        seq="42",
        refdes=sentinel.REFDES,
        syntax=[sentinel.SYNTAX],
        repeat="1",
        elements=[e],
        loop=sentinel.LOOP
    )
    assert c.attr_name == "XID_C_1".lower()
    assert c.class_name == "sentinel.LOOP_XID_C_1"
    assert c.required
    assert c.jsonschema() == {
        'items': {
            'description': 'xid=XID-C.1 name=sentinel.NAME refdes=sentinel.REFDES data_ele=sentinel.DATA_ELE',
            'properties': {sentinel.ELEMENT: {"schema": None}},
            'required': [sentinel.ELEMENT],
            'sequence': 42,
            'syntax': [sentinel.SYNTAX],
            'title': sentinel.NAME,
            'type': 'object',
            'usage': sentinel.USAGE},
        'maxItems': 1,
        'type': 'array'}


def test_segment() -> None:
    e = Mock(
        name="mock element",
        attr_name=sentinel.ELEMENT,
        usage="R",
        jsonschema=Mock(return_value={"schema": None}),
        class_name="Element"
    )
    c = Mock(
        name="mock composite",
        attr_name=sentinel.COMPOSITE,
        usage="R",
        jsonschema=Mock(return_value={"schema": None}),
        class_name = "Composite"
    )

    s = xml_extract.Segment(
        xid="XID-S.1",
        name=sentinel.NAME,
        end_tag=sentinel.END_TAG,
        usage=sentinel.USAGE,
        pos="42",
        max_use=">1",
        syntax=[sentinel.SYNTAX],
        children=[c, e],
        loop=sentinel.LOOP
    )
    assert s.attr_name == "XID_S_1".lower()
    assert s.class_name == "sentinel.LOOP_XID_S_1"
    assert s.required == [sentinel.COMPOSITE, sentinel.ELEMENT]
    assert s.repeat
    assert s.jsonschema() == {
        'items': {'description': 'xid=XID-S.1 name=sentinel.NAME',
            'endTag': sentinel.END_TAG,
            'position': 42,
            'properties': {'xid': {'literal': 'XID-S.1'},
                          sentinel.COMPOSITE: {'$ref': '#/$elements/Composite'},
                          sentinel.ELEMENT: {'$ref': '#/$elements/Element'}},
            'required': [sentinel.COMPOSITE, sentinel.ELEMENT],
            'syntax': [sentinel.SYNTAX],
            'title': sentinel.NAME,
            'type': 'object',
            'usage': sentinel.USAGE},
        'type': 'array'}

def test_loop() -> None:
    s = Mock(
        name="mock segmnent",
        attr_name=sentinel.SEGMENT,
        usage="R",
        jsonschema=Mock(return_value={"schema": None}),
        class_name = "Segment"
    )
    l = xml_extract.Loop(
        xid="XID-L.1",
        name=sentinel.NAME,
        usage=sentinel.USAGE,
        pos="42",
        repeat="1",
        type=sentinel.TYPE,
        children=[s],
    )
    assert l.attr_name == "XID_L_1".lower()
    assert l.class_name == "XID_L_1"
    assert l.required == [sentinel.SEGMENT]
    assert l.repeat
    assert l.jsonschema() == {
        'items': {'description': 'xid=XID-L.1 name=sentinel.NAME type=sentinel.TYPE',
               'position': 42,
               'properties': {sentinel.SEGMENT: {'$ref': '#/$segments/Segment'}},
               'required': [sentinel.SEGMENT],
               'title': sentinel.NAME,
               'type': 'object',
               'usage': sentinel.USAGE},
        'maxItems': 1,
        'type': 'array'}

def test_message() -> None:
    m = xml_extract.Message(
        xid="999",
        name=sentinel.NAME,
        loops=[Mock(name="mock loop", usage="R", attr_name=sentinel.LOOP, class_name=sentinel.LOOP_CLASS)]
    )

    assert m.class_name == "MSG999"
    assert m.required == [sentinel.LOOP]
    assert m.jsonschema() == {
        'description': 'xid=999 name=sentinel.NAME',
        'properties': {sentinel.LOOP: {'$ref': "#/$loops/sentinel.LOOP_CLASS"}},
        'required': [sentinel.LOOP],
        'title': sentinel.NAME,
        'type': 'object'}

@fixture
def mock_message_xml() -> str:
    mock_doc = StringIO("""<?xml version="1.0" encoding="UTF-8"?>
    <transaction xid="999">
        <name>Test Case 999</name>
        <loop xid="ISA_LOOP" type="explicit">
            <name>Interchange Control Header</name>
            <usage>R</usage>
            <pos>001</pos>
            <repeat>&gt;1</repeat>
            <segment xid="ISA">
              <name>Interchange Control Header</name>
              <usage>R</usage>
              <pos>010</pos>
              <max_use>1</max_use>
              <element xid="ISA01">
                <data_ele>I01</data_ele>
                <name>Authorization Information Qualifier</name>
                <usage>R</usage>
                <seq>01</seq>
                <valid_codes>
                  <code>00</code>
                  <code>03</code>
                </valid_codes>
              </element>
          </segment>
        </loop>
    </transaction>
    """)
    return mock_doc


def test_message_reader(mock_message_xml) -> None:
    m = xml_extract.message_reader(mock_message_xml)
    assert m.xid == "999"
    assert m.name == "Test Case 999"
    assert len(m.loops) == 1

    loop = m.loops[0]
    assert loop.xid == "ISA_LOOP"
    assert loop.name == "Interchange Control Header"
    assert loop.usage == "R"
    assert loop.pos == "001"
    assert loop.repeat == ">1"
    assert len(loop.children) == 1

    segment = loop.children[0]
    assert segment.xid == "ISA"
    assert segment.name == "Interchange Control Header"
    assert segment.usage == "R"
    assert segment.pos == "010"
    assert segment.max_use == "1"
    assert len(segment.children) == 1

    element = segment.children[0]
    assert element.xid == "ISA01"
    assert element.data_ele == "I01"
    assert element.name == "Authorization Information Qualifier"
    assert element.usage == "R"
    assert element.seq == "01"
    assert element.common_def == "I01"
    assert element.codes == ["00", "03"]

@fixture
def mock_message() -> xml_extract.Message:
    e = xml_extract.Element(
        xid="ISA01",
        data_ele="I01",
        name="Authorization Information Qualifier",
        usage="R",
        seq="01",
        refdes="",
        repeat="",
        codes=["00", "03"],
        external="",
        common_def="I01",
        loop="ISA_LOOP"
    )
    s = xml_extract.Segment(
        xid="ISA",
        name="Interchange Control Header",
        end_tag="IEA",
        usage="R",
        pos="010",
        max_use="1",
        syntax=[],
        children=[e],
        loop="ISA_LOOP"
    )
    l = xml_extract.Loop(
        xid="ISA_LOOP",
        name="ISA LOOP",
        usage="R",
        pos="001",
        repeat=">1",
        type="explicit",
        children=[s]
    )
    m = xml_extract.Message(
        xid="999",
        name="Test Case 999",
        loops = [l]
    )
    return m


def test_emit_python(mock_message: xml_extract.Message, capsys: CaptureFixture) -> None:
    data_elements = {"I01": Mock(name="Mock DataElement", min_len=2, max_len=2)}
    codes = {}
    ep = xml_extract.EmitPython().data_elements(data_elements).codesets(codes)
    ep.visit(mock_message)
    python_source, _ = capsys.readouterr()

    # Assert the code is valid
    module = ast.parse(python_source, filename="__test__", mode="exec")

    class ClassVisitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.names = []
        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            # print(node.body)
            # TODO: Visit the body. They're all very similar.
            # optional ast.Expr (the docstring)
            # internal ast.ClassDef (name == "Schema")
            # the fields are the remaining ast.AnnAssign statments
            self.names.append(node.name)

    # Check the structure of the code
    cv = ClassVisitor()
    cv.visit(module)
    assert cv.names == ['ISA_LOOP_ISA01', 'ISA_LOOP_ISA', 'ISA_LOOP', 'MSG999']

