"""
271.4010.X092.A1
Created 2023-03-25 09:22:27.908888
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
        min_len = 3
        max_len = 3


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
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['HB']}]}}
        datatype = common.D_479
        codes = ['HB']
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
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['004010X092A1']}]}}
        datatype = common.D_480
        codes = ['004010X092A1']
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
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['271']}]}}
        datatype = common.D_143
        codes = ['271']
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
         'type': {'allOf': [{'$ref': '#/$common/1005'}, {'enum': ['0022']}]}}
        datatype = common.D_1005
        codes = ['0022']
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
         'usage': 'S',
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
         'usage': 'N',
         'description': 'xid=BHT06 data_ele=640',
         'sequence': 6,
         'type': {'$ref': '#/$common/640'}}
        datatype = common.D_640
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
                        'bht05': {'$ref': '#/$elements/HEADER_BHT05'}},
         'required': ['bht01', 'bht02', 'bht04', 'bht05']}
        segment_name = 'BHT'
    bht01: HEADER_BHT01
    bht02: HEADER_BHT02
    bht03: HEADER_BHT03 | None
    bht04: HEADER_BHT04
    bht05: HEADER_BHT05


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
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['0', '1']}]}}
        datatype = common.D_736
        codes = ['0', '1']
        min_len = 1
        max_len = 1


class L2000A_HL(Segment):
    """Information Source Level"""
    class Schema:
        json = {'title': 'Information Source Level',
         'usage': 'R',
         'description': 'xid=HL name=Information Source Level',
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
         'type': {'allOf': [{'$ref': '#/$common/889'},
                            {'enum': ['C', 'N', 'P', 'R', 'S', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'P', 'R', 'S', 'Y']
        min_len = 1
        max_len = 1


class L2000A_AAA(Segment):
    """Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Request Validation',
                   'position': 25,
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


class L2100A_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['2B', '36', 'GP', 'P5', 'PR']}]}}
        datatype = common.D_98
        codes = ['2B', '36', 'GP', 'P5', 'PR']
        min_len = 2
        max_len = 3


class L2100A_NM102(Element):
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


class L2100A_NM103(Element):
    """Information Source Last or Organization Name"""
    class Schema:
        json = {'title': 'Information Source Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100A_NM104(Element):
    """Information Source First Name"""
    class Schema:
        json = {'title': 'Information Source First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100A_NM105(Element):
    """Information Source Middle Name"""
    class Schema:
        json = {'title': 'Information Source Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100A_NM106(Element):
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


class L2100A_NM107(Element):
    """Information Source Name Suffix"""
    class Schema:
        json = {'title': 'Information Source Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '46', 'FI', 'NI', 'PI', 'XV', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '46', 'FI', 'NI', 'PI', 'XV', 'XX']
        min_len = 1
        max_len = 2


class L2100A_NM109(Element):
    """Information Source Primary Identifier"""
    class Schema:
        json = {'title': 'Information Source Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100A_NM110(Element):
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


class L2100A_NM111(Element):
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


class L2100A_NM1(Segment):
    """Information Source Name"""
    class Schema:
        json = {'title': 'Information Source Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Information Source Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100A_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100A_NM101
    nm102: L2100A_NM102
    nm103: L2100A_NM103 | None
    nm104: L2100A_NM104 | None
    nm105: L2100A_NM105 | None
    nm107: L2100A_NM107 | None
    nm108: L2100A_NM108
    nm109: L2100A_NM109


class L2100A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['18', '55']}]}}
        datatype = common.D_128
        codes = ['18', '55']
        min_len = 2
        max_len = 3


class L2100A_REF02(Element):
    """Information Source Additional Plan Identifier"""
    class Schema:
        json = {'title': 'Information Source Additional Plan Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2100A_REF03(Element):
    """Plan Name"""
    class Schema:
        json = {'title': 'Plan Name',
         'usage': 'S',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100A_REF(Segment):
    """Information Source Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Source Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Information Source Additional '
                                  'Identification',
                   'position': 40,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100A_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2100A_REF03'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2100A_REF01
    ref02: L2100A_REF02
    ref03: L2100A_REF03 | None


class L2100A_PER01(Element):
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


class L2100A_PER02(Element):
    """Information Source Contact Name"""
    class Schema:
        json = {'title': 'Information Source Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100A_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100A_PER04(Element):
    """Information Source Communication Number"""
    class Schema:
        json = {'title': 'Information Source Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100A_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100A_PER06(Element):
    """Information Source Communication Number"""
    class Schema:
        json = {'title': 'Information Source Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100A_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100A_PER08(Element):
    """Information Source Communication Number"""
    class Schema:
        json = {'title': 'Information Source Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100A_PER09(Element):
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


class L2100A_PER(Segment):
    """Information Source Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Source Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Information Source Contact Information',
                   'position': 80,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2100A_PER01'},
                                  'per02': {'$ref': '#/$elements/L2100A_PER02'},
                                  'per03': {'$ref': '#/$elements/L2100A_PER03'},
                                  'per04': {'$ref': '#/$elements/L2100A_PER04'},
                                  'per05': {'$ref': '#/$elements/L2100A_PER05'},
                                  'per06': {'$ref': '#/$elements/L2100A_PER06'},
                                  'per07': {'$ref': '#/$elements/L2100A_PER07'},
                                  'per08': {'$ref': '#/$elements/L2100A_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2100A_PER01
    per02: L2100A_PER02 | None
    per03: L2100A_PER03 | None
    per04: L2100A_PER04 | None
    per05: L2100A_PER05 | None
    per06: L2100A_PER06 | None
    per07: L2100A_PER07 | None
    per08: L2100A_PER08 | None


class L2100A_AAA01(Element):
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


class L2100A_AAA02(Element):
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


class L2100A_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'R',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['04', '41', '42', '79', '80', 'T4']}]}}
        datatype = common.D_901
        codes = ['04', '41', '42', '79', '80', 'T4']
        min_len = 2
        max_len = 2


class L2100A_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'R',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'},
                            {'enum': ['C', 'N', 'P', 'R', 'S', 'W', 'X', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'P', 'R', 'S', 'W', 'X', 'Y']
        min_len = 1
        max_len = 1


class L2100A_AAA(Segment):
    """Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Request Validation',
                   'position': 85,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2100A_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2100A_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2100A_AAA04'}},
                   'required': ['aaa01', 'aaa03', 'aaa04']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2100A_AAA01
    aaa03: L2100A_AAA03
    aaa04: L2100A_AAA04


class L2100A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Source Name',
                   'usage': 'R',
                   'description': 'xid=2100A name=Information Source Name type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100A_NM1'},
                                  'ref': {'$ref': '#/$segments/L2100A_REF'},
                                  'per': {'$ref': '#/$segments/L2100A_PER'},
                                  'aaa': {'$ref': '#/$segments/L2100A_AAA'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100A_NM1
    ref: list[L2100A_REF] | None
    per: list[L2100A_PER] | None
    aaa: list[L2100A_AAA] | None


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
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['0', '1']}]}}
        datatype = common.D_736
        codes = ['0', '1']
        min_len = 1
        max_len = 1


class L2000B_HL(Segment):
    """Information Receiver Level"""
    class Schema:
        json = {'title': 'Information Receiver Level',
         'usage': 'R',
         'description': 'xid=HL name=Information Receiver Level',
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


class L2100B_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['1P', '2B', '36', '80', 'FA', 'GP', 'P5',
                                      'PR']}]}}
        datatype = common.D_98
        codes = ['1P', '2B', '36', '80', 'FA', 'GP', 'P5', 'PR']
        min_len = 2
        max_len = 3


class L2100B_NM102(Element):
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


class L2100B_NM103(Element):
    """Information Receiver Last or Organization Name"""
    class Schema:
        json = {'title': 'Information Receiver Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100B_NM104(Element):
    """Information Receiver First Name"""
    class Schema:
        json = {'title': 'Information Receiver First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100B_NM105(Element):
    """Information Receiver Middle Name"""
    class Schema:
        json = {'title': 'Information Receiver Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100B_NM106(Element):
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


class L2100B_NM107(Element):
    """Information Receiver Name Suffix"""
    class Schema:
        json = {'title': 'Information Receiver Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100B_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', 'FI', 'PI', 'PP', 'SV', 'XV',
                                      'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'FI', 'PI', 'PP', 'SV', 'XV', 'XX']
        min_len = 1
        max_len = 2


class L2100B_NM109(Element):
    """Information Receiver Identification Number"""
    class Schema:
        json = {'title': 'Information Receiver Identification Number',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100B_NM110(Element):
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


class L2100B_NM111(Element):
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


class L2100B_NM1(Segment):
    """Information Receiver Name"""
    class Schema:
        json = {'title': 'Information Receiver Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Information Receiver Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100B_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100B_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100B_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100B_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100B_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100B_NM101
    nm102: L2100B_NM102
    nm103: L2100B_NM103 | None
    nm104: L2100B_NM104 | None
    nm105: L2100B_NM105 | None
    nm107: L2100B_NM107 | None
    nm108: L2100B_NM108
    nm109: L2100B_NM109


class L2100B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1C', '1D', '1J', '4A', 'CT', 'EL', 'EO',
                                      'JD', 'N5', 'N7', 'Q4', 'SY', 'TJ', 'HPI']}]}}
        datatype = common.D_128
        codes = ['0B', '1C', '1D', '1J', '4A', 'CT', 'EL', 'EO', 'JD', 'N5', 'N7', 'Q4', 'SY', 'TJ', 'HPI']
        min_len = 2
        max_len = 3


class L2100B_REF02(Element):
    """Information Receiver Additional Identifier"""
    class Schema:
        json = {'title': 'Information Receiver Additional Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2100B_REF03(Element):
    """License Number State Code"""
    class Schema:
        json = {'title': 'License Number State Code',
         'usage': 'S',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        codes = common.states
        min_len = 1
        max_len = 80


class L2100B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100B_REF(Segment):
    """Information Receiver Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Information Receiver Additional '
                                  'Identification',
                   'position': 40,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100B_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2100B_REF03'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2100B_REF01
    ref02: L2100B_REF02
    ref03: L2100B_REF03 | None


class L2100B_AAA01(Element):
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


class L2100B_AAA02(Element):
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


class L2100B_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'R',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '41', '43', '44', '45', '46', '47', '48',
                                      '50', '51', '79', '97', 'T4']}]}}
        datatype = common.D_901
        codes = ['15', '41', '43', '44', '45', '46', '47', '48', '50', '51', '79', '97', 'T4']
        min_len = 2
        max_len = 2


class L2100B_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'R',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'},
                            {'enum': ['C', 'N', 'R', 'S', 'W', 'X', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'R', 'S', 'W', 'X', 'Y']
        min_len = 1
        max_len = 1


class L2100B_AAA(Segment):
    """Information Receiver Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Information Receiver Request '
                                  'Validation',
                   'position': 85,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2100B_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2100B_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2100B_AAA04'}},
                   'required': ['aaa01', 'aaa03', 'aaa04']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2100B_AAA01
    aaa03: L2100B_AAA03
    aaa04: L2100B_AAA04


class L2100B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Name',
                   'usage': 'R',
                   'description': 'xid=2100B name=Information Receiver Name type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100B_NM1'},
                                  'ref': {'$ref': '#/$segments/L2100B_REF'},
                                  'aaa': {'$ref': '#/$segments/L2100B_AAA'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100B_NM1
    ref: list[L2100B_REF] | None
    aaa: list[L2100B_AAA] | None


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
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['0', '1']}]}}
        datatype = common.D_736
        codes = ['0', '1']
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
    """Trace Number"""
    class Schema:
        json = {'title': 'Trace Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000C_TRN03(Element):
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
    """Subscriber Trace Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Trace Number',
                   'usage': 'S',
                   'description': 'xid=TRN name=Subscriber Trace Number',
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


class L2100C_NM101(Element):
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


class L2100C_NM102(Element):
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


class L2100C_NM103(Element):
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


class L2100C_NM104(Element):
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


class L2100C_NM105(Element):
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


class L2100C_NM106(Element):
    """Subscriber Name Prefix"""
    class Schema:
        json = {'title': 'Subscriber Name Prefix',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100C_NM107(Element):
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


class L2100C_NM108(Element):
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


class L2100C_NM109(Element):
    """Subscriber Primary Identifier"""
    class Schema:
        json = {'title': 'Subscriber Primary Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100C_NM110(Element):
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


class L2100C_NM111(Element):
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


class L2100C_NM1(Segment):
    """Subscriber Name"""
    class Schema:
        json = {'title': 'Subscriber Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Subscriber Name',
         'position': 30,
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
                        'nm109': {'$ref': '#/$elements/L2100C_NM109'}},
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


class L2100C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['18', '1L', '1W', '3H', '49', '6P', 'CT', 'A6',
                                      'EA', 'EJ', 'F6', 'GH', 'HJ', 'IF', 'IG', 'ML',
                                      'N6', 'NQ', 'Q4', 'SY']}]}}
        datatype = common.D_128
        codes = ['18', '1L', '1W', '3H', '49', '6P', 'CT', 'A6', 'EA', 'EJ', 'F6', 'GH', 'HJ', 'IF', 'IG', 'ML', 'N6', 'NQ', 'Q4', 'SY']
        min_len = 2
        max_len = 3


