"""
820.5010.X218.v2
Created 2023-03-25 09:22:28.312330
"""
from .base import *
from . import common


class ST_LOOP_ST01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ST01 data_ele=143',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['820']}]}}
        datatype = common.D_143
        codes = ['820']
        min_len = 3
        max_len = 3


class ST_LOOP_ST02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ST02 data_ele=329',
         'sequence': 2,
         'type': {'$ref': '#/$common/329'}}
        datatype = common.D_329
        min_len = 4
        max_len = 9


class ST_LOOP_ST03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ST03 data_ele=1705',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1705'}, {'enum': ['005010X218']}]}}
        datatype = common.D_1705
        codes = ['005010X218']
        min_len = 1
        max_len = 35


class ST_LOOP_ST(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ST name=',
         'position': 100,
         'type': 'object',
         'properties': {'xid': {'literal': 'ST'},
                        'st01': {'$ref': '#/$elements/ST_LOOP_ST01'},
                        'st02': {'$ref': '#/$elements/ST_LOOP_ST02'},
                        'st03': {'$ref': '#/$elements/ST_LOOP_ST03'}},
         'required': ['st01', 'st02', 'st03']}
        segment_name = 'ST'
    st01: ST_LOOP_ST01
    st02: ST_LOOP_ST02
    st03: ST_LOOP_ST03


class HEADER_BPR01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BPR01 data_ele=305',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/305'},
                            {'enum': ['C', 'D', 'I', 'P', 'U', 'X']}]}}
        datatype = common.D_305
        codes = ['C', 'D', 'I', 'P', 'U', 'X']
        min_len = 1
        max_len = 2


class HEADER_BPR02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BPR02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class HEADER_BPR03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BPR03 data_ele=478',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/478'}, {'enum': ['C']}]}}
        datatype = common.D_478
        codes = ['C']
        min_len = 1
        max_len = 1


class HEADER_BPR04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BPR04 data_ele=591',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/591'},
                            {'enum': ['ACH', 'BOP', 'CHK', 'FWT', 'NON', 'SWT']}]}}
        datatype = common.D_591
        codes = ['ACH', 'BOP', 'CHK', 'FWT', 'NON', 'SWT']
        min_len = 3
        max_len = 3


class HEADER_BPR05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR05 data_ele=812',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/812'}, {'enum': ['CCP', 'CTX']}]}}
        datatype = common.D_812
        codes = ['CCP', 'CTX']
        min_len = 1
        max_len = 10


class HEADER_BPR06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR06 data_ele=506',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/506'}, {'enum': ['01', '02', '04']}]}}
        datatype = common.D_506
        codes = ['01', '02', '04']
        min_len = 2
        max_len = 2


class HEADER_BPR07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR07 data_ele=507',
         'sequence': 7,
         'type': {'$ref': '#/$common/507'}}
        datatype = common.D_507
        min_len = 3
        max_len = 12


class HEADER_BPR08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR08 data_ele=569',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/569'}, {'enum': ['ALC', 'DA']}]}}
        datatype = common.D_569
        codes = ['ALC', 'DA']
        min_len = 1
        max_len = 3


class HEADER_BPR09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR09 data_ele=508',
         'sequence': 9,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class HEADER_BPR10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BPR10 data_ele=509',
         'sequence': 10,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class HEADER_BPR11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR11 data_ele=510',
         'sequence': 11,
         'type': {'$ref': '#/$common/510'}}
        datatype = common.D_510
        min_len = 9
        max_len = 9


class HEADER_BPR12(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR12 data_ele=506',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/506'}, {'enum': ['01', '02', '04']}]}}
        datatype = common.D_506
        codes = ['01', '02', '04']
        min_len = 2
        max_len = 2


class HEADER_BPR13(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR13 data_ele=507',
         'sequence': 13,
         'type': {'$ref': '#/$common/507'}}
        datatype = common.D_507
        min_len = 3
        max_len = 12


class HEADER_BPR14(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR14 data_ele=569',
         'sequence': 14,
         'type': {'allOf': [{'$ref': '#/$common/569'}, {'enum': ['DA', 'SG']}]}}
        datatype = common.D_569
        codes = ['DA', 'SG']
        min_len = 1
        max_len = 3


class HEADER_BPR15(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BPR15 data_ele=508',
         'sequence': 15,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class HEADER_BPR16(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BPR16 data_ele=373',
         'sequence': 16,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BPR17(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=BPR17 data_ele=1048',
         'sequence': 17,
         'type': {'$ref': '#/$common/1048'}}
        datatype = common.D_1048
        min_len = 1
        max_len = 3


class HEADER_BPR18(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=BPR18 data_ele=506',
         'sequence': 18,
         'type': {'$ref': '#/$common/506'}}
        datatype = common.D_506
        min_len = 2
        max_len = 2


class HEADER_BPR19(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=BPR19 data_ele=507',
         'sequence': 19,
         'type': {'$ref': '#/$common/507'}}
        datatype = common.D_507
        min_len = 3
        max_len = 12


class HEADER_BPR20(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=BPR20 data_ele=569',
         'sequence': 20,
         'type': {'$ref': '#/$common/569'}}
        datatype = common.D_569
        min_len = 1
        max_len = 3


class HEADER_BPR21(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=BPR21 data_ele=508',
         'sequence': 21,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class HEADER_BPR(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BPR name=',
         'position': 200,
         'syntax': ['P0607', 'C0809', 'P1213', 'C1415', 'P1819', 'C2021'],
         'type': 'object',
         'properties': {'xid': {'literal': 'BPR'},
                        'bpr01': {'$ref': '#/$elements/HEADER_BPR01'},
                        'bpr02': {'$ref': '#/$elements/HEADER_BPR02'},
                        'bpr03': {'$ref': '#/$elements/HEADER_BPR03'},
                        'bpr04': {'$ref': '#/$elements/HEADER_BPR04'},
                        'bpr05': {'$ref': '#/$elements/HEADER_BPR05'},
                        'bpr06': {'$ref': '#/$elements/HEADER_BPR06'},
                        'bpr07': {'$ref': '#/$elements/HEADER_BPR07'},
                        'bpr08': {'$ref': '#/$elements/HEADER_BPR08'},
                        'bpr09': {'$ref': '#/$elements/HEADER_BPR09'},
                        'bpr10': {'$ref': '#/$elements/HEADER_BPR10'},
                        'bpr11': {'$ref': '#/$elements/HEADER_BPR11'},
                        'bpr12': {'$ref': '#/$elements/HEADER_BPR12'},
                        'bpr13': {'$ref': '#/$elements/HEADER_BPR13'},
                        'bpr14': {'$ref': '#/$elements/HEADER_BPR14'},
                        'bpr15': {'$ref': '#/$elements/HEADER_BPR15'},
                        'bpr16': {'$ref': '#/$elements/HEADER_BPR16'}},
         'required': ['bpr01', 'bpr02', 'bpr03', 'bpr04', 'bpr10', 'bpr16']}
        segment_name = 'BPR'
    bpr01: HEADER_BPR01
    bpr02: HEADER_BPR02
    bpr03: HEADER_BPR03
    bpr04: HEADER_BPR04
    bpr05: HEADER_BPR05 | None
    bpr06: HEADER_BPR06 | None
    bpr07: HEADER_BPR07 | None
    bpr08: HEADER_BPR08 | None
    bpr09: HEADER_BPR09 | None
    bpr10: HEADER_BPR10
    bpr11: HEADER_BPR11 | None
    bpr12: HEADER_BPR12 | None
    bpr13: HEADER_BPR13 | None
    bpr14: HEADER_BPR14 | None
    bpr15: HEADER_BPR15 | None
    bpr16: HEADER_BPR16


class HEADER_TRN01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['1', '3']}]}}
        datatype = common.D_481
        codes = ['1', '3']
        min_len = 1
        max_len = 2


