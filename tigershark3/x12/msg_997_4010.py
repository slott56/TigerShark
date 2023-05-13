"""
997.4010
Created 2023-05-12 20:25:36.094251
"""
from .base import *
from . import common


class ISA_LOOP_ISA01(Element):
    """Authorization Information Qualifier"""
    class Schema:
        json = {'title': 'Authorization Information Qualifier',
         'usage': 'R',
         'description': 'xid=ISA01 data_ele=I01',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/I01'}, {'enum': ['00', '03']}]}}
        datatype = common.I01
        codes = ['00', '03']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA02(Element):
    """Authorization Information"""
    class Schema:
        json = {'title': 'Authorization Information',
         'usage': 'R',
         'description': 'xid=ISA02 data_ele=I02',
         'position': 2,
         'type': {'$ref': '#/$common/I02'}}
        datatype = common.I02
        min_len = 10
        max_len = 10


class ISA_LOOP_ISA03(Element):
    """Security Information Qualifier"""
    class Schema:
        json = {'title': 'Security Information Qualifier',
         'usage': 'R',
         'description': 'xid=ISA03 data_ele=I03',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/I03'}, {'enum': ['00', '01']}]}}
        datatype = common.I03
        codes = ['00', '01']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA04(Element):
    """Security Information"""
    class Schema:
        json = {'title': 'Security Information',
         'usage': 'R',
         'description': 'xid=ISA04 data_ele=I04',
         'position': 4,
         'type': {'$ref': '#/$common/I04'}}
        datatype = common.I04
        min_len = 10
        max_len = 10


class ISA_LOOP_ISA05(Element):
    """Interchange ID Qualifier"""
    class Schema:
        json = {'title': 'Interchange ID Qualifier',
         'usage': 'R',
         'description': 'xid=ISA05 data_ele=I05',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/I05'},
                            {'enum': ['01', '14', '20', '27', '28', '29', '30', '33',
                                      'ZZ']}]}}
        datatype = common.I05
        codes = ['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA06(Element):
    """Interchange Sender ID"""
    class Schema:
        json = {'title': 'Interchange Sender ID',
         'usage': 'R',
         'description': 'xid=ISA06 data_ele=I06',
         'position': 6,
         'type': {'$ref': '#/$common/I06'}}
        datatype = common.I06
        min_len = 15
        max_len = 15


class ISA_LOOP_ISA07(Element):
    """Interchange ID Qualifier"""
    class Schema:
        json = {'title': 'Interchange ID Qualifier',
         'usage': 'R',
         'description': 'xid=ISA07 data_ele=I05',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/I05'},
                            {'enum': ['01', '14', '20', '27', '28', '29', '30', '33',
                                      'ZZ']}]}}
        datatype = common.I05
        codes = ['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA08(Element):
    """Interchange Receiver ID"""
    class Schema:
        json = {'title': 'Interchange Receiver ID',
         'usage': 'R',
         'description': 'xid=ISA08 data_ele=I07',
         'position': 8,
         'type': {'$ref': '#/$common/I07'}}
        datatype = common.I07
        min_len = 15
        max_len = 15


class ISA_LOOP_ISA09(Element):
    """Interchange Date"""
    class Schema:
        json = {'title': 'Interchange Date',
         'usage': 'R',
         'description': 'xid=ISA09 data_ele=I08',
         'position': 9,
         'type': {'$ref': '#/$common/I08'}}
        datatype = common.I08
        min_len = 6
        max_len = 6


class ISA_LOOP_ISA10(Element):
    """Interchange Time"""
    class Schema:
        json = {'title': 'Interchange Time',
         'usage': 'R',
         'description': 'xid=ISA10 data_ele=I09',
         'position': 10,
         'type': {'$ref': '#/$common/I09'}}
        datatype = common.I09
        min_len = 4
        max_len = 4


class ISA_LOOP_ISA11(Element):
    """Interchange Control Standards Identifier"""
    class Schema:
        json = {'title': 'Interchange Control Standards Identifier',
         'usage': 'R',
         'description': 'xid=ISA11 data_ele=I10',
         'position': 11,
         'type': {'allOf': [{'$ref': '#/$common/I10'}, {'enum': ['U']}]}}
        datatype = common.I10
        codes = ['U']
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA12(Element):
    """Interchange Control Version Number"""
    class Schema:
        json = {'title': 'Interchange Control Version Number',
         'usage': 'R',
         'description': 'xid=ISA12 data_ele=I11',
         'position': 12,
         'type': {'allOf': [{'$ref': '#/$common/I11'}, {'enum': ['00401']}]}}
        datatype = common.I11
        codes = ['00401']
        min_len = 5
        max_len = 5


class ISA_LOOP_ISA13(Element):
    """Interchange Control Number"""
    class Schema:
        json = {'title': 'Interchange Control Number',
         'usage': 'R',
         'description': 'xid=ISA13 data_ele=I12',
         'position': 13,
         'type': {'$ref': '#/$common/I12'}}
        datatype = common.I12
        min_len = 9
        max_len = 9


class ISA_LOOP_ISA14(Element):
    """Acknowledgment Requested"""
    class Schema:
        json = {'title': 'Acknowledgment Requested',
         'usage': 'R',
         'description': 'xid=ISA14 data_ele=I13',
         'position': 14,
         'type': {'allOf': [{'$ref': '#/$common/I13'}, {'enum': ['0', '1']}]}}
        datatype = common.I13
        codes = ['0', '1']
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA15(Element):
    """Usage Indicator"""
    class Schema:
        json = {'title': 'Usage Indicator',
         'usage': 'R',
         'description': 'xid=ISA15 data_ele=I14',
         'position': 15,
         'type': {'allOf': [{'$ref': '#/$common/I14'}, {'enum': ['P', 'T']}]}}
        datatype = common.I14
        codes = ['P', 'T']
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA16(Element):
    """Component Element Separator"""
    class Schema:
        json = {'title': 'Component Element Separator',
         'usage': 'R',
         'description': 'xid=ISA16 data_ele=I15',
         'position': 16,
         'type': {'$ref': '#/$common/I15'}}
        datatype = common.I15
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA(Segment):
    """Interchange Control Header"""
    class Schema:
        json = {'title': 'Interchange Control Header',
         'usage': 'R',
         'description': 'xid=ISA name=Interchange Control Header',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'ISA'},
                        'isa01': {'$ref': '#/$elements/ISA_LOOP_ISA01'},
                        'isa02': {'$ref': '#/$elements/ISA_LOOP_ISA02'},
                        'isa03': {'$ref': '#/$elements/ISA_LOOP_ISA03'},
                        'isa04': {'$ref': '#/$elements/ISA_LOOP_ISA04'},
                        'isa05': {'$ref': '#/$elements/ISA_LOOP_ISA05'},
                        'isa06': {'$ref': '#/$elements/ISA_LOOP_ISA06'},
                        'isa07': {'$ref': '#/$elements/ISA_LOOP_ISA07'},
                        'isa08': {'$ref': '#/$elements/ISA_LOOP_ISA08'},
                        'isa09': {'$ref': '#/$elements/ISA_LOOP_ISA09'},
                        'isa10': {'$ref': '#/$elements/ISA_LOOP_ISA10'},
                        'isa11': {'$ref': '#/$elements/ISA_LOOP_ISA11'},
                        'isa12': {'$ref': '#/$elements/ISA_LOOP_ISA12'},
                        'isa13': {'$ref': '#/$elements/ISA_LOOP_ISA13'},
                        'isa14': {'$ref': '#/$elements/ISA_LOOP_ISA14'},
                        'isa15': {'$ref': '#/$elements/ISA_LOOP_ISA15'},
                        'isa16': {'$ref': '#/$elements/ISA_LOOP_ISA16'}},
         'required': ['isa01', 'isa02', 'isa03', 'isa04', 'isa05', 'isa06', 'isa07',
                      'isa08', 'isa09', 'isa10', 'isa11', 'isa12', 'isa13', 'isa14',
                      'isa15', 'isa16']}
        segment_name = 'ISA'
    isa01: ISA_LOOP_ISA01
    isa02: ISA_LOOP_ISA02
    isa03: ISA_LOOP_ISA03
    isa04: ISA_LOOP_ISA04
    isa05: ISA_LOOP_ISA05
    isa06: ISA_LOOP_ISA06
    isa07: ISA_LOOP_ISA07
    isa08: ISA_LOOP_ISA08
    isa09: ISA_LOOP_ISA09
    isa10: ISA_LOOP_ISA10
    isa11: ISA_LOOP_ISA11
    isa12: ISA_LOOP_ISA12
    isa13: ISA_LOOP_ISA13
    isa14: ISA_LOOP_ISA14
    isa15: ISA_LOOP_ISA15
    isa16: ISA_LOOP_ISA16


