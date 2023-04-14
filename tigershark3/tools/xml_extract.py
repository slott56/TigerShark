"""
Read the schema from the PYx12 project's XML-based schema definitions.

See https://github.com/azoner/pyx12

See https://github.com/azoner/pyx12/tree/master/pyx12/map for the message definitions.

This application extracts the Element, Composite, Segment, Loop, and Message schemas from these definitions.

The idea is to create two useful documents:

- A JSONSchema definition as a common structure to describe the EDI messages.

- This package's X12 modules with class definitions for each message based on an ``x12.base`` module's
  parent classes.

Source
=======

Several sources of data are integrated to create the full schema.

1. The nnn.nnnn.xnnnn...xml files. Example 270.4010.X092.A1.xml. These have the message definitions.

2. The codes.xml, detaele.xml with additional data to support the data type definitions.

3. The x12.control.00401.xml and x12.control.00501.xml with core structural information
   used to map a message to the specific message definition.

It's not perfectly clear that maps.xml is *required*, but it seems useful for creating
a declarative set of X12 messages.

The complication here is that within a given message definition,
the Element, Segment, Loop, Message structure is unique, but the names are reused.
This means the message -- as a whole -- is a kind of namespace around the structural elements.

The class definitions here are *only* used to extract the XML-based schema information.
They're not related in any way to processing X12 EDI messages.

X12 Schema
==========

The X12 schema definitions created here depend on an ``x12.base`` module to provide
the superclass definitions of Element, Composite, Segment, Loop, and Message.

This app writes a collection of message-specific modules
with subclass definitions for all of the elements, etc., that are part of that message.
Reuse is not considered at this point.
In many cases, the Control segments (ISA, IEA, GS, GE, etc.) are reusable,
and should not be repeated in each module.

Structure and Naming
=====================

Names of Segments and Elements are reused extensively.
The Loop is the context in which Segment, Composite, and Element names are understood.

The idea of exposing the Segments as if they are dataclass-like records
is made challenging by way Segments are reused in distinct Loops.

The overall "mapping" from source text to message is a separate capability
This uses generic x12.control.* module generic definitions to locate the correct module to process a message.

Type Definitions
=================

The Data Element definitions, used to create Elements, are heavily reused.
These become a module of Schema details used to build the final schema
for a given Element.

The Code definitions, similarly, are part of the module of schema details.
These are incorporated explicitly into the JSON Schema.

The "$ref" path will be "#/$common/some_code" or "#/$common/some_element_schema".
This parallels the Python ``x12.common`` module which has these definitions.

The idea is the "$common" section is part of each message's overall JSONSchema definition.
It could be replace with an external reference using a full URI, which might be more
sensible in the long run.

These are generally ``"type": {"$ref": "#/$common/some_element_schema"}`` constructs.

X12 Message Version Mapping
===========================

The base mapping superclass permits a subclass to provide a rule
for disambiguating messages.

A mapping search class uses the collection of mapping objects
to locate the module that can parse a message.

.. todo:: This version identification is not implemented

"""
from collections import deque
from collections.abc import Iterator
from contextlib import redirect_stdout
from dataclasses import dataclass, asdict, field
import datetime
import logging
from pathlib import Path
from pprint import pprint, pformat
import sys
from textwrap import indent
from typing import Union, TypeAlias, Any, TextIO, Self
from xml.etree import ElementTree as XML


logger = logging.getLogger("xml_extract")

optional_text = lambda tag, name: (
    sub_tag.text if (sub_tag := tag.find(name)) is not None else ""
)


@dataclass
class Codeset:
    """
    An enumerated set of values used to define an Element.

    A JSONSchema {"type": "string", "enum": []} schema
    """
    id: str
    data_ele: str
    source: str
    values: list[str]

    @property
    def label(self):
        return self.id

    def jsonschema(self) -> dict[str, Any]:
        return self.values


