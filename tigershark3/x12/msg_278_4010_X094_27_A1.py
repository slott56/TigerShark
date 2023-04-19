"""
278.4010.X094.27.A1
Created 2023-03-25 09:22:28.106529
"""
from .base import *
from . import common


class ISA_LOOP_ISA01(Element):
    """Authorization Information Qualifier"""
    class Schema:
        json = {'title': 'Authorization Information Qualifier',
         'usage': 'R',
         'description': 'xid=ISA01 data_ele=I01',
         'sequence': 1,
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
         'sequence': 2,
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
         'sequence': 3,
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
         'sequence': 4,
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
         'sequence': 5,
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
         'sequence': 6,
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
         'sequence': 7,
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
         'sequence': 8,
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
         'sequence': 9,
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
         'sequence': 10,
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
         'sequence': 11,
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
         'sequence': 12,
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
         'sequence': 13,
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
         'sequence': 14,
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
         'sequence': 15,
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
         'sequence': 16,
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
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['HI']}]}}
        datatype = common.D_479
        codes = ['HI']
        min_len = 2
        max_len = 2


class GS_LOOP_GS02(Element):
    """Application Sender's Code"""
    class Schema:
        json = {'title': "Application Sender's Code",
         'usage': 'R',
         'description': 'xid=GS02 data_ele=142',
         'sequence': 2,
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
         'sequence': 3,
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
         'sequence': 4,
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
         'sequence': 5,
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
         'sequence': 6,
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
         'sequence': 7,
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
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['004010X094A1']}]}}
        datatype = common.D_480
        codes = ['004010X094A1']
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
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['278']}]}}
        datatype = common.D_143
        codes = ['278']
        min_len = 3
        max_len = 3


class ST_LOOP_ST02(Element):
    """Transaction Set Control Number"""
    class Schema:
        json = {'title': 'Transaction Set Control Number',
         'usage': 'R',
         'description': 'xid=ST02 data_ele=329',
         'sequence': 2,
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
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'ST'},
                        'st01': {'$ref': '#/$elements/ST_LOOP_ST01'},
                        'st02': {'$ref': '#/$elements/ST_LOOP_ST02'}},
         'required': ['st01', 'st02']}
        segment_name = 'ST'
    st01: ST_LOOP_ST01
    st02: ST_LOOP_ST02


class HEADER_BHT01(Element):
    """Hierarchical Structure Code"""
    class Schema:
        json = {'title': 'Hierarchical Structure Code',
         'usage': 'R',
         'description': 'xid=BHT01 data_ele=1005',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1005'}, {'enum': ['0078']}]}}
        datatype = common.D_1005
        codes = ['0078']
        min_len = 4
        max_len = 4


class HEADER_BHT02(Element):
    """Transaction Set Purpose Code"""
    class Schema:
        json = {'title': 'Transaction Set Purpose Code',
         'usage': 'R',
         'description': 'xid=BHT02 data_ele=353',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/353'}, {'enum': ['11']}]}}
        datatype = common.D_353
        codes = ['11']
        min_len = 2
        max_len = 2


class HEADER_BHT03(Element):
    """Submitter Transaction Identifier"""
    class Schema:
        json = {'title': 'Submitter Transaction Identifier',
         'usage': 'R',
         'description': 'xid=BHT03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_BHT04(Element):
    """Transaction Set Creation Date"""
    class Schema:
        json = {'title': 'Transaction Set Creation Date',
         'usage': 'R',
         'description': 'xid=BHT04 data_ele=373',
         'sequence': 4,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BHT05(Element):
    """Transaction Set Creation Time"""
    class Schema:
        json = {'title': 'Transaction Set Creation Time',
         'usage': 'R',
         'description': 'xid=BHT05 data_ele=337',
         'sequence': 5,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_BHT06(Element):
    """Transaction Type Code"""
    class Schema:
        json = {'title': 'Transaction Type Code',
         'usage': 'S',
         'description': 'xid=BHT06 data_ele=640',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/640'}, {'enum': ['18', '19', 'AT']}]}}
        datatype = common.D_640
        codes = ['18', '19', 'AT']
        min_len = 2
        max_len = 2


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    class Schema:
        json = {'title': 'Beginning of Hierarchical Transaction',
         'usage': 'R',
         'description': 'xid=BHT name=Beginning of Hierarchical Transaction',
         'position': 20,
         'type': 'object',
         'properties': {'xid': {'literal': 'BHT'},
                        'bht01': {'$ref': '#/$elements/HEADER_BHT01'},
                        'bht02': {'$ref': '#/$elements/HEADER_BHT02'},
                        'bht03': {'$ref': '#/$elements/HEADER_BHT03'},
                        'bht04': {'$ref': '#/$elements/HEADER_BHT04'},
                        'bht05': {'$ref': '#/$elements/HEADER_BHT05'},
                        'bht06': {'$ref': '#/$elements/HEADER_BHT06'}},
         'required': ['bht01', 'bht02', 'bht03', 'bht04', 'bht05']}
        segment_name = 'BHT'
    bht01: HEADER_BHT01
    bht02: HEADER_BHT02
    bht03: HEADER_BHT03
    bht04: HEADER_BHT04
    bht05: HEADER_BHT05
    bht06: HEADER_BHT06 | None


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 1 - Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Table 1 - Header type=wrapper',
                   'position': 15,
                   'type': 'object',
                   'properties': {'bht': {'$ref': '#/$segments/HEADER_BHT'}},
                   'required': ['bht']},
         'maxItems': 1}
    bht: HEADER_BHT


class L2000A_HL01(Element):
    """Hierarchical ID Number"""
    class Schema:
        json = {'title': 'Hierarchical ID Number',
         'usage': 'R',
         'description': 'xid=HL01 data_ele=628',
         'sequence': 1,
         'type': {'$ref': '#/$common/628'}}
        datatype = common.D_628
        min_len = 1
        max_len = 12


class L2000A_HL02(Element):
    """Hierarchical Parent ID Number"""
    class Schema:
        json = {'title': 'Hierarchical Parent ID Number',
         'usage': 'N',
         'description': 'xid=HL02 data_ele=734',
         'sequence': 2,
         'type': {'$ref': '#/$common/734'}}
        datatype = common.D_734
        min_len = 1
        max_len = 12


class L2000A_HL03(Element):
    """Hierarchical Level Code"""
    class Schema:
        json = {'title': 'Hierarchical Level Code',
         'usage': 'R',
         'description': 'xid=HL03 data_ele=735',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['20']}]}}
        datatype = common.D_735
        codes = ['20']
        min_len = 1
        max_len = 2


class L2000A_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'R',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['1']}]}}
        datatype = common.D_736
        codes = ['1']
        min_len = 1
        max_len = 1


class L2000A_HL(Segment):
    """Utilization Management Organization (UMO) Level"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Level',
         'usage': 'R',
         'description': 'xid=HL name=Utilization Management Organization (UMO) Level',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000A_HL01'},
                        'hl03': {'$ref': '#/$elements/L2000A_HL03'},
                        'hl04': {'$ref': '#/$elements/L2000A_HL04'}},
         'required': ['hl01', 'hl03', 'hl04']}
        segment_name = 'HL'
    hl01: L2000A_HL01
    hl03: L2000A_HL03
    hl04: L2000A_HL04


class L2000A_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000A_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2000A_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'R',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['04', '41', '42', '79']}]}}
        datatype = common.D_901
        codes = ['04', '41', '42', '79']
        min_len = 2
        max_len = 2


class L2000A_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'R',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N', 'P', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'P', 'Y']
        min_len = 1
        max_len = 1


class L2000A_AAA(Segment):
    """Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Request Validation',
                   'position': 30,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2000A_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2000A_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2000A_AAA04'}},
                   'required': ['aaa01', 'aaa03', 'aaa04']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2000A_AAA01
    aaa03: L2000A_AAA03
    aaa04: L2000A_AAA04


class L2010A_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['X3']}]}}
        datatype = common.D_98
        codes = ['X3']
        min_len = 2
        max_len = 3


class L2010A_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2010A_NM103(Element):
    """Utilization Management Organization (UMO) Last or Organization Name"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010A_NM104(Element):
    """Utilization Management Organization (UMO) First Name"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010A_NM105(Element):
    """Utilization Management Organization (UMO) Middle Name"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010A_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010A_NM107(Element):
    """Utilization Management Organization (UMO) Name Suffix"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'PI', 'XV', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'PI', 'XV', 'XX']
        min_len = 1
        max_len = 2


class L2010A_NM109(Element):
    """Utilization Management Organization (UMO) Identifier"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010A_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010A_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010A_NM1(Segment):
    """Utilization Management Organization (UMO) Name"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Utilization Management Organization (UMO) Name',
         'position': 170,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010A_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2010A_NM101
    nm102: L2010A_NM102
    nm103: L2010A_NM103 | None
    nm104: L2010A_NM104 | None
    nm105: L2010A_NM105 | None
    nm107: L2010A_NM107 | None
    nm108: L2010A_NM108
    nm109: L2010A_NM109


class L2010A_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L2010A_PER02(Element):
    """Utilization Management Organization (UMO) Contact Name"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2010A_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010A_PER04(Element):
    """Utilization Management Organization (UMO) Contact Communication Number"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Contact Communication '
                  'Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010A_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010A_PER06(Element):
    """Utilization Management Organization (UMO) Contact Communication Number"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Contact Communication '
                  'Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010A_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010A_PER08(Element):
    """Utilization Management Organization (UMO) Contact Communication Number"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Contact Communication '
                  'Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010A_PER09(Element):
    """Contact Inquiry Reference"""
    class Schema:
        json = {'title': 'Contact Inquiry Reference',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'sequence': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2010A_PER(Segment):
    """Utilization Management Organization (UMO) Contact Information"""
    class Schema:
        json = {'title': 'Utilization Management Organization (UMO) Contact Information',
         'usage': 'S',
         'description': 'xid=PER name=Utilization Management Organization (UMO) '
                        'Contact Information',
         'position': 220,
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2010A_PER01'},
                        'per02': {'$ref': '#/$elements/L2010A_PER02'},
                        'per03': {'$ref': '#/$elements/L2010A_PER03'},
                        'per04': {'$ref': '#/$elements/L2010A_PER04'},
                        'per05': {'$ref': '#/$elements/L2010A_PER05'},
                        'per06': {'$ref': '#/$elements/L2010A_PER06'},
                        'per07': {'$ref': '#/$elements/L2010A_PER07'},
                        'per08': {'$ref': '#/$elements/L2010A_PER08'}},
         'required': ['per01']}
        segment_name = 'PER'
    per01: L2010A_PER01
    per02: L2010A_PER02 | None
    per03: L2010A_PER03 | None
    per04: L2010A_PER04 | None
    per05: L2010A_PER05 | None
    per06: L2010A_PER06 | None
    per07: L2010A_PER07 | None
    per08: L2010A_PER08 | None


class L2010A_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2010A_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2010A_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['04', '41', '42', '79', '80', 'T4']}]}}
        datatype = common.D_901
        codes = ['04', '41', '42', '79', '80', 'T4']
        min_len = 2
        max_len = 2


class L2010A_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['N', 'P', 'Y']}]}}
        datatype = common.D_889
        codes = ['N', 'P', 'Y']
        min_len = 1
        max_len = 1


class L2010A_AAA(Segment):
    """Utilization Management Organization (UMO) Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Utilization Management Organization (UMO) Request '
                            'Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Utilization Management Organization '
                                  '(UMO) Request Validation',
                   'position': 230,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2010A_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2010A_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2010A_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2010A_AAA01
    aaa03: L2010A_AAA03 | None
    aaa04: L2010A_AAA04 | None


class L2010A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Utilization Management Organization (UMO) Name',
                   'usage': 'R',
                   'description': 'xid=2010A name=Utilization Management Organization '
                                  '(UMO) Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010A_NM1'},
                                  'per': {'$ref': '#/$segments/L2010A_PER'},
                                  'aaa': {'$ref': '#/$segments/L2010A_AAA'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010A_NM1
    per: L2010A_PER | None
    aaa: list[L2010A_AAA] | None


class L2000B_HL01(Element):
    """Hierarchical ID Number"""
    class Schema:
        json = {'title': 'Hierarchical ID Number',
         'usage': 'R',
         'description': 'xid=HL01 data_ele=628',
         'sequence': 1,
         'type': {'$ref': '#/$common/628'}}
        datatype = common.D_628
        min_len = 1
        max_len = 12


class L2000B_HL02(Element):
    """Hierarchical Parent ID Number"""
    class Schema:
        json = {'title': 'Hierarchical Parent ID Number',
         'usage': 'R',
         'description': 'xid=HL02 data_ele=734',
         'sequence': 2,
         'type': {'$ref': '#/$common/734'}}
        datatype = common.D_734
        min_len = 1
        max_len = 12


class L2000B_HL03(Element):
    """Hierarchical Level Code"""
    class Schema:
        json = {'title': 'Hierarchical Level Code',
         'usage': 'R',
         'description': 'xid=HL03 data_ele=735',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['21']}]}}
        datatype = common.D_735
        codes = ['21']
        min_len = 1
        max_len = 2


class L2000B_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'R',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['1']}]}}
        datatype = common.D_736
        codes = ['1']
        min_len = 1
        max_len = 1


class L2000B_HL(Segment):
    """Requester Level"""
    class Schema:
        json = {'title': 'Requester Level',
         'usage': 'R',
         'description': 'xid=HL name=Requester Level',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000B_HL01'},
                        'hl02': {'$ref': '#/$elements/L2000B_HL02'},
                        'hl03': {'$ref': '#/$elements/L2000B_HL03'},
                        'hl04': {'$ref': '#/$elements/L2000B_HL04'}},
         'required': ['hl01', 'hl02', 'hl03', 'hl04']}
        segment_name = 'HL'
    hl01: L2000B_HL01
    hl02: L2000B_HL02
    hl03: L2000B_HL03
    hl04: L2000B_HL04


class L2010B_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['1P', 'FA']}]}}
        datatype = common.D_98
        codes = ['1P', 'FA']
        min_len = 2
        max_len = 3


class L2010B_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2010B_NM103(Element):
    """Requester Last or Organization Name"""
    class Schema:
        json = {'title': 'Requester Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010B_NM104(Element):
    """Requester First Name"""
    class Schema:
        json = {'title': 'Requester First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010B_NM105(Element):
    """Requester Middle Name"""
    class Schema:
        json = {'title': 'Requester Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010B_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010B_NM107(Element):
    """Requester Name Suffix"""
    class Schema:
        json = {'title': 'Requester Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010B_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'XX']
        min_len = 1
        max_len = 2


class L2010B_NM109(Element):
    """Requester Identifier"""
    class Schema:
        json = {'title': 'Requester Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010B_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010B_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010B_NM1(Segment):
    """Requester Name"""
    class Schema:
        json = {'title': 'Requester Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Requester Name',
         'position': 170,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010B_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010B_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010B_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010B_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010B_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2010B_NM101
    nm102: L2010B_NM102
    nm103: L2010B_NM103 | None
    nm104: L2010B_NM104 | None
    nm105: L2010B_NM105 | None
    nm107: L2010B_NM107 | None
    nm108: L2010B_NM108
    nm109: L2010B_NM109


class L2010B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1G', '1J', 'CT', 'EI', 'N5', 'N7', 'SY',
                                      'ZH']}]}}
        datatype = common.D_128
        codes = ['1G', '1J', 'CT', 'EI', 'N5', 'N7', 'SY', 'ZH']
        min_len = 2
        max_len = 3


class L2010B_REF02(Element):
    """Requester Supplemental Identifier"""
    class Schema:
        json = {'title': 'Requester Supplemental Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010B_REF03(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2010B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010B_REF(Segment):
    """Requester Supplemental Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Requester Supplemental Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Requester Supplemental Identification',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 8}
        segment_name = 'REF'
    ref01: L2010B_REF01
    ref02: L2010B_REF02


class L2010B_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2010B_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2010B_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['35', '41', '43', '44', '45', '46', '47', '49',
                                      '50', '51', '79', '97']}]}}
        datatype = common.D_901
        codes = ['35', '41', '43', '44', '45', '46', '47', '49', '50', '51', '79', '97']
        min_len = 2
        max_len = 2


class L2010B_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N', 'R']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'R']
        min_len = 1
        max_len = 1


class L2010B_AAA(Segment):
    """Requester Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Requester Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Requester Request Validation',
                   'position': 230,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2010B_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2010B_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2010B_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2010B_AAA01
    aaa03: L2010B_AAA03 | None
    aaa04: L2010B_AAA04 | None


class L2010B_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'},
                            {'enum': ['AD', 'AS', 'AT', 'CO', 'CV', 'OP', 'OR', 'OT',
                                      'PC', 'PE', 'RF']}]}}
        datatype = common.D_1221
        codes = ['AD', 'AS', 'AT', 'CO', 'CV', 'OP', 'OR', 'OT', 'PC', 'PE', 'RF']
        min_len = 1
        max_len = 3


class L2010B_PRV02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=PRV02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['ZZ']}]}}
        datatype = common.D_128
        codes = ['ZZ']
        min_len = 2
        max_len = 3


class L2010B_PRV03(Element):
    """Provider Taxonomy Code"""
    class Schema:
        json = {'title': 'Provider Taxonomy Code',
         'usage': 'R',
         'description': 'xid=PRV03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010B_PRV04(Element):
    """State or Province Code"""
    class Schema:
        json = {'title': 'State or Province Code',
         'usage': 'N',
         'description': 'xid=PRV04 data_ele=156',
         'sequence': 4,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        min_len = 2
        max_len = 2


class L2010B_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2010B_PRV06(Element):
    """Provider Organization Code"""
    class Schema:
        json = {'title': 'Provider Organization Code',
         'usage': 'N',
         'description': 'xid=PRV06 data_ele=1223',
         'sequence': 6,
         'type': {'$ref': '#/$common/1223'}}
        datatype = common.D_1223
        min_len = 3
        max_len = 3


class L2010B_PRV(Segment):
    """Requester Provider Information"""
    class Schema:
        json = {'title': 'Requester Provider Information',
         'usage': 'S',
         'description': 'xid=PRV name=Requester Provider Information',
         'position': 240,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2010B_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2010B_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2010B_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2010B_PRV01
    prv02: L2010B_PRV02
    prv03: L2010B_PRV03


class L2010B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Requester Name',
                   'usage': 'R',
                   'description': 'xid=2010B name=Requester Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010B_NM1'},
                                  'ref': {'$ref': '#/$segments/L2010B_REF'},
                                  'aaa': {'$ref': '#/$segments/L2010B_AAA'},
                                  'prv': {'$ref': '#/$segments/L2010B_PRV'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010B_NM1
    ref: list[L2010B_REF] | None
    aaa: list[L2010B_AAA] | None
    prv: L2010B_PRV | None


class L2000C_HL01(Element):
    """Hierarchical ID Number"""
    class Schema:
        json = {'title': 'Hierarchical ID Number',
         'usage': 'R',
         'description': 'xid=HL01 data_ele=628',
         'sequence': 1,
         'type': {'$ref': '#/$common/628'}}
        datatype = common.D_628
        min_len = 1
        max_len = 12


class L2000C_HL02(Element):
    """Hierarchical Parent ID Number"""
    class Schema:
        json = {'title': 'Hierarchical Parent ID Number',
         'usage': 'R',
         'description': 'xid=HL02 data_ele=734',
         'sequence': 2,
         'type': {'$ref': '#/$common/734'}}
        datatype = common.D_734
        min_len = 1
        max_len = 12


class L2000C_HL03(Element):
    """Hierarchical Level Code"""
    class Schema:
        json = {'title': 'Hierarchical Level Code',
         'usage': 'R',
         'description': 'xid=HL03 data_ele=735',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['22']}]}}
        datatype = common.D_735
        codes = ['22']
        min_len = 1
        max_len = 2


class L2000C_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'R',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['1']}]}}
        datatype = common.D_736
        codes = ['1']
        min_len = 1
        max_len = 1


class L2000C_HL(Segment):
    """Subscriber Level"""
    class Schema:
        json = {'title': 'Subscriber Level',
         'usage': 'R',
         'description': 'xid=HL name=Subscriber Level',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000C_HL01'},
                        'hl02': {'$ref': '#/$elements/L2000C_HL02'},
                        'hl03': {'$ref': '#/$elements/L2000C_HL03'},
                        'hl04': {'$ref': '#/$elements/L2000C_HL04'}},
         'required': ['hl01', 'hl02', 'hl03', 'hl04']}
        segment_name = 'HL'
    hl01: L2000C_HL01
    hl02: L2000C_HL02
    hl03: L2000C_HL03
    hl04: L2000C_HL04


class L2000C_TRN01(Element):
    """Trace Type Code"""
    class Schema:
        json = {'title': 'Trace Type Code',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['1', '2']}]}}
        datatype = common.D_481
        codes = ['1', '2']
        min_len = 1
        max_len = 2


class L2000C_TRN02(Element):
    """Patient Event Tracking Number"""
    class Schema:
        json = {'title': 'Patient Event Tracking Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000C_TRN03(Element):
    """Trace Assigning Entity Number"""
    class Schema:
        json = {'title': 'Trace Assigning Entity Number',
         'usage': 'R',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class L2000C_TRN04(Element):
    """Trace Assigning Entity Additional Identifier"""
    class Schema:
        json = {'title': 'Trace Assigning Entity Additional Identifier',
         'usage': 'S',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000C_TRN(Segment):
    """Patient Event Tracking Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Patient Event Tracking Number',
                   'usage': 'S',
                   'description': 'xid=TRN name=Patient Event Tracking Number',
                   'position': 20,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'TRN'},
                                  'trn01': {'$ref': '#/$elements/L2000C_TRN01'},
                                  'trn02': {'$ref': '#/$elements/L2000C_TRN02'},
                                  'trn03': {'$ref': '#/$elements/L2000C_TRN03'},
                                  'trn04': {'$ref': '#/$elements/L2000C_TRN04'}},
                   'required': ['trn01', 'trn02', 'trn03']},
         'maxItems': 3}
        segment_name = 'TRN'
    trn01: L2000C_TRN01
    trn02: L2000C_TRN02
    trn03: L2000C_TRN03
    trn04: L2000C_TRN04 | None


