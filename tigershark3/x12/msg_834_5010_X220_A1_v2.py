"""
834.5010.X220.A1.v2
Created 2023-05-12 20:25:34.268566
"""
from .base import *
from . import common


class ST_LOOP_ST01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ST01 data_ele=143',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['834']}]}}
        datatype = common.D_143
        codes = ['834']
        min_len = 3
        max_len = 3


class ST_LOOP_ST02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ST02 data_ele=329',
         'position': 2,
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
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/1705'}, {'enum': ['005010X220A1']}]}}
        datatype = common.D_1705
        codes = ['005010X220A1']
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


class HEADER_BGN01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BGN01 data_ele=353',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/353'}, {'enum': ['00', '15', '22']}]}}
        datatype = common.D_353
        codes = ['00', '15', '22']
        min_len = 2
        max_len = 2


class HEADER_BGN02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BGN02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_BGN03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BGN03 data_ele=373',
         'position': 3,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BGN04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BGN04 data_ele=337',
         'position': 4,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_BGN05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BGN05 data_ele=623',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/623'},
                            {'enum': ['01', '02', '03', '04', '05', '06', '07', '08',
                                      '09', '10', '11', '12', '13', '14', '15', '16',
                                      '17', '18', '19', '20', '21', '22', '23', '24',
                                      'AD', 'AS', 'AT', 'CD', 'CS', 'CT', 'ED', 'ES',
                                      'ET', 'GM', 'HD', 'HS', 'HT', 'LT', 'MD', 'MS',
                                      'MT', 'ND', 'NS', 'NT', 'PD', 'PS', 'PT', 'TD',
                                      'TS', 'TT', 'UT']}]}}
        datatype = common.D_623
        codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', 'AD', 'AS', 'AT', 'CD', 'CS', 'CT', 'ED', 'ES', 'ET', 'GM', 'HD', 'HS', 'HT', 'LT', 'MD', 'MS', 'MT', 'ND', 'NS', 'NT', 'PD', 'PS', 'PT', 'TD', 'TS', 'TT', 'UT']
        min_len = 2
        max_len = 2


class HEADER_BGN06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=BGN06 data_ele=127',
         'position': 6,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_BGN07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=BGN07 data_ele=640',
         'position': 7,
         'type': {'$ref': '#/$common/640'}}
        datatype = common.D_640
        min_len = 2
        max_len = 2


class HEADER_BGN08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BGN08 data_ele=306',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/306'}, {'enum': ['2', '4', 'RX']}]}}
        datatype = common.D_306
        codes = ['2', '4', 'RX']
        min_len = 1
        max_len = 2


class HEADER_BGN09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=BGN09 data_ele=786',
         'position': 9,
         'type': {'$ref': '#/$common/786'}}
        datatype = common.D_786
        min_len = 2
        max_len = 2


class HEADER_BGN(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=BGN name=',
         'position': 200,
         'syntax': ['C0504'],
         'type': 'object',
         'properties': {'xid': {'literal': 'BGN'},
                        'bgn01': {'$ref': '#/$elements/HEADER_BGN01'},
                        'bgn02': {'$ref': '#/$elements/HEADER_BGN02'},
                        'bgn03': {'$ref': '#/$elements/HEADER_BGN03'},
                        'bgn04': {'$ref': '#/$elements/HEADER_BGN04'},
                        'bgn05': {'$ref': '#/$elements/HEADER_BGN05'},
                        'bgn06': {'$ref': '#/$elements/HEADER_BGN06'},
                        'bgn07': {'$ref': '#/$elements/HEADER_BGN07'},
                        'bgn08': {'$ref': '#/$elements/HEADER_BGN08'},
                        'bgn09': {'$ref': '#/$elements/HEADER_BGN09'}},
         'required': ['bgn01', 'bgn02', 'bgn03', 'bgn04', 'bgn08']}
        segment_name = 'BGN'
    bgn01: HEADER_BGN01
    bgn02: HEADER_BGN02
    bgn03: HEADER_BGN03
    bgn04: HEADER_BGN04
    bgn05: HEADER_BGN05 | None
    bgn06: HEADER_BGN06 | None
    bgn07: HEADER_BGN07 | None
    bgn08: HEADER_BGN08
    bgn09: HEADER_BGN09 | None


class HEADER_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['38']}]}}
        datatype = common.D_128
        codes = ['38']
        min_len = 2
        max_len = 3


class HEADER_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
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
         'position': 3,
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
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=REF name=',
         'position': 300,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                        'ref02': {'$ref': '#/$elements/HEADER_REF02'},
                        'ref03': {'$ref': '#/$elements/HEADER_REF03'},
                        'ref04': {'$ref': '#/$elements/HEADER_REF04'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02
    ref03: HEADER_REF03 | None


class HEADER_DTP01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['007', '090', '091', '303', '382', '388']}]}}
        datatype = common.D_374
        codes = ['007', '090', '091', '303', '382', '388']
        min_len = 3
        max_len = 3


class HEADER_DTP02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class HEADER_DTP03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'position': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class HEADER_DTP(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=DTP name=',
                   'position': 400,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/HEADER_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/HEADER_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/HEADER_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']}}
        segment_name = 'DTP'
    dtp01: HEADER_DTP01
    dtp02: HEADER_DTP02
    dtp03: HEADER_DTP03


class HEADER_QTY01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=QTY01 data_ele=673',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'}, {'enum': ['DT', 'ET', 'TO']}]}}
        datatype = common.D_673
        codes = ['DT', 'ET', 'TO']
        min_len = 2
        max_len = 2


class HEADER_QTY02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=QTY02 data_ele=380',
         'position': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class HEADER_QTY03(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=QTY03 name= refdes= data_ele=C001',
         'sequence': 3,
         'syntax': []}


class HEADER_QTY04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=QTY04 data_ele=61',
         'position': 4,
         'type': {'$ref': '#/$common/61'}}
        datatype = common.D_61
        min_len = 1
        max_len = 30


class HEADER_QTY(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=QTY name=',
                   'position': 600,
                   'syntax': ['E0204', 'R0204'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'QTY'},
                                  'qty01': {'$ref': '#/$elements/HEADER_QTY01'},
                                  'qty02': {'$ref': '#/$elements/HEADER_QTY02'},
                                  'qty03': {'$ref': '#/$elements/HEADER_QTY03'},
                                  'qty04': {'$ref': '#/$elements/HEADER_QTY04'}},
                   'required': ['qty01', 'qty02']},
         'maxItems': 3}
        segment_name = 'QTY'
    qty01: HEADER_QTY01
    qty02: HEADER_QTY02
    qty04: HEADER_QTY04 | None


class L1000A_N101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['P5']}]}}
        datatype = common.D_98
        codes = ['P5']
        min_len = 2
        max_len = 3


class L1000A_N102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000A_N103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N103 data_ele=66',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '94', 'FI']}]}}
        datatype = common.D_66
        codes = ['24', '94', 'FI']
        min_len = 1
        max_len = 2


class L1000A_N104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N104 data_ele=67',
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
                        'n104': {'$ref': '#/$elements/L1000A_N104'},
                        'n105': {'$ref': '#/$elements/L1000A_N105'},
                        'n106': {'$ref': '#/$elements/L1000A_N106'}},
         'required': ['n101', 'n103', 'n104']}
        segment_name = 'N1'
    n101: L1000A_N101
    n102: L1000A_N102 | None
    n103: L1000A_N103
    n104: L1000A_N104
    n105: L1000A_N105 | None
    n106: L1000A_N106 | None


class L1000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=1000A name= type=None',
                   'position': 700,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000A_N1'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000A_N1


class L1000B_N101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['IN']}]}}
        datatype = common.D_98
        codes = ['IN']
        min_len = 2
        max_len = 3


class L1000B_N102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000B_N103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N103 data_ele=66',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['94', 'FI', 'XV']}]}}
        datatype = common.D_66
        codes = ['94', 'FI', 'XV']
        min_len = 1
        max_len = 2


class L1000B_N104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N104 data_ele=67',
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
                        'n104': {'$ref': '#/$elements/L1000B_N104'},
                        'n105': {'$ref': '#/$elements/L1000B_N105'},
                        'n106': {'$ref': '#/$elements/L1000B_N106'}},
         'required': ['n101', 'n103', 'n104']}
        segment_name = 'N1'
    n101: L1000B_N101
    n102: L1000B_N102 | None
    n103: L1000B_N103
    n104: L1000B_N104
    n105: L1000B_N105 | None
    n106: L1000B_N106 | None


class L1000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=1000B name= type=None',
                   'position': 1900,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000B_N1'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000B_N1


class L1000C_N101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['BO', 'TV']}]}}
        datatype = common.D_98
        codes = ['BO', 'TV']
        min_len = 2
        max_len = 3


class L1000C_N102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N102 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000C_N103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N103 data_ele=66',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['94', 'FI', 'XV']}]}}
        datatype = common.D_66
        codes = ['94', 'FI', 'XV']
        min_len = 1
        max_len = 2


class L1000C_N104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N104 data_ele=67',
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
                        'n104': {'$ref': '#/$elements/L1000C_N104'},
                        'n105': {'$ref': '#/$elements/L1000C_N105'},
                        'n106': {'$ref': '#/$elements/L1000C_N106'}},
         'required': ['n101', 'n102', 'n103', 'n104']}
        segment_name = 'N1'
    n101: L1000C_N101
    n102: L1000C_N102
    n103: L1000C_N103
    n104: L1000C_N104
    n105: L1000C_N105 | None
    n106: L1000C_N106 | None


class L1100C_ACT01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ACT01 data_ele=508',
         'position': 1,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class L1100C_ACT02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ACT02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1100C_ACT03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ACT03 data_ele=66',
         'position': 3,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L1100C_ACT04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ACT04 data_ele=67',
         'position': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1100C_ACT05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ACT05 data_ele=569',
         'position': 5,
         'type': {'$ref': '#/$common/569'}}
        datatype = common.D_569
        min_len = 1
        max_len = 3


class L1100C_ACT06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=ACT06 data_ele=508',
         'position': 6,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class L1100C_ACT07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ACT07 data_ele=352',
         'position': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L1100C_ACT08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ACT08 data_ele=107',
         'position': 8,
         'type': {'$ref': '#/$common/107'}}
        datatype = common.D_107
        min_len = 1
        max_len = 2


class L1100C_ACT09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ACT09 data_ele=1216',
         'position': 9,
         'type': {'$ref': '#/$common/1216'}}
        datatype = common.D_1216
        min_len = 1
        max_len = 1


class L1100C_ACT(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ACT name=',
         'position': 1200,
         'syntax': ['P0304', 'C0506', 'C0705'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ACT'},
                        'act01': {'$ref': '#/$elements/L1100C_ACT01'},
                        'act02': {'$ref': '#/$elements/L1100C_ACT02'},
                        'act03': {'$ref': '#/$elements/L1100C_ACT03'},
                        'act04': {'$ref': '#/$elements/L1100C_ACT04'},
                        'act05': {'$ref': '#/$elements/L1100C_ACT05'},
                        'act06': {'$ref': '#/$elements/L1100C_ACT06'},
                        'act07': {'$ref': '#/$elements/L1100C_ACT07'},
                        'act08': {'$ref': '#/$elements/L1100C_ACT08'},
                        'act09': {'$ref': '#/$elements/L1100C_ACT09'}},
         'required': ['act01']}
        segment_name = 'ACT'
    act01: L1100C_ACT01
    act02: L1100C_ACT02 | None
    act03: L1100C_ACT03 | None
    act04: L1100C_ACT04 | None
    act05: L1100C_ACT05 | None
    act06: L1100C_ACT06 | None
    act07: L1100C_ACT07 | None
    act08: L1100C_ACT08 | None
    act09: L1100C_ACT09 | None


class L1100C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=1100C name= type=None',
                   'position': 3600,
                   'type': 'object',
                   'properties': {'act': {'$ref': '#/$segments/L1100C_ACT'}},
                   'required': ['act']},
         'maxItems': 1}
    act: L1100C_ACT


class L1000C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=1000C name= type=None',
                   'position': 3100,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000C_N1'},
                                  'l1100c': {'$ref': '#/$segments/L1100C'}},
                   'required': ['n1', 'l1100c']},
         'maxItems': 2}
    n1: L1000C_N1
    l1100c: list[L1100C]


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=HEADER name= type=wrapper',
                   'position': 110,
                   'type': 'object',
                   'properties': {'bgn': {'$ref': '#/$segments/HEADER_BGN'},
                                  'ref': {'$ref': '#/$segments/HEADER_REF'},
                                  'dtp': {'$ref': '#/$segments/HEADER_DTP'},
                                  'qty': {'$ref': '#/$segments/HEADER_QTY'},
                                  'l1000a': {'$ref': '#/$segments/L1000A'},
                                  'l1000b': {'$ref': '#/$segments/L1000B'},
                                  'l1000c': {'$ref': '#/$segments/L1000C'}},
                   'required': ['bgn', 'l1000a', 'l1000b', 'l1000c']},
         'maxItems': 1}
    bgn: HEADER_BGN
    ref: HEADER_REF | None
    dtp: list[HEADER_DTP] | None
    qty: list[HEADER_QTY] | None
    l1000a: list[L1000A]
    l1000b: list[L1000B]
    l1000c: list[L1000C]