def code_reader(source: TextIO) -> Iterator[Codeset]:
    """
    See https://github.com/azoner/pyx12/blob/master/pyx12/map/codes.rng

    The RelaxNG schema doesn't exactly match the XML.

    The schema is approximately this
    ::

        schema:
            description: codesets
            type: array
            items:
                description: codeset
                type: object
                properties:
                    id:
                        type: string
                        maxLength: 20
                    name:
                        type: string
                        maxLength: 100
                    data_ele:
                        type: string
                        maxLength: 6
                    source:
                        type: string
                    version:
                        type: array
                        items:
                            description: version
                            type: object
                            properties:
                                id:
                                    type: string
                                    maxLength: 20
                                eff_dte:
                                    type: stringh
                                code:
                                    type: array
                                    items:
                                        type: str
                                        maxLength: 6
    """
    document = XML.parse(source)
    codesets = document.getroot()
    for codeset_tag in codesets.findall('codeset'):
        id = codeset_tag.find('id').text
        data_ele = optional_text(codeset_tag, 'data_ele')
        source = optional_text(codeset_tag, 'source')
        version_tag = codeset_tag.find('version')
        values = [
            code.text for code in version_tag.findall('code')
        ]
        codeset = Codeset(
            id=id,
            data_ele=data_ele,
            source=source,
            values=values
        )
        logger.debug(codeset)
        yield codeset


X12_TYPE_SCHEMA = {
    "AN": {"type": "string"},
    "B": {"type": "string"},  # Binary?
    "DT": {"type": "string", "format": "\d\d\d\d\d\d\d\d"},
    "ID": {"type": "string"}, # Identifier, numeric string.
    "R": {"type": "number"},  # Real
    "TM": {"type": "string", "format": "\d\d\d\d"},
    "N": {"type": "number"},  # Number
    "N0": {"type": "number", "scale": 0}, # 0 decimal places, i.e. integer.
    "N1": {"type": "number", "scale": 1},
    "N2": {"type": "number", "scale": 2}, # 2 decimal places, i.e. currency.
    "N3": {"type": "number", "scale": 3},
    "N4": {"type": "number", "scale": 4},
    "N5": {"type": "number", "scale": 5},
    "N6": {"type": "number", "scale": 6},
    "N7": {"type": "number", "scale": 7},
    "N8": {"type": "number", "scale": 8},
    "N9": {"type": "number", "scale": 9},
}


@dataclass
class DataElement:
    """
    A data element description, often reused by multiple Elements.

    A JSONSchema {"type": ..., "minLength": ..., "maxLength": ..., "description": ...} schema
    """
    ele_num: str
    data_type: str
    min_len: str | None
    max_len: str | None
    name: str

    def jsonschema(self) -> dict[str, Any]:
        schema: dict[str, Any] = X12_TYPE_SCHEMA[self.data_type]
        schema |= {
            "title": self.name,
            "data_type_code": self.data_type,
        }
        if self.min_len is not None:
            schema["minLength"] = int(self.min_len)
        if self.max_len is not None:
            schema["maxLength"] = int(self.max_len)
        return schema


def element_reader(source: TextIO) -> Iterator[DataElement]:
    """
    See https://github.com/azoner/pyx12/blob/master/pyx12/map/codes.rng

    The RelaxNG schema seems to match the XML.
    Note that the schema is all attributes, not actual tags.

    The schema is approximately this
    ::

        description: data_elements
        type: array
        items:
            description: data_ele
            type: object
            properties:
                ele_num:
                    type: string
                    max-length: 4
                data_type:
                    type: string
                    enum: ["AN", "B", "DT", "ID", "R", "TM", "N", "N0", "N1", "N2",  "N3", "N4", "N5",  "N6", "N7", "N8",
                    "N9"]
                min_len:
                    type: number
                    maximum: 16384
                max_len:
                    type: number
                    maximum: 16384
                name:
                    type: string
    """
    document = XML.parse(source)
    data_elements = document.getroot()
    for data_ele_tag in data_elements.findall('data_ele'):
        ele_num = data_ele_tag.attrib.get('ele_num', '')
        data_type = data_ele_tag.attrib.get('data_type', '')
        min_len = data_ele_tag.attrib.get('min_len', '')
        max_len = data_ele_tag.attrib.get('max_len', '')
        name = data_ele_tag.attrib.get('name', '')
        assert data_type in ["AN", "B", "DT", "ID", "R", "TM", "N", "N0", "N1", "N2",  "N3", "N4", "N5",  "N6", "N7", "N8", "N9"]
        data_ele = DataElement(
            ele_num=ele_num,
            data_type=data_type,
            min_len=min_len,
            max_len=max_len,
            name=name
        )
        logger.debug(data_ele)
        yield data_ele