class GS_LOOP_GS01(Element):
    """Functional Identifier Code"""
    class Schema:
        json = {'title': 'Functional Identifier Code',
         'usage': 'R',
         'description': 'xid=GS01 data_ele=479',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/479'},
                            {'enum': ['HI', 'HC', 'BE', 'HP', 'HB', 'HS', 'RA', 'HN',
                                      'HR', 'FA']}]}}
        datatype = common.D_479
        codes = ['HI', 'HC', 'BE', 'HP', 'HB', 'HS', 'RA', 'HN', 'HR', 'FA']
        min_len = 2
        max_len = 2


class GS_LOOP_GS02(Element):
    """Application Sender's Code"""
    class Schema:
        json = {'title': "Application Sender's Code",
         'usage': 'R',
         'description': 'xid=GS02 data_ele=142',
         'position': 2,
         'type': {'$ref': '#/$common/142'}}
        datatype = common.D_142
        min_len = 2
        max_len = 15


class GS_LOOP_GS03(Element):
    """Application Receiver's Code"""
    class Schema:
        json = {'title': "Application Receiver's Code",
         'usage': 'R',
         'description': 'xid=GS03 data_ele=124',
         'position': 3,
         'type': {'$ref': '#/$common/124'}}
        datatype = common.D_124
        min_len = 2
        max_len = 15