class L2000C_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000C_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2000C_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'}, {'enum': ['15', '33', '56']}]}}
        datatype = common.D_901
        codes = ['15', '33', '56']
        min_len = 2
        max_len = 2


class L2000C_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N']}]}}
        datatype = common.D_889
        codes = ['C', 'N']
        min_len = 1
        max_len = 1


class L2000C_AAA(Segment):
    """Subscriber Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Subscriber Request Validation',
                   'position': 30,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2000C_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2000C_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2000C_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2000C_AAA01
    aaa03: L2000C_AAA03 | None
    aaa04: L2000C_AAA04 | None


class L2000C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['439']}]}}
        datatype = common.D_374
        codes = ['439']
        min_len = 3
        max_len = 3


class L2000C_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_DTP03(Element):
    """Accident Date"""
    class Schema:
        json = {'title': 'Accident Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_DTP(Segment):
    """Accident Date"""
    class Schema:
        json = {'title': 'Accident Date',
         'usage': 'S',
         'description': 'xid=DTP name=Accident Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000C_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000C_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000C_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000C_DTP01
    dtp02: L2000C_DTP02
    dtp03: L2000C_DTP03


class L2000C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['484']}]}}
        datatype = common.D_374
        codes = ['484']
        min_len = 3
        max_len = 3


class L2000C_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_DTP03(Element):
    """Last Menstrual Period Date"""
    class Schema:
        json = {'title': 'Last Menstrual Period Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_DTP(Segment):
    """Last Menstrual Period Date"""
    class Schema:
        json = {'title': 'Last Menstrual Period Date',
         'usage': 'S',
         'description': 'xid=DTP name=Last Menstrual Period Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000C_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000C_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000C_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000C_DTP01
    dtp02: L2000C_DTP02
    dtp03: L2000C_DTP03


class L2000C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['ABC']}]}}
        datatype = common.D_374
        codes = ['ABC']
        min_len = 3
        max_len = 3


class L2000C_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_DTP03(Element):
    """Estimated Birth Date"""
    class Schema:
        json = {'title': 'Estimated Birth Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_DTP(Segment):
    """Estimated Date of Birth"""
    class Schema:
        json = {'title': 'Estimated Date of Birth',
         'usage': 'S',
         'description': 'xid=DTP name=Estimated Date of Birth',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000C_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000C_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000C_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000C_DTP01
    dtp02: L2000C_DTP02
    dtp03: L2000C_DTP03


class L2000C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['431']}]}}
        datatype = common.D_374
        codes = ['431']
        min_len = 3
        max_len = 3


class L2000C_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_DTP03(Element):
    """Onset of Current Symptoms or Illness Date"""
    class Schema:
        json = {'title': 'Onset of Current Symptoms or Illness Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_DTP(Segment):
    """Onset of Current Symptoms or Illness Date"""
    class Schema:
        json = {'title': 'Onset of Current Symptoms or Illness Date',
         'usage': 'S',
         'description': 'xid=DTP name=Onset of Current Symptoms or Illness Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000C_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000C_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000C_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000C_DTP01
    dtp02: L2000C_DTP02
    dtp03: L2000C_DTP03


class L2000C_HI01_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI01-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['BF', 'BJ', 'BK', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'BJ', 'BK', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI01_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI01_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI01-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI01_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI01-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI01_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI01-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI01_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI01-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI01_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI01-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 1',
         'usage': 'R',
         'description': 'xid=None name=Diagnosis 1 refdes= data_ele=C022',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'hi01_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI01-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'BJ', 'BK',
                                                                 'LOI']}]}},
                        'hi01_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI01-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi01_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI01-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi01_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI01-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi01_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI01-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi01_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI01-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi01_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI01-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi01_01', 'hi01_02']}
    hi01_01: L2000C_HI01_01
    hi01_02: L2000C_HI01_02
    hi01_03: L2000C_HI01_03 | None
    hi01_04: L2000C_HI01_04 | None


class L2000C_HI02_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI02-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'BJ', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'BJ', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI02_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI02-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI02_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI02-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI02_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI02-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI02_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI02-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI02_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI02-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI02_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI02-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 2',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 2 refdes= data_ele=C022',
         'sequence': 2,
         'syntax': [],
         'type': 'object',
         'properties': {'hi02_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI02-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'BJ', 'LOI']}]}},
                        'hi02_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI02-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi02_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI02-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi02_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI02-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi02_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI02-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi02_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI02-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi02_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI02-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi02_01', 'hi02_02']}
    hi02_01: L2000C_HI02_01
    hi02_02: L2000C_HI02_02
    hi02_03: L2000C_HI02_03 | None
    hi02_04: L2000C_HI02_04 | None


class L2000C_HI03_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI03-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI03_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI03-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI03_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI03-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI03_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI03-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI03_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI03-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI03_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI03-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI03_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI03-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 3',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 3 refdes= data_ele=C022',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'hi03_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI03-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi03_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI03-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi03_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI03-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi03_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI03-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi03_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI03-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi03_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI03-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi03_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI03-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi03_01', 'hi03_02']}
    hi03_01: L2000C_HI03_01
    hi03_02: L2000C_HI03_02
    hi03_03: L2000C_HI03_03 | None
    hi03_04: L2000C_HI03_04 | None


class L2000C_HI04_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI04-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI04_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI04-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI04_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI04-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI04_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI04-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI04_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI04-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI04_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI04-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI04_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI04-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 4',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 4 refdes= data_ele=C022',
         'sequence': 4,
         'syntax': [],
         'type': 'object',
         'properties': {'hi04_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI04-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi04_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI04-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi04_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI04-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi04_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI04-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi04_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI04-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi04_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI04-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi04_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI04-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi04_01', 'hi04_02']}
    hi04_01: L2000C_HI04_01
    hi04_02: L2000C_HI04_02
    hi04_03: L2000C_HI04_03 | None
    hi04_04: L2000C_HI04_04 | None


class L2000C_HI05_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI05-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI05_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI05-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI05_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI05-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI05_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI05-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI05_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI05-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI05_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI05-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI05_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI05-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 5',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 5 refdes= data_ele=C022',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'hi05_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI05-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi05_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI05-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi05_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI05-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi05_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI05-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi05_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI05-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi05_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI05-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi05_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI05-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi05_01', 'hi05_02']}
    hi05_01: L2000C_HI05_01
    hi05_02: L2000C_HI05_02
    hi05_03: L2000C_HI05_03 | None
    hi05_04: L2000C_HI05_04 | None


class L2000C_HI06_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI06-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI06_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI06-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI06_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI06-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI06_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI06-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI06_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI06-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI06_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI06-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI06_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI06-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 6',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 6 refdes= data_ele=C022',
         'sequence': 6,
         'syntax': [],
         'type': 'object',
         'properties': {'hi06_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI06-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi06_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI06-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi06_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI06-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi06_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI06-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi06_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI06-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi06_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI06-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi06_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI06-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi06_01', 'hi06_02']}
    hi06_01: L2000C_HI06_01
    hi06_02: L2000C_HI06_02
    hi06_03: L2000C_HI06_03 | None
    hi06_04: L2000C_HI06_04 | None


class L2000C_HI07_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI07-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI07_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI07-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI07_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI07-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI07_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI07-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI07_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI07-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI07_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI07-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI07_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI07-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 7',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 7 refdes= data_ele=C022',
         'sequence': 7,
         'syntax': [],
         'type': 'object',
         'properties': {'hi07_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI07-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi07_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI07-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi07_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI07-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi07_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI07-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi07_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI07-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi07_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI07-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi07_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI07-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi07_01', 'hi07_02']}
    hi07_01: L2000C_HI07_01
    hi07_02: L2000C_HI07_02
    hi07_03: L2000C_HI07_03 | None
    hi07_04: L2000C_HI07_04 | None


class L2000C_HI08_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI08-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI08_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI08-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI08_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI08-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI08_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI08-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI08_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI08-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI08_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI08-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI08_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI08-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 8',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 8 refdes= data_ele=C022',
         'sequence': 8,
         'syntax': [],
         'type': 'object',
         'properties': {'hi08_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI08-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi08_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI08-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi08_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI08-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi08_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI08-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi08_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI08-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi08_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI08-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi08_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI08-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi08_01', 'hi08_02']}
    hi08_01: L2000C_HI08_01
    hi08_02: L2000C_HI08_02
    hi08_03: L2000C_HI08_03 | None
    hi08_04: L2000C_HI08_04 | None


class L2000C_HI09_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI09-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI09_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI09-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI09_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI09-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI09_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI09-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI09_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI09-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI09_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI09-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI09_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI09-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 9',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 9 refdes= data_ele=C022',
         'sequence': 9,
         'syntax': [],
         'type': 'object',
         'properties': {'hi09_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI09-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi09_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI09-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi09_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI09-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi09_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI09-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi09_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI09-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi09_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI09-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi09_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI09-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi09_01', 'hi09_02']}
    hi09_01: L2000C_HI09_01
    hi09_02: L2000C_HI09_02
    hi09_03: L2000C_HI09_03 | None
    hi09_04: L2000C_HI09_04 | None


class L2000C_HI10_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI10-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI10_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI10_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI10-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI10_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI10-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI10_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI10-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI10_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI10-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI10_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI10-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 10',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 10 refdes= data_ele=C022',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'hi10_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI10-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi10_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI10-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi10_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI10-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi10_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI10-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi10_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI10-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi10_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI10-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi10_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI10-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi10_01', 'hi10_02']}
    hi10_01: L2000C_HI10_01
    hi10_02: L2000C_HI10_02
    hi10_03: L2000C_HI10_03 | None
    hi10_04: L2000C_HI10_04 | None


class L2000C_HI11_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI11-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI11_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI11_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI11-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI11_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI11-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI11_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI11-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI11_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI11-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI11_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI11-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 11',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 11 refdes= data_ele=C022',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'hi11_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI11-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi11_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI11-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi11_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI11-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi11_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI11-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi11_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI11-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi11_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI11-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi11_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI11-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi11_01', 'hi11_02']}
    hi11_01: L2000C_HI11_01
    hi11_02: L2000C_HI11_02
    hi11_03: L2000C_HI11_03 | None
    hi11_04: L2000C_HI11_04 | None


class L2000C_HI12_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI12-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000C_HI12_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI12-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000C_HI12_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI12-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000C_HI12_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI12-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_HI12_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI12-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000C_HI12_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI12-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000C_HI12_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI12-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000C_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 12',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 12 refdes= data_ele=C022',
         'sequence': 12,
         'syntax': [],
         'type': 'object',
         'properties': {'hi12_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI12-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi12_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI12-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi12_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI12-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi12_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI12-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi12_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI12-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi12_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI12-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi12_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI12-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi12_01', 'hi12_02']}
    hi12_01: L2000C_HI12_01
    hi12_02: L2000C_HI12_02
    hi12_03: L2000C_HI12_03 | None
    hi12_04: L2000C_HI12_04 | None


class L2000C_HI(Segment):
    """Subscriber Diagnosis"""
    class Schema:
        json = {'title': 'Subscriber Diagnosis',
         'usage': 'S',
         'description': 'xid=HI name=Subscriber Diagnosis',
         'position': 80,
         'type': 'object',
         'properties': {'xid': {'literal': 'HI'},
                        'c022': {'$ref': '#/$elements/L2000C_C022'}},
         'required': ['c022']}
        segment_name = 'HI'
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022
    c022: L2000C_C022


class L2000C_PWK01(Element):
    """Attachment Report Type Code"""
    class Schema:
        json = {'title': 'Attachment Report Type Code',
         'usage': 'R',
         'description': 'xid=PWK01 data_ele=755',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/755'},
                            {'enum': ['03', '04', '05', '06', '07', '08', '09', '10',
                                      '11', '13', '15', '21', '48', '55', '59', '77',
                                      'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR',
                                      'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG',
                                      'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA',
                                      'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4',
                                      'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY',
                                      'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG',
                                      'V5', 'XP']}]}}
        datatype = common.D_755
        codes = ['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', '48', '55', '59', '77', 'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR', 'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4', 'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP']
        min_len = 2
        max_len = 2


class L2000C_PWK02(Element):
    """Attachment Transmission Code"""
    class Schema:
        json = {'title': 'Attachment Transmission Code',
         'usage': 'R',
         'description': 'xid=PWK02 data_ele=756',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/756'},
                            {'enum': ['BM', 'EL', 'EM', 'FX', 'VO']}]}}
        datatype = common.D_756
        codes = ['BM', 'EL', 'EM', 'FX', 'VO']
        min_len = 1
        max_len = 2


class L2000C_PWK03(Element):
    """Report Copies Needed"""
    class Schema:
        json = {'title': 'Report Copies Needed',
         'usage': 'N',
         'description': 'xid=PWK03 data_ele=757',
         'sequence': 3,
         'type': {'$ref': '#/$common/757'}}
        datatype = common.D_757
        min_len = 1
        max_len = 2


class L2000C_PWK04(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=PWK04 data_ele=98',
         'sequence': 4,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2000C_PWK05(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=PWK05 data_ele=66',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['AC']}]}}
        datatype = common.D_66
        codes = ['AC']
        min_len = 1
        max_len = 2


class L2000C_PWK06(Element):
    """Attachment Control Number"""
    class Schema:
        json = {'title': 'Attachment Control Number',
         'usage': 'S',
         'description': 'xid=PWK06 data_ele=67',
         'sequence': 6,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2000C_PWK07(Element):
    """Attachment Description"""
    class Schema:
        json = {'title': 'Attachment Description',
         'usage': 'S',
         'description': 'xid=PWK07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000C_C002(Composite):
    class Schema:
        json = {'title': 'Actions Indicated',
         'usage': 'N',
         'description': 'xid=None name=Actions Indicated refdes= data_ele=C002',
         'sequence': 8,
         'syntax': []}


class L2000C_PWK09(Element):
    """Request Category Code"""
    class Schema:
        json = {'title': 'Request Category Code',
         'usage': 'N',
         'description': 'xid=PWK09 data_ele=1525',
         'sequence': 9,
         'type': {'$ref': '#/$common/1525'}}
        datatype = common.D_1525
        min_len = 1
        max_len = 2


class L2000C_PWK(Segment):
    """Additional Patient Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Patient Information',
                   'usage': 'S',
                   'description': 'xid=PWK name=Additional Patient Information',
                   'position': 155,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PWK'},
                                  'pwk01': {'$ref': '#/$elements/L2000C_PWK01'},
                                  'pwk02': {'$ref': '#/$elements/L2000C_PWK02'},
                                  'pwk05': {'$ref': '#/$elements/L2000C_PWK05'},
                                  'pwk06': {'$ref': '#/$elements/L2000C_PWK06'},
                                  'pwk07': {'$ref': '#/$elements/L2000C_PWK07'}},
                   'required': ['pwk01', 'pwk02']},
         'maxItems': 10}
        segment_name = 'PWK'
    pwk01: L2000C_PWK01
    pwk02: L2000C_PWK02
    pwk05: L2000C_PWK05 | None
    pwk06: L2000C_PWK06 | None
    pwk07: L2000C_PWK07 | None


class L2010CA_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['IL']}]}}
        datatype = common.D_98
        codes = ['IL']
        min_len = 2
        max_len = 3