@dataclass
class SchemaMap:
    """
    Rules for mapping a given message to a specific versioned type.
    """
    icvn: str  # Interchange Control Version Number (ISA12)
    vriic: str  # Version / Release / Industry Identifier Code (GS08)
    fic: str  # Functional Identifier Code (GS01)
    abbr: str
    definition: str


def map_reader(source: TextIO) -> Iterator[SchemaMap]:
    """
    Mapping of document to schema version.

    See https://github.com/azoner/pyx12/blob/master/pyx12/map/maps.xsd

    Attributes used to distinguish the document schema

    - icvn - Interchange Control Version Number (ISA12)
    - fic - Functional Identifier Code (GS01)
    - vriic - Version / Release / Industry Identifier Code (GS08)
    """
    document = XML.parse(source)
    maps_tag = document.getroot()
    for version_tag in maps_tag.findall("version"):
        icvn = version_tag.attrib.get("icvn")
        for map_tag in version_tag.findall("map"):
            vriic = map_tag.attrib.get("vriic")
            fic = map_tag.attrib.get("fic")
            abbr = map_tag.attrib.get("abbr")
            definition = map_tag.text
            map = SchemaMap(
                icvn=icvn,
                vriic=vriic,
                fic=fic,
                abbr=abbr,
                definition=definition
            )
            logger.info(map)
            yield map


def pythonify(x12_name: str, prefix="_") -> str:
    revised = x12_name.replace("-", "_").replace(".", "_")
    if revised[0] in "0123456789":
        revised = prefix + revised
    return revised


@dataclass
class Element:
    """
    Atomic Element.

    A JSONSchema property value: "name": {"type": ..., etc.} piece of a Segment or Composite

    Yes, codes are locally defined codes, where code_set is an imported set of codes.
    They're both the same JSONSchema enum attribute.

    Usage="R" (required) percolates up to the containing Composite or Segment.
    """
    xid: str
    data_ele: str
    name: str
    usage: str
    seq: str
    refdes: str  # Not used
    repeat: str
    codes: list[str]
    external: str
    common_def: str  # DataElement or Codeset identifier
    loop: str  # Containing Loop to make a class name unique

    @property
    def attr_name(self) -> str:
        return pythonify(self.xid, "E").lower()

    @property
    def class_name(self) -> None:
        return f"{self.loop}_{pythonify(self.xid, 'E')}"

    def jsonschema(self) -> dict[str, Any]:
        schema: dict[str, Any] = {
            "title": self.name,
            "usage": self.usage,  # Required, Situational, Not-Used
            "description": f"xid={self.xid} data_ele={self.data_ele}",
            "sequence": int(self.seq),
        }
        # Can have both common type def & locally-defined codes.
        # This is a "allOf" merge between {$ref: common_def} type and {"enum": ...} for codes.
        if self.codes and not self.common_def:
            schema["type"] = "string"
            schema["enum"] = self.codes
        elif self.common_def and not self.codes:
            schema["type"] = {"$ref": f"#/$common/{self.common_def}"}
        elif self.common_def and (self.codes or self.external):
            schema["type"] = {
                "allOf": [
                    {"$ref": f"#/$common/{self.common_def}"},
                    {"enum": self.codes or f"#/$codes/{self.external}"}
                ]
            }
        else:
            raise RuntimeError(f"no type information in {self}")
        if self.repeat:
            schema = {
                "type": "array",
                "items": schema,
                "maxItems": int(self.repeat)
            }
        return schema

@dataclass
class Composite:
    """
    Composite of multiple Elements; an inline segment-like collection of Elements.

    A JSONSchema {"type": "object": "properties": {...}} schema

    From a JSONSchema perspective, a composite isn't flattened into a sequence
    of attributes of the containing Segment.
    The composite is described as if it's a sub-segment.
    """
    xid: str
    data_ele: str
    name: str
    usage: str  # Required, Situational, Not-Used
    seq: str
    refdes: str  # When used, this seems to be the proper XID
    syntax: list[str]
    repeat: str
    elements: list[Element]
    loop: str  # Containing Loop to make a class name unique

    @property
    def attr_name(self) -> str:
        return pythonify(self.xid or self.refdes or self.data_ele, "C").lower()

    @property
    def class_name(self) -> None:
        return f"{self.loop}_{pythonify(self.xid or self.refdes or self.data_ele, 'C')}"

    @property
    def required(self):
        return [elt.attr_name for elt in self.elements if elt.usage == "R"]

    def jsonschema(self) -> dict[str, Any]:
        schema = {
            "title": self.name,
            "usage": self.usage,  # Required, Situational, Not-Used
            "description": f"xid={self.xid} name={self.name} refdes={self.refdes} data_ele={self.data_ele}",
            "sequence": int(self.seq),
            "syntax": self.syntax,
        }
        if self.elements:
            schema["type"] = "object"
            schema["properties"] = {
                elt.attr_name: elt.jsonschema()
                for elt in self.elements
            }
        if req := self.required:
            schema["required"] = req
        if self.repeat:
            schema = {
                "type": "array",
                "items": schema,
                "maxItems": int(self.repeat)
            }
        return schema

