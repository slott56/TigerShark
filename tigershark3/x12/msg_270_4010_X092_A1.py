"""
270.4010.X092.A1
Created 2023-03-25 09:22:27.877147
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
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['HS']}]}}
        datatype = common.D_479
        codes = ['HS']
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
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['270']}]}}
        datatype = common.D_143
        codes = ['270']
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
         'type': {'allOf': [{'$ref': '#/$common/353'}, {'enum': ['01', '13', '36']}]}}
        datatype = common.D_353
        codes = ['01', '13', '36']
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
         'usage': 'S',
         'description': 'xid=BHT06 data_ele=640',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/640'}, {'enum': ['RT', 'RU']}]}}
        datatype = common.D_640
        codes = ['RT', 'RU']
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
         'required': ['bht01', 'bht02', 'bht04', 'bht05']}
        segment_name = 'BHT'
    bht01: HEADER_BHT01
    bht02: HEADER_BHT02
    bht03: HEADER_BHT03 | None
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


class L2100A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Source Name',
                   'usage': 'R',
                   'description': 'xid=2100A name=Information Source Name type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100A_NM1'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100A_NM1


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


class L2100B_N301(Element):
    """Information Receiver Address Line"""
    class Schema:
        json = {'title': 'Information Receiver Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100B_N302(Element):
    """Information Receiver Additional Address Line"""
    class Schema:
        json = {'title': 'Information Receiver Additional Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100B_N3(Segment):
    """Information Receiver Address"""
    class Schema:
        json = {'title': 'Information Receiver Address',
         'usage': 'S',
         'description': 'xid=N3 name=Information Receiver Address',
         'position': 60,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100B_N301'},
                        'n302': {'$ref': '#/$elements/L2100B_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100B_N301
    n302: L2100B_N302 | None


class L2100B_N401(Element):
    """Information Receiver City Name"""
    class Schema:
        json = {'title': 'Information Receiver City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100B_N402(Element):
    """Information Receiver State Code"""
    class Schema:
        json = {'title': 'Information Receiver State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100B_N403(Element):
    """Information Receiver Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Information Receiver Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100B_N404(Element):
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


class L2100B_N405(Element):
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


class L2100B_N406(Element):
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


