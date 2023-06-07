######################
Using TigerShark
######################

There are several things you can do.

1.  `Create a Python class`_. This is a Python subclass of :py:class:`x12.base.Message` to parse exchange format messages or create JSON Schema.
    The :py:mod:`tools.xml_extract` converts the XML versions of .SEF files to class definitions.

2.  `Emit a JSON Schema`_. The extracts JSON Schema from a subclass of :py:class:`x12.base.Message`.

3.  `Parse X12 Exchange-formatted messages`_. This uses the subclass of :py:class:`x12.base.Message` to create Plain Old Python Objects from the message text.

4.  `Emit a parsed X12 message a variety of formats`_. This includes "segments" format, JSON format, or even a Python expression to rebuild the message object.

We'll look at each of these in some detail

Create a Python class
=====================

The :mod:`tools.xml_extract` application parses an XML
file and writes a Python module from the XML.
This module will have a subclass of :py:class:`x12.base.Message`
that can parse messages or emit a schema.

..  important:: .SEF files have the authoritative definitions.

    This tool uses the PyX12 XML versions of the .SEF files.
    Ideally, a version of this could work with the source .SEF
    files.

It works like this.

1.  Git Checkout the `PyX12 <https://github.com/azoner/pyx12>`_ project.

2.  Tweak the :py:mod:`tools.xml_extract` module to point to the checked-out files
    and the target directory.

3.  Run the :py:mod:`tools.xml_extract` tool to build the x12 package.

::

    python tools/xml_extract.py

This tool has assumptions about the output directory.

-   The directory tree the Git Clone of the TigerShark project.

-   The Current Working Directory is the :file:`tigershark3/tools` directory.

-   The message classes are written to the :file:`tigershark3/x12` directory.

Emit a JSON Schema
==================

Each generated class has a :meth:`schema` method to emit
a dictionary that can be converted to JSON
notation.

A script might look like this:

::

    from x12 import msg_270_4010_X092_A1
    import json

    schema = msg_270_4010_X092_A1.MSG270.schema()
    print(json.dumps(schema, indent=2))

This will emit a JSON Schema file that can be
shared with non-Python applications.

The :mod:`tools.xml_extract` application parses an XML
file and **can** write a JSON Schema directly from the XML.
It seems, however, better to work directly with the Python
:py:class:`Message` subclass definitions, as shown above.

Parse X12 Exchange-formatted messages
=====================================

A script can look like the following:

::

    from pathlib import Path
    from x12 import msg_270_4010_X092_A1

    source = Path("/path") / "to" / "file.txt"
    document = Source(source.read_text())
    msg = message_class.parse(document)

The ``document`` object is a reader that scans the source
file, looking for the text of segments with appropriate
element and segment separators.

Many message files will have an ISA segment that has
a fixed layout, making it easy to locate the element and
segment separators. In the case where the ISA segment is not
easily parsed, The :py:mod:`Source` initialization can be provided
with the separators. And, yes, this requires someone to look
at the files to see how they're formatted.

If the source is valid, this will create an object, ``msg`` with
attributes for the various components (loops, segments, composites, and elements) of the message.
If the source is invalid, this will raise exceptions showing
the elements that could not be validated.

It is possible to skip validation for a given element.

Emit a parsed X12 message a variety of formats
===============================================

Given a message, ``msg``, parsed by the :meth:`x12.base.Message.parse` method.
it can be emitted in a number of formats:

1.  `Sequence of segments output`_.
    This is a list of segments, similar to the exchange format,
    except it's in Python notation: a list of lists.

2.  `JSON output`_.
    This is a representation of the message/loop/segment/composite/element structure
    with some additional ``_kind`` and ``_name`` fields added.

3.  `Python output`_.
    This is an expression that can rebuild the Plain-Old Python Object.
    The reconstruction requires a ``from msg... import *`` import to
    provide all the required names for loops, segments, composites, and elements.

Sequence of segments output
---------------------------

Use the :meth:`x12.base.Message.segment_iter` method
of a message to get the segments.
The built-in :meth:`__str__` provides the list of strings output for each segment.

::

    print(list(msg.segment_iter()))

This produces a list-of-lists structure::

    [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '12345          ', datetime.date(2012, 6, 5), datetime.time(23, 24), 'U', '00401', Decimal('50033'), '1', 'P', '^'],
        ['GS', 'HB', 'ZIRMED', '12345', datetime.date(2012, 6, 5), datetime.time(23, 24), Decimal('50025'), 'X', '004010X092A1'],
        ['ST', '271', '0001'],
        ['BHT', '0022', '11', '11111', datetime.date(2012, 6, 5), datetime.time(23, 24, 23), None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'Health Net Inc', '', '', '', '', 'PI', '10385', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', 'DR. ACULA', '', '', '', '', 'XX', '1111111111', None, None],
        ['HL', '3', '2', '22', '0'],
        ['TRN', '1', '222222222', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '2', '333333333', '9ZIRMEDCOM', 'ELI ID'],
        ['TRN', '1', '4444444444', '9MEDDATACO', None],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'R11111111', None, None],
        ['AAA', 'N', '', '72', 'C'],
        ['AAA', 'N', '', '73', 'C'],
        ['AAA', 'N', '', '73', 'C'],
        ['AAA', 'N', '', '58', 'C'],
        ['DTP', '291', 'D8', '20120408'],
        ['SE', Decimal('17'), '0001'],
        ['GE', Decimal('1'), Decimal('50025')],
        ['IEA', Decimal('1'), Decimal('50033')]
    ]