@dataclass
class Segment:
    """
    A collection of Elements and Composites.

    A JSONSchema {"type": "object": "properties": {...}} schema
    """
    xid: str
    name: str
    end_tag: str  # Used rarely
    usage: str  # Required, Situational, Not-Used
    pos: str
    max_use: str
    syntax: list[str]
    children: list[Element | Composite]
    loop: str  # Containing Loop to make a class name unique

    @property
    def attr_name(self) -> str:
        return pythonify(self.xid, "S").lower()

    @property
    def class_name(self) -> None:
        return f"{self.loop}_{pythonify(self.xid, 'S')}"

    @property
    def required(self) -> bool:
        return [elt.attr_name for elt in self.children if elt.usage == "R"]

    @property
    def repeat(self) -> bool:
        return self.max_use and self.max_use != "1"

    def jsonschema(self) -> dict[str, Any]:
        schema = {
            "title": self.name,
            "usage": self.usage,  # Required, Situational, Not-Used
            "description": f"xid={self.xid} name={self.name}",
            "position": int(self.pos),
        }
        if self.syntax:
            schema["syntax"] = self.syntax
        if self.end_tag:
            schema["endTag"] = self.end_tag
        if self.children:
            schema["type"] = "object"
            schema["properties"] = {"xid": {"literal": self.xid}}
            for elt in self.children:
                if elt.usage == "N":
                    continue
                schema["properties"][elt.attr_name] = {"$ref": f"#/$elements/{elt.class_name}"}  # elt.jsonschema()
        if req := self.required:
            schema["required"] = req
        if self.max_use and self.max_use != "1":
            schema = {
                "type": "array",
                "items": schema,
            }
            if self.max_use != ">1":
                schema['maxItems'] = int(self.max_use)
        return schema

@dataclass
class Loop:
    """
    A higher-level collection of Loops and Segments.

    A JSONSchema {"type": "object": "properties": {...}} schema
    """
    xid: str
    name: str
    usage: str  # Required, Situational, Not-Used
    pos: str
    repeat: str
    type: str
    children: list[Union[Segment, "Loop"]]

    @property
    def attr_name(self):
        return pythonify(self.xid, "L").lower()

    @property
    def class_name(self):
        return pythonify(self.xid, "L")

    @property
    def required(self):
        return [elt.attr_name for elt in self.children if elt.usage == "R"]

    def jsonschema(self) -> dict[str, Any]:
        schema = {
            "title": self.name,
            "usage": self.usage,  # Required, Situational, Not-Used
            "description": f"xid={self.xid} name={self.name} type={self.type}",
            "position": int(self.pos),
        }
        if self.children:
            schema["type"] = "object"
            schema["properties"] = {
                elt.attr_name: {"$ref": f"#/$segments/{elt.class_name}"}  # elt.jsonschema()
                for elt in self.children
                if elt.usage != "N"
            }
        if req := self.required:
            schema["required"] = req
        if self.repeat:
            schema = {
                "type": "array",
                "items": schema,
            }
            if self.repeat != ">1":
                schema['maxItems'] = int(self.repeat)
        return schema

@dataclass
class Message:
    """
    A Complete Message.
    """
    xid: str
    name: str
    loops: list[Loop]

    @property
    def class_name(self):
        return pythonify(self.xid, "MSG")

    @property
    def required(self):
        return [elt.attr_name for elt in self.loops if elt.usage == "R"]

    def jsonschema(self) -> dict[str, Any]:
        schema = {
            "title": self.name,
            "description": f"xid={self.xid} name={self.name}",
        }
        if self.loops:
            schema["type"] = "object"
            schema["properties"] = {
                elt.attr_name: {"$ref": f"#/$loops/{elt.class_name}"}  # elt.jsonschema()
                for elt in self.loops
                if elt.usage != "N"
            }
        if req := self.required:
            schema["required"] = req
        return schema