class L2100B_N4(Segment):
    """Information Receiver City/State/Zip Code"""
    class Schema:
        json = {'title': 'Information Receiver City/State/Zip Code',
         'usage': 'S',
         'description': 'xid=N4 name=Information Receiver City/State/Zip Code',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100B_N401'},
                        'n402': {'$ref': '#/$elements/L2100B_N402'},
                        'n403': {'$ref': '#/$elements/L2100B_N403'},
                        'n404': {'$ref': '#/$elements/L2100B_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2100B_N401
    n402: L2100B_N402
    n403: L2100B_N403
    n404: L2100B_N404 | None


class L2100B_PER01(Element):
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


class L2100B_PER02(Element):
    """Information Receiver Contact Name"""
    class Schema:
        json = {'title': 'Information Receiver Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100B_PER03(Element):
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


class L2100B_PER04(Element):
    """Information Receiver Communication Number"""
    class Schema:
        json = {'title': 'Information Receiver Communication Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100B_PER05(Element):
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


class L2100B_PER06(Element):
    """Information Receiver Communication Number"""
    class Schema:
        json = {'title': 'Information Receiver Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100B_PER07(Element):
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


class L2100B_PER08(Element):
    """Information Receiver Communication Number"""
    class Schema:
        json = {'title': 'Information Receiver Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100B_PER09(Element):
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


class L2100B_PER(Segment):
    """Information Receiver Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Information Receiver Contact '
                                  'Information',
                   'position': 80,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2100B_PER01'},
                                  'per02': {'$ref': '#/$elements/L2100B_PER02'},
                                  'per03': {'$ref': '#/$elements/L2100B_PER03'},
                                  'per04': {'$ref': '#/$elements/L2100B_PER04'},
                                  'per05': {'$ref': '#/$elements/L2100B_PER05'},
                                  'per06': {'$ref': '#/$elements/L2100B_PER06'},
                                  'per07': {'$ref': '#/$elements/L2100B_PER07'},
                                  'per08': {'$ref': '#/$elements/L2100B_PER08'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2100B_PER01
    per02: L2100B_PER02 | None
    per03: L2100B_PER03 | None
    per04: L2100B_PER04 | None
    per05: L2100B_PER05 | None
    per06: L2100B_PER06 | None
    per07: L2100B_PER07 | None
    per08: L2100B_PER08 | None


class L2100B_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'},
                            {'enum': ['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA',
                                      'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB',
                                      'SK', 'SU']}]}}
        datatype = common.D_1221
        codes = ['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB', 'SK', 'SU']
        min_len = 1
        max_len = 3


class L2100B_PRV02(Element):
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


class L2100B_PRV03(Element):
    """Receiver Provider Specialty Code"""
    class Schema:
        json = {'title': 'Receiver Provider Specialty Code',
         'usage': 'R',
         'description': 'xid=PRV03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2100B_PRV04(Element):
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


class L2100B_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2100B_PRV06(Element):
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


class L2100B_PRV(Segment):
    """Information Receiver Provider Information"""
    class Schema:
        json = {'title': 'Information Receiver Provider Information',
         'usage': 'S',
         'description': 'xid=PRV name=Information Receiver Provider Information',
         'position': 90,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2100B_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2100B_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2100B_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2100B_PRV01
    prv02: L2100B_PRV02
    prv03: L2100B_PRV03


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
                                  'n3': {'$ref': '#/$segments/L2100B_N3'},
                                  'n4': {'$ref': '#/$segments/L2100B_N4'},
                                  'per': {'$ref': '#/$segments/L2100B_PER'},
                                  'prv': {'$ref': '#/$segments/L2100B_PRV'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100B_NM1
    ref: list[L2100B_REF] | None
    n3: L2100B_N3 | None
    n4: L2100B_N4 | None
    per: list[L2100B_PER] | None
    prv: L2100B_PRV | None


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
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['1']}]}}
        datatype = common.D_481
        codes = ['1']
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
         'maxItems': 2}
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
                            {'enum': ['18', '1L', '1W', '49', '6P', 'A6', 'CT', 'EA',
                                      'EJ', 'F6', 'GH', 'HJ', 'IG', 'N6', 'NQ',
                                      'SY']}]}}
        datatype = common.D_128
        codes = ['18', '1L', '1W', '49', '6P', 'A6', 'CT', 'EA', 'EJ', 'F6', 'GH', 'HJ', 'IG', 'N6', 'NQ', 'SY']
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
                                  'ref02': {'$ref': '#/$elements/L2100C_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2100C_REF01
    ref02: L2100C_REF02


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
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'$ref': '#/$common/309'}}
        datatype = common.D_309
        min_len = 1
        max_len = 2


class L2100C_N406(Element):
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
                        'n404': {'$ref': '#/$elements/L2100C_N404'}}}
        segment_name = 'N4'
    n401: L2100C_N401 | None
    n402: L2100C_N402 | None
    n403: L2100C_N403 | None
    n404: L2100C_N404 | None


class L2100C_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'},
                            {'enum': ['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA',
                                      'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB',
                                      'SK', 'SU']}]}}
        datatype = common.D_1221
        codes = ['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB', 'SK', 'SU']
        min_len = 1
        max_len = 3


class L2100C_PRV02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=PRV02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['9K', 'D3', 'EI', 'HPI', 'SY', 'TJ', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['9K', 'D3', 'EI', 'HPI', 'SY', 'TJ', 'ZZ']
        min_len = 2
        max_len = 3


class L2100C_PRV03(Element):
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


class L2100C_PRV04(Element):
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


class L2100C_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2100C_PRV06(Element):
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


class L2100C_PRV(Segment):
    """Provider Information"""
    class Schema:
        json = {'title': 'Provider Information',
         'usage': 'S',
         'description': 'xid=PRV name=Provider Information',
         'position': 90,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2100C_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2100C_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2100C_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2100C_PRV01
    prv02: L2100C_PRV02
    prv03: L2100C_PRV03


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
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M']}]}}
        datatype = common.D_1068
        codes = ['F', 'M']
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
         'usage': 'N',
         'description': 'xid=INS03 data_ele=875',
         'sequence': 3,
         'type': {'$ref': '#/$common/875'}}
        datatype = common.D_875
        min_len = 3
        max_len = 3


class L2100C_INS04(Element):
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
    """Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying"""
    class Schema:
        json = {'title': 'Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying',
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
         'usage': 'N',
         'description': 'xid=INS09 data_ele=1220',
         'sequence': 9,
         'type': {'$ref': '#/$common/1220'}}
        datatype = common.D_1220
        min_len = 1
        max_len = 1


class L2100C_INS10(Element):
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
         'usage': 'R',
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
                        'ins17': {'$ref': '#/$elements/L2100C_INS17'}},
         'required': ['ins01', 'ins02', 'ins17']}
        segment_name = 'INS'
    ins01: L2100C_INS01
    ins02: L2100C_INS02
    ins17: L2100C_INS17


class L2100C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['102', '307', '435', '472']}]}}
        datatype = common.D_374
        codes = ['102', '307', '435', '472']
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
         'maxItems': 2}
        segment_name = 'DTP'
    dtp01: L2100C_DTP01
    dtp02: L2100C_DTP02
    dtp03: L2100C_DTP03


class L2110C_EQ01(Element):
    """Service Type Code"""
    class Schema:
        json = {'title': 'Service Type Code',
         'usage': 'S',
         'description': 'xid=EQ01 data_ele=1365',
         'sequence': 1,
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


class L2110C_EQ02_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=EQ02-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']
        min_len = 2
        max_len = 2


class L2110C_EQ02_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=EQ02-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110C_EQ02_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EQ02_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EQ02_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EQ02_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110C_EQ02_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=EQ02-07 data_ele=352',
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
         'sequence': 2,
         'syntax': [],
         'type': 'object',
         'properties': {'eq02_01': {'title': 'Product or Service ID Qualifier',
                                    'usage': 'R',
                                    'description': 'xid=EQ02-01 data_ele=235',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/235'},
                                                       {'enum': ['AD', 'CJ', 'HC', 'ID',
                                                                 'IV', 'N4', 'ZZ']}]}},
                        'eq02_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=EQ02-02 data_ele=234',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/234'}},
                        'eq02_03': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-03 data_ele=1339',
                                    'sequence': 3,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_04': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-04 data_ele=1339',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_05': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-05 data_ele=1339',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_06': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-06 data_ele=1339',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_07': {'title': 'Description',
                                    'usage': 'N',
                                    'description': 'xid=EQ02-07 data_ele=352',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/352'}}},
         'required': ['eq02_01', 'eq02_02']}
    eq02_01: L2110C_EQ02_01
    eq02_02: L2110C_EQ02_02
    eq02_03: L2110C_EQ02_03 | None
    eq02_04: L2110C_EQ02_04 | None
    eq02_05: L2110C_EQ02_05 | None
    eq02_06: L2110C_EQ02_06 | None


class L2110C_EQ03(Element):
    """Benefit Coverage Level Code"""
    class Schema:
        json = {'title': 'Benefit Coverage Level Code',
         'usage': 'S',
         'description': 'xid=EQ03 data_ele=1207',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1207'},
                            {'enum': ['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND',
                                      'SPC', 'SPO']}]}}
        datatype = common.D_1207
        codes = ['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO']
        min_len = 3
        max_len = 3


class L2110C_EQ04(Element):
    """Insurance Type Code"""
    class Schema:
        json = {'title': 'Insurance Type Code',
         'usage': 'S',
         'description': 'xid=EQ04 data_ele=1336',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1336'},
                            {'enum': ['AP', 'C1', 'CO', 'GP', 'HM', 'HN', 'IP', 'MA',
                                      'MB', 'MC', 'PR', 'PS', 'SP', 'WC']}]}}
        datatype = common.D_1336
        codes = ['AP', 'C1', 'CO', 'GP', 'HM', 'HN', 'IP', 'MA', 'MB', 'MC', 'PR', 'PS', 'SP', 'WC']
        min_len = 1
        max_len = 3


class L2110C_EQ(Segment):
    """Subscriber Eligibility or Benefit Inquiry Information"""
    class Schema:
        json = {'title': 'Subscriber Eligibility or Benefit Inquiry Information',
         'usage': 'R',
         'description': 'xid=EQ name=Subscriber Eligibility or Benefit Inquiry '
                        'Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'EQ'},
                        'eq01': {'$ref': '#/$elements/L2110C_EQ01'},
                        'c003': {'$ref': '#/$elements/L2110C_C003'},
                        'eq03': {'$ref': '#/$elements/L2110C_EQ03'},
                        'eq04': {'$ref': '#/$elements/L2110C_EQ04'}}}
        segment_name = 'EQ'
    eq01: L2110C_EQ01 | None
    c003: L2110C_C003 | None
    eq03: L2110C_EQ03 | None
    eq04: L2110C_EQ04 | None


class L2110C_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['R']}]}}
        datatype = common.D_522
        codes = ['R']
        min_len = 1
        max_len = 3


class L2110C_AMT02(Element):
    """Spend Down Amount"""
    class Schema:
        json = {'title': 'Spend Down Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2110C_AMT03(Element):
    """Credit/Debit Flag Code"""
    class Schema:
        json = {'title': 'Credit/Debit Flag Code',
         'usage': 'N',
         'description': 'xid=AMT03 data_ele=478',
         'sequence': 3,
         'type': {'$ref': '#/$common/478'}}
        datatype = common.D_478
        min_len = 1
        max_len = 1


class L2110C_AMT(Segment):
    """Subscriber Spend Down Amount"""
    class Schema:
        json = {'title': 'Subscriber Spend Down Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Subscriber Spend Down Amount',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2110C_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2110C_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2110C_AMT01
    amt02: L2110C_AMT02


class L2110C_III01(Element):
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


class L2110C_III02(Element):
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


class L2110C_III03(Element):
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


class L2110C_III04(Element):
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


class L2110C_III05(Element):
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


class L2110C_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 6,
         'syntax': []}


class L2110C_III07(Element):
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


class L2110C_III08(Element):
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


class L2110C_III09(Element):
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


class L2110C_III(Segment):
    """Subscriber Eligibility or Benefit Additional Inquiry Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Eligibility or Benefit Additional Inquiry '
                            'Information',
                   'usage': 'S',
                   'description': 'xid=III name=Subscriber Eligibility or Benefit '
                                  'Additional Inquiry Information',
                   'position': 170,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'III'},
                                  'iii01': {'$ref': '#/$elements/L2110C_III01'},
                                  'iii02': {'$ref': '#/$elements/L2110C_III02'}},
                   'required': ['iii01', 'iii02']},
         'maxItems': 10}
        segment_name = 'III'
    iii01: L2110C_III01
    iii02: L2110C_III02


class L2110C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['9F', 'G1']}]}}
        datatype = common.D_128
        codes = ['9F', 'G1']
        min_len = 2
        max_len = 3