class L2000_INS01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=INS01 data_ele=1073',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000_INS02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=INS02 data_ele=1069',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'},
                            {'enum': ['01', '03', '04', '05', '06', '07', '08', '09',
                                      '10', '11', '12', '13', '14', '15', '16', '17',
                                      '18', '19', '23', '24', '25', '26', '31', '38',
                                      '53', '60', 'D2', 'G8', 'G9']}]}}
        datatype = common.D_1069
        codes = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26', '31', '38', '53', '60', 'D2', 'G8', 'G9']
        min_len = 2
        max_len = 2


class L2000_INS03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=INS03 data_ele=875',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/875'},
                            {'enum': ['001', '021', '024', '025', '030']}]}}
        datatype = common.D_875
        codes = ['001', '021', '024', '025', '030']
        min_len = 3
        max_len = 3


class L2000_INS04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS04 data_ele=1203',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/1203'},
                            {'enum': ['01', '02', '03', '04', '05', '06', '07', '08',
                                      '09', '10', '11', '14', '15', '16', '17', '18',
                                      '20', '21', '22', '25', '26', '27', '28', '29',
                                      '31', '32', '33', '37', '38', '39', '40', '41',
                                      '43', '59', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF',
                                      'AG', 'AH', 'AI', 'AJ', 'AL', 'EC', 'XN',
                                      'XT']}]}}
        datatype = common.D_1203
        codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '14', '15', '16', '17', '18', '20', '21', '22', '25', '26', '27', '28', '29', '31', '32', '33', '37', '38', '39', '40', '41', '43', '59', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AL', 'EC', 'XN', 'XT']
        min_len = 2
        max_len = 3


class L2000_INS05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=INS05 data_ele=1216',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/1216'},
                            {'enum': ['A', 'C', 'S', 'T']}]}}
        datatype = common.D_1216
        codes = ['A', 'C', 'S', 'T']
        min_len = 1
        max_len = 1


class L2000_INS06_01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=INS06-01 data_ele=1218',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1218'},
                            {'enum': ['A', 'B', 'C', 'D', 'E']}]}}
        datatype = common.D_1218
        codes = ['A', 'B', 'C', 'D', 'E']
        min_len = 1
        max_len = 1


class L2000_INS06_02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS06-02 data_ele=1701',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1701'}, {'enum': ['0', '1', '2']}]}}
        datatype = common.D_1701
        codes = ['0', '1', '2']
        min_len = 1
        max_len = 1


class L2000_INS06_03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=INS06-03 data_ele=1701',
         'position': 3,
         'type': {'$ref': '#/$common/1701'}}
        datatype = common.D_1701
        min_len = 1
        max_len = 1


class L2000_INS06_04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=INS06-04 data_ele=1701',
         'position': 4,
         'type': {'$ref': '#/$common/1701'}}
        datatype = common.D_1701
        min_len = 1
        max_len = 1


class L2000_INS06(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS06 name= refdes= data_ele=C052',
         'sequence': 6,
         'syntax': [],
         'type': 'object',
         'properties': {'ins06_01': {'title': '',
                                     'usage': 'R',
                                     'description': 'xid=INS06-01 data_ele=1218',
                                     'position': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1218'},
                                                        {'enum': ['A', 'B', 'C', 'D',
                                                                  'E']}]}},
                        'ins06_02': {'title': '',
                                     'usage': 'S',
                                     'description': 'xid=INS06-02 data_ele=1701',
                                     'position': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1701'},
                                                        {'enum': ['0', '1', '2']}]}},
                        'ins06_03': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=INS06-03 data_ele=1701',
                                     'position': 3,
                                     'type': {'$ref': '#/$common/1701'}},
                        'ins06_04': {'title': '',
                                     'usage': 'N',
                                     'description': 'xid=INS06-04 data_ele=1701',
                                     'position': 4,
                                     'type': {'$ref': '#/$common/1701'}}},
         'required': ['ins06_01']}
    ins06_01: L2000_INS06_01
    ins06_02: L2000_INS06_02 | None
    ins06_03: L2000_INS06_03 | None
    ins06_04: L2000_INS06_04 | None


class L2000_INS07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS07 data_ele=1219',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/1219'},
                            {'enum': ['1', '10', '2', '3', '4', '5', '6', '7', '8', '9',
                                      'ZZ']}]}}
        datatype = common.D_1219
        codes = ['1', '10', '2', '3', '4', '5', '6', '7', '8', '9', 'ZZ']
        min_len = 1
        max_len = 2


class L2000_INS08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS08 data_ele=584',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/584'},
                            {'enum': ['AC', 'AO', 'AU', 'FT', 'L1', 'PT', 'RT',
                                      'TE']}]}}
        datatype = common.D_584
        codes = ['AC', 'AO', 'AU', 'FT', 'L1', 'PT', 'RT', 'TE']
        min_len = 2
        max_len = 2


class L2000_INS09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS09 data_ele=1220',
         'position': 9,
         'type': {'allOf': [{'$ref': '#/$common/1220'}, {'enum': ['F', 'N', 'P']}]}}
        datatype = common.D_1220
        codes = ['F', 'N', 'P']
        min_len = 1
        max_len = 1


class L2000_INS10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS10 data_ele=1073',
         'position': 10,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000_INS11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS11 data_ele=1250',
         'position': 11,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000_INS12(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS12 data_ele=1251',
         'position': 12,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000_INS13(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS13 data_ele=1165',
         'position': 13,
         'type': {'allOf': [{'$ref': '#/$common/1165'}, {'enum': ['R', 'U']}]}}
        datatype = common.D_1165
        codes = ['R', 'U']
        min_len = 1
        max_len = 1


class L2000_INS14(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=INS14 data_ele=19',
         'position': 14,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2000_INS15(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=INS15 data_ele=156',
         'position': 15,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        min_len = 2
        max_len = 2


class L2000_INS16(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=INS16 data_ele=26',
         'position': 16,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L2000_INS17(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=INS17 data_ele=1470',
         'position': 17,
         'type': {'$ref': '#/$common/1470'}}
        datatype = common.D_1470
        min_len = 1
        max_len = 9


class L2000_INS(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=INS name=',
         'position': 100,
         'syntax': ['P1112'],
         'type': 'object',
         'properties': {'xid': {'literal': 'INS'},
                        'ins01': {'$ref': '#/$elements/L2000_INS01'},
                        'ins02': {'$ref': '#/$elements/L2000_INS02'},
                        'ins03': {'$ref': '#/$elements/L2000_INS03'},
                        'ins04': {'$ref': '#/$elements/L2000_INS04'},
                        'ins05': {'$ref': '#/$elements/L2000_INS05'},
                        'ins06': {'$ref': '#/$elements/L2000_INS06'},
                        'ins07': {'$ref': '#/$elements/L2000_INS07'},
                        'ins08': {'$ref': '#/$elements/L2000_INS08'},
                        'ins09': {'$ref': '#/$elements/L2000_INS09'},
                        'ins10': {'$ref': '#/$elements/L2000_INS10'},
                        'ins11': {'$ref': '#/$elements/L2000_INS11'},
                        'ins12': {'$ref': '#/$elements/L2000_INS12'},
                        'ins13': {'$ref': '#/$elements/L2000_INS13'},
                        'ins14': {'$ref': '#/$elements/L2000_INS14'},
                        'ins15': {'$ref': '#/$elements/L2000_INS15'},
                        'ins16': {'$ref': '#/$elements/L2000_INS16'},
                        'ins17': {'$ref': '#/$elements/L2000_INS17'}},
         'required': ['ins01', 'ins02', 'ins03', 'ins05']}
        segment_name = 'INS'
    ins01: L2000_INS01
    ins02: L2000_INS02
    ins03: L2000_INS03
    ins04: L2000_INS04 | None
    ins05: L2000_INS05
    ins06: L2000_INS06 | None
    ins07: L2000_INS07 | None
    ins08: L2000_INS08 | None
    ins09: L2000_INS09 | None
    ins10: L2000_INS10 | None
    ins11: L2000_INS11 | None
    ins12: L2000_INS12 | None
    ins13: L2000_INS13 | None
    ins14: L2000_INS14 | None
    ins15: L2000_INS15 | None
    ins16: L2000_INS16 | None
    ins17: L2000_INS17 | None


class L2000_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['0F']}]}}
        datatype = common.D_128
        codes = ['0F']
        min_len = 2
        max_len = 3


class L2000_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000_REF(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF name=',
         'position': 200,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2000_REF01'},
                        'ref02': {'$ref': '#/$elements/L2000_REF02'},
                        'ref03': {'$ref': '#/$elements/L2000_REF03'},
                        'ref04': {'$ref': '#/$elements/L2000_REF04'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2000_REF01
    ref02: L2000_REF02
    ref03: L2000_REF03 | None


class L2000_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['1L']}]}}
        datatype = common.D_128
        codes = ['1L']
        min_len = 2
        max_len = 3


class L2000_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000_REF(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=REF name=',
         'position': 200,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2000_REF01'},
                        'ref02': {'$ref': '#/$elements/L2000_REF02'},
                        'ref03': {'$ref': '#/$elements/L2000_REF03'},
                        'ref04': {'$ref': '#/$elements/L2000_REF04'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2000_REF01
    ref02: L2000_REF02
    ref03: L2000_REF03 | None


class L2000_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['17', '23', '3H', '4A', '6O', 'ABB', 'D3', 'DX',
                                      'F6', 'P5', 'Q4', 'QQ', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['17', '23', '3H', '4A', '6O', 'ABB', 'D3', 'DX', 'F6', 'P5', 'Q4', 'QQ', 'ZZ']
        min_len = 2
        max_len = 3


class L2000_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000_REF(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=REF name=',
                   'position': 200,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2000_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2000_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2000_REF03'},
                                  'ref04': {'$ref': '#/$elements/L2000_REF04'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 13}
        segment_name = 'REF'
    ref01: L2000_REF01
    ref02: L2000_REF02
    ref03: L2000_REF03 | None


class L2000_DTP01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['050', '286', '296', '297', '300', '301', '303',
                                      '336', '337', '338', '339', '340', '341', '350',
                                      '351', '356', '357', '383', '385', '386', '393',
                                      '394', '473', '474']}]}}
        datatype = common.D_374
        codes = ['050', '286', '296', '297', '300', '301', '303', '336', '337', '338', '339', '340', '341', '350', '351', '356', '357', '383', '385', '386', '393', '394', '473', '474']
        min_len = 3
        max_len = 3


class L2000_DTP02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000_DTP03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'position': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000_DTP(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=DTP name=',
                   'position': 250,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2000_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2000_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2000_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 24}
        segment_name = 'DTP'
    dtp01: L2000_DTP01
    dtp02: L2000_DTP02
    dtp03: L2000_DTP03


class L2100A_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['74', 'IL']}]}}
        datatype = common.D_98
        codes = ['74', 'IL']
        min_len = 2
        max_len = 3


class L2100A_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100A_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100A_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100A_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100A_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100A_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100A_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100A_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100A_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100A_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100A_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100A_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100A_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100A_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100A_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100A_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100A_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100A_NM112'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2100A_NM101
    nm102: L2100A_NM102
    nm103: L2100A_NM103
    nm104: L2100A_NM104 | None
    nm105: L2100A_NM105 | None
    nm106: L2100A_NM106 | None
    nm107: L2100A_NM107 | None
    nm108: L2100A_NM108 | None
    nm109: L2100A_NM109 | None
    nm110: L2100A_NM110 | None
    nm111: L2100A_NM111 | None
    nm112: L2100A_NM112 | None


class L2100A_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IP']}]}}
        datatype = common.D_366
        codes = ['IP']
        min_len = 2
        max_len = 2