class L2100C_REF02(Element):
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


class L2100C_REF03(Element):
    """Plan Sponsor Name"""
    class Schema:
        json = {'title': 'Plan Sponsor Name',
         'usage': 'S',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100C_REF(Segment):
    """Subscriber Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Subscriber Additional Identification',
                   'position': 40,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100C_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100C_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2100C_REF03'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2100C_REF01
    ref02: L2100C_REF02
    ref03: L2100C_REF03 | None


class L2100C_N301(Element):
    """Subscriber Address Line 1"""
    class Schema:
        json = {'title': 'Subscriber Address Line 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100C_N302(Element):
    """Subscriber Address Line 2"""
    class Schema:
        json = {'title': 'Subscriber Address Line 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100C_N3(Segment):
    """Subscriber Address"""
    class Schema:
        json = {'title': 'Subscriber Address',
         'usage': 'S',
         'description': 'xid=N3 name=Subscriber Address',
         'position': 60,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100C_N301'},
                        'n302': {'$ref': '#/$elements/L2100C_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100C_N301
    n302: L2100C_N302 | None


class L2100C_N401(Element):
    """Subscriber City Name"""
    class Schema:
        json = {'title': 'Subscriber City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100C_N402(Element):
    """Subscriber State Code"""
    class Schema:
        json = {'title': 'Subscriber State Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100C_N403(Element):
    """Subscriber Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Subscriber Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100C_N404(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100C_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['CY', 'FI']}]}}
        datatype = common.D_309
        codes = ['CY', 'FI']
        min_len = 1
        max_len = 2


class L2100C_N406(Element):
    """Location Identification Code"""
    class Schema:
        json = {'title': 'Location Identification Code',
         'usage': 'S',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100C_N4(Segment):
    """Subscriber City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Subscriber City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Subscriber City/State/ZIP Code',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100C_N401'},
                        'n402': {'$ref': '#/$elements/L2100C_N402'},
                        'n403': {'$ref': '#/$elements/L2100C_N403'},
                        'n404': {'$ref': '#/$elements/L2100C_N404'},
                        'n405': {'$ref': '#/$elements/L2100C_N405'},
                        'n406': {'$ref': '#/$elements/L2100C_N406'}}}
        segment_name = 'N4'
    n401: L2100C_N401 | None
    n402: L2100C_N402 | None
    n403: L2100C_N403 | None
    n404: L2100C_N404 | None
    n405: L2100C_N405 | None
    n406: L2100C_N406 | None


class L2100C_PER01(Element):
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


class L2100C_PER02(Element):
    """Subscriber Contact Name"""
    class Schema:
        json = {'title': 'Subscriber Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100C_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100C_PER04(Element):
    """Subscriber Contact Number"""
    class Schema:
        json = {'title': 'Subscriber Contact Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100C_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100C_PER06(Element):
    """Subscriber Contact Number"""
    class Schema:
        json = {'title': 'Subscriber Contact Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100C_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100C_PER08(Element):
    """Subscriber Contact Number"""
    class Schema:
        json = {'title': 'Subscriber Contact Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100C_PER09(Element):
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


class L2100C_PER(Segment):
    """Subscriber Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Subscriber Contact Information',
                   'position': 80,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2100C_PER01'},
                                  'per02': {'$ref': '#/$elements/L2100C_PER02'},
                                  'per03': {'$ref': '#/$elements/L2100C_PER03'},
                                  'per04': {'$ref': '#/$elements/L2100C_PER04'},
                                  'per05': {'$ref': '#/$elements/L2100C_PER05'},
                                  'per06': {'$ref': '#/$elements/L2100C_PER06'},
                                  'per07': {'$ref': '#/$elements/L2100C_PER07'},
                                  'per08': {'$ref': '#/$elements/L2100C_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2100C_PER01
    per02: L2100C_PER02 | None
    per03: L2100C_PER03 | None
    per04: L2100C_PER04 | None
    per05: L2100C_PER05 | None
    per06: L2100C_PER06 | None
    per07: L2100C_PER07 | None
    per08: L2100C_PER08 | None


class L2100C_AAA01(Element):
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


class L2100C_AAA02(Element):
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


class L2100C_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'R',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '42', '43', '45', '47', '48', '49', '51',
                                      '52', '56', '57', '58', '60', '61', '62', '63',
                                      '64', '65', '66', '67', '68', '71', '72', '73',
                                      '74', '75', '76', '77', '78']}]}}
        datatype = common.D_901
        codes = ['15', '42', '43', '45', '47', '48', '49', '51', '52', '56', '57', '58', '60', '61', '62', '63', '64', '65', '66', '67', '68', '71', '72', '73', '74', '75', '76', '77', '78']
        min_len = 2
        max_len = 2


class L2100C_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'R',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'},
                            {'enum': ['C', 'N', 'R', 'S', 'W', 'X', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'R', 'S', 'W', 'X', 'Y']
        min_len = 1
        max_len = 1


class L2100C_AAA(Segment):
    """Subscriber Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Subscriber Request Validation',
                   'position': 85,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2100C_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2100C_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2100C_AAA04'}},
                   'required': ['aaa01', 'aaa03', 'aaa04']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2100C_AAA01
    aaa03: L2100C_AAA03
    aaa04: L2100C_AAA04


class L2100C_DMG01(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=DMG01 data_ele=1250',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2100C_DMG02(Element):
    """Subscriber Birth Date"""
    class Schema:
        json = {'title': 'Subscriber Birth Date',
         'usage': 'S',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100C_DMG03(Element):
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


class L2100C_DMG04(Element):
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


class L2100C_DMG05(Element):
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


class L2100C_DMG06(Element):
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


class L2100C_DMG07(Element):
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


class L2100C_DMG08(Element):
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


class L2100C_DMG09(Element):
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


class L2100C_DMG(Segment):
    """Subscriber Demographic Information"""
    class Schema:
        json = {'title': 'Subscriber Demographic Information',
         'usage': 'S',
         'description': 'xid=DMG name=Subscriber Demographic Information',
         'position': 100,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2100C_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2100C_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2100C_DMG03'}}}
        segment_name = 'DMG'
    dmg01: L2100C_DMG01 | None
    dmg02: L2100C_DMG02 | None
    dmg03: L2100C_DMG03 | None


class L2100C_INS01(Element):
    """Insured Indicator"""
    class Schema:
        json = {'title': 'Insured Indicator',
         'usage': 'R',
         'description': 'xid=INS01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['Y']}]}}
        datatype = common.D_1073
        codes = ['Y']
        min_len = 1
        max_len = 1


class L2100C_INS02(Element):
    """Individual Relationship Code"""
    class Schema:
        json = {'title': 'Individual Relationship Code',
         'usage': 'R',
         'description': 'xid=INS02 data_ele=1069',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'}, {'enum': ['18']}]}}
        datatype = common.D_1069
        codes = ['18']
        min_len = 2
        max_len = 2


class L2100C_INS03(Element):
    """Maintenance Type Code"""
    class Schema:
        json = {'title': 'Maintenance Type Code',
         'usage': 'S',
         'description': 'xid=INS03 data_ele=875',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/875'}, {'enum': ['001']}]}}
        datatype = common.D_875
        codes = ['001']
        min_len = 3
        max_len = 3


class L2100C_INS04(Element):
    """Maintenance Reason Code"""
    class Schema:
        json = {'title': 'Maintenance Reason Code',
         'usage': 'S',
         'description': 'xid=INS04 data_ele=1203',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1203'}, {'enum': ['25']}]}}
        datatype = common.D_1203
        codes = ['25']
        min_len = 2
        max_len = 3


class L2100C_INS05(Element):
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


class L2100C_INS06(Element):
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


class L2100C_INS07(Element):
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


class L2100C_INS08(Element):
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


class L2100C_INS09(Element):
    """Student Status Code"""
    class Schema:
        json = {'title': 'Student Status Code',
         'usage': 'S',
         'description': 'xid=INS09 data_ele=1220',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/1220'}, {'enum': ['F', 'N', 'P']}]}}
        datatype = common.D_1220
        codes = ['F', 'N', 'P']
        min_len = 1
        max_len = 1


class L2100C_INS10(Element):
    """Handicap Indicator"""
    class Schema:
        json = {'title': 'Handicap Indicator',
         'usage': 'S',
         'description': 'xid=INS10 data_ele=1073',
         'sequence': 10,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2100C_INS11(Element):
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


class L2100C_INS12(Element):
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


class L2100C_INS13(Element):
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


class L2100C_INS14(Element):
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


class L2100C_INS15(Element):
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


class L2100C_INS16(Element):
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


class L2100C_INS17(Element):
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


class L2100C_INS(Segment):
    """Subscriber Relationship"""
    class Schema:
        json = {'title': 'Subscriber Relationship',
         'usage': 'S',
         'description': 'xid=INS name=Subscriber Relationship',
         'position': 110,
         'type': 'object',
         'properties': {'xid': {'literal': 'INS'},
                        'ins01': {'$ref': '#/$elements/L2100C_INS01'},
                        'ins02': {'$ref': '#/$elements/L2100C_INS02'},
                        'ins03': {'$ref': '#/$elements/L2100C_INS03'},
                        'ins04': {'$ref': '#/$elements/L2100C_INS04'},
                        'ins09': {'$ref': '#/$elements/L2100C_INS09'},
                        'ins10': {'$ref': '#/$elements/L2100C_INS10'},
                        'ins17': {'$ref': '#/$elements/L2100C_INS17'}},
         'required': ['ins01', 'ins02']}
        segment_name = 'INS'
    ins01: L2100C_INS01
    ins02: L2100C_INS02
    ins03: L2100C_INS03 | None
    ins04: L2100C_INS04 | None
    ins09: L2100C_INS09 | None
    ins10: L2100C_INS10 | None
    ins17: L2100C_INS17 | None


class L2100C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['102', '152', '291', '307', '318', '340', '341',
                                      '342', '343', '346', '347', '356', '357', '382',
                                      '435', '442', '458', '472', '539', '540', '636',
                                      '771']}]}}
        datatype = common.D_374
        codes = ['102', '152', '291', '307', '318', '340', '341', '342', '343', '346', '347', '356', '357', '382', '435', '442', '458', '472', '539', '540', '636', '771']
        min_len = 3
        max_len = 3


class L2100C_DTP02(Element):
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


class L2100C_DTP03(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100C_DTP(Segment):
    """Subscriber Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Date',
                   'usage': 'S',
                   'description': 'xid=DTP name=Subscriber Date',
                   'position': 120,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2100C_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2100C_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2100C_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 9}
        segment_name = 'DTP'
    dtp01: L2100C_DTP01
    dtp02: L2100C_DTP02
    dtp03: L2100C_DTP03


class L2110C_EB01(Element):
    """Eligibility or Benefit Information"""
    class Schema:
        json = {'title': 'Eligibility or Benefit Information',
         'usage': 'R',
         'description': 'xid=EB01 data_ele=1390',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1390'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', 'A', 'B',
                                      'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                                      'W', 'X', 'Y', 'CB', 'MC']}]}}
        datatype = common.D_1390
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'CB', 'MC']
        min_len = 1
        max_len = 2


class L2110C_EB02(Element):
    """Benefit Coverage Level Code"""
    class Schema:
        json = {'title': 'Benefit Coverage Level Code',
         'usage': 'S',
         'description': 'xid=EB02 data_ele=1207',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1207'},
                            {'enum': ['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND',
                                      'SPC', 'SPO']}]}}
        datatype = common.D_1207
        codes = ['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO']
        min_len = 3
        max_len = 3


class L2110C_EB03(Element):
    """Service Type Code"""
    class Schema:
        json = {'title': 'Service Type Code',
         'usage': 'S',
         'description': 'xid=EB03 data_ele=1365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1365'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '14', '15', '16', '17', '18',
                                      '19', '20', '21', '22', '23', '24', '25', '26',
                                      '27', '28', '30', '32', '33', '34', '35', '36',
                                      '37', '38', '39', '40', '41', '42', '43', '44',
                                      '45', '46', '47', '48', '49', '50', '51', '52',
                                      '53', '54', '55', '56', '57', '58', '59', '60',
                                      '61', '62', '63', '64', '65', '66', '67', '68',
                                      '69', '70', '71', '72', '73', '74', '75', '76',
                                      '77', '78', '79', '80', '81', '82', '83', '84',
                                      '85', '86', '87', '88', '89', '90', '91', '92',
                                      '93', '94', '95', '96', '97', '98', '99', 'A0',
                                      'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                                      'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG',
                                      'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO',
                                      'AQ', 'AR', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF',
                                      'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN',
                                      'BP', 'BQ', 'BR', 'BS']}]}}
        datatype = common.D_1365
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BP', 'BQ', 'BR', 'BS']
        min_len = 1
        max_len = 2