class HEADER_TRN02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_TRN03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class HEADER_TRN04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_TRN(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=TRN name=',
         'position': 350,
         'type': 'object',
         'properties': {'xid': {'literal': 'TRN'},
                        'trn01': {'$ref': '#/$elements/HEADER_TRN01'},
                        'trn02': {'$ref': '#/$elements/HEADER_TRN02'},
                        'trn03': {'$ref': '#/$elements/HEADER_TRN03'},
                        'trn04': {'$ref': '#/$elements/HEADER_TRN04'}},
         'required': ['trn01', 'trn02']}
        segment_name = 'TRN'
    trn01: HEADER_TRN01
    trn02: HEADER_TRN02
    trn03: HEADER_TRN03 | None
    trn04: HEADER_TRN04 | None


class HEADER_CUR01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=CUR01 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['2B', 'PR']}]}}
        datatype = common.D_98
        codes = ['2B', 'PR']
        min_len = 2
        max_len = 3


class HEADER_CUR02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=CUR02 data_ele=100',
         'sequence': 2,
         'type': {'$ref': '#/$common/100'}}
        datatype = common.D_100
        codes = common.currency
        min_len = 3
        max_len = 3


class HEADER_CUR03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR03 data_ele=280',
         'sequence': 3,
         'type': {'$ref': '#/$common/280'}}
        datatype = common.D_280
        min_len = 4
        max_len = 10


class HEADER_CUR04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR04 data_ele=98',
         'sequence': 4,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class HEADER_CUR05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR05 data_ele=100',
         'sequence': 5,
         'type': {'$ref': '#/$common/100'}}
        datatype = common.D_100
        min_len = 3
        max_len = 3


class HEADER_CUR06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR06 data_ele=669',
         'sequence': 6,
         'type': {'$ref': '#/$common/669'}}
        datatype = common.D_669
        min_len = 3
        max_len = 3


class HEADER_CUR07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR07 data_ele=374',
         'sequence': 7,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class HEADER_CUR08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_CUR09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR09 data_ele=337',
         'sequence': 9,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_CUR10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR10 data_ele=374',
         'sequence': 10,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class HEADER_CUR11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR11 data_ele=373',
         'sequence': 11,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_CUR12(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR12 data_ele=337',
         'sequence': 12,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_CUR13(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR13 data_ele=374',
         'sequence': 13,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class HEADER_CUR14(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR14 data_ele=373',
         'sequence': 14,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_CUR15(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR15 data_ele=337',
         'sequence': 15,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_CUR16(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR16 data_ele=374',
         'sequence': 16,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class HEADER_CUR17(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR17 data_ele=373',
         'sequence': 17,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_CUR18(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR18 data_ele=337',
         'sequence': 18,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_CUR19(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR19 data_ele=374',
         'sequence': 19,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class HEADER_CUR20(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR20 data_ele=373',
         'sequence': 20,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_CUR21(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=CUR21 data_ele=337',
         'sequence': 21,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_CUR(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=CUR name=',
         'position': 400,
         'syntax': ['C0807', 'C0907', 'L101112', 'C1110', 'C1210', 'L131415', 'C1413',
                    'C1513', 'L161718', 'C1716', 'C1816', 'L192021', 'C2019', 'C2119'],
         'type': 'object',
         'properties': {'xid': {'literal': 'CUR'},
                        'cur01': {'$ref': '#/$elements/HEADER_CUR01'},
                        'cur02': {'$ref': '#/$elements/HEADER_CUR02'}},
         'required': ['cur01', 'cur02']}
        segment_name = 'CUR'
    cur01: HEADER_CUR01
    cur02: HEADER_CUR02


class HEADER_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['14', '17', '18', '2F', '38', '72', 'LB']}]}}
        datatype = common.D_128
        codes = ['14', '17', '18', '2F', '38', '72', 'LB']
        min_len = 2
        max_len = 3


class HEADER_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class HEADER_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class HEADER_REF(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=REF name=',
                   'position': 500,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                                  'ref02': {'$ref': '#/$elements/HEADER_REF02'}},
                   'required': ['ref01', 'ref02']}}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02


class HEADER_DTM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['009']}]}}
        datatype = common.D_374
        codes = ['009']
        min_len = 3
        max_len = 3


class HEADER_DTM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_DTM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_DTM04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class HEADER_DTM05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class HEADER_DTM06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class HEADER_DTM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM name=',
         'position': 600,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/HEADER_DTM01'},
                        'dtm02': {'$ref': '#/$elements/HEADER_DTM02'}},
         'required': ['dtm01', 'dtm02']}
        segment_name = 'DTM'
    dtm01: HEADER_DTM01
    dtm02: HEADER_DTM02


class HEADER_DTM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['035']}]}}
        datatype = common.D_374
        codes = ['035']
        min_len = 3
        max_len = 3


class HEADER_DTM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_DTM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_DTM04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class HEADER_DTM05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class HEADER_DTM06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class HEADER_DTM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM name=',
         'position': 600,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/HEADER_DTM01'},
                        'dtm02': {'$ref': '#/$elements/HEADER_DTM02'}},
         'required': ['dtm01', 'dtm02']}
        segment_name = 'DTM'
    dtm01: HEADER_DTM01
    dtm02: HEADER_DTM02


class HEADER_DTM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['582']}]}}
        datatype = common.D_374
        codes = ['582']
        min_len = 3
        max_len = 3


class HEADER_DTM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_DTM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_DTM04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class HEADER_DTM05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['RD8']}]}}
        datatype = common.D_1250
        codes = ['RD8']
        min_len = 2
        max_len = 3


class HEADER_DTM06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class HEADER_DTM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM name=',
         'position': 600,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/HEADER_DTM01'},
                        'dtm05': {'$ref': '#/$elements/HEADER_DTM05'},
                        'dtm06': {'$ref': '#/$elements/HEADER_DTM06'}},
         'required': ['dtm01', 'dtm05', 'dtm06']}
        segment_name = 'DTM'
    dtm01: HEADER_DTM01
    dtm05: HEADER_DTM05
    dtm06: HEADER_DTM06


class HEADER_DTM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['097']}]}}
        datatype = common.D_374
        codes = ['097']
        min_len = 3
        max_len = 3


class HEADER_DTM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_DTM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_DTM04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class HEADER_DTM05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class HEADER_DTM06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class HEADER_DTM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM name=',
         'position': 600,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/HEADER_DTM01'},
                        'dtm02': {'$ref': '#/$elements/HEADER_DTM02'}},
         'required': ['dtm01', 'dtm02']}
        segment_name = 'DTM'
    dtm01: HEADER_DTM01
    dtm02: HEADER_DTM02


class L1000A_N101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PE']}]}}
        datatype = common.D_98
        codes = ['PE']
        min_len = 2
        max_len = 3


class L1000A_N102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000A_N103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['1', '9', 'EQ', 'FI', 'XV']}]}}
        datatype = common.D_66
        codes = ['1', '9', 'EQ', 'FI', 'XV']
        min_len = 1
        max_len = 2


class L1000A_N104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000A_N105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L1000A_N106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L1000A_N1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N1 name=',
         'position': 700,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000A_N101'},
                        'n102': {'$ref': '#/$elements/L1000A_N102'},
                        'n103': {'$ref': '#/$elements/L1000A_N103'},
                        'n104': {'$ref': '#/$elements/L1000A_N104'}},
         'required': ['n101']}
        segment_name = 'N1'
    n101: L1000A_N101
    n102: L1000A_N102 | None
    n103: L1000A_N103 | None
    n104: L1000A_N104 | None