class L2100A_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100A_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100A_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100A_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100A_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'position': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100A_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100A_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'position': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100A_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2100A_PER(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER name=',
         'position': 400,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100A_PER01'},
                        'per02': {'$ref': '#/$elements/L2100A_PER02'},
                        'per03': {'$ref': '#/$elements/L2100A_PER03'},
                        'per04': {'$ref': '#/$elements/L2100A_PER04'},
                        'per05': {'$ref': '#/$elements/L2100A_PER05'},
                        'per06': {'$ref': '#/$elements/L2100A_PER06'},
                        'per07': {'$ref': '#/$elements/L2100A_PER07'},
                        'per08': {'$ref': '#/$elements/L2100A_PER08'},
                        'per09': {'$ref': '#/$elements/L2100A_PER09'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100A_PER01
    per02: L2100A_PER02 | None
    per03: L2100A_PER03
    per04: L2100A_PER04
    per05: L2100A_PER05 | None
    per06: L2100A_PER06 | None
    per07: L2100A_PER07 | None
    per08: L2100A_PER08 | None
    per09: L2100A_PER09 | None


class L2100A_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100A_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100A_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100A_N301'},
                        'n302': {'$ref': '#/$elements/L2100A_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100A_N301
    n302: L2100A_N302 | None


class L2100A_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100A_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100A_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100A_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100A_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['60', 'CY']}]}}
        datatype = common.D_309
        codes = ['60', 'CY']
        min_len = 1
        max_len = 2


class L2100A_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100A_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2100A_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100A_N401'},
                        'n402': {'$ref': '#/$elements/L2100A_N402'},
                        'n403': {'$ref': '#/$elements/L2100A_N403'},
                        'n404': {'$ref': '#/$elements/L2100A_N404'},
                        'n405': {'$ref': '#/$elements/L2100A_N405'},
                        'n406': {'$ref': '#/$elements/L2100A_N406'},
                        'n407': {'$ref': '#/$elements/L2100A_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2100A_N401
    n402: L2100A_N402 | None
    n403: L2100A_N403 | None
    n404: L2100A_N404 | None
    n405: L2100A_N405 | None
    n406: L2100A_N406 | None
    n407: L2100A_N407 | None


class L2100A_DMG01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DMG01 data_ele=1250',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2100A_DMG02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'position': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100A_DMG03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DMG03 data_ele=1068',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2100A_DMG04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG04 data_ele=1067',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/1067'},
                            {'enum': ['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X']}]}}
        datatype = common.D_1067
        codes = ['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X']
        min_len = 1
        max_len = 1


class L2100A_DMG05_01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05-01 data_ele=1109',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1109'},
                            {'enum': ['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                      'I', 'J', 'N', 'O', 'P', 'Z']}]}}
        datatype = common.D_1109
        codes = ['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'N', 'O', 'P', 'Z']
        min_len = 1
        max_len = 1


class L2100A_DMG05_02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05-02 data_ele=1270',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RET']}]}}
        datatype = common.D_1270
        codes = ['RET']
        min_len = 1
        max_len = 3


class L2100A_DMG05_03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05-03 data_ele=1271',
         'position': 3,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2100A_DMG05(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05 name= refdes= data_ele=C056',
         'sequence': 5,
         'syntax': ['P0203'],
         'type': 'object',
         'properties': {'dmg05_01': {'title': '',
                                     'usage': 'S',
                                     'description': 'xid=DMG05-01 data_ele=1109',
                                     'position': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1109'},
                                                        {'enum': ['7', '8', 'A', 'B',
                                                                  'C', 'D', 'E', 'F',
                                                                  'G', 'H', 'I', 'J',
                                                                  'N', 'O', 'P',
                                                                  'Z']}]}},
                        'dmg05_02': {'title': '',
                                     'usage': 'S',
                                     'description': 'xid=DMG05-02 data_ele=1270',
                                     'position': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RET']}]}},
                        'dmg05_03': {'title': '',
                                     'usage': 'S',
                                     'description': 'xid=DMG05-03 data_ele=1271',
                                     'position': 3,
                                     'type': {'$ref': '#/$common/1271'}}}}
    dmg05_01: L2100A_DMG05_01 | None
    dmg05_02: L2100A_DMG05_02 | None
    dmg05_03: L2100A_DMG05_03 | None


class L2100A_DMG06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG06 data_ele=1066',
         'position': 6,
         'type': {'allOf': [{'$ref': '#/$common/1066'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7']}]}}
        datatype = common.D_1066
        codes = ['1', '2', '3', '4', '5', '6', '7']
        min_len = 1
        max_len = 2


class L2100A_DMG07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DMG07 data_ele=26',
         'position': 7,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L2100A_DMG08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DMG08 data_ele=659',
         'position': 8,
         'type': {'$ref': '#/$common/659'}}
        datatype = common.D_659
        min_len = 1
        max_len = 2


class L2100A_DMG09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DMG09 data_ele=380',
         'position': 9,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100A_DMG10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG10 data_ele=1270',
         'position': 10,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['REC']}]}}
        datatype = common.D_1270
        codes = ['REC']
        min_len = 1
        max_len = 3


class L2100A_DMG11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG11 data_ele=1271',
         'position': 11,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2100A_DMG(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG name=',
         'position': 800,
         'syntax': ['P0102', 'P1011', 'C1105'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2100A_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2100A_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2100A_DMG03'},
                        'dmg04': {'$ref': '#/$elements/L2100A_DMG04'},
                        'dmg05': {'$ref': '#/$elements/L2100A_DMG05'},
                        'dmg06': {'$ref': '#/$elements/L2100A_DMG06'},
                        'dmg07': {'$ref': '#/$elements/L2100A_DMG07'},
                        'dmg08': {'$ref': '#/$elements/L2100A_DMG08'},
                        'dmg09': {'$ref': '#/$elements/L2100A_DMG09'},
                        'dmg10': {'$ref': '#/$elements/L2100A_DMG10'},
                        'dmg11': {'$ref': '#/$elements/L2100A_DMG11'}},
         'required': ['dmg01', 'dmg02', 'dmg03']}
        segment_name = 'DMG'
    dmg01: L2100A_DMG01
    dmg02: L2100A_DMG02
    dmg03: L2100A_DMG03
    dmg04: L2100A_DMG04 | None
    dmg05: L2100A_DMG05 | None
    dmg06: L2100A_DMG06 | None
    dmg07: L2100A_DMG07 | None
    dmg08: L2100A_DMG08 | None
    dmg09: L2100A_DMG09 | None
    dmg10: L2100A_DMG10 | None
    dmg11: L2100A_DMG11 | None


class L2100A_EC01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=EC01 data_ele=1176',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1176'},
                            {'enum': ['01', '02', '03', '04', '05', '06', '07', '08',
                                      '09', '10', '11', '12', '17', '18', '19', '20',
                                      '21', '22', '23']}]}}
        datatype = common.D_1176
        codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23']
        min_len = 2
        max_len = 3


class L2100A_EC02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=EC02 data_ele=1176',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1176'},
                            {'enum': ['01', '02', '03', '04', '05', '06', '07', '08',
                                      '09', '10', '11', '12', '17', '18', '19', '20',
                                      '21', '22', '23']}]}}
        datatype = common.D_1176
        codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23']
        min_len = 2
        max_len = 3


class L2100A_EC03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=EC03 data_ele=1176',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/1176'},
                            {'enum': ['01', '02', '03', '04', '05', '06', '07', '08',
                                      '09', '10', '11', '12', '17', '18', '19', '20',
                                      '21', '22', '23']}]}}
        datatype = common.D_1176
        codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23']
        min_len = 2
        max_len = 3


class L2100A_EC04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=EC04 data_ele=954',
         'position': 4,
         'type': {'$ref': '#/$common/954'}}
        datatype = common.D_954
        min_len = 1
        max_len = 10


class L2100A_EC05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=EC05 data_ele=1201',
         'position': 5,
         'type': {'$ref': '#/$common/1201'}}
        datatype = common.D_1201
        min_len = 1
        max_len = 1


class L2100A_EC06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=EC06 data_ele=1149',
         'position': 6,
         'type': {'$ref': '#/$common/1149'}}
        datatype = common.D_1149
        min_len = 4
        max_len = 6


class L2100A_EC(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=EC name=',
                   'position': 1000,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'EC'},
                                  'ec01': {'$ref': '#/$elements/L2100A_EC01'},
                                  'ec02': {'$ref': '#/$elements/L2100A_EC02'},
                                  'ec03': {'$ref': '#/$elements/L2100A_EC03'},
                                  'ec04': {'$ref': '#/$elements/L2100A_EC04'},
                                  'ec05': {'$ref': '#/$elements/L2100A_EC05'},
                                  'ec06': {'$ref': '#/$elements/L2100A_EC06'}},
                   'required': ['ec01']}}
        segment_name = 'EC'
    ec01: L2100A_EC01
    ec02: L2100A_EC02 | None
    ec03: L2100A_EC03 | None
    ec04: L2100A_EC04 | None
    ec05: L2100A_EC05 | None
    ec06: L2100A_EC06 | None


class L2100A_ICM01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ICM01 data_ele=594',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/594'},
                            {'enum': ['1', '2', '3', '4', '6', '7', '8', '9', 'B', 'C',
                                      'H', 'Q', 'S', 'U']}]}}
        datatype = common.D_594
        codes = ['1', '2', '3', '4', '6', '7', '8', '9', 'B', 'C', 'H', 'Q', 'S', 'U']
        min_len = 1
        max_len = 1


class L2100A_ICM02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=ICM02 data_ele=782',
         'position': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100A_ICM03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=ICM03 data_ele=380',
         'position': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100A_ICM04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=ICM04 data_ele=310',
         'position': 4,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100A_ICM05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=ICM05 data_ele=1214',
         'position': 5,
         'type': {'$ref': '#/$common/1214'}}
        datatype = common.D_1214
        min_len = 1
        max_len = 5


class L2100A_ICM06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=ICM06 data_ele=100',
         'position': 6,
         'type': {'$ref': '#/$common/100'}}
        datatype = common.D_100
        min_len = 3
        max_len = 3


class L2100A_ICM(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=ICM name=',
         'position': 1100,
         'type': 'object',
         'properties': {'xid': {'literal': 'ICM'},
                        'icm01': {'$ref': '#/$elements/L2100A_ICM01'},
                        'icm02': {'$ref': '#/$elements/L2100A_ICM02'},
                        'icm03': {'$ref': '#/$elements/L2100A_ICM03'},
                        'icm04': {'$ref': '#/$elements/L2100A_ICM04'},
                        'icm05': {'$ref': '#/$elements/L2100A_ICM05'},
                        'icm06': {'$ref': '#/$elements/L2100A_ICM06'}},
         'required': ['icm01', 'icm02']}
        segment_name = 'ICM'
    icm01: L2100A_ICM01
    icm02: L2100A_ICM02
    icm03: L2100A_ICM03 | None
    icm04: L2100A_ICM04 | None
    icm05: L2100A_ICM05 | None
    icm06: L2100A_ICM06 | None


class L2100A_AMT01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R']}]}}
        datatype = common.D_522
        codes = ['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R']
        min_len = 1
        max_len = 3


class L2100A_AMT02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'position': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100A_AMT03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=AMT03 data_ele=478',
         'position': 3,
         'type': {'$ref': '#/$common/478'}}
        datatype = common.D_478
        min_len = 1
        max_len = 1


class L2100A_AMT(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=AMT name=',
                   'position': 1200,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2100A_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2100A_AMT02'},
                                  'amt03': {'$ref': '#/$elements/L2100A_AMT03'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 7}
        segment_name = 'AMT'
    amt01: L2100A_AMT01
    amt02: L2100A_AMT02
    amt03: L2100A_AMT03 | None


class L2100A_HLH01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=HLH01 data_ele=1212',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1212'},
                            {'enum': ['N', 'S', 'T', 'U', 'X']}]}}
        datatype = common.D_1212
        codes = ['N', 'S', 'T', 'U', 'X']
        min_len = 1
        max_len = 1


class L2100A_HLH02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=HLH02 data_ele=65',
         'position': 2,
         'type': {'$ref': '#/$common/65'}}
        datatype = common.D_65
        min_len = 1
        max_len = 8


class L2100A_HLH03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=HLH03 data_ele=81',
         'position': 3,
         'type': {'$ref': '#/$common/81'}}
        datatype = common.D_81
        min_len = 1
        max_len = 10


class L2100A_HLH04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HLH04 data_ele=81',
         'position': 4,
         'type': {'$ref': '#/$common/81'}}
        datatype = common.D_81
        min_len = 1
        max_len = 10


class L2100A_HLH05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HLH05 data_ele=352',
         'position': 5,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100A_HLH06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HLH06 data_ele=1213',
         'position': 6,
         'type': {'$ref': '#/$common/1213'}}
        datatype = common.D_1213
        min_len = 1
        max_len = 1


class L2100A_HLH07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HLH07 data_ele=352',
         'position': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100A_HLH(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=HLH name=',
         'position': 1300,
         'type': 'object',
         'properties': {'xid': {'literal': 'HLH'},
                        'hlh01': {'$ref': '#/$elements/L2100A_HLH01'},
                        'hlh02': {'$ref': '#/$elements/L2100A_HLH02'},
                        'hlh03': {'$ref': '#/$elements/L2100A_HLH03'},
                        'hlh04': {'$ref': '#/$elements/L2100A_HLH04'},
                        'hlh05': {'$ref': '#/$elements/L2100A_HLH05'},
                        'hlh06': {'$ref': '#/$elements/L2100A_HLH06'},
                        'hlh07': {'$ref': '#/$elements/L2100A_HLH07'}},
         'required': ['hlh01']}
        segment_name = 'HLH'
    hlh01: L2100A_HLH01
    hlh02: L2100A_HLH02 | None
    hlh03: L2100A_HLH03 | None
    hlh04: L2100A_HLH04 | None
    hlh05: L2100A_HLH05 | None
    hlh06: L2100A_HLH06 | None
    hlh07: L2100A_HLH07 | None