class L2010CA_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2010CA_NM103(Element):
    """Subscriber Last Name"""
    class Schema:
        json = {'title': 'Subscriber Last Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010CA_NM104(Element):
    """Subscriber First Name"""
    class Schema:
        json = {'title': 'Subscriber First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010CA_NM105(Element):
    """Subscriber Middle Name"""
    class Schema:
        json = {'title': 'Subscriber Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010CA_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010CA_NM107(Element):
    """Subscriber Name Suffix"""
    class Schema:
        json = {'title': 'Subscriber Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010CA_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['MI', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['MI', 'ZZ']
        min_len = 1
        max_len = 2


class L2010CA_NM109(Element):
    """Subscriber Primary Identifier"""
    class Schema:
        json = {'title': 'Subscriber Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010CA_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010CA_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010CA_NM1(Segment):
    """Subscriber Name"""
    class Schema:
        json = {'title': 'Subscriber Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Subscriber Name',
         'position': 170,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010CA_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010CA_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010CA_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010CA_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010CA_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010CA_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010CA_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010CA_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2010CA_NM101
    nm102: L2010CA_NM102
    nm103: L2010CA_NM103 | None
    nm104: L2010CA_NM104 | None
    nm105: L2010CA_NM105 | None
    nm107: L2010CA_NM107 | None
    nm108: L2010CA_NM108
    nm109: L2010CA_NM109


class L2010CA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1L', '1W', '6P', 'A6', 'EJ', 'F6', 'HJ', 'IG',
                                      'N6', 'NQ', 'SY']}]}}
        datatype = common.D_128
        codes = ['1L', '1W', '6P', 'A6', 'EJ', 'F6', 'HJ', 'IG', 'N6', 'NQ', 'SY']
        min_len = 2
        max_len = 3


class L2010CA_REF02(Element):
    """Subscriber Supplemental Identifier"""
    class Schema:
        json = {'title': 'Subscriber Supplemental Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010CA_REF03(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2010CA_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010CA_REF(Segment):
    """Subscriber Supplemental Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Supplemental Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Subscriber Supplemental Identification',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010CA_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010CA_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2010CA_REF01
    ref02: L2010CA_REF02


class L2010CA_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2010CA_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2010CA_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '58', '64', '65', '66', '67', '68', '71',
                                      '72', '73', '74', '75', '76', '77', '78', '79',
                                      '95']}]}}
        datatype = common.D_901
        codes = ['15', '58', '64', '65', '66', '67', '68', '71', '72', '73', '74', '75', '76', '77', '78', '79', '95']
        min_len = 2
        max_len = 2


class L2010CA_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N']}]}}
        datatype = common.D_889
        codes = ['C', 'N']
        min_len = 1
        max_len = 1


class L2010CA_AAA(Segment):
    """Subscriber Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Subscriber Request Validation',
                   'position': 230,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2010CA_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2010CA_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2010CA_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2010CA_AAA01
    aaa03: L2010CA_AAA03 | None
    aaa04: L2010CA_AAA04 | None


class L2010CA_DMG01(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DMG01 data_ele=1250',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2010CA_DMG02(Element):
    """Subscriber Birth Date"""
    class Schema:
        json = {'title': 'Subscriber Birth Date',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2010CA_DMG03(Element):
    """Subscriber Gender Code"""
    class Schema:
        json = {'title': 'Subscriber Gender Code',
         'usage': 'S',
         'description': 'xid=DMG03 data_ele=1068',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2010CA_DMG04(Element):
    """Marital Status Code"""
    class Schema:
        json = {'title': 'Marital Status Code',
         'usage': 'N',
         'description': 'xid=DMG04 data_ele=1067',
         'sequence': 4,
         'type': {'$ref': '#/$common/1067'}}
        datatype = common.D_1067
        min_len = 1
        max_len = 1


class L2010CA_DMG05(Element):
    """Race or Ethnicity Code"""
    class Schema:
        json = {'title': 'Race or Ethnicity Code',
         'usage': 'N',
         'description': 'xid=DMG05 data_ele=1109',
         'sequence': 5,
         'type': {'$ref': '#/$common/1109'}}
        datatype = common.D_1109
        min_len = 1
        max_len = 1


class L2010CA_DMG06(Element):
    """Citizenship Status Code"""
    class Schema:
        json = {'title': 'Citizenship Status Code',
         'usage': 'N',
         'description': 'xid=DMG06 data_ele=1066',
         'sequence': 6,
         'type': {'$ref': '#/$common/1066'}}
        datatype = common.D_1066
        min_len = 1
        max_len = 2


class L2010CA_DMG07(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'N',
         'description': 'xid=DMG07 data_ele=26',
         'sequence': 7,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L2010CA_DMG08(Element):
    """Basis of Verification Code"""
    class Schema:
        json = {'title': 'Basis of Verification Code',
         'usage': 'N',
         'description': 'xid=DMG08 data_ele=659',
         'sequence': 8,
         'type': {'$ref': '#/$common/659'}}
        datatype = common.D_659
        min_len = 1
        max_len = 2


class L2010CA_DMG09(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=DMG09 data_ele=380',
         'sequence': 9,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2010CA_DMG(Segment):
    """Subscriber Demographic Information"""
    class Schema:
        json = {'title': 'Subscriber Demographic Information',
         'usage': 'S',
         'description': 'xid=DMG name=Subscriber Demographic Information',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2010CA_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2010CA_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2010CA_DMG03'}},
         'required': ['dmg01', 'dmg02']}
        segment_name = 'DMG'
    dmg01: L2010CA_DMG01
    dmg02: L2010CA_DMG02
    dmg03: L2010CA_DMG03 | None


class L2010CA(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Name',
                   'usage': 'R',
                   'description': 'xid=2010CA name=Subscriber Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010CA_NM1'},
                                  'ref': {'$ref': '#/$segments/L2010CA_REF'},
                                  'aaa': {'$ref': '#/$segments/L2010CA_AAA'},
                                  'dmg': {'$ref': '#/$segments/L2010CA_DMG'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010CA_NM1
    ref: list[L2010CA_REF] | None
    aaa: list[L2010CA_AAA] | None
    dmg: L2010CA_DMG | None


class L2010CB_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['1P', '2B', 'ABG', 'FA', 'PR', 'X3']}]}}
        datatype = common.D_98
        codes = ['1P', '2B', 'ABG', 'FA', 'PR', 'X3']
        min_len = 2
        max_len = 3


class L2010CB_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2010CB_NM103(Element):
    """Response Contact Last or Organization Name"""
    class Schema:
        json = {'title': 'Response Contact Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010CB_NM104(Element):
    """Response Contact First Name"""
    class Schema:
        json = {'title': 'Response Contact First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010CB_NM105(Element):
    """Response Contact Middle Name"""
    class Schema:
        json = {'title': 'Response Contact Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010CB_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010CB_NM107(Element):
    """Response Contact Name Suffix"""
    class Schema:
        json = {'title': 'Response Contact Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010CB_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'PI', 'XV', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'PI', 'XV', 'XX']
        min_len = 1
        max_len = 2


class L2010CB_NM109(Element):
    """Response Contact Identifier"""
    class Schema:
        json = {'title': 'Response Contact Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010CB_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010CB_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010CB_NM1(Segment):
    """Additional Patient Information Contact Name"""
    class Schema:
        json = {'title': 'Additional Patient Information Contact Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Additional Patient Information Contact Name',
         'position': 170,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010CB_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010CB_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010CB_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010CB_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010CB_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010CB_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010CB_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010CB_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2010CB_NM101
    nm102: L2010CB_NM102
    nm103: L2010CB_NM103 | None
    nm104: L2010CB_NM104 | None
    nm105: L2010CB_NM105 | None
    nm107: L2010CB_NM107 | None
    nm108: L2010CB_NM108 | None
    nm109: L2010CB_NM109 | None


class L2010CB_N301(Element):
    """Response Contact Address Line"""
    class Schema:
        json = {'title': 'Response Contact Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010CB_N302(Element):
    """Response Contact Address Line"""
    class Schema:
        json = {'title': 'Response Contact Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010CB_N3(Segment):
    """Additional Patient Information Contact Address"""
    class Schema:
        json = {'title': 'Additional Patient Information Contact Address',
         'usage': 'S',
         'description': 'xid=N3 name=Additional Patient Information Contact Address',
         'position': 200,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010CB_N301'},
                        'n302': {'$ref': '#/$elements/L2010CB_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010CB_N301
    n302: L2010CB_N302 | None


class L2010CB_N401(Element):
    """Response Contact City Name"""
    class Schema:
        json = {'title': 'Response Contact City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010CB_N402(Element):
    """Response Contact State or Province Code"""
    class Schema:
        json = {'title': 'Response Contact State or Province Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010CB_N403(Element):
    """Response Contact Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Response Contact Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010CB_N404(Element):
    """Response Contact Country Code"""
    class Schema:
        json = {'title': 'Response Contact Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010CB_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['B1', 'DP']}]}}
        datatype = common.D_309
        codes = ['B1', 'DP']
        min_len = 1
        max_len = 2


class L2010CB_N406(Element):
    """Response Contact Specific Location"""
    class Schema:
        json = {'title': 'Response Contact Specific Location',
         'usage': 'S',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2010CB_N4(Segment):
    """Additional Patient Information Contact City/State/Zip Code"""
    class Schema:
        json = {'title': 'Additional Patient Information Contact City/State/Zip Code',
         'usage': 'S',
         'description': 'xid=N4 name=Additional Patient Information Contact '
                        'City/State/Zip Code',
         'position': 210,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010CB_N401'},
                        'n402': {'$ref': '#/$elements/L2010CB_N402'},
                        'n403': {'$ref': '#/$elements/L2010CB_N403'},
                        'n404': {'$ref': '#/$elements/L2010CB_N404'},
                        'n405': {'$ref': '#/$elements/L2010CB_N405'},
                        'n406': {'$ref': '#/$elements/L2010CB_N406'}}}
        segment_name = 'N4'
    n401: L2010CB_N401 | None
    n402: L2010CB_N402 | None
    n403: L2010CB_N403 | None
    n404: L2010CB_N404 | None
    n405: L2010CB_N405 | None
    n406: L2010CB_N406 | None


class L2010CB_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L2010CB_PER02(Element):
    """Response Contact Name"""
    class Schema:
        json = {'title': 'Response Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2010CB_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010CB_PER04(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010CB_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010CB_PER06(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010CB_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010CB_PER08(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010CB_PER09(Element):
    """Contact Inquiry Reference"""
    class Schema:
        json = {'title': 'Contact Inquiry Reference',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'sequence': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2010CB_PER(Segment):
    """Additional Patient Information Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Patient Information Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Additional Patient Information Contact '
                                  'Information',
                   'position': 220,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2010CB_PER01'},
                                  'per02': {'$ref': '#/$elements/L2010CB_PER02'},
                                  'per03': {'$ref': '#/$elements/L2010CB_PER03'},
                                  'per04': {'$ref': '#/$elements/L2010CB_PER04'},
                                  'per05': {'$ref': '#/$elements/L2010CB_PER05'},
                                  'per06': {'$ref': '#/$elements/L2010CB_PER06'},
                                  'per07': {'$ref': '#/$elements/L2010CB_PER07'},
                                  'per08': {'$ref': '#/$elements/L2010CB_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2010CB_PER01
    per02: L2010CB_PER02 | None
    per03: L2010CB_PER03 | None
    per04: L2010CB_PER04 | None
    per05: L2010CB_PER05 | None
    per06: L2010CB_PER06 | None
    per07: L2010CB_PER07 | None
    per08: L2010CB_PER08 | None


class L2010CB(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Patient Information Contact Name',
                   'usage': 'S',
                   'description': 'xid=2010CB name=Additional Patient Information '
                                  'Contact Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010CB_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010CB_N3'},
                                  'n4': {'$ref': '#/$segments/L2010CB_N4'},
                                  'per': {'$ref': '#/$segments/L2010CB_PER'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010CB_NM1
    n3: L2010CB_N3 | None
    n4: L2010CB_N4 | None
    per: list[L2010CB_PER] | None


class L2000D_HL01(Element):
    """Hierarchical ID Number"""
    class Schema:
        json = {'title': 'Hierarchical ID Number',
         'usage': 'R',
         'description': 'xid=HL01 data_ele=628',
         'sequence': 1,
         'type': {'$ref': '#/$common/628'}}
        datatype = common.D_628
        min_len = 1
        max_len = 12


class L2000D_HL02(Element):
    """Hierarchical Parent ID Number"""
    class Schema:
        json = {'title': 'Hierarchical Parent ID Number',
         'usage': 'R',
         'description': 'xid=HL02 data_ele=734',
         'sequence': 2,
         'type': {'$ref': '#/$common/734'}}
        datatype = common.D_734
        min_len = 1
        max_len = 12


class L2000D_HL03(Element):
    """Hierarchical Level Code"""
    class Schema:
        json = {'title': 'Hierarchical Level Code',
         'usage': 'R',
         'description': 'xid=HL03 data_ele=735',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['23']}]}}
        datatype = common.D_735
        codes = ['23']
        min_len = 1
        max_len = 2


class L2000D_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'R',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['1']}]}}
        datatype = common.D_736
        codes = ['1']
        min_len = 1
        max_len = 1


class L2000D_HL(Segment):
    """Dependent Level"""
    class Schema:
        json = {'title': 'Dependent Level',
         'usage': 'R',
         'description': 'xid=HL name=Dependent Level',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000D_HL01'},
                        'hl02': {'$ref': '#/$elements/L2000D_HL02'},
                        'hl03': {'$ref': '#/$elements/L2000D_HL03'},
                        'hl04': {'$ref': '#/$elements/L2000D_HL04'}},
         'required': ['hl01', 'hl02', 'hl03', 'hl04']}
        segment_name = 'HL'
    hl01: L2000D_HL01
    hl02: L2000D_HL02
    hl03: L2000D_HL03
    hl04: L2000D_HL04


class L2000D_TRN01(Element):
    """Trace Type Code"""
    class Schema:
        json = {'title': 'Trace Type Code',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['1', '2']}]}}
        datatype = common.D_481
        codes = ['1', '2']
        min_len = 1
        max_len = 2


class L2000D_TRN02(Element):
    """Patient Event Tracking Number"""
    class Schema:
        json = {'title': 'Patient Event Tracking Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000D_TRN03(Element):
    """Trace Assigning Entity Number"""
    class Schema:
        json = {'title': 'Trace Assigning Entity Number',
         'usage': 'R',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class L2000D_TRN04(Element):
    """Trace Assigning Entity Additional Identifier"""
    class Schema:
        json = {'title': 'Trace Assigning Entity Additional Identifier',
         'usage': 'S',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000D_TRN(Segment):
    """Patient Event Tracking Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Patient Event Tracking Number',
                   'usage': 'S',
                   'description': 'xid=TRN name=Patient Event Tracking Number',
                   'position': 20,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'TRN'},
                                  'trn01': {'$ref': '#/$elements/L2000D_TRN01'},
                                  'trn02': {'$ref': '#/$elements/L2000D_TRN02'},
                                  'trn03': {'$ref': '#/$elements/L2000D_TRN03'},
                                  'trn04': {'$ref': '#/$elements/L2000D_TRN04'}},
                   'required': ['trn01', 'trn02', 'trn03']},
         'maxItems': 3}
        segment_name = 'TRN'
    trn01: L2000D_TRN01
    trn02: L2000D_TRN02
    trn03: L2000D_TRN03
    trn04: L2000D_TRN04 | None


class L2000D_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000D_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2000D_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'}, {'enum': ['15', '33', '56']}]}}
        datatype = common.D_901
        codes = ['15', '33', '56']
        min_len = 2
        max_len = 2


class L2000D_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N']}]}}
        datatype = common.D_889
        codes = ['C', 'N']
        min_len = 1
        max_len = 1


class L2000D_AAA(Segment):
    """Dependent Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Dependent Request Validation',
                   'position': 30,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2000D_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2000D_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2000D_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2000D_AAA01
    aaa03: L2000D_AAA03 | None
    aaa04: L2000D_AAA04 | None


class L2000D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['439']}]}}
        datatype = common.D_374
        codes = ['439']
        min_len = 3
        max_len = 3


class L2000D_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_DTP03(Element):
    """Accident Date"""
    class Schema:
        json = {'title': 'Accident Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_DTP(Segment):
    """Accident Date"""
    class Schema:
        json = {'title': 'Accident Date',
         'usage': 'S',
         'description': 'xid=DTP name=Accident Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000D_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000D_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000D_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000D_DTP01
    dtp02: L2000D_DTP02
    dtp03: L2000D_DTP03


class L2000D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['484']}]}}
        datatype = common.D_374
        codes = ['484']
        min_len = 3
        max_len = 3


class L2000D_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_DTP03(Element):
    """Last Menstrual Period Date"""
    class Schema:
        json = {'title': 'Last Menstrual Period Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_DTP(Segment):
    """Last Menstrual Period Date"""
    class Schema:
        json = {'title': 'Last Menstrual Period Date',
         'usage': 'S',
         'description': 'xid=DTP name=Last Menstrual Period Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000D_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000D_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000D_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000D_DTP01
    dtp02: L2000D_DTP02
    dtp03: L2000D_DTP03


class L2000D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['ABC']}]}}
        datatype = common.D_374
        codes = ['ABC']
        min_len = 3
        max_len = 3


class L2000D_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_DTP03(Element):
    """Estimated Birth Date"""
    class Schema:
        json = {'title': 'Estimated Birth Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_DTP(Segment):
    """Estimated Date of Birth"""
    class Schema:
        json = {'title': 'Estimated Date of Birth',
         'usage': 'S',
         'description': 'xid=DTP name=Estimated Date of Birth',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000D_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000D_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000D_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000D_DTP01
    dtp02: L2000D_DTP02
    dtp03: L2000D_DTP03


class L2000D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['431']}]}}
        datatype = common.D_374
        codes = ['431']
        min_len = 3
        max_len = 3


class L2000D_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_DTP03(Element):
    """Onset of Current Symptoms or Illness Date"""
    class Schema:
        json = {'title': 'Onset of Current Symptoms or Illness Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_DTP(Segment):
    """Onset of Current Symptoms or Illness Date"""
    class Schema:
        json = {'title': 'Onset of Current Symptoms or Illness Date',
         'usage': 'S',
         'description': 'xid=DTP name=Onset of Current Symptoms or Illness Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000D_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000D_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000D_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000D_DTP01
    dtp02: L2000D_DTP02
    dtp03: L2000D_DTP03


class L2000D_HI01_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI01-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['BF', 'BJ', 'BK', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'BJ', 'BK', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI01_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI01_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI01-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI01_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI01-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI01_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI01-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI01_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI01-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI01_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI01-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 1',
         'usage': 'R',
         'description': 'xid=None name=Diagnosis 1 refdes= data_ele=C022',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'hi01_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI01-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'BJ', 'BK',
                                                                 'LOI']}]}},
                        'hi01_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI01-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi01_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI01-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi01_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI01-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi01_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI01-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi01_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI01-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi01_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI01-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi01_01', 'hi01_02']}
    hi01_01: L2000D_HI01_01
    hi01_02: L2000D_HI01_02
    hi01_03: L2000D_HI01_03 | None
    hi01_04: L2000D_HI01_04 | None


class L2000D_HI02_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI02-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'BJ', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'BJ', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI02_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI02-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI02_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI02-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI02_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI02-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI02_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI02-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI02_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI02-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI02_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI02-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 2',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 2 refdes= data_ele=C022',
         'sequence': 2,
         'syntax': [],
         'type': 'object',
         'properties': {'hi02_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI02-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'BJ', 'LOI']}]}},
                        'hi02_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI02-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi02_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI02-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi02_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI02-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi02_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI02-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi02_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI02-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi02_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI02-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi02_01', 'hi02_02']}
    hi02_01: L2000D_HI02_01
    hi02_02: L2000D_HI02_02
    hi02_03: L2000D_HI02_03 | None
    hi02_04: L2000D_HI02_04 | None


class L2000D_HI03_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI03-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI03_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI03-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI03_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI03-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI03_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI03-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI03_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI03-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI03_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI03-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI03_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI03-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 3',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 3 refdes= data_ele=C022',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'hi03_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI03-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi03_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI03-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi03_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI03-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi03_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI03-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi03_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI03-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi03_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI03-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi03_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI03-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi03_01', 'hi03_02']}
    hi03_01: L2000D_HI03_01
    hi03_02: L2000D_HI03_02
    hi03_03: L2000D_HI03_03 | None
    hi03_04: L2000D_HI03_04 | None


class L2000D_HI04_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI04-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI04_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI04-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI04_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI04-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI04_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI04-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI04_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI04-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI04_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI04-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI04_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI04-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 4',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 4 refdes= data_ele=C022',
         'sequence': 4,
         'syntax': [],
         'type': 'object',
         'properties': {'hi04_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI04-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi04_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI04-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi04_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI04-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi04_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI04-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi04_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI04-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi04_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI04-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi04_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI04-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi04_01', 'hi04_02']}
    hi04_01: L2000D_HI04_01
    hi04_02: L2000D_HI04_02
    hi04_03: L2000D_HI04_03 | None
    hi04_04: L2000D_HI04_04 | None


class L2000D_HI05_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI05-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI05_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI05-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI05_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI05-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI05_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI05-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI05_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI05-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI05_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI05-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI05_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI05-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 5',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 5 refdes= data_ele=C022',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'hi05_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI05-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi05_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI05-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi05_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI05-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi05_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI05-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi05_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI05-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi05_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI05-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi05_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI05-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi05_01', 'hi05_02']}
    hi05_01: L2000D_HI05_01
    hi05_02: L2000D_HI05_02
    hi05_03: L2000D_HI05_03 | None
    hi05_04: L2000D_HI05_04 | None


class L2000D_HI06_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI06-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI06_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI06-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI06_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI06-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI06_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI06-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI06_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI06-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI06_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI06-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI06_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI06-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 6',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 6 refdes= data_ele=C022',
         'sequence': 6,
         'syntax': [],
         'type': 'object',
         'properties': {'hi06_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI06-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi06_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI06-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi06_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI06-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi06_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI06-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi06_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI06-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi06_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI06-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi06_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI06-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi06_01', 'hi06_02']}
    hi06_01: L2000D_HI06_01
    hi06_02: L2000D_HI06_02
    hi06_03: L2000D_HI06_03 | None
    hi06_04: L2000D_HI06_04 | None


class L2000D_HI07_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI07-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI07_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI07-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI07_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI07-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI07_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI07-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI07_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI07-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI07_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI07-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI07_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI07-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 7',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 7 refdes= data_ele=C022',
         'sequence': 7,
         'syntax': [],
         'type': 'object',
         'properties': {'hi07_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI07-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi07_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI07-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi07_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI07-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi07_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI07-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi07_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI07-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi07_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI07-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi07_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI07-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi07_01', 'hi07_02']}
    hi07_01: L2000D_HI07_01
    hi07_02: L2000D_HI07_02
    hi07_03: L2000D_HI07_03 | None
    hi07_04: L2000D_HI07_04 | None


class L2000D_HI08_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI08-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI08_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI08-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI08_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI08-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI08_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI08-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI08_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI08-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI08_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI08-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI08_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI08-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 8',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 8 refdes= data_ele=C022',
         'sequence': 8,
         'syntax': [],
         'type': 'object',
         'properties': {'hi08_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI08-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi08_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI08-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi08_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI08-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi08_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI08-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi08_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI08-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi08_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI08-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi08_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI08-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi08_01', 'hi08_02']}
    hi08_01: L2000D_HI08_01
    hi08_02: L2000D_HI08_02
    hi08_03: L2000D_HI08_03 | None
    hi08_04: L2000D_HI08_04 | None


class L2000D_HI09_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI09-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI09_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI09-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI09_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI09-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI09_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI09-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI09_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI09-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI09_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI09-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI09_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI09-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 9',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 9 refdes= data_ele=C022',
         'sequence': 9,
         'syntax': [],
         'type': 'object',
         'properties': {'hi09_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI09-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi09_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI09-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi09_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI09-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi09_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI09-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi09_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI09-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi09_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI09-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi09_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI09-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi09_01', 'hi09_02']}
    hi09_01: L2000D_HI09_01
    hi09_02: L2000D_HI09_02
    hi09_03: L2000D_HI09_03 | None
    hi09_04: L2000D_HI09_04 | None


class L2000D_HI10_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI10-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI10_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI10_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI10-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI10_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI10-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI10_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI10-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI10_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI10-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI10_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI10-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 10',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 10 refdes= data_ele=C022',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'hi10_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI10-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi10_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI10-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi10_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI10-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi10_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI10-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi10_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI10-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi10_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI10-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi10_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI10-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi10_01', 'hi10_02']}
    hi10_01: L2000D_HI10_01
    hi10_02: L2000D_HI10_02
    hi10_03: L2000D_HI10_03 | None
    hi10_04: L2000D_HI10_04 | None


class L2000D_HI11_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI11-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI11_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI11_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI11-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI11_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI11-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI11_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI11-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI11_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI11-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI11_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI11-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 11',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 11 refdes= data_ele=C022',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'hi11_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI11-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi11_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI11-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi11_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI11-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi11_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI11-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi11_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI11-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi11_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI11-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi11_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI11-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi11_01', 'hi11_02']}
    hi11_01: L2000D_HI11_01
    hi11_02: L2000D_HI11_02
    hi11_03: L2000D_HI11_03 | None
    hi11_04: L2000D_HI11_04 | None