class L1000A_N201(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N201 data_ele=93',
         'sequence': 1,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000A_N202(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N202 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000A_N2(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N2 name=',
         'position': 800,
         'type': 'object',
         'properties': {'xid': {'literal': 'N2'},
                        'n201': {'$ref': '#/$elements/L1000A_N201'}},
         'required': ['n201']}
        segment_name = 'N2'
    n201: L1000A_N201


class L1000A_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000A_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000A_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 900,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L1000A_N301'},
                        'n302': {'$ref': '#/$elements/L1000A_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L1000A_N301
    n302: L1000A_N302 | None


class L1000A_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L1000A_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L1000A_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L1000A_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L1000A_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L1000A_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L1000A_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'sequence': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L1000A_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 1000,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L1000A_N401'},
                        'n402': {'$ref': '#/$elements/L1000A_N402'},
                        'n403': {'$ref': '#/$elements/L1000A_N403'},
                        'n404': {'$ref': '#/$elements/L1000A_N404'},
                        'n407': {'$ref': '#/$elements/L1000A_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L1000A_N401
    n402: L1000A_N402 | None
    n403: L1000A_N403 | None
    n404: L1000A_N404 | None
    n407: L1000A_N407 | None


class L1000A_RDM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RDM01 data_ele=756',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/756'},
                            {'enum': ['BM', 'EM', 'FT', 'FX', 'IA', 'OL']}]}}
        datatype = common.D_756
        codes = ['BM', 'EM', 'FT', 'FX', 'IA', 'OL']
        min_len = 1
        max_len = 2


class L1000A_RDM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=RDM02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000A_RDM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=RDM03 data_ele=364',
         'sequence': 3,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000A_RDM04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RDM04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L1000A_RDM05(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RDM05 name= refdes= data_ele=C040',
         'sequence': 5,
         'syntax': []}


class L1000A_RDM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=RDM name=',
         'position': 1300,
         'type': 'object',
         'properties': {'xid': {'literal': 'RDM'},
                        'rdm01': {'$ref': '#/$elements/L1000A_RDM01'},
                        'rdm02': {'$ref': '#/$elements/L1000A_RDM02'},
                        'rdm03': {'$ref': '#/$elements/L1000A_RDM03'}},
         'required': ['rdm01']}
        segment_name = 'RDM'
    rdm01: L1000A_RDM01
    rdm02: L1000A_RDM02 | None
    rdm03: L1000A_RDM03 | None


class L1000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=1000A name= type=None',
                   'position': 700,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000A_N1'},
                                  'n2': {'$ref': '#/$segments/L1000A_N2'},
                                  'n3': {'$ref': '#/$segments/L1000A_N3'},
                                  'n4': {'$ref': '#/$segments/L1000A_N4'},
                                  'rdm': {'$ref': '#/$segments/L1000A_RDM'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000A_N1
    n2: L1000A_N2 | None
    n3: L1000A_N3 | None
    n4: L1000A_N4 | None
    rdm: L1000A_RDM | None


class L1000B_N101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PR']}]}}
        datatype = common.D_98
        codes = ['PR']
        min_len = 2
        max_len = 3


class L1000B_N102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000B_N103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['1', '24', '75', '9', 'EQ', 'FI', 'PI']}]}}
        datatype = common.D_66
        codes = ['1', '24', '75', '9', 'EQ', 'FI', 'PI']
        min_len = 1
        max_len = 2


class L1000B_N104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000B_N105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L1000B_N106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L1000B_N1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N1 name=',
         'position': 700,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000B_N101'},
                        'n102': {'$ref': '#/$elements/L1000B_N102'},
                        'n103': {'$ref': '#/$elements/L1000B_N103'},
                        'n104': {'$ref': '#/$elements/L1000B_N104'}},
         'required': ['n101']}
        segment_name = 'N1'
    n101: L1000B_N101
    n102: L1000B_N102 | None
    n103: L1000B_N103 | None
    n104: L1000B_N104 | None


class L1000B_N201(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N201 data_ele=93',
         'sequence': 1,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000B_N202(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N202 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000B_N2(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N2 name=',
         'position': 800,
         'type': 'object',
         'properties': {'xid': {'literal': 'N2'},
                        'n201': {'$ref': '#/$elements/L1000B_N201'}},
         'required': ['n201']}
        segment_name = 'N2'
    n201: L1000B_N201


class L1000B_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000B_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000B_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 900,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L1000B_N301'},
                        'n302': {'$ref': '#/$elements/L1000B_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L1000B_N301
    n302: L1000B_N302 | None


class L1000B_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L1000B_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L1000B_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L1000B_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L1000B_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L1000B_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L1000B_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'sequence': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L1000B_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 1000,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L1000B_N401'},
                        'n402': {'$ref': '#/$elements/L1000B_N402'},
                        'n403': {'$ref': '#/$elements/L1000B_N403'},
                        'n404': {'$ref': '#/$elements/L1000B_N404'},
                        'n407': {'$ref': '#/$elements/L1000B_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L1000B_N401
    n402: L1000B_N402 | None
    n403: L1000B_N403 | None
    n404: L1000B_N404 | None
    n407: L1000B_N407 | None


class L1000B_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L1000B_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000B_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L1000B_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000B_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L1000B_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000B_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L1000B_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000B_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'sequence': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L1000B_PER(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=PER name=',
                   'position': 1200,
                   'syntax': ['P0304', 'P0506', 'P0708'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L1000B_PER01'},
                                  'per02': {'$ref': '#/$elements/L1000B_PER02'},
                                  'per03': {'$ref': '#/$elements/L1000B_PER03'},
                                  'per04': {'$ref': '#/$elements/L1000B_PER04'},
                                  'per05': {'$ref': '#/$elements/L1000B_PER05'},
                                  'per06': {'$ref': '#/$elements/L1000B_PER06'},
                                  'per07': {'$ref': '#/$elements/L1000B_PER07'},
                                  'per08': {'$ref': '#/$elements/L1000B_PER08'}},
                   'required': ['per01', 'per02', 'per03', 'per04']}}
        segment_name = 'PER'
    per01: L1000B_PER01
    per02: L1000B_PER02
    per03: L1000B_PER03
    per04: L1000B_PER04
    per05: L1000B_PER05 | None
    per06: L1000B_PER06 | None
    per07: L1000B_PER07 | None
    per08: L1000B_PER08 | None


class L1000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=1000B name= type=None',
                   'position': 1500,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000B_N1'},
                                  'n2': {'$ref': '#/$segments/L1000B_N2'},
                                  'n3': {'$ref': '#/$segments/L1000B_N3'},
                                  'n4': {'$ref': '#/$segments/L1000B_N4'},
                                  'per': {'$ref': '#/$segments/L1000B_PER'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000B_N1
    n2: L1000B_N2 | None
    n3: L1000B_N3 | None
    n4: L1000B_N4 | None
    per: list[L1000B_PER] | None


class L1000C_N101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['04', '0B', '8W', 'AK', 'BE', 'BK', 'C1', 'C2',
                                      'IAT', 'MJ', 'RB', 'Z6', 'ZB', 'ZL']}]}}
        datatype = common.D_98
        codes = ['04', '0B', '8W', 'AK', 'BE', 'BK', 'C1', 'C2', 'IAT', 'MJ', 'RB', 'Z6', 'ZB', 'ZL']
        min_len = 2
        max_len = 3


class L1000C_N102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000C_N103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['31', '57', '94', 'A3', 'A4', 'A6', 'CF', 'G',
                                      'PA']}]}}
        datatype = common.D_66
        codes = ['31', '57', '94', 'A3', 'A4', 'A6', 'CF', 'G', 'PA']
        min_len = 1
        max_len = 2


class L1000C_N104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000C_N105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L1000C_N106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L1000C_N1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N1 name=',
         'position': 700,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000C_N101'},
                        'n102': {'$ref': '#/$elements/L1000C_N102'},
                        'n103': {'$ref': '#/$elements/L1000C_N103'},
                        'n104': {'$ref': '#/$elements/L1000C_N104'}},
         'required': ['n101']}
        segment_name = 'N1'
    n101: L1000C_N101
    n102: L1000C_N102 | None
    n103: L1000C_N103 | None
    n104: L1000C_N104 | None