def message_reader(source: TextIO) -> Message:
    """
    See https://github.com/azoner/pyx12/blob/master/pyx12/map/map.xsd

    Note that the common (control) messages use a lot of named elements.
    The other messages use a lot of attributes.
    Hence the duplication.

    The summary of the schema is as follows:

    ::

        transaction (xid)
            name
            loop

        loop (xid, pos, usage, repeat, type)
            name
            usage
            pos
            repeat
            segment | loop

        segment (xid, usage, pos, max_use)
            name
            end_tag
            usage
            pos
            max_use
            syntax
            element | composite

        composite (xid, data_ele, usage, seq)
            data_ele
            name
            usage
            seq
            refdes
            syntax
            repeat
            element

        element (xid, data_ele, name, usage, seq)
            data_ele
            name
            usage
            seq
            refdes
            repeat
            valid_codes (external)
                code

    format: one of D8 (yyyymmdd), D6 (yymmdd), RD8 (yyyymmdd-yyyymmdd), TM (hhmm)  Not sure where this is used.

    usage: one of R (required), S (situational), N (not used)

    syntax: uses a string with the following structure ``(E|L|P|C|R)([0-9]{2}){2,20}``

        E - Exclusion - Not more than one specified element may be present

        L - List - If first is present, at least one other must be present

        P - Paired or Multiple - If any element specified is present, all must be present

        C - Conditional - If first is present, all others must be present

        R - Required - At least one must be present

        Followed by two-digit numbers to list elements to which this syntax applies.
    """
    def element_walker(loop_context: str, base_tag: XML.Element) -> Element:
        xid_a = base_tag.attrib.get("xid")
        data_ele_a = base_tag.attrib.get("data_ele")
        usage_a = base_tag.attrib.get("usage")
        seq_a = base_tag.attrib.get("seq")
        data_ele = optional_text(base_tag, "data_ele")
        name = optional_text(base_tag, "name")
        usage = optional_text(base_tag, "usage")  # See usageType
        seq = optional_text(base_tag, "seq")
        refdes = optional_text(base_tag, "refdes")
        repeat = optional_text(base_tag, "repeat")
        if (valid_codes_tag := base_tag.find("valid_codes")) is not None:
            codes = [c.text for c in valid_codes_tag.findall("code")]
            external = valid_codes_tag.attrib.get("external")
        else:
            codes = []
            external = ""
        element_id = data_ele_a or data_ele
        # data_element = data_elements.get(element_id, None)
        # code_set = codesets.get(element_id, None)
        element = Element(
            xid=xid_a,
            data_ele=element_id,
            name=name,
            usage=usage_a or usage,
            seq=seq_a or seq,
            refdes=refdes,
            repeat=repeat,
            codes=codes,
            external=external,
            common_def=element_id,
            loop=loop_context
        )
        logger.debug(element)
        return element

    def composite_walker(loop_context: str, base_tag: XML.Element) -> Composite:
        xid_a = base_tag.attrib.get("xid")
        data_ele_a = base_tag.attrib.get("data_ele")
        usage_a = base_tag.attrib.get("usage")
        seq_a = base_tag.attrib.get("seq")
        data_ele = optional_text(base_tag, "data_ele")
        name = optional_text(base_tag, "name")
        usage = optional_text(base_tag, "usage")  # See usageType
        seq = optional_text(base_tag, "seq")
        refdes = optional_text(base_tag, "refdes")
        syntax = [t.text for t in base_tag.findall("syntax")]  # See syntaxType rules
        repeat = optional_text(base_tag, "repeat")
        elements = [
            element_walker(loop_context, element)
            for element in base_tag.findall("element")
        ]
        composite = Composite(
            xid=xid_a,
            data_ele=data_ele_a or data_ele,
            name=name,
            usage=usage_a or usage,
            seq=seq_a or seq,
            refdes=refdes,
            syntax=syntax,
            repeat=repeat,
            elements=elements,
            loop=loop_context
        )
        logger.debug(composite)
        return composite

    def segment_walker(loop_context: str, base_tag: XML.Element):
        xid_a = base_tag.attrib.get("xid")
        pos_a = base_tag.attrib.get("pos")
        usage_a = base_tag.attrib.get("usage")
        max_use_a = base_tag.attrib.get("max_use")
        name = optional_text(base_tag, "name")
        end_tag = optional_text(base_tag, "end_tag")
        usage = optional_text(base_tag, "usage")
        pos = optional_text(base_tag, "pos")
        max_use = optional_text(base_tag, "max_use")
        syntax = [t.text for t in base_tag.findall("syntax")]  # See syntaxType rules
        # Any number of element or composite may follow...
        children = []
        for child_tag in base_tag.findall("*"):
            if child_tag.tag == "element":
                c = element_walker(loop_context, child_tag)
                children.append(c)
            elif child_tag.tag == "composite":
                c = composite_walker(loop_context, child_tag)
                children.append(c)
            elif child_tag.tag in {"name", "end_tag", "usage", "pos", "max_use", "syntax"}:
                pass  # Skip already processed tags
            else:
                raise RuntimeError(f"Unexpected {child_tag.tag}")
        segment = Segment(
            xid=xid_a,
            name=name,
            end_tag=end_tag,
            usage=usage_a or usage,
            pos=pos_a or pos,
            max_use=max_use_a or max_use,
            syntax=syntax,
            children=children,
            loop=loop_context
        )
        logger.debug(segment)
        return segment

    def loop_walker(base_tag: XML.Element) -> Loop:
        xid_a = base_tag.attrib.get("xid")
        pos_a = base_tag.attrib.get("pos")
        usage_a = base_tag.attrib.get("usage")
        repeat_a = base_tag.attrib.get("repeat")
        type_a = base_tag.attrib.get("type")  # Actually used, doesn't seem appropriate at this level.
        name = optional_text(base_tag, "name")
        usage = optional_text(base_tag, "usage")
        pos = optional_text(base_tag, "pos")
        repeat = optional_text(base_tag, "repeat")
        # Any number of loop OR segment may follow...
        children = []
        for child_tag in base_tag.findall("*"):
            if child_tag.tag == "loop":
                c = loop_walker(child_tag)
                children.append(c)
            elif child_tag.tag == "segment":
                c = segment_walker(pythonify(xid_a, "L"), child_tag)
                children.append(c)
            elif child_tag.tag in {"name", "usage", "pos", "repeat"}:
                pass  # Skip already processed tags
            else:
                raise RuntimeError(f"Unexpected {child_tag.tag}")
        # TODO: DRY issue. The segment_walker (above) is given the class_name value from the Loop class (below).
        loop = Loop(
            xid=xid_a,
            name=name,
            usage=usage_a or usage,
            pos=pos_a or pos,
            repeat=repeat_a or repeat,
            type=type_a,
            children=children,
        )
        logger.debug(loop)
        return loop

    document = XML.parse(source)
    transaction_tag = document.getroot()
    xid = transaction_tag.attrib.get("xid")
    name = transaction_tag.find("name").text
    loops = [
        loop_walker(loop_tag)
        for loop_tag in transaction_tag.findall("loop")
    ]
    message = Message(
        xid=xid,
        name=name,
        loops=loops
    )
    return message