class GS_LOOP_GS04(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'R',
         'description': 'xid=GS04 data_ele=373',
         'position': 4,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class GS_LOOP_GS05(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'R',
         'description': 'xid=GS05 data_ele=337',
         'position': 5,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class GS_LOOP_GS06(Element):
    """Group Control Number"""
    class Schema:
        json = {'title': 'Group Control Number',
         'usage': 'R',
         'description': 'xid=GS06 data_ele=28',
         'position': 6,
         'type': {'$ref': '#/$common/28'}}
        datatype = common.D_28
        min_len = 1
        max_len = 9


class GS_LOOP_GS07(Element):
    """Responsible Agency Code"""
    class Schema:
        json = {'title': 'Responsible Agency Code',
         'usage': 'R',
         'description': 'xid=GS07 data_ele=455',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/455'}, {'enum': ['X']}]}}
        datatype = common.D_455
        codes = ['X']
        min_len = 1
        max_len = 2


class GS_LOOP_GS08(Element):
    """Version / Release / Industry Identifier Code"""
    class Schema:
        json = {'title': 'Version / Release / Industry Identifier Code',
         'usage': 'R',
         'description': 'xid=GS08 data_ele=480',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/480'},
                            {'enum': ['004010', '004010X061', '004010X091',
                                      '004010X092', '004010X093', '004010X094',
                                      '004010X095', '004010X096', '004010X097',
                                      '004010X098', '004010X061A1', '004010X091A1',
                                      '004010X092A1', '004010X093A1', '004010X094A1',
                                      '004010X095A1', '004010X096A1', '004010X097A1',
                                      '004010X098A1']}]}}
        datatype = common.D_480
        codes = ['004010', '004010X061', '004010X091', '004010X092', '004010X093', '004010X094', '004010X095', '004010X096', '004010X097', '004010X098', '004010X061A1', '004010X091A1', '004010X092A1', '004010X093A1', '004010X094A1', '004010X095A1', '004010X096A1', '004010X097A1', '004010X098A1']
        min_len = 1
        max_len = 12


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    class Schema:
        json = {'title': 'Functional Group Header',
         'usage': 'R',
         'description': 'xid=GS name=Functional Group Header',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'GS'},
                        'gs01': {'$ref': '#/$elements/GS_LOOP_GS01'},
                        'gs02': {'$ref': '#/$elements/GS_LOOP_GS02'},
                        'gs03': {'$ref': '#/$elements/GS_LOOP_GS03'},
                        'gs04': {'$ref': '#/$elements/GS_LOOP_GS04'},
                        'gs05': {'$ref': '#/$elements/GS_LOOP_GS05'},
                        'gs06': {'$ref': '#/$elements/GS_LOOP_GS06'},
                        'gs07': {'$ref': '#/$elements/GS_LOOP_GS07'},
                        'gs08': {'$ref': '#/$elements/GS_LOOP_GS08'}},
         'required': ['gs01', 'gs02', 'gs03', 'gs04', 'gs05', 'gs06', 'gs07', 'gs08']}
        segment_name = 'GS'
    gs01: GS_LOOP_GS01
    gs02: GS_LOOP_GS02
    gs03: GS_LOOP_GS03
    gs04: GS_LOOP_GS04
    gs05: GS_LOOP_GS05
    gs06: GS_LOOP_GS06
    gs07: GS_LOOP_GS07
    gs08: GS_LOOP_GS08


class ST_LOOP_ST01(Element):
    """Transaction Set Identifier Code"""
    class Schema:
        json = {'title': 'Transaction Set Identifier Code',
         'usage': 'R',
         'description': 'xid=ST01 data_ele=143',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['997']}]}}
        datatype = common.D_143
        codes = ['997']
        min_len = 3
        max_len = 3


class ST_LOOP_ST02(Element):
    """Transaction Set Control Number"""
    class Schema:
        json = {'title': 'Transaction Set Control Number',
         'usage': 'R',
         'description': 'xid=ST02 data_ele=329',
         'position': 2,
         'type': {'$ref': '#/$common/329'}}
        datatype = common.D_329
        min_len = 4
        max_len = 9


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    class Schema:
        json = {'title': 'Transaction Set Header',
         'usage': 'R',
         'description': 'xid=ST name=Transaction Set Header',
         'position': 5,
         'type': 'object',
         'properties': {'xid': {'literal': 'ST'},
                        'st01': {'$ref': '#/$elements/ST_LOOP_ST01'},
                        'st02': {'$ref': '#/$elements/ST_LOOP_ST02'}},
         'required': ['st01', 'st02']}
        segment_name = 'ST'
    st01: ST_LOOP_ST01
    st02: ST_LOOP_ST02


class HEADER_AK101(Element):
    """Functional Identifier Code"""
    class Schema:
        json = {'title': 'Functional Identifier Code',
         'usage': 'R',
         'description': 'xid=AK101 data_ele=479',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/479'},
                            {'enum': ['BE', 'HB', 'HC', 'HI', 'HN', 'HP', 'HR', 'HS',
                                      'RA']}]}}
        datatype = common.D_479
        codes = ['BE', 'HB', 'HC', 'HI', 'HN', 'HP', 'HR', 'HS', 'RA']
        min_len = 2
        max_len = 2


class HEADER_AK102(Element):
    """Group Control Number"""
    class Schema:
        json = {'title': 'Group Control Number',
         'usage': 'R',
         'description': 'xid=AK102 data_ele=28',
         'position': 2,
         'type': {'$ref': '#/$common/28'}}
        datatype = common.D_28
        min_len = 1
        max_len = 9


class HEADER_AK1(Segment):
    """Functional Group Response Header"""
    class Schema:
        json = {'title': 'Functional Group Response Header',
         'usage': 'R',
         'description': 'xid=AK1 name=Functional Group Response Header',
         'position': 20,
         'type': 'object',
         'properties': {'xid': {'literal': 'AK1'},
                        'ak101': {'$ref': '#/$elements/HEADER_AK101'},
                        'ak102': {'$ref': '#/$elements/HEADER_AK102'}},
         'required': ['ak101', 'ak102']}
        segment_name = 'AK1'
    ak101: HEADER_AK101
    ak102: HEADER_AK102