class L1000C_N201(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N201 data_ele=93',
         'sequence': 1,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000C_N202(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N202 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000C_N2(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N2 name=',
         'position': 800,
         'type': 'object',
         'properties': {'xid': {'literal': 'N2'},
                        'n201': {'$ref': '#/$elements/L1000C_N201'}},
         'required': ['n201']}
        segment_name = 'N2'
    n201: L1000C_N201


class L1000C_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000C_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000C_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 900,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L1000C_N301'},
                        'n302': {'$ref': '#/$elements/L1000C_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L1000C_N301
    n302: L1000C_N302 | None


class L1000C_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L1000C_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L1000C_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L1000C_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L1000C_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L1000C_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L1000C_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'sequence': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L1000C_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 1000,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L1000C_N401'},
                        'n402': {'$ref': '#/$elements/L1000C_N402'},
                        'n403': {'$ref': '#/$elements/L1000C_N403'},
                        'n404': {'$ref': '#/$elements/L1000C_N404'},
                        'n407': {'$ref': '#/$elements/L1000C_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L1000C_N401
    n402: L1000C_N402 | None
    n403: L1000C_N403 | None
    n404: L1000C_N404 | None
    n407: L1000C_N407 | None


class L1000C_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L1000C_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000C_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L1000C_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000C_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L1000C_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000C_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L1000C_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000C_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'sequence': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L1000C_PER(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=PER name=',
                   'position': 1200,
                   'syntax': ['P0304', 'P0506', 'P0708'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L1000C_PER01'},
                                  'per02': {'$ref': '#/$elements/L1000C_PER02'},
                                  'per03': {'$ref': '#/$elements/L1000C_PER03'},
                                  'per04': {'$ref': '#/$elements/L1000C_PER04'},
                                  'per05': {'$ref': '#/$elements/L1000C_PER05'},
                                  'per06': {'$ref': '#/$elements/L1000C_PER06'},
                                  'per07': {'$ref': '#/$elements/L1000C_PER07'},
                                  'per08': {'$ref': '#/$elements/L1000C_PER08'}},
                   'required': ['per01', 'per02', 'per03', 'per04']}}
        segment_name = 'PER'
    per01: L1000C_PER01
    per02: L1000C_PER02
    per03: L1000C_PER03
    per04: L1000C_PER04
    per05: L1000C_PER05 | None
    per06: L1000C_PER06 | None
    per07: L1000C_PER07 | None
    per08: L1000C_PER08 | None


class L1000C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=1000C name= type=None',
                   'position': 2300,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000C_N1'},
                                  'n2': {'$ref': '#/$segments/L1000C_N2'},
                                  'n3': {'$ref': '#/$segments/L1000C_N3'},
                                  'n4': {'$ref': '#/$segments/L1000C_N4'},
                                  'per': {'$ref': '#/$segments/L1000C_PER'}},
                   'required': ['n1']},
         'maxItems': 14}
    n1: L1000C_N1
    n2: L1000C_N2 | None
    n3: L1000C_N3 | None
    n4: L1000C_N4 | None
    per: list[L1000C_PER] | None


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=HEADER name= type=wrapper',
                   'position': 110,
                   'type': 'object',
                   'properties': {'bpr': {'$ref': '#/$segments/HEADER_BPR'},
                                  'trn': {'$ref': '#/$segments/HEADER_TRN'},
                                  'cur': {'$ref': '#/$segments/HEADER_CUR'},
                                  'ref': {'$ref': '#/$segments/HEADER_REF'},
                                  'dtm': {'$ref': '#/$segments/HEADER_DTM'},
                                  'l1000a': {'$ref': '#/$segments/L1000A'},
                                  'l1000b': {'$ref': '#/$segments/L1000B'},
                                  'l1000c': {'$ref': '#/$segments/L1000C'}},
                   'required': ['bpr', 'trn', 'l1000a', 'l1000b']},
         'maxItems': 1}
    bpr: HEADER_BPR
    trn: HEADER_TRN
    cur: HEADER_CUR | None
    ref: list[HEADER_REF] | None
    dtm: HEADER_DTM | None
    dtm: HEADER_DTM | None
    dtm: HEADER_DTM | None
    dtm: HEADER_DTM | None
    l1000a: list[L1000A]
    l1000b: list[L1000B]
    l1000c: list[L1000C] | None


class L2000A_ENT01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT01 data_ele=554',
         'sequence': 1,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2000A_ENT02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT02 data_ele=98',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['2L', 'AG', 'NH', 'RGA', 'UN']}]}}
        datatype = common.D_98
        codes = ['2L', 'AG', 'NH', 'RGA', 'UN']
        min_len = 2
        max_len = 3


class L2000A_ENT03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT03 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['1', '24', '9', 'FI']}]}}
        datatype = common.D_66
        codes = ['1', '24', '9', 'FI']
        min_len = 1
        max_len = 2


class L2000A_ENT04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT04 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2000A_ENT05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT05 data_ele=98',
         'sequence': 5,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2000A_ENT06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT06 data_ele=66',
         'sequence': 6,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L2000A_ENT07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT07 data_ele=67',
         'sequence': 7,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2000A_ENT08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT08 data_ele=128',
         'sequence': 8,
         'type': {'$ref': '#/$common/128'}}
        datatype = common.D_128
        min_len = 2
        max_len = 3


class L2000A_ENT09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT09 data_ele=127',
         'sequence': 9,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000A_ENT(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT name=',
         'position': 100,
         'syntax': ['P020304', 'P050607', 'P0809'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ENT'},
                        'ent01': {'$ref': '#/$elements/L2000A_ENT01'},
                        'ent02': {'$ref': '#/$elements/L2000A_ENT02'},
                        'ent03': {'$ref': '#/$elements/L2000A_ENT03'},
                        'ent04': {'$ref': '#/$elements/L2000A_ENT04'}},
         'required': ['ent01', 'ent02', 'ent03', 'ent04']}
        segment_name = 'ENT'
    ent01: L2000A_ENT01
    ent02: L2000A_ENT02
    ent03: L2000A_ENT03
    ent04: L2000A_ENT04


class L2200A_ADX01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX01 data_ele=782',
         'sequence': 1,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200A_ADX02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX02 data_ele=426',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/426'},
                            {'enum': ['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6',
                                      'RU', 'WO', 'WW']}]}}
        datatype = common.D_426
        codes = ['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6', 'RU', 'WO', 'WW']
        min_len = 2
        max_len = 2


class L2200A_ADX03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX03 data_ele=128',
         'sequence': 3,
         'type': {'$ref': '#/$common/128'}}
        datatype = common.D_128
        min_len = 2
        max_len = 3


class L2200A_ADX04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200A_ADX(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX name=',
         'position': 800,
         'syntax': ['P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ADX'},
                        'adx01': {'$ref': '#/$elements/L2200A_ADX01'},
                        'adx02': {'$ref': '#/$elements/L2200A_ADX02'}},
         'required': ['adx01', 'adx02']}
        segment_name = 'ADX'
    adx01: L2200A_ADX01
    adx02: L2200A_ADX02


class L2200A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2200A name= type=None',
                   'position': 800,
                   'type': 'object',
                   'properties': {'adx': {'$ref': '#/$segments/L2200A_ADX'}},
                   'required': ['adx']}}
    adx: L2200A_ADX


class L2300A_RMR01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['11', '1L', 'CT', 'IK']}]}}
        datatype = common.D_128
        codes = ['11', '1L', 'CT', 'IK']
        min_len = 2
        max_len = 3


class L2300A_RMR02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300A_RMR03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=RMR03 data_ele=482',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/482'},
                            {'enum': ['PA', 'PI', 'PO', 'PP']}]}}
        datatype = common.D_482
        codes = ['PA', 'PI', 'PO', 'PP']
        min_len = 2
        max_len = 2


