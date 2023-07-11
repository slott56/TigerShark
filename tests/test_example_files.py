"""
Test the example .txt files

The 837I-Examples.txt appears damaged.
There's no SE,GE, or IEA segments at the end of the first message.
We do not use it as a test case.

"""
import datetime
from decimal import Decimal
from pathlib import Path
from pprint import pprint
from textwrap import dedent

from pytest import fixture, mark

from x12.base import Source, X12Parser
from x12 import msg_271_4010_X092_A1
from x12 import msg_834_5010_X220_A1
from x12 import msg_834_5010_X220_A1_v2
from x12 import msg_835_4010_X091_A1
from x12 import msg_835_5010_X221_A1
from x12 import msg_837_4010_X098_A1
# from x12 import msg_837_4010_X097_A1  # Error -- undefined common attribute C035
from x12 import msg_837_4010_X096_A1
from x12 import msg_837_5010_X222_A1
from x12 import msg_837Q3_I_5010_X223_A1_v2  # Not usable, missing ISA, GS, etc., starts with ST.
from x12 import msg_276_4010_X093_A1
from x12 import msg_278_4010_X094_A1
from x12 import msg_278_4010_X094_27_A1

EXAMPLES = Path.cwd() / "tests"  # Should be run in the parent directory

expected_271_dependent_benefits = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '10864          ',
     datetime.date(2010, 10, 6), datetime.time(9, 31), 'U', '00401', Decimal('418'), '1', 'P', '^'],
    ['GS', 'HB', 'ZIRMED', '10864', datetime.date(2012, 8, 30), datetime.time(9, 31), Decimal('410'), 'X',
     '004010X092A1'],
    ['ST', '271', '0001'],
    ['BHT', '0022', '11', '140', datetime.date(2012, 10, 1), datetime.time(9, 2, 31), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'COMMERCIAL SAMPLE', '', '', '', '', 'PI', '44444', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
    ['HL', '3', '2', '22', '1'],
    ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
    ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
    ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
    ['NM1', 'IL', '1', 'DOE', 'JOHN', 'P', '', '', 'MI', '111111111', None, None],
    ['REF', '6P', '11111', 'ACME MEDICAL, INC'],
    ['HL', '4', '3', '23', '0'],
    ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
    ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
    ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
    ['NM1', '03', '1', 'DOE', 'JANE', None, None, None, None, None, None, None],
    ['REF', '18', '1234567', None],
    ['N3', '3333 SOMEWHERE ST', None],
    ['N4', 'ANYWHERE', 'LA', '71104', None, None, None],
    ['DMG', 'D8', '19370305', 'F', None, None, None, None, None, None],
    ['DTP', '346', 'D8', '20110801'],
    ['DTP', '472', 'D8', '20120928'],
    ['DTP', '307', 'D8', '20110801'],
    ['EB', 'L', 'FAM', '30', 'PS', None, None, None, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['MSG', 'PCP SELECTION NOT REQUIRED', None, None],
    ['EB', 'W', None, None, None, None, None, None, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['LS', '2120'],
    ['NM1', 'PR', '2', 'Aetna', None, None, None, None, None, None, None, None],
    ['N3', 'PO Box 14079', None],
    ['N4', 'Lexington', 'KY', '40512', None, None, None],
    ['LE', '2120'],
    ['EB', '1', 'FAM', '30', 'PS', 'Aetna Choice POS II', None, None, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['EB', 'C', 'FAM', '30', '', '', '23', 600.0, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['DTP', '307', 'D8', '20120101'],
    ['MSG', 'Med Dent', None, None],
    ['MSG', 'LAB OP DIR ACC', None, None],
    ['MSG', 'OP LAB', None, None],
    ['EB', 'C', 'FAM', '30', '', '', '29', 186.89, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['MSG', 'Med Dent', None, None],
    ['EB', 'C', 'FAM', '30', '', '', '23', 600.0, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['DTP', '307', 'D8', '20120101'],
    ['MSG', 'PAP SMEAR', None, None],
    ['EB', 'C', 'IND', '30', '', '', '23', 200.0, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['DTP', '307', 'D8', '20120101'],
    ['MSG', 'Med Dent', None, None],
    ['MSG', 'LAB OP DIR ACC', None, None],
    ['MSG', 'OP LAB', None, None],
    ['EB', 'C', 'IND', '30', '', '', '29', 78.8, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['MSG', 'Med Dent', None, None],
    ['EB', 'C', 'IND', '30', '', '', '23', 200.0, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['DTP', '307', 'D8', '20120101'],
    ['MSG', 'PAP SMEAR', None, None],
    ['EB', 'G', 'IND', '30', '', '', '', 1000.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', '', '', '29', 1000.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', '', '', '', 3000.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', '', '', '29', 3000.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', '1', 'FAM', '5', '', 'Aetna Choice POS II', None, None, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['EB', 'A', 'FAM', '5', '', '', '', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'LAB OP DIR ACC', None, None],
    ['MSG', 'OP LAB', None, None],
    ['MSG', 'PAP SMEAR', None, None],
    ['EB', 'F', 'FAM', '5', '', '', '', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'PAP SMEAR /Plan Ded Waived', None, None],
    ['EB', 'B', 'FAM', '5', '', '', '', 0.0, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['MSG', 'LAB OP DIR ACC', None, None],
    ['MSG', 'OP LAB', None, None],
    ['MSG', 'PAP SMEAR', None, None],
    ['EB', 'F', 'FAM', '5', None, None, None, None, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['MSG', 'Plan Requires PreCert', None, None],
    ['EB', 'F', 'FAM', '5', '', '', '32', None, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['MSG', 'Unlimited Lifetime Benefits', None, None],
    ['EB', 'F', 'FAM', '5', None, None, None, None, None, None, None, None, None,
     [None, None, None, None, None, None, None]],
    ['MSG', 'Self Funded', None, None],
    ['MSG', 'Plan includes NAP', None, None],
    ['EB', 'A', 'FAM', '5', '', '', '', 0.0, 0.3, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['MSG', 'LAB OP DIR ACC', None, None],
    ['MSG', 'COINS APPLIES TO OUT OF POCKET', None, None],
    ['MSG', 'OP LAB', None, None],
    ['MSG', 'PAP SMEAR', None, None],
    ['SE', Decimal('79'), '0001'],
    ['GE', Decimal('1'), Decimal('931')],
    ['IEA', Decimal('1'), Decimal('90132')]
]

def test_271_dependent_benefits() -> None:
    example = EXAMPLES / "271-dependent-benefits.txt"
    document = Source(example.read_text())
    parser = X12Parser(msg_271_4010_X092_A1.MSG271)
    msg = parser.parse(document)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl.hl01)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl.hl03)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl.hl04)
    # print(list(msg.segment_iter()))
    assert list(msg.segment_iter()) == expected_271_dependent_benefits

expected_271_example = [
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
    ['IEA', Decimal('1'), Decimal('50033')]]

def test_271_example(capsys) -> None:
    example = EXAMPLES / "271-example.txt"
    document = Source(example.read_text())
    parser = X12Parser(msg_271_4010_X092_A1.MSG271)
    msg = parser.parse(document)
    # print(list(msg.segment_iter()))
    assert list(msg.segment_iter()) == expected_271_example

    # TODO: Separate test.
    print(msg.json(indent=2))
    json_text, _ = capsys.readouterr()
    assert json_text == dedent("""\
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
    """)

    dict_msg = msg.asdict()
    assert dict_msg == {
        '_kind': 'Message',
         '_name': 'MSG271',
         'isa_loop': [{'_kind': 'Loop',
                       '_name': 'ISA_LOOP',
                       'gs_loop': [{'_kind': 'Loop',
                                    '_name': 'GS_LOOP',
                                    'ge': {'_kind': 'Segment',
                                           '_name': 'GS_LOOP_GE',
                                           'ge01': '1',
                                           'ge02': '50025'},
                                    'gs': {'_kind': 'Segment',
                                           '_name': 'GS_LOOP_GS',
                                           'gs01': 'HB',
                                           'gs02': 'ZIRMED',
                                           'gs03': '12345',
                                           'gs04': {'_format': '%Y%m%d',
                                                    'date': '20120605'},
                                           'gs05': {'_format': '%H%M', 'time': '2324'},
                                           'gs06': '50025',
                                           'gs07': 'X',
                                           'gs08': '004010X092A1'},
                                    'st_loop': [{'_kind': 'Loop',
                                                 '_name': 'ST_LOOP',
                                                 'detail': [{'_kind': 'Loop',
                                                             '_name': 'DETAIL',
                                                             'l2000a': [{'_kind': 'Loop',
                                                                         '_name': 'L2000A',
                                                                         'hl': {'_kind': 'Segment',
                                                                                '_name': 'L2000A_HL',
                                                                                'hl01': '1',
                                                                                'hl02': '',
                                                                                'hl03': '20',
                                                                                'hl04': '1'},
                                                                         'l2000b': [{'_kind': 'Loop',
                                                                                     '_name': 'L2000B',
                                                                                     'hl': {'_kind': 'Segment',
                                                                                            '_name': 'L2000B_HL',
                                                                                            'hl01': '2',
                                                                                            'hl02': '1',
                                                                                            'hl03': '21',
                                                                                            'hl04': '1'},
                                                                                     'l2000c': [{'_kind': 'Loop',
                                                                                                 '_name': 'L2000C',
                                                                                                 'hl': {'_kind': 'Segment',
                                                                                                        '_name': 'L2000C_HL',
                                                                                                        'hl01': '3',
                                                                                                        'hl02': '2',
                                                                                                        'hl03': '22',
                                                                                                        'hl04': '0'},
                                                                                                 'l2100c': [
                                                                                                     {'_kind': 'Loop',
                                                                                                      '_name': 'L2100C',
                                                                                                      'aaa': [{
                                                                                                                  '_kind': 'Segment',
                                                                                                                  '_name': 'L2100C_AAA',
                                                                                                                  'aaa01': 'N',
                                                                                                                  'aaa02': '',
                                                                                                                  'aaa03': '72',
                                                                                                                  'aaa04': 'C'},
                                                                                                              {
                                                                                                                  '_kind': 'Segment',
                                                                                                                  '_name': 'L2100C_AAA',
                                                                                                                  'aaa01': 'N',
                                                                                                                  'aaa02': '',
                                                                                                                  'aaa03': '73',
                                                                                                                  'aaa04': 'C'},
                                                                                                              {
                                                                                                                  '_kind': 'Segment',
                                                                                                                  '_name': 'L2100C_AAA',
                                                                                                                  'aaa01': 'N',
                                                                                                                  'aaa02': '',
                                                                                                                  'aaa03': '73',
                                                                                                                  'aaa04': 'C'},
                                                                                                              {
                                                                                                                  '_kind': 'Segment',
                                                                                                                  '_name': 'L2100C_AAA',
                                                                                                                  'aaa01': 'N',
                                                                                                                  'aaa02': '',
                                                                                                                  'aaa03': '58',
                                                                                                                  'aaa04': 'C'}],
                                                                                                      'dtp': [{
                                                                                                                  '_kind': 'Segment',
                                                                                                                  '_name': 'L2100C_DTP',
                                                                                                                  'dtp01': '291',
                                                                                                                  'dtp02': 'D8',
                                                                                                                  'dtp03': '20120408'}],
                                                                                                      'nm1': {
                                                                                                          '_kind': 'Segment',
                                                                                                          '_name': 'L2100C_NM1',
                                                                                                          'nm101': 'IL',
                                                                                                          'nm102': '1',
                                                                                                          'nm103': '',
                                                                                                          'nm104': '',
                                                                                                          'nm105': '',
                                                                                                          'nm106': '',
                                                                                                          'nm107': '',
                                                                                                          'nm108': 'MI',
                                                                                                          'nm109': 'R11111111'}}],
                                                                                                 'trn': [
                                                                                                     {'_kind': 'Segment',
                                                                                                      '_name': 'L2000C_TRN',
                                                                                                      'trn01': '1',
                                                                                                      'trn02': '222222222',
                                                                                                      'trn03': '9ZIRMEDCOM',
                                                                                                      'trn04': 'ELR '
                                                                                                               'ID'},
                                                                                                     {'_kind': 'Segment',
                                                                                                      '_name': 'L2000C_TRN',
                                                                                                      'trn01': '2',
                                                                                                      'trn02': '333333333',
                                                                                                      'trn03': '9ZIRMEDCOM',
                                                                                                      'trn04': 'ELI '
                                                                                                               'ID'},
                                                                                                     {'_kind': 'Segment',
                                                                                                      '_name': 'L2000C_TRN',
                                                                                                      'trn01': '1',
                                                                                                      'trn02': '4444444444',
                                                                                                      'trn03': '9MEDDATACO'}]}],
                                                                                     'l2100b': [{'_kind': 'Loop',
                                                                                                 '_name': 'L2100B',
                                                                                                 'nm1': {'_kind': 'Segment',
                                                                                                         '_name': 'L2100B_NM1',
                                                                                                         'nm101': '1P',
                                                                                                         'nm102': '2',
                                                                                                         'nm103': 'DR. '
                                                                                                                  'ACULA',
                                                                                                         'nm104': '',
                                                                                                         'nm105': '',
                                                                                                         'nm106': '',
                                                                                                         'nm107': '',
                                                                                                         'nm108': 'XX',
                                                                                                         'nm109': '1111111111'}}]}],
                                                                         'l2100a': [{'_kind': 'Loop',
                                                                                     '_name': 'L2100A',
                                                                                     'nm1': {'_kind': 'Segment',
                                                                                             '_name': 'L2100A_NM1',
                                                                                             'nm101': 'PR',
                                                                                             'nm102': '2',
                                                                                             'nm103': 'Health '
                                                                                                      'Net '
                                                                                                      'Inc',
                                                                                             'nm104': '',
                                                                                             'nm105': '',
                                                                                             'nm106': '',
                                                                                             'nm107': '',
                                                                                             'nm108': 'PI',
                                                                                             'nm109': '10385'}}]}]}],
                                                 'header': [{'_kind': 'Loop',
                                                             '_name': 'HEADER',
                                                             'bht': {'_kind': 'Segment',
                                                                     '_name': 'HEADER_BHT',
                                                                     'bht01': '0022',
                                                                     'bht02': '11',
                                                                     'bht03': '11111',
                                                                     'bht04': {'_format': '%Y%m%d',
                                                                               'date': '20120605'},
                                                                     'bht05': {'_format': '%H%M',
                                                                               'time': '2324'}}}],
                                                 'se': {'_kind': 'Segment',
                                                        '_name': 'ST_LOOP_SE',
                                                        'se01': '17',
                                                        'se02': '0001'},
                                                 'st': {'_kind': 'Segment',
                                                        '_name': 'ST_LOOP_ST',
                                                        'st01': '271',
                                                        'st02': '0001'}}]}],
                       'iea': {'_kind': 'Segment',
                               '_name': 'ISA_LOOP_IEA',
                               'iea01': '1',
                               'iea02': '50033'},
                       'isa': {'_kind': 'Segment',
                               '_name': 'ISA_LOOP_ISA',
                               'isa01': '00',
                               'isa02': '          ',
                               'isa03': '00',
                               'isa04': '          ',
                               'isa05': 'ZZ',
                               'isa06': 'ZIRMED         ',
                               'isa07': 'ZZ',
                               'isa08': '12345          ',
                               'isa09': {'_format': '%Y%m%d', 'date': '20120605'},
                               'isa10': {'_format': '%H%M', 'time': '2324'},
                               'isa11': 'U',
                               'isa12': '00401',
                               'isa13': '50033',
                               'isa14': '1',
                               'isa15': 'P',
                               'isa16': '^'}}]
    }

    repr_msg = repr(msg)
    assert repr_msg == (
        "MSG271(isa_loop=[ISA_LOOP(isa=ISA_LOOP_ISA(isa01='00', isa02='          ', "
         "isa03='00', isa04='          ', isa05='ZZ', isa06='ZIRMED         ', "
         "isa07='ZZ', isa08='12345          ', isa09=datetime.date(2012, 6, 5), "
         "isa10=datetime.time(23, 24), isa11='U', isa12='00401', "
         "isa13=Decimal('50033'), isa14='1', isa15='P', isa16='^'), "
         "gs_loop=[GS_LOOP(gs=GS_LOOP_GS(gs01='HB', gs02='ZIRMED', gs03='12345', "
         'gs04=datetime.date(2012, 6, 5), gs05=datetime.time(23, 24), '
         "gs06=Decimal('50025'), gs07='X', gs08='004010X092A1'), "
         "st_loop=[ST_LOOP(st=ST_LOOP_ST(st01='271', st02='0001'), "
         "header=[HEADER(bht=HEADER_BHT(bht01='0022', bht02='11', bht03='11111', "
         'bht04=datetime.date(2012, 6, 5), bht05=datetime.time(23, 24, 23), '
         "bht06=None))], detail=[DETAIL(l2000a=[L2000A(hl=L2000A_HL(hl01='1', hl02='', "
         "hl03='20', hl04='1'), aaa=None, l2100a=[L2100A(nm1=L2100A_NM1(nm101='PR', "
         "nm102='2', nm103='Health Net Inc', nm104='', nm105='', nm106='', nm107='', "
         "nm108='PI', nm109='10385', nm110=None, nm111=None), ref=None, per=None, "
         "aaa=None)], l2000b=[L2000B(hl=L2000B_HL(hl01='2', hl02='1', hl03='21', "
         "hl04='1'), l2100b=[L2100B(nm1=L2100B_NM1(nm101='1P', nm102='2', nm103='DR. "
         "ACULA', nm104='', nm105='', nm106='', nm107='', nm108='XX', "
         "nm109='1111111111', nm110=None, nm111=None), ref=None, aaa=None)], "
         "l2000c=[L2000C(hl=L2000C_HL(hl01='3', hl02='2', hl03='22', hl04='0'), "
         "trn=[L2000C_TRN(trn01='1', trn02='222222222', trn03='9ZIRMEDCOM', trn04='ELR "
         "ID'), L2000C_TRN(trn01='2', trn02='333333333', trn03='9ZIRMEDCOM', "
         "trn04='ELI ID'), L2000C_TRN(trn01='1', trn02='4444444444', "
         "trn03='9MEDDATACO', trn04=None)], l2100c=[L2100C(nm1=L2100C_NM1(nm101='IL', "
         "nm102='1', nm103='', nm104='', nm105='', nm106='', nm107='', nm108='MI', "
         "nm109='R11111111', nm110=None, nm111=None), ref=None, n3=None, n4=None, "
         "per=None, aaa=[L2100C_AAA(aaa01='N', aaa02='', aaa03='72', aaa04='C'), "
         "L2100C_AAA(aaa01='N', aaa02='', aaa03='73', aaa04='C'), "
         "L2100C_AAA(aaa01='N', aaa02='', aaa03='73', aaa04='C'), "
         "L2100C_AAA(aaa01='N', aaa02='', aaa03='58', aaa04='C')], dmg=None, ins=None, "
         "dtp=[L2100C_DTP(dtp01='291', dtp02='D8', dtp03='20120408')], l2110c=None)], "
         "l2000d=None)])])])], footer=None, se=ST_LOOP_SE(se01=Decimal('17'), "
         "se02='0001'))], ge=GS_LOOP_GE(ge01=Decimal('1'), ge02=Decimal('50025')))], "
         "ta1=None, iea=ISA_LOOP_IEA(iea01=Decimal('1'), iea02=Decimal('50033')))])")

expected_271_example_2 = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '10864          ', datetime.date(2010, 10, 6), datetime.time(9, 31), 'U', '00401', Decimal('418'), '1', 'P', '^'],
    ['GS', 'HB', 'ZIRMED', '10864', datetime.date(2012, 8, 30), datetime.time(9, 31), Decimal('410'), 'X', '004010X092A1'],
    ['ST', '271', '0001'],
    ['BHT', '0022', '11', '140', datetime.date(2012, 8, 30), datetime.time(9, 31, 22), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'COMMERCIAL SAMPLE', '', '', '', '', 'PI', '44444', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
    ['HL', '3', '2', '22', '0'],
    ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
    ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
    ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
    ['NM1', 'IL', '1', 'DOE', 'JANET', '', '', '', 'MI', '111111111', None, None],
    ['REF', '6P', '00000', None],
    ['N3', '3333 SOMEWHERE ST', None],
    ['N4', 'ANYWHERE', 'LA', '71104', None, None, None],
    ['DMG', 'D8', '19370305', 'F', None, None, None, None, None, None],
    ['INS', 'Y', '18', '001', '25', '', '', '', '', '', '', '', '', '', '', '', '', Decimal('1')],
    ['DTP', '307', 'D8', '20050201'],
    ['EB', '1', '', '30', 'C1', 'MANAGED INDEMNITY', None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['LS', '2120'],
    ['NM1', 'PR', '2', 'UNITEDHEALTHCARE', None, None, None, None, None, None, None, None],
    ['N3', 'P.O. BOX 740800', 'P.O. BOX 740800'],
    ['N4', 'ATLANTA', 'GA', '303740800', None, None, None],
    ['LE', '2120'],
    ['EB', 'G', 'FAM', '30', 'C1', '', '', 3000.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', 'C1', '', '24', 3025.9, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', 'C1', '', '29', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'FAM', '30', '', '', '', 236.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'FAM', '30', '', '', '24', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'FAM', '30', '', '', '29', 236.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', 'C1', '', '', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', 'C1', '', '24', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', 'C1', '', '29', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'FAM', '30', '', '', '', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'FAM', '30', '', '', '24', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'FAM', '30', '', '', '29', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', 'C1', '', '', 1500.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', 'C1', '', '24', 1500.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', 'C1', '', '29', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'IND', '30', '', '', '', 118.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'IND', '30', '', '', '24', 118.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'IND', '30', '', '', '29', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', 'C1', '', '', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', 'C1', '', '24', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', 'C1', '', '29', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'IND', '30', '', '', '', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'IND', '30', '', '', '24', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'C', 'IND', '30', '', '', '29', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'I', '', '35', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'I', '', '92', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'I', '', '91', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'I', '', '88', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', '1', '', 'AE', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', 'AE', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', 'AE', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', 'AL', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', 'AL', '', '', '27', 0.0, 1.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', 'AL', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', 'A4', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', 'A4', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', 'A4', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', 'A6', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', 'A6', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', 'A6', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', 'A7', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', 'A7', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', 'A7', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', 'A8', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', 'A8', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', 'A8', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '1', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '1', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '1', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '2', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '2', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '2', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '4', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '4', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '4', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '5', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '5', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '5', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '7', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '7', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '7', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '9', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '9', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '9', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '12', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '12', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '12', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '13', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '13', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '13', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '47', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '47', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '47', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '48', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '48', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '48', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '50', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '50', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '50', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '52', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '52', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '52', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '53', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '53', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '53', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '60', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '60', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '60', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '68', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '68', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '68', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '81', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '81', '', '', '27', 0.0, 0.1, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '81', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '86', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '86', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '86', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '96', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'A', 'IND', '96', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', 'IND', '96', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', '1', '', '98', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['MSG', 'OFFICE VISIT', None, None],
    ['EB', 'A', 'IND', '98', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'OFFICE VISIT', None, None],
    ['EB', 'B', 'IND', '98', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'OFFICE VISIT', None, None],
    ['EB', '1', '', '98', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['MSG', 'PRIMARY CARE PHYSICIAN', None, None],
    ['EB', 'A', 'IND', '98', '', '', '27', 0.0, 0.2, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'PRIMARY CARE PHYSICIAN', None, None],
    ['EB', 'B', 'IND', '98', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'PRIMARY CARE PHYSICIAN', None, None],
    ['EB', 'R', '', '30', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['LS', '2120'],
    ['NM1', 'PR', '2', 'MEDICARE', None, None, None, None, None, None, None, None],
    ['LE', '2120'],
    ['EB', 'X', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['LS', '2120'],
    ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
    ['LE', '2120'],
    ['SE', Decimal('144'), '0001'],
    ['GE', Decimal('1'), Decimal('410')],
    ['IEA', Decimal('1'), Decimal('418')],
]

def test_271_example_2() -> None:
    example = EXAMPLES / "271-example-2.txt"
    document = Source(example.read_text())
    parser = X12Parser(msg_271_4010_X092_A1.MSG271)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_271_example_2

expected_271_dependent_rejection = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '12345          ',
     datetime.date(2012, 6, 29), datetime.time(17, 45), 'U', '00401', Decimal('59247'), '1', 'P', '^'],
    ['GS', 'HB', 'ZIRMED', '12345', datetime.date(2012, 6, 29), datetime.time(17, 45), Decimal('59239'), 'X',
     '004010X092A1'],
    ['ST', '271', '0001'],
    ['BHT', '0022', '11', '58446', datetime.date(2012, 6, 29), datetime.time(17, 45, 29), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'ANTHEM BLUE CROSS', '', '', '', '', 'PI', '10319', None, None],
    ['PER', 'IC', 'BLUECARD ELIGIBILITY', 'TE', '8006762583', None, None, None, None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '2', 'DR. SPACEMAN', '', '', '', '', 'XX', '1111111111', None, None],
    ['HL', '3', '2', '22', '1'],
    ['TRN', '1', '222222222', '9ZIRMEDCOM', 'ELR ID'],
    ['TRN', '2', '333333333', '9ZIRMEDCOM', 'ELI ID'],
    ['TRN', '1', '4444444444', '9MEDDATACO', None],
    ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'R11111111', None, None],
    ['AAA', 'Y', '', '72', 'N'],
    ['HL', '4', '3', '23', '0'],
    ['TRN', '1', '222222222', '9ZIRMEDCOM', 'ELR ID'],
    ['TRN', '2', '333333333', '9ZIRMEDCOM', 'ELI ID'],
    ['TRN', '1', '4444444444', '9MEDDATACO', None],
    ['NM1', '03', '1', 'DOE', 'JANE', None, None, None, None, None, None, None],
    ['DMG', 'D8', '19810810', None, None, None, None, None, None, None],
    ['SE', Decimal('20'), '0001'],
    ['GE', Decimal('1'), Decimal('59239')],
    ['IEA', Decimal('1'), Decimal('59247')],
]


def test_271_dependent_rejection() -> None:
    example = EXAMPLES / "271-example-dependent-rejection.txt"
    document = Source(example.read_text())
    parser = X12Parser(msg_271_4010_X092_A1.MSG271)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_271_dependent_rejection

expected_271_related_entity = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '10864          ', datetime.date(2012, 9, 27), datetime.time(14, 3), 'U', '00401', Decimal('89573'), '1', 'P', '^'],
    ['GS', 'HB', 'ZIRMED', '10864', datetime.date(2012, 9, 27), datetime.time(14, 3), Decimal('89565'), 'X', '004010X092A1'],
    ['ST', '271', '0001'],
    ['BHT', '0022', '11', '11111', datetime.date(2012, 9, 27), datetime.time(14, 3, 33), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'COMMERCIAL SAMPLE', '', '', '', '', 'PI', '44444', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
    ['HL', '3', '2', '22', '1'],
    ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
    ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
    ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
    ['NM1', 'IL', '1', 'DOE', 'JOHN', 'P', '', '', 'MI', '111111111', None, None],
    ['REF', '3H', '0GEU', None],
    ['INS', 'Y', '18', '001', '25', None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['HL', '4', '3', '23', '0'],
    ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
    ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
    ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
    ['NM1', '03', '1', 'DOE', 'JANE', None, None, None, None, None, None, None],
    ['REF', '6P', '55555G', 'CEDARS-SINAI HEALTH SYSTEM'],
    ['REF', 'IF', 'HVU', None],
    ['DMG', 'D8', '19370305', 'F', None, None, None, None, None, None],
    ['DTP', '291', 'RD8', '20120101-99991231'],
    ['EB', '1', 'ESP', '30', 'HM', 'HMO CEDARS SINAI ONLY', None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['EB', 'G', 'FAM', '30', '', '', '23', 1000.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'TWO PARTY COPAY MAXIMUM', None, None],
    ['EB', 'G', 'FAM', '30', '', '', '29', 870.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'TWO PARTY COPAY MAXIMUM', None, None],
    ['EB', 'G', 'FAM', '30', '', '', '23', 1500.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'COPAY MAXIMUM', None, None],
    ['EB', 'G', 'FAM', '30', '', '', '29', 1370.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'G', 'IND', '30', '', '', '23', 500.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'SINGLE PARTY COPAY MAXIMUM', None, None],
    ['EB', 'G', 'IND', '30', '', '', '29', 460.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['EB', 'B', '', '5', '', '', '26', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'FETAL GENETIC', None, None],
    ['EB', 'B', '', '5', '', '', '27', 0.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'BLOOD LEAD SCREENING', None, None],
    ['MSG', 'MAMMOGRAPHY', None, None],
    ['MSG', 'PAP/CERVICAL CANCER SCREEN', None, None],
    ['MSG', 'PROSTATE SCREEN', None, None],
    ['EB', 'B', '', '5', '', '', '27', 20.0, 0.0, '', 0.0, '', 'Y', [None, None, None, None, None, None, None]],
    ['MSG', 'ALLERGY TESTING', None, None],
    ['MSG', 'MAMMOGRAM ROUTINE COPAY', None, None],
    ['EB', 'I', '', '5', '', '', '', 0.0, 0.0, '', 0.0, '', 'N', [None, None, None, None, None, None, None]],
    ['EB', 'N', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['DTP', '295', 'RD8', '20110701-99991231'],
    ['LS', '2120'],
    ['N3', '123 RELATED ST # 1', None],
    ['N4', 'ANYTOWN', 'CA', '902101234', None, None, None],
    ['PER', 'IC', '', 'TE', '8005554160', None, None, None, None, None],
    ['LE', '2120'],
    ['EB', 'L', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['DTP', '295', 'RD8', '20110701-99991231'],
    ['LS', '2120'],
    ['NM1', '36', '2', 'EMPLOYER', None, None, None, None, None, None, None, None],
    ['N3', '123 RELATED ST # 2', None],
    ['N4', 'ANYTOWN', 'WA', '98101', None, None, None],
    ['PER', 'IC', '', 'TE', '2065551234', None, None, None, None, None],
    ['LE', '2120'],
    ['EB', 'P', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
    ['MSG', 'UNLESS OTHERWISE REQUIRED BY STATE LAW, THIS NOTICE IS NOT A GUARANTEE OF PAYMENT. BENEFITS ARE SUBJECT TO ALL CONTRACT LIMITATIONS AND THE MEMBERS ELIGIBILITY STATUS ON THE DATE OF SERVICE. FOR ANY QUESTIONS PLEASE CALL PHONE NUMBER ON BACK OF MEMBERS CARD.', None, None],
    ['SE', Decimal('77'), '0001'],
    ['GE', Decimal('1'), Decimal('89565')],
    ['IEA', Decimal('1'), Decimal('89573')],
]


def test_271_related_entity() -> None:
    example = EXAMPLES / "271-related-entity.txt"
    document = Source(example.read_text())
    parser = X12Parser(msg_271_4010_X092_A1.MSG271)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_271_related_entity


expected_834_example = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'D00XXX         ', 'ZZ', '00AA           ', datetime.date(2007, 3, 5), datetime.time(18, 32), '^', '00501', Decimal('676048320'), '0', 'P', '\\'],
    ['GS', 'BE', 'D00XXX', '00AA', datetime.date(2015, 3, 5), datetime.time(18, 32), Decimal('260007982'), 'X', '005010X220A1'],
    ['ST', '834', '0001', '005010X220A1'],
    ['BGN', '00', '88880070301  00', datetime.date(2015, 3, 5), datetime.time(18, 12, 45), '', '', '', '4', None],
    ['DTP', '007', 'D8', '20150301'],
    ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
    ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
    ['INS', 'Y', '18', '030', 'XN', 'A', ['C   ', None, None, None], '', 'FT', None, None, None, None, None, None, None, None, None],
    ['REF', '0F', '00389999', None],
    ['REF', '1L', '000003409999', None],
    ['REF', '3H', 'K129999A', None],
    ['DTP', '356', 'D8', '20150301'],
    ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
    ['N3', '777 ELM ST', None],
    ['N4', 'ALLEGAN', 'MI', '49010', '', 'CY', '03', None],
    ['DMG', 'D8', '19670330', 'M', '', [['O', None, None]], None, None, None, None, None, None],
    ['LUI', '', '', 'ESSPANISH', None, None],
    ['HD', '030', '', 'AK', '064703', 'IND', None, None, None, None, None, None],
    ['DTP', '348', 'D8', '20150301'],
    ['AMT', 'P3', 45.34, None],
    ['REF', '17', 'E  1F', None],
    ['SE', Decimal('20'), '0001'],
    ['GE', Decimal('1'), Decimal('260007982')],
    ['IEA', Decimal('1'), Decimal('676048320')],
]


def test_834_example() -> None:
    example = EXAMPLES / "834-example.txt"
    document = Source(example.read_text())
    # A few validation errors.
    # Bad example? Wrong message class definition? Don't know.
    errors_here = [
        "*_N1:n101:Enumerated",
        "*_INS:ins06_01:MaxLen",
        "*_INS:ins06_01:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_DMG:dmg06:Enumerated"]
    parser = X12Parser(msg_834_5010_X220_A1.MSG834A1, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_834_example

expected_834_example_2 = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'D00XXX         ', 'ZZ', '00AA           ', datetime.date(2007, 3, 5), datetime.time(18, 32), 'U', '00501', Decimal('701336'), '0', 'P', ':'],
    ['GS', 'BE', 'D00XXX', '00AA', datetime.date(2007, 3, 5), datetime.time(18, 32), Decimal('13360001'), 'X', '005010X220A1'],
    ['ST', '834', '0001', '005010X220A1'],
    ['BGN', '00', '88880070301  00', datetime.date(2007, 3, 5), datetime.time(18, 12, 45), '', '', '', '4', None],
    ['DTP', '007', 'D8', '20070301'],
    ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
    ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
    ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], '', 'FT', None, None, None, None, None, None, None, None, None],
    ['REF', '0F', '00389999', None],
    ['REF', '1L', '000003409999', None],
    ['REF', '3H', 'K129999A', None],
    ['DTP', '356', 'D8', '20070301'],
    ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
    ['N3', '777 ELM ST', None],
    ['N4', 'ALLEGAN', 'MI', '49010', '', 'CY', '03', None],
    ['DMG', 'D8', '19670330', 'M', '', [['O', None, None]], None, None, None, None, None, None],
    ['LUI', '', '', 'ESSPANISH', None, None],
    ['HD', '030', '', 'AK', '064703', 'IND', None, None, None, None, None, None],
    ['DTP', '348', 'D8', '20070301'],
    ['AMT', 'P3', 45.34, None],
    ['REF', '17', 'E  1F', None],
    ['SE', Decimal('20'), '0001'],
    ['ST', '834', '0002', '005010X220A1'],
    ['BGN', '00', '88880070301  00', datetime.date(2007, 3, 5), datetime.time(18, 12, 45), '', '', '', '4', None],
    ['DTP', '007', 'D8', '20070301'],
    ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
    ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
    ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], '', 'FT', None, None, None, None, None, None, None, None, None],
    ['REF', '0F', '00389999', None],
    ['REF', '1L', '000003409999', None],
    ['REF', '3H', 'K129999A', None],
    ['DTP', '356', 'D8', '20070301'],
    ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
    ['N3', '777 ELM ST', None],
    ['N4', 'ALLEGAN', 'MI', '49010', '', 'CY', '03', None],
    ['DMG', 'D8', '19670330', 'M', '', [['O', None, None]], None, None, None, None, None, None],
    ['LUI', '', '', 'ESSPANISH', None, None],
    ['HD', '030', '', 'AK', '064703', 'IND', None, None, None, None, None, None],
    ['DTP', '348', 'D8', '20070301'],
    ['AMT', 'P3', 45.34, None],
    ['REF', '17', 'E  1F', None],
    ['SE', Decimal('20'), '0002'],
    ['ST', '834', '0003', '005010X220A1'],
    ['BGN', '00', '88880070301  00', datetime.date(2007, 3, 5), datetime.time(18, 12, 45), '', '', '', '4', None],
    ['DTP', '007', 'D8', '20070301'],
    ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
    ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
    ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], '', 'FT', None, None, None, None, None, None, None, None, None],
    ['REF', '0F', '00389999', None],
    ['REF', '1L', '000003409999', None],
    ['REF', '3H', 'K129999A', None],
    ['DTP', '356', 'D8', '20070301'],
    ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
    ['N3', '777 ELM ST', None],
    ['N4', 'ALLEGAN', 'MI', '49010', '', 'CY', '03', None],
    ['DMG', 'D8', '19670330', 'M', '', [['O', None, None]], None, None, None, None, None, None],
    ['LUI', '', '', 'ESSPANISH', None, None],
    ['HD', '030', '', 'AK', '064703', 'IND', None, None, None, None, None, None],
    ['DTP', '348', 'D8', '20070301'],
    ['AMT', 'P3', 45.34, None],
    ['REF', '17', 'E  1F', None],
    ['SE', Decimal('20'), '0003'],
    ['ST', '834', '0004', '005010X220A1'],
    ['BGN', '00', '88880070301  00', datetime.date(2007, 3, 5), datetime.time(18, 12, 45), '', '', '', '4', None],
    ['DTP', '007', 'D8', '20070301'],
    ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
    ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
    ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], '', 'FT', None, None, None, None, None, None, None, None, None],
    ['REF', '0F', '00389999', None],
    ['REF', '1L', '000003409999', None],
    ['REF', '3H', 'K129999A', None],
    ['DTP', '356', 'D8', '20070301'],
    ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
    ['N3', '777 ELM ST', None],
    ['N4', 'ALLEGAN', 'MI', '49010', '', 'CY', '03', None],
    ['DMG', 'D8', '19670330', 'M', '', [['O', None, None]], None, None, None, None, None, None],
    ['LUI', '', '', 'ESSPANISH', None, None],
    ['HD', '030', '', 'AK', '064703', 'IND', None, None, None, None, None, None],
    ['DTP', '348', 'D8', '20070301'],
    ['AMT', 'P3', 45.34, None],
    ['REF', '17', 'E  1F', None],
    ['SE', Decimal('20'), '0004'],
    ['GE', Decimal('4'), Decimal('13360001')],
    ['IEA', Decimal('1'), Decimal('000701336')],
]


def test_834_example_2() -> None:
    example = EXAMPLES / "834-example-2.txt"
    document = Source(example.read_text())
    errors_here = [
        "*_N1:n101:Enumerated",
        "*_REF:ref01:Enumerated",
    ]
    parser = X12Parser(msg_834_5010_X220_A1.MSG834A1, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_834_example_2

expected_835_example = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'MYCLEARINGHOUSE', 'ZZ', 'RECVCODE       ', datetime.date(2012, 3, 23), datetime.time(19, 38), 'U', '00401', Decimal('000015442'), '1', 'P', '^'],
    ['GS', 'HP', 'MYCLEARINGHOUSE', 'RECVCODE', datetime.date(2012, 3, 23), datetime.time(19, 38), Decimal('15555'), 'X', '004010X091A1'],
    ['ST', '835', '0001'],
    ['BPR', 'I', 12345.67, 'C', 'ACH', 'CCP', '01', '999999999', 'DA', '1234567890', '1111111111', '000011111', '01', '222222222', 'DA', '3333333333', datetime.date(2012, 3, 22), None, None, None, None, None],
    ['TRN', '1', '1QG11111111', '1111111111', '000011111'],
    ['DTM', '405', datetime.date(2012, 3, 19), None, None, None, None],
    ['N1', 'PR', 'UNITED HEALTHCARE INSURANCE COMPANY', 'XV', '87726', None, None],
    ['N3', '9900 BREN ROAD', None],
    ['N4', 'MINNETONKA', 'MN', '553430000', None, None, None],
    ['REF', '2U', '87726', None],
    ['PER', 'CX', 'ATLANTA SERVICE CENTER', 'TE', '8778423210', None, None, None, None, None],
    ['N1', 'PE', 'MY CLINIC', 'XX', '1333333333', None, None],
    ['N3', '123 HEALTHCARE STREET', None],
    ['N4', 'SAN FRANCISCO', 'CA', '94109', None, None, None],
    ['REF', 'TJ', '777777777', None],
    ['LX', Decimal('1')],
    ['TS3', '1333333333', '81',  datetime.date(2012, 12, 31), 2.0, 23456.78, 12345.67, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['CLP', '001-DDDDDDDDDD', '1', 200.02, 200.02, 0.0, '13', '1234567890 0987654321', '81', None, None, None, None, None],
    ['NM1', 'QC', '1', 'DOE', 'JOHN', None, None, None, None, None, None, None],
    ['NM1', 'IL', '1', 'DOE', 'JANE', '', '', '', 'MI', '123111111', None, None],
    ['NM1', '74', '1', 'DOE', 'JANE', 'D', None, None, None, None, None, None],
    ['NM1', '82', '2', 'MY CLINIC', '', '', '', '', 'XX', '1333333333', None, None],
    ['REF', 'CE', 'CHOYC+', None],
    ['REF', '1L', '5G5G5G', None],
    ['DTM', '232', datetime.date(2012, 2, 22), None, None, None, None],
    ['AMT', 'AU', 200.02, None],
    ['SVC', ['HC', '88888', None, None, None, None, None], 200.02, 200.02, '', 1.0, None],
    ['DTM', '472',  datetime.date(2012, 2, 22), None, None, None, None],
    ['REF', '6R', '251111111111', None],
    ['AMT', 'B6', 200.02, None],
    ['CLP', '001-SSSSSSSSSS', '1', 23276.56, 12000.65, 145.0, '14', '2234567890 0987654322', '81', None, None, None, None, None],
    ['CAS', 'PR', '1', 145.0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'SMITH', 'JOHN', None, None, None, None, None, None, None],
    ['NM1', 'IL', '1', 'SMITH', 'JANE', '', '', '', 'MI', '123222222', None, None],
    ['NM1', '74', '1', 'SMITH', 'JANE', 'A', None, None, None, None, None, None],
    ['REF', 'CE', 'CHOYC', None],
    ['REF', '1L', '717171', None],
    ['DTM', '050', datetime.date(2012, 3, 3), None, None, None, None],
    ['DTM', '232', datetime.date(2012, 2, 23), None, None, None, None],
    ['AMT', 'AU', 12145.65, None],
    ['SVC', ['HC', '88888', None, None, None, None, None], 23276.56, 12145.65, '', 1.0, None],
    ['DTM', '472', datetime.date(2012, 2, 21), None, None, None, None],
    ['CAS', 'CO', '45', 11130.91, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['REF', '6R', '252222222222', None],
    ['AMT', 'B6', 12145.65, None],
    ['LQ', 'HE', 'N220'],
    ['LQ', 'HE', 'M68'],
    ['PLB', '743238060', datetime.date(2012, 12, 31), ['WO', '12104411559120820 001GAL295513'], -361.19, None, None, None, None, None],
    ['SE', Decimal('43'), '0001'],
    ['GE', Decimal('1'), Decimal('15555')],
    ['IEA', Decimal('1'), Decimal('000015442')],
]


def test_835_example() -> None:
    example = EXAMPLES / "835-example.txt"
    document = Source(example.read_text())
    # Bad example? Wrong message class definition? Don't know.
    errors_here = [
        "*_N1:n101:Enumerated", "*_N1:n103:Enumerated", "*_REF:ref01:Enumerated",
        "*_NM1:nm101:Enumerated", "*_NM1:nm102:Enumerated", "*_NM1:nm108:Enumerated"
    ]
    parser = X12Parser(msg_835_4010_X091_A1.MSG835, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_835_example

expected_835_example_2 = [
    ['ISA', '00', '          ', '00', '          ', 'ZZ', 'MYCLEARINGHOUSE', 'ZZ', 'RECVCODE       ', datetime.date(2012, 3, 23), datetime.time(19, 38), 'U', '00401', Decimal('000015442'), '1', 'P', '^'],
    ['GS', 'HP', 'MYCLEARINGHOUSE', 'RECVCODE', datetime.date(2012, 3, 23), datetime.time(19, 38), Decimal('15555'), 'X', '004010X091A1'],
    ['ST', '835', '0001'],
    ['BPR', 'I', 12345.67, 'C', 'ACH', 'CCP', '01', '999999999', 'DA', '1234567890', '1111111111', '000011111', '01', '222222222', 'DA', '3333333333', datetime.date(2012, 3, 22), None, None, None, None, None],
    ['TRN', '1', '1QG11111111', '1111111111', '000011111'],
    ['DTM', '405', datetime.date(2012, 3, 19), None, None, None, None],
    ['N1', 'PR', 'UNITED HEALTHCARE INSURANCE COMPANY', 'XV', '87726', None, None],
    ['N3', '9900 BREN ROAD', None],
    ['N4', 'MINNETONKA', 'MN', '553430000', None, None, None],
    ['REF', '2U', '87726', None],
    ['PER', 'CX', 'ATLANTA SERVICE CENTER', 'TE', '8778423210', None, None, None, None, None],
    ['N1', 'PE', 'MY CLINIC', 'XX', '1333333333', None, None],
    ['N3', '123 HEALTHCARE STREET', None],
    ['N4', 'SAN FRANCISCO', 'CA', '94109', None, None, None],
    ['REF', 'TJ', '777777777', None],
    ['LX', Decimal('1')],
    ['TS3', '1333333333', '81', datetime.date(2012, 12, 31), 1.0, 200.02, 200.02, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['CLP', '001-DDDDDDDDDD', '1', 200.02, 200.02, 0.0, '13', '1234567890 0987654321', '81', None, None, None, None, None],
    ['NM1', 'QC', '1', 'DOE', 'JOHN', None, None, None, None, None, None, None],
    ['NM1', 'IL', '1', 'DOE', 'JANE', '', '', '', 'MI', '123111111', None, None],
    ['NM1', '74', '1', 'DOE', 'JANE', 'D', None, None, None, None, None, None],
    ['NM1', '82', '2', 'MY CLINIC', '', '', '', '', 'XX', '1333333333', None, None],
    ['REF', 'CE', 'CHOYC+', None],
    ['REF', '1L', '5G5G5G', None],
    ['DTM', '232', datetime.date(2012, 2, 22), None, None, None, None],
    ['AMT', 'AU', 200.02, None],
    ['SVC', ['HC', '88888', None, None, None, None, None], 200.02, 200.02, '', 1.0, None],
    ['DTM', '472', datetime.date(2012, 2, 22), None, None, None, None],
    ['REF', '6R', '251111111111', None],
    ['AMT', 'B6', 200.02, None],
    ['SE', Decimal('28'), '0001'],
    ['ST', '835', '0002'],
    ['BPR', 'I', 12000.65, 'C', 'ACH', 'CCP', '01', '999999990', 'DA', '1234567891', '1111111112', '000011112', '01', '222222223', 'DA', '3333333334', datetime.date(2012, 3, 22), None, None, None, None, None],
    ['TRN', '1', '1QG11111112', '1111111112', '000011112'],
    ['DTM', '405', datetime.date(2012, 3, 19), None, None, None, None],
    ['N1', 'PR', 'ACME, INC. A WHOLLY OWNED SUBSIDIARY OF UNITED HEALTHCARE INSURANCE COMPANY', 'XV', '87726', None, None],
    ['N3', '123 MAIN STREET', None],
    ['N4', 'ANYTOWN', 'CA', '940660000', None, None, None],
    ['REF', '2U', '87726', None],
    ['N1', 'PE', 'MY CLINIC', 'XX', '1333333333', None, None],
    ['N3', '123 HEALTHCARE STREET', None],
    ['N4', 'SAN FRANCISCO', 'CA', '94109', None, None, None],
    ['REF', 'TJ', '777777777', None],
    ['LX', Decimal('1')],
    ['TS3', '1333333333', '81', datetime.date(2012, 12, 31), 1.0, 23276.56, 12000.65, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['CLP', '001-SSSSSSSSST', '1', 23276.56, 12000.65, 145.0, '14', '2234567891 1987654322', '81', None, None, None, None, None],
    ['CAS', 'PR', '1', 145.0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'SMITH', 'JOHN', None, None, None, None, None, None, None],
    ['NM1', 'IL', '1', 'SMITH', 'JANE', '', '', '', 'MI', '123222222', None, None],
    ['NM1', '74', '1', 'SMITH', 'JANE', 'A', None, None, None, None, None, None],
    ['REF', 'CE', 'CHOYC', None],
    ['REF', '1L', '717171', None],
    ['DTM', '050', datetime.date(2012, 3, 3), None, None, None, None],
    ['DTM', '232', datetime.date(2012, 2, 23), None, None, None, None],
    ['AMT', 'AU', 12145.65, None],
    ['SVC', ['HC', '88888', None, None, None, None, None], 23276.56, 12145.65, '', 1.0, None],
    ['DTM', '472', datetime.date(2012, 2, 21), None, None, None, None],
    ['CAS', 'CO', '45', 11130.91, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['REF', '6R', '252222222222', None],
    ['AMT', 'B6', 12145.65, None],
    ['SE', Decimal('28'), '0002'],
    ['GE', Decimal('1'), Decimal('15555')],
    ['IEA', Decimal('1'), Decimal('000015442')],
]


def test_835_example_2() -> None:
    example = EXAMPLES / "835-example-2.txt"
    document = Source(example.read_text())
    # Bad example? Wrong message class definition? Don't know.
    errors_here = [
        "*_N1:n101:Enumerated",
        "*_N1:n102:MaxLen",
        "*_N1:n103:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_NM1:nm101:Enumerated",
        "*_NM1:nm102:Enumerated",
        "*_NM1:nm108:Enumerated",
    ]
    parser = X12Parser(msg_835_4010_X091_A1.MSG835, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_835_example_2

expected_837_example = [
    ['ISA', '00', ' ', '00', ' ', 'ZZ', '123456789 ', '30', '41-1674742 ', datetime.date(2006, 2, 9), datetime.time(8, 26), 'U', '00401', Decimal('000000002'), '0', 'P', ':'],
    ['GS', 'HC', '123456789', '41-1674742', datetime.date(2006, 2, 9), datetime.time(8, 26), Decimal('2'), 'X', '004010X098A1'],
    ['ST', '837', '0001'],
    ['BHT', '0019', '00', '180', datetime.date(2006, 2, 9), datetime.time(8, 26), 'CH'],
    ['REF', '87', '004010X098A1', None],
    ['NM1', '41', '2', 'Brisbane Schools', '', '', '', '', '46', '567891234', None, None],
    ['PER', 'IC', 'Some Contact', 'TE', '5551231234', None, None, None, None, None],
    ['NM1', '40', '2', 'MN Department of Human Services', '', '', '', '', '46', '41-1674742', None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', '85', '2', 'Brisbane Schools', '', '', '', '', '24', '12-3456789', None, None],
    ['N3', '101 Brisbane Lane', None],
    ['N4', 'Brisbane', 'MN', '561641234', None, None, None],
    ['REF', '1D', '123456789', None],
    ['HL', '2', '1', '22', '0'],
    ['SBR', 'S', '18', '', '', '', '', '', '', 'MC'],
    ['NM1', 'IL', '1', 'Student', 'Some', '', '', '', 'MI', '12345678', None, None],
    ['N3', '109 Plum Street', None],
    ['N4', 'Somewherein', 'MN', '56123', None, None, None],
    ['DMG', 'D8', '19950505', 'M', None, None, None, None, None, None],
    ['NM1', 'PR', '2', 'MN Department of Human Services', '', '', '', '', 'PI', '41-1674742', None, None],
    ['CLM', '0777-0777-12345678', 32.73, '', '', ['03', '', '1'], 'Y', 'A', 'Y', 'Y', 'C', [None, None, None, None, None], None, None, None, None, None, None, None, None, None],
    ['LX', Decimal('1')],
    ['SV1', ['HC', 'T1018', 'U1', None, None, None, None], 10.63, 'UN', 1.0, None, None, [None, None, None, None], None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['DTP', '472', 'D8', '20060102'],
    ['LX', Decimal('2')],
    ['SV1', ['HC', 'T1018', 'U8', None, None, None, None], 22.1, 'UN', 10.0, None, None, [None, None, None, None], None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['DTP', '472', 'D8', '20060102'],
    ['SE', Decimal('26'), '0001'],
    ['GE', Decimal('1'), Decimal('2')],
    ['IEA', Decimal('1'), Decimal('000000002')],
]


def test_837_example() -> None:
    """File with a 'compressed' ISA header."""
    example = EXAMPLES / "837-example.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    # Handle compressed ISA header by skipping validation.
    # Other errors could be message definitions or examples.
    errors_here = [
        "*_ISA:*:MinLen",  # Compressed ISA header
        "*_NM1:nm101:Enumerated",
        "*_NM1:nm108:Enumerated",
        "*_DTP:dtp01:Enumerated",
        "*_REF:ref01:Enumerated",
    ]
    parser = X12Parser(msg_837_4010_X098_A1.MSG837, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_837_example

expected_837I_patient_notsubscriber = [
    ['ISA', '00', '00 ', '00', '00 ', 'ZZ', 'GENERAL HOSP ', 'ZZ', 'WI911234567', datetime.date(2002, 1, 22), datetime.time(11, 0), 'U', '00401', Decimal('000000001'), '0', 'T', ':'],
    ['GS', 'HC', '91-7777666', '91-1234567', datetime.date(2002, 1, 22), datetime.time(11, 0), Decimal('1'), 'X', '004010X096A1'],
    ['ST', '837', '0001'],
    ['BHT', '0019', '00', '0001', datetime.date(2002, 1, 22), datetime.time(11, 0), 'CH'],
    ['REF', '87', '004010X096A1', None],
    ['NM1', '41', '2', 'GENERAL HOSP', '', '', '', '', '46', '91-7777666', None, None],
    ['PER', 'IC', 'SUSAN', 'TE', '2064551111', None, None, None, None, None],
    ['NM1', '40', '2', ' WORLDWIDE INSUR', '', '', '', '', '46', '91-1234567', None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', '85', '2', 'GENERAL HOSP', '', '', '', '', '24', '91-7777666', None, None],
    ['N3', '404 2ND AVE', None],
    ['N4', 'SEATTLE', 'WA', '98112', None, None, None],
    ['HL', '2', '1', '22', '1'],
    ['SBR', 'P', '', '', 'CSI INC', '', '', '', '', 'CI'],
    ['NM1', 'IL', '1', 'FLINTSTONE', 'FRED', '', '', '', 'MI', 'WW2020-01', None, None],
    ['N3', '666 BEDROCK LN', None],
    ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None],
    ['NM1', 'PR', '2', ' WORLDWIDE INSUR', '', '', '', '', 'PI', '91-1234567', None, None],
    ['N3', '2020 1ST AVE', None],
    ['N4', 'SEATTLE', 'WA', '98112', None, None, None],
    ['HL', '3', '2', '23', '0'],
    ['PAT', '19', None, None, None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'FLINSTONE', 'PEBBLES', '', '', '', 'MI', 'WW2020-03', None, None],
    ['N3', '666 BEDROCK LN', None],
    ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None],
    ['DMG', 'D8', '19721201', 'F', None, None, None, None, None, None],
    ['CLM', 'FF555672020', 974.0, '', '', ['13', 'A', '1'], 'Y', 'A', 'Y', 'A', '', '', '', '', '', '', '', '', 'Y', None],
    ['DTP', '434', 'D8', '20011101'],
    ['CL1', '3', '7', None, None],
    ['REF', 'EA', '310628838', None],
    ['NTE', 'ADD', 'ACC-FELL OUT OF CAR'],
    ['HI', ['BK', '78907', None, None, None, None, None]],
    ['HI', ['BH', '11', 'D8', '20011101', None, None, None]],
    ['HI', ['BG', '09', None, None, None, None, None]],
    ['NM1', '71', '1', 'WELBY', 'MARCUS', '', '', 'MD', '34', '886027777', None, None],
    ['PRV', 'AT', 'ZZ', '363LN0000X', None, None],
    ['REF', 'G2', 'MWB7777', None],
    ['SBR', 'S', '17', '', 'WIZYWIG INC', '', '', '', '', 'CI'],
    ['DMG', 'D8', '19521001', 'F', None, None, None, None, None, None],
    ['OI', '', '', 'Y', '', '', 'A'],
    ['NM1', 'IL', '1', 'FLINTSTONE', 'WILMA', '', '', '', 'MI', 'WF55550', None, None],
    ['NM1', 'PR', '2', 'WASHINGTON HEALTH SERVICES', '', '', '', '', 'PI', '91-5779491', None, None],
    ['NM1', 'QC', '1', '', '', '', '', '', 'MI', 'WF5555002', None, None],
    ['LX', Decimal('1')],
    ['SV2', '301', ['', None, None, None, None, None, None], 350.0, 'UN', 1.0, None, None, None, None, None],
    ['DTP', '472', 'D8', '20011101'],
    ['LX', Decimal('2')],
    ['SV2', '450', ['HC', '99283', None, None, None, None, None], 500.0, 'UN', 1.0, None, None, None, None, None],
    ['DTP', '472', 'D8', '20011101'],
    ['LX', Decimal('3')],
    ['SV2', '650', ['', None, None, None, None, None, None], 124.0, 'UN', 1.0, None, None, None, None, None],
    ['DTP', '472', 'D8', '20011101'],
    ['SE', Decimal('51'), '0001'],
    ['GE', Decimal('1'), Decimal('1')],
    ['IEA', Decimal('1'), Decimal('1')]
]


def test_837I_patient_notsubscriber() -> None:
    """File with a 'compressed' ISA header. Special source setup."""
    example = EXAMPLES / "837I-Patient-NotSubscriber.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    # Handle compressed ISA header by skipping validation.
    # Other errors could be message definitions or examples.
    errors_here = [
        "*_ISA:*:MinLen",  # Compressed ISA header.
        "*_NM1:nm101:Enumerated",
        "*_NM1:nm103:MinLen",
        "*_NM1:nm108:Enumerated",
        "*_CLM:clm18:MinLen",
        "*_CLM:clm18:Enumerated",
        "*_CLM:clm19:MinLen",
        "*_DTP:dtp01:Enumerated",
        "*_DTP:dtp02:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_HI:hi12_01:Enumerated",
        "*_SV2:sv202_01:MinLen",
        "*_SV2:sv202_01:Enumerated",
    ]
    parser = X12Parser(msg_837_4010_X096_A1.MSG837, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_837I_patient_notsubscriber

expected_837I_patient_notsubscriber2 = [
    ['ISA', '00', '00 ', '00', '00 ', 'ZZ', 'GENERAL HOSP ', 'ZZ', 'WHS915779491', datetime.date(2002, 1, 22), datetime.time(11, 0), 'U', '00401', Decimal('000000001'), '0', 'T', ':'],
    ['GS', 'HC', '91-7777666', '91-5779491', datetime.date(2002, 1, 22), datetime.time(11, 0), Decimal('1'), 'X', '004010X096A1'],
    ['ST', '837', '0001'],
    ['BHT', '0019', '00', '0001', datetime.date(2002, 1, 22), datetime.time(11, 0), 'CH'],
    ['REF', '87', '004010X096A1', None],
    ['NM1', '41', '2', 'GENERAL HOSP', '', '', '', '', '46', '917777666', None, None],
    ['PER', 'IC', 'SUSAN', 'TE', '2064551111', None, None, None, None, None],
    ['NM1', '40', '2', ' WASHINGTON HEALTH SERVICES', '', '', '', '', '46', '915779491', None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', '85', '2', 'GENERAL HOSP', '', '', '', '', '24', '917777666', None, None],
    ['N3', '404 2ND AVE', None],
    ['N4', 'SEATTLE', 'WA', '98112', None, None, None],
    ['HL', '2', '1', '22', '1'],
    ['SBR', 'S', '', '', 'CSI INC', '', '', '', '', 'CI'],
    ['NM1', 'IL', '1', 'FLINTSTONE', 'WILMA', '', '', '', 'MI', 'WF55550', None, None],
    ['N3', '666 BEDROCK LN', None],
    ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None],
    ['NM1', 'PR', '2', ' WASHINGTON HEALTH SERVICES', '', '', '', '', 'PI', '915779491', None, None],
    ['N3', '234 2ND AVE', None],
    ['N4', 'SEATTLE', 'WA', '98112', None, None, None],
    ['HL', '3', '2', '23', '0'],
    ['PAT', '17', None, None, None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'FLINSTONE', 'PEBBLES', '', '', '', 'MI', 'WF5555002', None, None],
    ['N3', '666 BEDROCK LN', None],
    ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None],
    ['DMG', 'D8', '19721201', 'F', None, None, None, None, None, None],
    ['CLM', 'FF559872032', 3712.0, '', '', ['11', 'A', '1'], 'Y', 'A', 'Y', 'A', '', '', '', '', '', '', '', '', 'Y', None],
    ['DTP', '096', 'TM', '1700'],
    ['DTP', '434', 'RD8', '20011115-20011117'],
    ['DTP', '435', 'DT', '200111151500'],
    ['CL1', '4', '1', '01', None],
    ['REF', 'EA', '310628838', None],
    ['HI', ['BK', '65421', None, None, None, None, None]],
    ['HI', ['BF', '64891', None, None, None, None, None]],
    ['HI', ['BR', '741', None, None, None, None, None]],
    ['HI', ['BQ', '7279', None, None, None, None, None]],
    ['NM1', '71', '1', 'WELBY', 'MARCUS', '', '', 'MD', '34', '886027777', None, None],
    ['PRV', 'AT', 'ZZ', '363LN0000X', None, None],
    ['REF', 'G2', 'YT5555', None],
    ['SBR', 'P', '19', '', 'CSI INC', '', '', '', '', 'CI'],
    ['AMT', 'C4', 2500.0, None],
    ['DMG', 'D8', '19501101', 'M', None, None, None, None, None, None],
    ['OI', '', '', 'Y', '', '', 'A'],
    ['NM1', 'IL', '1', 'FLINTSTONE', 'FRED', '', '', '', 'MI', 'WW2020-01', None, None],
    ['N3', '666 BEDROCK LANE', None],
    ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None],
    ['NM1', 'PR', '2', 'WORLDWIDE INSURANCE', '', '', '', '', 'PI', '911234567', None, None],
    ['REF', 'G1', '888990', None],
    ['NM1', 'QC', '1', '', '', '', '', '', 'MI', 'WF2020-03', None, None],
    ['LX', Decimal('1')],
    ['SV2', '120', ['', None, None, None, None, None, None], 1670.0, 'DA', 2.0, 835.0, None, None, None, None],
    ['DTP', '472', 'RD8', '20011115-20011117'],
    ['LX', Decimal('2')],
    ['SV2', '250', ['', None, None, None, None, None, None], 667.0, 'UN', 1.0, None, None, None, None, None],
    ['DTP', '472', 'D8', '20011117'],
    ['LX', Decimal('3')],
    ['SV2', '370', ['', None, None, None, None, None, None], 375.0, 'UN', 1.0, None, None, None, None, None],
    ['DTP', '472', 'D8', '20011115'],
    ['LX', Decimal('4')],
    ['SV2', '720', [' ', None, None, None, None, None, None], 1000.0, 'UN', 1.0, None, None, None, None, None],
    ['DTP', '472', 'D8', '20011115'],
    ['SE', Decimal('61'), '0001'],
    ['GE', Decimal('1'), Decimal('1')],
    ['IEA', Decimal('1'), Decimal('1')]
]


def test_837I_patient_notsubscriber2() -> None:
    """File with a 'compressed' ISA header. Special source setup."""
    example = EXAMPLES / "837I-Patient-NotSubscriber2.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    # Handle compressed ISA header by skipping validation.
    # Other errors could be message definitions or examples.
    errors_here = [
        "*_ISA:*:MinLen",  # Compressed ISA header.
        "*_AMT:amt01:Enumerated",
        "*_NM1:nm101:Enumerated",
        "*_NM1:nm103:MinLen",
        "*_NM1:nm108:Enumerated",
        "*_CLM:clm18:MinLen",
        "*_CLM:clm19:MinLen",
        "*_DTP:dtp01:Enumerated",
        "*_DTP:dtp02:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_HI:hi12_01:Enumerated",
        "*_SV2:sv202_01:MinLen",
    ]
    parser = X12Parser(msg_837_4010_X096_A1.MSG837, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_837I_patient_notsubscriber2

expected_837I_patient_subscriber = [
    ['ISA', '00', '00 ', '00', '00 ', 'ZZ', 'CRU1234 ', 'ZZ', 'WI911234567 ', datetime.date(2002, 1, 22), datetime.time(11, 0), 'U', '00401', Decimal('000000001'), '0', 'T', ':'],
    ['GS', 'HC', '91-1257070', '91-1234567', datetime.date(2002, 1, 22), datetime.time(11, 0), Decimal('1'), 'X', '004010X096A1'],
    ['ST', '837', '0001'],
    ['BHT', '0019', '00', '0001', datetime.date(2002, 1, 22), datetime.time(11, 0), 'CH'],
    ['REF', '87', '004010X096A1', None],
    ['NM1', '41', '2', 'CLAIMS R US', '', '', '', '', '46', '911257070', None, None],
    ['PER', 'IC', 'CONTACT NAME', 'TE', '555-546-1234', None, None, None, None, None],
    ['NM1', '40', '2', ' WORLDWIDE INSUR', '', '', '', '', '46', '911234567', None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', '85', '2', 'GENERAL HOSP', '', '', '', '', '24', '917777666', None, None],
    ['N3', '404 2ND AVE', None],
    ['N4', 'SEATTLE', 'WA', '98112', None, None, None],
    ['REF', 'G2', 'XYZ', None],
    ['HL', '2', '1', '22', '0'],
    ['SBR', 'P', '18', '', 'CSI INC', '', '', '', '', 'CI'],
    ['NM1', 'IL', '1', 'FLINTSTONE', 'FRED', '', '', '', 'MI', 'WW2020-01', None, None],
    ['N3', '666 BEDROCK LN', None],
    ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None],
    ['DMG', 'D8', '19501101', 'M', None, None, None, None, None, None],
    ['NM1', 'PR', '2', ' WORLDWIDE INSUR', '', '', '', '', 'PI', '911234567', None, None],
    ['N3', '2020 1ST AVE', None],
    ['N4', 'SEATTLE', 'WA', '98112', None, None, None],
    ['CLM', 'FF555202020', 2750.0, '', '', ['11', 'A', '1'], 'Y', 'A', 'Y', 'Y', '', '', '', '', '', '', '', '', 'Y', None],
    ['DTP', '096', 'TM', '0900'],
    ['DTP', '434', 'RD8', '20011205-20011207'],
    ['DTP', '435', 'DT', '200112051000'],
    ['CL1', '3', '1', '01', None],
    ['HI', ['BK', '27542', None, None, None, None, None]],
    ['HI', ['BF', '260', None, None, None, None, None]],
    ['NM1', '71', '1', 'WELBY', 'MARCUS', '', '', 'MD', '34', '886027777', None, None],
    ['PRV', 'AT', 'ZZ', '363LN0000X', None, None],
    ['REF', 'G2', 'MWB7777', None],
    ['LX', Decimal('1')],
    ['SV2', '120', ['', None, None, None, None, None, None], 2000.0, 'DA', 2.0, 1000.0, None, None, None, None],
    ['LX', Decimal('2')],
    ['SV2', '250', ['', None, None, None, None, None, None], 250.0, 'UN', 1.0, None, None, None, None, None],
    ['LX', Decimal('3')],
    ['SV2', '300', ['', None, None, None, None, None, None], 500.0, 'UN', 1.0, None, None, None, None, None],
    ['SE', Decimal('37'), '0001'],
    ['GE', Decimal('1'), Decimal('1')],
    ['IEA', Decimal('1'), Decimal('1')]
]


def test_837I_patient_subscriber() -> None:
    """File with a 'compressed' ISA header."""
    example = EXAMPLES / "837I-Patient-Subscriber.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    # Handle compressed ISA header by skipping validation.
    # Other errors could be message definitions or examples.
    errors_here = [
        "*_ISA:*:MinLen",  # Compressed ISA header.
        "*_NM1:nm101:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_NM1:nm108:Enumerated",
        "*_CLM:clm18:MinLen",
        "*_CLM:clm19:MinLen",
        "*_DTP:dtp01:Enumerated",
        "*_DTP:dtp02:Enumerated",
        "*_HI:hi12_01:Enumerated",
        "*_SV2:sv202_01:MinLen",
        # "*_AMT:amt01:Enumerated",
    ]
    parser = X12Parser(msg_837_4010_X096_A1.MSG837, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_837I_patient_subscriber

expected_837I_examples = [
    ['ISA', '00', ' ', '00', ' ', 'ZZ', '9999999 ', 'ZZ', 'DMA7384 ', datetime.date(2003, 2, 28), datetime.time(9, 34), 'U', '00401', Decimal('3'), '1', 'T', ':'],
    ['GS', 'HC', '9999999', 'DMA7384', datetime.date(2003, 2, 28), datetime.time(9, 34), Decimal('3'), 'X', '004010X096A1'],
    ['ST', '837', '30001'],
    ['BHT', '0019', '00', '484', datetime.date(2003, 2, 28), datetime.time(9, 34), 'CH'],
    ['REF', '87', '004010X096A1', None],
    ['NM1', '41', '2', 'MEDICAL CLAIMS', '', '', '', '', '46', '9999999', None, None],
    ['PER', 'IC', 'JANE DOE', 'TE', '8605551124', 'FX', '8605551146', None, None, None],
    ['NM1', '40', '2', 'MA MEDICAID', '', '', '', '', '46', 'DMA7384', None, None],
    ['HL', '1', '', '20', '1'],
    ['PRV', 'PE', 'ZZ', '103T00000X', None, None],
    ['NM1', '85', '2', 'BILLING AGENT', '', '', '', '', '24', '123456789', None, None],
    ['N3', '345 ZERO DRIVE', None],
    ['N4', 'ANDOVER', 'MA', '01810', None, None, None],
    ['REF', '1D', '9812345', None],
    ['NM1', '87', '2', 'HOSPITAL', '', '', '', '', 'XX', '1234567890', None, None],
    ['N3', '111 OVERHILL DRIVE', None],
    ['N4', 'ANDOVER', 'MA', '01810', None, None, None],
    ['HL', '2', '1', '22', '0'],
    ['SBR', 'P', '18', '', ' MassHealth', '', '', '', '', 'MC'],
    ['NM1', 'IL', '1', 'LAST', 'FIRST', '', '', '', 'MI', '0101010101', None, None],
    ['N3', '230 1ST AVE', None],
    ['N4', 'FALL RIVER', 'MA', '02721', None, None, None],
    ['DMG', 'D8', '19511204', 'F', None, None, None, None, None, None],
    ['NM1', 'PR', '2', 'MEDICAID', '', '', '', '', 'PI', 'DMA7384', None, None],
    ['CLM', '12225850', 10157.05, '', '', ['11', 'A', '1'], 'N', 'A', 'Y', 'Y', '', '', '', '', '', '', '', '', 'N', None],
    ['DTP', '096', 'TM', '1130'],
    ['DTP', '434', 'D8', '20030116'],
    ['DTP', '435', 'DT', '200204091242'],
    ['CL1', '2', '1', '01', None],
    ['AMT', 'F3', 100.0, None],
    ['PWK', 'AS', 'EL', Decimal('0'), '', 'AC', '123456', None, None],
    ['REF', 'G1', 'MAA36169000029', None],
    ['REF', 'F8', 'MAA36169000029', None],
    ['REF', 'EA', 'MAA36169000029', None],
    ['REF', 'G4', 'MAA36169000029', None],
    ['NTE', 'ADD', ' TEST TEST'],
    ['HI', ['BK', '29382', None, None, None, None, None]],
    ['HI', ['BF', '12345', None, None, None, None, None]],
    ['HI', ['BR', '8703', 'D8', '20020327', None, None, None]],
    ['HI', ['BQ', '8871', 'D8', '20020328', None, None, None]],
    ['HI', ['BH', '11', 'D8', '20020330', None, None, None]],
    ['HI', ['BE', '37', '', '', 4.0, None, None]],
    ['HI', ['BG', 'C5', None, None, None, None, None]],
    ['QTY', 'CA', 4.0, ['DA', None, None, None, None, None, None, None, None, None, None, None, None, None, None], None],
    ['HI', ['BI', '11', 'RD8', '20020330-20020402', None, None, None]],
    ['NM1', '71', '2', 'DOCTOR, ONE', '', '', '', '', 'XX', '1234567890', None, None],
    ['PRV', 'AT', 'ZZ', '103T00000X', None, None],
    ['NM1', '72', '2', 'DOCTOR, TWO', '', '', '', '', 'XX', '1234567890', None, None],
    ['PRV', 'OP', 'ZZ', '103T00001X', None, None],
    ['LX', Decimal('1')],
    ['SV2', '0150', ['HC', '270', '21', None, None, None, None], 2753.0, 'UN', 1.0, None, None, None, None, None],
    ['DTP', '435', 'DT', '200204091242'],
    ['DTP', '472', 'D8', '20030201'],

    ['ISA', '00', ' ', '00', ' ', 'ZZ', '0605638 ', 'ZZ', 'DMA7384 ', datetime.date(2003, 3, 6), datetime.time(10, 0), 'U', '00401', Decimal('49'), '0', 'P', ':'],
    ['GS', 'HC', '00181', '112111001', datetime.date(2002, 11, 6), datetime.time(12, 54), Decimal('1'), 'X', '004010X096A1'],
    ['ST', '837', '0001'],
    ['BHT', '0019', '00', '021119001', datetime.date(2002, 11, 6), datetime.time(12, 54), 'CH'],
    ['REF', '87', '004010X096A1', None],
    ['NM1', '41', '2', 'XYZ SVC 81', '', '', '', '', '46', '00189', None, None],
    ['PER', 'IC', 'NOT LISTED', 'TE', '8775679999', None, None, None, None, None],
    ['NM1', '40', '2', 'MEDICAID', '', '', '', '', '46', '112111001', None, None],
    ['HL', '1', '', '20', '1'],
    ['PRV', 'BI', 'ZZ', '273R000999', None, None],
    ['NM1', '85', '2', 'HEALTH XYZ HOSPITALS', '', '', '', '', 'XX', '1234567890', None, None],
    ['N3', 'xx HOSPITAL ROAD', None],
    ['N4', 'CITY', 'MA', '014599004', None, None, None],
    ['HL', '2', '1', '22', '0'],
    ['SBR', 'S', '18', '112111001', '', '', '', '', '', 'ZZ'],
    ['NM1', 'IL', '1', 'xxx', 'yyy', 'S', '', '', 'MI', '01346623999', None, None],
    ['N3', '54 xyz RD', 'W'],
    ['N4', 'CITY', 'MA', '019992008', None, None, None],
    ['DMG', 'D8', '19990508', 'F', None, None, None, None, None, None],
    ['NM1', 'PR', '2', 'MEDICAID', '', '', '', '', 'PI', '112111001', None, None],
    ['N3', '600 WASHINGTON ST.', None],
    ['N4', 'BOSTON', 'MA', '02111', None, None, None],
    ['CLM', '5006935999', 5370.1, '', '', ['11', 'A', '1'], 'Y', '', 'Y', 'Y', '', '', '', '', '', '', '', '', 'Y', None],
    ['DTP', '096', 'TM', '1100'],
    ['DTP', '434', 'RD8', '20021011-20021016'],
    ['DTP', '435', 'DT', '200210110100'],
    ['CL1', '1', '1', '01', None],
    ['REF', 'EA', '3611889', None],
    ['HI', ['BK', '29630', None, None, None, None, None]],
    ['HI', ['DR', '430', None, None, None, None, None]],
    ['HI', ['BF', '30019', None, None, None, None, None]],
    ['HI', ['BE', '08', '', '', 2030.0, None, None]],
    ['HI', ['BG', 'C5', None, None, None, None, None]],
    ['QTY', 'CA', 5.0, ['DA', None, None, None, None, None, None, None, None, None, None, None, None, None, None], None],
    ['QTY', 'LA', 5.0, ['DA', None, None, None, None, None, None, None, None, None, None, None, None, None, None], None],
    ['NM1', '71', '1', 'XYZ', 'J', '', '', '', 'XX', '1234569990', None, None],
    ['PRV', 'AT', 'ZZ', '203B000999', None, None],
    ['REF', '1G', '9995339', None],
    ['SBR', 'P', '18', '', 'XXX', '', '', '', '', 'CI'],
    ['CAS', 'CO', 'A2', 3533.63, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['AMT', 'C4', 1836.47, None],
    ['AMT', 'B6', 5370.1, None],
    ['AMT', 'N1', 1836.47, None],
    ['AMT', 'AA', 1836.47, None],
    ['DMG', 'D8', '19700508', 'F', None, None, None, None, None, None],
    ['OI', '', '', 'Y', '', '', 'Y'],
    ['NM1', 'IL', '1', 'XXX', 'YYY', 'S', '', '', 'MI', '01346623999', None, None],
    ['N3', '54 XYZ RD', 'W'],
    ['N4', 'TOWN', 'MA', '019992008', None, None, None],
    ['NM1', 'PR', '2', 'XYZ 81', '', '', '', '', 'PI', '001991', None, None],
    ['N3', '2 XYZ DRIVE', None],
    ['N4', 'TOWN', 'ME', '041999911', None, None, None],
    ['DTP', '573', 'D8', '20021106'],
    ['REF', 'F8', '1229630212', None],
    ['NM1', '71', '1', None, None, None, None, None, None, None, None, None],
    ['REF', '1G', '9939533', None],
    ['NM1', '72', '1', None, None, None, None, None, None, None, None, None],
    ['REF', '1G', '9993533', None],
    ['LX', Decimal('1')],
    ['SV2', '0124', ['', None, None, None, None, None, None], 4400.0, 'UN', 5.0, 880.0, None, None, None, None],
    ['SVD', '00181', 0.0, ['', None, None, None, None, None, None], '0124', 5.0, None],
    ['DTP', '573', 'D8', '20021106'],
    ['LX', Decimal('2')],
    ['SV2', '0250', ['', None, None, None, None, None, None], 2.76, 'UN', 2.0, None, None, None, None, None],
    ['SVD', '00181', 0.0, ['', None, None, None, None, None, None], '0250', 2.0, None],
    ['DTP', '573', 'D8', '20021106'],
    ['LX', Decimal('3')],
    ['SV2', '0259', ['', None, None, None, None, None, None], 410.34, 'UN', 95.0, None, None, None, None, None],
    ['SVD', '00181', 0.0, ['', None, None, None, None, None, None], '0259', 95.0, None],
    ['DTP', '573', 'D8', '20021106'],
    ['LX', Decimal('4')],
    ['SV2', '0300', ['', None, None, None, None, None, None], 557.0, 'UN', 13.0, None, None, None, None, None],
    ['SVD', '00181', 0.0, ['', None, None, None, None, None, None], '0300', 13.0, None],
    ['DTP', '573', 'D8', '20021106'],
    ['SE', Decimal('74'), '0001'],
    ['GE', Decimal('1'), Decimal('1')],
    ['IEA', Decimal('1'), Decimal('49')],
]


def test_837I_examples() -> None:
    """
    The source file seems damaged.
    The first section ends abruptly with a DTP
    and then picks up with a new ISA.
    """
    example = EXAMPLES / "837I-Examples.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    # Handle compressed ISA header by skipping validation.
    # Other errors could be message definitions or examples.
    errors_here = [
        "*_ISA:*:MinLen",  # Compressed ISA header.
        "*_PRV:prv01:Enumerated",
        "*_NM1:nm101:Enumerated",
        "*_NM1:nm102:Enumerated",
        "*_NM1:nm108:Enumerated",
        "*_SVD:svd03_01:MinLen",
        "*_SVD:svd03_01:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_CLM:clm18:MinLen",
        "*_CLM:clm19:MinLen",
        "*_DTP:dtp01:Enumerated",
        "*_DTP:dtp02:Enumerated",
        "*_AMT:amt01:Enumerated",
        "*_HI:hi12_01:Enumerated",
        "*_SV2:sv202_01:MinLen",
    ]
    parser = X12Parser(msg_837_4010_X096_A1.MSG837, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_837I_examples


expected_276_txns = [
    ['ISA', '03', 'mdycha1   ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 4), 'U', '00401', Decimal('246742'), '0', 'T', ':'],
    ['GS', 'HR', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 4), Decimal('245842'), 'X', '004010X093A1'],
    ['ST', '276', '246742'],
    ['BHT', '0010', '13', '', datetime.date(2007, 10, 15), None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '41', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'FI', '830382654', None, None],
    ['HL', '3', '2', '19', '1'],
    ['NM1', '1P', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'SV', '000000042000', None, None],
    ['HL', '4', '3', '22', '0'],
    ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'YJP88091836301', None, None],
    ['TRN', '1', 'GZCSMXKRDR', None, None],
    ['AMT', 'T3', 0.0, None],
    ['DTP', '232', 'RD8', '20070919-20070921'],
    ['SE', Decimal('15'), '246742'],
    ['GE', Decimal('1'), Decimal('245842')],
    ['IEA', Decimal('1'), Decimal('246742')],

    ['ISA', '03', 'mdycha1   ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), 'U', '00401', Decimal('246785'), '0', 'T', ':'],
    ['GS', 'HR', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), Decimal('245885'), 'X', '004010X093A1'],
    ['ST', '276', '246785'],
    ['BHT', '0010', '13', '', datetime.date(2007, 10, 15), None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '41', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'FI', '830382654', None, None],
    ['HL', '3', '2', '19', '1'],
    ['NM1', '1P', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'SV', '000000042000', None, None],
    ['HL', '4', '3', '22', '0'],
    ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'YJP88101119801', None, None],
    ['TRN', '1', 'MVFWVYEJJD', None, None],
    ['AMT', 'T3', 0.0, None],
    ['DTP', '232', 'RD8', '20070919-20070922'],
    ['SE', Decimal('15'), '246785'],
    ['GE', Decimal('1'), Decimal('245885')],
    ['IEA', Decimal('1'), Decimal('246785')],

    ['ISA', '03', 'lhammond1 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 9), 'U', '00401', Decimal('32685'), '0', 'T', ':'],
    ['GS', 'HR', '0000000Eliginet', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 9), Decimal('31785'), 'X', '004010X093A1'],
    ['ST', '276', '32685'],
    ['BHT', '0010', '13', '', datetime.date(2007, 10, 15), None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '41', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'FI', '141338413', None, None],
    ['HL', '3', '2', '19', '1'],
    ['NM1', '1P', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'SV', '000400010000', None, None],
    ['HL', '4', '3', '22', '0'],
    ['DMG', 'D8', '19740201', 'U', None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'ZWP88005432001', None, None],
    ['TRN', '1', 'COPROCKESA', None, None],
    ['AMT', 'T3', 0.0, None],
    ['DTP', '232', 'RD8', '20070815-20070815'],
    ['SE', Decimal('15'), '32685'],
    ['GE', Decimal('1'), Decimal('31785')],
    ['IEA', Decimal('1'), Decimal('32685')],

    ['ISA', '03', 'lhammond1 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 11), 'U', '00401', Decimal('32694'), '0', 'T', ':'],
    ['GS', 'HR', '0000000Eliginet', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 11), Decimal('31794'), 'X', '004010X093A1'],
    ['ST', '276', '32694'],
    ['BHT', '0010', '13', '', datetime.date(2007, 10, 15), None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '41', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'FI', '141338413', None, None],
    ['HL', '3', '2', '19', '1'],
    ['NM1', '1P', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'SV', '000400010000', None, None],
    ['HL', '4', '3', '22', '0'],
    ['DMG', 'D8', '19990705', 'U', None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'ZWX88065356704', None, None],
    ['TRN', '1', 'UGXSOJFCFD', None, None],
    ['AMT', 'T3', 0.0, None],
    ['DTP', '232', 'RD8', '20070725-20070725'],
    ['SE', Decimal('15'), '32694'],
    ['GE', Decimal('1'), Decimal('31794')],
    ['IEA', Decimal('1'), Decimal('32694')],

    ['ISA', '03', 'mormond   ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 26), 'U', '00401', Decimal('247238'), '0', 'T', ':'],
    ['GS', 'HR', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 26), Decimal('246338'), 'X', '004010X093A1'],
    ['ST', '276', '247238'],
    ['BHT', '0010', '13', '', datetime.date(2007, 10, 15), None, None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'PR', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '41', '2', "MOUNT ST MARY'S HOSPITAL", '', '', '', '', 'FI', '161523353', None, None],
    ['HL', '3', '2', '19', '1'],
    ['NM1', '1P', '2', "MOUNT ST MARY'S HOSPITAL", '', '', '', '', 'SV', '000000022000', None, None],
    ['HL', '4', '3', '22', '0'],
    ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
    ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'yjw99000745701', None, None],
    ['TRN', '1', 'GGEEMIMLEV', None, None],
    ['AMT', 'T3', 0.0, None],
    ['DTP', '232', 'RD8', '20070827-20070830'],
    ['SE', Decimal('15'), '247238'],
    ['GE', Decimal('1'), Decimal('246338')],
    ['IEA', Decimal('1'), Decimal('247238')],
]


def test_276_txns_x12parse() -> None:
    """
    Transaction set, Multiple messages in a single file.
    File with a 'compressed' ISA header.
    """
    example = EXAMPLES / "TEST 276 TXNs.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    parser = X12Parser(msg_276_4010_X093_A1.MSG276)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_276_txns

expected_278_13_txns = [
    ['ISA', '03', 'gjohnson2 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 3), 'U', '00401', Decimal('242835'), '0', 'P', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 3), Decimal('241935'), 'X', '004010X094A1'],
    ['ST', '278', '242835'],
    ['BHT', '0078', '13', 'GXEDWLXQYKII', datetime.date(2007, 10, 15), datetime.time(9, 3), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '1', 'SHEIKH', 'ZIA', '', '', '', '24', '161590688', None, None],
    ['REF', 'ZH', '000524454008', None],
    ['N3', '4039 ROUTE 219', 'SUITE 102'],
    ['N4', 'SALAMANCA', 'NY', '14779', None, None, None],
    ['HL', '3', '2', '22', '1'],
    ['HI', ['BF', '706.1', None, None, None, None, None]],
    ['NM1', 'IL', '1', 'burton', 'amanda', '', '', '', 'MI', 'yjw88034076701', None, None],
    ['DMG', 'D8', '19900815', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', '19', '1'],
    ['NM1', 'SJ', '1', 'JAREMKO', 'WILLIAM', '', '', '', '24', '161482964', None, None],
    ['REF', 'ZH', '000511127003', None],
    ['N3', '2646 WEST STATE STREET', 'SUITE 405'],
    ['N4', 'OLEAN', 'NY', '147600000', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'SC', 'I', '', ['', None, None], ['', None, None, None, None], '', '', '', 'Y', None],
    ['DTP', '472', 'RD8', '20071015-20080415'],
    ['HSD', 'VS', 30.0, None, None, None, None, None, None],
    ['SE', Decimal('24'), '242835'],
    ['GE', Decimal('1'), Decimal('241935')],
    ['IEA', Decimal('1'), Decimal('242835')],

    ['ISA', '03', 'jrandazzo ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 3), 'U', '00401', Decimal('242836'), '0', 'P', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 3), Decimal('241936'), 'X', '004010X094A1'],
    ['ST', '278', '242836'],
    ['BHT', '0078', '13', 'KLTVJTDDRYEM', datetime.date(2007, 10, 15), datetime.time(9, 3), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '1', 'PERNA', 'ANTHONY', '', '', '', '24', '161260886', None, None],
    ['REF', 'ZH', '000500338001', None],
    ['N3', '41 DELAWARE ROAD', None],
    ['N4', 'KENMORE', 'NY', '142172742', None, None, None],
    ['HL', '3', '2', '22', '1'],
    ['HI', ['BF', '599.7', None, None, None, None, None]],
    ['NM1', 'IL', '1', 'farrugia', 'brenda', '', '', '', 'MI', '88027756201', None, None],
    ['DMG', 'D8', '19391111', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', '19', '1'],
    ['NM1', 'SJ', '1', 'GRECO', 'JOSEPH', '', '', '', '24', '161511795', None, None],
    ['REF', 'ZH', '000507772005', None],
    ['N3', '55 SPINDRIFT DRIVE', 'SUITE 240'],
    ['N4', 'WILLIAMSVILLE', 'NY', '14221', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'SC', 'I', '', ['', None, None], ['', None, None, None, None], '', '', '', 'Y', None],
    ['DTP', '472', 'RD8', '20071015-20080415'],
    ['HSD', 'VS', 10.0, None, None, None, None, None, None],
    ['SE', Decimal('24'), '242836'],
    ['GE', Decimal('1'), Decimal('241936')],
    ['IEA', Decimal('1'), Decimal('242836')],

    ['ISA', '03', 'dnoone    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 3), 'U', '00401', Decimal('32674'), '0', 'P', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 3), Decimal('31774'), 'X', '004010X094A1'],
    ['ST', '278', '32674'],
    ['BHT', '0078', '13', 'ENLENGSDPMTQ', datetime.date(2007, 10, 15), datetime.time(9, 3), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '1', 'VACEK', 'JAMES', '', '', '', '24', '141338465', None, None],
    ['REF', 'ZH', '000401141002', None],
    ['N3', '99 EAST STATE STREET', None],
    ['N4', 'GLOVERSVILLE', 'NY', None, None, None, None],
    ['HL', '3', '2', '22', '1'],
    ['HI', ['BF', '366.19', None, None, None, None, None]],
    ['NM1', 'IL', '1', '', '', '', '', '', 'MI', '88003509901', None, None],
    ['DMG', 'D8', '19221209', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', '19', '1'],
    ['NM1', 'SJ', '1', 'MAIRS', 'MICHAEL', '', '', '', '24', '141786068', None, None],
    ['REF', 'ZH', '000407032001', None],
    ['N3', '185 SECOND AVENUE', None],
    ['N4', 'GLOVERSVILLE', 'NY', '12078', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'SC', 'I', '', ['', None, None], ['', None, None, None, None], '', '', '', 'Y', None],
    ['DTP', '472', 'RD8', '20071015-20080415'],
    ['HSD', 'VS', 20.0, None, None, None, None, None, None],
    ['SE', Decimal('24'), '32674'],
    ['GE', Decimal('1'), Decimal('31774')],
    ['IEA', Decimal('1'), Decimal('32674')],

    ['ISA', '03', 'gjohnson2 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 4), 'U', '00401', Decimal('242839'), '0', 'P', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 4), Decimal('241939'), 'X', '004010X094A1'],
    ['ST', '278', '242839'],
    ['BHT', '0078', '13', 'WHBMBBXDSPML', datetime.date(2007, 10, 15), datetime.time(9, 4), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '1', 'SHEIKH', 'ZIA', '', '', '', '24', '161590688', None, None],
    ['REF', 'ZH', '000524454008', None],
    ['N3', '4039 ROUTE 219', 'SUITE 102'],
    ['N4', 'SALAMANCA', 'NY', '14779', None, None, None],
    ['HL', '3', '2', '22', '1'],
    ['HI', ['BF', '706.1', None, None, None, None, None]],
    ['NM1', 'IL', '1', 'burton', 'amanda', '', '', '', 'MI', 'yjw88034076701', None, None],
    ['DMG', 'D8', '19900815', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', '19', '1'],
    ['NM1', 'SJ', '1', 'JAREMKO', 'WILLIAM', '', '', '', '24', '161482964', None, None],
    ['REF', 'ZH', '000511127003', None],
    ['N3', '2646 WEST STATE STREET', 'SUITE 405'],
    ['N4', 'OLEAN', 'NY', '147600000', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'SC', 'I', '', ['', None, None], ['', None, None, None, None], '', '', '', 'Y', None],
    ['DTP', '472', 'RD8', '20071015-20080415'],
    ['HSD', 'VS', 30.0, None, None, None, None, None, None],
    ['SE', Decimal('24'), '242839'],
    ['GE', Decimal('1'), Decimal('241939')],
    ['IEA', Decimal('1'), Decimal('242839')],

    ['ISA', '03', 'tmason    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 5), 'U', '00401', Decimal('32679'), '0', 'P', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BlueShield of N', datetime.date(2007, 10, 15), datetime.time(9, 5), Decimal('31779'), 'X', '004010X094A1'],
    ['ST', '278', '32679'],
    ['BHT', '0078', '13', 'EOCMUPJPJCEO', datetime.date(2007, 10, 15), datetime.time(9, 5), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '1', 'MAZZEI', 'RENATA', '', '', '', '24', '141338428', None, None],
    ['REF', 'ZH', '000404963001', None],
    ['N3', '460 SARATOGA ROAD', None],
    ['N4', 'SCOTIA', 'NY', '12302', None, None, None],
    ['HL', '3', '2', '22', '1'],
    ['HI', ['BF', 'V65.8', None, None, None, None, None]],
    ['NM1', 'IL', '1', 'whitney', 'james', '', '', '', 'MI', '88059250301', None, None],
    ['DMG', 'D8', '19701002', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', '19', '1'],
    ['NM1', 'SJ', '1', 'NYDEGGER', 'RUDY', '', '', '', '24', '141787916', None, None],
    ['REF', 'ZH', '000471951001', None],
    ['N3', '1201 NOTT STREET', 'SUITE 103'],
    ['N4', 'SCHENECTADY', 'NY', '123082589', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'SC', 'I', '', ['', None, None], ['', None, None, None, None], '', '', '', 'Y', None],
    ['DTP', '472', 'RD8', '20071015-20080415'],
    ['HSD', 'VS', 6.0, None, None, None, None, None, None],
    ['SE', Decimal('24'), '32679'],
    ['GE', Decimal('1'), Decimal('31779')],
    ['IEA', Decimal('1'), Decimal('32679')],
]


def test_278_13_txns() -> None:
    """
    Transaction set, Multiple messages in a single file.
    File with a 'compressed' ISA header.
    """
    example = EXAMPLES / "TEST 278_13 TXNS.txt"
    document = Source(example.read_text())
    # Bad example? Wrong message class definition? Don't know.
    errors_here = [
        "*_HL:hl03:Enumerated",
        "*_NM1:nm101:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_UM:um04_01:MinLen",
        "*_UM:um05_01:MinLen",
        "*_UM:um05_01:Enumerated",
        "*_DTP:dtp01:Enumerated",
        "*_DTP:dtp02:Enumerated",
    ]
    parser = X12Parser(msg_278_4010_X094_A1.MSG278, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_278_13_txns

expected_278_28_txns_soa = [
    ['ISA', '03', 'jking3    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), 'U', '00401', Decimal('246767'), '0', 'T', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), Decimal('245867'), 'X', '004010X059'],
    ['ST', '278', '246767'],
    ['BHT', '0083', '28', 'XPMPDTETJDHS', datetime.date(2007, 10, 15), datetime.time(9, 5), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '1', 'SHAH', 'SIDDHARTHA', '', '', '', '24', '161569074', None, None],
    ['REF', 'ZH', '000511391004', None],
    ['HL', '3', '2', '22', '1'],
    ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJE88000251501', None, None],
    ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', 'PA', '1'],
    ['NM1', 'DN', '1', 'SHAH', 'SIDDHARTHA', '', '', '', '24', '161569074', None, None],
    ['REF', 'ZH', '000511391004', None],
    ['N3', '60 MAPLE ROAD', None],
    ['N4', 'WILLIAMSVILLE', 'NY', '142212918', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'SC', '', '', ['', None, None], '', '', '', '', 'Y'],
    ['DTP', '472', 'RD8', '20071015-20071113'],
    ['SE', Decimal('20'), '246767'],
    ['GE', Decimal('1'), Decimal('245867')],
    ['IEA', Decimal('1'), Decimal('246767')],

    ['ISA', '03', 'bjary     ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), 'U', '00401', Decimal('242872'), '0', 'T', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), Decimal('241972'), 'X', '004010X059'],
    ['ST', '278', '242872'],
    ['BHT', '0083', '28', 'JVQWCOPYJBYW', datetime.date(2007, 10, 15), datetime.time(9, 5), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '1', 'SANSANO JR', 'MICHAEL', '', '', '', '24', '161505558', None, None],
    ['REF', 'ZH', '000511031001', None],
    ['HL', '3', '2', '22', '1'],
    ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJE88001567901', None, None],
    ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', 'PA', '1'],
    ['NM1', 'DN', '1', 'SANSANO JR', 'MICHAEL', '', '', '', '24', '161505558', None, None],
    ['REF', 'ZH', '000511031001', None],
    ['N3', '515 ABBOTT ROAD', 'SUITE 206'],
    ['N4', 'BUFFALO', 'NY', '14220', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'SC', '', '', ['', None, None], '', '', '', '', 'Y'],
    ['DTP', '472', 'RD8', '20071012-20071110'],
    ['SE', Decimal('20'), '242872'],
    ['GE', Decimal('1'), Decimal('241972')],
    ['IEA', Decimal('1'), Decimal('242872')],

    ['ISA', '03', 'HEALTHNOW ', '00', 'HEALTHNOW ', 'ZZ', 'KALEIDAHEALTH01', 'ZZ', 'KaleidaHealth01', datetime.date(2007, 10, 15), datetime.time(9, 5), 'U', '00401', Decimal('905310466'), '0', 'T', ':'],
    ['GS', 'HI', '2000002', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), Decimal('905310467'), 'X', '004010X059'],
    ['ST', '278', '905310467'],
    ['BHT', '0083', '28', '278R2   6370177   3CWW585', datetime.date(2007, 10, 15), datetime.time(9, 5), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', '', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '2', '', '', '', '', '', '24', '161533232', None, None],
    ['REF', 'ZH', '000000001000', None],
    ['HL', '3', '2', '22', '1'],
    ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJP88045401902', None, None],
    ['HL', '4', '3', 'SS', '0'],
    ['TRN', '1', 'CWW585', '9999999999', '6370177'],
    ['UM', 'AR', '', '', ['', None, None], '', '', '', '', 'Y'],
    ['DTP', '472', 'RD8', '20071015-20071114'],
    ['SE', Decimal('14'), '905310467'],
    ['GE', Decimal('1'), Decimal('905310467')],
    ['IEA', Decimal('1'), Decimal('905310466')],

    ['ISA', '03', 'cww585    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), 'U', '00401', Decimal('246782'), '0', 'T', ':'],
    ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', datetime.date(2007, 10, 15), datetime.time(9, 5), Decimal('245882'), 'X', '004010X059'],
    ['ST', '278', '246782'],
    ['BHT', '0083', '28', 'JNPLOLKXXOBO', datetime.date(2007, 10, 15), datetime.time(9, 5), None],
    ['HL', '1', '', '20', '1'],
    ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
    ['HL', '2', '1', '21', '1'],
    ['NM1', '1P', '2', 'BUFFALO GENERAL HOSPITAL', '', '', '', '', '24', '161533232', None, None],
    ['REF', 'ZH', '000000001000', None],
    ['HL', '3', '2', '22', '1'],
    ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJP88045401902', None, None],
    ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
    ['HL', '4', '3', 'PA', '1'],
    ['NM1', 'DN', '2', 'BUFFALO GENERAL HOSPITAL', '', '', '', '', '24', '161533232', None, None],
    ['REF', 'ZH', '000000001000', None],
    ['N3', '100 HIGH STREET', None],
    ['N4', 'BUFFALO', 'NY', '14203', None, None, None],
    ['HL', '5', '4', 'SS', '0'],
    ['TRN', '1', '1', '9999955204', None],
    ['UM', 'AR', '', '', ['', None, None], '', '', '', '', 'Y'],
    ['DTP', '472', 'RD8', '20071015-20071113'],
    ['SE', Decimal('20'), '246782'],
    ['GE', Decimal('1'), Decimal('245882')],
    ['IEA', Decimal('1'), Decimal('246782')],
]


def test_278_28_txns_soa() -> None:
    """
    Transaction set, Multiple messages in a single file.

    We don't seem to have the proper definition
    for this particular set of transactions.

    It seems to require msg_278_4010_X059.
    """
    example = EXAMPLES / "TEST 278_28 TXNS_SOA.txt"
    document = Source(example.read_text())
    # Requires msg_278_4010_X059, which we don't seem to have source for.
    errors_here = [
        "*_GS:gs08:Enumerated",  # Bypass version check.
        # Bypass other incompatibilities in version??
        "*_BHT:bht01:Enumerated",
        "*_BHT:bht02:Enumerated",
        "*_HL:hl03:Enumerated",
        "*_HL:hl04:Enumerated",
        "*_NM1:nm101:Enumerated",
        "*_NM1:nm102:Enumerated",
        "*_NM1:nm108:Enumerated",
        "*_REF:ref01:Enumerated",
        "*_UM:um02:MinLen",
        "*_UM:um02:Enumerated",
        "*_UM:um04_01:MinLen",
        "*_DTP:dtp01:Enumerated",
    ]
    parser = X12Parser(msg_278_4010_X094_27_A1.MSG278, skip_validation=errors_here)
    msg = parser.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    assert list(msg.segment_iter()) == expected_278_28_txns_soa