class L2000D_HI12_01(Element):
    """Diagnosis Type Code"""
    class Schema:
        json = {'title': 'Diagnosis Type Code',
         'usage': 'R',
         'description': 'xid=HI12-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'LOI']}]}}
        datatype = common.D_1270
        codes = ['BF', 'LOI']
        min_len = 1
        max_len = 3


class L2000D_HI12_02(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'R',
         'description': 'xid=HI12-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000D_HI12_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI12-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000D_HI12_04(Element):
    """Diagnosis Date"""
    class Schema:
        json = {'title': 'Diagnosis Date',
         'usage': 'S',
         'description': 'xid=HI12-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000D_HI12_05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=HI12-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000D_HI12_06(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=HI12-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000D_HI12_07(Element):
    """Version Identifier"""
    class Schema:
        json = {'title': 'Version Identifier',
         'usage': 'N',
         'description': 'xid=HI12-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000D_C022(Composite):
    class Schema:
        json = {'title': 'Diagnosis 12',
         'usage': 'S',
         'description': 'xid=None name=Diagnosis 12 refdes= data_ele=C022',
         'sequence': 12,
         'syntax': [],
         'type': 'object',
         'properties': {'hi12_01': {'title': 'Diagnosis Type Code',
                                    'usage': 'R',
                                    'description': 'xid=HI12-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['BF', 'LOI']}]}},
                        'hi12_02': {'title': 'Diagnosis Code',
                                    'usage': 'R',
                                    'description': 'xid=HI12-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi12_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI12-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8']}]}},
                        'hi12_04': {'title': 'Diagnosis Date',
                                    'usage': 'S',
                                    'description': 'xid=HI12-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi12_05': {'title': 'Monetary Amount',
                                    'usage': 'N',
                                    'description': 'xid=HI12-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi12_06': {'title': 'Quantity',
                                    'usage': 'N',
                                    'description': 'xid=HI12-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi12_07': {'title': 'Version Identifier',
                                    'usage': 'N',
                                    'description': 'xid=HI12-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi12_01', 'hi12_02']}
    hi12_01: L2000D_HI12_01
    hi12_02: L2000D_HI12_02
    hi12_03: L2000D_HI12_03 | None
    hi12_04: L2000D_HI12_04 | None


class L2000D_HI(Segment):
    """Dependent Diagnosis"""
    class Schema:
        json = {'title': 'Dependent Diagnosis',
         'usage': 'S',
         'description': 'xid=HI name=Dependent Diagnosis',
         'position': 80,
         'type': 'object',
         'properties': {'xid': {'literal': 'HI'},
                        'c022': {'$ref': '#/$elements/L2000D_C022'}},
         'required': ['c022']}
        segment_name = 'HI'
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022
    c022: L2000D_C022


class L2000D_PWK01(Element):
    """Attachment Report Type Code"""
    class Schema:
        json = {'title': 'Attachment Report Type Code',
         'usage': 'R',
         'description': 'xid=PWK01 data_ele=755',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/755'},
                            {'enum': ['03', '04', '05', '06', '07', '08', '09', '10',
                                      '11', '13', '15', '21', '48', '55', '59', '77',
                                      'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR',
                                      'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG',
                                      'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA',
                                      'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4',
                                      'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY',
                                      'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG',
                                      'V5', 'XP']}]}}
        datatype = common.D_755
        codes = ['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', '48', '55', '59', '77', 'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR', 'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4', 'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP']
        min_len = 2
        max_len = 2


class L2000D_PWK02(Element):
    """Attachment Transmission Code"""
    class Schema:
        json = {'title': 'Attachment Transmission Code',
         'usage': 'R',
         'description': 'xid=PWK02 data_ele=756',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/756'},
                            {'enum': ['BM', 'EL', 'EM', 'FX', 'VO']}]}}
        datatype = common.D_756
        codes = ['BM', 'EL', 'EM', 'FX', 'VO']
        min_len = 1
        max_len = 2


class L2000D_PWK03(Element):
    """Report Copies Needed"""
    class Schema:
        json = {'title': 'Report Copies Needed',
         'usage': 'N',
         'description': 'xid=PWK03 data_ele=757',
         'sequence': 3,
         'type': {'$ref': '#/$common/757'}}
        datatype = common.D_757
        min_len = 1
        max_len = 2


class L2000D_PWK04(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=PWK04 data_ele=98',
         'sequence': 4,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2000D_PWK05(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=PWK05 data_ele=66',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['AC']}]}}
        datatype = common.D_66
        codes = ['AC']
        min_len = 1
        max_len = 2


class L2000D_PWK06(Element):
    """Attachment Control Number"""
    class Schema:
        json = {'title': 'Attachment Control Number',
         'usage': 'S',
         'description': 'xid=PWK06 data_ele=67',
         'sequence': 6,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2000D_PWK07(Element):
    """Attachment Description"""
    class Schema:
        json = {'title': 'Attachment Description',
         'usage': 'S',
         'description': 'xid=PWK07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000D_C002(Composite):
    class Schema:
        json = {'title': 'Actions Indicated',
         'usage': 'N',
         'description': 'xid=None name=Actions Indicated refdes= data_ele=C002',
         'sequence': 8,
         'syntax': []}


class L2000D_PWK09(Element):
    """Request Category Code"""
    class Schema:
        json = {'title': 'Request Category Code',
         'usage': 'N',
         'description': 'xid=PWK09 data_ele=1525',
         'sequence': 9,
         'type': {'$ref': '#/$common/1525'}}
        datatype = common.D_1525
        min_len = 1
        max_len = 2


class L2000D_PWK(Segment):
    """Additional Patient Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Patient Information',
                   'usage': 'S',
                   'description': 'xid=PWK name=Additional Patient Information',
                   'position': 155,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PWK'},
                                  'pwk01': {'$ref': '#/$elements/L2000D_PWK01'},
                                  'pwk02': {'$ref': '#/$elements/L2000D_PWK02'},
                                  'pwk05': {'$ref': '#/$elements/L2000D_PWK05'},
                                  'pwk06': {'$ref': '#/$elements/L2000D_PWK06'},
                                  'pwk07': {'$ref': '#/$elements/L2000D_PWK07'}},
                   'required': ['pwk01', 'pwk02']},
         'maxItems': 10}
        segment_name = 'PWK'
    pwk01: L2000D_PWK01
    pwk02: L2000D_PWK02
    pwk05: L2000D_PWK05 | None
    pwk06: L2000D_PWK06 | None
    pwk07: L2000D_PWK07 | None


class L2010DA_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['QC']}]}}
        datatype = common.D_98
        codes = ['QC']
        min_len = 2
        max_len = 3


class L2010DA_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2010DA_NM103(Element):
    """Dependent Last Name"""
    class Schema:
        json = {'title': 'Dependent Last Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010DA_NM104(Element):
    """Dependent First Name"""
    class Schema:
        json = {'title': 'Dependent First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010DA_NM105(Element):
    """Dependent Middle Name"""
    class Schema:
        json = {'title': 'Dependent Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010DA_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010DA_NM107(Element):
    """Dependent Name Suffix"""
    class Schema:
        json = {'title': 'Dependent Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010DA_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['MI', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['MI', 'ZZ']
        min_len = 1
        max_len = 2


class L2010DA_NM109(Element):
    """Dependent Primary Identifier"""
    class Schema:
        json = {'title': 'Dependent Primary Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010DA_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010DA_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010DA_NM1(Segment):
    """Dependent Name"""
    class Schema:
        json = {'title': 'Dependent Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Dependent Name',
         'position': 170,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010DA_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010DA_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010DA_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010DA_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010DA_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010DA_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010DA_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010DA_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2010DA_NM101
    nm102: L2010DA_NM102
    nm103: L2010DA_NM103 | None
    nm104: L2010DA_NM104 | None
    nm105: L2010DA_NM105 | None
    nm107: L2010DA_NM107 | None
    nm108: L2010DA_NM108 | None
    nm109: L2010DA_NM109 | None


class L2010DA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['A6', 'EJ', 'SY']}]}}
        datatype = common.D_128
        codes = ['A6', 'EJ', 'SY']
        min_len = 2
        max_len = 3


class L2010DA_REF02(Element):
    """Dependent Supplemental Identifier"""
    class Schema:
        json = {'title': 'Dependent Supplemental Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010DA_REF03(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2010DA_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010DA_REF(Segment):
    """Dependent Supplemental Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Supplemental Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Dependent Supplemental Identification',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010DA_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010DA_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2010DA_REF01
    ref02: L2010DA_REF02


class L2010DA_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2010DA_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2010DA_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '33', '58', '64', '65', '66', '67', '68',
                                      '71', '77', '95']}]}}
        datatype = common.D_901
        codes = ['15', '33', '58', '64', '65', '66', '67', '68', '71', '77', '95']
        min_len = 2
        max_len = 2


class L2010DA_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N']}]}}
        datatype = common.D_889
        codes = ['C', 'N']
        min_len = 1
        max_len = 1


class L2010DA_AAA(Segment):
    """Dependent Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Dependent Request Validation',
                   'position': 230,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2010DA_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2010DA_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2010DA_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2010DA_AAA01
    aaa03: L2010DA_AAA03 | None
    aaa04: L2010DA_AAA04 | None


class L2010DA_DMG01(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DMG01 data_ele=1250',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2010DA_DMG02(Element):
    """Dependent Birth Date"""
    class Schema:
        json = {'title': 'Dependent Birth Date',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2010DA_DMG03(Element):
    """Dependent Gender Code"""
    class Schema:
        json = {'title': 'Dependent Gender Code',
         'usage': 'S',
         'description': 'xid=DMG03 data_ele=1068',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2010DA_DMG04(Element):
    """Marital Status Code"""
    class Schema:
        json = {'title': 'Marital Status Code',
         'usage': 'N',
         'description': 'xid=DMG04 data_ele=1067',
         'sequence': 4,
         'type': {'$ref': '#/$common/1067'}}
        datatype = common.D_1067
        min_len = 1
        max_len = 1


class L2010DA_DMG05(Element):
    """Race or Ethnicity Code"""
    class Schema:
        json = {'title': 'Race or Ethnicity Code',
         'usage': 'N',
         'description': 'xid=DMG05 data_ele=1109',
         'sequence': 5,
         'type': {'$ref': '#/$common/1109'}}
        datatype = common.D_1109
        min_len = 1
        max_len = 1


class L2010DA_DMG06(Element):
    """Citizenship Status Code"""
    class Schema:
        json = {'title': 'Citizenship Status Code',
         'usage': 'N',
         'description': 'xid=DMG06 data_ele=1066',
         'sequence': 6,
         'type': {'$ref': '#/$common/1066'}}
        datatype = common.D_1066
        min_len = 1
        max_len = 2


class L2010DA_DMG07(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'N',
         'description': 'xid=DMG07 data_ele=26',
         'sequence': 7,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L2010DA_DMG08(Element):
    """Basis of Verification Code"""
    class Schema:
        json = {'title': 'Basis of Verification Code',
         'usage': 'N',
         'description': 'xid=DMG08 data_ele=659',
         'sequence': 8,
         'type': {'$ref': '#/$common/659'}}
        datatype = common.D_659
        min_len = 1
        max_len = 2


class L2010DA_DMG09(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=DMG09 data_ele=380',
         'sequence': 9,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2010DA_DMG(Segment):
    """Dependent Demographic Information"""
    class Schema:
        json = {'title': 'Dependent Demographic Information',
         'usage': 'S',
         'description': 'xid=DMG name=Dependent Demographic Information',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2010DA_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2010DA_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2010DA_DMG03'}},
         'required': ['dmg01', 'dmg02']}
        segment_name = 'DMG'
    dmg01: L2010DA_DMG01
    dmg02: L2010DA_DMG02
    dmg03: L2010DA_DMG03 | None


class L2010DA_INS01(Element):
    """Insured Indicator"""
    class Schema:
        json = {'title': 'Insured Indicator',
         'usage': 'R',
         'description': 'xid=INS01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N']}]}}
        datatype = common.D_1073
        codes = ['N']
        min_len = 1
        max_len = 1


class L2010DA_INS02(Element):
    """Relationship to Insured"""
    class Schema:
        json = {'title': 'Relationship to Insured',
         'usage': 'R',
         'description': 'xid=INS02 data_ele=1069',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'},
                            {'enum': ['01', '04', '05', '07', '09', '10', '15', '17',
                                      '19', '20', '21', '22', '23', '24', '29', '32',
                                      '33', '34', '39', '40', '41', '43', '53',
                                      'G8']}]}}
        datatype = common.D_1069
        codes = ['01', '04', '05', '07', '09', '10', '15', '17', '19', '20', '21', '22', '23', '24', '29', '32', '33', '34', '39', '40', '41', '43', '53', 'G8']
        min_len = 2
        max_len = 2


class L2010DA_INS03(Element):
    """Maintenance Type Code"""
    class Schema:
        json = {'title': 'Maintenance Type Code',
         'usage': 'N',
         'description': 'xid=INS03 data_ele=875',
         'sequence': 3,
         'type': {'$ref': '#/$common/875'}}
        datatype = common.D_875
        min_len = 3
        max_len = 3


class L2010DA_INS04(Element):
    """Maintenance Reason Code"""
    class Schema:
        json = {'title': 'Maintenance Reason Code',
         'usage': 'N',
         'description': 'xid=INS04 data_ele=1203',
         'sequence': 4,
         'type': {'$ref': '#/$common/1203'}}
        datatype = common.D_1203
        min_len = 2
        max_len = 3


class L2010DA_INS05(Element):
    """Benefit Status Code"""
    class Schema:
        json = {'title': 'Benefit Status Code',
         'usage': 'N',
         'description': 'xid=INS05 data_ele=1216',
         'sequence': 5,
         'type': {'$ref': '#/$common/1216'}}
        datatype = common.D_1216
        min_len = 1
        max_len = 1


class L2010DA_INS06(Element):
    """Medicare Plan Code"""
    class Schema:
        json = {'title': 'Medicare Plan Code',
         'usage': 'N',
         'description': 'xid=INS06 data_ele=1218',
         'sequence': 6,
         'type': {'$ref': '#/$common/1218'}}
        datatype = common.D_1218
        min_len = 1
        max_len = 1


class L2010DA_INS07(Element):
    """Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event Code"""
    class Schema:
        json = {'title': 'Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying '
                  'Event Code',
         'usage': 'N',
         'description': 'xid=INS07 data_ele=1219',
         'sequence': 7,
         'type': {'$ref': '#/$common/1219'}}
        datatype = common.D_1219
        min_len = 1
        max_len = 2


class L2010DA_INS08(Element):
    """Employment Status Code"""
    class Schema:
        json = {'title': 'Employment Status Code',
         'usage': 'N',
         'description': 'xid=INS08 data_ele=584',
         'sequence': 8,
         'type': {'$ref': '#/$common/584'}}
        datatype = common.D_584
        min_len = 2
        max_len = 2


class L2010DA_INS09(Element):
    """Student Status Code"""
    class Schema:
        json = {'title': 'Student Status Code',
         'usage': 'N',
         'description': 'xid=INS09 data_ele=1220',
         'sequence': 9,
         'type': {'$ref': '#/$common/1220'}}
        datatype = common.D_1220
        min_len = 1
        max_len = 1


class L2010DA_INS10(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=INS10 data_ele=1073',
         'sequence': 10,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2010DA_INS11(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=INS11 data_ele=1250',
         'sequence': 11,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2010DA_INS12(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=INS12 data_ele=1251',
         'sequence': 12,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2010DA_INS13(Element):
    """Confidentiality Code"""
    class Schema:
        json = {'title': 'Confidentiality Code',
         'usage': 'N',
         'description': 'xid=INS13 data_ele=1165',
         'sequence': 13,
         'type': {'$ref': '#/$common/1165'}}
        datatype = common.D_1165
        min_len = 1
        max_len = 1


class L2010DA_INS14(Element):
    """City Name"""
    class Schema:
        json = {'title': 'City Name',
         'usage': 'N',
         'description': 'xid=INS14 data_ele=19',
         'sequence': 14,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010DA_INS15(Element):
    """State or Province Code"""
    class Schema:
        json = {'title': 'State or Province Code',
         'usage': 'N',
         'description': 'xid=INS15 data_ele=156',
         'sequence': 15,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        min_len = 2
        max_len = 2


class L2010DA_INS16(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'N',
         'description': 'xid=INS16 data_ele=26',
         'sequence': 16,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L2010DA_INS17(Element):
    """Birth Sequence Number"""
    class Schema:
        json = {'title': 'Birth Sequence Number',
         'usage': 'S',
         'description': 'xid=INS17 data_ele=1470',
         'sequence': 17,
         'type': {'$ref': '#/$common/1470'}}
        datatype = common.D_1470
        min_len = 1
        max_len = 9


class L2010DA_INS(Segment):
    """Dependent Relationship"""
    class Schema:
        json = {'title': 'Dependent Relationship',
         'usage': 'S',
         'description': 'xid=INS name=Dependent Relationship',
         'position': 260,
         'type': 'object',
         'properties': {'xid': {'literal': 'INS'},
                        'ins01': {'$ref': '#/$elements/L2010DA_INS01'},
                        'ins02': {'$ref': '#/$elements/L2010DA_INS02'},
                        'ins17': {'$ref': '#/$elements/L2010DA_INS17'}},
         'required': ['ins01', 'ins02']}
        segment_name = 'INS'
    ins01: L2010DA_INS01
    ins02: L2010DA_INS02
    ins17: L2010DA_INS17 | None


class L2010DA(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Name',
                   'usage': 'R',
                   'description': 'xid=2010DA name=Dependent Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010DA_NM1'},
                                  'ref': {'$ref': '#/$segments/L2010DA_REF'},
                                  'aaa': {'$ref': '#/$segments/L2010DA_AAA'},
                                  'dmg': {'$ref': '#/$segments/L2010DA_DMG'},
                                  'ins': {'$ref': '#/$segments/L2010DA_INS'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010DA_NM1
    ref: list[L2010DA_REF] | None
    aaa: list[L2010DA_AAA] | None
    dmg: L2010DA_DMG | None
    ins: L2010DA_INS | None


class L2010DB_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['1P', '2B', 'ABG', 'FA', 'PR', 'X3']}]}}
        datatype = common.D_98
        codes = ['1P', '2B', 'ABG', 'FA', 'PR', 'X3']
        min_len = 2
        max_len = 3


class L2010DB_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2010DB_NM103(Element):
    """Response Contact Last or Organization Name"""
    class Schema:
        json = {'title': 'Response Contact Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010DB_NM104(Element):
    """Response Contact First Name"""
    class Schema:
        json = {'title': 'Response Contact First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010DB_NM105(Element):
    """Response Contact Middle Name"""
    class Schema:
        json = {'title': 'Response Contact Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010DB_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010DB_NM107(Element):
    """Response Contact Name Suffix"""
    class Schema:
        json = {'title': 'Response Contact Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010DB_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'PI', 'XV', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'PI', 'XV', 'XX']
        min_len = 1
        max_len = 2


class L2010DB_NM109(Element):
    """Response Contact Identifier"""
    class Schema:
        json = {'title': 'Response Contact Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010DB_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010DB_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010DB_NM1(Segment):
    """Additional Patient Information Contact Name"""
    class Schema:
        json = {'title': 'Additional Patient Information Contact Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Additional Patient Information Contact Name',
         'position': 170,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010DB_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010DB_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010DB_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010DB_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010DB_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010DB_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010DB_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010DB_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2010DB_NM101
    nm102: L2010DB_NM102
    nm103: L2010DB_NM103 | None
    nm104: L2010DB_NM104 | None
    nm105: L2010DB_NM105 | None
    nm107: L2010DB_NM107 | None
    nm108: L2010DB_NM108 | None
    nm109: L2010DB_NM109 | None


class L2010DB_N301(Element):
    """Response Contact Address Line"""
    class Schema:
        json = {'title': 'Response Contact Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010DB_N302(Element):
    """Response Contact Address Line"""
    class Schema:
        json = {'title': 'Response Contact Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010DB_N3(Segment):
    """Additional Patient Information Contact Address"""
    class Schema:
        json = {'title': 'Additional Patient Information Contact Address',
         'usage': 'S',
         'description': 'xid=N3 name=Additional Patient Information Contact Address',
         'position': 200,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010DB_N301'},
                        'n302': {'$ref': '#/$elements/L2010DB_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010DB_N301
    n302: L2010DB_N302 | None


class L2010DB_N401(Element):
    """Response Contact City Name"""
    class Schema:
        json = {'title': 'Response Contact City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010DB_N402(Element):
    """Response Contact State or Province Code"""
    class Schema:
        json = {'title': 'Response Contact State or Province Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010DB_N403(Element):
    """Response Contact Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Response Contact Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010DB_N404(Element):
    """Response Contact Country Code"""
    class Schema:
        json = {'title': 'Response Contact Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010DB_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['B1', 'DP']}]}}
        datatype = common.D_309
        codes = ['B1', 'DP']
        min_len = 1
        max_len = 2


class L2010DB_N406(Element):
    """Response Contact Specific Location"""
    class Schema:
        json = {'title': 'Response Contact Specific Location',
         'usage': 'S',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2010DB_N4(Segment):
    """Additional Patient Information Contact City/State/Zip Code"""
    class Schema:
        json = {'title': 'Additional Patient Information Contact City/State/Zip Code',
         'usage': 'S',
         'description': 'xid=N4 name=Additional Patient Information Contact '
                        'City/State/Zip Code',
         'position': 210,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010DB_N401'},
                        'n402': {'$ref': '#/$elements/L2010DB_N402'},
                        'n403': {'$ref': '#/$elements/L2010DB_N403'},
                        'n404': {'$ref': '#/$elements/L2010DB_N404'},
                        'n405': {'$ref': '#/$elements/L2010DB_N405'},
                        'n406': {'$ref': '#/$elements/L2010DB_N406'}}}
        segment_name = 'N4'
    n401: L2010DB_N401 | None
    n402: L2010DB_N402 | None
    n403: L2010DB_N403 | None
    n404: L2010DB_N404 | None
    n405: L2010DB_N405 | None
    n406: L2010DB_N406 | None


class L2010DB_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L2010DB_PER02(Element):
    """Response Contact Name"""
    class Schema:
        json = {'title': 'Response Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2010DB_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010DB_PER04(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010DB_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010DB_PER06(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010DB_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010DB_PER08(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010DB_PER09(Element):
    """Contact Inquiry Reference"""
    class Schema:
        json = {'title': 'Contact Inquiry Reference',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'sequence': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2010DB_PER(Segment):
    """Additional Patient Information Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Patient Information Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Additional Patient Information Contact '
                                  'Information',
                   'position': 220,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2010DB_PER01'},
                                  'per02': {'$ref': '#/$elements/L2010DB_PER02'},
                                  'per03': {'$ref': '#/$elements/L2010DB_PER03'},
                                  'per04': {'$ref': '#/$elements/L2010DB_PER04'},
                                  'per05': {'$ref': '#/$elements/L2010DB_PER05'},
                                  'per06': {'$ref': '#/$elements/L2010DB_PER06'},
                                  'per07': {'$ref': '#/$elements/L2010DB_PER07'},
                                  'per08': {'$ref': '#/$elements/L2010DB_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2010DB_PER01
    per02: L2010DB_PER02 | None
    per03: L2010DB_PER03 | None
    per04: L2010DB_PER04 | None
    per05: L2010DB_PER05 | None
    per06: L2010DB_PER06 | None
    per07: L2010DB_PER07 | None
    per08: L2010DB_PER08 | None


class L2010DB(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Patient Information Contact Name',
                   'usage': 'S',
                   'description': 'xid=2010DB name=Additional Patient Information '
                                  'Contact Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010DB_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010DB_N3'},
                                  'n4': {'$ref': '#/$segments/L2010DB_N4'},
                                  'per': {'$ref': '#/$segments/L2010DB_PER'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010DB_NM1
    n3: L2010DB_N3 | None
    n4: L2010DB_N4 | None
    per: list[L2010DB_PER] | None


class L2000E_HL01(Element):
    """Hierarchical ID Number"""
    class Schema:
        json = {'title': 'Hierarchical ID Number',
         'usage': 'R',
         'description': 'xid=HL01 data_ele=628',
         'sequence': 1,
         'type': {'$ref': '#/$common/628'}}
        datatype = common.D_628
        min_len = 1
        max_len = 12


class L2000E_HL02(Element):
    """Hierarchical Parent ID Number"""
    class Schema:
        json = {'title': 'Hierarchical Parent ID Number',
         'usage': 'R',
         'description': 'xid=HL02 data_ele=734',
         'sequence': 2,
         'type': {'$ref': '#/$common/734'}}
        datatype = common.D_734
        min_len = 1
        max_len = 12


class L2000E_HL03(Element):
    """Hierarchical Level Code"""
    class Schema:
        json = {'title': 'Hierarchical Level Code',
         'usage': 'R',
         'description': 'xid=HL03 data_ele=735',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['19']}]}}
        datatype = common.D_735
        codes = ['19']
        min_len = 1
        max_len = 2


class L2000E_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'R',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['1']}]}}
        datatype = common.D_736
        codes = ['1']
        min_len = 1
        max_len = 1


class L2000E_HL(Segment):
    """Service Provider Level"""
    class Schema:
        json = {'title': 'Service Provider Level',
         'usage': 'R',
         'description': 'xid=HL name=Service Provider Level',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000E_HL01'},
                        'hl02': {'$ref': '#/$elements/L2000E_HL02'},
                        'hl03': {'$ref': '#/$elements/L2000E_HL03'},
                        'hl04': {'$ref': '#/$elements/L2000E_HL04'}},
         'required': ['hl01', 'hl02', 'hl03', 'hl04']}
        segment_name = 'HL'
    hl01: L2000E_HL01
    hl02: L2000E_HL02
    hl03: L2000E_HL03
    hl04: L2000E_HL04


class L2000E_MSG01(Element):
    """Free Form Message Text"""
    class Schema:
        json = {'title': 'Free Form Message Text',
         'usage': 'R',
         'description': 'xid=MSG01 data_ele=933',
         'sequence': 1,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2000E_MSG02(Element):
    """Printer Carriage Control Code"""
    class Schema:
        json = {'title': 'Printer Carriage Control Code',
         'usage': 'N',
         'description': 'xid=MSG02 data_ele=934',
         'sequence': 2,
         'type': {'$ref': '#/$common/934'}}
        datatype = common.D_934
        min_len = 2
        max_len = 2


class L2000E_MSG03(Element):
    """Number"""
    class Schema:
        json = {'title': 'Number',
         'usage': 'N',
         'description': 'xid=MSG03 data_ele=1470',
         'sequence': 3,
         'type': {'$ref': '#/$common/1470'}}
        datatype = common.D_1470
        min_len = 1
        max_len = 9


class L2000E_MSG(Segment):
    """Message Text"""
    class Schema:
        json = {'title': 'Message Text',
         'usage': 'S',
         'description': 'xid=MSG name=Message Text',
         'position': 160,
         'type': 'object',
         'properties': {'xid': {'literal': 'MSG'},
                        'msg01': {'$ref': '#/$elements/L2000E_MSG01'}},
         'required': ['msg01']}
        segment_name = 'MSG'
    msg01: L2000E_MSG01


class L2010E_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['1T', 'FA', 'SJ']}]}}
        datatype = common.D_98
        codes = ['1T', 'FA', 'SJ']
        min_len = 2
        max_len = 3


class L2010E_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2010E_NM103(Element):
    """Service Provider Last or Organization Name"""
    class Schema:
        json = {'title': 'Service Provider Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010E_NM104(Element):
    """Service Provider First Name"""
    class Schema:
        json = {'title': 'Service Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010E_NM105(Element):
    """Service Provider Middle Name"""
    class Schema:
        json = {'title': 'Service Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010E_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010E_NM107(Element):
    """Service Provider Name Suffix"""
    class Schema:
        json = {'title': 'Service Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010E_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'XX']
        min_len = 1
        max_len = 2


class L2010E_NM109(Element):
    """Service Provider Identifier"""
    class Schema:
        json = {'title': 'Service Provider Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010E_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010E_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010E_NM1(Segment):
    """Service Provider Name"""
    class Schema:
        json = {'title': 'Service Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Service Provider Name',
         'position': 170,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010E_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010E_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010E_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010E_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010E_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010E_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010E_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010E_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2010E_NM101
    nm102: L2010E_NM102
    nm103: L2010E_NM103 | None
    nm104: L2010E_NM104 | None
    nm105: L2010E_NM105 | None
    nm107: L2010E_NM107 | None
    nm108: L2010E_NM108 | None
    nm109: L2010E_NM109 | None


class L2010E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1G', '1J', 'EI', 'N5', 'N7', 'SY', 'ZH']}]}}
        datatype = common.D_128
        codes = ['1G', '1J', 'EI', 'N5', 'N7', 'SY', 'ZH']
        min_len = 2
        max_len = 3


class L2010E_REF02(Element):
    """Service Provider Supplemental Identifier"""
    class Schema:
        json = {'title': 'Service Provider Supplemental Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010E_REF03(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2010E_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010E_REF(Segment):
    """Service Provider Supplemental Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Provider Supplemental Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Service Provider Supplemental '
                                  'Identification',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010E_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010E_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 7}
        segment_name = 'REF'
    ref01: L2010E_REF01
    ref02: L2010E_REF02


class L2010E_N301(Element):
    """Service Provider Address Line"""
    class Schema:
        json = {'title': 'Service Provider Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010E_N302(Element):
    """Service Provider Address Line"""
    class Schema:
        json = {'title': 'Service Provider Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010E_N3(Segment):
    """Service Provider Address"""
    class Schema:
        json = {'title': 'Service Provider Address',
         'usage': 'S',
         'description': 'xid=N3 name=Service Provider Address',
         'position': 200,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010E_N301'},
                        'n302': {'$ref': '#/$elements/L2010E_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010E_N301
    n302: L2010E_N302 | None


class L2010E_N401(Element):
    """Service Provider City Name"""
    class Schema:
        json = {'title': 'Service Provider City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010E_N402(Element):
    """Service Provider State or Province Code"""
    class Schema:
        json = {'title': 'Service Provider State or Province Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010E_N403(Element):
    """Service Provider Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Service Provider Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010E_N404(Element):
    """Service Provider Country Code"""
    class Schema:
        json = {'title': 'Service Provider Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010E_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2010E_N406(Element):
    """Location Identifier"""
    class Schema:
        json = {'title': 'Location Identifier',
         'usage': 'N',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2010E_N4(Segment):
    """Service Provider City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Service Provider City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Service Provider City/State/ZIP Code',
         'position': 210,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010E_N401'},
                        'n402': {'$ref': '#/$elements/L2010E_N402'},
                        'n403': {'$ref': '#/$elements/L2010E_N403'},
                        'n404': {'$ref': '#/$elements/L2010E_N404'}}}
        segment_name = 'N4'
    n401: L2010E_N401 | None
    n402: L2010E_N402 | None
    n403: L2010E_N403 | None
    n404: L2010E_N404 | None


class L2010E_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L2010E_PER02(Element):
    """Service Provider Contact Name"""
    class Schema:
        json = {'title': 'Service Provider Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2010E_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010E_PER04(Element):
    """Service Provider Contact Communication Number"""
    class Schema:
        json = {'title': 'Service Provider Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010E_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010E_PER06(Element):
    """Service Provider Contact Communication Number"""
    class Schema:
        json = {'title': 'Service Provider Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010E_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010E_PER08(Element):
    """Service Provider Contact Communication Number"""
    class Schema:
        json = {'title': 'Service Provider Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010E_PER09(Element):
    """Contact Inquiry Reference"""
    class Schema:
        json = {'title': 'Contact Inquiry Reference',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'sequence': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2010E_PER(Segment):
    """Service Provider Contact Information"""
    class Schema:
        json = {'title': 'Service Provider Contact Information',
         'usage': 'S',
         'description': 'xid=PER name=Service Provider Contact Information',
         'position': 220,
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2010E_PER01'},
                        'per02': {'$ref': '#/$elements/L2010E_PER02'},
                        'per03': {'$ref': '#/$elements/L2010E_PER03'},
                        'per04': {'$ref': '#/$elements/L2010E_PER04'},
                        'per05': {'$ref': '#/$elements/L2010E_PER05'},
                        'per06': {'$ref': '#/$elements/L2010E_PER06'},
                        'per07': {'$ref': '#/$elements/L2010E_PER07'},
                        'per08': {'$ref': '#/$elements/L2010E_PER08'}},
         'required': ['per01']}
        segment_name = 'PER'
    per01: L2010E_PER01
    per02: L2010E_PER02 | None
    per03: L2010E_PER03 | None
    per04: L2010E_PER04 | None
    per05: L2010E_PER05 | None
    per06: L2010E_PER06 | None
    per07: L2010E_PER07 | None
    per08: L2010E_PER08 | None


class L2010E_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2010E_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2010E_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '33', '35', '41', '43', '44', '45', '46',
                                      '47', '49', '51', '52', '79', '97']}]}}
        datatype = common.D_901
        codes = ['15', '33', '35', '41', '43', '44', '45', '46', '47', '49', '51', '52', '79', '97']
        min_len = 2
        max_len = 2


class L2010E_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N']}]}}
        datatype = common.D_889
        codes = ['C', 'N']
        min_len = 1
        max_len = 1


class L2010E_AAA(Segment):
    """Service Provider Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Provider Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Service Provider Request Validation',
                   'position': 230,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2010E_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2010E_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2010E_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2010E_AAA01
    aaa03: L2010E_AAA03 | None
    aaa04: L2010E_AAA04 | None


class L2010E_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'},
                            {'enum': ['AD', 'AS', 'AT', 'CO', 'CV', 'OP', 'OR', 'OT',
                                      'PC', 'PE']}]}}
        datatype = common.D_1221
        codes = ['AD', 'AS', 'AT', 'CO', 'CV', 'OP', 'OR', 'OT', 'PC', 'PE']
        min_len = 1
        max_len = 3


class L2010E_PRV02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=PRV02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['ZZ']}]}}
        datatype = common.D_128
        codes = ['ZZ']
        min_len = 2
        max_len = 3


class L2010E_PRV03(Element):
    """Provider Taxonomy Code"""
    class Schema:
        json = {'title': 'Provider Taxonomy Code',
         'usage': 'R',
         'description': 'xid=PRV03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010E_PRV04(Element):
    """State or Province Code"""
    class Schema:
        json = {'title': 'State or Province Code',
         'usage': 'N',
         'description': 'xid=PRV04 data_ele=156',
         'sequence': 4,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        min_len = 2
        max_len = 2


class L2010E_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2010E_PRV06(Element):
    """Provider Organization Code"""
    class Schema:
        json = {'title': 'Provider Organization Code',
         'usage': 'N',
         'description': 'xid=PRV06 data_ele=1223',
         'sequence': 6,
         'type': {'$ref': '#/$common/1223'}}
        datatype = common.D_1223
        min_len = 3
        max_len = 3


class L2010E_PRV(Segment):
    """Service Provider Information"""
    class Schema:
        json = {'title': 'Service Provider Information',
         'usage': 'S',
         'description': 'xid=PRV name=Service Provider Information',
         'position': 240,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2010E_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2010E_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2010E_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2010E_PRV01
    prv02: L2010E_PRV02
    prv03: L2010E_PRV03


class L2010E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Provider Name',
                   'usage': 'R',
                   'description': 'xid=2010E name=Service Provider Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010E_NM1'},
                                  'ref': {'$ref': '#/$segments/L2010E_REF'},
                                  'n3': {'$ref': '#/$segments/L2010E_N3'},
                                  'n4': {'$ref': '#/$segments/L2010E_N4'},
                                  'per': {'$ref': '#/$segments/L2010E_PER'},
                                  'aaa': {'$ref': '#/$segments/L2010E_AAA'},
                                  'prv': {'$ref': '#/$segments/L2010E_PRV'}},
                   'required': ['nm1']},
         'maxItems': 3}
    nm1: L2010E_NM1
    ref: list[L2010E_REF] | None
    n3: L2010E_N3 | None
    n4: L2010E_N4 | None
    per: L2010E_PER | None
    aaa: list[L2010E_AAA] | None
    prv: L2010E_PRV | None


class L2000F_HL01(Element):
    """Hierarchical ID Number"""
    class Schema:
        json = {'title': 'Hierarchical ID Number',
         'usage': 'R',
         'description': 'xid=HL01 data_ele=628',
         'sequence': 1,
         'type': {'$ref': '#/$common/628'}}
        datatype = common.D_628
        min_len = 1
        max_len = 12


class L2000F_HL02(Element):
    """Hierarchical Parent ID Number"""
    class Schema:
        json = {'title': 'Hierarchical Parent ID Number',
         'usage': 'R',
         'description': 'xid=HL02 data_ele=734',
         'sequence': 2,
         'type': {'$ref': '#/$common/734'}}
        datatype = common.D_734
        min_len = 1
        max_len = 12


class L2000F_HL03(Element):
    """Hierarchical Level Code"""
    class Schema:
        json = {'title': 'Hierarchical Level Code',
         'usage': 'R',
         'description': 'xid=HL03 data_ele=735',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['SS']}]}}
        datatype = common.D_735
        codes = ['SS']
        min_len = 1
        max_len = 2


class L2000F_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'R',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['0']}]}}
        datatype = common.D_736
        codes = ['0']
        min_len = 1
        max_len = 1


class L2000F_HL(Segment):
    """Service Level"""
    class Schema:
        json = {'title': 'Service Level',
         'usage': 'R',
         'description': 'xid=HL name=Service Level',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000F_HL01'},
                        'hl02': {'$ref': '#/$elements/L2000F_HL02'},
                        'hl03': {'$ref': '#/$elements/L2000F_HL03'},
                        'hl04': {'$ref': '#/$elements/L2000F_HL04'}},
         'required': ['hl01', 'hl02', 'hl03', 'hl04']}
        segment_name = 'HL'
    hl01: L2000F_HL01
    hl02: L2000F_HL02
    hl03: L2000F_HL03
    hl04: L2000F_HL04


class L2000F_TRN01(Element):
    """Trace Type Code"""
    class Schema:
        json = {'title': 'Trace Type Code',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['1', '2']}]}}
        datatype = common.D_481
        codes = ['1', '2']
        min_len = 1
        max_len = 2


class L2000F_TRN02(Element):
    """Service Trace Number"""
    class Schema:
        json = {'title': 'Service Trace Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000F_TRN03(Element):
    """Trace Assigning Entity Identifier"""
    class Schema:
        json = {'title': 'Trace Assigning Entity Identifier',
         'usage': 'R',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class L2000F_TRN04(Element):
    """Trace Assigning Entity Additional Identifier"""
    class Schema:
        json = {'title': 'Trace Assigning Entity Additional Identifier',
         'usage': 'S',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000F_TRN(Segment):
    """Service Trace Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Trace Number',
                   'usage': 'S',
                   'description': 'xid=TRN name=Service Trace Number',
                   'position': 20,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'TRN'},
                                  'trn01': {'$ref': '#/$elements/L2000F_TRN01'},
                                  'trn02': {'$ref': '#/$elements/L2000F_TRN02'},
                                  'trn03': {'$ref': '#/$elements/L2000F_TRN03'},
                                  'trn04': {'$ref': '#/$elements/L2000F_TRN04'}},
                   'required': ['trn01', 'trn02', 'trn03']},
         'maxItems': 3}
        segment_name = 'TRN'
    trn01: L2000F_TRN01
    trn02: L2000F_TRN02
    trn03: L2000F_TRN03
    trn04: L2000F_TRN04 | None


class L2000F_AAA01(Element):
    """Valid Request Indicator"""
    class Schema:
        json = {'title': 'Valid Request Indicator',
         'usage': 'R',
         'description': 'xid=AAA01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000F_AAA02(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=AAA02 data_ele=559',
         'sequence': 2,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2000F_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '33', '52', '57', '60', '61', '62',
                                      'T5']}]}}
        datatype = common.D_901
        codes = ['15', '33', '52', '57', '60', '61', '62', 'T5']
        min_len = 2
        max_len = 2