class L2300A_RMR04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300A_RMR05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=RMR05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300A_RMR06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RMR06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300A_RMR07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RMR07 data_ele=426',
         'sequence': 7,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class L2300A_RMR08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RMR08 data_ele=782',
         'sequence': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300A_RMR(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR name=',
         'position': 1500,
         'syntax': ['P0102', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'RMR'},
                        'rmr01': {'$ref': '#/$elements/L2300A_RMR01'},
                        'rmr02': {'$ref': '#/$elements/L2300A_RMR02'},
                        'rmr03': {'$ref': '#/$elements/L2300A_RMR03'},
                        'rmr04': {'$ref': '#/$elements/L2300A_RMR04'},
                        'rmr05': {'$ref': '#/$elements/L2300A_RMR05'}},
         'required': ['rmr01', 'rmr02', 'rmr04']}
        segment_name = 'RMR'
    rmr01: L2300A_RMR01
    rmr02: L2300A_RMR02
    rmr03: L2300A_RMR03 | None
    rmr04: L2300A_RMR04
    rmr05: L2300A_RMR05 | None


class L2300A_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['14', '17', '18', '2F', '38', 'E9', 'LB', 'LU',
                                      'ZZ']}]}}
        datatype = common.D_128
        codes = ['14', '17', '18', '2F', '38', 'E9', 'LB', 'LU', 'ZZ']
        min_len = 2
        max_len = 3


class L2300A_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300A_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300A_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300A_REF(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=REF name=',
                   'position': 1700,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300A_REF02'}},
                   'required': ['ref01', 'ref02']}}
        segment_name = 'REF'
    ref01: L2300A_REF01
    ref02: L2300A_REF02


class L2300A_DTM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['582', 'AAG']}]}}
        datatype = common.D_374
        codes = ['582', 'AAG']
        min_len = 3
        max_len = 3


class L2300A_DTM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2300A_DTM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2300A_DTM04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L2300A_DTM05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['RD8']}]}}
        datatype = common.D_1250
        codes = ['RD8']
        min_len = 2
        max_len = 3


class L2300A_DTM06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300A_DTM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM name=',
         'position': 1800,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/L2300A_DTM01'},
                        'dtm02': {'$ref': '#/$elements/L2300A_DTM02'},
                        'dtm05': {'$ref': '#/$elements/L2300A_DTM05'},
                        'dtm06': {'$ref': '#/$elements/L2300A_DTM06'}},
         'required': ['dtm01']}
        segment_name = 'DTM'
    dtm01: L2300A_DTM01
    dtm02: L2300A_DTM02 | None
    dtm05: L2300A_DTM05 | None
    dtm06: L2300A_DTM06 | None


class L2310A_IT101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=IT101 data_ele=350',
         'sequence': 1,
         'type': {'$ref': '#/$common/350'}}
        datatype = common.D_350
        min_len = 1
        max_len = 20


class L2310A_IT102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT102 data_ele=358',
         'sequence': 2,
         'type': {'$ref': '#/$common/358'}}
        datatype = common.D_358
        min_len = 1
        max_len = 15


class L2310A_IT103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT103 data_ele=355',
         'sequence': 3,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2310A_IT104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT104 data_ele=212',
         'sequence': 4,
         'type': {'$ref': '#/$common/212'}}
        datatype = common.D_212
        min_len = 1
        max_len = 17


class L2310A_IT105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT105 data_ele=639',
         'sequence': 5,
         'type': {'$ref': '#/$common/639'}}
        datatype = common.D_639
        min_len = 2
        max_len = 2


class L2310A_IT106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT106 data_ele=235',
         'sequence': 6,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT107 data_ele=234',
         'sequence': 7,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT108 data_ele=235',
         'sequence': 8,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT109 data_ele=234',
         'sequence': 9,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT110 data_ele=235',
         'sequence': 10,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT111 data_ele=234',
         'sequence': 11,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT112 data_ele=235',
         'sequence': 12,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT113(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT113 data_ele=234',
         'sequence': 13,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT114(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT114 data_ele=235',
         'sequence': 14,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT115(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT115 data_ele=234',
         'sequence': 15,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT116(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT116 data_ele=235',
         'sequence': 16,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT117(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT117 data_ele=234',
         'sequence': 17,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT118(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT118 data_ele=235',
         'sequence': 18,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT119(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT119 data_ele=234',
         'sequence': 19,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT120(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT120 data_ele=235',
         'sequence': 20,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT121(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT121 data_ele=234',
         'sequence': 21,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT122(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT122 data_ele=235',
         'sequence': 22,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT123(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT123 data_ele=234',
         'sequence': 23,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT124(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT124 data_ele=235',
         'sequence': 24,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2310A_IT125(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=IT125 data_ele=234',
         'sequence': 25,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2310A_IT1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=IT1 name=',
         'position': 1900,
         'syntax': ['P020304', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617',
                    'P1819', 'P2021', 'P2223', 'P2425'],
         'type': 'object',
         'properties': {'xid': {'literal': 'IT1'},
                        'it101': {'$ref': '#/$elements/L2310A_IT101'}},
         'required': ['it101']}
        segment_name = 'IT1'
    it101: L2310A_IT101


class L2312A_SAC01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SAC01 data_ele=248',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/248'}, {'enum': ['C']}]}}
        datatype = common.D_248
        codes = ['C']
        min_len = 1
        max_len = 1


class L2312A_SAC02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SAC02 data_ele=1300',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1300'},
                            {'enum': ['A172', 'B680', 'D940', 'G740']}]}}
        datatype = common.D_1300
        codes = ['A172', 'B680', 'D940', 'G740']
        min_len = 4
        max_len = 4


class L2312A_SAC03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC03 data_ele=559',
         'sequence': 3,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2312A_SAC04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC04 data_ele=1301',
         'sequence': 4,
         'type': {'$ref': '#/$common/1301'}}
        datatype = common.D_1301
        min_len = 1
        max_len = 10


class L2312A_SAC05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SAC05 data_ele=610',
         'sequence': 5,
         'type': {'$ref': '#/$common/610'}}
        datatype = common.D_610
        min_len = 1
        max_len = 15


class L2312A_SAC06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC06 data_ele=378',
         'sequence': 6,
         'type': {'$ref': '#/$common/378'}}
        datatype = common.D_378
        min_len = 1
        max_len = 1


class L2312A_SAC07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC07 data_ele=332',
         'sequence': 7,
         'type': {'$ref': '#/$common/332'}}
        datatype = common.D_332
        min_len = 1
        max_len = 6


class L2312A_SAC08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC08 data_ele=118',
         'sequence': 8,
         'type': {'$ref': '#/$common/118'}}
        datatype = common.D_118
        min_len = 1
        max_len = 9


class L2312A_SAC09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC09 data_ele=355',
         'sequence': 9,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2312A_SAC10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC10 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2312A_SAC11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC11 data_ele=380',
         'sequence': 11,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2312A_SAC12(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC12 data_ele=331',
         'sequence': 12,
         'type': {'$ref': '#/$common/331'}}
        datatype = common.D_331
        min_len = 2
        max_len = 2


class L2312A_SAC13(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC13 data_ele=127',
         'sequence': 13,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2312A_SAC14(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC14 data_ele=770',
         'sequence': 14,
         'type': {'$ref': '#/$common/770'}}
        datatype = common.D_770
        min_len = 1
        max_len = 20


class L2312A_SAC15(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC15 data_ele=352',
         'sequence': 15,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2312A_SAC16(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SAC16 data_ele=819',
         'sequence': 16,
         'type': {'$ref': '#/$common/819'}}
        datatype = common.D_819
        min_len = 2
        max_len = 3


class L2312A_SAC(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SAC name=',
         'position': 2020,
         'syntax': ['R0203', 'P0304', 'P0607', 'P0910', 'C1110', 'C1413', 'C1615'],
         'type': 'object',
         'properties': {'xid': {'literal': 'SAC'},
                        'sac01': {'$ref': '#/$elements/L2312A_SAC01'},
                        'sac02': {'$ref': '#/$elements/L2312A_SAC02'},
                        'sac05': {'$ref': '#/$elements/L2312A_SAC05'}},
         'required': ['sac01', 'sac02', 'sac05']}
        segment_name = 'SAC'
    sac01: L2312A_SAC01
    sac02: L2312A_SAC02
    sac05: L2312A_SAC05


class L2312A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2312A name= type=None',
                   'position': 2020,
                   'type': 'object',
                   'properties': {'sac': {'$ref': '#/$segments/L2312A_SAC'}},
                   'required': ['sac']},
         'maxItems': 4}
    sac: L2312A_SAC