class L2110C_EB04(Element):
    """Insurance Type Code"""
    class Schema:
        json = {'title': 'Insurance Type Code',
         'usage': 'S',
         'description': 'xid=EB04 data_ele=1336',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1336'},
                            {'enum': ['D', '12', '13', '14', '15', '16', '41', '42',
                                      '43', '47', 'AP', 'C1', 'CO', 'CP', 'DB', 'EP',
                                      'FF', 'GP', 'HM', 'HN', 'HS', 'IN', 'IP', 'LC',
                                      'LD', 'LI', 'LT', 'MA', 'MB', 'MC', 'MH', 'MI',
                                      'MP', 'OT', 'PE', 'PL', 'PP', 'PR', 'PS', 'QM',
                                      'RP', 'SP', 'TF', 'WC', 'WU']}]}}
        datatype = common.D_1336
        codes = ['D', '12', '13', '14', '15', '16', '41', '42', '43', '47', 'AP', 'C1', 'CO', 'CP', 'DB', 'EP', 'FF', 'GP', 'HM', 'HN', 'HS', 'IN', 'IP', 'LC', 'LD', 'LI', 'LT', 'MA', 'MB', 'MC', 'MH', 'MI', 'MP', 'OT', 'PE', 'PL', 'PP', 'PR', 'PS', 'QM', 'RP', 'SP', 'TF', 'WC', 'WU']
        min_len = 1
        max_len = 3


class L2110C_EB05(Element):
    """Plan Coverage Description"""
    class Schema:
        json = {'title': 'Plan Coverage Description',
         'usage': 'S',
         'description': 'xid=EB05 data_ele=1204',
         'sequence': 5,
         'type': {'$ref': '#/$common/1204'}}
        datatype = common.D_1204
        min_len = 1
        max_len = 50


class L2110C_EB06(Element):
    """Time Period Qualifier"""
    class Schema:
        json = {'title': 'Time Period Qualifier',
         'usage': 'S',
         'description': 'xid=EB06 data_ele=615',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/615'},
                            {'enum': ['6', '7', '13', '21', '22', '23', '24', '25',
                                      '26', '27', '28', '29', '30', '31', '32', '33',
                                      '34', '35', '36']}]}}
        datatype = common.D_615
        codes = ['6', '7', '13', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
        min_len = 1
        max_len = 2


class L2110C_EB07(Element):
    """Benefit Amount"""
    class Schema:
        json = {'title': 'Benefit Amount',
         'usage': 'S',
         'description': 'xid=EB07 data_ele=782',
         'sequence': 7,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2110C_EB08(Element):
    """Benefit Percent"""
    class Schema:
        json = {'title': 'Benefit Percent',
         'usage': 'S',
         'description': 'xid=EB08 data_ele=954',
         'sequence': 8,
         'type': {'$ref': '#/$common/954'}}
        datatype = common.D_954
        min_len = 1
        max_len = 10


class L2110C_EB09(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'S',
         'description': 'xid=EB09 data_ele=673',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['99', 'CA', 'CE', 'DB', 'DY', 'HS', 'LA', 'LE',
                                      'MN', 'P6', 'QA', 'S7', 'S8', 'VS', 'YY']}]}}
        datatype = common.D_673
        codes = ['99', 'CA', 'CE', 'DB', 'DY', 'HS', 'LA', 'LE', 'MN', 'P6', 'QA', 'S7', 'S8', 'VS', 'YY']
        min_len = 2
        max_len = 2


class L2110C_EB10(Element):
    """Benefit Quantity"""
    class Schema:
        json = {'title': 'Benefit Quantity',
         'usage': 'S',
         'description': 'xid=EB10 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110C_EB11(Element):
    """Authorization or Certification Indicator"""
    class Schema:
        json = {'title': 'Authorization or Certification Indicator',
         'usage': 'S',
         'description': 'xid=EB11 data_ele=1073',
         'sequence': 11,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'U', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'U', 'Y']
        min_len = 1
        max_len = 1


class L2110C_EB12(Element):
    """In Plan Network Indicator"""
    class Schema:
        json = {'title': 'In Plan Network Indicator',
         'usage': 'S',
         'description': 'xid=EB12 data_ele=1073',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'U', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'U', 'Y']
        min_len = 1
        max_len = 1


class L2110C_EB13_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=EB13-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']
        min_len = 2
        max_len = 2


class L2110C_EB13_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=EB13-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110C_EB13_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EB13_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EB13_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EB13_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EB13_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=EB13-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110C_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'S',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 13,
         'syntax': [],
         'type': 'object',
         'properties': {'eb13_01': {'title': 'Product or Service ID Qualifier',
                                    'usage': 'R',
                                    'description': 'xid=EB13-01 data_ele=235',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/235'},
                                                       {'enum': ['AD', 'CJ', 'HC', 'ID',
                                                                 'IV', 'N4', 'ZZ']}]}},
                        'eb13_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=EB13-02 data_ele=234',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/234'}},
                        'eb13_03': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-03 data_ele=1339',
                                    'sequence': 3,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_04': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-04 data_ele=1339',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_05': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-05 data_ele=1339',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_06': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-06 data_ele=1339',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_07': {'title': 'Description',
                                    'usage': 'N',
                                    'description': 'xid=EB13-07 data_ele=352',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/352'}}},
         'required': ['eb13_01', 'eb13_02']}
    eb13_01: L2110C_EB13_01
    eb13_02: L2110C_EB13_02
    eb13_03: L2110C_EB13_03 | None
    eb13_04: L2110C_EB13_04 | None
    eb13_05: L2110C_EB13_05 | None
    eb13_06: L2110C_EB13_06 | None


class L2110C_EB(Segment):
    """Subscriber Eligibility or Benefit Information"""
    class Schema:
        json = {'title': 'Subscriber Eligibility or Benefit Information',
         'usage': 'R',
         'description': 'xid=EB name=Subscriber Eligibility or Benefit Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'EB'},
                        'eb01': {'$ref': '#/$elements/L2110C_EB01'},
                        'eb02': {'$ref': '#/$elements/L2110C_EB02'},
                        'eb03': {'$ref': '#/$elements/L2110C_EB03'},
                        'eb04': {'$ref': '#/$elements/L2110C_EB04'},
                        'eb05': {'$ref': '#/$elements/L2110C_EB05'},
                        'eb06': {'$ref': '#/$elements/L2110C_EB06'},
                        'eb07': {'$ref': '#/$elements/L2110C_EB07'},
                        'eb08': {'$ref': '#/$elements/L2110C_EB08'},
                        'eb09': {'$ref': '#/$elements/L2110C_EB09'},
                        'eb10': {'$ref': '#/$elements/L2110C_EB10'},
                        'eb11': {'$ref': '#/$elements/L2110C_EB11'},
                        'eb12': {'$ref': '#/$elements/L2110C_EB12'},
                        'c003': {'$ref': '#/$elements/L2110C_C003'}},
         'required': ['eb01']}
        segment_name = 'EB'
    eb01: L2110C_EB01
    eb02: L2110C_EB02 | None
    eb03: L2110C_EB03 | None
    eb04: L2110C_EB04 | None
    eb05: L2110C_EB05 | None
    eb06: L2110C_EB06 | None
    eb07: L2110C_EB07 | None
    eb08: L2110C_EB08 | None
    eb09: L2110C_EB09 | None
    eb10: L2110C_EB10 | None
    eb11: L2110C_EB11 | None
    eb12: L2110C_EB12 | None
    c003: L2110C_C003 | None


class L2110C_HSD01(Element):
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


class L2110C_HSD02(Element):
    """Benefit Quantity"""
    class Schema:
        json = {'title': 'Benefit Quantity',
         'usage': 'S',
         'description': 'xid=HSD02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110C_HSD03(Element):
    """Unit or Basis for Measurement Code"""
    class Schema:
        json = {'title': 'Unit or Basis for Measurement Code',
         'usage': 'S',
         'description': 'xid=HSD03 data_ele=355',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/355'},
                            {'enum': ['DA', 'MO', 'VS', 'WK', 'YR']}]}}
        datatype = common.D_355
        codes = ['DA', 'MO', 'VS', 'WK', 'YR']
        min_len = 2
        max_len = 2


class L2110C_HSD04(Element):
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


class L2110C_HSD05(Element):
    """Time Period Qualifier"""
    class Schema:
        json = {'title': 'Time Period Qualifier',
         'usage': 'S',
         'description': 'xid=HSD05 data_ele=615',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/615'},
                            {'enum': ['6', '7', '21', '22', '23', '24', '25', '26',
                                      '27', '28', '29', '30', '31', '32', '33', '34',
                                      '35']}]}}
        datatype = common.D_615
        codes = ['6', '7', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
        min_len = 1
        max_len = 2


class L2110C_HSD06(Element):
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


class L2110C_HSD07(Element):
    """Delivery Frequency Code"""
    class Schema:
        json = {'title': 'Delivery Frequency Code',
         'usage': 'S',
         'description': 'xid=HSD07 data_ele=678',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/678'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                                      'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
                                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                                      'W', 'X', 'Y', 'Z', 'SG', 'SL', 'SP', 'SX', 'SY',
                                      'SZ']}]}}
        datatype = common.D_678
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ']
        min_len = 1
        max_len = 2


class L2110C_HSD08(Element):
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


class L2110C_HSD(Segment):
    """Health Care Services Delivery"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Health Care Services Delivery',
                   'usage': 'S',
                   'description': 'xid=HSD name=Health Care Services Delivery',
                   'position': 135,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'HSD'},
                                  'hsd01': {'$ref': '#/$elements/L2110C_HSD01'},
                                  'hsd02': {'$ref': '#/$elements/L2110C_HSD02'},
                                  'hsd03': {'$ref': '#/$elements/L2110C_HSD03'},
                                  'hsd04': {'$ref': '#/$elements/L2110C_HSD04'},
                                  'hsd05': {'$ref': '#/$elements/L2110C_HSD05'},
                                  'hsd06': {'$ref': '#/$elements/L2110C_HSD06'},
                                  'hsd07': {'$ref': '#/$elements/L2110C_HSD07'},
                                  'hsd08': {'$ref': '#/$elements/L2110C_HSD08'}}},
         'maxItems': 9}
        segment_name = 'HSD'
    hsd01: L2110C_HSD01 | None
    hsd02: L2110C_HSD02 | None
    hsd03: L2110C_HSD03 | None
    hsd04: L2110C_HSD04 | None
    hsd05: L2110C_HSD05 | None
    hsd06: L2110C_HSD06 | None
    hsd07: L2110C_HSD07 | None
    hsd08: L2110C_HSD08 | None


class L2110C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['18', '1L', '1W', '49', '6P', '9F', 'A6', 'F6',
                                      'G1', 'IG', 'N6', 'NQ']}]}}
        datatype = common.D_128
        codes = ['18', '1L', '1W', '49', '6P', '9F', 'A6', 'F6', 'G1', 'IG', 'N6', 'NQ']
        min_len = 2
        max_len = 3


class L2110C_REF02(Element):
    """Subscriber Eligibility or Benefit Identifier"""
    class Schema:
        json = {'title': 'Subscriber Eligibility or Benefit Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2110C_REF03(Element):
    """Plan Sponsor Name"""
    class Schema:
        json = {'title': 'Plan Sponsor Name',
         'usage': 'S',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110C_REF(Segment):
    """Subscriber Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Subscriber Additional Identification',
                   'position': 140,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2110C_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2110C_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2110C_REF03'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2110C_REF01
    ref02: L2110C_REF02
    ref03: L2110C_REF03 | None


class L2110C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['193', '194', '198', '290', '292', '295', '304',
                                      '307', '318', '348', '349', '356', '357', '435',
                                      '472', '636']}]}}
        datatype = common.D_374
        codes = ['193', '194', '198', '290', '292', '295', '304', '307', '318', '348', '349', '356', '357', '435', '472', '636']
        min_len = 3
        max_len = 3


class L2110C_DTP02(Element):
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