class L2000F_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'S',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'}, {'enum': ['C', 'N']}]}}
        datatype = common.D_889
        codes = ['C', 'N']
        min_len = 1
        max_len = 1


class L2000F_AAA(Segment):
    """Service Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Service Request Validation',
                   'position': 30,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2000F_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2000F_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2000F_AAA04'}},
                   'required': ['aaa01']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2000F_AAA01
    aaa03: L2000F_AAA03 | None
    aaa04: L2000F_AAA04 | None


class L2000F_UM01(Element):
    """Request Category Code"""
    class Schema:
        json = {'title': 'Request Category Code',
         'usage': 'R',
         'description': 'xid=UM01 data_ele=1525',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1525'}, {'enum': ['AR', 'HS', 'SC']}]}}
        datatype = common.D_1525
        codes = ['AR', 'HS', 'SC']
        min_len = 1
        max_len = 2


class L2000F_UM02(Element):
    """Certification Type Code"""
    class Schema:
        json = {'title': 'Certification Type Code',
         'usage': 'R',
         'description': 'xid=UM02 data_ele=1322',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1322'},
                            {'enum': ['1', '2', '3', '4', 'I', 'R', 'S']}]}}
        datatype = common.D_1322
        codes = ['1', '2', '3', '4', 'I', 'R', 'S']
        min_len = 1
        max_len = 1


class L2000F_UM03(Element):
    """Service Type Code"""
    class Schema:
        json = {'title': 'Service Type Code',
         'usage': 'S',
         'description': 'xid=UM03 data_ele=1365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1365'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '12',
                                      '14', '15', '16', '17', '18', '20', '21', '23',
                                      '24', '25', '26', '27', '28', '33', '34', '35',
                                      '36', '37', '38', '39', '40', '42', '44', '45',
                                      '46', '48', '50', '51', '52', '53', '54', '56',
                                      '57', '58', '59', '61', '62', '63', '64', '65',
                                      '67', '68', '69', '70', '71', '72', '73', '74',
                                      '75', '76', '77', '78', '79', '80', '82', '83',
                                      '84', '85', '86', '93', '94', '95', '98', '99',
                                      'A0', 'A1', 'A2', 'A3', 'A4', 'A6', 'A7', 'A8',
                                      'A9', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AI',
                                      'AJ', 'AK', 'AL', 'AR', 'BB', 'BC', 'BD', 'BE',
                                      'BF', 'BG', 'BS']}]}}
        datatype = common.D_1365
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '12', '14', '15', '16', '17', '18', '20', '21', '23', '24', '25', '26', '27', '28', '33', '34', '35', '36', '37', '38', '39', '40', '42', '44', '45', '46', '48', '50', '51', '52', '53', '54', '56', '57', '58', '59', '61', '62', '63', '64', '65', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '82', '83', '84', '85', '86', '93', '94', '95', '98', '99', 'A0', 'A1', 'A2', 'A3', 'A4', 'A6', 'A7', 'A8', 'A9', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AI', 'AJ', 'AK', 'AL', 'AR', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BS']
        min_len = 1
        max_len = 2


class L2000F_UM04_01(Element):
    """Facility Type Code"""
    class Schema:
        json = {'title': 'Facility Type Code',
         'usage': 'R',
         'description': 'xid=UM04-01 data_ele=1331',
         'sequence': 1,
         'type': {'$ref': '#/$common/1331'}}
        datatype = common.D_1331
        min_len = 1
        max_len = 2


class L2000F_UM04_02(Element):
    """Facility Code Qualifier"""
    class Schema:
        json = {'title': 'Facility Code Qualifier',
         'usage': 'R',
         'description': 'xid=UM04-02 data_ele=1332',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1332'}, {'enum': ['A', 'B']}]}}
        datatype = common.D_1332
        codes = ['A', 'B']
        min_len = 1
        max_len = 2


class L2000F_UM04_03(Element):
    """Claim Frequency Type Code"""
    class Schema:
        json = {'title': 'Claim Frequency Type Code',
         'usage': 'N',
         'description': 'xid=UM04-03 data_ele=1325',
         'sequence': 3,
         'type': {'$ref': '#/$common/1325'}}
        datatype = common.D_1325
        min_len = 1
        max_len = 1


class L2000F_C023(Composite):
    class Schema:
        json = {'title': 'Health Care Service Location Information',
         'usage': 'S',
         'description': 'xid=None name=Health Care Service Location Information '
                        'refdes= data_ele=C023',
         'sequence': 4,
         'syntax': [],
         'type': 'object',
         'properties': {'um04_01': {'title': 'Facility Type Code',
                                    'usage': 'R',
                                    'description': 'xid=UM04-01 data_ele=1331',
                                    'sequence': 1,
                                    'type': {'$ref': '#/$common/1331'}},
                        'um04_02': {'title': 'Facility Code Qualifier',
                                    'usage': 'R',
                                    'description': 'xid=UM04-02 data_ele=1332',
                                    'sequence': 2,
                                    'type': {'allOf': [{'$ref': '#/$common/1332'},
                                                       {'enum': ['A', 'B']}]}},
                        'um04_03': {'title': 'Claim Frequency Type Code',
                                    'usage': 'N',
                                    'description': 'xid=UM04-03 data_ele=1325',
                                    'sequence': 3,
                                    'type': {'$ref': '#/$common/1325'}}},
         'required': ['um04_01', 'um04_02']}
    um04_01: L2000F_UM04_01
    um04_02: L2000F_UM04_02


class L2000F_C024(Composite):
    class Schema:
        json = {'title': 'Related Causes Information',
         'usage': 'N',
         'description': 'xid=None name=Related Causes Information refdes= '
                        'data_ele=C024',
         'sequence': 5,
         'syntax': []}


class L2000F_UM06(Element):
    """Level of Service Code"""
    class Schema:
        json = {'title': 'Level of Service Code',
         'usage': 'S',
         'description': 'xid=UM06 data_ele=1338',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1338'}, {'enum': ['03', 'U']}]}}
        datatype = common.D_1338
        codes = ['03', 'U']
        min_len = 1
        max_len = 3


class L2000F_UM07(Element):
    """Current Health Condition Code"""
    class Schema:
        json = {'title': 'Current Health Condition Code',
         'usage': 'N',
         'description': 'xid=UM07 data_ele=1213',
         'sequence': 7,
         'type': {'$ref': '#/$common/1213'}}
        datatype = common.D_1213
        min_len = 1
        max_len = 1


class L2000F_UM08(Element):
    """Prognosis Code"""
    class Schema:
        json = {'title': 'Prognosis Code',
         'usage': 'N',
         'description': 'xid=UM08 data_ele=923',
         'sequence': 8,
         'type': {'$ref': '#/$common/923'}}
        datatype = common.D_923
        min_len = 1
        max_len = 1


class L2000F_UM09(Element):
    """Release of Information Code"""
    class Schema:
        json = {'title': 'Release of Information Code',
         'usage': 'N',
         'description': 'xid=UM09 data_ele=1363',
         'sequence': 9,
         'type': {'$ref': '#/$common/1363'}}
        datatype = common.D_1363
        min_len = 1
        max_len = 1


class L2000F_UM10(Element):
    """Delay Reason Code"""
    class Schema:
        json = {'title': 'Delay Reason Code',
         'usage': 'N',
         'description': 'xid=UM10 data_ele=1514',
         'sequence': 10,
         'type': {'$ref': '#/$common/1514'}}
        datatype = common.D_1514
        min_len = 1
        max_len = 2


class L2000F_UM(Segment):
    """Health Care Services Review Information"""
    class Schema:
        json = {'title': 'Health Care Services Review Information',
         'usage': 'R',
         'description': 'xid=UM name=Health Care Services Review Information',
         'position': 40,
         'type': 'object',
         'properties': {'xid': {'literal': 'UM'},
                        'um01': {'$ref': '#/$elements/L2000F_UM01'},
                        'um02': {'$ref': '#/$elements/L2000F_UM02'},
                        'um03': {'$ref': '#/$elements/L2000F_UM03'},
                        'c023': {'$ref': '#/$elements/L2000F_C023'},
                        'um06': {'$ref': '#/$elements/L2000F_UM06'}},
         'required': ['um01', 'um02']}
        segment_name = 'UM'
    um01: L2000F_UM01
    um02: L2000F_UM02
    um03: L2000F_UM03 | None
    c023: L2000F_C023 | None
    um06: L2000F_UM06 | None


class L2000F_HCR01(Element):
    """Certification Action Code"""
    class Schema:
        json = {'title': 'Certification Action Code',
         'usage': 'R',
         'description': 'xid=HCR01 data_ele=306',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/306'},
                            {'enum': ['A1', 'A3', 'A4', 'A6', 'CT', 'NA']}]}}
        datatype = common.D_306
        codes = ['A1', 'A3', 'A4', 'A6', 'CT', 'NA']
        min_len = 1
        max_len = 2


class L2000F_HCR02(Element):
    """Certification Number"""
    class Schema:
        json = {'title': 'Certification Number',
         'usage': 'S',
         'description': 'xid=HCR02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000F_HCR03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'S',
         'description': 'xid=HCR03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['35', '36', '37', '41', '53', '69', '70', '82',
                                      '83', '84', '85', '86', '87', '88', '89', '90',
                                      '91', '92', '96', '98', 'E8']}]}}
        datatype = common.D_901
        codes = ['35', '36', '37', '41', '53', '69', '70', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '96', '98', 'E8']
        min_len = 2
        max_len = 2


class L2000F_HCR04(Element):
    """Second Surgical Opinion Indicator"""
    class Schema:
        json = {'title': 'Second Surgical Opinion Indicator',
         'usage': 'S',
         'description': 'xid=HCR04 data_ele=1073',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000F_HCR(Segment):
    """Health Care Services Review"""
    class Schema:
        json = {'title': 'Health Care Services Review',
         'usage': 'S',
         'description': 'xid=HCR name=Health Care Services Review',
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'HCR'},
                        'hcr01': {'$ref': '#/$elements/L2000F_HCR01'},
                        'hcr02': {'$ref': '#/$elements/L2000F_HCR02'},
                        'hcr03': {'$ref': '#/$elements/L2000F_HCR03'},
                        'hcr04': {'$ref': '#/$elements/L2000F_HCR04'}},
         'required': ['hcr01']}
        segment_name = 'HCR'
    hcr01: L2000F_HCR01
    hcr02: L2000F_HCR02 | None
    hcr03: L2000F_HCR03 | None
    hcr04: L2000F_HCR04 | None


class L2000F_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['BB']}]}}
        datatype = common.D_128
        codes = ['BB']
        min_len = 2
        max_len = 3


class L2000F_REF02(Element):
    """Previous Certification Identifier"""
    class Schema:
        json = {'title': 'Previous Certification Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000F_REF03(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000F_REF(Segment):
    """Previous Certification Identification"""
    class Schema:
        json = {'title': 'Previous Certification Identification',
         'usage': 'S',
         'description': 'xid=REF name=Previous Certification Identification',
         'position': 60,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2000F_REF01'},
                        'ref02': {'$ref': '#/$elements/L2000F_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2000F_REF01
    ref02: L2000F_REF02


class L2000F_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['472']}]}}
        datatype = common.D_374
        codes = ['472']
        min_len = 3
        max_len = 3


class L2000F_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_DTP03(Element):
    """Proposed or Actual Service Date"""
    class Schema:
        json = {'title': 'Proposed or Actual Service Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_DTP(Segment):
    """Service Date"""
    class Schema:
        json = {'title': 'Service Date',
         'usage': 'S',
         'description': 'xid=DTP name=Service Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000F_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000F_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000F_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000F_DTP01
    dtp02: L2000F_DTP02
    dtp03: L2000F_DTP03


class L2000F_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['435']}]}}
        datatype = common.D_374
        codes = ['435']
        min_len = 3
        max_len = 3


class L2000F_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_DTP03(Element):
    """Proposed or Actual Admission Date"""
    class Schema:
        json = {'title': 'Proposed or Actual Admission Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_DTP(Segment):
    """Admission Date"""
    class Schema:
        json = {'title': 'Admission Date',
         'usage': 'S',
         'description': 'xid=DTP name=Admission Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000F_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000F_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000F_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000F_DTP01
    dtp02: L2000F_DTP02
    dtp03: L2000F_DTP03


class L2000F_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['096']}]}}
        datatype = common.D_374
        codes = ['096']
        min_len = 3
        max_len = 3


class L2000F_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000F_DTP03(Element):
    """Proposed or Actual Discharge Date"""
    class Schema:
        json = {'title': 'Proposed or Actual Discharge Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_DTP(Segment):
    """Discharge Date"""
    class Schema:
        json = {'title': 'Discharge Date',
         'usage': 'S',
         'description': 'xid=DTP name=Discharge Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000F_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000F_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000F_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000F_DTP01
    dtp02: L2000F_DTP02
    dtp03: L2000F_DTP03


class L2000F_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['456']}]}}
        datatype = common.D_374
        codes = ['456']
        min_len = 3
        max_len = 3


class L2000F_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000F_DTP03(Element):
    """Proposed or Actual Surgery Date"""
    class Schema:
        json = {'title': 'Proposed or Actual Surgery Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_DTP(Segment):
    """Surgery Date"""
    class Schema:
        json = {'title': 'Surgery Date',
         'usage': 'S',
         'description': 'xid=DTP name=Surgery Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000F_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000F_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000F_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000F_DTP01
    dtp02: L2000F_DTP02
    dtp03: L2000F_DTP03


class L2000F_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['102']}]}}
        datatype = common.D_374
        codes = ['102']
        min_len = 3
        max_len = 3


class L2000F_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000F_DTP03(Element):
    """Certification Issue Date"""
    class Schema:
        json = {'title': 'Certification Issue Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_DTP(Segment):
    """Certification Issue Date"""
    class Schema:
        json = {'title': 'Certification Issue Date',
         'usage': 'S',
         'description': 'xid=DTP name=Certification Issue Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000F_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000F_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000F_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000F_DTP01
    dtp02: L2000F_DTP02
    dtp03: L2000F_DTP03


class L2000F_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['036']}]}}
        datatype = common.D_374
        codes = ['036']
        min_len = 3
        max_len = 3


class L2000F_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000F_DTP03(Element):
    """Certification Expiration Date"""
    class Schema:
        json = {'title': 'Certification Expiration Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_DTP(Segment):
    """Certification Expiration Date"""
    class Schema:
        json = {'title': 'Certification Expiration Date',
         'usage': 'S',
         'description': 'xid=DTP name=Certification Expiration Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000F_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000F_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000F_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000F_DTP01
    dtp02: L2000F_DTP02
    dtp03: L2000F_DTP03


class L2000F_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['007']}]}}
        datatype = common.D_374
        codes = ['007']
        min_len = 3
        max_len = 3


class L2000F_DTP02(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'R',
         'description': 'xid=DTP02 data_ele=1250',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_DTP03(Element):
    """Certification Effective Date"""
    class Schema:
        json = {'title': 'Certification Effective Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_DTP(Segment):
    """Certification Effective Date"""
    class Schema:
        json = {'title': 'Certification Effective Date',
         'usage': 'S',
         'description': 'xid=DTP name=Certification Effective Date',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2000F_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2000F_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2000F_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2000F_DTP01
    dtp02: L2000F_DTP02
    dtp03: L2000F_DTP03


class L2000F_HI01_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI01-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI01_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI01_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI01-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI01_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI01-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI01_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI01-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI01_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI01-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI01_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI01-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 1',
         'usage': 'R',
         'description': 'xid=None name=Procedure Code 1 refdes= data_ele=C022',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'hi01_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI01-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi01_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI01-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi01_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI01-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi01_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI01-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi01_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI01-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi01_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI01-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi01_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI01-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi01_01', 'hi01_02']}
    hi01_01: L2000F_HI01_01
    hi01_02: L2000F_HI01_02
    hi01_03: L2000F_HI01_03 | None
    hi01_04: L2000F_HI01_04 | None
    hi01_05: L2000F_HI01_05 | None
    hi01_06: L2000F_HI01_06 | None
    hi01_07: L2000F_HI01_07 | None


class L2000F_HI02_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI02-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI02_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI02-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI02_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI02-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI02_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI02-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI02_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI02-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI02_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI02-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI02_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI02-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 2',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 2 refdes= data_ele=C022',
         'sequence': 2,
         'syntax': [],
         'type': 'object',
         'properties': {'hi02_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI02-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi02_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI02-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi02_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI02-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi02_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI02-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi02_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI02-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi02_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI02-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi02_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI02-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi02_01', 'hi02_02']}
    hi02_01: L2000F_HI02_01
    hi02_02: L2000F_HI02_02
    hi02_03: L2000F_HI02_03 | None
    hi02_04: L2000F_HI02_04 | None
    hi02_05: L2000F_HI02_05 | None
    hi02_06: L2000F_HI02_06 | None
    hi02_07: L2000F_HI02_07 | None


class L2000F_HI03_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI03-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI03_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI03-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI03_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI03-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI03_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI03-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI03_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI03-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI03_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI03-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI03_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI03-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 3',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 3 refdes= data_ele=C022',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'hi03_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI03-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi03_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI03-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi03_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI03-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi03_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI03-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi03_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI03-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi03_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI03-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi03_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI03-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi03_01', 'hi03_02']}
    hi03_01: L2000F_HI03_01
    hi03_02: L2000F_HI03_02
    hi03_03: L2000F_HI03_03 | None
    hi03_04: L2000F_HI03_04 | None
    hi03_05: L2000F_HI03_05 | None
    hi03_06: L2000F_HI03_06 | None
    hi03_07: L2000F_HI03_07 | None


class L2000F_HI04_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI04-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI04_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI04-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI04_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI04-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI04_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI04-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI04_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI04-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI04_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI04-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI04_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI04-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 4',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 4 refdes= data_ele=C022',
         'sequence': 4,
         'syntax': [],
         'type': 'object',
         'properties': {'hi04_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI04-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi04_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI04-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi04_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI04-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi04_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI04-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi04_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI04-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi04_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI04-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi04_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI04-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi04_01', 'hi04_02']}
    hi04_01: L2000F_HI04_01
    hi04_02: L2000F_HI04_02
    hi04_03: L2000F_HI04_03 | None
    hi04_04: L2000F_HI04_04 | None
    hi04_05: L2000F_HI04_05 | None
    hi04_06: L2000F_HI04_06 | None
    hi04_07: L2000F_HI04_07 | None


class L2000F_HI05_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI05-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI05_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI05-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI05_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI05-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI05_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI05-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI05_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI05-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI05_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI05-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI05_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI05-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 5',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 5 refdes= data_ele=C022',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'hi05_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI05-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi05_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI05-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi05_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI05-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi05_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI05-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi05_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI05-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi05_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI05-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi05_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI05-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi05_01', 'hi05_02']}
    hi05_01: L2000F_HI05_01
    hi05_02: L2000F_HI05_02
    hi05_03: L2000F_HI05_03 | None
    hi05_04: L2000F_HI05_04 | None
    hi05_05: L2000F_HI05_05 | None
    hi05_06: L2000F_HI05_06 | None
    hi05_07: L2000F_HI05_07 | None


class L2000F_HI06_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI06-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI06_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI06-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI06_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI06-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI06_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI06-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI06_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI06-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI06_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI06-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI06_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI06-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 6',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 6 refdes= data_ele=C022',
         'sequence': 6,
         'syntax': [],
         'type': 'object',
         'properties': {'hi06_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI06-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi06_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI06-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi06_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI06-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi06_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI06-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi06_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI06-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi06_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI06-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi06_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI06-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi06_01', 'hi06_02']}
    hi06_01: L2000F_HI06_01
    hi06_02: L2000F_HI06_02
    hi06_03: L2000F_HI06_03 | None
    hi06_04: L2000F_HI06_04 | None
    hi06_05: L2000F_HI06_05 | None
    hi06_06: L2000F_HI06_06 | None
    hi06_07: L2000F_HI06_07 | None


class L2000F_HI07_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI07-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI07_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI07-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI07_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI07-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI07_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI07-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI07_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI07-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI07_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI07-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI07_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI07-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 7',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 7 refdes= data_ele=C022',
         'sequence': 7,
         'syntax': [],
         'type': 'object',
         'properties': {'hi07_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI07-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi07_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI07-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi07_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI07-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi07_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI07-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi07_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI07-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi07_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI07-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi07_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI07-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi07_01', 'hi07_02']}
    hi07_01: L2000F_HI07_01
    hi07_02: L2000F_HI07_02
    hi07_03: L2000F_HI07_03 | None
    hi07_04: L2000F_HI07_04 | None
    hi07_05: L2000F_HI07_05 | None
    hi07_06: L2000F_HI07_06 | None
    hi07_07: L2000F_HI07_07 | None


class L2000F_HI08_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI08-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI08_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI08-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI08_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI08-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI08_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI08-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI08_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI08-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI08_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI08-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI08_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI08-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 8',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 8 refdes= data_ele=C022',
         'sequence': 8,
         'syntax': [],
         'type': 'object',
         'properties': {'hi08_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI08-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi08_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI08-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi08_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI08-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi08_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI08-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi08_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI08-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi08_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI08-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi08_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI08-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi08_01', 'hi08_02']}
    hi08_01: L2000F_HI08_01
    hi08_02: L2000F_HI08_02
    hi08_03: L2000F_HI08_03 | None
    hi08_04: L2000F_HI08_04 | None
    hi08_05: L2000F_HI08_05 | None
    hi08_06: L2000F_HI08_06 | None
    hi08_07: L2000F_HI08_07 | None


class L2000F_HI09_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI09-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI09_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI09-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI09_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI09-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI09_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI09-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI09_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI09-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI09_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI09-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI09_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI09-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 9',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 9 refdes= data_ele=C022',
         'sequence': 9,
         'syntax': [],
         'type': 'object',
         'properties': {'hi09_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI09-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi09_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI09-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi09_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI09-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi09_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI09-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi09_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI09-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi09_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI09-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi09_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI09-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi09_01', 'hi09_02']}
    hi09_01: L2000F_HI09_01
    hi09_02: L2000F_HI09_02
    hi09_03: L2000F_HI09_03 | None
    hi09_04: L2000F_HI09_04 | None
    hi09_05: L2000F_HI09_05 | None
    hi09_06: L2000F_HI09_06 | None
    hi09_07: L2000F_HI09_07 | None


class L2000F_HI10_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI10-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI10_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI10_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI10-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI10_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI10-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI10_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI10-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI10_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI10-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI10_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI10-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 10',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 10 refdes= data_ele=C022',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'hi10_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI10-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi10_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI10-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi10_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI10-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi10_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI10-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi10_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI10-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi10_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI10-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi10_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI10-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi10_01', 'hi10_02']}
    hi10_01: L2000F_HI10_01
    hi10_02: L2000F_HI10_02
    hi10_03: L2000F_HI10_03 | None
    hi10_04: L2000F_HI10_04 | None
    hi10_05: L2000F_HI10_05 | None
    hi10_06: L2000F_HI10_06 | None
    hi10_07: L2000F_HI10_07 | None


class L2000F_HI11_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI11-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI11_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI11_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI11-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI11_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI11-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI11_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI11-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI11_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI11-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI11_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI11-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 11',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 11 refdes= data_ele=C022',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'hi11_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI11-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi11_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI11-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi11_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI11-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi11_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI11-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi11_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI11-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi11_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI11-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi11_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI11-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi11_01', 'hi11_02']}
    hi11_01: L2000F_HI11_01
    hi11_02: L2000F_HI11_02
    hi11_03: L2000F_HI11_03 | None
    hi11_04: L2000F_HI11_04 | None
    hi11_05: L2000F_HI11_05 | None
    hi11_06: L2000F_HI11_06 | None
    hi11_07: L2000F_HI11_07 | None


class L2000F_HI12_01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=HI12-01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'},
                            {'enum': ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['ABR', 'BO', 'BQ', 'JP', 'LOI', 'NDC', 'ZZ']
        min_len = 1
        max_len = 3


class L2000F_HI12_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=HI12-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2000F_HI12_03(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=HI12-03 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8', 'RD8']}]}}
        datatype = common.D_1250
        codes = ['D8', 'RD8']
        min_len = 2
        max_len = 3


class L2000F_HI12_04(Element):
    """Procedure Date"""
    class Schema:
        json = {'title': 'Procedure Date',
         'usage': 'S',
         'description': 'xid=HI12-04 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_HI12_05(Element):
    """Procedure Monetary Amount"""
    class Schema:
        json = {'title': 'Procedure Monetary Amount',
         'usage': 'S',
         'description': 'xid=HI12-05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000F_HI12_06(Element):
    """Procedure Quantity"""
    class Schema:
        json = {'title': 'Procedure Quantity',
         'usage': 'S',
         'description': 'xid=HI12-06 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HI12_07(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'S',
         'description': 'xid=HI12-07 data_ele=799',
         'sequence': 7,
         'type': {'$ref': '#/$common/799'}}
        datatype = common.D_799
        min_len = 1
        max_len = 30


class L2000F_C022(Composite):
    class Schema:
        json = {'title': 'Procedure Code 12',
         'usage': 'S',
         'description': 'xid=None name=Procedure Code 12 refdes= data_ele=C022',
         'sequence': 12,
         'syntax': [],
         'type': 'object',
         'properties': {'hi12_01': {'title': 'Code List Qualifier Code',
                                    'usage': 'R',
                                    'description': 'xid=HI12-01 data_ele=1270',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                       {'enum': ['ABR', 'BO', 'BQ',
                                                                 'JP', 'LOI', 'NDC',
                                                                 'ZZ']}]}},
                        'hi12_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=HI12-02 data_ele=1271',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/1271'}},
                        'hi12_03': {'title': 'Date Time Period Format Qualifier',
                                    'usage': 'S',
                                    'description': 'xid=HI12-03 data_ele=1250',
                                    'sequence': 3,
                                    'type': {'allOf': [{'$ref': '#/$common/1250'},
                                                       {'enum': ['D8', 'RD8']}]}},
                        'hi12_04': {'title': 'Procedure Date',
                                    'usage': 'S',
                                    'description': 'xid=HI12-04 data_ele=1251',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1251'}},
                        'hi12_05': {'title': 'Procedure Monetary Amount',
                                    'usage': 'S',
                                    'description': 'xid=HI12-05 data_ele=782',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/782'}},
                        'hi12_06': {'title': 'Procedure Quantity',
                                    'usage': 'S',
                                    'description': 'xid=HI12-06 data_ele=380',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/380'}},
                        'hi12_07': {'title': 'Version, Release, or Industry Identifier',
                                    'usage': 'S',
                                    'description': 'xid=HI12-07 data_ele=799',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/799'}}},
         'required': ['hi12_01', 'hi12_02']}
    hi12_01: L2000F_HI12_01
    hi12_02: L2000F_HI12_02
    hi12_03: L2000F_HI12_03 | None
    hi12_04: L2000F_HI12_04 | None
    hi12_05: L2000F_HI12_05 | None
    hi12_06: L2000F_HI12_06 | None
    hi12_07: L2000F_HI12_07 | None


class L2000F_HI(Segment):
    """Procedures"""
    class Schema:
        json = {'title': 'Procedures',
         'usage': 'S',
         'description': 'xid=HI name=Procedures',
         'position': 80,
         'type': 'object',
         'properties': {'xid': {'literal': 'HI'},
                        'c022': {'$ref': '#/$elements/L2000F_C022'}},
         'required': ['c022']}
        segment_name = 'HI'
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022
    c022: L2000F_C022


class L2000F_HSD01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'S',
         'description': 'xid=HSD01 data_ele=673',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['DY', 'FL', 'HS', 'MN', 'VS']}]}}
        datatype = common.D_673
        codes = ['DY', 'FL', 'HS', 'MN', 'VS']
        min_len = 2
        max_len = 2


class L2000F_HSD02(Element):
    """Service Unit Count"""
    class Schema:
        json = {'title': 'Service Unit Count',
         'usage': 'S',
         'description': 'xid=HSD02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_HSD03(Element):
    """Unit or Basis for Measurement Code"""
    class Schema:
        json = {'title': 'Unit or Basis for Measurement Code',
         'usage': 'S',
         'description': 'xid=HSD03 data_ele=355',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/355'}, {'enum': ['DA', 'MO', 'WK']}]}}
        datatype = common.D_355
        codes = ['DA', 'MO', 'WK']
        min_len = 2
        max_len = 2


class L2000F_HSD04(Element):
    """Sample Selection Modulus"""
    class Schema:
        json = {'title': 'Sample Selection Modulus',
         'usage': 'S',
         'description': 'xid=HSD04 data_ele=1167',
         'sequence': 4,
         'type': {'$ref': '#/$common/1167'}}
        datatype = common.D_1167
        min_len = 1
        max_len = 6


class L2000F_HSD05(Element):
    """Time Period Qualifier"""
    class Schema:
        json = {'title': 'Time Period Qualifier',
         'usage': 'S',
         'description': 'xid=HSD05 data_ele=615',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/615'},
                            {'enum': ['6', '7', '21', '26', '27', '34', '35']}]}}
        datatype = common.D_615
        codes = ['6', '7', '21', '26', '27', '34', '35']
        min_len = 1
        max_len = 2


class L2000F_HSD06(Element):
    """Period Count"""
    class Schema:
        json = {'title': 'Period Count',
         'usage': 'S',
         'description': 'xid=HSD06 data_ele=616',
         'sequence': 6,
         'type': {'$ref': '#/$common/616'}}
        datatype = common.D_616
        min_len = 1
        max_len = 3


class L2000F_HSD07(Element):
    """Ship, Delivery or Calendar Pattern Code"""
    class Schema:
        json = {'title': 'Ship, Delivery or Calendar Pattern Code',
         'usage': 'S',
         'description': 'xid=HSD07 data_ele=678',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/678'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                                      'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
                                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'SA', 'SB',
                                      'SC', 'SD', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ',
                                      'T', 'U', 'V', 'W', 'X', 'Y']}]}}
        datatype = common.D_678
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'SA', 'SB', 'SC', 'SD', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ', 'T', 'U', 'V', 'W', 'X', 'Y']
        min_len = 1
        max_len = 2


class L2000F_HSD08(Element):
    """Delivery Pattern Time Code"""
    class Schema:
        json = {'title': 'Delivery Pattern Time Code',
         'usage': 'S',
         'description': 'xid=HSD08 data_ele=679',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/679'},
                            {'enum': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Y']}]}}
        datatype = common.D_679
        codes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Y']
        min_len = 1
        max_len = 1


class L2000F_HSD(Segment):
    """Health Care Services Delivery"""
    class Schema:
        json = {'title': 'Health Care Services Delivery',
         'usage': 'S',
         'description': 'xid=HSD name=Health Care Services Delivery',
         'position': 90,
         'type': 'object',
         'properties': {'xid': {'literal': 'HSD'},
                        'hsd01': {'$ref': '#/$elements/L2000F_HSD01'},
                        'hsd02': {'$ref': '#/$elements/L2000F_HSD02'},
                        'hsd03': {'$ref': '#/$elements/L2000F_HSD03'},
                        'hsd04': {'$ref': '#/$elements/L2000F_HSD04'},
                        'hsd05': {'$ref': '#/$elements/L2000F_HSD05'},
                        'hsd06': {'$ref': '#/$elements/L2000F_HSD06'},
                        'hsd07': {'$ref': '#/$elements/L2000F_HSD07'},
                        'hsd08': {'$ref': '#/$elements/L2000F_HSD08'}}}
        segment_name = 'HSD'
    hsd01: L2000F_HSD01 | None
    hsd02: L2000F_HSD02 | None
    hsd03: L2000F_HSD03 | None
    hsd04: L2000F_HSD04 | None
    hsd05: L2000F_HSD05 | None
    hsd06: L2000F_HSD06 | None
    hsd07: L2000F_HSD07 | None
    hsd08: L2000F_HSD08 | None


class L2000F_CL101(Element):
    """Admission Type Code"""
    class Schema:
        json = {'title': 'Admission Type Code',
         'usage': 'S',
         'description': 'xid=CL101 data_ele=1315',
         'sequence': 1,
         'type': {'$ref': '#/$common/1315'}}
        datatype = common.D_1315
        min_len = 1
        max_len = 1


class L2000F_CL102(Element):
    """Admission Source Code"""
    class Schema:
        json = {'title': 'Admission Source Code',
         'usage': 'S',
         'description': 'xid=CL102 data_ele=1314',
         'sequence': 2,
         'type': {'$ref': '#/$common/1314'}}
        datatype = common.D_1314
        min_len = 1
        max_len = 1


class L2000F_CL103(Element):
    """Patient Status Code"""
    class Schema:
        json = {'title': 'Patient Status Code',
         'usage': 'S',
         'description': 'xid=CL103 data_ele=1352',
         'sequence': 3,
         'type': {'$ref': '#/$common/1352'}}
        datatype = common.D_1352
        min_len = 1
        max_len = 2


class L2000F_CL104(Element):
    """Nursing Home Residential Status Code"""
    class Schema:
        json = {'title': 'Nursing Home Residential Status Code',
         'usage': 'S',
         'description': 'xid=CL104 data_ele=1345',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1345'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9']}]}}
        datatype = common.D_1345
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        min_len = 1
        max_len = 1


class L2000F_CL1(Segment):
    """Institutional Claim Code"""
    class Schema:
        json = {'title': 'Institutional Claim Code',
         'usage': 'S',
         'description': 'xid=CL1 name=Institutional Claim Code',
         'position': 110,
         'type': 'object',
         'properties': {'xid': {'literal': 'CL1'},
                        'cl101': {'$ref': '#/$elements/L2000F_CL101'},
                        'cl102': {'$ref': '#/$elements/L2000F_CL102'},
                        'cl103': {'$ref': '#/$elements/L2000F_CL103'},
                        'cl104': {'$ref': '#/$elements/L2000F_CL104'}}}
        segment_name = 'CL1'
    cl101: L2000F_CL101 | None
    cl102: L2000F_CL102 | None
    cl103: L2000F_CL103 | None
    cl104: L2000F_CL104 | None


class L2000F_CR101(Element):
    """Unit or Basis for Measurement Code"""
    class Schema:
        json = {'title': 'Unit or Basis for Measurement Code',
         'usage': 'N',
         'description': 'xid=CR101 data_ele=355',
         'sequence': 1,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2000F_CR102(Element):
    """Weight"""
    class Schema:
        json = {'title': 'Weight',
         'usage': 'N',
         'description': 'xid=CR102 data_ele=81',
         'sequence': 2,
         'type': {'$ref': '#/$common/81'}}
        datatype = common.D_81
        min_len = 1
        max_len = 10


class L2000F_CR103(Element):
    """Ambulance Transport Code"""
    class Schema:
        json = {'title': 'Ambulance Transport Code',
         'usage': 'R',
         'description': 'xid=CR103 data_ele=1316',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1316'},
                            {'enum': ['I', 'R', 'T', 'X']}]}}
        datatype = common.D_1316
        codes = ['I', 'R', 'T', 'X']
        min_len = 1
        max_len = 1


class L2000F_CR104(Element):
    """Ambulance Transport Reason Code"""
    class Schema:
        json = {'title': 'Ambulance Transport Reason Code',
         'usage': 'N',
         'description': 'xid=CR104 data_ele=1317',
         'sequence': 4,
         'type': {'$ref': '#/$common/1317'}}
        datatype = common.D_1317
        min_len = 1
        max_len = 1


class L2000F_CR105(Element):
    """Unit or Basis for Measurement Code"""
    class Schema:
        json = {'title': 'Unit or Basis for Measurement Code',
         'usage': 'S',
         'description': 'xid=CR105 data_ele=355',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/355'}, {'enum': ['DH', 'DK']}]}}
        datatype = common.D_355
        codes = ['DH', 'DK']
        min_len = 2
        max_len = 2


class L2000F_CR106(Element):
    """Transport Distance"""
    class Schema:
        json = {'title': 'Transport Distance',
         'usage': 'S',
         'description': 'xid=CR106 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR107(Element):
    """Ambulance Trip Origin Address"""
    class Schema:
        json = {'title': 'Ambulance Trip Origin Address',
         'usage': 'S',
         'description': 'xid=CR107 data_ele=166',
         'sequence': 7,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2000F_CR108(Element):
    """Ambulance Trip Destination Address"""
    class Schema:
        json = {'title': 'Ambulance Trip Destination Address',
         'usage': 'S',
         'description': 'xid=CR108 data_ele=166',
         'sequence': 8,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2000F_CR109(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=CR109 data_ele=352',
         'sequence': 9,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_CR110(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=CR110 data_ele=352',
         'sequence': 10,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_CR1(Segment):
    """Ambulance Transport Information"""
    class Schema:
        json = {'title': 'Ambulance Transport Information',
         'usage': 'S',
         'description': 'xid=CR1 name=Ambulance Transport Information',
         'position': 120,
         'type': 'object',
         'properties': {'xid': {'literal': 'CR1'},
                        'cr103': {'$ref': '#/$elements/L2000F_CR103'},
                        'cr105': {'$ref': '#/$elements/L2000F_CR105'},
                        'cr106': {'$ref': '#/$elements/L2000F_CR106'},
                        'cr107': {'$ref': '#/$elements/L2000F_CR107'},
                        'cr108': {'$ref': '#/$elements/L2000F_CR108'}},
         'required': ['cr103']}
        segment_name = 'CR1'
    cr103: L2000F_CR103
    cr105: L2000F_CR105 | None
    cr106: L2000F_CR106 | None
    cr107: L2000F_CR107 | None
    cr108: L2000F_CR108 | None


class L2000F_CR201(Element):
    """Treatment Series Number"""
    class Schema:
        json = {'title': 'Treatment Series Number',
         'usage': 'S',
         'description': 'xid=CR201 data_ele=609',
         'sequence': 1,
         'type': {'$ref': '#/$common/609'}}
        datatype = common.D_609
        min_len = 1
        max_len = 9


class L2000F_CR202(Element):
    """Treatment Count"""
    class Schema:
        json = {'title': 'Treatment Count',
         'usage': 'S',
         'description': 'xid=CR202 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR203(Element):
    """Subluxation Level Code"""
    class Schema:
        json = {'title': 'Subluxation Level Code',
         'usage': 'S',
         'description': 'xid=CR203 data_ele=1367',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1367'},
                            {'enum': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO',
                                      'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA',
                                      'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5',
                                      'T6', 'T7', 'T8', 'T9']}]}}
        datatype = common.D_1367
        codes = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO', 'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA', 'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9']
        min_len = 2
        max_len = 3


class L2000F_CR204(Element):
    """Subluxation Level Code"""
    class Schema:
        json = {'title': 'Subluxation Level Code',
         'usage': 'S',
         'description': 'xid=CR204 data_ele=1367',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1367'},
                            {'enum': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO',
                                      'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA',
                                      'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5',
                                      'T6', 'T7', 'T8', 'T9']}]}}
        datatype = common.D_1367
        codes = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO', 'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA', 'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9']
        min_len = 2
        max_len = 3


class L2000F_CR205(Element):
    """Unit or Basis for Measurement Code"""
    class Schema:
        json = {'title': 'Unit or Basis for Measurement Code',
         'usage': 'S',
         'description': 'xid=CR205 data_ele=355',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/355'},
                            {'enum': ['DA', 'MO', 'WK', 'YR']}]}}
        datatype = common.D_355
        codes = ['DA', 'MO', 'WK', 'YR']
        min_len = 2
        max_len = 2


class L2000F_CR206(Element):
    """Treatment Period Count"""
    class Schema:
        json = {'title': 'Treatment Period Count',
         'usage': 'S',
         'description': 'xid=CR206 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR207(Element):
    """Monthly Treatment Count"""
    class Schema:
        json = {'title': 'Monthly Treatment Count',
         'usage': 'S',
         'description': 'xid=CR207 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR208(Element):
    """Nature of Condition Code"""
    class Schema:
        json = {'title': 'Nature of Condition Code',
         'usage': 'N',
         'description': 'xid=CR208 data_ele=1342',
         'sequence': 8,
         'type': {'$ref': '#/$common/1342'}}
        datatype = common.D_1342
        min_len = 1
        max_len = 1


class L2000F_CR209(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CR209 data_ele=1073',
         'sequence': 9,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2000F_CR210(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=CR210 data_ele=352',
         'sequence': 10,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_CR211(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=CR211 data_ele=352',
         'sequence': 11,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_CR212(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CR212 data_ele=1073',
         'sequence': 12,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2000F_CR2(Segment):
    """Spinal Manipulation Service Information"""
    class Schema:
        json = {'title': 'Spinal Manipulation Service Information',
         'usage': 'S',
         'description': 'xid=CR2 name=Spinal Manipulation Service Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'CR2'},
                        'cr201': {'$ref': '#/$elements/L2000F_CR201'},
                        'cr202': {'$ref': '#/$elements/L2000F_CR202'},
                        'cr203': {'$ref': '#/$elements/L2000F_CR203'},
                        'cr204': {'$ref': '#/$elements/L2000F_CR204'},
                        'cr205': {'$ref': '#/$elements/L2000F_CR205'},
                        'cr206': {'$ref': '#/$elements/L2000F_CR206'},
                        'cr207': {'$ref': '#/$elements/L2000F_CR207'}}}
        segment_name = 'CR2'
    cr201: L2000F_CR201 | None
    cr202: L2000F_CR202 | None
    cr203: L2000F_CR203 | None
    cr204: L2000F_CR204 | None
    cr205: L2000F_CR205 | None
    cr206: L2000F_CR206 | None
    cr207: L2000F_CR207 | None


class L2000F_CR501(Element):
    """Certification Type Code"""
    class Schema:
        json = {'title': 'Certification Type Code',
         'usage': 'N',
         'description': 'xid=CR501 data_ele=1322',
         'sequence': 1,
         'type': {'$ref': '#/$common/1322'}}
        datatype = common.D_1322
        min_len = 1
        max_len = 1


class L2000F_CR502(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=CR502 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR503(Element):
    """Oxygen Equipment Type Code"""
    class Schema:
        json = {'title': 'Oxygen Equipment Type Code',
         'usage': 'S',
         'description': 'xid=CR503 data_ele=1348',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1348'},
                            {'enum': ['A', 'B', 'C', 'D', 'E', 'O']}]}}
        datatype = common.D_1348
        codes = ['A', 'B', 'C', 'D', 'E', 'O']
        min_len = 1
        max_len = 1


class L2000F_CR504(Element):
    """Oxygen Equipment Type Code"""
    class Schema:
        json = {'title': 'Oxygen Equipment Type Code',
         'usage': 'S',
         'description': 'xid=CR504 data_ele=1348',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1348'},
                            {'enum': ['A', 'B', 'C', 'D', 'E', 'O']}]}}
        datatype = common.D_1348
        codes = ['A', 'B', 'C', 'D', 'E', 'O']
        min_len = 1
        max_len = 1


class L2000F_CR505(Element):
    """Equipment Reason Description"""
    class Schema:
        json = {'title': 'Equipment Reason Description',
         'usage': 'S',
         'description': 'xid=CR505 data_ele=352',
         'sequence': 5,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_CR506(Element):
    """Oxygen Flow Rate"""
    class Schema:
        json = {'title': 'Oxygen Flow Rate',
         'usage': 'R',
         'description': 'xid=CR506 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR507(Element):
    """Daily Oxygen Use Count"""
    class Schema:
        json = {'title': 'Daily Oxygen Use Count',
         'usage': 'S',
         'description': 'xid=CR507 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR508(Element):
    """Oxygen Use Period Hour Count"""
    class Schema:
        json = {'title': 'Oxygen Use Period Hour Count',
         'usage': 'S',
         'description': 'xid=CR508 data_ele=380',
         'sequence': 8,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR509(Element):
    """Respiratory Therapist Order Text"""
    class Schema:
        json = {'title': 'Respiratory Therapist Order Text',
         'usage': 'S',
         'description': 'xid=CR509 data_ele=352',
         'sequence': 9,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_CR510(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=CR510 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR511(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=CR511 data_ele=380',
         'sequence': 11,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR512(Element):
    """Oxygen Test Condition Code"""
    class Schema:
        json = {'title': 'Oxygen Test Condition Code',
         'usage': 'N',
         'description': 'xid=CR512 data_ele=1349',
         'sequence': 12,
         'type': {'$ref': '#/$common/1349'}}
        datatype = common.D_1349
        min_len = 1
        max_len = 1


class L2000F_CR513(Element):
    """Oxygen Test Findings Code"""
    class Schema:
        json = {'title': 'Oxygen Test Findings Code',
         'usage': 'N',
         'description': 'xid=CR513 data_ele=1350',
         'sequence': 13,
         'type': {'$ref': '#/$common/1350'}}
        datatype = common.D_1350
        min_len = 1
        max_len = 1


class L2000F_CR514(Element):
    """Oxygen Test Findings Code"""
    class Schema:
        json = {'title': 'Oxygen Test Findings Code',
         'usage': 'N',
         'description': 'xid=CR514 data_ele=1350',
         'sequence': 14,
         'type': {'$ref': '#/$common/1350'}}
        datatype = common.D_1350
        min_len = 1
        max_len = 1


class L2000F_CR515(Element):
    """Oxygen Test Findings Code"""
    class Schema:
        json = {'title': 'Oxygen Test Findings Code',
         'usage': 'N',
         'description': 'xid=CR515 data_ele=1350',
         'sequence': 15,
         'type': {'$ref': '#/$common/1350'}}
        datatype = common.D_1350
        min_len = 1
        max_len = 1


class L2000F_CR516(Element):
    """Portable Oxygen System Flow Rate"""
    class Schema:
        json = {'title': 'Portable Oxygen System Flow Rate',
         'usage': 'S',
         'description': 'xid=CR516 data_ele=380',
         'sequence': 16,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000F_CR517(Element):
    """Oxygen Delivery System Code"""
    class Schema:
        json = {'title': 'Oxygen Delivery System Code',
         'usage': 'R',
         'description': 'xid=CR517 data_ele=1382',
         'sequence': 17,
         'type': {'allOf': [{'$ref': '#/$common/1382'},
                            {'enum': ['A', 'B', 'C', 'D', 'E']}]}}
        datatype = common.D_1382
        codes = ['A', 'B', 'C', 'D', 'E']
        min_len = 1
        max_len = 1


class L2000F_CR518(Element):
    """Oxygen Equipment Type Code"""
    class Schema:
        json = {'title': 'Oxygen Equipment Type Code',
         'usage': 'S',
         'description': 'xid=CR518 data_ele=1348',
         'sequence': 18,
         'type': {'allOf': [{'$ref': '#/$common/1348'},
                            {'enum': ['A', 'B', 'C', 'D', 'E', 'O']}]}}
        datatype = common.D_1348
        codes = ['A', 'B', 'C', 'D', 'E', 'O']
        min_len = 1
        max_len = 1


class L2000F_CR5(Segment):
    """Home Oxygen Therapy Information"""
    class Schema:
        json = {'title': 'Home Oxygen Therapy Information',
         'usage': 'S',
         'description': 'xid=CR5 name=Home Oxygen Therapy Information',
         'position': 140,
         'type': 'object',
         'properties': {'xid': {'literal': 'CR5'},
                        'cr503': {'$ref': '#/$elements/L2000F_CR503'},
                        'cr504': {'$ref': '#/$elements/L2000F_CR504'},
                        'cr505': {'$ref': '#/$elements/L2000F_CR505'},
                        'cr506': {'$ref': '#/$elements/L2000F_CR506'},
                        'cr507': {'$ref': '#/$elements/L2000F_CR507'},
                        'cr508': {'$ref': '#/$elements/L2000F_CR508'},
                        'cr509': {'$ref': '#/$elements/L2000F_CR509'},
                        'cr516': {'$ref': '#/$elements/L2000F_CR516'},
                        'cr517': {'$ref': '#/$elements/L2000F_CR517'},
                        'cr518': {'$ref': '#/$elements/L2000F_CR518'}},
         'required': ['cr506', 'cr517']}
        segment_name = 'CR5'
    cr503: L2000F_CR503 | None
    cr504: L2000F_CR504 | None
    cr505: L2000F_CR505 | None
    cr506: L2000F_CR506
    cr507: L2000F_CR507 | None
    cr508: L2000F_CR508 | None
    cr509: L2000F_CR509 | None
    cr516: L2000F_CR516 | None
    cr517: L2000F_CR517
    cr518: L2000F_CR518 | None


class L2000F_CR601(Element):
    """Prognosis Code"""
    class Schema:
        json = {'title': 'Prognosis Code',
         'usage': 'R',
         'description': 'xid=CR601 data_ele=923',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/923'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8']}]}}
        datatype = common.D_923
        codes = ['1', '2', '3', '4', '5', '6', '7', '8']
        min_len = 1
        max_len = 1


class L2000F_CR602(Element):
    """Service From Date"""
    class Schema:
        json = {'title': 'Service From Date',
         'usage': 'R',
         'description': 'xid=CR602 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR603(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=CR603 data_ele=1250',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['RD8']}]}}
        datatype = common.D_1250
        codes = ['RD8']
        min_len = 2
        max_len = 3


class L2000F_CR604(Element):
    """Home Health Certification Period"""
    class Schema:
        json = {'title': 'Home Health Certification Period',
         'usage': 'S',
         'description': 'xid=CR604 data_ele=1251',
         'sequence': 4,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_CR605(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR605 data_ele=373',
         'sequence': 5,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR606(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CR606 data_ele=1073',
         'sequence': 6,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2000F_CR607(Element):
    """Medicare Coverage Indicator"""
    class Schema:
        json = {'title': 'Medicare Coverage Indicator',
         'usage': 'R',
         'description': 'xid=CR607 data_ele=1073',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'U', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'U', 'Y']
        min_len = 1
        max_len = 1


class L2000F_CR608(Element):
    """Certification Type Code"""
    class Schema:
        json = {'title': 'Certification Type Code',
         'usage': 'R',
         'description': 'xid=CR608 data_ele=1322',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/1322'},
                            {'enum': ['1', '2', '3', '4', 'I', 'R', 'S']}]}}
        datatype = common.D_1322
        codes = ['1', '2', '3', '4', 'I', 'R', 'S']
        min_len = 1
        max_len = 1


class L2000F_CR609(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR609 data_ele=373',
         'sequence': 9,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR610(Element):
    """Product/Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product/Service ID Qualifier',
         'usage': 'N',
         'description': 'xid=CR610 data_ele=235',
         'sequence': 10,
         'type': {'$ref': '#/$common/235'}}
        datatype = common.D_235
        min_len = 2
        max_len = 2