class L2315A_SLN01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SLN01 data_ele=350',
         'sequence': 1,
         'type': {'$ref': '#/$common/350'}}
        datatype = common.D_350
        min_len = 1
        max_len = 20


class L2315A_SLN02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN02 data_ele=350',
         'sequence': 2,
         'type': {'$ref': '#/$common/350'}}
        datatype = common.D_350
        min_len = 1
        max_len = 20


class L2315A_SLN03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SLN03 data_ele=662',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/662'}, {'enum': ['O']}]}}
        datatype = common.D_662
        codes = ['O']
        min_len = 1
        max_len = 1


class L2315A_SLN04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SLN04 data_ele=380',
         'sequence': 4,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2315A_SLN05_01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SLN05-01 data_ele=355',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/355'}, {'enum': ['10', 'IE', 'PR']}]}}
        datatype = common.D_355
        codes = ['10', 'IE', 'PR']
        min_len = 2
        max_len = 2


class L2315A_SLN05_02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-02 data_ele=1018',
         'sequence': 2,
         'type': {'$ref': '#/$common/1018'}}
        datatype = common.D_1018
        min_len = 1
        max_len = 15


class L2315A_SLN05_03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-03 data_ele=649',
         'sequence': 3,
         'type': {'$ref': '#/$common/649'}}
        datatype = common.D_649
        min_len = 1
        max_len = 10


class L2315A_SLN05_04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-04 data_ele=355',
         'sequence': 4,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2315A_SLN05_05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-05 data_ele=1018',
         'sequence': 5,
         'type': {'$ref': '#/$common/1018'}}
        datatype = common.D_1018
        min_len = 1
        max_len = 15


class L2315A_SLN05_06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-06 data_ele=649',
         'sequence': 6,
         'type': {'$ref': '#/$common/649'}}
        datatype = common.D_649
        min_len = 1
        max_len = 10


class L2315A_SLN05_07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-07 data_ele=355',
         'sequence': 7,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2315A_SLN05_08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-08 data_ele=1018',
         'sequence': 8,
         'type': {'$ref': '#/$common/1018'}}
        datatype = common.D_1018
        min_len = 1
        max_len = 15


class L2315A_SLN05_09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-09 data_ele=649',
         'sequence': 9,
         'type': {'$ref': '#/$common/649'}}
        datatype = common.D_649
        min_len = 1
        max_len = 10


class L2315A_SLN05_10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-10 data_ele=355',
         'sequence': 10,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2315A_SLN05_11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-11 data_ele=1018',
         'sequence': 11,
         'type': {'$ref': '#/$common/1018'}}
        datatype = common.D_1018
        min_len = 1
        max_len = 15


class L2315A_SLN05_12(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-12 data_ele=649',
         'sequence': 12,
         'type': {'$ref': '#/$common/649'}}
        datatype = common.D_649
        min_len = 1
        max_len = 10


class L2315A_SLN05_13(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-13 data_ele=355',
         'sequence': 13,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2315A_SLN05_14(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-14 data_ele=1018',
         'sequence': 14,
         'type': {'$ref': '#/$common/1018'}}
        datatype = common.D_1018
        min_len = 1
        max_len = 15


class L2315A_SLN05_15(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN05-15 data_ele=649',
         'sequence': 15,
         'type': {'$ref': '#/$common/649'}}
        datatype = common.D_649
        min_len = 1
        max_len = 10


class L2315A_SLN05(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SLN05 name= refdes= data_ele=C001',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'sln05_01': {'title': '',
                                     'usage': 'R',
                                     'description': 'xid=SLN05-01 data_ele=355',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/355'},
                                                        {'enum': ['10', 'IE', 'PR']}]}},
                        'sln05_02': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-02 data_ele=1018',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1018'}},
                        'sln05_03': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-03 data_ele=649',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/649'}},
                        'sln05_04': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-04 data_ele=355',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/355'}},
                        'sln05_05': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-05 data_ele=1018',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1018'}},
                        'sln05_06': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-06 data_ele=649',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/649'}},
                        'sln05_07': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-07 data_ele=355',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/355'}},
                        'sln05_08': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-08 data_ele=1018',
                                     'sequence': 8,
                                     'type': {'$ref': '#/$common/1018'}},
                        'sln05_09': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-09 data_ele=649',
                                     'sequence': 9,
                                     'type': {'$ref': '#/$common/649'}},
                        'sln05_10': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-10 data_ele=355',
                                     'sequence': 10,
                                     'type': {'$ref': '#/$common/355'}},
                        'sln05_11': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-11 data_ele=1018',
                                     'sequence': 11,
                                     'type': {'$ref': '#/$common/1018'}},
                        'sln05_12': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-12 data_ele=649',
                                     'sequence': 12,
                                     'type': {'$ref': '#/$common/649'}},
                        'sln05_13': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-13 data_ele=355',
                                     'sequence': 13,
                                     'type': {'$ref': '#/$common/355'}},
                        'sln05_14': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-14 data_ele=1018',
                                     'sequence': 14,
                                     'type': {'$ref': '#/$common/1018'}},
                        'sln05_15': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=SLN05-15 data_ele=649',
                                     'sequence': 15,
                                     'type': {'$ref': '#/$common/649'}}},
         'required': ['sln05_01']}
    sln05_01: L2315A_SLN05_01


class L2315A_SLN06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN06 data_ele=212',
         'sequence': 6,
         'type': {'$ref': '#/$common/212'}}
        datatype = common.D_212
        min_len = 1
        max_len = 17


class L2315A_SLN07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN07 data_ele=639',
         'sequence': 7,
         'type': {'$ref': '#/$common/639'}}
        datatype = common.D_639
        min_len = 2
        max_len = 2


class L2315A_SLN08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN08 data_ele=662',
         'sequence': 8,
         'type': {'$ref': '#/$common/662'}}
        datatype = common.D_662
        min_len = 1
        max_len = 1