class L2110C_DTP03(Element):
    """Eligibility or Benefit Date Time Period"""
    class Schema:
        json = {'title': 'Eligibility or Benefit Date Time Period',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2110C_DTP(Segment):
    """Subscriber Eligibility/Benefit Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Eligibility/Benefit Date',
                   'usage': 'S',
                   'description': 'xid=DTP name=Subscriber Eligibility/Benefit Date',
                   'position': 150,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2110C_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2110C_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2110C_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 20}
        segment_name = 'DTP'
    dtp01: L2110C_DTP01
    dtp02: L2110C_DTP02
    dtp03: L2110C_DTP03


class L2110C_AAA01(Element):
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


class L2110C_AAA02(Element):
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


class L2110C_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'R',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '52', '53', '54', '55', '56', '57', '60',
                                      '61', '62', '63', '69', '70']}]}}
        datatype = common.D_901
        codes = ['15', '52', '53', '54', '55', '56', '57', '60', '61', '62', '63', '69', '70']
        min_len = 2
        max_len = 2


class L2110C_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'R',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'},
                            {'enum': ['C', 'N', 'R', 'W', 'X', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'R', 'W', 'X', 'Y']
        min_len = 1
        max_len = 1


class L2110C_AAA(Segment):
    """Subscriber Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Subscriber Request Validation',
                   'position': 160,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2110C_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2110C_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2110C_AAA04'}},
                   'required': ['aaa01', 'aaa03', 'aaa04']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2110C_AAA01
    aaa03: L2110C_AAA03
    aaa04: L2110C_AAA04


class L2110C_MSG01(Element):
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


class L2110C_MSG02(Element):
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


class L2110C_MSG03(Element):
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


class L2110C_MSG(Segment):
    """Message Text"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Message Text',
                   'usage': 'S',
                   'description': 'xid=MSG name=Message Text',
                   'position': 250,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'MSG'},
                                  'msg01': {'$ref': '#/$elements/L2110C_MSG01'}},
                   'required': ['msg01']},
         'maxItems': 10}
        segment_name = 'MSG'
    msg01: L2110C_MSG01


class L2115C_III01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=III01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'BK', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['BF', 'BK', 'ZZ']
        min_len = 1
        max_len = 3


class L2115C_III02(Element):
    """Industry Code"""
    class Schema:
        json = {'title': 'Industry Code',
         'usage': 'R',
         'description': 'xid=III02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2115C_III03(Element):
    """Code Category"""
    class Schema:
        json = {'title': 'Code Category',
         'usage': 'N',
         'description': 'xid=III03 data_ele=1136',
         'sequence': 3,
         'type': {'$ref': '#/$common/1136'}}
        datatype = common.D_1136
        min_len = 2
        max_len = 2


class L2115C_III04(Element):
    """Free-Form Message Text"""
    class Schema:
        json = {'title': 'Free-Form Message Text',
         'usage': 'N',
         'description': 'xid=III04 data_ele=933',
         'sequence': 4,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2115C_III05(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=III05 data_ele=380',
         'sequence': 5,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2115C_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 6,
         'syntax': []}


class L2115C_III07(Element):
    """Surface/Layer/Position Code"""
    class Schema:
        json = {'title': 'Surface/Layer/Position Code',
         'usage': 'N',
         'description': 'xid=III07 data_ele=752',
         'sequence': 7,
         'type': {'$ref': '#/$common/752'}}
        datatype = common.D_752
        min_len = 2
        max_len = 2


class L2115C_III08(Element):
    """Surface/Layer/Position Code"""
    class Schema:
        json = {'title': 'Surface/Layer/Position Code',
         'usage': 'N',
         'description': 'xid=III08 data_ele=752',
         'sequence': 8,
         'type': {'$ref': '#/$common/752'}}
        datatype = common.D_752
        min_len = 2
        max_len = 2


class L2115C_III09(Element):
    """Surface/Layer/Position Code"""
    class Schema:
        json = {'title': 'Surface/Layer/Position Code',
         'usage': 'N',
         'description': 'xid=III09 data_ele=752',
         'sequence': 9,
         'type': {'$ref': '#/$common/752'}}
        datatype = common.D_752
        min_len = 2
        max_len = 2


class L2115C_III(Segment):
    """Subscriber Eligibility or Benefit Additional Information"""
    class Schema:
        json = {'title': 'Subscriber Eligibility or Benefit Additional Information',
         'usage': 'R',
         'description': 'xid=III name=Subscriber Eligibility or Benefit Additional '
                        'Information',
         'position': 260,
         'type': 'object',
         'properties': {'xid': {'literal': 'III'},
                        'iii01': {'$ref': '#/$elements/L2115C_III01'},
                        'iii02': {'$ref': '#/$elements/L2115C_III02'}},
         'required': ['iii01', 'iii02']}
        segment_name = 'III'
    iii01: L2115C_III01
    iii02: L2115C_III02


class L2115C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Eligibility or Benefit Additional Information',
                   'usage': 'S',
                   'description': 'xid=2115C name=Subscriber Eligibility or Benefit '
                                  'Additional Information type=None',
                   'position': 260,
                   'type': 'object',
                   'properties': {'iii': {'$ref': '#/$segments/L2115C_III'}},
                   'required': ['iii']},
         'maxItems': 10}
    iii: L2115C_III


class L2110C_LS01(Element):
    """Loop Identifier Code"""
    class Schema:
        json = {'title': 'Loop Identifier Code',
         'usage': 'R',
         'description': 'xid=LS01 data_ele=447',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/447'}, {'enum': ['2120']}]}}
        datatype = common.D_447
        codes = ['2120']
        min_len = 1
        max_len = 4


class L2110C_LS(Segment):
    """Loop Header"""
    class Schema:
        json = {'title': 'Loop Header',
         'usage': 'S',
         'description': 'xid=LS name=Loop Header',
         'position': 330,
         'type': 'object',
         'properties': {'xid': {'literal': 'LS'},
                        'ls01': {'$ref': '#/$elements/L2110C_LS01'}},
         'required': ['ls01']}
        segment_name = 'LS'
    ls01: L2110C_LS01


class L2120C_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['13', '1P', '2B', '36', '73', 'FA', 'GP', 'IL',
                                      'LR', 'P3', 'P4', 'P5', 'PR', 'VN', 'X3', 'PRP',
                                      'SEP', 'TTP']}]}}
        datatype = common.D_98
        codes = ['13', '1P', '2B', '36', '73', 'FA', 'GP', 'IL', 'LR', 'P3', 'P4', 'P5', 'PR', 'VN', 'X3', 'PRP', 'SEP', 'TTP']
        min_len = 2
        max_len = 3


class L2120C_NM102(Element):
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


class L2120C_NM103(Element):
    """Benefit Related Entity Last or Organization Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2120C_NM104(Element):
    """Benefit Related Entity First Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2120C_NM105(Element):
    """Benefit Related Entity Middle Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2120C_NM106(Element):
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


class L2120C_NM107(Element):
    """Benefit Related Entity Name Suffix"""
    class Schema:
        json = {'title': 'Benefit Related Entity Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2120C_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'FA', 'FI', 'MI', 'NI', 'PI',
                                      'PP', 'SV', 'XV', 'XX', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'FA', 'FI', 'MI', 'NI', 'PI', 'PP', 'SV', 'XV', 'XX', 'ZZ']
        min_len = 1
        max_len = 2


class L2120C_NM109(Element):
    """Benefit Related Entity Identifier"""
    class Schema:
        json = {'title': 'Benefit Related Entity Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2120C_NM110(Element):
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


class L2120C_NM111(Element):
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


class L2120C_NM1(Segment):
    """Subscriber Benefit Related Entity Name"""
    class Schema:
        json = {'title': 'Subscriber Benefit Related Entity Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Subscriber Benefit Related Entity Name',
         'position': 340,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2120C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2120C_NM102'},
                        'nm103': {'$ref': '#/$elements/L2120C_NM103'},
                        'nm104': {'$ref': '#/$elements/L2120C_NM104'},
                        'nm105': {'$ref': '#/$elements/L2120C_NM105'},
                        'nm107': {'$ref': '#/$elements/L2120C_NM107'},
                        'nm108': {'$ref': '#/$elements/L2120C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2120C_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2120C_NM101
    nm102: L2120C_NM102
    nm103: L2120C_NM103 | None
    nm104: L2120C_NM104 | None
    nm105: L2120C_NM105 | None
    nm107: L2120C_NM107 | None
    nm108: L2120C_NM108 | None
    nm109: L2120C_NM109 | None


class L2120C_N301(Element):
    """Benefit Related Entity Address Line 1"""
    class Schema:
        json = {'title': 'Benefit Related Entity Address Line 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2120C_N302(Element):
    """Benefit Related Entity Address Line 2"""
    class Schema:
        json = {'title': 'Benefit Related Entity Address Line 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2120C_N3(Segment):
    """Subscriber Benefit Related Entity Address"""
    class Schema:
        json = {'title': 'Subscriber Benefit Related Entity Address',
         'usage': 'S',
         'description': 'xid=N3 name=Subscriber Benefit Related Entity Address',
         'position': 360,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2120C_N301'},
                        'n302': {'$ref': '#/$elements/L2120C_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2120C_N301
    n302: L2120C_N302 | None


class L2120C_N401(Element):
    """Benefit Related Entity City Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2120C_N402(Element):
    """Benefit Related Entity State Code"""
    class Schema:
        json = {'title': 'Benefit Related Entity State Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2120C_N403(Element):
    """Benefit Related Entity Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Benefit Related Entity Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2120C_N404(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2120C_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['RJ']}]}}
        datatype = common.D_309
        codes = ['RJ']
        min_len = 1
        max_len = 2


class L2120C_N406(Element):
    """Department of Defense Health Service Region Code"""
    class Schema:
        json = {'title': 'Department of Defense Health Service Region Code',
         'usage': 'S',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2120C_N4(Segment):
    """Subscriber Benefit Related City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Subscriber Benefit Related City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Subscriber Benefit Related City/State/ZIP Code',
         'position': 370,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2120C_N401'},
                        'n402': {'$ref': '#/$elements/L2120C_N402'},
                        'n403': {'$ref': '#/$elements/L2120C_N403'},
                        'n404': {'$ref': '#/$elements/L2120C_N404'},
                        'n405': {'$ref': '#/$elements/L2120C_N405'},
                        'n406': {'$ref': '#/$elements/L2120C_N406'}}}
        segment_name = 'N4'
    n401: L2120C_N401 | None
    n402: L2120C_N402 | None
    n403: L2120C_N403 | None
    n404: L2120C_N404 | None
    n405: L2120C_N405 | None
    n406: L2120C_N406 | None


class L2120C_PER01(Element):
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


class L2120C_PER02(Element):
    """Benefit Related Entity Contact Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2120C_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'FX', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'FX', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2120C_PER04(Element):
    """Benefit Related Entity Communication Number"""
    class Schema:
        json = {'title': 'Benefit Related Entity Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2120C_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2120C_PER06(Element):
    """Benefit Related Entity Communication Number"""
    class Schema:
        json = {'title': 'Benefit Related Entity Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2120C_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2120C_PER08(Element):
    """Benefit Related Entity Communication Number"""
    class Schema:
        json = {'title': 'Benefit Related Entity Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2120C_PER09(Element):
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


class L2120C_PER(Segment):
    """Subscriber Benefit Related Entity Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Benefit Related Entity Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Subscriber Benefit Related Entity '
                                  'Contact Information',
                   'position': 380,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2120C_PER01'},
                                  'per02': {'$ref': '#/$elements/L2120C_PER02'},
                                  'per03': {'$ref': '#/$elements/L2120C_PER03'},
                                  'per04': {'$ref': '#/$elements/L2120C_PER04'},
                                  'per05': {'$ref': '#/$elements/L2120C_PER05'},
                                  'per06': {'$ref': '#/$elements/L2120C_PER06'},
                                  'per07': {'$ref': '#/$elements/L2120C_PER07'},
                                  'per08': {'$ref': '#/$elements/L2120C_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2120C_PER01
    per02: L2120C_PER02 | None
    per03: L2120C_PER03 | None
    per04: L2120C_PER04 | None
    per05: L2120C_PER05 | None
    per06: L2120C_PER06 | None
    per07: L2120C_PER07 | None
    per08: L2120C_PER08 | None


class L2120C_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'},
                            {'enum': ['AD', 'H', 'R', 'AT', 'BI', 'CO', 'CV', 'HH',
                                      'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'RF', 'SB',
                                      'SK', 'SU']}]}}
        datatype = common.D_1221
        codes = ['AD', 'H', 'R', 'AT', 'BI', 'CO', 'CV', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'RF', 'SB', 'SK', 'SU']
        min_len = 1
        max_len = 3


class L2120C_PRV02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=PRV02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['9K', 'D3', 'EI', 'SY', 'TJ', 'ZZ', 'HPI']}]}}
        datatype = common.D_128
        codes = ['9K', 'D3', 'EI', 'SY', 'TJ', 'ZZ', 'HPI']
        min_len = 2
        max_len = 3


class L2120C_PRV03(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
         'description': 'xid=PRV03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2120C_PRV04(Element):
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


class L2120C_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2120C_PRV06(Element):
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


class L2120C_PRV(Segment):
    """Subscriber Benefit Related Provider Information"""
    class Schema:
        json = {'title': 'Subscriber Benefit Related Provider Information',
         'usage': 'S',
         'description': 'xid=PRV name=Subscriber Benefit Related Provider Information',
         'position': 390,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2120C_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2120C_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2120C_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2120C_PRV01
    prv02: L2120C_PRV02
    prv03: L2120C_PRV03


class L2120C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Benefit Related Entity Name',
                   'usage': 'S',
                   'description': 'xid=2120C name=Subscriber Benefit Related Entity '
                                  'Name type=None',
                   'position': 340,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2120C_NM1'},
                                  'n3': {'$ref': '#/$segments/L2120C_N3'},
                                  'n4': {'$ref': '#/$segments/L2120C_N4'},
                                  'per': {'$ref': '#/$segments/L2120C_PER'},
                                  'prv': {'$ref': '#/$segments/L2120C_PRV'}}},
         'maxItems': 1}
    nm1: L2120C_NM1 | None
    n3: L2120C_N3 | None
    n4: L2120C_N4 | None
    per: list[L2120C_PER] | None
    prv: L2120C_PRV | None


class L2110C_LE01(Element):
    """Loop Identifier Code"""
    class Schema:
        json = {'title': 'Loop Identifier Code',
         'usage': 'R',
         'description': 'xid=LE01 data_ele=447',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/447'}, {'enum': ['2120']}]}}
        datatype = common.D_447
        codes = ['2120']
        min_len = 1
        max_len = 4


class L2110C_LE(Segment):
    """Loop Trailer"""
    class Schema:
        json = {'title': 'Loop Trailer',
         'usage': 'S',
         'description': 'xid=LE name=Loop Trailer',
         'position': 400,
         'type': 'object',
         'properties': {'xid': {'literal': 'LE'},
                        'le01': {'$ref': '#/$elements/L2110C_LE01'}},
         'required': ['le01']}
        segment_name = 'LE'
    le01: L2110C_LE01


class L2110C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Eligibility or Benefit Information',
                   'usage': 'S',
                   'description': 'xid=2110C name=Subscriber Eligibility or Benefit '
                                  'Information type=None',
                   'position': 130,
                   'type': 'object',
                   'properties': {'eb': {'$ref': '#/$segments/L2110C_EB'},
                                  'hsd': {'$ref': '#/$segments/L2110C_HSD'},
                                  'ref': {'$ref': '#/$segments/L2110C_REF'},
                                  'dtp': {'$ref': '#/$segments/L2110C_DTP'},
                                  'aaa': {'$ref': '#/$segments/L2110C_AAA'},
                                  'msg': {'$ref': '#/$segments/L2110C_MSG'},
                                  'l2115c': {'$ref': '#/$segments/L2115C'},
                                  'ls': {'$ref': '#/$segments/L2110C_LS'},
                                  'l2120c': {'$ref': '#/$segments/L2120C'},
                                  'le': {'$ref': '#/$segments/L2110C_LE'}},
                   'required': ['eb']}}
    eb: L2110C_EB
    hsd: list[L2110C_HSD] | None
    ref: list[L2110C_REF] | None
    dtp: list[L2110C_DTP] | None
    aaa: list[L2110C_AAA] | None
    msg: list[L2110C_MSG] | None
    l2115c: list[L2115C] | None
    ls: L2110C_LS | None
    l2120c: list[L2120C] | None
    le: L2110C_LE | None


class L2100C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Name',
                   'usage': 'R',
                   'description': 'xid=2100C name=Subscriber Name type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100C_NM1'},
                                  'ref': {'$ref': '#/$segments/L2100C_REF'},
                                  'n3': {'$ref': '#/$segments/L2100C_N3'},
                                  'n4': {'$ref': '#/$segments/L2100C_N4'},
                                  'per': {'$ref': '#/$segments/L2100C_PER'},
                                  'aaa': {'$ref': '#/$segments/L2100C_AAA'},
                                  'dmg': {'$ref': '#/$segments/L2100C_DMG'},
                                  'ins': {'$ref': '#/$segments/L2100C_INS'},
                                  'dtp': {'$ref': '#/$segments/L2100C_DTP'},
                                  'l2110c': {'$ref': '#/$segments/L2110C'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100C_NM1
    ref: list[L2100C_REF] | None
    n3: L2100C_N3 | None
    n4: L2100C_N4 | None
    per: list[L2100C_PER] | None
    aaa: list[L2100C_AAA] | None
    dmg: L2100C_DMG | None
    ins: L2100C_INS | None
    dtp: list[L2100C_DTP] | None
    l2110c: list[L2110C] | None


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
         'type': {'allOf': [{'$ref': '#/$common/736'}, {'enum': ['0']}]}}
        datatype = common.D_736
        codes = ['0']
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
    """Trace Number"""
    class Schema:
        json = {'title': 'Trace Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000D_TRN03(Element):
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
    """Dependent Trace Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Trace Number',
                   'usage': 'S',
                   'description': 'xid=TRN name=Dependent Trace Number',
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


class L2100D_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['03']}]}}
        datatype = common.D_98
        codes = ['03']
        min_len = 2
        max_len = 3


class L2100D_NM102(Element):
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


class L2100D_NM103(Element):
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


class L2100D_NM104(Element):
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


class L2100D_NM105(Element):
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


class L2100D_NM106(Element):
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


class L2100D_NM107(Element):
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


class L2100D_NM108(Element):
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


class L2100D_NM109(Element):
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


class L2100D_NM110(Element):
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


class L2100D_NM111(Element):
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


class L2100D_NM1(Segment):
    """Dependent Name"""
    class Schema:
        json = {'title': 'Dependent Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Dependent Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100D_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100D_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100D_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100D_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100D_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100D_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100D_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100D_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100D_NM101
    nm102: L2100D_NM102
    nm103: L2100D_NM103 | None
    nm104: L2100D_NM104 | None
    nm105: L2100D_NM105 | None
    nm107: L2100D_NM107 | None
    nm108: L2100D_NM108 | None
    nm109: L2100D_NM109 | None


class L2100D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['18', '1L', '1W', '49', '6P', 'A6', 'CT', 'EA',
                                      'EJ', 'F6', 'GH', 'HJ', 'IF', 'IG', 'M7', 'N6',
                                      'NQ', 'Q4', 'SY']}]}}
        datatype = common.D_128
        codes = ['18', '1L', '1W', '49', '6P', 'A6', 'CT', 'EA', 'EJ', 'F6', 'GH', 'HJ', 'IF', 'IG', 'M7', 'N6', 'NQ', 'Q4', 'SY']
        min_len = 2
        max_len = 3


class L2100D_REF02(Element):
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


class L2100D_REF03(Element):
    """Plan Sponsor Name"""
    class Schema:
        json = {'title': 'Plan Sponsor Name',
         'usage': 'S',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100D_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100D_REF(Segment):
    """Dependent Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Dependent Additional Identification',
                   'position': 40,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100D_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100D_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2100D_REF03'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2100D_REF01
    ref02: L2100D_REF02
    ref03: L2100D_REF03 | None


class L2100D_N301(Element):
    """Dependent Address Line 1"""
    class Schema:
        json = {'title': 'Dependent Address Line 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100D_N302(Element):
    """Dependent Address Line 2"""
    class Schema:
        json = {'title': 'Dependent Address Line 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100D_N3(Segment):
    """Dependent Address"""
    class Schema:
        json = {'title': 'Dependent Address',
         'usage': 'S',
         'description': 'xid=N3 name=Dependent Address',
         'position': 60,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100D_N301'},
                        'n302': {'$ref': '#/$elements/L2100D_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100D_N301
    n302: L2100D_N302 | None


class L2100D_N401(Element):
    """Dependent City Name"""
    class Schema:
        json = {'title': 'Dependent City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100D_N402(Element):
    """Dependent State Code"""
    class Schema:
        json = {'title': 'Dependent State Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100D_N403(Element):
    """Dependent Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Dependent Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100D_N404(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2100D_N405(Element):
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


class L2100D_N406(Element):
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


class L2100D_N4(Segment):
    """Dependent City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Dependent City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Dependent City/State/ZIP Code',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100D_N401'},
                        'n402': {'$ref': '#/$elements/L2100D_N402'},
                        'n403': {'$ref': '#/$elements/L2100D_N403'},
                        'n404': {'$ref': '#/$elements/L2100D_N404'}}}
        segment_name = 'N4'
    n401: L2100D_N401 | None
    n402: L2100D_N402 | None
    n403: L2100D_N403 | None
    n404: L2100D_N404 | None


class L2100D_PER01(Element):
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


class L2100D_PER02(Element):
    """Dependent Contact Name"""
    class Schema:
        json = {'title': 'Dependent Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100D_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100D_PER04(Element):
    """Dependent Contact Number"""
    class Schema:
        json = {'title': 'Dependent Contact Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100D_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100D_PER06(Element):
    """Dependent Contact Number"""
    class Schema:
        json = {'title': 'Dependent Contact Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100D_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100D_PER08(Element):
    """Dependent Contact Number"""
    class Schema:
        json = {'title': 'Dependent Contact Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100D_PER09(Element):
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


class L2100D_PER(Segment):
    """Dependent Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Dependent Contact Information',
                   'position': 80,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2100D_PER01'},
                                  'per02': {'$ref': '#/$elements/L2100D_PER02'},
                                  'per03': {'$ref': '#/$elements/L2100D_PER03'},
                                  'per04': {'$ref': '#/$elements/L2100D_PER04'},
                                  'per05': {'$ref': '#/$elements/L2100D_PER05'},
                                  'per06': {'$ref': '#/$elements/L2100D_PER06'},
                                  'per07': {'$ref': '#/$elements/L2100D_PER07'},
                                  'per08': {'$ref': '#/$elements/L2100D_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2100D_PER01
    per02: L2100D_PER02 | None
    per03: L2100D_PER03 | None
    per04: L2100D_PER04 | None
    per05: L2100D_PER05 | None
    per06: L2100D_PER06 | None
    per07: L2100D_PER07 | None
    per08: L2100D_PER08 | None


class L2100D_AAA01(Element):
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


class L2100D_AAA02(Element):
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


class L2100D_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'R',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '42', '43', '45', '47', '48', '49', '51',
                                      '52', '56', '57', '58', '60', '61', '62', '63',
                                      '64', '65', '66', '67', '68', '71']}]}}
        datatype = common.D_901
        codes = ['15', '42', '43', '45', '47', '48', '49', '51', '52', '56', '57', '58', '60', '61', '62', '63', '64', '65', '66', '67', '68', '71']
        min_len = 2
        max_len = 2