class L2100A_LUI01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=LUI01 data_ele=66',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['LD', 'LE']}]}}
        datatype = common.D_66
        codes = ['LD', 'LE']
        min_len = 1
        max_len = 2


class L2100A_LUI02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=LUI02 data_ele=67',
         'position': 2,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100A_LUI03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=LUI03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100A_LUI04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=LUI04 data_ele=1303',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/1303'},
                            {'enum': ['5', '6', '7', '8']}]}}
        datatype = common.D_1303
        codes = ['5', '6', '7', '8']
        min_len = 1
        max_len = 2


class L2100A_LUI05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=LUI05 data_ele=1476',
         'position': 5,
         'type': {'$ref': '#/$common/1476'}}
        datatype = common.D_1476
        min_len = 1
        max_len = 1


class L2100A_LUI(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=LUI name=',
                   'position': 1500,
                   'syntax': ['P0102', 'L040203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'LUI'},
                                  'lui01': {'$ref': '#/$elements/L2100A_LUI01'},
                                  'lui02': {'$ref': '#/$elements/L2100A_LUI02'},
                                  'lui03': {'$ref': '#/$elements/L2100A_LUI03'},
                                  'lui04': {'$ref': '#/$elements/L2100A_LUI04'},
                                  'lui05': {'$ref': '#/$elements/L2100A_LUI05'}}}}
        segment_name = 'LUI'
    lui01: L2100A_LUI01 | None
    lui02: L2100A_LUI02 | None
    lui03: L2100A_LUI03 | None
    lui04: L2100A_LUI04 | None
    lui05: L2100A_LUI05 | None


class L2100A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100A name= type=None',
                   'position': 300,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100A_NM1'},
                                  'per': {'$ref': '#/$segments/L2100A_PER'},
                                  'n3': {'$ref': '#/$segments/L2100A_N3'},
                                  'n4': {'$ref': '#/$segments/L2100A_N4'},
                                  'dmg': {'$ref': '#/$segments/L2100A_DMG'},
                                  'ec': {'$ref': '#/$segments/L2100A_EC'},
                                  'icm': {'$ref': '#/$segments/L2100A_ICM'},
                                  'amt': {'$ref': '#/$segments/L2100A_AMT'},
                                  'hlh': {'$ref': '#/$segments/L2100A_HLH'},
                                  'lui': {'$ref': '#/$segments/L2100A_LUI'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100A_NM1
    per: L2100A_PER | None
    n3: L2100A_N3 | None
    n4: L2100A_N4 | None
    dmg: L2100A_DMG | None
    ec: list[L2100A_EC] | None
    icm: L2100A_ICM | None
    amt: list[L2100A_AMT] | None
    hlh: L2100A_HLH | None
    lui: list[L2100A_LUI] | None


class L2100B_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['70']}]}}
        datatype = common.D_98
        codes = ['70']
        min_len = 2
        max_len = 3


class L2100B_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100B_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100B_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
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
         'position': 10,
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
         'position': 11,
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
         'position': 12,
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
         'position': 300,
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
                        'nm109': {'$ref': '#/$elements/L2100B_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100B_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100B_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100B_NM112'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2100B_NM101
    nm102: L2100B_NM102
    nm103: L2100B_NM103
    nm104: L2100B_NM104 | None
    nm105: L2100B_NM105 | None
    nm106: L2100B_NM106 | None
    nm107: L2100B_NM107 | None
    nm108: L2100B_NM108 | None
    nm109: L2100B_NM109 | None
    nm110: L2100B_NM110 | None
    nm111: L2100B_NM111 | None
    nm112: L2100B_NM112 | None


class L2100B_DMG01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG01 data_ele=1250',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2100B_DMG02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG02 data_ele=1251',
         'position': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100B_DMG03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG03 data_ele=1068',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2100B_DMG04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG04 data_ele=1067',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/1067'},
                            {'enum': ['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X']}]}}
        datatype = common.D_1067
        codes = ['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X']
        min_len = 1
        max_len = 1


class L2100B_DMG05_01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05-01 data_ele=1109',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1109'},
                            {'enum': ['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                      'I', 'J', 'N', 'O', 'P', 'Z']}]}}
        datatype = common.D_1109
        codes = ['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'N', 'O', 'P', 'Z']
        min_len = 1
        max_len = 1


class L2100B_DMG05_02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05-02 data_ele=1270',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RET']}]}}
        datatype = common.D_1270
        codes = ['RET']
        min_len = 1
        max_len = 3


class L2100B_DMG05_03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05-03 data_ele=1271',
         'position': 3,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2100B_DMG05(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG05 name= refdes= data_ele=C056',
         'sequence': 5,
         'syntax': ['P0203'],
         'type': 'object',
         'properties': {'dmg05_01': {'title': '',
                                     'usage': 'S',
                                     'description': 'xid=DMG05-01 data_ele=1109',
                                     'position': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1109'},
                                                        {'enum': ['7', '8', 'A', 'B',
                                                                  'C', 'D', 'E', 'F',
                                                                  'G', 'H', 'I', 'J',
                                                                  'N', 'O', 'P',
                                                                  'Z']}]}},
                        'dmg05_02': {'title': '',
                                     'usage': 'S',
                                     'description': 'xid=DMG05-02 data_ele=1270',
                                     'position': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RET']}]}},
                        'dmg05_03': {'title': '',
                                     'usage': 'S',
                                     'description': 'xid=DMG05-03 data_ele=1271',
                                     'position': 3,
                                     'type': {'$ref': '#/$common/1271'}}}}
    dmg05_01: L2100B_DMG05_01 | None
    dmg05_02: L2100B_DMG05_02 | None
    dmg05_03: L2100B_DMG05_03 | None


class L2100B_DMG06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG06 data_ele=1066',
         'position': 6,
         'type': {'allOf': [{'$ref': '#/$common/1066'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7']}]}}
        datatype = common.D_1066
        codes = ['1', '2', '3', '4', '5', '6', '7']
        min_len = 1
        max_len = 2


class L2100B_DMG07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DMG07 data_ele=26',
         'position': 7,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L2100B_DMG08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DMG08 data_ele=659',
         'position': 8,
         'type': {'$ref': '#/$common/659'}}
        datatype = common.D_659
        min_len = 1
        max_len = 2


class L2100B_DMG09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DMG09 data_ele=380',
         'position': 9,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100B_DMG10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG10 data_ele=1270',
         'position': 10,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['REC']}]}}
        datatype = common.D_1270
        codes = ['REC']
        min_len = 1
        max_len = 3


class L2100B_DMG11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG11 data_ele=1271',
         'position': 11,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2100B_DMG(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DMG name=',
         'position': 800,
         'syntax': ['P0102', 'P1011', 'C1105'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2100B_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2100B_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2100B_DMG03'},
                        'dmg04': {'$ref': '#/$elements/L2100B_DMG04'},
                        'dmg05': {'$ref': '#/$elements/L2100B_DMG05'},
                        'dmg06': {'$ref': '#/$elements/L2100B_DMG06'},
                        'dmg07': {'$ref': '#/$elements/L2100B_DMG07'},
                        'dmg08': {'$ref': '#/$elements/L2100B_DMG08'},
                        'dmg09': {'$ref': '#/$elements/L2100B_DMG09'},
                        'dmg10': {'$ref': '#/$elements/L2100B_DMG10'},
                        'dmg11': {'$ref': '#/$elements/L2100B_DMG11'}}}
        segment_name = 'DMG'
    dmg01: L2100B_DMG01 | None
    dmg02: L2100B_DMG02 | None
    dmg03: L2100B_DMG03 | None
    dmg04: L2100B_DMG04 | None
    dmg05: L2100B_DMG05 | None
    dmg06: L2100B_DMG06 | None
    dmg07: L2100B_DMG07 | None
    dmg08: L2100B_DMG08 | None
    dmg09: L2100B_DMG09 | None
    dmg10: L2100B_DMG10 | None
    dmg11: L2100B_DMG11 | None


class L2100B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100B name= type=None',
                   'position': 300,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100B_NM1'},
                                  'dmg': {'$ref': '#/$segments/L2100B_DMG'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100B_NM1
    dmg: L2100B_DMG | None


class L2100C_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['31']}]}}
        datatype = common.D_98
        codes = ['31']
        min_len = 2
        max_len = 3


class L2100C_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100C_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100C_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100C_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100C_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100C_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100C_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L2100C_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100C_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100C_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100C_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100C_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100C_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100C_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100C_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100C_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100C_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100C_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100C_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100C_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100C_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100C_NM112'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100C_NM101
    nm102: L2100C_NM102
    nm103: L2100C_NM103 | None
    nm104: L2100C_NM104 | None
    nm105: L2100C_NM105 | None
    nm106: L2100C_NM106 | None
    nm107: L2100C_NM107 | None
    nm108: L2100C_NM108 | None
    nm109: L2100C_NM109 | None
    nm110: L2100C_NM110 | None
    nm111: L2100C_NM111 | None
    nm112: L2100C_NM112 | None


class L2100C_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100C_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100C_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N3 name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100C_N301'},
                        'n302': {'$ref': '#/$elements/L2100C_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100C_N301
    n302: L2100C_N302 | None


class L2100C_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100C_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100C_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100C_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100C_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2100C_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100C_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2100C_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N4 name=',
         'position': 600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100C_N401'},
                        'n402': {'$ref': '#/$elements/L2100C_N402'},
                        'n403': {'$ref': '#/$elements/L2100C_N403'},
                        'n404': {'$ref': '#/$elements/L2100C_N404'},
                        'n405': {'$ref': '#/$elements/L2100C_N405'},
                        'n406': {'$ref': '#/$elements/L2100C_N406'},
                        'n407': {'$ref': '#/$elements/L2100C_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2100C_N401
    n402: L2100C_N402 | None
    n403: L2100C_N403 | None
    n404: L2100C_N404 | None
    n405: L2100C_N405 | None
    n406: L2100C_N406 | None
    n407: L2100C_N407 | None


class L2100C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100C name= type=None',
                   'position': 300,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100C_NM1'},
                                  'n3': {'$ref': '#/$segments/L2100C_N3'},
                                  'n4': {'$ref': '#/$segments/L2100C_N4'}},
                   'required': ['nm1', 'n3', 'n4']},
         'maxItems': 1}
    nm1: L2100C_NM1
    n3: L2100C_N3
    n4: L2100C_N4


class L2100D_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['36']}]}}
        datatype = common.D_98
        codes = ['36']
        min_len = 2
        max_len = 3


class L2100D_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2100D_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100D_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100D_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100D_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100D_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100D_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34']}]}}
        datatype = common.D_66
        codes = ['24', '34']
        min_len = 1
        max_len = 2


class L2100D_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100D_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100D_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100D_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100D_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100D_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100D_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100D_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100D_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100D_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100D_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100D_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100D_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100D_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100D_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100D_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100D_NM112'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100D_NM101
    nm102: L2100D_NM102
    nm103: L2100D_NM103 | None
    nm104: L2100D_NM104 | None
    nm105: L2100D_NM105 | None
    nm106: L2100D_NM106 | None
    nm107: L2100D_NM107 | None
    nm108: L2100D_NM108 | None
    nm109: L2100D_NM109 | None
    nm110: L2100D_NM110 | None
    nm111: L2100D_NM111 | None
    nm112: L2100D_NM112 | None


class L2100D_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['EP']}]}}
        datatype = common.D_366
        codes = ['EP']
        min_len = 2
        max_len = 2