class L2315A_SLN09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN09 data_ele=235',
         'sequence': 9,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN10 data_ele=234',
         'sequence': 10,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN11 data_ele=235',
         'sequence': 11,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN12(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN12 data_ele=234',
         'sequence': 12,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN13(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN13 data_ele=235',
         'sequence': 13,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN14(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN14 data_ele=234',
         'sequence': 14,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN15(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN15 data_ele=235',
         'sequence': 15,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN16(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN16 data_ele=234',
         'sequence': 16,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN17(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN17 data_ele=235',
         'sequence': 17,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN18(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN18 data_ele=234',
         'sequence': 18,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN19(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN19 data_ele=235',
         'sequence': 19,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN20(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN20 data_ele=234',
         'sequence': 20,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN21(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN21 data_ele=235',
         'sequence': 21,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN22(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN22 data_ele=234',
         'sequence': 22,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN23(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN23 data_ele=235',
         'sequence': 23,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN24(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN24 data_ele=234',
         'sequence': 24,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN25(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN25 data_ele=235',
         'sequence': 25,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN26(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN26 data_ele=234',
         'sequence': 26,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN27(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN27 data_ele=235',
         'sequence': 27,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2315A_SLN28(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=SLN28 data_ele=234',
         'sequence': 28,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2315A_SLN(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SLN name=',
         'position': 2040,
         'syntax': ['P0405', 'C0706', 'C0806', 'P0910', 'P1112', 'P1314', 'P1516',
                    'P1718', 'P1920', 'P2122', 'P2324', 'P2526', 'P2728'],
         'type': 'object',
         'properties': {'xid': {'literal': 'SLN'},
                        'sln01': {'$ref': '#/$elements/L2315A_SLN01'},
                        'sln03': {'$ref': '#/$elements/L2315A_SLN03'},
                        'sln04': {'$ref': '#/$elements/L2315A_SLN04'},
                        'sln05': {'$ref': '#/$elements/L2315A_SLN05'}},
         'required': ['sln01', 'sln03', 'sln04', 'sln05']}
        segment_name = 'SLN'
    sln01: L2315A_SLN01
    sln03: L2315A_SLN03
    sln04: L2315A_SLN04
    sln05: L2315A_SLN05


class L2315A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2315A name= type=None',
                   'position': 2040,
                   'type': 'object',
                   'properties': {'sln': {'$ref': '#/$segments/L2315A_SLN'}},
                   'required': ['sln']},
         'maxItems': 3}
    sln: L2315A_SLN


class L2310A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2310A name= type=None',
                   'position': 1900,
                   'type': 'object',
                   'properties': {'it1': {'$ref': '#/$segments/L2310A_IT1'},
                                  'l2312a': {'$ref': '#/$segments/L2312A'},
                                  'l2315a': {'$ref': '#/$segments/L2315A'}},
                   'required': ['it1']},
         'maxItems': 1}
    it1: L2310A_IT1
    l2312a: list[L2312A] | None
    l2315a: list[L2315A] | None


class L2320A_ADX01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX01 data_ele=782',
         'sequence': 1,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320A_ADX02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX02 data_ele=426',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/426'},
                            {'enum': ['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA',
                                      'J3']}]}}
        datatype = common.D_426
        codes = ['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA', 'J3']
        min_len = 2
        max_len = 2


class L2320A_ADX03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX03 data_ele=128',
         'sequence': 3,
         'type': {'$ref': '#/$common/128'}}
        datatype = common.D_128
        min_len = 2
        max_len = 3


class L2320A_ADX04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320A_ADX(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX name=',
         'position': 2100,
         'syntax': ['P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ADX'},
                        'adx01': {'$ref': '#/$elements/L2320A_ADX01'},
                        'adx02': {'$ref': '#/$elements/L2320A_ADX02'}},
         'required': ['adx01', 'adx02']}
        segment_name = 'ADX'
    adx01: L2320A_ADX01
    adx02: L2320A_ADX02


class L2320A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2320A name= type=None',
                   'position': 2100,
                   'type': 'object',
                   'properties': {'adx': {'$ref': '#/$segments/L2320A_ADX'}},
                   'required': ['adx']}}
    adx: L2320A_ADX


class L2300A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2300A name= type=None',
                   'position': 1500,
                   'type': 'object',
                   'properties': {'rmr': {'$ref': '#/$segments/L2300A_RMR'},
                                  'ref': {'$ref': '#/$segments/L2300A_REF'},
                                  'dtm': {'$ref': '#/$segments/L2300A_DTM'},
                                  'l2310a': {'$ref': '#/$segments/L2310A'},
                                  'l2320a': {'$ref': '#/$segments/L2320A'}},
                   'required': ['rmr']}}
    rmr: L2300A_RMR
    ref: list[L2300A_REF] | None
    dtm: L2300A_DTM | None
    l2310a: list[L2310A] | None
    l2320a: list[L2320A] | None


class L2000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2000A name= type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'ent': {'$ref': '#/$segments/L2000A_ENT'},
                                  'l2200a': {'$ref': '#/$segments/L2200A'},
                                  'l2300a': {'$ref': '#/$segments/L2300A'}},
                   'required': ['ent', 'l2300a']},
         'maxItems': 1}
    ent: L2000A_ENT
    l2200a: list[L2200A] | None
    l2300a: list[L2300A]


class TABLE2AREA2(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=TABLE2AREA2 name= type=wrapper',
                   'position': 120,
                   'type': 'object',
                   'properties': {'l2000a': {'$ref': '#/$segments/L2000A'}}}}
    l2000a: list[L2000A] | None


class L2000B_ENT01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT01 data_ele=554',
         'sequence': 1,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2000B_ENT02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT02 data_ele=98',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['2J']}]}}
        datatype = common.D_98
        codes = ['2J']
        min_len = 2
        max_len = 3


class L2000B_ENT03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT03 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'EI', 'II']}]}}
        datatype = common.D_66
        codes = ['34', 'EI', 'II']
        min_len = 1
        max_len = 2


class L2000B_ENT04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT04 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2000B_ENT05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT05 data_ele=98',
         'sequence': 5,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2000B_ENT06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT06 data_ele=66',
         'sequence': 6,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L2000B_ENT07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT07 data_ele=67',
         'sequence': 7,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2000B_ENT08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT08 data_ele=128',
         'sequence': 8,
         'type': {'$ref': '#/$common/128'}}
        datatype = common.D_128
        min_len = 2
        max_len = 3


class L2000B_ENT09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ENT09 data_ele=127',
         'sequence': 9,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000B_ENT(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ENT name=',
         'position': 100,
         'syntax': ['P020304', 'P050607', 'P0809'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ENT'},
                        'ent01': {'$ref': '#/$elements/L2000B_ENT01'},
                        'ent02': {'$ref': '#/$elements/L2000B_ENT02'},
                        'ent03': {'$ref': '#/$elements/L2000B_ENT03'},
                        'ent04': {'$ref': '#/$elements/L2000B_ENT04'}},
         'required': ['ent01', 'ent02', 'ent03', 'ent04']}
        segment_name = 'ENT'
    ent01: L2000B_ENT01
    ent02: L2000B_ENT02
    ent03: L2000B_ENT03
    ent04: L2000B_ENT04


class L2100B_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['DO', 'EY', 'IL', 'QE']}]}}
        datatype = common.D_98
        codes = ['DO', 'EY', 'IL', 'QE']
        min_len = 2
        max_len = 3


class L2100B_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100B_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100B_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100B_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100B_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100B_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100B_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'EI', 'N']}]}}
        datatype = common.D_66
        codes = ['34', 'EI', 'N']
        min_len = 1
        max_len = 2


class L2100B_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100B_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100B_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100B_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'sequence': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100B_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 200,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100B_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100B_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100B_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100B_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100B_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100B_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100B_NM101
    nm102: L2100B_NM102
    nm103: L2100B_NM103 | None
    nm104: L2100B_NM104 | None
    nm105: L2100B_NM105 | None
    nm106: L2100B_NM106 | None
    nm107: L2100B_NM107 | None
    nm108: L2100B_NM108 | None
    nm109: L2100B_NM109 | None


class L2100B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2100B name= type=None',
                   'position': 200,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100B_NM1'}},
                   'required': ['nm1']}}
    nm1: L2100B_NM1


class L2200B_ADX01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX01 data_ele=782',
         'sequence': 1,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200B_ADX02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX02 data_ele=426',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/426'},
                            {'enum': ['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6',
                                      'RU', 'WO']}]}}
        datatype = common.D_426
        codes = ['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6', 'RU', 'WO']
        min_len = 2
        max_len = 2


class L2200B_ADX03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX03 data_ele=128',
         'sequence': 3,
         'type': {'$ref': '#/$common/128'}}
        datatype = common.D_128
        min_len = 2
        max_len = 3


class L2200B_ADX04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200B_ADX(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX name=',
         'position': 800,
         'syntax': ['P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ADX'},
                        'adx01': {'$ref': '#/$elements/L2200B_ADX01'},
                        'adx02': {'$ref': '#/$elements/L2200B_ADX02'}},
         'required': ['adx01', 'adx02']}
        segment_name = 'ADX'
    adx01: L2200B_ADX01
    adx02: L2200B_ADX02