class L2100D_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'R',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'},
                            {'enum': ['C', 'N', 'R', 'S', 'W', 'X', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'R', 'S', 'W', 'X', 'Y']
        min_len = 1
        max_len = 1


class L2100D_AAA(Segment):
    """Dependent Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Dependent Request Validation',
                   'position': 85,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2100D_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2100D_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2100D_AAA04'}},
                   'required': ['aaa01', 'aaa03', 'aaa04']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2100D_AAA01
    aaa03: L2100D_AAA03
    aaa04: L2100D_AAA04


class L2100D_DMG01(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=DMG01 data_ele=1250',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2100D_DMG02(Element):
    """Dependent Birth Date"""
    class Schema:
        json = {'title': 'Dependent Birth Date',
         'usage': 'S',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100D_DMG03(Element):
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


class L2100D_DMG04(Element):
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


class L2100D_DMG05(Element):
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


class L2100D_DMG06(Element):
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


class L2100D_DMG07(Element):
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


class L2100D_DMG08(Element):
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


class L2100D_DMG09(Element):
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


class L2100D_DMG(Segment):
    """Dependent Demographic Information"""
    class Schema:
        json = {'title': 'Dependent Demographic Information',
         'usage': 'S',
         'description': 'xid=DMG name=Dependent Demographic Information',
         'position': 100,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2100D_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2100D_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2100D_DMG03'}}}
        segment_name = 'DMG'
    dmg01: L2100D_DMG01 | None
    dmg02: L2100D_DMG02 | None
    dmg03: L2100D_DMG03 | None


class L2100D_INS01(Element):
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


class L2100D_INS02(Element):
    """Individual Relationship Code"""
    class Schema:
        json = {'title': 'Individual Relationship Code',
         'usage': 'R',
         'description': 'xid=INS02 data_ele=1069',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'},
                            {'enum': ['01', '19', '21', '34']}]}}
        datatype = common.D_1069
        codes = ['01', '19', '21', '34']
        min_len = 2
        max_len = 2


class L2100D_INS03(Element):
    """Maintenance Type Code"""
    class Schema:
        json = {'title': 'Maintenance Type Code',
         'usage': 'S',
         'description': 'xid=INS03 data_ele=875',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/875'}, {'enum': ['001']}]}}
        datatype = common.D_875
        codes = ['001']
        min_len = 3
        max_len = 3


class L2100D_INS04(Element):
    """Maintenance Reason Code"""
    class Schema:
        json = {'title': 'Maintenance Reason Code',
         'usage': 'S',
         'description': 'xid=INS04 data_ele=1203',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1203'}, {'enum': ['25']}]}}
        datatype = common.D_1203
        codes = ['25']
        min_len = 2
        max_len = 3


class L2100D_INS05(Element):
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


class L2100D_INS06(Element):
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


class L2100D_INS07(Element):
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


class L2100D_INS08(Element):
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


class L2100D_INS09(Element):
    """Student Status Code"""
    class Schema:
        json = {'title': 'Student Status Code',
         'usage': 'S',
         'description': 'xid=INS09 data_ele=1220',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/1220'}, {'enum': ['F', 'N', 'P']}]}}
        datatype = common.D_1220
        codes = ['F', 'N', 'P']
        min_len = 1
        max_len = 1


class L2100D_INS10(Element):
    """Handicap Indicator"""
    class Schema:
        json = {'title': 'Handicap Indicator',
         'usage': 'S',
         'description': 'xid=INS10 data_ele=1073',
         'sequence': 10,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2100D_INS11(Element):
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


class L2100D_INS12(Element):
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


class L2100D_INS13(Element):
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


class L2100D_INS14(Element):
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


class L2100D_INS15(Element):
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


class L2100D_INS16(Element):
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


class L2100D_INS17(Element):
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


class L2100D_INS(Segment):
    """Dependent Relationship"""
    class Schema:
        json = {'title': 'Dependent Relationship',
         'usage': 'S',
         'description': 'xid=INS name=Dependent Relationship',
         'position': 110,
         'type': 'object',
         'properties': {'xid': {'literal': 'INS'},
                        'ins01': {'$ref': '#/$elements/L2100D_INS01'},
                        'ins02': {'$ref': '#/$elements/L2100D_INS02'},
                        'ins03': {'$ref': '#/$elements/L2100D_INS03'},
                        'ins04': {'$ref': '#/$elements/L2100D_INS04'},
                        'ins09': {'$ref': '#/$elements/L2100D_INS09'},
                        'ins10': {'$ref': '#/$elements/L2100D_INS10'},
                        'ins17': {'$ref': '#/$elements/L2100D_INS17'}},
         'required': ['ins01', 'ins02']}
        segment_name = 'INS'
    ins01: L2100D_INS01
    ins02: L2100D_INS02
    ins03: L2100D_INS03 | None
    ins04: L2100D_INS04 | None
    ins09: L2100D_INS09 | None
    ins10: L2100D_INS10 | None
    ins17: L2100D_INS17 | None


class L2100D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['102', '152', '291', '307', '318', '340', '341',
                                      '342', '343', '346', '347', '382', '435', '442',
                                      '458', '472', '539', '540', '636']}]}}
        datatype = common.D_374
        codes = ['102', '152', '291', '307', '318', '340', '341', '342', '343', '346', '347', '382', '435', '442', '458', '472', '539', '540', '636']
        min_len = 3
        max_len = 3


class L2100D_DTP02(Element):
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


class L2100D_DTP03(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100D_DTP(Segment):
    """Dependent Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Date',
                   'usage': 'S',
                   'description': 'xid=DTP name=Dependent Date',
                   'position': 120,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2100D_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2100D_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2100D_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 9}
        segment_name = 'DTP'
    dtp01: L2100D_DTP01
    dtp02: L2100D_DTP02
    dtp03: L2100D_DTP03