class L2100D_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100D_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100D_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100D_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100D_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'position': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100D_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100D_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'position': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100D_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2100D_PER(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER name=',
         'position': 400,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100D_PER01'},
                        'per02': {'$ref': '#/$elements/L2100D_PER02'},
                        'per03': {'$ref': '#/$elements/L2100D_PER03'},
                        'per04': {'$ref': '#/$elements/L2100D_PER04'},
                        'per05': {'$ref': '#/$elements/L2100D_PER05'},
                        'per06': {'$ref': '#/$elements/L2100D_PER06'},
                        'per07': {'$ref': '#/$elements/L2100D_PER07'},
                        'per08': {'$ref': '#/$elements/L2100D_PER08'},
                        'per09': {'$ref': '#/$elements/L2100D_PER09'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100D_PER01
    per02: L2100D_PER02 | None
    per03: L2100D_PER03
    per04: L2100D_PER04
    per05: L2100D_PER05 | None
    per06: L2100D_PER06 | None
    per07: L2100D_PER07 | None
    per08: L2100D_PER08 | None
    per09: L2100D_PER09 | None


class L2100D_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100D_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100D_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100D_N301'},
                        'n302': {'$ref': '#/$elements/L2100D_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100D_N301
    n302: L2100D_N302 | None


class L2100D_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100D_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100D_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100D_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100D_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2100D_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100D_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2100D_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100D_N401'},
                        'n402': {'$ref': '#/$elements/L2100D_N402'},
                        'n403': {'$ref': '#/$elements/L2100D_N403'},
                        'n404': {'$ref': '#/$elements/L2100D_N404'},
                        'n405': {'$ref': '#/$elements/L2100D_N405'},
                        'n406': {'$ref': '#/$elements/L2100D_N406'},
                        'n407': {'$ref': '#/$elements/L2100D_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2100D_N401
    n402: L2100D_N402 | None
    n403: L2100D_N403 | None
    n404: L2100D_N404 | None
    n405: L2100D_N405 | None
    n406: L2100D_N406 | None
    n407: L2100D_N407 | None


class L2100D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100D name= type=None',
                   'position': 300,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100D_NM1'},
                                  'per': {'$ref': '#/$segments/L2100D_PER'},
                                  'n3': {'$ref': '#/$segments/L2100D_N3'},
                                  'n4': {'$ref': '#/$segments/L2100D_N4'}},
                   'required': ['nm1']},
         'maxItems': 3}
    nm1: L2100D_NM1
    per: L2100D_PER | None
    n3: L2100D_N3 | None
    n4: L2100D_N4 | None


class L2100E_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['M8']}]}}
        datatype = common.D_98
        codes = ['M8']
        min_len = 2
        max_len = 3


class L2100E_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['2']}]}}
        datatype = common.D_1065
        codes = ['2']
        min_len = 1
        max_len = 1


class L2100E_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100E_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100E_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100E_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100E_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100E_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L2100E_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100E_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100E_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100E_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100E_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100E_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100E_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100E_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100E_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100E_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100E_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100E_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100E_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100E_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100E_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100E_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100E_NM112'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2100E_NM101
    nm102: L2100E_NM102
    nm103: L2100E_NM103
    nm104: L2100E_NM104 | None
    nm105: L2100E_NM105 | None
    nm106: L2100E_NM106 | None
    nm107: L2100E_NM107 | None
    nm108: L2100E_NM108 | None
    nm109: L2100E_NM109 | None
    nm110: L2100E_NM110 | None
    nm111: L2100E_NM111 | None
    nm112: L2100E_NM112 | None


class L2100E_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['SK']}]}}
        datatype = common.D_366
        codes = ['SK']
        min_len = 2
        max_len = 2


class L2100E_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100E_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100E_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100E_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100E_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'position': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100E_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100E_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'position': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100E_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2100E_PER(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER name=',
         'position': 400,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100E_PER01'},
                        'per02': {'$ref': '#/$elements/L2100E_PER02'},
                        'per03': {'$ref': '#/$elements/L2100E_PER03'},
                        'per04': {'$ref': '#/$elements/L2100E_PER04'},
                        'per05': {'$ref': '#/$elements/L2100E_PER05'},
                        'per06': {'$ref': '#/$elements/L2100E_PER06'},
                        'per07': {'$ref': '#/$elements/L2100E_PER07'},
                        'per08': {'$ref': '#/$elements/L2100E_PER08'},
                        'per09': {'$ref': '#/$elements/L2100E_PER09'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100E_PER01
    per02: L2100E_PER02 | None
    per03: L2100E_PER03
    per04: L2100E_PER04
    per05: L2100E_PER05 | None
    per06: L2100E_PER06 | None
    per07: L2100E_PER07 | None
    per08: L2100E_PER08 | None
    per09: L2100E_PER09 | None


class L2100E_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100E_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100E_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100E_N301'},
                        'n302': {'$ref': '#/$elements/L2100E_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100E_N301
    n302: L2100E_N302 | None


class L2100E_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100E_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100E_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100E_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100E_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2100E_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100E_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2100E_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100E_N401'},
                        'n402': {'$ref': '#/$elements/L2100E_N402'},
                        'n403': {'$ref': '#/$elements/L2100E_N403'},
                        'n404': {'$ref': '#/$elements/L2100E_N404'},
                        'n405': {'$ref': '#/$elements/L2100E_N405'},
                        'n406': {'$ref': '#/$elements/L2100E_N406'},
                        'n407': {'$ref': '#/$elements/L2100E_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2100E_N401
    n402: L2100E_N402 | None
    n403: L2100E_N403 | None
    n404: L2100E_N404 | None
    n405: L2100E_N405 | None
    n406: L2100E_N406 | None
    n407: L2100E_N407 | None


class L2100E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100E name= type=None',
                   'position': 300,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100E_NM1'},
                                  'per': {'$ref': '#/$segments/L2100E_PER'},
                                  'n3': {'$ref': '#/$segments/L2100E_N3'},
                                  'n4': {'$ref': '#/$segments/L2100E_N4'}},
                   'required': ['nm1']},
         'maxItems': 3}
    nm1: L2100E_NM1
    per: L2100E_PER | None
    n3: L2100E_N3 | None
    n4: L2100E_N4 | None


class L2100F_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['S3']}]}}
        datatype = common.D_98
        codes = ['S3']
        min_len = 2
        max_len = 3


class L2100F_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100F_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100F_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100F_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100F_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100F_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100F_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100F_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100F_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100F_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100F_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100F_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100F_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100F_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100F_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100F_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100F_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100F_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100F_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100F_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100F_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100F_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100F_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100F_NM112'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm104']}
        segment_name = 'NM1'
    nm101: L2100F_NM101
    nm102: L2100F_NM102
    nm103: L2100F_NM103
    nm104: L2100F_NM104
    nm105: L2100F_NM105 | None
    nm106: L2100F_NM106 | None
    nm107: L2100F_NM107 | None
    nm108: L2100F_NM108 | None
    nm109: L2100F_NM109 | None
    nm110: L2100F_NM110 | None
    nm111: L2100F_NM111 | None
    nm112: L2100F_NM112 | None


class L2100F_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['PQ']}]}}
        datatype = common.D_366
        codes = ['PQ']
        min_len = 2
        max_len = 2


class L2100F_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100F_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100F_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100F_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100F_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'position': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100F_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100F_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'position': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100F_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2100F_PER(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER name=',
         'position': 400,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100F_PER01'},
                        'per02': {'$ref': '#/$elements/L2100F_PER02'},
                        'per03': {'$ref': '#/$elements/L2100F_PER03'},
                        'per04': {'$ref': '#/$elements/L2100F_PER04'},
                        'per05': {'$ref': '#/$elements/L2100F_PER05'},
                        'per06': {'$ref': '#/$elements/L2100F_PER06'},
                        'per07': {'$ref': '#/$elements/L2100F_PER07'},
                        'per08': {'$ref': '#/$elements/L2100F_PER08'},
                        'per09': {'$ref': '#/$elements/L2100F_PER09'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100F_PER01
    per02: L2100F_PER02 | None
    per03: L2100F_PER03
    per04: L2100F_PER04
    per05: L2100F_PER05 | None
    per06: L2100F_PER06 | None
    per07: L2100F_PER07 | None
    per08: L2100F_PER08 | None
    per09: L2100F_PER09 | None


class L2100F_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100F_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100F_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100F_N301'},
                        'n302': {'$ref': '#/$elements/L2100F_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100F_N301
    n302: L2100F_N302 | None


class L2100F_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100F_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100F_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100F_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100F_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2100F_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100F_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2100F_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100F_N401'},
                        'n402': {'$ref': '#/$elements/L2100F_N402'},
                        'n403': {'$ref': '#/$elements/L2100F_N403'},
                        'n404': {'$ref': '#/$elements/L2100F_N404'},
                        'n405': {'$ref': '#/$elements/L2100F_N405'},
                        'n406': {'$ref': '#/$elements/L2100F_N406'},
                        'n407': {'$ref': '#/$elements/L2100F_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2100F_N401
    n402: L2100F_N402 | None
    n403: L2100F_N403 | None
    n404: L2100F_N404 | None
    n405: L2100F_N405 | None
    n406: L2100F_N406 | None
    n407: L2100F_N407 | None


class L2100F(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100F name= type=None',
                   'position': 300,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100F_NM1'},
                                  'per': {'$ref': '#/$segments/L2100F_PER'},
                                  'n3': {'$ref': '#/$segments/L2100F_N3'},
                                  'n4': {'$ref': '#/$segments/L2100F_N4'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100F_NM1
    per: L2100F_PER | None
    n3: L2100F_N3 | None
    n4: L2100F_N4 | None


class L2100G_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['6Y', '9K', 'E1', 'EI', 'EXS', 'GB', 'GD', 'J6',
                                      'LR', 'QD', 'S1', 'TZ', 'X4']}]}}
        datatype = common.D_98
        codes = ['6Y', '9K', 'E1', 'EI', 'EXS', 'GB', 'GD', 'J6', 'LR', 'QD', 'S1', 'TZ', 'X4']
        min_len = 2
        max_len = 3


class L2100G_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100G_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100G_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100G_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100G_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100G_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100G_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100G_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100G_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100G_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100G_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100G_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100G_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100G_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100G_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100G_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100G_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100G_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100G_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100G_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100G_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100G_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100G_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100G_NM112'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2100G_NM101
    nm102: L2100G_NM102
    nm103: L2100G_NM103
    nm104: L2100G_NM104 | None
    nm105: L2100G_NM105 | None
    nm106: L2100G_NM106 | None
    nm107: L2100G_NM107 | None
    nm108: L2100G_NM108 | None
    nm109: L2100G_NM109 | None
    nm110: L2100G_NM110 | None
    nm111: L2100G_NM111 | None
    nm112: L2100G_NM112 | None


class L2100G_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['RP']}]}}
        datatype = common.D_366
        codes = ['RP']
        min_len = 2
        max_len = 2


class L2100G_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100G_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100G_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100G_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100G_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'position': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100G_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100G_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'position': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100G_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2100G_PER(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER name=',
         'position': 400,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100G_PER01'},
                        'per02': {'$ref': '#/$elements/L2100G_PER02'},
                        'per03': {'$ref': '#/$elements/L2100G_PER03'},
                        'per04': {'$ref': '#/$elements/L2100G_PER04'},
                        'per05': {'$ref': '#/$elements/L2100G_PER05'},
                        'per06': {'$ref': '#/$elements/L2100G_PER06'},
                        'per07': {'$ref': '#/$elements/L2100G_PER07'},
                        'per08': {'$ref': '#/$elements/L2100G_PER08'},
                        'per09': {'$ref': '#/$elements/L2100G_PER09'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100G_PER01
    per02: L2100G_PER02 | None
    per03: L2100G_PER03
    per04: L2100G_PER04
    per05: L2100G_PER05 | None
    per06: L2100G_PER06 | None
    per07: L2100G_PER07 | None
    per08: L2100G_PER08 | None
    per09: L2100G_PER09 | None


class L2100G_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100G_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100G_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100G_N301'},
                        'n302': {'$ref': '#/$elements/L2100G_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100G_N301
    n302: L2100G_N302 | None


class L2100G_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100G_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100G_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100G_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100G_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2100G_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100G_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2100G_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100G_N401'},
                        'n402': {'$ref': '#/$elements/L2100G_N402'},
                        'n403': {'$ref': '#/$elements/L2100G_N403'},
                        'n404': {'$ref': '#/$elements/L2100G_N404'},
                        'n405': {'$ref': '#/$elements/L2100G_N405'},
                        'n406': {'$ref': '#/$elements/L2100G_N406'},
                        'n407': {'$ref': '#/$elements/L2100G_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2100G_N401
    n402: L2100G_N402 | None
    n403: L2100G_N403 | None
    n404: L2100G_N404 | None
    n405: L2100G_N405 | None
    n406: L2100G_N406 | None
    n407: L2100G_N407 | None


class L2100G(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100G name= type=None',
                   'position': 300,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100G_NM1'},
                                  'per': {'$ref': '#/$segments/L2100G_PER'},
                                  'n3': {'$ref': '#/$segments/L2100G_N3'},
                                  'n4': {'$ref': '#/$segments/L2100G_N4'}},
                   'required': ['nm1']},
         'maxItems': 13}
    nm1: L2100G_NM1
    per: L2100G_PER | None
    n3: L2100G_N3 | None
    n4: L2100G_N4 | None


class L2100H_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['45']}]}}
        datatype = common.D_98
        codes = ['45']
        min_len = 2
        max_len = 3