Component: TypeAlias = Union[Element, Composite, Segment, Loop, Message]


class MessageVisitor:
    """
    Abstract Visitor for all layers of a message, in Post-Order traversal.

    This works UP the message structure from elements to composites, segments, loops,
    and finally the containing message.
    """
    def __init__(self) -> None:
        self.source_name = ""
        self.path = deque()

    def visit(self, component: Component) -> None:
        match component:
            case Element():
                self.element(component)
            case Composite():
                self.path.append(("COMPOSITE", component.class_name))
                for element in component.elements:
                    self.visit(element)
                self.path.pop()
                self.composite(component)
            case Segment():
                self.path.append(("SEGMENT", component.class_name))
                for child in component.children:
                    self.visit(child)
                self.path.pop()
                self.segment(component)
            case Loop():
                self.path.append(("LOOP", component.class_name))
                for child in component.children:
                    self.visit(child)
                self.path.pop()
                self.loop(component)
            case Message():
                self.path = [("MESSAGE", component.class_name)]
                for loop in component.loops:
                    self.visit(loop)
                self.path.pop()
                self.message(component)
            case _:
                raise RuntimeError(f"unexpected {component!r}")

    def element(self, element: Element) -> None:
        pass

    def composite(self, composite: Composite) -> None:
        pass

    def segment(self, segment: Segment) -> None:
        pass

    def loop(self, loop: Loop) -> None:
        pass

    def message(self, message: Message) -> None:
        pass