class L2110D_EB01(Element):
    """Eligibility or Benefit Information"""
    class Schema:
        json = {'title': 'Eligibility or Benefit Information',
         'usage': 'R',
         'description': 'xid=EB01 data_ele=1390',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1390'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', 'A', 'B',
                                      'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                                      'W', 'X', 'Y', 'CB', 'MC']}]}}
        datatype = common.D_1390
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'CB', 'MC']
        min_len = 1
        max_len = 2


class L2110D_EB02(Element):
    """Benefit Coverage Level Code"""
    class Schema:
        json = {'title': 'Benefit Coverage Level Code',
         'usage': 'S',
         'description': 'xid=EB02 data_ele=1207',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1207'},
                            {'enum': ['CHD', 'DEP', 'ECH', 'ESP', 'FAM', 'IND', 'SPC',
                                      'SPO']}]}}
        datatype = common.D_1207
        codes = ['CHD', 'DEP', 'ECH', 'ESP', 'FAM', 'IND', 'SPC', 'SPO']
        min_len = 3
        max_len = 3


class L2110D_EB03(Element):
    """Service Type Code"""
    class Schema:
        json = {'title': 'Service Type Code',
         'usage': 'S',
         'description': 'xid=EB03 data_ele=1365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1365'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11', '12', '13', '14', '15', '16', '17', '18',
                                      '19', '20', '21', '22', '23', '24', '25', '26',
                                      '27', '28', '30', '32', '33', '34', '35', '36',
                                      '37', '38', '39', '40', '41', '42', '43', '44',
                                      '45', '46', '47', '48', '49', '50', '51', '52',
                                      '53', '54', '55', '56', '57', '58', '59', '60',
                                      '61', '62', '63', '64', '65', '66', '67', '68',
                                      '69', '70', '71', '72', '73', '74', '75', '76',
                                      '77', '78', '79', '80', '81', '82', '83', '84',
                                      '85', '86', '87', '88', '89', '90', '91', '92',
                                      '93', '94', '95', '96', '97', '98', '99', 'A0',
                                      'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
                                      'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG',
                                      'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO',
                                      'AQ', 'AR', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF',
                                      'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN',
                                      'BP', 'BQ', 'BR', 'BS']}]}}
        datatype = common.D_1365
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BP', 'BQ', 'BR', 'BS']
        min_len = 1
        max_len = 2


class L2110D_EB04(Element):
    """Insurance Type Code"""
    class Schema:
        json = {'title': 'Insurance Type Code',
         'usage': 'S',
         'description': 'xid=EB04 data_ele=1336',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1336'},
                            {'enum': ['D', '12', '13', '14', '15', '16', '41', '42',
                                      '43', '47', 'AP', 'C1', 'CO', 'CP', 'DB', 'EP',
                                      'FF', 'GP', 'HM', 'HN', 'HS', 'IN', 'IP', 'LC',
                                      'LD', 'LI', 'LT', 'MA', 'MB', 'MC', 'MH', 'MI',
                                      'MP', 'OT', 'PE', 'PL', 'PP', 'PR', 'PS', 'QM',
                                      'RP', 'SP', 'TF', 'WC', 'WU']}]}}
        datatype = common.D_1336
        codes = ['D', '12', '13', '14', '15', '16', '41', '42', '43', '47', 'AP', 'C1', 'CO', 'CP', 'DB', 'EP', 'FF', 'GP', 'HM', 'HN', 'HS', 'IN', 'IP', 'LC', 'LD', 'LI', 'LT', 'MA', 'MB', 'MC', 'MH', 'MI', 'MP', 'OT', 'PE', 'PL', 'PP', 'PR', 'PS', 'QM', 'RP', 'SP', 'TF', 'WC', 'WU']
        min_len = 1
        max_len = 3


class L2110D_EB05(Element):
    """Plan Coverage Description"""
    class Schema:
        json = {'title': 'Plan Coverage Description',
         'usage': 'S',
         'description': 'xid=EB05 data_ele=1204',
         'sequence': 5,
         'type': {'$ref': '#/$common/1204'}}
        datatype = common.D_1204
        min_len = 1
        max_len = 50


class L2110D_EB06(Element):
    """Time Period Qualifier"""
    class Schema:
        json = {'title': 'Time Period Qualifier',
         'usage': 'S',
         'description': 'xid=EB06 data_ele=615',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/615'},
                            {'enum': ['6', '7', '13', '21', '22', '23', '24', '25',
                                      '26', '27', '28', '29', '30', '31', '32', '33',
                                      '34', '35', '36']}]}}
        datatype = common.D_615
        codes = ['6', '7', '13', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
        min_len = 1
        max_len = 2


class L2110D_EB07(Element):
    """Benefit Amount"""
    class Schema:
        json = {'title': 'Benefit Amount',
         'usage': 'S',
         'description': 'xid=EB07 data_ele=782',
         'sequence': 7,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2110D_EB08(Element):
    """Benefit Percent"""
    class Schema:
        json = {'title': 'Benefit Percent',
         'usage': 'S',
         'description': 'xid=EB08 data_ele=954',
         'sequence': 8,
         'type': {'$ref': '#/$common/954'}}
        datatype = common.D_954
        min_len = 1
        max_len = 10


class L2110D_EB09(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'S',
         'description': 'xid=EB09 data_ele=673',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['99', 'CA', 'CE', 'DB', 'DY', 'HS', 'LA', 'LE',
                                      'MN', 'P6', 'QA', 'S7', 'S8', 'VS', 'YY']}]}}
        datatype = common.D_673
        codes = ['99', 'CA', 'CE', 'DB', 'DY', 'HS', 'LA', 'LE', 'MN', 'P6', 'QA', 'S7', 'S8', 'VS', 'YY']
        min_len = 2
        max_len = 2


class L2110D_EB10(Element):
    """Benefit Quantity"""
    class Schema:
        json = {'title': 'Benefit Quantity',
         'usage': 'S',
         'description': 'xid=EB10 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110D_EB11(Element):
    """Authorization or Certification Indicator"""
    class Schema:
        json = {'title': 'Authorization or Certification Indicator',
         'usage': 'S',
         'description': 'xid=EB11 data_ele=1073',
         'sequence': 11,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'U', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'U', 'Y']
        min_len = 1
        max_len = 1


class L2110D_EB12(Element):
    """In Plan Network Indicator"""
    class Schema:
        json = {'title': 'In Plan Network Indicator',
         'usage': 'S',
         'description': 'xid=EB12 data_ele=1073',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'U', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'U', 'Y']
        min_len = 1
        max_len = 1


class L2110D_EB13_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=EB13-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']
        min_len = 2
        max_len = 2


class L2110D_EB13_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=EB13-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110D_EB13_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EB13_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EB13_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EB13_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EB13-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EB13_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=EB13-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110D_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'S',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 13,
         'syntax': [],
         'type': 'object',
         'properties': {'eb13_01': {'title': 'Product or Service ID Qualifier',
                                    'usage': 'R',
                                    'description': 'xid=EB13-01 data_ele=235',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/235'},
                                                       {'enum': ['AD', 'CJ', 'HC', 'ID',
                                                                 'IV', 'N4', 'ZZ']}]}},
                        'eb13_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=EB13-02 data_ele=234',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/234'}},
                        'eb13_03': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-03 data_ele=1339',
                                    'sequence': 3,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_04': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-04 data_ele=1339',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_05': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-05 data_ele=1339',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_06': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EB13-06 data_ele=1339',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eb13_07': {'title': 'Description',
                                    'usage': 'N',
                                    'description': 'xid=EB13-07 data_ele=352',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/352'}}},
         'required': ['eb13_01', 'eb13_02']}
    eb13_01: L2110D_EB13_01
    eb13_02: L2110D_EB13_02
    eb13_03: L2110D_EB13_03 | None
    eb13_04: L2110D_EB13_04 | None
    eb13_05: L2110D_EB13_05 | None
    eb13_06: L2110D_EB13_06 | None


class L2110D_EB(Segment):
    """Dependent Eligibility or Benefit Information"""
    class Schema:
        json = {'title': 'Dependent Eligibility or Benefit Information',
         'usage': 'R',
         'description': 'xid=EB name=Dependent Eligibility or Benefit Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'EB'},
                        'eb01': {'$ref': '#/$elements/L2110D_EB01'},
                        'eb02': {'$ref': '#/$elements/L2110D_EB02'},
                        'eb03': {'$ref': '#/$elements/L2110D_EB03'},
                        'eb04': {'$ref': '#/$elements/L2110D_EB04'},
                        'eb05': {'$ref': '#/$elements/L2110D_EB05'},
                        'eb06': {'$ref': '#/$elements/L2110D_EB06'},
                        'eb07': {'$ref': '#/$elements/L2110D_EB07'},
                        'eb08': {'$ref': '#/$elements/L2110D_EB08'},
                        'eb09': {'$ref': '#/$elements/L2110D_EB09'},
                        'eb10': {'$ref': '#/$elements/L2110D_EB10'},
                        'eb11': {'$ref': '#/$elements/L2110D_EB11'},
                        'eb12': {'$ref': '#/$elements/L2110D_EB12'},
                        'c003': {'$ref': '#/$elements/L2110D_C003'}},
         'required': ['eb01']}
        segment_name = 'EB'
    eb01: L2110D_EB01
    eb02: L2110D_EB02 | None
    eb03: L2110D_EB03 | None
    eb04: L2110D_EB04 | None
    eb05: L2110D_EB05 | None
    eb06: L2110D_EB06 | None
    eb07: L2110D_EB07 | None
    eb08: L2110D_EB08 | None
    eb09: L2110D_EB09 | None
    eb10: L2110D_EB10 | None
    eb11: L2110D_EB11 | None
    eb12: L2110D_EB12 | None
    c003: L2110D_C003 | None


class L2110D_HSD01(Element):
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


