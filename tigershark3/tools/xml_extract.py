"""
The ``xml_extract`` application converts the schema from the PyX12 project's XML-based schema definitions
into Python class definitions using Annotated types.


SYNOPSIS
===========

::

    python tools/xml_extract.py

DESCRIPTION
============

This application creates subclasses of :py:class:`x12.base.Composite`, :py:class:`x12.base.Segment`, :py:class:`x12.base.Loop`, and :py:class:`x12.base.Message` definitions.
This writes a module file with the class definitions for each message.

It also creates a :py:mod:`x12.common` module with base
types and reused type definitions.


OPTIONS
=======

Currently, there are no command-line options. The ``__main__`` section sets
two global variables::

:base:

    This has default value of ``Path.home() / "github" / "pyx12" / "pyx12" / "map"``
    It's the location of the GitHub checked out of the PyX12 project.

:output:
    This is the format of the output. The default  value is ``"python"``.
        Other choices include ``"schema-python"`` and ``"json"``.

The results are written to the ``../x12`` or the ``../json`` directory.
For python and schema-python options, the output goes to ``../x12``.
The ``"json"`` output is written to ``../x12``.

EXIT STATUS
============

:0:
    if it worked.

:2:
    if it raises an exception. This is often because of unparsable XML input or unwritable output directories.


ENVIRONMENT
===========

TBD


FILES
=======

See https://github.com/azoner/pyx12

See https://github.com/azoner/pyx12/tree/master/pyx12/map for the message definitions.

Several sources of data are integrated to create the full schema.

1. The :file:`nnn.nnnn.xnnnn...xml` files. Example :file:`270.4010.X092.A1.xml`. These have the message definitions.

2. The :file:`codes.xml` file, and :file:`detaele.xml` file with additional data to support the data type definitions.

3. The :file:`x12.control.00401.xml` and :file:`x12.control.00501.xml` with core structural information
   used to map a message to the specific version of a message definition.

It's not perfectly clear that the :file:`maps.xml` file is *required*, but it seems useful for creating
a declarative set of X12 messages.

NOTES
==========

X12 Schema
-----------

The X12 schema definitions created here depend on an ``x12.base`` module to provide
the superclass definitions of Element, Composite, Segment, Loop, and Message.

This app writes a collection of message-specific modules
with class definitions for all of the elements, etc., that are part of that message.
Reuse is not considered at this point.
In many cases, the Control segment definitions (ISA, IEA, GS, GE, etc.) are reusable.
They're repeated in each module, however.

Structure and Naming
---------------------

One complication here is that within a given message definition,
the ``Element``, ``Segment``, ``Loop``, and ``Message`` structure is unique, but subsidiary structure names are reused.
This means the message -- as a whole -- is a kind of namespace around the structural elements.
This means Segment names are qualified by the Loop that contains the Segment.

The idea of exposing a Segment class as if it is a dataclass-like record
is made challenging by way Segments are reused in distinct Loops.

Type Definitions
-----------------

The Element definitions, used to define the atomic elements of Segments and Composites, are heavily reused.
These become a module of common definitions.

The X12 Data Type attribute is defines the base Python type.
These include numerous string types (``AN``, ``ID``),
integer types (``N``), float types (``R``), Decimal types (``Nx``),
datetime.date (``DT``) and datetime.time (``TM``).

There are 3 variations on DT formatting:

-   ``<data_ele ele_num="I08" data_type="DT" min_len="6" max_len="6" name="I08"/>``

-   ``<data_ele ele_num="373" data_type="DT" min_len="8" max_len="8" name="Date"/>``

-   ``<data_ele ele_num="29" data_type="DT" min_len="6" max_len="8" name="Date"/>``

This means there are three underlying data element definitions

::

    DT: TypeAlias = datetime.date

    I08: TypeAlias = Annotated[DT, MinLen(6), MaxLen(6)]
    D_373: TypeAlias = Annotated[DT, MinLen(8), MaxLen(8)]
    D_29: TypeAlias = Annotated[DT, MinLen(6), MaxLen(8)]

The Code definitions, similarly, are part of the module of schema details.
These are enumerations of all valid code values.
The raw values are in the common module. From these an :py:class:`x12.annotations.Enumerated`
annotation is built.

In a JSON Schema, a "$ref" path of the form "#/$common/some_code" or "#/$common/some_element_schema",
can provide a reference to the reusable data element definitions.
This parallels the Python ``x12.common`` module which has these definitions.

Using "#" implies  the "$common" section is part of each message's overall JSONSchema definition.
It could be replaced with an external reference using a full URI, which might be more
sensible in the long run.

Type Names and Stuctures
------------------------

There are two pools of type definitions in ``dataele.xml``

-   ``Ixx`` names, part of the reused ISA segment.

-   ``nnn`` numbers, used everywhere else. We rename these to ``D_nnn`` to provide a Pythonic name.

There are two pools of code definitions:

-   Common codesets defined in the ``codes.xml``.  (There are 9 of these.)

-   Data-element specific codesets defined within the element of a message.

A data type, then, has the following definition aspects:

-   Base ``data_type_code`` ("AN", "ID", "DT", "TM", etc.)
    These are -- generally -- mappings to a Python type.
    For the ``Nx``, it includes the decimal scale factor.
    For ``DT`` and ``TM``, a length is required, also.

-   Annotations with common definition details (minLength, maxLength, title) from ``common.xml``.
    A "format" value is implied by the length for ``DT``, ``TM``, ``Nx``, ``N``, and ``R``.

-   Enumerated literals come either from a ``codes.xml`` or from the element definition.


Type Extensions
---------------

Some messages will have two AN fields. One with a type and the second with a value.
This extra type detail is one of the following:

-   D8 (yyyymmdd),

-   D6 (yymmdd),

-   RD8 (yyyymmdd-yyyymmdd),

-   TM (hhmm)

These are types **outside** the X12 definitions.
They're application-specific.

X12 Message Version Mapping
---------------------------

The overall "mapping" from source text to message is a separate capability
This can use ``x12.control.*`` module generic definitions to locate the correct module to process a message.

The base mapping superclass permits a subclass to provide a rule
for disambiguating messages.

A mapping search class could use the collection of mapping objects
to locate the module that can parse a message.

.. todo:: This version identification is not implemented

"""
import abc
from collections import deque
from collections.abc import Iterator
from contextlib import redirect_stdout
from dataclasses import dataclass, asdict, field
import datetime
from decimal import Decimal
import logging
from pathlib import Path
from pprint import pprint, pformat
import sys
from textwrap import indent
from typing import (
    Union, TypeAlias, Any, TextIO,
    Self, cast, Deque, Type
)
from xml.etree import ElementTree as XML