class L2100H_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100H_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100H_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100H_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100H_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100H_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100H_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L2100H_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100H_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2100H_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100H_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100H_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100H_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100H_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100H_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100H_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100H_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100H_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100H_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100H_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100H_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100H_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100H_NM111'},
                        'nm112': {'$ref': '#/$elements/L2100H_NM112'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100H_NM101
    nm102: L2100H_NM102
    nm103: L2100H_NM103 | None
    nm104: L2100H_NM104 | None
    nm105: L2100H_NM105 | None
    nm106: L2100H_NM106 | None
    nm107: L2100H_NM107 | None
    nm108: L2100H_NM108 | None
    nm109: L2100H_NM109 | None
    nm110: L2100H_NM110 | None
    nm111: L2100H_NM111 | None
    nm112: L2100H_NM112 | None


class L2100H_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100H_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100H_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100H_N301'},
                        'n302': {'$ref': '#/$elements/L2100H_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100H_N301
    n302: L2100H_N302 | None


class L2100H_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100H_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100H_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100H_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100H_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2100H_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100H_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2100H_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100H_N401'},
                        'n402': {'$ref': '#/$elements/L2100H_N402'},
                        'n403': {'$ref': '#/$elements/L2100H_N403'},
                        'n404': {'$ref': '#/$elements/L2100H_N404'},
                        'n405': {'$ref': '#/$elements/L2100H_N405'},
                        'n406': {'$ref': '#/$elements/L2100H_N406'},
                        'n407': {'$ref': '#/$elements/L2100H_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2100H_N401
    n402: L2100H_N402 | None
    n403: L2100H_N403 | None
    n404: L2100H_N404 | None
    n405: L2100H_N405 | None
    n406: L2100H_N406 | None
    n407: L2100H_N407 | None


class L2100H(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2100H name= type=None',
                   'position': 700,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100H_NM1'},
                                  'n3': {'$ref': '#/$segments/L2100H_N3'},
                                  'n4': {'$ref': '#/$segments/L2100H_N4'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100H_NM1
    n3: L2100H_N3 | None
    n4: L2100H_N4 | None


class L2200_DSB01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DSB01 data_ele=1146',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1146'},
                            {'enum': ['1', '2', '3', '4']}]}}
        datatype = common.D_1146
        codes = ['1', '2', '3', '4']
        min_len = 1
        max_len = 1


class L2200_DSB02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DSB02 data_ele=380',
         'position': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2200_DSB03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DSB03 data_ele=1149',
         'position': 3,
         'type': {'$ref': '#/$common/1149'}}
        datatype = common.D_1149
        min_len = 4
        max_len = 6


class L2200_DSB04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DSB04 data_ele=1154',
         'position': 4,
         'type': {'$ref': '#/$common/1154'}}
        datatype = common.D_1154
        min_len = 1
        max_len = 1


class L2200_DSB05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DSB05 data_ele=1161',
         'position': 5,
         'type': {'$ref': '#/$common/1161'}}
        datatype = common.D_1161
        min_len = 1
        max_len = 2


class L2200_DSB06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=DSB06 data_ele=782',
         'position': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200_DSB07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DSB07 data_ele=235',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/235'}, {'enum': ['DX', 'ZZ']}]}}
        datatype = common.D_235
        codes = ['DX', 'ZZ']
        min_len = 2
        max_len = 2


class L2200_DSB08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DSB08 data_ele=1137',
         'position': 8,
         'type': {'$ref': '#/$common/1137'}}
        datatype = common.D_1137
        min_len = 1
        max_len = 15


class L2200_DSB(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DSB name=',
         'position': 2000,
         'syntax': ['P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DSB'},
                        'dsb01': {'$ref': '#/$elements/L2200_DSB01'},
                        'dsb02': {'$ref': '#/$elements/L2200_DSB02'},
                        'dsb03': {'$ref': '#/$elements/L2200_DSB03'},
                        'dsb04': {'$ref': '#/$elements/L2200_DSB04'},
                        'dsb05': {'$ref': '#/$elements/L2200_DSB05'},
                        'dsb06': {'$ref': '#/$elements/L2200_DSB06'},
                        'dsb07': {'$ref': '#/$elements/L2200_DSB07'},
                        'dsb08': {'$ref': '#/$elements/L2200_DSB08'}},
         'required': ['dsb01']}
        segment_name = 'DSB'
    dsb01: L2200_DSB01
    dsb02: L2200_DSB02 | None
    dsb03: L2200_DSB03 | None
    dsb04: L2200_DSB04 | None
    dsb05: L2200_DSB05 | None
    dsb06: L2200_DSB06 | None
    dsb07: L2200_DSB07 | None
    dsb08: L2200_DSB08 | None


class L2200_DTP01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['360', '361']}]}}
        datatype = common.D_374
        codes = ['360', '361']
        min_len = 3
        max_len = 3


class L2200_DTP02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2200_DTP03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'position': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2200_DTP(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=DTP name=',
                   'position': 2100,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2200_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2200_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2200_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 2}
        segment_name = 'DTP'
    dtp01: L2200_DTP01
    dtp02: L2200_DTP02
    dtp03: L2200_DTP03


class L2200(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2200 name= type=None',
                   'position': 2000,
                   'type': 'object',
                   'properties': {'dsb': {'$ref': '#/$segments/L2200_DSB'},
                                  'dtp': {'$ref': '#/$segments/L2200_DTP'}},
                   'required': ['dsb']}}
    dsb: L2200_DSB
    dtp: list[L2200_DTP] | None


class L2300_HD01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=HD01 data_ele=875',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/875'},
                            {'enum': ['001', '002', '021', '024', '025', '026', '030',
                                      '032']}]}}
        datatype = common.D_875
        codes = ['001', '002', '021', '024', '025', '026', '030', '032']
        min_len = 3
        max_len = 3


class L2300_HD02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HD02 data_ele=1203',
         'position': 2,
         'type': {'$ref': '#/$common/1203'}}
        datatype = common.D_1203
        min_len = 2
        max_len = 3


class L2300_HD03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=HD03 data_ele=1205',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/1205'},
                            {'enum': ['AG', 'AH', 'AJ', 'AK', 'DCP', 'DEN', 'EPO',
                                      'FAC', 'HE', 'HLT', 'HMO', 'LTC', 'LTD', 'MM',
                                      'MOD', 'PDG', 'POS', 'PPO', 'PRA', 'STD', 'UR',
                                      'VIS']}]}}
        datatype = common.D_1205
        codes = ['AG', 'AH', 'AJ', 'AK', 'DCP', 'DEN', 'EPO', 'FAC', 'HE', 'HLT', 'HMO', 'LTC', 'LTD', 'MM', 'MOD', 'PDG', 'POS', 'PPO', 'PRA', 'STD', 'UR', 'VIS']
        min_len = 2
        max_len = 3


class L2300_HD04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=HD04 data_ele=1204',
         'position': 4,
         'type': {'$ref': '#/$common/1204'}}
        datatype = common.D_1204
        min_len = 1
        max_len = 50


class L2300_HD05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=HD05 data_ele=1207',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/1207'},
                            {'enum': ['CHD', 'DEP', 'E1D', 'E2D', 'E3D', 'E5D', 'E6D',
                                      'E7D', 'E8D', 'E9D', 'ECH', 'EMP', 'ESP', 'FAM',
                                      'IND', 'SPC', 'SPO', 'TWO']}]}}
        datatype = common.D_1207
        codes = ['CHD', 'DEP', 'E1D', 'E2D', 'E3D', 'E5D', 'E6D', 'E7D', 'E8D', 'E9D', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO', 'TWO']
        min_len = 3
        max_len = 3


class L2300_HD06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HD06 data_ele=609',
         'position': 6,
         'type': {'$ref': '#/$common/609'}}
        datatype = common.D_609
        min_len = 1
        max_len = 9


class L2300_HD07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HD07 data_ele=609',
         'position': 7,
         'type': {'$ref': '#/$common/609'}}
        datatype = common.D_609
        min_len = 1
        max_len = 9


class L2300_HD08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HD08 data_ele=1209',
         'position': 8,
         'type': {'$ref': '#/$common/1209'}}
        datatype = common.D_1209
        min_len = 1
        max_len = 1


class L2300_HD09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=HD09 data_ele=1073',
         'position': 9,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2300_HD10(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HD10 data_ele=1211',
         'position': 10,
         'type': {'$ref': '#/$common/1211'}}
        datatype = common.D_1211
        min_len = 2
        max_len = 3


class L2300_HD11(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=HD11 data_ele=1073',
         'position': 11,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_HD(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=HD name=',
         'position': 2600,
         'type': 'object',
         'properties': {'xid': {'literal': 'HD'},
                        'hd01': {'$ref': '#/$elements/L2300_HD01'},
                        'hd02': {'$ref': '#/$elements/L2300_HD02'},
                        'hd03': {'$ref': '#/$elements/L2300_HD03'},
                        'hd04': {'$ref': '#/$elements/L2300_HD04'},
                        'hd05': {'$ref': '#/$elements/L2300_HD05'},
                        'hd06': {'$ref': '#/$elements/L2300_HD06'},
                        'hd07': {'$ref': '#/$elements/L2300_HD07'},
                        'hd08': {'$ref': '#/$elements/L2300_HD08'},
                        'hd09': {'$ref': '#/$elements/L2300_HD09'},
                        'hd10': {'$ref': '#/$elements/L2300_HD10'},
                        'hd11': {'$ref': '#/$elements/L2300_HD11'}},
         'required': ['hd01', 'hd03']}
        segment_name = 'HD'
    hd01: L2300_HD01
    hd02: L2300_HD02 | None
    hd03: L2300_HD03
    hd04: L2300_HD04 | None
    hd05: L2300_HD05 | None
    hd06: L2300_HD06 | None
    hd07: L2300_HD07 | None
    hd08: L2300_HD08 | None
    hd09: L2300_HD09 | None
    hd10: L2300_HD10 | None
    hd11: L2300_HD11 | None


class L2300_DTP01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['300', '303', '343', '348', '349', '543',
                                      '695']}]}}
        datatype = common.D_374
        codes = ['300', '303', '343', '348', '349', '543', '695']
        min_len = 3
        max_len = 3


class L2300_DTP02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2300_DTP03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'position': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=DTP name=',
                   'position': 2700,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 6}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_AMT01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R']}]}}
        datatype = common.D_522
        codes = ['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R']
        min_len = 1
        max_len = 3


class L2300_AMT02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'position': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300_AMT03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=AMT03 data_ele=478',
         'position': 3,
         'type': {'$ref': '#/$common/478'}}
        datatype = common.D_478
        min_len = 1
        max_len = 1


class L2300_AMT(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=AMT name=',
                   'position': 2800,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2300_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2300_AMT02'},
                                  'amt03': {'$ref': '#/$elements/L2300_AMT03'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 9}
        segment_name = 'AMT'
    amt01: L2300_AMT01
    amt02: L2300_AMT02
    amt03: L2300_AMT03 | None


class L2300_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['17', '1L', '9V', 'CE', 'E8', 'M7', 'PID', 'RB',
                                      'X9', 'XM', 'XX1', 'XX2', 'ZX', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['17', '1L', '9V', 'CE', 'E8', 'M7', 'PID', 'RB', 'X9', 'XM', 'XX1', 'XX2', 'ZX', 'ZZ']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=REF name=',
                   'position': 2900,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2300_REF03'},
                                  'ref04': {'$ref': '#/$elements/L2300_REF04'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 14}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02
    ref03: L2300_REF03 | None


class L2300_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['QQ']}]}}
        datatype = common.D_128
        codes = ['QQ']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=REF name=',
         'position': 2900,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2300_REF01'},
                        'ref02': {'$ref': '#/$elements/L2300_REF02'},
                        'ref03': {'$ref': '#/$elements/L2300_REF03'},
                        'ref04': {'$ref': '#/$elements/L2300_REF04'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02
    ref03: L2300_REF03 | None


class L2300_IDC01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=IDC01 data_ele=1204',
         'position': 1,
         'type': {'$ref': '#/$common/1204'}}
        datatype = common.D_1204
        min_len = 1
        max_len = 50


class L2300_IDC02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=IDC02 data_ele=1215',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1215'}, {'enum': ['D', 'H', 'P']}]}}
        datatype = common.D_1215
        codes = ['D', 'H', 'P']
        min_len = 1
        max_len = 1


class L2300_IDC03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=IDC03 data_ele=380',
         'position': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_IDC04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=IDC04 data_ele=306',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/306'}, {'enum': ['1', '2', 'RX']}]}}
        datatype = common.D_306
        codes = ['1', '2', 'RX']
        min_len = 1
        max_len = 2