class AK2_AK201(Element):
    """Transaction Set Identifier Code"""
    class Schema:
        json = {'title': 'Transaction Set Identifier Code',
         'usage': 'R',
         'description': 'xid=AK201 data_ele=143',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/143'},
                            {'enum': ['270', '271', '276', '277', '278', '820', '834',
                                      '835', '837']}]}}
        datatype = common.D_143
        codes = ['270', '271', '276', '277', '278', '820', '834', '835', '837']
        min_len = 3
        max_len = 3


class AK2_AK202(Element):
    """Transaction Set Control Number"""
    class Schema:
        json = {'title': 'Transaction Set Control Number',
         'usage': 'R',
         'description': 'xid=AK202 data_ele=329',
         'position': 2,
         'type': {'$ref': '#/$common/329'}}
        datatype = common.D_329
        min_len = 4
        max_len = 9


class AK2_AK2(Segment):
    """Transaction Set Response Header"""
    class Schema:
        json = {'title': 'Transaction Set Response Header',
         'usage': 'R',
         'description': 'xid=AK2 name=Transaction Set Response Header',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'AK2'},
                        'ak201': {'$ref': '#/$elements/AK2_AK201'},
                        'ak202': {'$ref': '#/$elements/AK2_AK202'}},
         'required': ['ak201', 'ak202']}
        segment_name = 'AK2'
    ak201: AK2_AK201
    ak202: AK2_AK202


class AK3_AK301(Element):
    """Segment ID Code"""
    class Schema:
        json = {'title': 'Segment ID Code',
         'usage': 'R',
         'description': 'xid=AK301 data_ele=721',
         'position': 1,
         'type': {'$ref': '#/$common/721'}}
        datatype = common.D_721
        min_len = 2
        max_len = 3


class AK3_AK302(Element):
    """Segment Position in Transaction Set"""
    class Schema:
        json = {'title': 'Segment Position in Transaction Set',
         'usage': 'R',
         'description': 'xid=AK302 data_ele=719',
         'position': 2,
         'type': {'$ref': '#/$common/719'}}
        datatype = common.D_719
        min_len = 1
        max_len = 6


class AK3_AK303(Element):
    """Loop Identifier Code"""
    class Schema:
        json = {'title': 'Loop Identifier Code',
         'usage': 'S',
         'description': 'xid=AK303 data_ele=447',
         'position': 3,
         'type': {'$ref': '#/$common/447'}}
        datatype = common.D_447
        min_len = 1
        max_len = 4


class AK3_AK304(Element):
    """Segment Syntax Error Code"""
    class Schema:
        json = {'title': 'Segment Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK304 data_ele=720',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/720'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8']}]}}
        datatype = common.D_720
        codes = ['1', '2', '3', '4', '5', '6', '7', '8']
        min_len = 1
        max_len = 3


class AK3_AK3(Segment):
    """Data Segment Note"""
    class Schema:
        json = {'title': 'Data Segment Note',
         'usage': 'R',
         'description': 'xid=AK3 name=Data Segment Note',
         'position': 40,
         'type': 'object',
         'properties': {'xid': {'literal': 'AK3'},
                        'ak301': {'$ref': '#/$elements/AK3_AK301'},
                        'ak302': {'$ref': '#/$elements/AK3_AK302'},
                        'ak303': {'$ref': '#/$elements/AK3_AK303'},
                        'ak304': {'$ref': '#/$elements/AK3_AK304'}},
         'required': ['ak301', 'ak302']}
        segment_name = 'AK3'
    ak301: AK3_AK301
    ak302: AK3_AK302
    ak303: AK3_AK303 | None
    ak304: AK3_AK304 | None


class AK3_AK401_01(Element):
    """Element Position in Segment"""
    class Schema:
        json = {'title': 'Element Position in Segment',
         'usage': 'R',
         'description': 'xid=AK401-01 data_ele=722',
         'position': 1,
         'type': {'$ref': '#/$common/722'}}
        datatype = common.D_722
        min_len = 1
        max_len = 2


class AK3_AK401_02(Element):
    """Component Data Element Position in Composite"""
    class Schema:
        json = {'title': 'Component Data Element Position in Composite',
         'usage': 'S',
         'description': 'xid=AK401-02 data_ele=1528',
         'position': 2,
         'type': {'$ref': '#/$common/1528'}}
        datatype = common.D_1528
        min_len = 1
        max_len = 2


class AK3_C030(Composite):
    class Schema:
        json = {'title': 'Position in Segment',
         'usage': 'R',
         'description': 'xid=None name=Position in Segment refdes= data_ele=C030',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'ak401_01': {'title': 'Element Position in Segment',
                                     'usage': 'R',
                                     'description': 'xid=AK401-01 data_ele=722',
                                     'position': 1,
                                     'type': {'$ref': '#/$common/722'}},
                        'ak401_02': {'title': 'Component Data Element Position in '
                                              'Composite',
                                     'usage': 'S',
                                     'description': 'xid=AK401-02 data_ele=1528',
                                     'position': 2,
                                     'type': {'$ref': '#/$common/1528'}}},
         'required': ['ak401_01']}
    ak401_01: AK3_AK401_01
    ak401_02: AK3_AK401_02 | None


class AK3_AK402(Element):
    """Data Element Reference Number"""
    class Schema:
        json = {'title': 'Data Element Reference Number',
         'usage': 'S',
         'description': 'xid=AK402 data_ele=725',
         'position': 2,
         'type': {'$ref': '#/$common/725'}}
        datatype = common.D_725
        min_len = 1
        max_len = 4