class L2110C_REF02(Element):
    """Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2110C_REF03(Element):
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


class L2110C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110C_REF(Segment):
    """Subscriber Additional Information"""
    class Schema:
        json = {'title': 'Subscriber Additional Information',
         'usage': 'S',
         'description': 'xid=REF name=Subscriber Additional Information',
         'position': 190,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2110C_REF01'},
                        'ref02': {'$ref': '#/$elements/L2110C_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2110C_REF01
    ref02: L2110C_REF02


class L2110C_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['307', '435', '472']}]}}
        datatype = common.D_374
        codes = ['307', '435', '472']
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


class L2110C_DTP(Segment):
    """Subscriber Eligibility/Benefit Date"""
    class Schema:
        json = {'title': 'Subscriber Eligibility/Benefit Date',
         'usage': 'S',
         'description': 'xid=DTP name=Subscriber Eligibility/Benefit Date',
         'position': 200,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2110C_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2110C_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2110C_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2110C_DTP01
    dtp02: L2110C_DTP02
    dtp03: L2110C_DTP03


class L2110C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Eligibility or Benefit Inquiry Information',
                   'usage': 'S',
                   'description': 'xid=2110C name=Subscriber Eligibility or Benefit '
                                  'Inquiry Information type=None',
                   'position': 130,
                   'type': 'object',
                   'properties': {'eq': {'$ref': '#/$segments/L2110C_EQ'},
                                  'amt': {'$ref': '#/$segments/L2110C_AMT'},
                                  'iii': {'$ref': '#/$segments/L2110C_III'},
                                  'ref': {'$ref': '#/$segments/L2110C_REF'},
                                  'dtp': {'$ref': '#/$segments/L2110C_DTP'}},
                   'required': ['eq']},
         'maxItems': 99}
    eq: L2110C_EQ
    amt: L2110C_AMT | None
    iii: list[L2110C_III] | None
    ref: L2110C_REF | None
    dtp: L2110C_DTP | None


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
                                  'prv': {'$ref': '#/$segments/L2100C_PRV'},
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
    prv: L2100C_PRV | None
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
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['1']}]}}
        datatype = common.D_481
        codes = ['1']
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
         'maxItems': 2}
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
         'usage': 'N',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L2100D_NM109(Element):
    """Identification Code"""
    class Schema:
        json = {'title': 'Identification Code',
         'usage': 'N',
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
                        'nm107': {'$ref': '#/$elements/L2100D_NM107'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100D_NM101
    nm102: L2100D_NM102
    nm103: L2100D_NM103 | None
    nm104: L2100D_NM104 | None
    nm105: L2100D_NM105 | None
    nm107: L2100D_NM107 | None


class L2100D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['18', '1L', '6P', 'A6', 'CT', 'EA', 'EJ', 'F6',
                                      'GH', 'HJ', 'IF', 'IG', 'N6', 'SY']}]}}
        datatype = common.D_128
        codes = ['18', '1L', '6P', 'A6', 'CT', 'EA', 'EJ', 'F6', 'GH', 'HJ', 'IF', 'IG', 'N6', 'SY']
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
                                  'ref02': {'$ref': '#/$elements/L2100D_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 9}
        segment_name = 'REF'
    ref01: L2100D_REF01
    ref02: L2100D_REF02


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


class L2100D_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'},
                            {'enum': ['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA',
                                      'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB',
                                      'SK', 'SU']}]}}
        datatype = common.D_1221
        codes = ['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB', 'SK', 'SU']
        min_len = 1
        max_len = 3


class L2100D_PRV02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=PRV02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['9K', 'D3', 'EI', 'HPI', 'SY', 'TJ', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['9K', 'D3', 'EI', 'HPI', 'SY', 'TJ', 'ZZ']
        min_len = 2
        max_len = 3


class L2100D_PRV03(Element):
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


class L2100D_PRV04(Element):
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


class L2100D_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2100D_PRV06(Element):
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


class L2100D_PRV(Segment):
    """Provider Information"""
    class Schema:
        json = {'title': 'Provider Information',
         'usage': 'S',
         'description': 'xid=PRV name=Provider Information',
         'position': 90,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2100D_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2100D_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2100D_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2100D_PRV01
    prv02: L2100D_PRV02
    prv03: L2100D_PRV03


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
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M']}]}}
        datatype = common.D_1068
        codes = ['F', 'M']
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
         'type': {'allOf': [{'$ref': '#/$common/1069'}, {'enum': ['01', '19', '34']}]}}
        datatype = common.D_1069
        codes = ['01', '19', '34']
        min_len = 2
        max_len = 2


class L2100D_INS03(Element):
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


class L2100D_INS04(Element):
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
    """Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying"""
    class Schema:
        json = {'title': 'Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying',
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
         'usage': 'N',
         'description': 'xid=INS09 data_ele=1220',
         'sequence': 9,
         'type': {'$ref': '#/$common/1220'}}
        datatype = common.D_1220
        min_len = 1
        max_len = 1


class L2100D_INS10(Element):
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
                        'ins17': {'$ref': '#/$elements/L2100D_INS17'}},
         'required': ['ins01', 'ins02']}
        segment_name = 'INS'
    ins01: L2100D_INS01
    ins02: L2100D_INS02
    ins17: L2100D_INS17 | None


class L2100D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['102', '307', '435', '472']}]}}
        datatype = common.D_374
        codes = ['102', '307', '435', '472']
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
         'maxItems': 2}
        segment_name = 'DTP'
    dtp01: L2100D_DTP01
    dtp02: L2100D_DTP02
    dtp03: L2100D_DTP03


class L2110D_EQ01(Element):
    """Service Type Code"""
    class Schema:
        json = {'title': 'Service Type Code',
         'usage': 'S',
         'description': 'xid=EQ01 data_ele=1365',
         'sequence': 1,
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


class L2110D_EQ02_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=EQ02-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ']
        min_len = 2
        max_len = 2


class L2110D_EQ02_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=EQ02-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110D_EQ02_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EQ02_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EQ02_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EQ02_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=EQ02-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110D_EQ02_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=EQ02-07 data_ele=352',
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
         'sequence': 2,
         'syntax': [],
         'type': 'object',
         'properties': {'eq02_01': {'title': 'Product or Service ID Qualifier',
                                    'usage': 'R',
                                    'description': 'xid=EQ02-01 data_ele=235',
                                    'sequence': 1,
                                    'type': {'allOf': [{'$ref': '#/$common/235'},
                                                       {'enum': ['AD', 'CJ', 'HC', 'ID',
                                                                 'IV', 'N4', 'ZZ']}]}},
                        'eq02_02': {'title': 'Procedure Code',
                                    'usage': 'R',
                                    'description': 'xid=EQ02-02 data_ele=234',
                                    'sequence': 2,
                                    'type': {'$ref': '#/$common/234'}},
                        'eq02_03': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-03 data_ele=1339',
                                    'sequence': 3,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_04': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-04 data_ele=1339',
                                    'sequence': 4,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_05': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-05 data_ele=1339',
                                    'sequence': 5,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_06': {'title': 'Procedure Modifier',
                                    'usage': 'S',
                                    'description': 'xid=EQ02-06 data_ele=1339',
                                    'sequence': 6,
                                    'type': {'$ref': '#/$common/1339'}},
                        'eq02_07': {'title': 'Description',
                                    'usage': 'N',
                                    'description': 'xid=EQ02-07 data_ele=352',
                                    'sequence': 7,
                                    'type': {'$ref': '#/$common/352'}}},
         'required': ['eq02_01', 'eq02_02']}
    eq02_01: L2110D_EQ02_01
    eq02_02: L2110D_EQ02_02
    eq02_03: L2110D_EQ02_03 | None
    eq02_04: L2110D_EQ02_04 | None
    eq02_05: L2110D_EQ02_05 | None
    eq02_06: L2110D_EQ02_06 | None


class L2110D_EQ03(Element):
    """Benefit Coverage Level Code"""
    class Schema:
        json = {'title': 'Benefit Coverage Level Code',
         'usage': 'S',
         'description': 'xid=EQ03 data_ele=1207',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1207'},
                            {'enum': ['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND',
                                      'SPC', 'SPO']}]}}
        datatype = common.D_1207
        codes = ['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO']
        min_len = 3
        max_len = 3


class L2110D_EQ04(Element):
    """Insurance Type Code"""
    class Schema:
        json = {'title': 'Insurance Type Code',
         'usage': 'S',
         'description': 'xid=EQ04 data_ele=1336',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1336'},
                            {'enum': ['AP', 'C1', 'CO', 'GP', 'HM', 'IP', 'MA', 'MB',
                                      'MC', 'PR', 'PS', 'SP', 'WC']}]}}
        datatype = common.D_1336
        codes = ['AP', 'C1', 'CO', 'GP', 'HM', 'IP', 'MA', 'MB', 'MC', 'PR', 'PS', 'SP', 'WC']
        min_len = 1
        max_len = 3


class L2110D_EQ(Segment):
    """Dependent Eligibility or Benefit Inquiry Information"""
    class Schema:
        json = {'title': 'Dependent Eligibility or Benefit Inquiry Information',
         'usage': 'R',
         'description': 'xid=EQ name=Dependent Eligibility or Benefit Inquiry '
                        'Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'EQ'},
                        'eq01': {'$ref': '#/$elements/L2110D_EQ01'},
                        'c003': {'$ref': '#/$elements/L2110D_C003'},
                        'eq03': {'$ref': '#/$elements/L2110D_EQ03'},
                        'eq04': {'$ref': '#/$elements/L2110D_EQ04'}}}
        segment_name = 'EQ'
    eq01: L2110D_EQ01 | None
    c003: L2110D_C003 | None
    eq03: L2110D_EQ03 | None
    eq04: L2110D_EQ04 | None


class L2110D_III01(Element):
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


class L2110D_III02(Element):
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


class L2110D_III03(Element):
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


class L2110D_III04(Element):
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


class L2110D_III05(Element):
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


class L2110D_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 6,
         'syntax': []}


class L2110D_III07(Element):
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


class L2110D_III08(Element):
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


class L2110D_III09(Element):
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


class L2110D_III(Segment):
    """Dependent Eligibility or Benefit Additional Inquiry Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Eligibility or Benefit Additional Inquiry '
                            'Information',
                   'usage': 'S',
                   'description': 'xid=III name=Dependent Eligibility or Benefit '
                                  'Additional Inquiry Information',
                   'position': 170,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'III'},
                                  'iii01': {'$ref': '#/$elements/L2110D_III01'},
                                  'iii02': {'$ref': '#/$elements/L2110D_III02'}},
                   'required': ['iii01', 'iii02']},
         'maxItems': 10}
        segment_name = 'III'
    iii01: L2110D_III01
    iii02: L2110D_III02