class EmitPython(MessageVisitor):
    """
    Message visitor to emit Pythonic definitions for
    Elements, Composites, Segments, Loops, and Messages.

    These will be extension subclasses to definitions in ``x12.base``.
    """
    def __init__(self) -> None:
        super().__init__()
        self.codes: dict[str, Codeset]
        self.types: dict[str, DataElement]

    def codesets(self, c: dict[str, Codeset]) -> Self:
        self.codes = c
        return self

    def data_elements(self, d: dict[str, DataElement]) -> Self:
        self.types = d
        return self

    def element(self, element: Element) -> None:
        print("\n")
        print(f'class {element.class_name}(Element):\n    """{element.name}"""')
        print(f'    class Schema:')
        print(f"        json = {indent(pformat(element.jsonschema(), compact=True, sort_dicts=False), 8*' ').lstrip()}")
        if element.common_def:
            print(f"        datatype = common.{pythonify(element.common_def, 'D_')}")
        if element.external:
            print(f"        codes = common.{pythonify(element.external, 'D_')}")
        if element.codes:
            print(f"        codes = {element.codes}")
        # Size -- mostly for ISA segment, which is fixed length, ignoring the separators.
        if element.data_ele in self.types:
            if self.types[element.data_ele].min_len:
                print(f"        min_len = {int(self.types[element.common_def].min_len)}")
            if self.types[element.data_ele].max_len:
                print(f"        max_len = {int(self.types[element.common_def].max_len)}")
        else:
            logger.warning("no data_element for %s", element)


    def composite(self, composite: Composite) -> None:
        print("\n")
        # print(f"# {self.path}")
        print(f'class {composite.class_name}(Composite):')
        print(f'    class Schema:')
        print(f"        json = {indent(pformat(composite.jsonschema(), compact=True, sort_dicts=False), 8*' ').lstrip()}")
        for elt in composite.elements:
            if elt.usage == "N":
                continue
            if elt.repeat:
                type_text = f"list[{elt.class_name}]"
            else:
                type_text = elt.class_name
            if elt.attr_name not in composite.required:
                type_text = f"{type_text} | None"
            print(f"    {elt.attr_name}: {type_text}")

    def segment(self, segment: Segment) -> None:
        print("\n")
        # print(f"# {self.path}")
        print(f'class {segment.class_name}(Segment):\n    """{segment.name}"""')
        print(f'    class Schema:')
        print(f"        json = {indent(pformat(segment.jsonschema(), compact=True, sort_dicts=False), 8*' ').lstrip()}")
        print(f"        segment_name = {segment.xid!r}")
        for elt in segment.children:
            if elt.usage == "N":
                continue
            if elt.repeat:
                type_text = f"list[{elt.class_name}]"
            else:
                type_text = elt.class_name
            if elt.attr_name not in segment.required:
                type_text = f"{type_text} | None"
            print(f"    {elt.attr_name}: {type_text}")

    def loop(self, loop: Loop) -> None:
        print("\n")
        # print(f"# {self.path}")
        print(f'class {loop.class_name}(Loop):')
        print(f'    class Schema:')
        print(f"        json = {indent(pformat(loop.jsonschema(), compact=True, sort_dicts=False), 8*' ').lstrip()}")
        for elt in loop.children:
            if elt.usage == "N":
                continue
            if elt.repeat:
                type_text = f"list[{elt.class_name}]"
            else:
                type_text = elt.class_name
            if elt.attr_name not in loop.required:
                type_text = f"{type_text} | None"
            print(f"    {elt.attr_name}: {type_text}")

    def message(self, message: Message) -> None:
        print("\n")
        print(f'class {message.class_name}(Message):\n    """{message.name}"""')
        print(f'    class Schema:')
        print(f"        json = {indent(pformat(message.jsonschema(), compact=True, sort_dicts=False), 8*' ').lstrip()}")
        for elt in message.loops:
            if elt.usage == "N":
                continue
            if elt.repeat:
                type_text = f"list[{elt.class_name}]"
            else:
                type_text = elt.class_name
            if elt.attr_name not in message.required:
                type_text = f"{type_text} | None"
            print(f"    {elt.attr_name}: {type_text}")