class L2300_IDC(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=IDC name=',
                   'position': 3000,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'IDC'},
                                  'idc01': {'$ref': '#/$elements/L2300_IDC01'},
                                  'idc02': {'$ref': '#/$elements/L2300_IDC02'},
                                  'idc03': {'$ref': '#/$elements/L2300_IDC03'},
                                  'idc04': {'$ref': '#/$elements/L2300_IDC04'}},
                   'required': ['idc01', 'idc02']},
         'maxItems': 3}
        segment_name = 'IDC'
    idc01: L2300_IDC01
    idc02: L2300_IDC02
    idc03: L2300_IDC03 | None
    idc04: L2300_IDC04 | None


class L2310_LX01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=LX01 data_ele=554',
         'position': 1,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2310_LX(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=LX name=',
         'position': 3100,
         'type': 'object',
         'properties': {'xid': {'literal': 'LX'},
                        'lx01': {'$ref': '#/$elements/L2310_LX01'}},
         'required': ['lx01']}
        segment_name = 'LX'
    lx01: L2310_LX01


class L2310_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['1X', '3D', '80', 'FA', 'OD', 'P3', 'QA', 'QN',
                                      'Y2']}]}}
        datatype = common.D_98
        codes = ['1X', '3D', '80', 'FA', 'OD', 'P3', 'QA', 'QN', 'Y2']
        min_len = 2
        max_len = 3


class L2310_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2310_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2310_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2310_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2310_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2310_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['34', 'FI', 'SV', 'XX']}]}}
        datatype = common.D_66
        codes = ['34', 'FI', 'SV', 'XX']
        min_len = 1
        max_len = 2


class L2310_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'allOf': [{'$ref': '#/$common/706'}, {'enum': ['25', '26', '72']}]}}
        datatype = common.D_706
        codes = ['25', '26', '72']
        min_len = 2
        max_len = 2


class L2310_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2310_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 3200,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310_NM103'},
                        'nm104': {'$ref': '#/$elements/L2310_NM104'},
                        'nm105': {'$ref': '#/$elements/L2310_NM105'},
                        'nm106': {'$ref': '#/$elements/L2310_NM106'},
                        'nm107': {'$ref': '#/$elements/L2310_NM107'},
                        'nm108': {'$ref': '#/$elements/L2310_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310_NM109'},
                        'nm110': {'$ref': '#/$elements/L2310_NM110'},
                        'nm111': {'$ref': '#/$elements/L2310_NM111'},
                        'nm112': {'$ref': '#/$elements/L2310_NM112'}},
         'required': ['nm101', 'nm102', 'nm110']}
        segment_name = 'NM1'
    nm101: L2310_NM101
    nm102: L2310_NM102
    nm103: L2310_NM103 | None
    nm104: L2310_NM104 | None
    nm105: L2310_NM105 | None
    nm106: L2310_NM106 | None
    nm107: L2310_NM107 | None
    nm108: L2310_NM108 | None
    nm109: L2310_NM109 | None
    nm110: L2310_NM110
    nm111: L2310_NM111 | None
    nm112: L2310_NM112 | None


class L2310_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2310_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2310_N3(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=N3 name=',
                   'position': 3500,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'N3'},
                                  'n301': {'$ref': '#/$elements/L2310_N301'},
                                  'n302': {'$ref': '#/$elements/L2310_N302'}},
                   'required': ['n301']},
         'maxItems': 2}
        segment_name = 'N3'
    n301: L2310_N301
    n302: L2310_N302 | None


class L2310_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2310_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2310_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2310_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2310_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2310_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2310_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2310_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 3600,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2310_N401'},
                        'n402': {'$ref': '#/$elements/L2310_N402'},
                        'n403': {'$ref': '#/$elements/L2310_N403'},
                        'n404': {'$ref': '#/$elements/L2310_N404'},
                        'n405': {'$ref': '#/$elements/L2310_N405'},
                        'n406': {'$ref': '#/$elements/L2310_N406'},
                        'n407': {'$ref': '#/$elements/L2310_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2310_N401
    n402: L2310_N402 | None
    n403: L2310_N403 | None
    n404: L2310_N404 | None
    n405: L2310_N405 | None
    n406: L2310_N406 | None
    n407: L2310_N407 | None


class L2310_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L2310_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2310_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2310_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2310_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2310_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'position': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2310_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE',
                                      'WP']}]}}
        datatype = common.D_365
        codes = ['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2310_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'position': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2310_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2310_PER(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=PER name=',
                   'position': 3700,
                   'syntax': ['P0304', 'P0506', 'P0708'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2310_PER01'},
                                  'per02': {'$ref': '#/$elements/L2310_PER02'},
                                  'per03': {'$ref': '#/$elements/L2310_PER03'},
                                  'per04': {'$ref': '#/$elements/L2310_PER04'},
                                  'per05': {'$ref': '#/$elements/L2310_PER05'},
                                  'per06': {'$ref': '#/$elements/L2310_PER06'},
                                  'per07': {'$ref': '#/$elements/L2310_PER07'},
                                  'per08': {'$ref': '#/$elements/L2310_PER08'},
                                  'per09': {'$ref': '#/$elements/L2310_PER09'}},
                   'required': ['per01', 'per03', 'per04']},
         'maxItems': 2}
        segment_name = 'PER'
    per01: L2310_PER01
    per02: L2310_PER02 | None
    per03: L2310_PER03
    per04: L2310_PER04
    per05: L2310_PER05 | None
    per06: L2310_PER06 | None
    per07: L2310_PER07 | None
    per08: L2310_PER08 | None
    per09: L2310_PER09 | None


class L2310_PLA01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PLA01 data_ele=306',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/306'}, {'enum': ['2']}]}}
        datatype = common.D_306
        codes = ['2']
        min_len = 1
        max_len = 2


class L2310_PLA02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PLA02 data_ele=98',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['1P']}]}}
        datatype = common.D_98
        codes = ['1P']
        min_len = 2
        max_len = 3


class L2310_PLA03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PLA03 data_ele=373',
         'position': 3,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2310_PLA04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PLA04 data_ele=337',
         'position': 4,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2310_PLA05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PLA05 data_ele=1203',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/1203'},
                            {'enum': ['14', '22', '46', 'AA', 'AB', 'AC', 'AD', 'AE',
                                      'AF', 'AG', 'AH', 'AI', 'AJ']}]}}
        datatype = common.D_1203
        codes = ['14', '22', '46', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ']
        min_len = 2
        max_len = 3


class L2310_PLA(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PLA name=',
         'position': 3950,
         'type': 'object',
         'properties': {'xid': {'literal': 'PLA'},
                        'pla01': {'$ref': '#/$elements/L2310_PLA01'},
                        'pla02': {'$ref': '#/$elements/L2310_PLA02'},
                        'pla03': {'$ref': '#/$elements/L2310_PLA03'},
                        'pla04': {'$ref': '#/$elements/L2310_PLA04'},
                        'pla05': {'$ref': '#/$elements/L2310_PLA05'}},
         'required': ['pla01', 'pla02', 'pla03', 'pla05']}
        segment_name = 'PLA'
    pla01: L2310_PLA01
    pla02: L2310_PLA02
    pla03: L2310_PLA03
    pla04: L2310_PLA04 | None
    pla05: L2310_PLA05


class L2310(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2310 name= type=None',
                   'position': 3100,
                   'type': 'object',
                   'properties': {'lx': {'$ref': '#/$segments/L2310_LX'},
                                  'nm1': {'$ref': '#/$segments/L2310_NM1'},
                                  'n3': {'$ref': '#/$segments/L2310_N3'},
                                  'n4': {'$ref': '#/$segments/L2310_N4'},
                                  'per': {'$ref': '#/$segments/L2310_PER'},
                                  'pla': {'$ref': '#/$segments/L2310_PLA'}},
                   'required': ['lx', 'nm1']},
         'maxItems': 30}
    lx: L2310_LX
    nm1: L2310_NM1
    n3: list[L2310_N3] | None
    n4: L2310_N4 | None
    per: list[L2310_PER] | None
    pla: L2310_PLA | None


class L2320_COB01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=COB01 data_ele=1138',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1138'},
                            {'enum': ['P', 'S', 'T', 'U']}]}}
        datatype = common.D_1138
        codes = ['P', 'S', 'T', 'U']
        min_len = 1
        max_len = 1


class L2320_COB02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=COB02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320_COB03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=COB03 data_ele=1143',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/1143'}, {'enum': ['1', '5', '6']}]}}
        datatype = common.D_1143
        codes = ['1', '5', '6']
        min_len = 1
        max_len = 1


class L2320_COB04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=COB04 data_ele=1365',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/1365'},
                            {'enum': ['1', '35', '48', '50', '54', '89', '90', 'A4',
                                      'AG', 'AL', 'BB']}]}}
        datatype = common.D_1365
        codes = ['1', '35', '48', '50', '54', '89', '90', 'A4', 'AG', 'AL', 'BB']
        min_len = 1
        max_len = 2


class L2320_COB(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=COB name=',
         'position': 4000,
         'type': 'object',
         'properties': {'xid': {'literal': 'COB'},
                        'cob01': {'$ref': '#/$elements/L2320_COB01'},
                        'cob02': {'$ref': '#/$elements/L2320_COB02'},
                        'cob03': {'$ref': '#/$elements/L2320_COB03'},
                        'cob04': {'$ref': '#/$elements/L2320_COB04'}},
         'required': ['cob01', 'cob03']}
        segment_name = 'COB'
    cob01: L2320_COB01
    cob02: L2320_COB02 | None
    cob03: L2320_COB03
    cob04: L2320_COB04 | None


class L2320_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['60', '6P', 'SY', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['60', '6P', 'SY', 'ZZ']
        min_len = 2
        max_len = 3


class L2320_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2320_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2320_REF(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=REF name=',
                   'position': 4050,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2320_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2320_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2320_REF03'},
                                  'ref04': {'$ref': '#/$elements/L2320_REF04'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 4}
        segment_name = 'REF'
    ref01: L2320_REF01
    ref02: L2320_REF02
    ref03: L2320_REF03 | None


class L2320_DTP01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['344', '345']}]}}
        datatype = common.D_374
        codes = ['344', '345']
        min_len = 3
        max_len = 3