class L2110D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['9F', 'G1']}]}}
        datatype = common.D_128
        codes = ['9F', 'G1']
        min_len = 2
        max_len = 3


class L2110D_REF02(Element):
    """Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2110D_REF03(Element):
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


class L2110D_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110D_REF(Segment):
    """Dependent Additional Information"""
    class Schema:
        json = {'title': 'Dependent Additional Information',
         'usage': 'S',
         'description': 'xid=REF name=Dependent Additional Information',
         'position': 190,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2110D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2110D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2110D_REF01
    ref02: L2110D_REF02


class L2110D_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['307', '435', '472']}]}}
        datatype = common.D_374
        codes = ['307', '435', '472']
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


class L2110D_DTP(Segment):
    """Dependent Eligibility/Benefit Date"""
    class Schema:
        json = {'title': 'Dependent Eligibility/Benefit Date',
         'usage': 'S',
         'description': 'xid=DTP name=Dependent Eligibility/Benefit Date',
         'position': 200,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2110D_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2110D_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2110D_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2110D_DTP01
    dtp02: L2110D_DTP02
    dtp03: L2110D_DTP03


class L2110D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Eligibility or Benefit Inquiry Information',
                   'usage': 'R',
                   'description': 'xid=2110D name=Dependent Eligibility or Benefit '
                                  'Inquiry Information type=None',
                   'position': 130,
                   'type': 'object',
                   'properties': {'eq': {'$ref': '#/$segments/L2110D_EQ'},
                                  'iii': {'$ref': '#/$segments/L2110D_III'},
                                  'ref': {'$ref': '#/$segments/L2110D_REF'},
                                  'dtp': {'$ref': '#/$segments/L2110D_DTP'}},
                   'required': ['eq']},
         'maxItems': 99}
    eq: L2110D_EQ
    iii: list[L2110D_III] | None
    ref: L2110D_REF | None
    dtp: L2110D_DTP | None


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
                                  'prv': {'$ref': '#/$segments/L2100D_PRV'},
                                  'dmg': {'$ref': '#/$segments/L2100D_DMG'},
                                  'ins': {'$ref': '#/$segments/L2100D_INS'},
                                  'dtp': {'$ref': '#/$segments/L2100D_DTP'},
                                  'l2110d': {'$ref': '#/$segments/L2110D'}},
                   'required': ['nm1', 'l2110d']},
         'maxItems': 1}
    nm1: L2100D_NM1
    ref: list[L2100D_REF] | None
    n3: L2100D_N3 | None
    n4: L2100D_N4 | None
    prv: L2100D_PRV | None
    dmg: L2100D_DMG | None
    ins: L2100D_INS | None
    dtp: list[L2100D_DTP] | None
    l2110d: list[L2110D]


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
                   'usage': 'R',
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
                   'usage': 'R',
                   'description': 'xid=2000B name=Information Receiver Level type=None',
                   'position': 40,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000B_HL'},
                                  'l2100b': {'$ref': '#/$segments/L2100B'},
                                  'l2000c': {'$ref': '#/$segments/L2000C'}},
                   'required': ['hl', 'l2100b', 'l2000c']}}
    hl: L2000B_HL
    l2100b: list[L2100B]
    l2000c: list[L2000C]


class L2000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Source Level',
                   'usage': 'R',
                   'description': 'xid=2000A name=Information Source Level type=None',
                   'position': 10,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000A_HL'},
                                  'l2100a': {'$ref': '#/$segments/L2100A'},
                                  'l2000b': {'$ref': '#/$segments/L2000B'}},
                   'required': ['hl', 'l2100a', 'l2000b']}}
    hl: L2000A_HL
    l2100a: list[L2100A]
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
         'position': 210,
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


class MSG270(Message):
    """HIPAA Health Care Eligibility Inquiry X092A1-270"""
    class Schema:
        json = {'title': 'HIPAA Health Care Eligibility Inquiry X092A1-270',
         'description': 'xid=270 name=HIPAA Health Care Eligibility Inquiry X092A1-270',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