class L2000F_CR611(Element):
    """Medical Code Value"""
    class Schema:
        json = {'title': 'Medical Code Value',
         'usage': 'N',
         'description': 'xid=CR611 data_ele=1137',
         'sequence': 11,
         'type': {'$ref': '#/$common/1137'}}
        datatype = common.D_1137
        min_len = 1
        max_len = 15


class L2000F_CR612(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR612 data_ele=373',
         'sequence': 12,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR613(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR613 data_ele=373',
         'sequence': 13,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR614(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR614 data_ele=373',
         'sequence': 14,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR615(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=CR615 data_ele=1250',
         'sequence': 15,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2000F_CR616(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=CR616 data_ele=1251',
         'sequence': 16,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000F_CR617(Element):
    """Patient Location Code"""
    class Schema:
        json = {'title': 'Patient Location Code',
         'usage': 'N',
         'description': 'xid=CR617 data_ele=1384',
         'sequence': 17,
         'type': {'$ref': '#/$common/1384'}}
        datatype = common.D_1384
        min_len = 1
        max_len = 1


class L2000F_CR618(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR618 data_ele=373',
         'sequence': 18,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR619(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR619 data_ele=373',
         'sequence': 19,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR620(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR620 data_ele=373',
         'sequence': 20,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR621(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CR621 data_ele=373',
         'sequence': 21,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000F_CR6(Segment):
    """Home Health Care Information"""
    class Schema:
        json = {'title': 'Home Health Care Information',
         'usage': 'S',
         'description': 'xid=CR6 name=Home Health Care Information',
         'position': 150,
         'type': 'object',
         'properties': {'xid': {'literal': 'CR6'},
                        'cr601': {'$ref': '#/$elements/L2000F_CR601'},
                        'cr602': {'$ref': '#/$elements/L2000F_CR602'},
                        'cr603': {'$ref': '#/$elements/L2000F_CR603'},
                        'cr604': {'$ref': '#/$elements/L2000F_CR604'},
                        'cr607': {'$ref': '#/$elements/L2000F_CR607'},
                        'cr608': {'$ref': '#/$elements/L2000F_CR608'}},
         'required': ['cr601', 'cr602', 'cr607', 'cr608']}
        segment_name = 'CR6'
    cr601: L2000F_CR601
    cr602: L2000F_CR602
    cr603: L2000F_CR603 | None
    cr604: L2000F_CR604 | None
    cr607: L2000F_CR607
    cr608: L2000F_CR608


class L2000F_PWK01(Element):
    """Attachment Report Type Code"""
    class Schema:
        json = {'title': 'Attachment Report Type Code',
         'usage': 'R',
         'description': 'xid=PWK01 data_ele=755',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/755'},
                            {'enum': ['03', '04', '05', '06', '07', '08', '09', '10',
                                      '11', '13', '15', '21', '48', '55', '59', '77',
                                      'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR',
                                      'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG',
                                      'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA',
                                      'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4',
                                      'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY',
                                      'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG',
                                      'V5', 'XP']}]}}
        datatype = common.D_755
        codes = ['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', '48', '55', '59', '77', 'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR', 'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4', 'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP']
        min_len = 2
        max_len = 2


class L2000F_PWK02(Element):
    """Attachment Transmission Code"""
    class Schema:
        json = {'title': 'Attachment Transmission Code',
         'usage': 'R',
         'description': 'xid=PWK02 data_ele=756',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/756'},
                            {'enum': ['BM', 'EL', 'EM', 'FX', 'VO']}]}}
        datatype = common.D_756
        codes = ['BM', 'EL', 'EM', 'FX', 'VO']
        min_len = 1
        max_len = 2


class L2000F_PWK03(Element):
    """Report Copies Needed"""
    class Schema:
        json = {'title': 'Report Copies Needed',
         'usage': 'N',
         'description': 'xid=PWK03 data_ele=757',
         'sequence': 3,
         'type': {'$ref': '#/$common/757'}}
        datatype = common.D_757
        min_len = 1
        max_len = 2


class L2000F_PWK04(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=PWK04 data_ele=98',
         'sequence': 4,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2000F_PWK05(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=PWK05 data_ele=66',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['AC']}]}}
        datatype = common.D_66
        codes = ['AC']
        min_len = 1
        max_len = 2


class L2000F_PWK06(Element):
    """Attachment Control Number"""
    class Schema:
        json = {'title': 'Attachment Control Number',
         'usage': 'S',
         'description': 'xid=PWK06 data_ele=67',
         'sequence': 6,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2000F_PWK07(Element):
    """Attachment Description"""
    class Schema:
        json = {'title': 'Attachment Description',
         'usage': 'S',
         'description': 'xid=PWK07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2000F_C002(Composite):
    class Schema:
        json = {'title': 'Actions Indicated',
         'usage': 'N',
         'description': 'xid=None name=Actions Indicated refdes= data_ele=C002',
         'sequence': 8,
         'syntax': []}


class L2000F_PWK09(Element):
    """Request Category Code"""
    class Schema:
        json = {'title': 'Request Category Code',
         'usage': 'N',
         'description': 'xid=PWK09 data_ele=1525',
         'sequence': 9,
         'type': {'$ref': '#/$common/1525'}}
        datatype = common.D_1525
        min_len = 1
        max_len = 2


class L2000F_PWK(Segment):
    """Additional Service Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Service Information',
                   'usage': 'S',
                   'description': 'xid=PWK name=Additional Service Information',
                   'position': 155,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PWK'},
                                  'pwk01': {'$ref': '#/$elements/L2000F_PWK01'},
                                  'pwk02': {'$ref': '#/$elements/L2000F_PWK02'},
                                  'pwk05': {'$ref': '#/$elements/L2000F_PWK05'},
                                  'pwk06': {'$ref': '#/$elements/L2000F_PWK06'},
                                  'pwk07': {'$ref': '#/$elements/L2000F_PWK07'}},
                   'required': ['pwk01', 'pwk02']},
         'maxItems': 10}
        segment_name = 'PWK'
    pwk01: L2000F_PWK01
    pwk02: L2000F_PWK02
    pwk05: L2000F_PWK05 | None
    pwk06: L2000F_PWK06 | None
    pwk07: L2000F_PWK07 | None


class L2000F_MSG01(Element):
    """Free Form Message Text"""
    class Schema:
        json = {'title': 'Free Form Message Text',
         'usage': 'R',
         'description': 'xid=MSG01 data_ele=933',
         'sequence': 1,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2000F_MSG02(Element):
    """Printer Carriage Control Code"""
    class Schema:
        json = {'title': 'Printer Carriage Control Code',
         'usage': 'N',
         'description': 'xid=MSG02 data_ele=934',
         'sequence': 2,
         'type': {'$ref': '#/$common/934'}}
        datatype = common.D_934
        min_len = 2
        max_len = 2


class L2000F_MSG03(Element):
    """Number"""
    class Schema:
        json = {'title': 'Number',
         'usage': 'N',
         'description': 'xid=MSG03 data_ele=1470',
         'sequence': 3,
         'type': {'$ref': '#/$common/1470'}}
        datatype = common.D_1470
        min_len = 1
        max_len = 9


class L2000F_MSG(Segment):
    """Message Text"""
    class Schema:
        json = {'title': 'Message Text',
         'usage': 'S',
         'description': 'xid=MSG name=Message Text',
         'position': 160,
         'type': 'object',
         'properties': {'xid': {'literal': 'MSG'},
                        'msg01': {'$ref': '#/$elements/L2000F_MSG01'}},
         'required': ['msg01']}
        segment_name = 'MSG'
    msg01: L2000F_MSG01


class L2010F_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['1P', '2B', 'ABG', 'FA', 'PR', 'X3']}]}}
        datatype = common.D_98
        codes = ['1P', '2B', 'ABG', 'FA', 'PR', 'X3']
        min_len = 2
        max_len = 3


class L2010F_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2010F_NM103(Element):
    """Response Contact Last or Organization Name"""
    class Schema:
        json = {'title': 'Response Contact Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010F_NM104(Element):
    """Response Contact First Name"""
    class Schema:
        json = {'title': 'Response Contact First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010F_NM105(Element):
    """Response Contact Middle Name"""
    class Schema:
        json = {'title': 'Response Contact Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010F_NM106(Element):
    """Name Prefix"""
    class Schema:
        json = {'title': 'Name Prefix',
         'usage': 'N',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2010F_NM107(Element):
    """Response Contact Name Suffix"""
    class Schema:
        json = {'title': 'Response Contact Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010F_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'PI', 'XV', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'PI', 'XV', 'XX']
        min_len = 1
        max_len = 2


class L2010F_NM109(Element):
    """Response Contact Identifier"""
    class Schema:
        json = {'title': 'Response Contact Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010F_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2010F_NM111(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=NM111 data_ele=98',
         'sequence': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2010F_NM1(Segment):
    """Additional Service Information Contact Name"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Service Information Contact Name',
                   'usage': 'S',
                   'description': 'xid=NM1 name=Additional Service Information Contact '
                                  'Name',
                   'position': 170,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'NM1'},
                                  'nm101': {'$ref': '#/$elements/L2010F_NM101'},
                                  'nm102': {'$ref': '#/$elements/L2010F_NM102'},
                                  'nm103': {'$ref': '#/$elements/L2010F_NM103'},
                                  'nm104': {'$ref': '#/$elements/L2010F_NM104'},
                                  'nm105': {'$ref': '#/$elements/L2010F_NM105'},
                                  'nm107': {'$ref': '#/$elements/L2010F_NM107'},
                                  'nm108': {'$ref': '#/$elements/L2010F_NM108'},
                                  'nm109': {'$ref': '#/$elements/L2010F_NM109'}},
                   'required': ['nm101', 'nm102']}}
        segment_name = 'NM1'
    nm101: L2010F_NM101
    nm102: L2010F_NM102
    nm103: L2010F_NM103 | None
    nm104: L2010F_NM104 | None
    nm105: L2010F_NM105 | None
    nm107: L2010F_NM107 | None
    nm108: L2010F_NM108 | None
    nm109: L2010F_NM109 | None


class L2010F_N301(Element):
    """Response Contact Address Line"""
    class Schema:
        json = {'title': 'Response Contact Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010F_N302(Element):
    """Response Contact Address Line"""
    class Schema:
        json = {'title': 'Response Contact Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010F_N3(Segment):
    """Additional Service Information Contact Address"""
    class Schema:
        json = {'title': 'Additional Service Information Contact Address',
         'usage': 'S',
         'description': 'xid=N3 name=Additional Service Information Contact Address',
         'position': 200,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010F_N301'},
                        'n302': {'$ref': '#/$elements/L2010F_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010F_N301
    n302: L2010F_N302 | None


class L2010F_N401(Element):
    """Response Contact City Name"""
    class Schema:
        json = {'title': 'Response Contact City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010F_N402(Element):
    """Response Contact State or Province Code"""
    class Schema:
        json = {'title': 'Response Contact State or Province Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010F_N403(Element):
    """Response Contact Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Response Contact Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010F_N404(Element):
    """Response Contact Country Code"""
    class Schema:
        json = {'title': 'Response Contact Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010F_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['B1', 'DP']}]}}
        datatype = common.D_309
        codes = ['B1', 'DP']
        min_len = 1
        max_len = 2


class L2010F_N406(Element):
    """Response Contact Specific Location"""
    class Schema:
        json = {'title': 'Response Contact Specific Location',
         'usage': 'S',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2010F_N4(Segment):
    """Additional Service Information Contact City/State/Zip Code"""
    class Schema:
        json = {'title': 'Additional Service Information Contact City/State/Zip Code',
         'usage': 'S',
         'description': 'xid=N4 name=Additional Service Information Contact '
                        'City/State/Zip Code',
         'position': 210,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010F_N401'},
                        'n402': {'$ref': '#/$elements/L2010F_N402'},
                        'n403': {'$ref': '#/$elements/L2010F_N403'},
                        'n404': {'$ref': '#/$elements/L2010F_N404'},
                        'n405': {'$ref': '#/$elements/L2010F_N405'},
                        'n406': {'$ref': '#/$elements/L2010F_N406'}}}
        segment_name = 'N4'
    n401: L2010F_N401 | None
    n402: L2010F_N402 | None
    n403: L2010F_N403 | None
    n404: L2010F_N404 | None
    n405: L2010F_N405 | None
    n406: L2010F_N406 | None


class L2010F_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IC']}]}}
        datatype = common.D_366
        codes = ['IC']
        min_len = 2
        max_len = 2


class L2010F_PER02(Element):
    """Response Contact Name"""
    class Schema:
        json = {'title': 'Response Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2010F_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010F_PER04(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010F_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010F_PER06(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010F_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2010F_PER08(Element):
    """Response Contact Communication Number"""
    class Schema:
        json = {'title': 'Response Contact Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2010F_PER09(Element):
    """Contact Inquiry Reference"""
    class Schema:
        json = {'title': 'Contact Inquiry Reference',
         'usage': 'N',
         'description': 'xid=PER09 data_ele=443',
         'sequence': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L2010F_PER(Segment):
    """Additional Service Information Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Service Information Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Additional Service Information Contact '
                                  'Information',
                   'position': 220,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2010F_PER01'},
                                  'per02': {'$ref': '#/$elements/L2010F_PER02'},
                                  'per03': {'$ref': '#/$elements/L2010F_PER03'},
                                  'per04': {'$ref': '#/$elements/L2010F_PER04'},
                                  'per05': {'$ref': '#/$elements/L2010F_PER05'},
                                  'per06': {'$ref': '#/$elements/L2010F_PER06'},
                                  'per07': {'$ref': '#/$elements/L2010F_PER07'},
                                  'per08': {'$ref': '#/$elements/L2010F_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2010F_PER01
    per02: L2010F_PER02 | None
    per03: L2010F_PER03 | None
    per04: L2010F_PER04 | None
    per05: L2010F_PER05 | None
    per06: L2010F_PER06 | None
    per07: L2010F_PER07 | None
    per08: L2010F_PER08 | None


class L2010F(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Service Information Contact Name',
                   'usage': 'S',
                   'description': 'xid=2010F name=Additional Service Information '
                                  'Contact Name type=None',
                   'position': 170,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010F_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010F_N3'},
                                  'n4': {'$ref': '#/$segments/L2010F_N4'},
                                  'per': {'$ref': '#/$segments/L2010F_PER'}}},
         'maxItems': 1}
    nm1: list[L2010F_NM1] | None
    n3: L2010F_N3 | None
    n4: L2010F_N4 | None
    per: list[L2010F_PER] | None


class L2000F(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Level',
                   'usage': 'R',
                   'description': 'xid=2000F name=Service Level type=None',
                   'position': 180,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000F_HL'},
                                  'trn': {'$ref': '#/$segments/L2000F_TRN'},
                                  'aaa': {'$ref': '#/$segments/L2000F_AAA'},
                                  'um': {'$ref': '#/$segments/L2000F_UM'},
                                  'hcr': {'$ref': '#/$segments/L2000F_HCR'},
                                  'ref': {'$ref': '#/$segments/L2000F_REF'},
                                  'dtp': {'$ref': '#/$segments/L2000F_DTP'},
                                  'hi': {'$ref': '#/$segments/L2000F_HI'},
                                  'hsd': {'$ref': '#/$segments/L2000F_HSD'},
                                  'cl1': {'$ref': '#/$segments/L2000F_CL1'},
                                  'cr1': {'$ref': '#/$segments/L2000F_CR1'},
                                  'cr2': {'$ref': '#/$segments/L2000F_CR2'},
                                  'cr5': {'$ref': '#/$segments/L2000F_CR5'},
                                  'cr6': {'$ref': '#/$segments/L2000F_CR6'},
                                  'pwk': {'$ref': '#/$segments/L2000F_PWK'},
                                  'msg': {'$ref': '#/$segments/L2000F_MSG'},
                                  'l2010f': {'$ref': '#/$segments/L2010F'}},
                   'required': ['hl', 'um']}}
    hl: L2000F_HL
    trn: list[L2000F_TRN] | None
    aaa: list[L2000F_AAA] | None
    um: L2000F_UM
    hcr: L2000F_HCR | None
    ref: L2000F_REF | None
    dtp: L2000F_DTP | None
    dtp: L2000F_DTP | None
    dtp: L2000F_DTP | None
    dtp: L2000F_DTP | None
    dtp: L2000F_DTP | None
    dtp: L2000F_DTP | None
    dtp: L2000F_DTP | None
    hi: L2000F_HI | None
    hsd: L2000F_HSD | None
    cl1: L2000F_CL1 | None
    cr1: L2000F_CR1 | None
    cr2: L2000F_CR2 | None
    cr5: L2000F_CR5 | None
    cr6: L2000F_CR6 | None
    pwk: list[L2000F_PWK] | None
    msg: L2000F_MSG | None
    l2010f: list[L2010F] | None


class L2000E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Provider Level',
                   'usage': 'R',
                   'description': 'xid=2000E name=Service Provider Level type=None',
                   'position': 180,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000E_HL'},
                                  'msg': {'$ref': '#/$segments/L2000E_MSG'},
                                  'l2010e': {'$ref': '#/$segments/L2010E'},
                                  'l2000f': {'$ref': '#/$segments/L2000F'}},
                   'required': ['hl', 'l2010e', 'l2000f']}}
    hl: L2000E_HL
    msg: L2000E_MSG | None
    l2010e: list[L2010E]
    l2000f: list[L2000F]


class L2000D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Level',
                   'usage': 'S',
                   'description': 'xid=2000D name=Dependent Level type=None',
                   'position': 180,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000D_HL'},
                                  'trn': {'$ref': '#/$segments/L2000D_TRN'},
                                  'aaa': {'$ref': '#/$segments/L2000D_AAA'},
                                  'dtp': {'$ref': '#/$segments/L2000D_DTP'},
                                  'hi': {'$ref': '#/$segments/L2000D_HI'},
                                  'pwk': {'$ref': '#/$segments/L2000D_PWK'},
                                  'l2010da': {'$ref': '#/$segments/L2010DA'},
                                  'l2010db': {'$ref': '#/$segments/L2010DB'},
                                  'l2000e': {'$ref': '#/$segments/L2000E'}},
                   'required': ['hl', 'l2010da', 'l2000e']},
         'maxItems': 1}
    hl: L2000D_HL
    trn: list[L2000D_TRN] | None
    aaa: list[L2000D_AAA] | None
    dtp: L2000D_DTP | None
    dtp: L2000D_DTP | None
    dtp: L2000D_DTP | None
    dtp: L2000D_DTP | None
    hi: L2000D_HI | None
    pwk: list[L2000D_PWK] | None
    l2010da: list[L2010DA]
    l2010db: list[L2010DB] | None
    l2000e: list[L2000E]


class L2000C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Level',
                   'usage': 'R',
                   'description': 'xid=2000C name=Subscriber Level type=None',
                   'position': 180,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000C_HL'},
                                  'trn': {'$ref': '#/$segments/L2000C_TRN'},
                                  'aaa': {'$ref': '#/$segments/L2000C_AAA'},
                                  'dtp': {'$ref': '#/$segments/L2000C_DTP'},
                                  'hi': {'$ref': '#/$segments/L2000C_HI'},
                                  'pwk': {'$ref': '#/$segments/L2000C_PWK'},
                                  'l2010ca': {'$ref': '#/$segments/L2010CA'},
                                  'l2010cb': {'$ref': '#/$segments/L2010CB'},
                                  'l2000d': {'$ref': '#/$segments/L2000D'}},
                   'required': ['hl', 'l2010ca']},
         'maxItems': 1}
    hl: L2000C_HL
    trn: list[L2000C_TRN] | None
    aaa: list[L2000C_AAA] | None
    dtp: L2000C_DTP | None
    dtp: L2000C_DTP | None
    dtp: L2000C_DTP | None
    dtp: L2000C_DTP | None
    hi: L2000C_HI | None
    pwk: list[L2000C_PWK] | None
    l2010ca: list[L2010CA]
    l2010cb: list[L2010CB] | None
    l2000d: list[L2000D] | None