class L2110D_HSD02(Element):
    """Benefit Quantity"""
    class Schema:
        json = {'title': 'Benefit Quantity',
         'usage': 'S',
         'description': 'xid=HSD02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110D_HSD03(Element):
    """Unit or Basis for Measurement Code"""
    class Schema:
        json = {'title': 'Unit or Basis for Measurement Code',
         'usage': 'S',
         'description': 'xid=HSD03 data_ele=355',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/355'},
                            {'enum': ['DA', 'MO', 'VS', 'WK', 'YR']}]}}
        datatype = common.D_355
        codes = ['DA', 'MO', 'VS', 'WK', 'YR']
        min_len = 2
        max_len = 2


class L2110D_HSD04(Element):
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


class L2110D_HSD05(Element):
    """Qualifier"""
    class Schema:
        json = {'title': 'Qualifier',
         'usage': 'S',
         'description': 'xid=HSD05 data_ele=615',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/615'},
                            {'enum': ['6', '7', '21', '22', '23', '24', '25', '26',
                                      '27', '28', '29', '30', '31', '32', '33', '34',
                                      '35']}]}}
        datatype = common.D_615
        codes = ['6', '7', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
        min_len = 1
        max_len = 2


class L2110D_HSD06(Element):
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


class L2110D_HSD07(Element):
    """Delivery Frequency Code"""
    class Schema:
        json = {'title': 'Delivery Frequency Code',
         'usage': 'S',
         'description': 'xid=HSD07 data_ele=678',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/678'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                                      'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
                                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                                      'W', 'X', 'Y', 'SG', 'SL', 'SP', 'SX', 'SY',
                                      'SZ']}]}}
        datatype = common.D_678
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ']
        min_len = 1
        max_len = 2


class L2110D_HSD08(Element):
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


class L2110D_HSD(Segment):
    """Health Care Services Delivery"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Health Care Services Delivery',
                   'usage': 'S',
                   'description': 'xid=HSD name=Health Care Services Delivery',
                   'position': 135,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'HSD'},
                                  'hsd01': {'$ref': '#/$elements/L2110D_HSD01'},
                                  'hsd02': {'$ref': '#/$elements/L2110D_HSD02'},
                                  'hsd03': {'$ref': '#/$elements/L2110D_HSD03'},
                                  'hsd04': {'$ref': '#/$elements/L2110D_HSD04'},
                                  'hsd05': {'$ref': '#/$elements/L2110D_HSD05'},
                                  'hsd06': {'$ref': '#/$elements/L2110D_HSD06'},
                                  'hsd07': {'$ref': '#/$elements/L2110D_HSD07'},
                                  'hsd08': {'$ref': '#/$elements/L2110D_HSD08'}}},
         'maxItems': 9}
        segment_name = 'HSD'
    hsd01: L2110D_HSD01 | None
    hsd02: L2110D_HSD02 | None
    hsd03: L2110D_HSD03 | None
    hsd04: L2110D_HSD04 | None
    hsd05: L2110D_HSD05 | None
    hsd06: L2110D_HSD06 | None
    hsd07: L2110D_HSD07 | None
    hsd08: L2110D_HSD08 | None


class L2110D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['18', '1L', '1W', '49', '6P', '9F', 'A6', 'F6',
                                      'G1', 'IG', 'N6', 'NQ']}]}}
        datatype = common.D_128
        codes = ['18', '1L', '1W', '49', '6P', '9F', 'A6', 'F6', 'G1', 'IG', 'N6', 'NQ']
        min_len = 2
        max_len = 3


class L2110D_REF02(Element):
    """Dependent Eligibility or Benefit Identifier"""
    class Schema:
        json = {'title': 'Dependent Eligibility or Benefit Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2110D_REF03(Element):
    """Plan Sponsor Name"""
    class Schema:
        json = {'title': 'Plan Sponsor Name',
         'usage': 'S',
         'description': 'xid=REF03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110D_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110D_REF(Segment):
    """Dependent Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Dependent Additional Identification',
                   'position': 140,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2110D_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2110D_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2110D_REF03'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2110D_REF01
    ref02: L2110D_REF02
    ref03: L2110D_REF03 | None


class L2110D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['193', '194', '198', '290', '292', '295', '304',
                                      '307', '318', '348', '349', '356', '357', '435',
                                      '472', '636', '771']}]}}
        datatype = common.D_374
        codes = ['193', '194', '198', '290', '292', '295', '304', '307', '318', '348', '349', '356', '357', '435', '472', '636', '771']
        min_len = 3
        max_len = 3


class L2110D_DTP02(Element):
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


class L2110D_DTP03(Element):
    """Eligibility or Benefit Date Time Period"""
    class Schema:
        json = {'title': 'Eligibility or Benefit Date Time Period',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2110D_DTP(Segment):
    """Dependent Eligibility/Benefit Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Eligibility/Benefit Date',
                   'usage': 'S',
                   'description': 'xid=DTP name=Dependent Eligibility/Benefit Date',
                   'position': 150,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2110D_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2110D_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2110D_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 20}
        segment_name = 'DTP'
    dtp01: L2110D_DTP01
    dtp02: L2110D_DTP02
    dtp03: L2110D_DTP03


class L2110D_AAA01(Element):
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


class L2110D_AAA02(Element):
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


class L2110D_AAA03(Element):
    """Reject Reason Code"""
    class Schema:
        json = {'title': 'Reject Reason Code',
         'usage': 'R',
         'description': 'xid=AAA03 data_ele=901',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/901'},
                            {'enum': ['15', '52', '53', '54', '55', '56', '57', '60',
                                      '61', '62', '63', '69', '70']}]}}
        datatype = common.D_901
        codes = ['15', '52', '53', '54', '55', '56', '57', '60', '61', '62', '63', '69', '70']
        min_len = 2
        max_len = 2


class L2110D_AAA04(Element):
    """Follow-up Action Code"""
    class Schema:
        json = {'title': 'Follow-up Action Code',
         'usage': 'R',
         'description': 'xid=AAA04 data_ele=889',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/889'},
                            {'enum': ['C', 'N', 'R', 'W', 'X', 'Y']}]}}
        datatype = common.D_889
        codes = ['C', 'N', 'R', 'W', 'X', 'Y']
        min_len = 1
        max_len = 1


class L2110D_AAA(Segment):
    """Dependent Request Validation"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Request Validation',
                   'usage': 'S',
                   'description': 'xid=AAA name=Dependent Request Validation',
                   'position': 160,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AAA'},
                                  'aaa01': {'$ref': '#/$elements/L2110D_AAA01'},
                                  'aaa03': {'$ref': '#/$elements/L2110D_AAA03'},
                                  'aaa04': {'$ref': '#/$elements/L2110D_AAA04'}},
                   'required': ['aaa01', 'aaa03', 'aaa04']},
         'maxItems': 9}
        segment_name = 'AAA'
    aaa01: L2110D_AAA01
    aaa03: L2110D_AAA03
    aaa04: L2110D_AAA04


class L2110D_MSG01(Element):
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


class L2110D_MSG02(Element):
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


class L2110D_MSG03(Element):
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


class L2110D_MSG(Segment):
    """Message Text"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Message Text',
                   'usage': 'S',
                   'description': 'xid=MSG name=Message Text',
                   'position': 250,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'MSG'},
                                  'msg01': {'$ref': '#/$elements/L2110D_MSG01'}},
                   'required': ['msg01']},
         'maxItems': 10}
        segment_name = 'MSG'
    msg01: L2110D_MSG01


class L2115D_III01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=III01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['BF', 'BK', 'ZZ']}]}}
        datatype = common.D_1270
        codes = ['BF', 'BK', 'ZZ']
        min_len = 1
        max_len = 3


class L2115D_III02(Element):
    """Industry Code"""
    class Schema:
        json = {'title': 'Industry Code',
         'usage': 'R',
         'description': 'xid=III02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2115D_III03(Element):
    """Code Category"""
    class Schema:
        json = {'title': 'Code Category',
         'usage': 'N',
         'description': 'xid=III03 data_ele=1136',
         'sequence': 3,
         'type': {'$ref': '#/$common/1136'}}
        datatype = common.D_1136
        min_len = 2
        max_len = 2


class L2115D_III04(Element):
    """Free-Form Message Text"""
    class Schema:
        json = {'title': 'Free-Form Message Text',
         'usage': 'N',
         'description': 'xid=III04 data_ele=933',
         'sequence': 4,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2115D_III05(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=III05 data_ele=380',
         'sequence': 5,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2115D_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 6,
         'syntax': []}


class L2115D_III07(Element):
    """Surface/Layer/Position Code"""
    class Schema:
        json = {'title': 'Surface/Layer/Position Code',
         'usage': 'N',
         'description': 'xid=III07 data_ele=752',
         'sequence': 7,
         'type': {'$ref': '#/$common/752'}}
        datatype = common.D_752
        min_len = 2
        max_len = 2


class L2115D_III08(Element):
    """Surface/Layer/Position Code"""
    class Schema:
        json = {'title': 'Surface/Layer/Position Code',
         'usage': 'N',
         'description': 'xid=III08 data_ele=752',
         'sequence': 8,
         'type': {'$ref': '#/$common/752'}}
        datatype = common.D_752
        min_len = 2
        max_len = 2


class L2115D_III09(Element):
    """Surface/Layer/Position Code"""
    class Schema:
        json = {'title': 'Surface/Layer/Position Code',
         'usage': 'N',
         'description': 'xid=III09 data_ele=752',
         'sequence': 9,
         'type': {'$ref': '#/$common/752'}}
        datatype = common.D_752
        min_len = 2
        max_len = 2


class L2115D_III(Segment):
    """Dependent Eligibility or Benefit Additional Information"""
    class Schema:
        json = {'title': 'Dependent Eligibility or Benefit Additional Information',
         'usage': 'R',
         'description': 'xid=III name=Dependent Eligibility or Benefit Additional '
                        'Information',
         'position': 260,
         'type': 'object',
         'properties': {'xid': {'literal': 'III'},
                        'iii01': {'$ref': '#/$elements/L2115D_III01'},
                        'iii02': {'$ref': '#/$elements/L2115D_III02'}},
         'required': ['iii01', 'iii02']}
        segment_name = 'III'
    iii01: L2115D_III01
    iii02: L2115D_III02


class L2115D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Eligibility or Benefit Additional Information',
                   'usage': 'S',
                   'description': 'xid=2115D name=Dependent Eligibility or Benefit '
                                  'Additional Information type=None',
                   'position': 260,
                   'type': 'object',
                   'properties': {'iii': {'$ref': '#/$segments/L2115D_III'}},
                   'required': ['iii']},
         'maxItems': 10}
    iii: L2115D_III


class L2110D_LS01(Element):
    """Loop Identifier Code"""
    class Schema:
        json = {'title': 'Loop Identifier Code',
         'usage': 'R',
         'description': 'xid=LS01 data_ele=447',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/447'}, {'enum': ['2120']}]}}
        datatype = common.D_447
        codes = ['2120']
        min_len = 1
        max_len = 4


class L2110D_LS(Segment):
    """Dependent Eligibility or Benefit Information"""
    class Schema:
        json = {'title': 'Dependent Eligibility or Benefit Information',
         'usage': 'S',
         'description': 'xid=LS name=Dependent Eligibility or Benefit Information',
         'position': 330,
         'type': 'object',
         'properties': {'xid': {'literal': 'LS'},
                        'ls01': {'$ref': '#/$elements/L2110D_LS01'}},
         'required': ['ls01']}
        segment_name = 'LS'
    ls01: L2110D_LS01


class L2120D_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['13', '1P', '2B', '36', '73', 'FA', 'GP', 'IL',
                                      'LR', 'P3', 'P4', 'P5', 'PR', 'VN', 'X3', 'PRP',
                                      'SEP', 'TTP']}]}}
        datatype = common.D_98
        codes = ['13', '1P', '2B', '36', '73', 'FA', 'GP', 'IL', 'LR', 'P3', 'P4', 'P5', 'PR', 'VN', 'X3', 'PRP', 'SEP', 'TTP']
        min_len = 2
        max_len = 3


class L2120D_NM102(Element):
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


class L2120D_NM103(Element):
    """Benefit Related Entity Last or Organization Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2120D_NM104(Element):
    """Benefit Related Entity First Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2120D_NM105(Element):
    """Benefit Related Entity Middle Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2120D_NM106(Element):
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