class L2200B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2200B name= type=None',
                   'position': 800,
                   'type': 'object',
                   'properties': {'adx': {'$ref': '#/$segments/L2200B_ADX'}},
                   'required': ['adx']}}
    adx: L2200B_ADX


class L2300B_RMR01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['11', '9J', 'AZ', 'B7', 'CT', 'ID', 'IG', 'IK',
                                      'KW']}]}}
        datatype = common.D_128
        codes = ['11', '9J', 'AZ', 'B7', 'CT', 'ID', 'IG', 'IK', 'KW']
        min_len = 2
        max_len = 3


class L2300B_RMR02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300B_RMR03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RMR03 data_ele=482',
         'sequence': 3,
         'type': {'$ref': '#/$common/482'}}
        datatype = common.D_482
        min_len = 2
        max_len = 2


class L2300B_RMR04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300B_RMR05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=RMR05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300B_RMR06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RMR06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300B_RMR07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RMR07 data_ele=426',
         'sequence': 7,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class L2300B_RMR08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=RMR08 data_ele=782',
         'sequence': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300B_RMR(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=RMR name=',
         'position': 1500,
         'syntax': ['P0102', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'RMR'},
                        'rmr01': {'$ref': '#/$elements/L2300B_RMR01'},
                        'rmr02': {'$ref': '#/$elements/L2300B_RMR02'},
                        'rmr04': {'$ref': '#/$elements/L2300B_RMR04'},
                        'rmr05': {'$ref': '#/$elements/L2300B_RMR05'}},
         'required': ['rmr01', 'rmr02', 'rmr04']}
        segment_name = 'RMR'
    rmr01: L2300B_RMR01
    rmr02: L2300B_RMR02
    rmr04: L2300B_RMR04
    rmr05: L2300B_RMR05 | None


class L2300B_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['14', '18', '2F', '38', 'E9', 'LU', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['14', '18', '2F', '38', 'E9', 'LU', 'ZZ']
        min_len = 2
        max_len = 3


class L2300B_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300B_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300B_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300B_REF(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=REF name=',
                   'position': 1700,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300B_REF02'}},
                   'required': ['ref01', 'ref02']}}
        segment_name = 'REF'
    ref01: L2300B_REF01
    ref02: L2300B_REF02


class L2300B_DTM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['582', 'AAG']}]}}
        datatype = common.D_374
        codes = ['582', 'AAG']
        min_len = 3
        max_len = 3


class L2300B_DTM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2300B_DTM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2300B_DTM04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L2300B_DTM05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['RD8']}]}}
        datatype = common.D_1250
        codes = ['RD8']
        min_len = 2
        max_len = 3


class L2300B_DTM06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300B_DTM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTM name=',
         'position': 1800,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/L2300B_DTM01'},
                        'dtm02': {'$ref': '#/$elements/L2300B_DTM02'},
                        'dtm05': {'$ref': '#/$elements/L2300B_DTM05'},
                        'dtm06': {'$ref': '#/$elements/L2300B_DTM06'}},
         'required': ['dtm01']}
        segment_name = 'DTM'
    dtm01: L2300B_DTM01
    dtm02: L2300B_DTM02 | None
    dtm05: L2300B_DTM05 | None
    dtm06: L2300B_DTM06 | None


class L2320B_ADX01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX01 data_ele=782',
         'sequence': 1,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320B_ADX02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX02 data_ele=426',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/426'},
                            {'enum': ['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA',
                                      'J3']}]}}
        datatype = common.D_426
        codes = ['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA', 'J3']
        min_len = 2
        max_len = 2


class L2320B_ADX03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX03 data_ele=128',
         'sequence': 3,
         'type': {'$ref': '#/$common/128'}}
        datatype = common.D_128
        min_len = 2
        max_len = 3


class L2320B_ADX04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ADX04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320B_ADX(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ADX name=',
         'position': 2100,
         'syntax': ['P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ADX'},
                        'adx01': {'$ref': '#/$elements/L2320B_ADX01'},
                        'adx02': {'$ref': '#/$elements/L2320B_ADX02'}},
         'required': ['adx01', 'adx02']}
        segment_name = 'ADX'
    adx01: L2320B_ADX01
    adx02: L2320B_ADX02


class L2320B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2320B name= type=None',
                   'position': 2100,
                   'type': 'object',
                   'properties': {'adx': {'$ref': '#/$segments/L2320B_ADX'}},
                   'required': ['adx']}}
    adx: L2320B_ADX


class L2300B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2300B name= type=None',
                   'position': 1500,
                   'type': 'object',
                   'properties': {'rmr': {'$ref': '#/$segments/L2300B_RMR'},
                                  'ref': {'$ref': '#/$segments/L2300B_REF'},
                                  'dtm': {'$ref': '#/$segments/L2300B_DTM'},
                                  'l2320b': {'$ref': '#/$segments/L2320B'}},
                   'required': ['rmr']}}
    rmr: L2300B_RMR
    ref: list[L2300B_REF] | None
    dtm: L2300B_DTM | None
    l2320b: list[L2320B] | None


class L2000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2000B name= type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'ent': {'$ref': '#/$segments/L2000B_ENT'},
                                  'l2100b': {'$ref': '#/$segments/L2100B'},
                                  'l2200b': {'$ref': '#/$segments/L2200B'},
                                  'l2300b': {'$ref': '#/$segments/L2300B'}},
                   'required': ['ent', 'l2300b']}}
    ent: L2000B_ENT
    l2100b: list[L2100B] | None
    l2200b: list[L2200B] | None
    l2300b: list[L2300B]


class TABLE2AREA3(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=TABLE2AREA3 name= type=wrapper',
                   'position': 130,
                   'type': 'object',
                   'properties': {'l2000b': {'$ref': '#/$segments/L2000B'}}}}
    l2000b: list[L2000B] | None


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'N',
                   'description': 'xid=FOOTER name= type=wrapper',
                   'position': 140},
         'maxItems': 1}


class ST_LOOP_SE01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SE01 data_ele=96',
         'sequence': 1,
         'type': {'$ref': '#/$common/96'}}
        datatype = common.D_96
        min_len = 1
        max_len = 10


class ST_LOOP_SE02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SE02 data_ele=329',
         'sequence': 2,
         'type': {'$ref': '#/$common/329'}}
        datatype = common.D_329
        min_len = 4
        max_len = 9


class ST_LOOP_SE(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SE name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'SE'},
                        'se01': {'$ref': '#/$elements/ST_LOOP_SE01'},
                        'se02': {'$ref': '#/$elements/ST_LOOP_SE02'}},
         'required': ['se01', 'se02']}
        segment_name = 'SE'
    se01: ST_LOOP_SE01
    se02: ST_LOOP_SE02


class ST_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=ST_LOOP name= type=explicit',
                   'position': 200,
                   'type': 'object',
                   'properties': {'st': {'$ref': '#/$segments/ST_LOOP_ST'},
                                  'header': {'$ref': '#/$segments/HEADER'},
                                  'table2area2': {'$ref': '#/$segments/TABLE2AREA2'},
                                  'table2area3': {'$ref': '#/$segments/TABLE2AREA3'},
                                  'se': {'$ref': '#/$segments/ST_LOOP_SE'}},
                   'required': ['st', 'header', 'se']}}
    st: ST_LOOP_ST
    header: list[HEADER]
    table2area2: list[TABLE2AREA2] | None
    table2area3: list[TABLE2AREA3] | None
    se: ST_LOOP_SE


class MSG820A1(Message):
    """HIPAA Payment Order/Remittance Advice 005010X218 820A1"""
    class Schema:
        json = {'title': 'HIPAA Payment Order/Remittance Advice 005010X218 820A1',
         'description': 'xid=820A1 name=HIPAA Payment Order/Remittance Advice '
                        '005010X218 820A1',
         'type': 'object',
         'properties': {'st_loop': {'$ref': '#/$loops/ST_LOOP'}},
         'required': ['st_loop']}
    st_loop: list[ST_LOOP]