This tends to mirror the source format.

JSON output
-----------

Use the :meth:`x12.base.Message.json` method
of a message to get the JSON string.

::

    print(msg.json())

The :meth:`x12.base.Message.json` method accepts
an ``indent`` parameter to provide nicely indented output.
Here's the output with ``indent=2``.

::

    {
      "_kind": "Message",
      "_name": "MSG271",
      "isa_loop": [
        {
          "_kind": "Loop",
          "_name": "ISA_LOOP",
          "isa": {
            "_kind": "Segment",
            "_name": "ISA_LOOP_ISA",
            "isa01": "00",
            "isa02": "          ",
            "isa03": "00",
            "isa04": "          ",
            "isa05": "ZZ",
            "isa06": "ZIRMED         ",
            "isa07": "ZZ",
            "isa08": "12345          ",
            "isa09": {
              "date": "20120605",
              "_format": "%Y%m%d"
            },
            "isa10": {
              "time": "2324",
              "_format": "%H%M"
            },
            "isa11": "U",
            "isa12": "00401",
            "isa13": "50033",
            "isa14": "1",
            "isa15": "P",
            "isa16": "^"
          },
          "gs_loop": [
            {
              "_kind": "Loop",
              "_name": "GS_LOOP",
              "gs": {
                "_kind": "Segment",
                "_name": "GS_LOOP_GS",
                "gs01": "HB",
                "gs02": "ZIRMED",
                "gs03": "12345",
                "gs04": {
                  "date": "20120605",
                  "_format": "%Y%m%d"
                },
                "gs05": {
                  "time": "2324",
                  "_format": "%H%M"
                },
                "gs06": "50025",
                "gs07": "X",
                "gs08": "004010X092A1"
              },
              "st_loop": [
                {
                  "_kind": "Loop",
                  "_name": "ST_LOOP",
                  "st": {
                    "_kind": "Segment",
                    "_name": "ST_LOOP_ST",
                    "st01": "271",
                    "st02": "0001"
                  },
                  "header": [
                    {
                      "_kind": "Loop",
                      "_name": "HEADER",
                      "bht": {
                        "_kind": "Segment",
                        "_name": "HEADER_BHT",
                        "bht01": "0022",
                        "bht02": "11",
                        "bht03": "11111",
                        "bht04": {
                          "date": "20120605",
                          "_format": "%Y%m%d"
                        },
                        "bht05": {
                          "time": "2324",
                          "_format": "%H%M"
                        }
                      }
                    }
                  ],
                  "detail": [
                    {
                      "_kind": "Loop",
                      "_name": "DETAIL",
                      "l2000a": [
                        {
                          "_kind": "Loop",
                          "_name": "L2000A",
                          "hl": {
                            "_kind": "Segment",
                            "_name": "L2000A_HL",
                            "hl01": "1",
                            "hl02": "",
                            "hl03": "20",
                            "hl04": "1"
                          },
                          "l2100a": [
                            {
                              "_kind": "Loop",
                              "_name": "L2100A",
                              "nm1": {
                                "_kind": "Segment",
                                "_name": "L2100A_NM1",
                                "nm101": "PR",
                                "nm102": "2",
                                "nm103": "Health Net Inc",
                                "nm104": "",
                                "nm105": "",
                                "nm106": "",
                                "nm107": "",
                                "nm108": "PI",
                                "nm109": "10385"
                              }
                            }
                          ],
                          "l2000b": [
                            {
                              "_kind": "Loop",
                              "_name": "L2000B",
                              "hl": {
                                "_kind": "Segment",
                                "_name": "L2000B_HL",
                                "hl01": "2",
                                "hl02": "1",
                                "hl03": "21",
                                "hl04": "1"
                              },
                              "l2100b": [
                                {
                                  "_kind": "Loop",
                                  "_name": "L2100B",
                                  "nm1": {
                                    "_kind": "Segment",
                                    "_name": "L2100B_NM1",
                                    "nm101": "1P",
                                    "nm102": "2",
                                    "nm103": "DR. ACULA",
                                    "nm104": "",
                                    "nm105": "",
                                    "nm106": "",
                                    "nm107": "",
                                    "nm108": "XX",
                                    "nm109": "1111111111"
                                  }
                                }
                              ],
                              "l2000c": [
                                {
                                  "_kind": "Loop",
                                  "_name": "L2000C",
                                  "hl": {
                                    "_kind": "Segment",
                                    "_name": "L2000C_HL",
                                    "hl01": "3",
                                    "hl02": "2",
                                    "hl03": "22",
                                    "hl04": "0"
                                  },
                                  "trn": [
                                    {
                                      "_kind": "Segment",
                                      "_name": "L2000C_TRN",
                                      "trn01": "1",
                                      "trn02": "222222222",
                                      "trn03": "9ZIRMEDCOM",
                                      "trn04": "ELR ID"
                                    },
                                    {
                                      "_kind": "Segment",
                                      "_name": "L2000C_TRN",
                                      "trn01": "2",
                                      "trn02": "333333333",
                                      "trn03": "9ZIRMEDCOM",
                                      "trn04": "ELI ID"
                                    },
                                    {
                                      "_kind": "Segment",
                                      "_name": "L2000C_TRN",
                                      "trn01": "1",
                                      "trn02": "4444444444",
                                      "trn03": "9MEDDATACO"
                                    }
                                  ],
                                  "l2100c": [
                                    {
                                      "_kind": "Loop",
                                      "_name": "L2100C",
                                      "nm1": {
                                        "_kind": "Segment",
                                        "_name": "L2100C_NM1",
                                        "nm101": "IL",
                                        "nm102": "1",
                                        "nm103": "",
                                        "nm104": "",
                                        "nm105": "",
                                        "nm106": "",
                                        "nm107": "",
                                        "nm108": "MI",
                                        "nm109": "R11111111"
                                      },
                                      "aaa": [
                                        {
                                          "_kind": "Segment",
                                          "_name": "L2100C_AAA",
                                          "aaa01": "N",
                                          "aaa02": "",
                                          "aaa03": "72",
                                          "aaa04": "C"
                                        },
                                        {
                                          "_kind": "Segment",
                                          "_name": "L2100C_AAA",
                                          "aaa01": "N",
                                          "aaa02": "",
                                          "aaa03": "73",
                                          "aaa04": "C"
                                        },
                                        {
                                          "_kind": "Segment",
                                          "_name": "L2100C_AAA",
                                          "aaa01": "N",
                                          "aaa02": "",
                                          "aaa03": "73",
                                          "aaa04": "C"
                                        },
                                        {
                                          "_kind": "Segment",
                                          "_name": "L2100C_AAA",
                                          "aaa01": "N",
                                          "aaa02": "",
                                          "aaa03": "58",
                                          "aaa04": "C"
                                        }
                                      ],
                                      "dtp": [
                                        {
                                          "_kind": "Segment",
                                          "_name": "L2100C_DTP",
                                          "dtp01": "291",
                                          "dtp02": "D8",
                                          "dtp03": "20120408"
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ],
                  "se": {
                    "_kind": "Segment",
                    "_name": "ST_LOOP_SE",
                    "se01": "17",
                    "se02": "0001"
                  }
                }
              ],
              "ge": {
                "_kind": "Segment",
                "_name": "GS_LOOP_GE",
                "ge01": "1",
                "ge02": "50025"
              }
            }
          ],
          "iea": {
            "_kind": "Segment",
            "_name": "ISA_LOOP_IEA",
            "iea01": "1",
            "iea02": "50033"
          }
        }
      ]
    }

Each of the structures has a "_kind" and a "_name" attribute
to make it a little easier to track down the class definition.
For date and time values, the value is a small dictionary
with the source text and the format,
for example. ``{"time": "2324", "_format": "%H%M"}``.

An alternative is to use the  :meth:`x12.base.Message.json` method
of a message to get a JSON-friendly dictionary.

::

    print(json.dumps(msg.asdict()))

This can permit more flexibility in using
the features of :func:`json.dumps`.

Python output
-------------

Use the built-in :py:func:`repr` function
to emit Python code that can rebuild the message.

::

    print(repr(msg))

After formatting, the output starts like this::

    MSG271(
        isa_loop=[
            ISA_LOOP(
                isa=ISA_LOOP_ISA(
                    isa01='00',
                    isa02='          ',
                    isa03='00',
                    isa04='          ',
                    isa05='ZZ',
                    isa06='ZIRMED         ',
                    isa07='ZZ',
                    isa08='12345          ',
                    isa09=datetime.date(2012, 6, 5),
                    isa10=datetime.time(23, 24),
                    isa11='U',
                    isa12='00401',
                    isa13=Decimal('50033'),
                    isa14='1',
                    isa15='P',
                    isa16='^'),

In order to evaluate this, the entire message
source module must be present. This means using the following

::

    from x12.msg_271_4010_X092_A1 import *