class L2000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Requester Level',
                   'usage': 'R',
                   'description': 'xid=2000B name=Requester Level type=None',
                   'position': 180,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000B_HL'},
                                  'l2010b': {'$ref': '#/$segments/L2010B'},
                                  'l2000c': {'$ref': '#/$segments/L2000C'}},
                   'required': ['hl', 'l2010b', 'l2000c']},
         'maxItems': 1}
    hl: L2000B_HL
    l2010b: list[L2010B]
    l2000c: list[L2000C]


class L2000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Utilization Management Organization (UMO) Level',
                   'usage': 'R',
                   'description': 'xid=2000A name=Utilization Management Organization '
                                  '(UMO) Level type=None',
                   'position': 10,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000A_HL'},
                                  'aaa': {'$ref': '#/$segments/L2000A_AAA'},
                                  'l2010a': {'$ref': '#/$segments/L2010A'},
                                  'l2000b': {'$ref': '#/$segments/L2000B'}},
                   'required': ['hl', 'l2010a', 'l2000b']},
         'maxItems': 1}
    hl: L2000A_HL
    aaa: list[L2000A_AAA] | None
    l2010a: list[L2010A]
    l2000b: list[L2000B]


class DETAIL(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 2 - Detail',
                   'usage': 'S',
                   'description': 'xid=DETAIL name=Table 2 - Detail type=wrapper',
                   'position': 20,
                   'type': 'object',
                   'properties': {'l2000a': {'$ref': '#/$segments/L2000A'}},
                   'required': ['l2000a']}}
    l2000a: list[L2000A]


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 3 - Footer',
                   'usage': 'N',
                   'description': 'xid=FOOTER name=Table 3 - Footer type=wrapper',
                   'position': 30},
         'maxItems': 1}