class L2320_DTP02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2320_DTP03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'position': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2320_DTP(Segment):
    """"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=DTP name=',
                   'position': 4070,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2320_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2320_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2320_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 2}
        segment_name = 'DTP'
    dtp01: L2320_DTP01
    dtp02: L2320_DTP02
    dtp03: L2320_DTP03


class L2330_NM101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['36', 'GW', 'IN']}]}}
        datatype = common.D_98
        codes = ['36', 'GW', 'IN']
        min_len = 2
        max_len = 3


class L2330_NM102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['2']}]}}
        datatype = common.D_1065
        codes = ['2']
        min_len = 1
        max_len = 1


class L2330_NM103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330_NM104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2330_NM105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2330_NM106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'position': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2330_NM107(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM107 data_ele=1039',
         'position': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2330_NM108(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'NI', 'XV']}]}}
        datatype = common.D_66
        codes = ['FI', 'NI', 'XV']
        min_len = 1
        max_len = 2


class L2330_NM109(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2330_NM110(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'position': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2330_NM111(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2330_NM112(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'position': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330_NM1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=NM1 name=',
         'position': 4100,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330_NM102'},
                        'nm103': {'$ref': '#/$elements/L2330_NM103'},
                        'nm104': {'$ref': '#/$elements/L2330_NM104'},
                        'nm105': {'$ref': '#/$elements/L2330_NM105'},
                        'nm106': {'$ref': '#/$elements/L2330_NM106'},
                        'nm107': {'$ref': '#/$elements/L2330_NM107'},
                        'nm108': {'$ref': '#/$elements/L2330_NM108'},
                        'nm109': {'$ref': '#/$elements/L2330_NM109'},
                        'nm110': {'$ref': '#/$elements/L2330_NM110'},
                        'nm111': {'$ref': '#/$elements/L2330_NM111'},
                        'nm112': {'$ref': '#/$elements/L2330_NM112'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2330_NM101
    nm102: L2330_NM102
    nm103: L2330_NM103 | None
    nm104: L2330_NM104 | None
    nm105: L2330_NM105 | None
    nm106: L2330_NM106 | None
    nm107: L2330_NM107 | None
    nm108: L2330_NM108 | None
    nm109: L2330_NM109 | None
    nm110: L2330_NM110 | None
    nm111: L2330_NM111 | None
    nm112: L2330_NM112 | None


class L2330_N301(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2330_N302(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'position': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2330_N3(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N3 name=',
         'position': 4300,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2330_N301'},
                        'n302': {'$ref': '#/$elements/L2330_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2330_N301
    n302: L2330_N302 | None


class L2330_N401(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2330_N402(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2330_N403(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2330_N404(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2330_N405(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2330_N406(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2330_N407(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'position': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L2330_N4(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=N4 name=',
         'position': 4400,
         'syntax': ['E0207', 'C0605', 'C0704'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2330_N401'},
                        'n402': {'$ref': '#/$elements/L2330_N402'},
                        'n403': {'$ref': '#/$elements/L2330_N403'},
                        'n404': {'$ref': '#/$elements/L2330_N404'},
                        'n405': {'$ref': '#/$elements/L2330_N405'},
                        'n406': {'$ref': '#/$elements/L2330_N406'},
                        'n407': {'$ref': '#/$elements/L2330_N407'}},
         'required': ['n401']}
        segment_name = 'N4'
    n401: L2330_N401
    n402: L2330_N402 | None
    n403: L2330_N403 | None
    n404: L2330_N404 | None
    n405: L2330_N405 | None
    n406: L2330_N406 | None
    n407: L2330_N407 | None


class L2330_PER01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['CN']}]}}
        datatype = common.D_366
        codes = ['CN']
        min_len = 2
        max_len = 2


class L2330_PER02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2330_PER03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['TE']}]}}
        datatype = common.D_365
        codes = ['TE']
        min_len = 2
        max_len = 2


class L2330_PER04(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330_PER05(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER05 data_ele=365',
         'position': 5,
         'type': {'$ref': '#/$common/365'}}
        datatype = common.D_365
        min_len = 2
        max_len = 2


class L2330_PER06(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER06 data_ele=364',
         'position': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330_PER07(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER07 data_ele=365',
         'position': 7,
         'type': {'$ref': '#/$common/365'}}
        datatype = common.D_365
        min_len = 2
        max_len = 2


class L2330_PER08(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER08 data_ele=364',
         'position': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330_PER09(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2330_PER(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=PER name=',
         'position': 4500,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2330_PER01'},
                        'per02': {'$ref': '#/$elements/L2330_PER02'},
                        'per03': {'$ref': '#/$elements/L2330_PER03'},
                        'per04': {'$ref': '#/$elements/L2330_PER04'},
                        'per05': {'$ref': '#/$elements/L2330_PER05'},
                        'per06': {'$ref': '#/$elements/L2330_PER06'},
                        'per07': {'$ref': '#/$elements/L2330_PER07'},
                        'per08': {'$ref': '#/$elements/L2330_PER08'},
                        'per09': {'$ref': '#/$elements/L2330_PER09'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2330_PER01
    per02: L2330_PER02 | None
    per03: L2330_PER03
    per04: L2330_PER04
    per05: L2330_PER05 | None
    per06: L2330_PER06 | None
    per07: L2330_PER07 | None
    per08: L2330_PER08 | None
    per09: L2330_PER09 | None


class L2330(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2330 name= type=None',
                   'position': 4510,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330_NM1'},
                                  'n3': {'$ref': '#/$segments/L2330_N3'},
                                  'n4': {'$ref': '#/$segments/L2330_N4'},
                                  'per': {'$ref': '#/$segments/L2330_PER'}},
                   'required': ['nm1']},
         'maxItems': 3}
    nm1: L2330_NM1
    n3: L2330_N3 | None
    n4: L2330_N4 | None
    per: L2330_PER | None


class L2320(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2320 name= type=None',
                   'position': 4000,
                   'type': 'object',
                   'properties': {'cob': {'$ref': '#/$segments/L2320_COB'},
                                  'ref': {'$ref': '#/$segments/L2320_REF'},
                                  'dtp': {'$ref': '#/$segments/L2320_DTP'},
                                  'l2330': {'$ref': '#/$segments/L2330'}},
                   'required': ['cob', 'l2330']},
         'maxItems': 5}
    cob: L2320_COB
    ref: list[L2320_REF] | None
    dtp: list[L2320_DTP] | None
    l2330: list[L2330]


class L2300(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2300 name= type=None',
                   'position': 2600,
                   'type': 'object',
                   'properties': {'hd': {'$ref': '#/$segments/L2300_HD'},
                                  'dtp': {'$ref': '#/$segments/L2300_DTP'},
                                  'amt': {'$ref': '#/$segments/L2300_AMT'},
                                  'ref': {'$ref': '#/$segments/L2300_REF'},
                                  'idc': {'$ref': '#/$segments/L2300_IDC'},
                                  'l2310': {'$ref': '#/$segments/L2310'},
                                  'l2320': {'$ref': '#/$segments/L2320'}},
                   'required': ['hd', 'dtp', 'l2310', 'l2320']},
         'maxItems': 99}
    hd: L2300_HD
    dtp: list[L2300_DTP]
    amt: list[L2300_AMT] | None
    ref: list[L2300_REF] | None
    ref: L2300_REF | None
    idc: list[L2300_IDC] | None
    l2310: list[L2310]
    l2320: list[L2320]


class L2700_LS_LS01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=LS01 data_ele=447',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/447'}, {'enum': ['2700']}]}}
        datatype = common.D_447
        codes = ['2700']
        min_len = 1
        max_len = 4


class L2700_LS_LS(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=LS name=',
         'position': 6880,
         'type': 'object',
         'properties': {'xid': {'literal': 'LS'},
                        'ls01': {'$ref': '#/$elements/L2700_LS_LS01'}},
         'required': ['ls01']}
        segment_name = 'LS'
    ls01: L2700_LS_LS01


class L2700_LX01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=LX01 data_ele=554',
         'position': 1,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2700_LX(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=LX name=',
         'position': 6881,
         'type': 'object',
         'properties': {'xid': {'literal': 'LX'},
                        'lx01': {'$ref': '#/$elements/L2700_LX01'}},
         'required': ['lx01']}
        segment_name = 'LX'
    lx01: L2700_LX01


class L2750_N101(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['75']}]}}
        datatype = common.D_98
        codes = ['75']
        min_len = 2
        max_len = 3


class L2750_N102(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N102 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2750_N103(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N103 data_ele=66',
         'position': 3,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L2750_N104(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N104 data_ele=67',
         'position': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2750_N105(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'position': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2750_N106(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'position': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2750_N1(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=N1 name=',
         'position': 6882,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L2750_N101'},
                        'n102': {'$ref': '#/$elements/L2750_N102'},
                        'n103': {'$ref': '#/$elements/L2750_N103'},
                        'n104': {'$ref': '#/$elements/L2750_N104'},
                        'n105': {'$ref': '#/$elements/L2750_N105'},
                        'n106': {'$ref': '#/$elements/L2750_N106'}},
         'required': ['n101', 'n102']}
        segment_name = 'N1'
    n101: L2750_N101
    n102: L2750_N102
    n103: L2750_N103 | None
    n104: L2750_N104 | None
    n105: L2750_N105 | None
    n106: L2750_N106 | None


class L2750_REF01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['00', '17', '18', '19', '26', '3L', '6M', '9V',
                                      '9X', 'GE', 'LU', 'PID', 'XX1', 'XX2', 'YY',
                                      'ZZ']}]}}
        datatype = common.D_128
        codes = ['00', '17', '18', '19', '26', '3L', '6M', '9V', '9X', 'GE', 'LU', 'PID', 'XX1', 'XX2', 'YY', 'ZZ']
        min_len = 2
        max_len = 3


class L2750_REF02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2750_REF03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2750_REF04(Composite):
    class Schema:
        json = {'title': '',
         'usage': 'N',
         'description': 'xid=REF04 name= refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2750_REF(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=REF name=',
         'position': 6883,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2750_REF01'},
                        'ref02': {'$ref': '#/$elements/L2750_REF02'},
                        'ref03': {'$ref': '#/$elements/L2750_REF03'},
                        'ref04': {'$ref': '#/$elements/L2750_REF04'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2750_REF01
    ref02: L2750_REF02
    ref03: L2750_REF03 | None


class L2750_DTP01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['007']}]}}
        datatype = common.D_374
        codes = ['007']
        min_len = 3
        max_len = 3


class L2750_DTP02(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2750_DTP03(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'position': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2750_DTP(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=DTP name=',
         'position': 6884,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2750_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2750_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2750_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2750_DTP01
    dtp02: L2750_DTP02
    dtp03: L2750_DTP03


class L2750(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2750 name= type=None',
                   'position': 6882,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L2750_N1'},
                                  'ref': {'$ref': '#/$segments/L2750_REF'},
                                  'dtp': {'$ref': '#/$segments/L2750_DTP'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L2750_N1
    ref: L2750_REF | None
    dtp: L2750_DTP | None


class L2700_LE01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=LE01 data_ele=447',
         'position': 1,
         'type': {'$ref': '#/$common/447'}}
        datatype = common.D_447
        min_len = 1
        max_len = 4


class L2700_LE(Segment):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'S',
         'description': 'xid=LE name=',
         'position': 6885,
         'type': 'object',
         'properties': {'xid': {'literal': 'LE'},
                        'le01': {'$ref': '#/$elements/L2700_LE01'}},
         'required': ['le01']}
        segment_name = 'LE'
    le01: L2700_LE01


class L2700(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2700 name= type=None',
                   'position': 6881,
                   'type': 'object',
                   'properties': {'lx': {'$ref': '#/$segments/L2700_LX'},
                                  'l2750': {'$ref': '#/$segments/L2750'},
                                  'le': {'$ref': '#/$segments/L2700_LE'}},
                   'required': ['lx', 'l2750']}}
    lx: L2700_LX
    l2750: list[L2750]
    le: L2700_LE | None


class L2700_LS(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'S',
                   'description': 'xid=2700_LS name= type=None',
                   'position': 6800,
                   'type': 'object',
                   'properties': {'ls': {'$ref': '#/$segments/L2700_LS_LS'},
                                  'l2700': {'$ref': '#/$segments/L2700'}},
                   'required': ['ls', 'l2700']},
         'maxItems': 1}
    ls: L2700_LS_LS
    l2700: list[L2700]


class L2000(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=2000 name= type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'ins': {'$ref': '#/$segments/L2000_INS'},
                                  'ref': {'$ref': '#/$segments/L2000_REF'},
                                  'dtp': {'$ref': '#/$segments/L2000_DTP'},
                                  'l2100a': {'$ref': '#/$segments/L2100A'},
                                  'l2100b': {'$ref': '#/$segments/L2100B'},
                                  'l2100c': {'$ref': '#/$segments/L2100C'},
                                  'l2100d': {'$ref': '#/$segments/L2100D'},
                                  'l2100e': {'$ref': '#/$segments/L2100E'},
                                  'l2100f': {'$ref': '#/$segments/L2100F'},
                                  'l2100g': {'$ref': '#/$segments/L2100G'},
                                  'l2100h': {'$ref': '#/$segments/L2100H'},
                                  'l2200': {'$ref': '#/$segments/L2200'},
                                  'l2300': {'$ref': '#/$segments/L2300'},
                                  'l2700_ls': {'$ref': '#/$segments/L2700_LS'}},
                   'required': ['ins', 'ref', 'l2100a', 'l2100b', 'l2100c', 'l2100d',
                                'l2100e', 'l2100f', 'l2100g', 'l2100h', 'l2200',
                                'l2300']}}
    ins: L2000_INS
    ref: L2000_REF
    ref: L2000_REF
    ref: list[L2000_REF]
    dtp: list[L2000_DTP] | None
    l2100a: list[L2100A]
    l2100b: list[L2100B]
    l2100c: list[L2100C]
    l2100d: list[L2100D]
    l2100e: list[L2100E]
    l2100f: list[L2100F]
    l2100g: list[L2100G]
    l2100h: list[L2100H]
    l2200: list[L2200]
    l2300: list[L2300]
    l2700_ls: list[L2700_LS] | None


class TABLE2AREA2(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': '',
                   'usage': 'R',
                   'description': 'xid=TABLE2AREA2 name= type=wrapper',
                   'position': 120,
                   'type': 'object',
                   'properties': {'l2000': {'$ref': '#/$segments/L2000'}},
                   'required': ['l2000']}}
    l2000: list[L2000]


class ST_LOOP_SE01(Element):
    """"""
    class Schema:
        json = {'title': '',
         'usage': 'R',
         'description': 'xid=SE01 data_ele=96',
         'position': 1,
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
         'position': 2,
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
         'position': 6900,
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
                                  'se': {'$ref': '#/$segments/ST_LOOP_SE'}},
                   'required': ['st', 'header', 'table2area2', 'se']}}
    st: ST_LOOP_ST
    header: list[HEADER]
    table2area2: list[TABLE2AREA2]
    se: ST_LOOP_SE


class MSG834A1(Message):
    """HIPAA Benefit Enrollment and Maintenance 005010X220A1 834A1"""
    class Schema:
        json = {'title': 'HIPAA Benefit Enrollment and Maintenance 005010X220A1 834A1',
         'description': 'xid=834A1 name=HIPAA Benefit Enrollment and Maintenance '
                        '005010X220A1 834A1',
         'type': 'object',
         'properties': {'st_loop': {'$ref': '#/$loops/ST_LOOP'}},
         'required': ['st_loop']}
    st_loop: list[ST_LOOP]