logger = logging.getLogger("xml_extract")

optional_text = lambda tag, name: (
    sub_tag.text if (sub_tag := tag.find(name)) is not None else ""
)

JSONSchema: TypeAlias = dict[str, Any] | list[Any] | str

@dataclass
class Codeset:
    """
    An enumerated set of values used to define an Element.

    A JSONSchema ``{"type": "string", "enum": []}`` schema.

    No Annotation, these are ``name = [values]`` constructs in Python.
    """
    id: str
    data_ele: str
    source: str
    values: list[str]

    @property
    def label(self):
        return self.id

    def jsonschema(self) -> JSONSchema:
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
        id = cast(XML.Element, codeset_tag.find('id')).text
        data_ele = optional_text(codeset_tag, 'data_ele')
        source = optional_text(codeset_tag, 'source')
        version_tag = cast(XML.Element, codeset_tag.find('version'))
        values = [
            code.text for code in version_tag.findall('code')
        ]
        codeset = Codeset(
            id=cast(str, id),
            data_ele=data_ele,
            source=cast(str, source),
            values=cast(list[str], values),
        )
        logger.debug(codeset)
        yield codeset


X12_TYPE_SCHEMA: dict[str, JSONSchema] = {
    "AN": {"type": "string"}, # AlphaNumeric
    "B": {"type": "string"},  # Binary?
    "DT": {"type": "string"},  # date, format based on length, "format": "\\d{6,8}"
    "ID": {"type": "string"}, # Identifier, numeric string.
    "R": {"type": "number"},  # Real
    "TM": {"type": "string"},  # Time. format "format": "\\d{4,6}"
    "N": {"type": "integer"},  # Number (integer?)
    # These have no proper JSONSchema representation, the underlying type is "Decimal" with a scale.
    "N0": {"type": "number", "scale": 0}, # 0 decimal places.
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

X12_TYPE_ANNOTATION: dict[str, str] = {
    "AN": "str",  # AlphaNumeric
    "B": "str",  # Binary?
    "DT": "datetime.date",  # Annotation will add MinLen(6-8), MaxLen(6-8), Format(r"\d{6}{8}") details
    "ID": "str",  # Identifier, often (but not always) a numeric string.
    "R": "float",  # Real
    "TM": "datetime.time",  # Annotation will add MinLen(4-6), MaxLen(4-6), Format(r"\d{4}{6}") details
    "N": "int",  # Number (integer?)
    "N0": "Annotated[Decimal, Scale(0)]",  # 0 decimal places
    "N1": "Annotated[Decimal, Scale(1)]",
    "N2": "Annotated[Decimal, Scale(2)]",  # 2 decimal places, i.e. currency.
    "N3": "Annotated[Decimal, Scale(3)]",
    "N4": "Annotated[Decimal, Scale(4)]",
    "N5": "Annotated[Decimal, Scale(5)]",
    "N6": "Annotated[Decimal, Scale(6)]",
    "N7": "Annotated[Decimal, Scale(7)]",
    "N8": "Annotated[Decimal, Scale(8)]",
    "N9": "Annotated[Decimal, Scale(9)]",
}


@dataclass
class DataElement:
    """
    A data element description, often reused by multiple Elements.

    A JSONSchema {"type": ..., "minLength": ..., "maxLength": ..., "description": ...} schema
    """
    ele_num: str
    data_type: str  # Base type
    min_len: str | None
    max_len: str | None
    name: str

    @property
    def class_name(self) -> str:
        return f'{pythonify(self.ele_num, "D_")}'

    @property
    def int_min_len(self) -> int | None:
        if self.min_len is not None:
            return int(self.min_len)
        return None

    @property
    def int_max_len(self) -> int | None:
        if self.max_len is not None:
            return int(self.max_len)
        return None

    def jsonschema(self) -> JSONSchema:
        schema = cast(dict[str, Any], X12_TYPE_SCHEMA[self.data_type])
        schema |= {
            "title": self.name,
            "data_type_code": self.data_type,
        }
        if self.min_len is not None:
            schema["minLength"] = int(self.min_len)
        if self.max_len is not None:
            schema["maxLength"] = int(self.max_len)
        # additional special cases
        if self.data_type in {"DT", "TM"}:
            if self.min_len == self.max_len:
                schema["format"] = f"\\d{{{self.min_len}}}"
            else:
                schema["format"] = f"\\d{{{self.min_len},{self.max_len}}}"
        return schema

    def annotation(self) -> tuple[str, str]:
        base = X12_TYPE_ANNOTATION[self.data_type]
        extensions = [base, f"Title({self.name!r})"]
        if self.min_len is not None:
            extensions.append(f"MinLen({int(self.min_len)})")
        if self.max_len is not None:
            extensions.append(f"MaxLen({int(self.max_len)})")
        if self.data_type in {"DT", "TM"}:
            if self.min_len == self.max_len:
                extensions.append(f'Format("\\d{self.min_len}")')
            else:
                extensions.append(f'Format("\\d{self.min_len,self.max_len}")')
        return (
            f"{self.class_name}: TypeAlias = Annotated[{', '.join(extensions)}]",
            ""
        )

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
            name=name,
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
                icvn=cast(str, icvn),
                vriic=cast(str, vriic),
                fic=cast(str, fic),
                abbr=cast(str, abbr),
                definition=cast(str, definition),
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
    def class_name(self) -> str:
        return f"{self.loop}_{pythonify(self.xid, 'E')}"

    def jsonschema(self) -> JSONSchema:
        schema: dict[str, Any] = {
            "title": self.name,
            "usage": self.usage,  # Required, Situational, Not-Used
            "description": f"xid={self.xid} data_ele={self.data_ele}",
            "position": int(self.seq),
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

    def annotation(self) -> tuple[str, str]:
        """
        Some Segment or Composite will have

        ::

            name: Annotated[DT, Title("Item"), Usage("R"), Sequence("1")]

        The ``DT`` type alias is ``Annotated[datetime.date, ...]``.

        This flattens nicely to ``datetime.date`` with details.

        Or

        ::

            ItemName: TypeAlias = Annotated[DT, title("Item"), ...]
            name: Annotated[list[ItemName], MaxItems(4)]

        The list -- as a whole -- and the items both have annotations.
        The over-all ``list[]`` has a ``MaxItems()`` annotation.
        The Element within the list has the detailed annotations for this element.
        """
        base = [pythonify(self.data_ele, 'D_'), f"Title({self.name!r})",  f"Usage({self.usage!r})", f"Position({int(self.seq)})"]
        if self.codes:
            base.append(f"Enumerated(*{self.codes})")
        # if self.common_def:
        #     base.append(f"Enumerated(*data_element[{self.common_def}])")
        if self.external:
            base.append(f"Enumerated(*{self.external})")
        type_str = f"Annotated[{', '.join(base)}]"
        if self.repeat:
            annotations = (
                f"Item{self.attr_name.title()}: TypeAlias = {type_str}",
                f"{self.attr_name}: Annotated[list[Item{self.attr_name.title()}], MaxItems({int(self.repeat)})]"
            )
        else:
            annotations = (
                "",
                f"{self.attr_name}: {type_str}"
            )
        return annotations

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
    def class_name(self) -> str:
        return f"{self.loop}_{pythonify(self.xid or self.refdes or self.data_ele, 'C')}"

    @property
    def required(self):
        return [elt.attr_name for elt in self.elements if elt.usage == "R"]

    def jsonschema(self) -> JSONSchema:
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

    def annotation(self) -> tuple[str, str]:
        base = [self.class_name or pythonify(self.data_ele, 'D_'), f"Title({self.name!r})", f"Usage({self.usage!r})", f"Position({int(self.seq)})"]
        if self.required:
            base.append("Required(True)")
        type_str = f"Annotated[{', '.join(base)}]"
        if self.repeat:
            annotations = (
                f"Item{self.attr_name.title()}: TypeAlias = {type_str}",
                f"{self.attr_name}: Annotated[list[Item{self.attr_name.title()}], MaxItems({int(self.repeat)})]"
            )
        else:
            annotations = (
                "",
                f"{self.attr_name}: {type_str}"
            )
        return annotations

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
    def class_name(self) -> str:
        return f"{self.loop}_{pythonify(self.xid, 'S')}"

    @property
    def required(self) -> list[str]:
        return [elt.attr_name for elt in self.children if elt.usage == "R"]

    @property
    def repeat(self) -> bool:
        return bool(self.max_use) and self.max_use != "1"

    def jsonschema(self) -> JSONSchema:
        schema: dict[str, Any] = {
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
                # if elt.usage == "N":
                #     continue
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

    def annotation(self) -> tuple[str, str]:
        """
        Some Message or Loop will have

        ::

            segment: Annotated[Loop_Seg_Class, Title("Segnment"), Usage("R"), Sequence("1")]

        This flattens nicely to ``Loop_Seg_Class`` with details.

        Or

        ::

            ItemSegment: TypeAlias = Annotated[Loop_Seg_Class, title("Segnment"), ...]
            segment: Annotated[list[ItemSegment], MaxItems(4)]

        The list -- as a whole -- and the items both have annotations.
        List annotations are small (MaxItems).
        The Segment in the list has more complex annotations.
        """
        # While this works, mypy can't figure it out.
        base = [self.class_name, f"Title({self.name!r})", f"Usage({self.usage!r})", f"Position({int(self.pos)})"]
        if self.syntax:
            base.append(f"Syntax({self.syntax})")
        if self.required:
            base.append("Required(True)")
        type_str = f"Annotated[{', '.join(base)}]"
        if self.repeat:
            if self.max_use.startswith(">"):
                min_max = f"MinItems({int(self.max_use[1:])})"
            else:
                min_max = f"MaxItems({int(self.max_use)})"
            annotations = (
                f"Item{self.attr_name.title()}: TypeAlias = {type_str}",
                f"{self.attr_name}: Annotated[list[Item{self.attr_name.title()}], {min_max}]"
            )
        else:
            annotations = (
                "",
                f"{self.attr_name}: {type_str}"
            )
        return annotations

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
    def attr_name(self) -> str:
        return pythonify(self.xid, "L").lower()

    @property
    def class_name(self) -> str:
        return pythonify(self.xid, "L")

    @property
    def required(self) -> list[str]:
        return [elt.attr_name for elt in self.children if elt.usage == "R"]

    def jsonschema(self) -> JSONSchema:
        schema: dict[str, Any] = {
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
                # if elt.usage != "N"
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

    def annotation(self) -> tuple[str, str]:
        base = [self.class_name, f"Title({self.name!r})", f"Usage({self.usage!r})", f"Position({int(self.pos)})"]
        if self.required:
            base.append("Required(True)")
        type_str = f"Annotated[{', '.join(base)}]"
        if self.repeat:
            if self.repeat.startswith('>'):
                min_items = f"MinItems({int(self.repeat[1:])})"
            else:
                min_items = f"MinItems({int(self.repeat)})"
            annotations = (
                f"Item{self.attr_name.title()}: TypeAlias = {type_str}",
                f"{self.attr_name}: Annotated[list[Item{self.class_name.title()}], {min_items}]"
            )
        else:
            annotations = (
                "",
                f"{self.attr_name}: {type_str}"
            )
        return annotations

@dataclass
class Message:
    """
    A Complete Message.

    No annotation for a message as a whole,
    it's a collection of Loops, wrapped
    in a ``class`` statement.
    """
    xid: str
    name: str
    loops: list[Loop]

    @property
    def class_name(self) -> str:
        return pythonify(self.xid, "MSG")

    @property
    def required(self) -> list[str]:
        return [elt.attr_name for elt in self.loops if elt.usage == "R"]

    def jsonschema(self) -> JSONSchema:
        """
        Emits JSON Schema for a message.

        ..  todo:: properly flatten the message to emit $loop, $segment, $composite, and $element definitions.
        """
        schema: dict[str, Any] = {
            "title": self.name,
            "description": f"xid={self.xid} name={self.name}",
        }
        if self.loops:
            schema["type"] = "object"
            schema["properties"] = {
                elt.attr_name: {"$ref": f"#/$loops/{elt.class_name}"}  # elt.jsonschema()
                for elt in self.loops
                # if elt.usage != "N"
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
            xid=cast(str, xid_a),
            data_ele=element_id,
            name=name,
            usage=usage_a or usage,
            seq=seq_a or seq,
            refdes=refdes,
            repeat=repeat,
            codes=cast(list[str], codes),
            external=cast(str, external),
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
            xid=cast(str, xid_a),
            data_ele=data_ele_a or data_ele,
            name=name,
            usage=usage_a or usage,
            seq=seq_a or seq,
            refdes=refdes,
            syntax=cast(list[str], syntax),
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
        children: list[Element | Composite] = []
        for child_tag in base_tag.findall("*"):
            if child_tag.tag == "element":
                ec = element_walker(loop_context, child_tag)
                children.append(ec)
            elif child_tag.tag == "composite":
                cc = composite_walker(loop_context, child_tag)
                children.append(cc)
            elif child_tag.tag in {"name", "end_tag", "usage", "pos", "max_use", "syntax"}:
                pass  # Skip already processed tags
            else:
                raise RuntimeError(f"Unexpected {child_tag.tag}")
        segment = Segment(
            xid=cast(str, xid_a),
            name=name,
            end_tag=end_tag,
            usage=usage_a or usage,
            pos=pos_a or pos,
            max_use=max_use_a or max_use,
            syntax=cast(list[str], syntax),
            children=children,
            loop=loop_context
        )
        logger.debug(segment)
        return segment

    def loop_walker(base_tag: XML.Element) -> Loop:
        xid_a = cast(str, base_tag.attrib.get("xid"))
        pos_a = base_tag.attrib.get("pos")
        usage_a = base_tag.attrib.get("usage")
        repeat_a = base_tag.attrib.get("repeat")
        type_a = base_tag.attrib.get("type")  # Actually used, doesn't seem appropriate at this level.
        name = optional_text(base_tag, "name")
        usage = optional_text(base_tag, "usage")
        pos = optional_text(base_tag, "pos")
        repeat = optional_text(base_tag, "repeat")
        # Any number of loop OR segment may follow...
        children: list[Loop | Segment] = []
        for child_tag in base_tag.findall("*"):
            if child_tag.tag == "loop":
                cl = loop_walker(child_tag)
                children.append(cl)
            elif child_tag.tag == "segment":
                cs = segment_walker(pythonify(xid_a, "L"), child_tag)
                children.append(cs)
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
            type=cast(str, type_a),
            children=children,
        )
        logger.debug(loop)
        return loop

    document = XML.parse(source)
    transaction_tag = document.getroot()
    xid = transaction_tag.attrib.get("xid")
    name = cast(XML.Element, transaction_tag.find("name")).text
    loops = [
        loop_walker(loop_tag)
        for loop_tag in transaction_tag.findall("loop")
    ]
    message = Message(
        xid=cast(str, xid),
        name=cast(str, name),
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
        self.path: Deque[tuple[str, str]] = deque()
        self.codes: dict[str, Codeset]
        self.types: dict[str, DataElement]
        self.type_names: set[str]

    def codesets(self, c: dict[str, Codeset]) -> Self:
        """Setter for codesets."""
        self.codes = c
        return self

    def data_elements(self, d: dict[str, DataElement]) -> Self:
        """Setter for data elements."""
        self.types = d
        return self

    def dump_codesets(self) -> set[str]:
        return set()

    def dump_data_elements(self) -> set[str]:
        return set()

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
                for seg_child in component.children:
                    self.visit(seg_child)
                self.path.pop()
                self.segment(component)
            case Loop():
                self.path.append(("LOOP", component.class_name))
                for loop_child in component.children:
                    self.visit(loop_child)
                self.path.pop()
                self.loop(component)
            case Message():
                self.path = deque([("MESSAGE", component.class_name)])
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


class EmitPython_Interim(MessageVisitor):
    """
    Message visitor to emit Pythonic definitions for
    Elements, Composites, Segments, Loops, and Messages.

    This is "Interim", which uses an explicit ``Schema``
    internal class definition.

    The classes written will be extension subclasses to definitions in ``x12.base``.
    """
    def dump_codesets(self) -> set[str]:
        names: set[str] = set()
        for id in self.codes:
            name = pythonify(id, 'C_')
            print(f"{name} = {self.codes[id].jsonschema()}")
            names.add(name)
        return names

    def dump_data_elements(self) -> set[str]:
        self.type_names = set()
        for name in self.types:
            name = pythonify(name, 'D_')
            print(f"{name} = {self.types[name].jsonschema()}")
            self.type_names.add(name)
        return self.type_names

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
                print(f"        min_len = {self.types[element.common_def].int_min_len}")
            if self.types[element.data_ele].max_len:
                print(f"        max_len = {self.types[element.common_def].int_max_len}")
        else:
            logger.warning("no data_element for %s", element)


    def composite(self, composite: Composite) -> None:
        print("\n")
        # print(f"# {self.path}")
        print(f'class {composite.class_name}(Composite):')
        print(f'    class Schema:')
        print(f"        json = {indent(pformat(composite.jsonschema(), compact=True, sort_dicts=False), 8*' ').lstrip()}")
        for elt in composite.elements:
            # if elt.usage == "N":
            #    continue
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
                if isinstance(elt,Composite) and len(elt.elements) == 0:
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
            # if elt.usage == "N":
            #     continue
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
            # if elt.usage == "N":
            #    continue
            if elt.repeat:
                type_text = f"list[{elt.class_name}]"
            else:
                type_text = elt.class_name
            if elt.attr_name not in message.required:
                type_text = f"{type_text} | None"
            print(f"    {elt.attr_name}: {type_text}")


class EmitPython_Annotated(MessageVisitor):
    """
    Message visitor to emit Pythonic definitions for
    Elements, Composites, Segments, Loops, and Messages.

    This is "Annotated". Elements don't have a separate class,
    their annotations are part of the containing Segment or Composite.

    The classes created will be extension subclasses to definitions in ``x12.base``.
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

    def dump_codesets(self) -> set[str]:
        names: set[str] = set()
        for id, codeset in self.codes.items():
            # annotation = f"Annotated[str, Enumerated(*{codeset.values})]"
            name = pythonify(id, 'C_')
            print(f"{name} = {codeset.values!r}")
            names.add(name)
        return names

    def dump_data_elements(self) -> set[str]:
        self.type_names = set()
        for name, base_def in X12_TYPE_ANNOTATION.items():
            print(f"{name}: TypeAlias = {base_def}")
        for name, de_def in self.types.items():
            assert de_def.data_type in X12_TYPE_ANNOTATION, f"Data type {de_def.data_type!r} unknown"
            base = [str(de_def.data_type)]
            if de_def.min_len:
                base.append(f"MinLen({de_def.min_len})")
            if de_def.max_len:
                base.append(f"MaxLen({de_def.max_len})")
            name = pythonify(name, 'D_')
            print(
                f"{name}: TypeAlias = Annotated[{', '.join(base)}]"
            )
            self.type_names.add(name)
        return self.type_names

    def element(self, element: Element) -> None:
        pass  # Not a separate class in the Python.

    def composite(self, composite: Composite) -> None:
        print("\n")
        # print(f"# {self.path}")
        print(f'class {composite.class_name}(Composite):\n    """{composite.name}"""')
        if composite.elements:
            for elt in composite.elements:
                # if elt.usage == "N":
                #    continue
                alias, annotation = elt.annotation()
                # Not sure we can make optional attributes work via Union[]
                # if elt.attr_name not in composite.required:
                #     name, _, annotation = annotation.partition(":")
                #     annotation = f"{name}: Union[{annotation}, None]"
                print(f"    {alias}")
                print(f"    {annotation}")
        else:
            print("    pass")

    def segment(self, segment: Segment) -> None:
        print("\n")
        # print(f"# {self.path}")
        print(f'class {segment.class_name}(Segment):\n    """{segment.name}"""\n    _segment_name = {segment.attr_name.upper()!r}')
        if segment.children:
            for elt in segment.children:
                if elt.usage == "N":
                    if isinstance(elt,Composite) and len(elt.elements) == 0:
                        continue
                alias, annotation = elt.annotation()
                # Not sure we can make optional attributes work via Union[]
                # if elt.attr_name not in segment.required:
                #     name, _, annotation = annotation.partition(":")
                #     annotation = f"{name}: Union[{annotation}, None]"
                print(f"    {alias}")
                print(f"    {annotation}")
        else:
            print("    pass")

    def loop(self, loop: Loop) -> None:
        print("\n")
        # print(f"# {self.path}")
        print(f'class {loop.class_name}(Loop):')
        if loop.children:
            for elt in loop.children:
                # if elt.usage == "N":
                #    continue
                alias, annotation = elt.annotation()
                # Not sure we can make optional attributes work via Union[]
                # if elt.attr_name not in loop.required:
                #     name, _, annotation = annotation.partition(":")
                #     annotation = f"{name}: Union[{annotation}, None]"
                print(f"    {alias}")
                print(f"    {annotation}")
        else:
            print("    pass")

    def message(self, message: Message) -> None:
        print("\n")
        print(f'class {message.class_name}(Message):\n    """{message.name}"""')
        for elt in message.loops:
            # if elt.usage == "N":
            #    continue
            alias, annotation = elt.annotation()
            # Not sure we can make optional attributes work via Union[]
            # if elt.attr_name not in message.required:
            #     name, _, annotation = annotation.partition(":")
            #     annotation = f"{name}: Union[{annotation}, None]"
            print(f"    {alias}")
            print(f"    {annotation}")

class PythonMaker:
    visitor_class: Type[MessageVisitor]

    def make_common_module(
            self,
            codesets: dict[str, Codeset],
            data_elements: dict[str, DataElement],
            target_package: Path
    ) -> set[str]:
        """
        Emits common module with definitions of common data types.

        Depends on ``EmitPython_Interim`` class.
        """
        target_path = (target_package / "common").with_suffix(".py")

        cls = self.visitor_class
        code_writer = cls().data_elements(data_elements).codesets(codesets)
        names: set[str] = set()

        with target_path.open('w') as target_file:
            with redirect_stdout(target_file):
                print('"""')
                print(f"Created {datetime.datetime.now()}")
                print('"""')
                print()
                print("from typing import TypeAlias, Annotated")
                print("import datetime")
                print("from decimal import Decimal")
                print("from x12.annotations import *")
                names.union(code_writer.dump_codesets())
                names.union(code_writer.dump_data_elements())
        return names

    def make_message_module(
            self,
            codesets: dict[str, Codeset],
            data_elements: dict[str, DataElement],
            source_path: Path,
            target_package: Path
    ) -> None:
        """
        Emits a module to parse a message.

        Depends on ``EmitPython_Interim`` class.
        """
        target_stem = f'msg_{source_path.stem.replace(".", "_")}'
        target_path = (target_package / target_stem).with_suffix(".py")
        logger.info("%s -> %s", source_path.name, target_path.name)

        with source_path.open() as source:
            msg = message_reader(source)

        cls = self.visitor_class
        code_writer = cls().data_elements(data_elements).codesets(codesets)
        code_writer.source_name = source_path.stem

        with target_path.open('w') as target_file:
            with redirect_stdout(target_file):
                print('"""')
                print(source_path.stem)
                print(f"Created {datetime.datetime.now()}")
                # print(msg)
                print('"""')
                print("from .base import *")
                print("from .common import *")
                code_writer.visit(msg)


    def make_python(self, base: Path, target: Path) -> None:
        """
        Extract from XML schema, creating Python.

        Each message becomes a separate module in an overall "x12" package.

        Depends on EmitPython_Interim
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
        names = self.make_common_module(codesets, data_elements, x12_package)

        for source_path in sorted(base.glob("x12.control.*.xml")):
            self.make_message_module(codesets, data_elements, source_path, x12_package)

        for source_path in sorted(base.glob("[0-9][0-9][0-9]*.xml")):
            self.make_message_module(codesets, data_elements, source_path, x12_package)

        with (base / "maps.xml").open() as source:
            maps = list(map_reader(source))

        # TODO: Emit the mapping objects.
        # self.make_mapper(maps, message_modules)


class InterimPythonMaker(PythonMaker):
    """Make Python using Schema constructs."""
    visitor_class = EmitPython_Interim


class AnnotatedPythonMaker(PythonMaker):
    """Make Python using Annotated definitions."""
    visitor_class = EmitPython_Annotated


## TODO: Combine make_message_schema() and  make_jsonschema() into a class

def make_message_schema(
        codesets: dict[str, Codeset],
        data_elements: dict[str, DataElement],
        source_path: Path,
        target_package: Path
) -> None:
    """
    Emit JSON Schema for a message.

    ..  todo:: Include the "$ref" data types and code sets.

    JSON Schema **should** be created from the Python, not from the XML.
    """
    target_stem = f'msg_{source_path.stem.replace(".", "_")}'
    target_path = (target_package / target_stem).with_suffix(".json")
    logger.info("%s -> %s", source_path.name, target_path.name)
    with source_path.open() as source:
        msg = message_reader(source)
    print(msg.jsonschema())


def make_schema(base: Path, target: Path) -> None:
    """
    Extract from XML schema, creating JSON Schema.

    Each message becomes a separate .json document.

    JSON Schema **should** be created from the Python, not from the XML.
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


def make_python(maker: PythonMaker, base: Path, x12_package: Path) -> None:
    """
    Extract from XML schema and make Python modules for parsing messages.
    """
    logger.info("Source %s", base)
    logger.info("Creating %s", x12_package)
    # maker = InterimPythonMaker()
    # maker = AnnotatedPythonMaker()
    maker.make_python(base, x12_package)

def make_jsonschema(base: Path, json_dir: Path) -> None:
    """
    Making JSON Schema is possible.
    JSON Schema **should** be created from the Python, not directly from the XML.
    """
    logger.info("Source %s", base)
    logger.info("Creating %s", json_dir)
    make_schema(base, json_dir)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    base = Path.home() / "github" / "pyx12" / "pyx12" / "map"
    output = "python"

    if output == "python":
        x12_package = Path.cwd().parent / "x12"
        make_python(AnnotatedPythonMaker(), base, x12_package)
    elif output == "schema-python":
        x12_package = Path.cwd().parent / "x12"
        make_python(InterimPythonMaker(), base, x12_package)
    elif output == "json":
        json_dir = Path.cwd() / "json"
        make_jsonschema(base, json_dir)
    else:
        raise ValueError("unknown output option, {output}")
    logging.shutdown()