class ST_LOOP_SE01(Element):
    """Transaction Segment Count"""
    class Schema:
        json = {'title': 'Transaction Segment Count',
         'usage': 'R',
         'description': 'xid=SE01 data_ele=96',
         'sequence': 1,
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
         'sequence': 2,
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
         'position': 280,
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
                                  'se': {'$ref': '#/$segments/ST_LOOP_SE'}},
                   'required': ['st', 'header', 'se']}}
    st: ST_LOOP_ST
    header: list[HEADER]
    detail: list[DETAIL] | None
    se: ST_LOOP_SE


class GS_LOOP_GE01(Element):
    """Number of Transaction Sets Included"""
    class Schema:
        json = {'title': 'Number of Transaction Sets Included',
         'usage': 'R',
         'description': 'xid=GE01 data_ele=97',
         'sequence': 1,
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
         'sequence': 2,
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
         'sequence': 1,
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
         'sequence': 2,
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
         'sequence': 3,
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
         'sequence': 4,
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
         'sequence': 5,
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
         'sequence': 1,
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
         'sequence': 2,
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


class MSG278(Message):
    """HIPAA Health Care Services Review: Response X094A1-278"""
    class Schema:
        json = {'title': 'HIPAA Health Care Services Review: Response X094A1-278',
         'description': 'xid=278 name=HIPAA Health Care Services Review: Response '
                        'X094A1-278',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