class AK3_AK403(Element):
    """Data Element Syntax Error Code"""
    class Schema:
        json = {'title': 'Data Element Syntax Error Code',
         'usage': 'R',
         'description': 'xid=AK403 data_ele=723',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/723'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                      '10']}]}}
        datatype = common.D_723
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        min_len = 1
        max_len = 3


class AK3_AK404(Element):
    """Copy of Bad Data Element"""
    class Schema:
        json = {'title': 'Copy of Bad Data Element',
         'usage': 'S',
         'description': 'xid=AK404 data_ele=724',
         'position': 4,
         'type': {'$ref': '#/$common/724'}}
        datatype = common.D_724
        min_len = 1
        max_len = 99


class AK3_AK4(Segment):
    """Data Element Note"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Data Element Note',
                   'usage': 'S',
                   'description': 'xid=AK4 name=Data Element Note',
                   'position': 50,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AK4'},
                                  'c030': {'$ref': '#/$elements/AK3_C030'},
                                  'ak402': {'$ref': '#/$elements/AK3_AK402'},
                                  'ak403': {'$ref': '#/$elements/AK3_AK403'},
                                  'ak404': {'$ref': '#/$elements/AK3_AK404'}},
                   'required': ['c030', 'ak403']},
         'maxItems': 99}
        segment_name = 'AK4'
    c030: AK3_C030
    ak402: AK3_AK402 | None
    ak403: AK3_AK403
    ak404: AK3_AK404 | None


class AK3(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Data Segment Note',
                   'usage': 'S',
                   'description': 'xid=AK3 name=Data Segment Note type=None',
                   'position': 40,
                   'type': 'object',
                   'properties': {'ak3': {'$ref': '#/$segments/AK3_AK3'},
                                  'ak4': {'$ref': '#/$segments/AK3_AK4'}},
                   'required': ['ak3']},
         'maxItems': 999999}
    ak3: AK3_AK3
    ak4: list[AK3_AK4] | None


class AK2_AK501(Element):
    """Transaction Set Acknowledgment Code"""
    class Schema:
        json = {'title': 'Transaction Set Acknowledgment Code',
         'usage': 'R',
         'description': 'xid=AK501 data_ele=717',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/717'},
                            {'enum': ['A', 'E', 'M', 'R', 'W', 'X']}]}}
        datatype = common.D_717
        codes = ['A', 'E', 'M', 'R', 'W', 'X']
        min_len = 1
        max_len = 1


class AK2_AK502(Element):
    """Transaction Set Syntax Error Code"""
    class Schema:
        json = {'title': 'Transaction Set Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK502 data_ele=718',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/718'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '15', '16', '17', '23', '24',
                                      '25', '26', '27']}]}}
        datatype = common.D_718
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '23', '24', '25', '26', '27']
        min_len = 1
        max_len = 3


class AK2_AK503(Element):
    """Transaction Set Syntax Error Code"""
    class Schema:
        json = {'title': 'Transaction Set Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK503 data_ele=718',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/718'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '15', '16', '17', '23', '24',
                                      '25', '26', '27']}]}}
        datatype = common.D_718
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '23', '24', '25', '26', '27']
        min_len = 1
        max_len = 3


class AK2_AK504(Element):
    """Transaction Set Syntax Error Code"""
    class Schema:
        json = {'title': 'Transaction Set Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK504 data_ele=718',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/718'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '15', '16', '17', '23', '24',
                                      '25', '26', '27']}]}}
        datatype = common.D_718
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '23', '24', '25', '26', '27']
        min_len = 1
        max_len = 3


class AK2_AK505(Element):
    """Transaction Set Syntax Error Code"""
    class Schema:
        json = {'title': 'Transaction Set Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK505 data_ele=718',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/718'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '15', '16', '17', '23', '24',
                                      '25', '26', '27']}]}}
        datatype = common.D_718
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '23', '24', '25', '26', '27']
        min_len = 1
        max_len = 3


class AK2_AK506(Element):
    """Transaction Set Syntax Error Code"""
    class Schema:
        json = {'title': 'Transaction Set Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK506 data_ele=718',
         'position': 6,
         'type': {'allOf': [{'$ref': '#/$common/718'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '15', '16', '17', '23', '24',
                                      '25', '26', '27']}]}}
        datatype = common.D_718
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '23', '24', '25', '26', '27']
        min_len = 1
        max_len = 3


class AK2_AK5(Segment):
    """Transaction Set Response Trailer"""
    class Schema:
        json = {'title': 'Transaction Set Response Trailer',
         'usage': 'R',
         'description': 'xid=AK5 name=Transaction Set Response Trailer',
         'position': 60,
         'type': 'object',
         'properties': {'xid': {'literal': 'AK5'},
                        'ak501': {'$ref': '#/$elements/AK2_AK501'},
                        'ak502': {'$ref': '#/$elements/AK2_AK502'},
                        'ak503': {'$ref': '#/$elements/AK2_AK503'},
                        'ak504': {'$ref': '#/$elements/AK2_AK504'},
                        'ak505': {'$ref': '#/$elements/AK2_AK505'},
                        'ak506': {'$ref': '#/$elements/AK2_AK506'}},
         'required': ['ak501']}
        segment_name = 'AK5'
    ak501: AK2_AK501
    ak502: AK2_AK502 | None
    ak503: AK2_AK503 | None
    ak504: AK2_AK504 | None
    ak505: AK2_AK505 | None
    ak506: AK2_AK506 | None


class AK2(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Transaction Set Response Header',
                   'usage': 'S',
                   'description': 'xid=AK2 name=Transaction Set Response Header '
                                  'type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'ak2': {'$ref': '#/$segments/AK2_AK2'},
                                  'ak3': {'$ref': '#/$segments/AK3'},
                                  'ak5': {'$ref': '#/$segments/AK2_AK5'}},
                   'required': ['ak2', 'ak5']},
         'maxItems': 999999}
    ak2: AK2_AK2
    ak3: list[AK3] | None
    ak5: AK2_AK5


class HEADER_AK901(Element):
    """Functional Group Acknowledge Code"""
    class Schema:
        json = {'title': 'Functional Group Acknowledge Code',
         'usage': 'R',
         'description': 'xid=AK901 data_ele=715',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/715'},
                            {'enum': ['A', 'E', 'M', 'P', 'R', 'W', 'X']}]}}
        datatype = common.D_715
        codes = ['A', 'E', 'M', 'P', 'R', 'W', 'X']
        min_len = 1
        max_len = 1


class HEADER_AK902(Element):
    """Number of Transaction Sets Included"""
    class Schema:
        json = {'title': 'Number of Transaction Sets Included',
         'usage': 'R',
         'description': 'xid=AK902 data_ele=97',
         'position': 2,
         'type': {'$ref': '#/$common/97'}}
        datatype = common.D_97
        min_len = 1
        max_len = 6


class HEADER_AK903(Element):
    """Number of Received Transaction Sets"""
    class Schema:
        json = {'title': 'Number of Received Transaction Sets',
         'usage': 'R',
         'description': 'xid=AK903 data_ele=123',
         'position': 3,
         'type': {'$ref': '#/$common/123'}}
        datatype = common.D_123
        min_len = 1
        max_len = 6


class HEADER_AK904(Element):
    """Number of Accepted Transaction Sets"""
    class Schema:
        json = {'title': 'Number of Accepted Transaction Sets',
         'usage': 'R',
         'description': 'xid=AK904 data_ele=2',
         'position': 4,
         'type': {'$ref': '#/$common/2'}}
        datatype = common.D_2
        min_len = 1
        max_len = 6


class HEADER_AK905(Element):
    """Functional Group Syntax Error Code"""
    class Schema:
        json = {'title': 'Functional Group Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK905 data_ele=716',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/716'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '10', '11', '12',
                                      '13', '14', '15', '16', '17', '18', '23', '24',
                                      '25', '26']}]}}
        datatype = common.D_716
        codes = ['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '23', '24', '25', '26']
        min_len = 1
        max_len = 3


class HEADER_AK906(Element):
    """Functional Group Syntax Error Code"""
    class Schema:
        json = {'title': 'Functional Group Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK906 data_ele=716',
         'position': 6,
         'type': {'allOf': [{'$ref': '#/$common/716'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '10', '11', '12',
                                      '13', '14', '15', '16', '17', '18', '23', '24',
                                      '25', '26']}]}}
        datatype = common.D_716
        codes = ['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '23', '24', '25', '26']
        min_len = 1
        max_len = 3


class HEADER_AK907(Element):
    """Functional Group Syntax Error Code"""
    class Schema:
        json = {'title': 'Functional Group Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK907 data_ele=716',
         'position': 7,
         'type': {'allOf': [{'$ref': '#/$common/716'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '10', '11', '12',
                                      '13', '14', '15', '16', '17', '18', '23', '24',
                                      '25', '26']}]}}
        datatype = common.D_716
        codes = ['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '23', '24', '25', '26']
        min_len = 1
        max_len = 3


class HEADER_AK908(Element):
    """Functional Group Syntax Error Code"""
    class Schema:
        json = {'title': 'Functional Group Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK908 data_ele=716',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/716'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '10', '11', '12',
                                      '13', '14', '15', '16', '17', '18', '23', '24',
                                      '25', '26']}]}}
        datatype = common.D_716
        codes = ['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '23', '24', '25', '26']
        min_len = 1
        max_len = 3


class HEADER_AK909(Element):
    """Functional Group Syntax Error Code"""
    class Schema:
        json = {'title': 'Functional Group Syntax Error Code',
         'usage': 'S',
         'description': 'xid=AK909 data_ele=716',
         'position': 9,
         'type': {'allOf': [{'$ref': '#/$common/716'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '10', '11', '12',
                                      '13', '14', '15', '16', '17', '18', '23', '24',
                                      '25', '26']}]}}
        datatype = common.D_716
        codes = ['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '23', '24', '25', '26']
        min_len = 1
        max_len = 3


class HEADER_AK9(Segment):
    """Functional Group Response Trailer"""
    class Schema:
        json = {'title': 'Functional Group Response Trailer',
         'usage': 'R',
         'description': 'xid=AK9 name=Functional Group Response Trailer',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'AK9'},
                        'ak901': {'$ref': '#/$elements/HEADER_AK901'},
                        'ak902': {'$ref': '#/$elements/HEADER_AK902'},
                        'ak903': {'$ref': '#/$elements/HEADER_AK903'},
                        'ak904': {'$ref': '#/$elements/HEADER_AK904'},
                        'ak905': {'$ref': '#/$elements/HEADER_AK905'},
                        'ak906': {'$ref': '#/$elements/HEADER_AK906'},
                        'ak907': {'$ref': '#/$elements/HEADER_AK907'},
                        'ak908': {'$ref': '#/$elements/HEADER_AK908'},
                        'ak909': {'$ref': '#/$elements/HEADER_AK909'}},
         'required': ['ak901', 'ak902', 'ak903', 'ak904']}
        segment_name = 'AK9'
    ak901: HEADER_AK901
    ak902: HEADER_AK902
    ak903: HEADER_AK903
    ak904: HEADER_AK904
    ak905: HEADER_AK905 | None
    ak906: HEADER_AK906 | None
    ak907: HEADER_AK907 | None
    ak908: HEADER_AK908 | None
    ak909: HEADER_AK909 | None


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 1 - Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Table 1 - Header type=wrapper',
                   'position': 10,
                   'type': 'object',
                   'properties': {'ak1': {'$ref': '#/$segments/HEADER_AK1'},
                                  'ak2': {'$ref': '#/$segments/AK2'},
                                  'ak9': {'$ref': '#/$segments/HEADER_AK9'}},
                   'required': ['ak1', 'ak9']},
         'maxItems': 1}
    ak1: HEADER_AK1
    ak2: list[AK2] | None
    ak9: HEADER_AK9


class DETAIL(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 2 - Detail',
                   'usage': 'N',
                   'description': 'xid=DETAIL name=Table 2 - Detail type=wrapper',
                   'position': 20}}


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 3 - Footer',
                   'usage': 'N',
                   'description': 'xid=FOOTER name=Table 3 - Footer type=wrapper',
                   'position': 30},
         'maxItems': 1}


class ST_LOOP_SE01(Element):
    """Number of Included Segments"""
    class Schema:
        json = {'title': 'Number of Included Segments',
         'usage': 'R',
         'description': 'xid=SE01 data_ele=96',
         'position': 1,
         'type': {'$ref': '#/$common/96'}}
        datatype = common.D_96
        min_len = 1
        max_len = 10


class ST_LOOP_SE02(Element):
    """Transaction Set Control Number"""
    class Schema:
        json = {'title': 'Transaction Set Control Number',
         'usage': 'R',
         'description': 'xid=SE02 data_ele=329',
         'position': 2,
         'type': {'$ref': '#/$common/329'}}
        datatype = common.D_329
        min_len = 4
        max_len = 9


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    class Schema:
        json = {'title': 'Transaction Set Trailer',
         'usage': 'R',
         'description': 'xid=SE name=Transaction Set Trailer',
         'position': 80,
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
         'items': {'title': 'Transaction Set Header',
                   'usage': 'R',
                   'description': 'xid=ST_LOOP name=Transaction Set Header '
                                  'type=explicit',
                   'position': 20,
                   'type': 'object',
                   'properties': {'st': {'$ref': '#/$segments/ST_LOOP_ST'},
                                  'header': {'$ref': '#/$segments/HEADER'},
                                  'detail': {'$ref': '#/$segments/DETAIL'},
                                  'footer': {'$ref': '#/$segments/FOOTER'},
                                  'se': {'$ref': '#/$segments/ST_LOOP_SE'}},
                   'required': ['st', 'header', 'se']}}
    st: ST_LOOP_ST
    header: list[HEADER]
    detail: list[DETAIL] | None
    footer: list[FOOTER] | None
    se: ST_LOOP_SE


class GS_LOOP_GE01(Element):
    """Number of Transaction Sets Included"""
    class Schema:
        json = {'title': 'Number of Transaction Sets Included',
         'usage': 'R',
         'description': 'xid=GE01 data_ele=97',
         'position': 1,
         'type': {'$ref': '#/$common/97'}}
        datatype = common.D_97
        min_len = 1
        max_len = 6


class GS_LOOP_GE02(Element):
    """Group Control Number"""
    class Schema:
        json = {'title': 'Group Control Number',
         'usage': 'R',
         'description': 'xid=GE02 data_ele=28',
         'position': 2,
         'type': {'$ref': '#/$common/28'}}
        datatype = common.D_28
        min_len = 1
        max_len = 9


class GS_LOOP_GE(Segment):
    """Functional Group Trailer"""
    class Schema:
        json = {'title': 'Functional Group Trailer',
         'usage': 'R',
         'description': 'xid=GE name=Functional Group Trailer',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'GE'},
                        'ge01': {'$ref': '#/$elements/GS_LOOP_GE01'},
                        'ge02': {'$ref': '#/$elements/GS_LOOP_GE02'}},
         'required': ['ge01', 'ge02']}
        segment_name = 'GE'
    ge01: GS_LOOP_GE01
    ge02: GS_LOOP_GE02


class GS_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Functional Group Header',
                   'usage': 'R',
                   'description': 'xid=GS_LOOP name=Functional Group Header '
                                  'type=explicit',
                   'position': 20,
                   'type': 'object',
                   'properties': {'gs': {'$ref': '#/$segments/GS_LOOP_GS'},
                                  'st_loop': {'$ref': '#/$segments/ST_LOOP'},
                                  'ge': {'$ref': '#/$segments/GS_LOOP_GE'}},
                   'required': ['gs', 'st_loop', 'ge']}}
    gs: GS_LOOP_GS
    st_loop: list[ST_LOOP]
    ge: GS_LOOP_GE


class ISA_LOOP_TA101(Element):
    """Interchange Control Number"""
    class Schema:
        json = {'title': 'Interchange Control Number',
         'usage': 'R',
         'description': 'xid=TA101 data_ele=I12',
         'position': 1,
         'type': {'$ref': '#/$common/I12'}}
        datatype = common.I12
        min_len = 9
        max_len = 9


class ISA_LOOP_TA102(Element):
    """Interchange Date"""
    class Schema:
        json = {'title': 'Interchange Date',
         'usage': 'R',
         'description': 'xid=TA102 data_ele=I08',
         'position': 2,
         'type': {'$ref': '#/$common/I08'}}
        datatype = common.I08
        min_len = 6
        max_len = 6


class ISA_LOOP_TA103(Element):
    """Interchange Time"""
    class Schema:
        json = {'title': 'Interchange Time',
         'usage': 'R',
         'description': 'xid=TA103 data_ele=I09',
         'position': 3,
         'type': {'$ref': '#/$common/I09'}}
        datatype = common.I09
        min_len = 4
        max_len = 4


class ISA_LOOP_TA104(Element):
    """Interchange Acknowledgement Code"""
    class Schema:
        json = {'title': 'Interchange Acknowledgement Code',
         'usage': 'R',
         'description': 'xid=TA104 data_ele=I17',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/I17'}, {'enum': ['A', 'E', 'R']}]}}
        datatype = common.I17
        codes = ['A', 'E', 'R']
        min_len = 1
        max_len = 1


class ISA_LOOP_TA105(Element):
    """Interchange Note Code"""
    class Schema:
        json = {'title': 'Interchange Note Code',
         'usage': 'R',
         'description': 'xid=TA105 data_ele=I18',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/I18'},
                            {'enum': ['000', '001', '002', '003', '004', '005', '006',
                                      '007', '008', '009', '010', '011', '012', '013',
                                      '014', '015', '016', '017', '018', '019', '020',
                                      '021', '022', '023', '024', '025', '026', '027',
                                      '028', '029', '030', '031']}]}}
        datatype = common.I18
        codes = ['000', '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031']
        min_len = 3
        max_len = 3


class ISA_LOOP_TA1(Segment):
    """Interchange Acknowledgement"""
    class Schema:
        json = {'title': 'Interchange Acknowledgement',
         'usage': 'S',
         'description': 'xid=TA1 name=Interchange Acknowledgement',
         'position': 20,
         'type': 'object',
         'properties': {'xid': {'literal': 'TA1'},
                        'ta101': {'$ref': '#/$elements/ISA_LOOP_TA101'},
                        'ta102': {'$ref': '#/$elements/ISA_LOOP_TA102'},
                        'ta103': {'$ref': '#/$elements/ISA_LOOP_TA103'},
                        'ta104': {'$ref': '#/$elements/ISA_LOOP_TA104'},
                        'ta105': {'$ref': '#/$elements/ISA_LOOP_TA105'}},
         'required': ['ta101', 'ta102', 'ta103', 'ta104', 'ta105']}
        segment_name = 'TA1'
    ta101: ISA_LOOP_TA101
    ta102: ISA_LOOP_TA102
    ta103: ISA_LOOP_TA103
    ta104: ISA_LOOP_TA104
    ta105: ISA_LOOP_TA105


class ISA_LOOP_IEA01(Element):
    """Number of Included Functional Groups"""
    class Schema:
        json = {'title': 'Number of Included Functional Groups',
         'usage': 'R',
         'description': 'xid=IEA01 data_ele=I16',
         'position': 1,
         'type': {'$ref': '#/$common/I16'}}
        datatype = common.I16
        min_len = 1
        max_len = 5


class ISA_LOOP_IEA02(Element):
    """Interchange Control Number"""
    class Schema:
        json = {'title': 'Interchange Control Number',
         'usage': 'R',
         'description': 'xid=IEA02 data_ele=I12',
         'position': 2,
         'type': {'$ref': '#/$common/I12'}}
        datatype = common.I12
        min_len = 9
        max_len = 9


class ISA_LOOP_IEA(Segment):
    """Interchange Control Trailer"""
    class Schema:
        json = {'title': 'Interchange Control Trailer',
         'usage': 'R',
         'description': 'xid=IEA name=Interchange Control Trailer',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'IEA'},
                        'iea01': {'$ref': '#/$elements/ISA_LOOP_IEA01'},
                        'iea02': {'$ref': '#/$elements/ISA_LOOP_IEA02'}},
         'required': ['iea01', 'iea02']}
        segment_name = 'IEA'
    iea01: ISA_LOOP_IEA01
    iea02: ISA_LOOP_IEA02


class ISA_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Interchange Control Header',
                   'usage': 'R',
                   'description': 'xid=ISA_LOOP name=Interchange Control Header '
                                  'type=explicit',
                   'position': 1,
                   'type': 'object',
                   'properties': {'isa': {'$ref': '#/$segments/ISA_LOOP_ISA'},
                                  'gs_loop': {'$ref': '#/$segments/GS_LOOP'},
                                  'ta1': {'$ref': '#/$segments/ISA_LOOP_TA1'},
                                  'iea': {'$ref': '#/$segments/ISA_LOOP_IEA'}},
                   'required': ['isa', 'gs_loop', 'iea']}}
    isa: ISA_LOOP_ISA
    gs_loop: list[GS_LOOP]
    ta1: ISA_LOOP_TA1 | None
    iea: ISA_LOOP_IEA


class MSG997(Message):
    """HIPAA Functional Acknowledgment 997"""
    class Schema:
        json = {'title': 'HIPAA Functional Acknowledgment 997',
         'description': 'xid=997 name=HIPAA Functional Acknowledgment 997',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