def make_common_module(
        codesets: dict[str, Codeset],
        data_elements: dict[str, DataElement],
        target_package: Path
) -> None:
    target_path = (target_package / "common").with_suffix(".py")
    with target_path.open('w') as target_file:
        with redirect_stdout(target_file):
            print('"""')
            print(f"Created {datetime.datetime.now()}")
            print('"""')
            print()
            for id in codesets:
                print(f"{pythonify(id, 'C_')} = {codesets[id].jsonschema()}")
            for name in data_elements:
                print(f"{pythonify(name, 'D_')} = {data_elements[name].jsonschema()}")

def make_message_module(
        codesets: dict[str, Codeset],
        data_elements: dict[str, DataElement],
        source_path: Path,
        target_package: Path
) -> None:
    target_stem = f'msg_{source_path.stem.replace(".", "_")}'
    target_path = (target_package / target_stem).with_suffix(".py")
    logger.info("%s -> %s", source_path.name, target_path.name)

    code_writer = EmitPython().data_elements(data_elements).codesets(codesets)
    code_writer.source_name = source_path.stem
    with source_path.open() as source:
        msg = message_reader(source)
    with target_path.open('w') as target_file:
        with redirect_stdout(target_file):
            print('"""')
            print(source_path.stem)
            print(f"Created {datetime.datetime.now()}")
            # print(msg)
            print('"""')
            print("from .base import *\nfrom . import common")
            code_writer.visit(msg)


def make_python(base: Path, target: Path) -> None:
    """
    Extract from XML schema, creating Python (with some JSON Schema).

    Each message becomes a separate module in an overall "x12" package.
    """
    with (base / "codes.xml").open() as source:
        logger.info("Reading %s", source.name)
        codesets = {
            codeset.id: codeset
            for codeset in code_reader(source)
        }
    with (base / "dataele.xml").open() as source:
        logger.info("Reading %s", source.name)
        data_elements = {
            data_element.ele_num: data_element
            for data_element in element_reader(source)
        }
    make_common_module(codesets, data_elements, x12_package)

    for source_path in sorted(base.glob("x12.control.*.xml")):
        make_message_module(codesets, data_elements, source_path, x12_package)

    for source_path in sorted(base.glob("[0-9][0-9][0-9]*.xml")):
        make_message_module(codesets, data_elements, source_path, x12_package)

    with (base / "maps.xml").open() as source:
        maps = list(map_reader(source))
    # TODO: Emit the mapping objects.


def make_message_schema(
        codesets: dict[str, Codeset],
        data_elements: dict[str, DataElement],
        source_path: Path,
        target_package: Path
) -> None:
    target_stem = f'msg_{source_path.stem.replace(".", "_")}'
    target_path = (target_package / target_stem).with_suffix(".json")
    logger.info("%s -> %s", source_path.name, target_path.name)
    with source_path.open() as source:
        msg = message_reader(source)
    print(msg.jsonschema())


def make_jsonschema(base: Path, target: Path) -> None:
    """
    Extract from XML schema, creating JSON Schema.

    Each message becomes a separate .json document.
    """
    with (base / "codes.xml").open() as source:
        logger.info("Reading %s", source.name)
        codesets = {
            codeset.id: codeset
            for codeset in code_reader(source)
        }
    with (base / "dataele.xml").open() as source:
        logger.info("Reading %s", source.name)
        data_elements = {
            data_element.ele_num: data_element
            for data_element in element_reader(source)
        }
    for source_path in sorted(base.glob("x12.control.*.xml")):
        make_message_schema(codesets, data_elements, source_path, x12_package)

    for source_path in sorted(base.glob("[0-9][0-9][0-9]*.xml")):
        make_message_schema(codesets, data_elements, source_path, x12_package)


def main(base: Path, x12_package: Path | None, json_dir: Path | None) -> None:
    """
    Extract from XML schema.
    Make Python or Make JSONSchema.
    """
    logger.info("Source %s", base)
    if x12_package:
        logger.info("Creating %s", x12_package)
        make_python(base, x12_package)
    if json_dir:
        logger.info("Creating %s", json_dir)
        make_jsonschema(base, json_dir)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    base = Path.home() / "github" / "pyx12" / "pyx12" / "map"
    x12_package = Path.cwd().parent / "x12"
    main(base, x12_package, None)
    logging.shutdown()