class L2120D_NM107(Element):
    """Benefit Related Entity Name Suffix"""
    class Schema:
        json = {'title': 'Benefit Related Entity Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2120D_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['24', '34', '46', 'FA', 'FI', 'MI', 'NI', 'PI',
                                      'PP', 'SV', 'XV', 'XX', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['24', '34', '46', 'FA', 'FI', 'MI', 'NI', 'PI', 'PP', 'SV', 'XV', 'XX', 'ZZ']
        min_len = 1
        max_len = 2


class L2120D_NM109(Element):
    """Benefit Related Entity Identifier"""
    class Schema:
        json = {'title': 'Benefit Related Entity Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2120D_NM110(Element):
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


class L2120D_NM111(Element):
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


class L2120D_NM1(Segment):
    """Dependent Benefit Related Entity Name"""
    class Schema:
        json = {'title': 'Dependent Benefit Related Entity Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Dependent Benefit Related Entity Name',
         'position': 340,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2120D_NM101'},
                        'nm102': {'$ref': '#/$elements/L2120D_NM102'},
                        'nm103': {'$ref': '#/$elements/L2120D_NM103'},
                        'nm104': {'$ref': '#/$elements/L2120D_NM104'},
                        'nm105': {'$ref': '#/$elements/L2120D_NM105'},
                        'nm107': {'$ref': '#/$elements/L2120D_NM107'},
                        'nm108': {'$ref': '#/$elements/L2120D_NM108'},
                        'nm109': {'$ref': '#/$elements/L2120D_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2120D_NM101
    nm102: L2120D_NM102
    nm103: L2120D_NM103 | None
    nm104: L2120D_NM104 | None
    nm105: L2120D_NM105 | None
    nm107: L2120D_NM107 | None
    nm108: L2120D_NM108 | None
    nm109: L2120D_NM109 | None


class L2120D_N301(Element):
    """Benefit Related Entity Address Line 1"""
    class Schema:
        json = {'title': 'Benefit Related Entity Address Line 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2120D_N302(Element):
    """Benefit Related Entity Address Line 2"""
    class Schema:
        json = {'title': 'Benefit Related Entity Address Line 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2120D_N3(Segment):
    """Dependent Benefit Related Entity Address"""
    class Schema:
        json = {'title': 'Dependent Benefit Related Entity Address',
         'usage': 'S',
         'description': 'xid=N3 name=Dependent Benefit Related Entity Address',
         'position': 360,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2120D_N301'},
                        'n302': {'$ref': '#/$elements/L2120D_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2120D_N301
    n302: L2120D_N302 | None


class L2120D_N401(Element):
    """Benefit Related Entity City Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity City Name',
         'usage': 'S',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2120D_N402(Element):
    """Benefit Related Entity State Code"""
    class Schema:
        json = {'title': 'Benefit Related Entity State Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2120D_N403(Element):
    """Benefit Related Entity Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Benefit Related Entity Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2120D_N404(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2120D_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['RJ']}]}}
        datatype = common.D_309
        codes = ['RJ']
        min_len = 1
        max_len = 2


class L2120D_N406(Element):
    """Department of Defense Health Service Region Code"""
    class Schema:
        json = {'title': 'Department of Defense Health Service Region Code',
         'usage': 'S',
         'description': 'xid=N406 data_ele=310',
         'sequence': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2120D_N4(Segment):
    """Dependent Benefit Related Entity City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Dependent Benefit Related Entity City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Dependent Benefit Related Entity City/State/ZIP '
                        'Code',
         'position': 370,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2120D_N401'},
                        'n402': {'$ref': '#/$elements/L2120D_N402'},
                        'n403': {'$ref': '#/$elements/L2120D_N403'},
                        'n404': {'$ref': '#/$elements/L2120D_N404'},
                        'n405': {'$ref': '#/$elements/L2120D_N405'},
                        'n406': {'$ref': '#/$elements/L2120D_N406'}}}
        segment_name = 'N4'
    n401: L2120D_N401 | None
    n402: L2120D_N402 | None
    n403: L2120D_N403 | None
    n404: L2120D_N404 | None
    n405: L2120D_N405 | None
    n406: L2120D_N406 | None


class L2120D_PER01(Element):
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


class L2120D_PER02(Element):
    """Benefit Related Entity Contact Name"""
    class Schema:
        json = {'title': 'Benefit Related Entity Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2120D_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'FX', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'FX', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2120D_PER04(Element):
    """Benefit Related Entity Communication Number"""
    class Schema:
        json = {'title': 'Benefit Related Entity Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2120D_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2120D_PER06(Element):
    """Benefit Related Entity Communication Number"""
    class Schema:
        json = {'title': 'Benefit Related Entity Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2120D_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'EX', 'FX', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2120D_PER08(Element):
    """Benefit Related Entity Communication Number"""
    class Schema:
        json = {'title': 'Benefit Related Entity Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2120D_PER09(Element):
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


class L2120D_PER(Segment):
    """Dependent Benefit Related Entity Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Benefit Related Entity Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Dependent Benefit Related Entity '
                                  'Contact Information',
                   'position': 380,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2120D_PER01'},
                                  'per02': {'$ref': '#/$elements/L2120D_PER02'},
                                  'per03': {'$ref': '#/$elements/L2120D_PER03'},
                                  'per04': {'$ref': '#/$elements/L2120D_PER04'},
                                  'per05': {'$ref': '#/$elements/L2120D_PER05'},
                                  'per06': {'$ref': '#/$elements/L2120D_PER06'},
                                  'per07': {'$ref': '#/$elements/L2120D_PER07'},
                                  'per08': {'$ref': '#/$elements/L2120D_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2120D_PER01
    per02: L2120D_PER02 | None
    per03: L2120D_PER03 | None
    per04: L2120D_PER04 | None
    per05: L2120D_PER05 | None
    per06: L2120D_PER06 | None
    per07: L2120D_PER07 | None
    per08: L2120D_PER08 | None


class L2120D_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'},
                            {'enum': ['AD', 'H', 'R', 'AT', 'BI', 'CO', 'CV', 'HH',
                                      'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'RF', 'SB',
                                      'SK', 'SU']}]}}
        datatype = common.D_1221
        codes = ['AD', 'H', 'R', 'AT', 'BI', 'CO', 'CV', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'RF', 'SB', 'SK', 'SU']
        min_len = 1
        max_len = 3


class L2120D_PRV02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=PRV02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['9K', 'D3', 'EI', 'SY', 'TJ', 'ZZ', 'HPI']}]}}
        datatype = common.D_128
        codes = ['9K', 'D3', 'EI', 'SY', 'TJ', 'ZZ', 'HPI']
        min_len = 2
        max_len = 3


class L2120D_PRV03(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
         'description': 'xid=PRV03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2120D_PRV04(Element):
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


class L2120D_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2120D_PRV06(Element):
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


class L2120D_PRV(Segment):
    """Dependent Benefit Related Provider Information"""
    class Schema:
        json = {'title': 'Dependent Benefit Related Provider Information',
         'usage': 'S',
         'description': 'xid=PRV name=Dependent Benefit Related Provider Information',
         'position': 390,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2120D_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2120D_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2120D_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2120D_PRV01
    prv02: L2120D_PRV02
    prv03: L2120D_PRV03


class L2120D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Benefit Related Entity Name',
                   'usage': 'S',
                   'description': 'xid=2120D name=Dependent Benefit Related Entity '
                                  'Name type=None',
                   'position': 340,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2120D_NM1'},
                                  'n3': {'$ref': '#/$segments/L2120D_N3'},
                                  'n4': {'$ref': '#/$segments/L2120D_N4'},
                                  'per': {'$ref': '#/$segments/L2120D_PER'},
                                  'prv': {'$ref': '#/$segments/L2120D_PRV'}}},
         'maxItems': 1}
    nm1: L2120D_NM1 | None
    n3: L2120D_N3 | None
    n4: L2120D_N4 | None
    per: list[L2120D_PER] | None
    prv: L2120D_PRV | None


class L2110D_LE01(Element):
    """Loop Identifier Code"""
    class Schema:
        json = {'title': 'Loop Identifier Code',
         'usage': 'R',
         'description': 'xid=LE01 data_ele=447',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/447'}, {'enum': ['2120']}]}}
        datatype = common.D_447
        codes = ['2120']
        min_len = 1
        max_len = 4


class L2110D_LE(Segment):
    """Loop Trailer"""
    class Schema:
        json = {'title': 'Loop Trailer',
         'usage': 'S',
         'description': 'xid=LE name=Loop Trailer',
         'position': 400,
         'type': 'object',
         'properties': {'xid': {'literal': 'LE'},
                        'le01': {'$ref': '#/$elements/L2110D_LE01'}},
         'required': ['le01']}
        segment_name = 'LE'
    le01: L2110D_LE01


class L2110D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Eligibility or Benefit Information',
                   'usage': 'S',
                   'description': 'xid=2110D name=Dependent Eligibility or Benefit '
                                  'Information type=None',
                   'position': 130,
                   'type': 'object',
                   'properties': {'eb': {'$ref': '#/$segments/L2110D_EB'},
                                  'hsd': {'$ref': '#/$segments/L2110D_HSD'},
                                  'ref': {'$ref': '#/$segments/L2110D_REF'},
                                  'dtp': {'$ref': '#/$segments/L2110D_DTP'},
                                  'aaa': {'$ref': '#/$segments/L2110D_AAA'},
                                  'msg': {'$ref': '#/$segments/L2110D_MSG'},
                                  'l2115d': {'$ref': '#/$segments/L2115D'},
                                  'ls': {'$ref': '#/$segments/L2110D_LS'},
                                  'l2120d': {'$ref': '#/$segments/L2120D'},
                                  'le': {'$ref': '#/$segments/L2110D_LE'}},
                   'required': ['eb']}}
    eb: L2110D_EB
    hsd: list[L2110D_HSD] | None
    ref: list[L2110D_REF] | None
    dtp: list[L2110D_DTP] | None
    aaa: list[L2110D_AAA] | None
    msg: list[L2110D_MSG] | None
    l2115d: list[L2115D] | None
    ls: L2110D_LS | None
    l2120d: list[L2120D] | None
    le: L2110D_LE | None


class L2100D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Name',
                   'usage': 'R',
                   'description': 'xid=2100D name=Dependent Name type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100D_NM1'},
                                  'ref': {'$ref': '#/$segments/L2100D_REF'},
                                  'n3': {'$ref': '#/$segments/L2100D_N3'},
                                  'n4': {'$ref': '#/$segments/L2100D_N4'},
                                  'per': {'$ref': '#/$segments/L2100D_PER'},
                                  'aaa': {'$ref': '#/$segments/L2100D_AAA'},
                                  'dmg': {'$ref': '#/$segments/L2100D_DMG'},
                                  'ins': {'$ref': '#/$segments/L2100D_INS'},
                                  'dtp': {'$ref': '#/$segments/L2100D_DTP'},
                                  'l2110d': {'$ref': '#/$segments/L2110D'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100D_NM1
    ref: list[L2100D_REF] | None
    n3: L2100D_N3 | None
    n4: L2100D_N4 | None
    per: list[L2100D_PER] | None
    aaa: list[L2100D_AAA] | None
    dmg: L2100D_DMG | None
    ins: L2100D_INS | None
    dtp: list[L2100D_DTP] | None
    l2110d: list[L2110D] | None


class L2000D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Level',
                   'usage': 'S',
                   'description': 'xid=2000D name=Dependent Level type=None',
                   'position': 40,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000D_HL'},
                                  'trn': {'$ref': '#/$segments/L2000D_TRN'},
                                  'l2100d': {'$ref': '#/$segments/L2100D'}},
                   'required': ['hl', 'l2100d']}}
    hl: L2000D_HL
    trn: list[L2000D_TRN] | None
    l2100d: list[L2100D]


class L2000C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Level',
                   'usage': 'S',
                   'description': 'xid=2000C name=Subscriber Level type=None',
                   'position': 40,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000C_HL'},
                                  'trn': {'$ref': '#/$segments/L2000C_TRN'},
                                  'l2100c': {'$ref': '#/$segments/L2100C'},
                                  'l2000d': {'$ref': '#/$segments/L2000D'}},
                   'required': ['hl', 'l2100c']}}
    hl: L2000C_HL
    trn: list[L2000C_TRN] | None
    l2100c: list[L2100C]
    l2000d: list[L2000D] | None


class L2000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Level',
                   'usage': 'S',
                   'description': 'xid=2000B name=Information Receiver Level type=None',
                   'position': 40,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000B_HL'},
                                  'l2100b': {'$ref': '#/$segments/L2100B'},
                                  'l2000c': {'$ref': '#/$segments/L2000C'}},
                   'required': ['hl', 'l2100b']}}
    hl: L2000B_HL
    l2100b: list[L2100B]
    l2000c: list[L2000C] | None


class L2000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Source Level',
                   'usage': 'R',
                   'description': 'xid=2000A name=Information Source Level type=None',
                   'position': 10,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000A_HL'},
                                  'aaa': {'$ref': '#/$segments/L2000A_AAA'},
                                  'l2100a': {'$ref': '#/$segments/L2100A'},
                                  'l2000b': {'$ref': '#/$segments/L2000B'}},
                   'required': ['hl', 'l2100a']}}
    hl: L2000A_HL
    aaa: list[L2000A_AAA] | None
    l2100a: list[L2100A]
    l2000b: list[L2000B] | None


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
         'position': 410,
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


class MSG271(Message):
    """HIPAA Health Care Eligibility Benefit Response X092A1-271"""
    class Schema:
        json = {'title': 'HIPAA Health Care Eligibility Benefit Response X092A1-271',
         'description': 'xid=271 name=HIPAA Health Care Eligibility Benefit Response '
                        'X092A1-271',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
