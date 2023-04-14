"""
277.5010.X212
Created 2023-03-25 09:22:27.998908
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
         'description': 'xid=ISA11 data_ele=I65',
         'sequence': 11,
         'type': {'$ref': '#/$common/I65'}}
        datatype = common.I65
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA12(Element):
    """Interchange Control Version Number"""
    class Schema:
        json = {'title': 'Interchange Control Version Number',
         'usage': 'R',
         'description': 'xid=ISA12 data_ele=I11',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/I11'}, {'enum': ['00501']}]}}
        datatype = common.I11
        codes = ['00501']
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
         'position': 100,
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
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['RA']}]}}
        datatype = common.D_479
        codes = ['RA']
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
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['005010X218']}]}}
        datatype = common.D_480
        codes = ['005010X218']
        min_len = 1
        max_len = 12


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    class Schema:
        json = {'title': 'Functional Group Header',
         'usage': 'R',
         'description': 'xid=GS name=Functional Group Header',
         'position': 100,
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
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['277']}]}}
        datatype = common.D_143
        codes = ['277']
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


class ST_LOOP_ST03(Element):
    """Version, Release, or Industry Identifier"""
    class Schema:
        json = {'title': 'Version, Release, or Industry Identifier',
         'usage': 'R',
         'description': 'xid=ST03 data_ele=1705',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1705'}, {'enum': ['005010X212']}]}}
        datatype = common.D_1705
        codes = ['005010X212']
        min_len = 1
        max_len = 35


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    class Schema:
        json = {'title': 'Transaction Set Header',
         'usage': 'R',
         'description': 'xid=ST name=Transaction Set Header',
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


class HEADER_BHT01(Element):
    """Hierarchical Structure Code"""
    class Schema:
        json = {'title': 'Hierarchical Structure Code',
         'usage': 'R',
         'description': 'xid=BHT01 data_ele=1005',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1005'}, {'enum': ['0010']}]}}
        datatype = common.D_1005
        codes = ['0010']
        min_len = 4
        max_len = 4


class HEADER_BHT02(Element):
    """Transaction Set Purpose Code"""
    class Schema:
        json = {'title': 'Transaction Set Purpose Code',
         'usage': 'R',
         'description': 'xid=BHT02 data_ele=353',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/353'}, {'enum': ['08']}]}}
        datatype = common.D_353
        codes = ['08']
        min_len = 2
        max_len = 2


class HEADER_BHT03(Element):
    """Originator Application Transaction Identifier"""
    class Schema:
        json = {'title': 'Originator Application Transaction Identifier',
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
         'usage': 'R',
         'description': 'xid=BHT06 data_ele=640',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/640'}, {'enum': ['DG']}]}}
        datatype = common.D_640
        codes = ['DG']
        min_len = 2
        max_len = 2


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    class Schema:
        json = {'title': 'Beginning of Hierarchical Transaction',
         'usage': 'R',
         'description': 'xid=BHT name=Beginning of Hierarchical Transaction',
         'position': 200,
         'type': 'object',
         'properties': {'xid': {'literal': 'BHT'},
                        'bht01': {'$ref': '#/$elements/HEADER_BHT01'},
                        'bht02': {'$ref': '#/$elements/HEADER_BHT02'},
                        'bht03': {'$ref': '#/$elements/HEADER_BHT03'},
                        'bht04': {'$ref': '#/$elements/HEADER_BHT04'},
                        'bht05': {'$ref': '#/$elements/HEADER_BHT05'},
                        'bht06': {'$ref': '#/$elements/HEADER_BHT06'}},
         'required': ['bht01', 'bht02', 'bht03', 'bht04', 'bht05', 'bht06']}
        segment_name = 'BHT'
    bht01: HEADER_BHT01
    bht02: HEADER_BHT02
    bht03: HEADER_BHT03
    bht04: HEADER_BHT04
    bht05: HEADER_BHT05
    bht06: HEADER_BHT06


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Header type=wrapper',
                   'position': 110,
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
         'position': 100,
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
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PR']}]}}
        datatype = common.D_98
        codes = ['PR']
        min_len = 2
        max_len = 3


class L2100A_NM102(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['2']}]}}
        datatype = common.D_1065
        codes = ['2']
        min_len = 1
        max_len = 1


class L2100A_NM103(Element):
    """Payer Name"""
    class Schema:
        json = {'title': 'Payer Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100A_NM104(Element):
    """Name First"""
    class Schema:
        json = {'title': 'Name First',
         'usage': 'N',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100A_NM105(Element):
    """Name Middle"""
    class Schema:
        json = {'title': 'Name Middle',
         'usage': 'N',
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
    """Name Suffix"""
    class Schema:
        json = {'title': 'Name Suffix',
         'usage': 'N',
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
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['PI', 'XV']}]}}
        datatype = common.D_66
        codes = ['PI', 'XV']
        min_len = 1
        max_len = 2


class L2100A_NM109(Element):
    """Payer Identifier"""
    class Schema:
        json = {'title': 'Payer Identifier',
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


class L2100A_NM112(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'sequence': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100A_NM1(Segment):
    """Payer Name"""
    class Schema:
        json = {'title': 'Payer Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Payer Name',
         'position': 500,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100A_NM103'},
                        'nm108': {'$ref': '#/$elements/L2100A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100A_NM101
    nm102: L2100A_NM102
    nm103: L2100A_NM103
    nm108: L2100A_NM108
    nm109: L2100A_NM109


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
    """Payer Contact Name"""
    class Schema:
        json = {'title': 'Payer Contact Name',
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
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['ED', 'EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['ED', 'EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100A_PER04(Element):
    """Payer Contact Communication Number"""
    class Schema:
        json = {'title': 'Payer Contact Communication Number',
         'usage': 'R',
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
    """Payer Contact Communication Number"""
    class Schema:
        json = {'title': 'Payer Contact Communication Number',
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
    """Payer Contact Communication Number"""
    class Schema:
        json = {'title': 'Payer Contact Communication Number',
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
    """Payer Contact Information"""
    class Schema:
        json = {'title': 'Payer Contact Information',
         'usage': 'S',
         'description': 'xid=PER name=Payer Contact Information',
         'position': 800,
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
                        'per08': {'$ref': '#/$elements/L2100A_PER08'}},
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


class L2100A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer Name',
                   'usage': 'R',
                   'description': 'xid=2100A name=Payer Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100A_NM1'},
                                  'per': {'$ref': '#/$segments/L2100A_PER'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100A_NM1
    per: L2100A_PER | None


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
         'position': 100,
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
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['41']}]}}
        datatype = common.D_98
        codes = ['41']
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
    """Information Receiver Name Prefix"""
    class Schema:
        json = {'title': 'Information Receiver Name Prefix',
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
         'usage': 'N',
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
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['46']}]}}
        datatype = common.D_66
        codes = ['46']
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


class L2100B_NM112(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'sequence': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100B_NM1(Segment):
    """Information Receiver Name"""
    class Schema:
        json = {'title': 'Information Receiver Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Information Receiver Name',
         'position': 500,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100B_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100B_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100B_NM105'},
                        'nm108': {'$ref': '#/$elements/L2100B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100B_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100B_NM101
    nm102: L2100B_NM102
    nm103: L2100B_NM103 | None
    nm104: L2100B_NM104 | None
    nm105: L2100B_NM105 | None
    nm108: L2100B_NM108
    nm109: L2100B_NM109


class L2100B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Name',
                   'usage': 'R',
                   'description': 'xid=2100B name=Information Receiver Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100B_NM1'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100B_NM1


class L2200B_TRN01(Element):
    """Trace Type Code"""
    class Schema:
        json = {'title': 'Trace Type Code',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['2']}]}}
        datatype = common.D_481
        codes = ['2']
        min_len = 1
        max_len = 2


class L2200B_TRN02(Element):
    """Claim Transaction Batch Number"""
    class Schema:
        json = {'title': 'Claim Transaction Batch Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200B_TRN03(Element):
    """Originating Company Identifier"""
    class Schema:
        json = {'title': 'Originating Company Identifier',
         'usage': 'N',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class L2200B_TRN04(Element):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'N',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200B_TRN(Segment):
    """Information Receiver Trace Identifier"""
    class Schema:
        json = {'title': 'Information Receiver Trace Identifier',
         'usage': 'R',
         'description': 'xid=TRN name=Information Receiver Trace Identifier',
         'position': 900,
         'type': 'object',
         'properties': {'xid': {'literal': 'TRN'},
                        'trn01': {'$ref': '#/$elements/L2200B_TRN01'},
                        'trn02': {'$ref': '#/$elements/L2200B_TRN02'}},
         'required': ['trn01', 'trn02']}
        segment_name = 'TRN'
    trn01: L2200B_TRN01
    trn02: L2200B_TRN02


class L2200B_STC01_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC01-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200B_STC01_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200B_STC01_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC01-03 data_ele=98',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['41', 'AY', 'PR']}]}}
        datatype = common.D_98
        codes = ['41', 'AY', 'PR']
        min_len = 2
        max_len = 3


class L2200B_STC01_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'N',
         'description': 'xid=STC01-04 data_ele=1270',
         'sequence': 4,
         'type': {'$ref': '#/$common/1270'}}
        datatype = common.D_1270
        min_len = 1
        max_len = 3


class L2200B_STC01(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'R',
         'description': 'xid=STC01 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'stc01_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/98'},
                                                        {'enum': ['41', 'AY', 'PR']}]}},
                        'stc01_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'N',
                                     'description': 'xid=STC01-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1270'}}},
         'required': ['stc01_01', 'stc01_02']}
    stc01_01: L2200B_STC01_01
    stc01_02: L2200B_STC01_02
    stc01_03: L2200B_STC01_03 | None


class L2200B_STC02(Element):
    """Status Information Effective Date"""
    class Schema:
        json = {'title': 'Status Information Effective Date',
         'usage': 'R',
         'description': 'xid=STC02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200B_STC03(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'N',
         'description': 'xid=STC03 data_ele=306',
         'sequence': 3,
         'type': {'$ref': '#/$common/306'}}
        datatype = common.D_306
        min_len = 1
        max_len = 2


class L2200B_STC04(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200B_STC05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200B_STC06(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC06 data_ele=373',
         'sequence': 6,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200B_STC07(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'N',
         'description': 'xid=STC07 data_ele=591',
         'sequence': 7,
         'type': {'$ref': '#/$common/591'}}
        datatype = common.D_591
        min_len = 3
        max_len = 3


class L2200B_STC08(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200B_STC09(Element):
    """Check Number"""
    class Schema:
        json = {'title': 'Check Number',
         'usage': 'N',
         'description': 'xid=STC09 data_ele=429',
         'sequence': 9,
         'type': {'$ref': '#/$common/429'}}
        datatype = common.D_429
        min_len = 1
        max_len = 16


class L2200B_STC10_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC10-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200B_STC10_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200B_STC10_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC10-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200B_STC10_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'N',
         'description': 'xid=STC10-04 data_ele=1270',
         'sequence': 4,
         'type': {'$ref': '#/$common/1270'}}
        datatype = common.D_1270
        min_len = 1
        max_len = 3


class L2200B_STC10(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC10 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'stc10_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc10_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'N',
                                     'description': 'xid=STC10-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1270'}}},
         'required': ['stc10_01', 'stc10_02']}
    stc10_01: L2200B_STC10_01
    stc10_02: L2200B_STC10_02
    stc10_03: L2200B_STC10_03 | None


class L2200B_STC11_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC11-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200B_STC11_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200B_STC11_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC11-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200B_STC11_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'N',
         'description': 'xid=STC11-04 data_ele=1270',
         'sequence': 4,
         'type': {'$ref': '#/$common/1270'}}
        datatype = common.D_1270
        min_len = 1
        max_len = 3


class L2200B_STC11(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC11 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'stc11_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc11_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'N',
                                     'description': 'xid=STC11-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1270'}}},
         'required': ['stc11_01', 'stc11_02']}
    stc11_01: L2200B_STC11_01
    stc11_02: L2200B_STC11_02
    stc11_03: L2200B_STC11_03 | None


class L2200B_STC12(Element):
    """Free-form Message Text"""
    class Schema:
        json = {'title': 'Free-form Message Text',
         'usage': 'N',
         'description': 'xid=STC12 data_ele=933',
         'sequence': 12,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2200B_STC(Segment):
    """Information Receiver Status Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Status Information',
                   'usage': 'R',
                   'description': 'xid=STC name=Information Receiver Status '
                                  'Information',
                   'position': 1000,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'STC'},
                                  'stc01': {'$ref': '#/$elements/L2200B_STC01'},
                                  'stc02': {'$ref': '#/$elements/L2200B_STC02'},
                                  'stc10': {'$ref': '#/$elements/L2200B_STC10'},
                                  'stc11': {'$ref': '#/$elements/L2200B_STC11'}},
                   'required': ['stc01', 'stc02']}}
        segment_name = 'STC'
    stc01: L2200B_STC01
    stc02: L2200B_STC02
    stc10: L2200B_STC10 | None
    stc11: L2200B_STC11 | None


class L2200B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Trace Identifier',
                   'usage': 'S',
                   'description': 'xid=2200B name=Information Receiver Trace '
                                  'Identifier type=None',
                   'position': 900,
                   'type': 'object',
                   'properties': {'trn': {'$ref': '#/$segments/L2200B_TRN'},
                                  'stc': {'$ref': '#/$segments/L2200B_STC'}},
                   'required': ['trn', 'stc']},
         'maxItems': 1}
    trn: L2200B_TRN
    stc: list[L2200B_STC]


class L2000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Receiver Level',
                   'usage': 'R',
                   'description': 'xid=2000B name=Information Receiver Level type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000B_HL'},
                                  'l2100b': {'$ref': '#/$segments/L2100B'},
                                  'l2200b': {'$ref': '#/$segments/L2200B'}},
                   'required': ['hl', 'l2100b']}}
    hl: L2000B_HL
    l2100b: list[L2100B]
    l2200b: list[L2200B] | None


class L2000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Information Source Level',
                   'usage': 'R',
                   'description': 'xid=2000A name=Information Source Level type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000A_HL'},
                                  'l2100a': {'$ref': '#/$segments/L2100A'},
                                  'l2000b': {'$ref': '#/$segments/L2000B'}},
                   'required': ['hl', 'l2100a', 'l2000b']}}
    hl: L2000A_HL
    l2100a: list[L2100A]
    l2000b: list[L2000B]


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
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['19']}]}}
        datatype = common.D_735
        codes = ['19']
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
    """Service Provider Level"""
    class Schema:
        json = {'title': 'Service Provider Level',
         'usage': 'R',
         'description': 'xid=HL name=Service Provider Level',
         'position': 100,
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


class L2100C_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['1P']}]}}
        datatype = common.D_98
        codes = ['1P']
        min_len = 2
        max_len = 3


class L2100C_NM102(Element):
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


class L2100C_NM103(Element):
    """Provider Last or Organization Name"""
    class Schema:
        json = {'title': 'Provider Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100C_NM104(Element):
    """Provider First Name"""
    class Schema:
        json = {'title': 'Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100C_NM105(Element):
    """Provider Middle Name"""
    class Schema:
        json = {'title': 'Provider Middle Name',
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
    """Provider Name Suffix"""
    class Schema:
        json = {'title': 'Provider Name Suffix',
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
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'SV', 'XX']}]}}
        datatype = common.D_66
        codes = ['FI', 'SV', 'XX']
        min_len = 1
        max_len = 2


class L2100C_NM109(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
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


class L2100C_NM112(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'sequence': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100C_NM1(Segment):
    """Provider Name"""
    class Schema:
        json = {'title': 'Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Provider Name',
         'position': 500,
         'syntax': ['P0809', 'C1110', 'C1203'],
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
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100C_NM101
    nm102: L2100C_NM102
    nm103: L2100C_NM103 | None
    nm104: L2100C_NM104 | None
    nm105: L2100C_NM105 | None
    nm107: L2100C_NM107 | None
    nm108: L2100C_NM108
    nm109: L2100C_NM109


class L2100C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Provider Name',
                   'usage': 'R',
                   'description': 'xid=2100C name=Provider Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100C_NM1'}},
                   'required': ['nm1']},
         'maxItems': 2}
    nm1: L2100C_NM1


class L2200C_TRN01(Element):
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


class L2200C_TRN02(Element):
    """Provider of Service Information Trace Identifier"""
    class Schema:
        json = {'title': 'Provider of Service Information Trace Identifier',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200C_TRN03(Element):
    """Originating Company Identifier"""
    class Schema:
        json = {'title': 'Originating Company Identifier',
         'usage': 'N',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class L2200C_TRN04(Element):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'N',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200C_TRN(Segment):
    """Provider of Service Trace Identifier"""
    class Schema:
        json = {'title': 'Provider of Service Trace Identifier',
         'usage': 'R',
         'description': 'xid=TRN name=Provider of Service Trace Identifier',
         'position': 900,
         'type': 'object',
         'properties': {'xid': {'literal': 'TRN'},
                        'trn01': {'$ref': '#/$elements/L2200C_TRN01'},
                        'trn02': {'$ref': '#/$elements/L2200C_TRN02'}},
         'required': ['trn01', 'trn02']}
        segment_name = 'TRN'
    trn01: L2200C_TRN01
    trn02: L2200C_TRN02


class L2200C_STC01_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC01-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200C_STC01_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200C_STC01_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC01-03 data_ele=98',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['1P']}]}}
        datatype = common.D_98
        codes = ['1P']
        min_len = 2
        max_len = 3


class L2200C_STC01_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'N',
         'description': 'xid=STC01-04 data_ele=1270',
         'sequence': 4,
         'type': {'$ref': '#/$common/1270'}}
        datatype = common.D_1270
        min_len = 1
        max_len = 3


class L2200C_STC01(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'R',
         'description': 'xid=STC01 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'stc01_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/98'},
                                                        {'enum': ['1P']}]}},
                        'stc01_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'N',
                                     'description': 'xid=STC01-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1270'}}},
         'required': ['stc01_01', 'stc01_02']}
    stc01_01: L2200C_STC01_01
    stc01_02: L2200C_STC01_02
    stc01_03: L2200C_STC01_03 | None


class L2200C_STC02(Element):
    """Status Information Effective Date"""
    class Schema:
        json = {'title': 'Status Information Effective Date',
         'usage': 'R',
         'description': 'xid=STC02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200C_STC03(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'N',
         'description': 'xid=STC03 data_ele=306',
         'sequence': 3,
         'type': {'$ref': '#/$common/306'}}
        datatype = common.D_306
        min_len = 1
        max_len = 2


class L2200C_STC04(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200C_STC05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200C_STC06(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC06 data_ele=373',
         'sequence': 6,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200C_STC07(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'N',
         'description': 'xid=STC07 data_ele=591',
         'sequence': 7,
         'type': {'$ref': '#/$common/591'}}
        datatype = common.D_591
        min_len = 3
        max_len = 3


class L2200C_STC08(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200C_STC09(Element):
    """Check Number"""
    class Schema:
        json = {'title': 'Check Number',
         'usage': 'N',
         'description': 'xid=STC09 data_ele=429',
         'sequence': 9,
         'type': {'$ref': '#/$common/429'}}
        datatype = common.D_429
        min_len = 1
        max_len = 16


class L2200C_STC10_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC10-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200C_STC10_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200C_STC10_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC10-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200C_STC10_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'N',
         'description': 'xid=STC10-04 data_ele=1270',
         'sequence': 4,
         'type': {'$ref': '#/$common/1270'}}
        datatype = common.D_1270
        min_len = 1
        max_len = 3


class L2200C_STC10(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC10 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'stc10_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc10_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'N',
                                     'description': 'xid=STC10-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1270'}}},
         'required': ['stc10_01', 'stc10_02']}
    stc10_01: L2200C_STC10_01
    stc10_02: L2200C_STC10_02
    stc10_03: L2200C_STC10_03 | None


class L2200C_STC11_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC11-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200C_STC11_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200C_STC11_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC11-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200C_STC11_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'N',
         'description': 'xid=STC11-04 data_ele=1270',
         'sequence': 4,
         'type': {'$ref': '#/$common/1270'}}
        datatype = common.D_1270
        min_len = 1
        max_len = 3


class L2200C_STC11(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC11 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'stc11_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc11_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'N',
                                     'description': 'xid=STC11-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1270'}}},
         'required': ['stc11_01', 'stc11_02']}
    stc11_01: L2200C_STC11_01
    stc11_02: L2200C_STC11_02
    stc11_03: L2200C_STC11_03 | None


class L2200C_STC12(Element):
    """Free-form Message Text"""
    class Schema:
        json = {'title': 'Free-form Message Text',
         'usage': 'N',
         'description': 'xid=STC12 data_ele=933',
         'sequence': 12,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2200C_STC(Segment):
    """Provider Status Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Provider Status Information',
                   'usage': 'R',
                   'description': 'xid=STC name=Provider Status Information',
                   'position': 1000,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'STC'},
                                  'stc01': {'$ref': '#/$elements/L2200C_STC01'},
                                  'stc02': {'$ref': '#/$elements/L2200C_STC02'},
                                  'stc10': {'$ref': '#/$elements/L2200C_STC10'},
                                  'stc11': {'$ref': '#/$elements/L2200C_STC11'}},
                   'required': ['stc01', 'stc02']}}
        segment_name = 'STC'
    stc01: L2200C_STC01
    stc02: L2200C_STC02
    stc10: L2200C_STC10 | None
    stc11: L2200C_STC11 | None


class L2200C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Provider of Service Trace Identifier',
                   'usage': 'S',
                   'description': 'xid=2200C name=Provider of Service Trace Identifier '
                                  'type=None',
                   'position': 900,
                   'type': 'object',
                   'properties': {'trn': {'$ref': '#/$segments/L2200C_TRN'},
                                  'stc': {'$ref': '#/$segments/L2200C_STC'}},
                   'required': ['trn', 'stc']},
         'maxItems': 1}
    trn: L2200C_TRN
    stc: list[L2200C_STC]


class L2000C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Provider Level',
                   'usage': 'S',
                   'description': 'xid=2000C name=Service Provider Level type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000C_HL'},
                                  'l2100c': {'$ref': '#/$segments/L2100C'},
                                  'l2200c': {'$ref': '#/$segments/L2200C'}},
                   'required': ['hl', 'l2100c']}}
    hl: L2000C_HL
    l2100c: list[L2100C]
    l2200c: list[L2200C] | None


class TABLE2AREA4(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table2 - Area4',
                   'usage': 'S',
                   'description': 'xid=TABLE2AREA4 name=Table2 - Area4 type=wrapper',
                   'position': 140,
                   'type': 'object',
                   'properties': {'l2000c': {'$ref': '#/$segments/L2000C'}}}}
    l2000c: list[L2000C] | None


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
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['22']}]}}
        datatype = common.D_735
        codes = ['22']
        min_len = 1
        max_len = 2


class L2000D_HL04(Element):
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


class L2000D_HL(Segment):
    """Subscriber Level"""
    class Schema:
        json = {'title': 'Subscriber Level',
         'usage': 'R',
         'description': 'xid=HL name=Subscriber Level',
         'position': 100,
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


class L2100D_NM101(Element):
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


class L2100D_NM102(Element):
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


class L2100D_NM103(Element):
    """Subscriber Last Name"""
    class Schema:
        json = {'title': 'Subscriber Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100D_NM104(Element):
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


class L2100D_NM105(Element):
    """Subscriber Middle Name or Initial"""
    class Schema:
        json = {'title': 'Subscriber Middle Name or Initial',
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


class L2100D_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', 'II', 'MI']}]}}
        datatype = common.D_66
        codes = ['24', 'II', 'MI']
        min_len = 1
        max_len = 2


class L2100D_NM109(Element):
    """Subscriber Identifier"""
    class Schema:
        json = {'title': 'Subscriber Identifier',
         'usage': 'R',
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


class L2100D_NM112(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'sequence': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100D_NM1(Segment):
    """Subscriber Name"""
    class Schema:
        json = {'title': 'Subscriber Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Subscriber Name',
         'position': 500,
         'syntax': ['P0809', 'C1110', 'C1203'],
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
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100D_NM101
    nm102: L2100D_NM102
    nm103: L2100D_NM103
    nm104: L2100D_NM104 | None
    nm105: L2100D_NM105 | None
    nm107: L2100D_NM107 | None
    nm108: L2100D_NM108
    nm109: L2100D_NM109


class L2100D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Name',
                   'usage': 'R',
                   'description': 'xid=2100D name=Subscriber Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100D_NM1'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100D_NM1


class L2200D_TRN01(Element):
    """Trace Type Code"""
    class Schema:
        json = {'title': 'Trace Type Code',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['2']}]}}
        datatype = common.D_481
        codes = ['2']
        min_len = 1
        max_len = 2


class L2200D_TRN02(Element):
    """Referenced Transaction Trace Number"""
    class Schema:
        json = {'title': 'Referenced Transaction Trace Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_TRN03(Element):
    """Originating Company Identifier"""
    class Schema:
        json = {'title': 'Originating Company Identifier',
         'usage': 'N',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class L2200D_TRN04(Element):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'N',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_TRN(Segment):
    """Claim Status Tracking Number"""
    class Schema:
        json = {'title': 'Claim Status Tracking Number',
         'usage': 'R',
         'description': 'xid=TRN name=Claim Status Tracking Number',
         'position': 900,
         'type': 'object',
         'properties': {'xid': {'literal': 'TRN'},
                        'trn01': {'$ref': '#/$elements/L2200D_TRN01'},
                        'trn02': {'$ref': '#/$elements/L2200D_TRN02'}},
         'required': ['trn01', 'trn02']}
        segment_name = 'TRN'
    trn01: L2200D_TRN01
    trn02: L2200D_TRN02


class L2200D_STC01_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC01-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200D_STC01_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200D_STC01_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC01-03 data_ele=98',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['03', '13', '17', '1E', '1G', '1H', '1I', '1O',
                                      '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W',
                                      '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E',
                                      '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36',
                                      '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I',
                                      '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q',
                                      '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y',
                                      '3Z', '40', '43', '44', '4A', '4B', '4C', '4D',
                                      '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M',
                                      '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V',
                                      '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D',
                                      '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L',
                                      '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T',
                                      '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A',
                                      '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I',
                                      '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q',
                                      '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71',
                                      '72', '73', '74', '77', '7C', '80', '82', '84',
                                      '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ',
                                      'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9',
                                      'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI',
                                      'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ',
                                      'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD',
                                      'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP',
                                      'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE',
                                      'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY',
                                      'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL',
                                      'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5',
                                      'ZZ']}]}}
        datatype = common.D_98
        codes = ['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ']
        min_len = 2
        max_len = 3


class L2200D_STC01_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC01-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2200D_STC01(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'R',
         'description': 'xid=STC01 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'stc01_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/98'},
                                                        {'enum': ['03', '13', '17',
                                                                  '1E', '1G', '1H',
                                                                  '1I', '1O', '1P',
                                                                  '1Q', '1R', '1S',
                                                                  '1T', '1U', '1V',
                                                                  '1W', '1X', '1Y',
                                                                  '1Z', '28', '2A',
                                                                  '2B', '2D', '2E',
                                                                  '2I', '2K', '2P',
                                                                  '2Q', '2S', '2Z',
                                                                  '30', '36', '3A',
                                                                  '3C', '3D', '3E',
                                                                  '3F', '3G', '3H',
                                                                  '3I', '3J', '3K',
                                                                  '3L', '3M', '3N',
                                                                  '3O', '3P', '3Q',
                                                                  '3R', '3S', '3T',
                                                                  '3U', '3V', '3W',
                                                                  '3X', '3Y', '3Z',
                                                                  '40', '43', '44',
                                                                  '4A', '4B', '4C',
                                                                  '4D', '4E', '4F',
                                                                  '4G', '4H', '4I',
                                                                  '4J', '4L', '4M',
                                                                  '4N', '4O', '4P',
                                                                  '4Q', '4R', '4S',
                                                                  '4U', '4V', '4W',
                                                                  '4X', '4Y', '4Z',
                                                                  '5A', '5B', '5C',
                                                                  '5D', '5E', '5F',
                                                                  '5G', '5H', '5I',
                                                                  '5J', '5K', '5L',
                                                                  '5M', '5N', '5O',
                                                                  '5P', '5Q', '5R',
                                                                  '5S', '5T', '5U',
                                                                  '5V', '5W', '5X',
                                                                  '5Y', '5Z', '61',
                                                                  '6A', '6B', '6C',
                                                                  '6D', '6E', '6F',
                                                                  '6G', '6H', '6I',
                                                                  '6J', '6K', '6L',
                                                                  '6M', '6N', '6O',
                                                                  '6P', '6Q', '6R',
                                                                  '6S', '6U', '6V',
                                                                  '6W', '6X', '6Y',
                                                                  '71', '72', '73',
                                                                  '74', '77', '7C',
                                                                  '80', '82', '84',
                                                                  '85', '87', '95',
                                                                  'CK', 'CZ', 'D2',
                                                                  'DD', 'DJ', 'DK',
                                                                  'DN', 'DO', 'DQ',
                                                                  'E1', 'E2', 'E7',
                                                                  'E9', 'FA', 'FD',
                                                                  'FE', 'G0', 'G3',
                                                                  'GB', 'GD', 'GI',
                                                                  'GJ', 'GK', 'GM',
                                                                  'GY', 'HF', 'HH',
                                                                  'I3', 'IJ', 'IL',
                                                                  'IN', 'LI', 'LR',
                                                                  'MR', 'MSC', 'OB',
                                                                  'OD', 'OX', 'P0',
                                                                  'P2', 'P3', 'P4',
                                                                  'P6', 'P7', 'PRP',
                                                                  'PT', 'PV', 'PW',
                                                                  'QA', 'QB', 'QC',
                                                                  'QD', 'QE', 'QH',
                                                                  'QK', 'QL', 'QN',
                                                                  'QO', 'QS', 'QV',
                                                                  'QY', 'RC', 'RW',
                                                                  'S4', 'SEP', 'SJ',
                                                                  'SU', 'T4', 'TL',
                                                                  'TQ', 'TT', 'TTP',
                                                                  'TU', 'UH', 'X3',
                                                                  'X4', 'X5',
                                                                  'ZZ']}]}},
                        'stc01_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc01_01', 'stc01_02']}
    stc01_01: L2200D_STC01_01
    stc01_02: L2200D_STC01_02
    stc01_03: L2200D_STC01_03 | None
    stc01_04: L2200D_STC01_04 | None


class L2200D_STC02(Element):
    """Status Information Effective Date"""
    class Schema:
        json = {'title': 'Status Information Effective Date',
         'usage': 'R',
         'description': 'xid=STC02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200D_STC03(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'N',
         'description': 'xid=STC03 data_ele=306',
         'sequence': 3,
         'type': {'$ref': '#/$common/306'}}
        datatype = common.D_306
        min_len = 1
        max_len = 2


class L2200D_STC04(Element):
    """Total Claim Charge Amount"""
    class Schema:
        json = {'title': 'Total Claim Charge Amount',
         'usage': 'S',
         'description': 'xid=STC04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200D_STC05(Element):
    """Claim Payment Amount"""
    class Schema:
        json = {'title': 'Claim Payment Amount',
         'usage': 'S',
         'description': 'xid=STC05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200D_STC06(Element):
    """Adjudication Finalized Date"""
    class Schema:
        json = {'title': 'Adjudication Finalized Date',
         'usage': 'S',
         'description': 'xid=STC06 data_ele=373',
         'sequence': 6,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200D_STC07(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'N',
         'description': 'xid=STC07 data_ele=591',
         'sequence': 7,
         'type': {'$ref': '#/$common/591'}}
        datatype = common.D_591
        min_len = 3
        max_len = 3


class L2200D_STC08(Element):
    """Remittance Date"""
    class Schema:
        json = {'title': 'Remittance Date',
         'usage': 'S',
         'description': 'xid=STC08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200D_STC09(Element):
    """Remittance Trace Number"""
    class Schema:
        json = {'title': 'Remittance Trace Number',
         'usage': 'S',
         'description': 'xid=STC09 data_ele=429',
         'sequence': 9,
         'type': {'$ref': '#/$common/429'}}
        datatype = common.D_429
        min_len = 1
        max_len = 16


class L2200D_STC10_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC10-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200D_STC10_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200D_STC10_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC10-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200D_STC10_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC10-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2200D_STC10(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC10 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'stc10_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc10_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc10_01', 'stc10_02']}
    stc10_01: L2200D_STC10_01
    stc10_02: L2200D_STC10_02
    stc10_03: L2200D_STC10_03 | None
    stc10_04: L2200D_STC10_04 | None


class L2200D_STC11_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC11-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200D_STC11_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200D_STC11_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC11-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200D_STC11_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC11-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2200D_STC11(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC11 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'stc11_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc11_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc11_01', 'stc11_02']}
    stc11_01: L2200D_STC11_01
    stc11_02: L2200D_STC11_02
    stc11_03: L2200D_STC11_03 | None
    stc11_04: L2200D_STC11_04 | None


class L2200D_STC12(Element):
    """Free-form Message Text"""
    class Schema:
        json = {'title': 'Free-form Message Text',
         'usage': 'N',
         'description': 'xid=STC12 data_ele=933',
         'sequence': 12,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2200D_STC(Segment):
    """Claim Level Status Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Level Status Information',
                   'usage': 'R',
                   'description': 'xid=STC name=Claim Level Status Information',
                   'position': 1000,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'STC'},
                                  'stc01': {'$ref': '#/$elements/L2200D_STC01'},
                                  'stc02': {'$ref': '#/$elements/L2200D_STC02'},
                                  'stc04': {'$ref': '#/$elements/L2200D_STC04'},
                                  'stc05': {'$ref': '#/$elements/L2200D_STC05'},
                                  'stc06': {'$ref': '#/$elements/L2200D_STC06'},
                                  'stc08': {'$ref': '#/$elements/L2200D_STC08'},
                                  'stc09': {'$ref': '#/$elements/L2200D_STC09'},
                                  'stc10': {'$ref': '#/$elements/L2200D_STC10'},
                                  'stc11': {'$ref': '#/$elements/L2200D_STC11'}},
                   'required': ['stc01', 'stc02']}}
        segment_name = 'STC'
    stc01: L2200D_STC01
    stc02: L2200D_STC02
    stc04: L2200D_STC04 | None
    stc05: L2200D_STC05 | None
    stc06: L2200D_STC06 | None
    stc08: L2200D_STC08 | None
    stc09: L2200D_STC09 | None
    stc10: L2200D_STC10 | None
    stc11: L2200D_STC11 | None


class L2200D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['1K']}]}}
        datatype = common.D_128
        codes = ['1K']
        min_len = 2
        max_len = 3


class L2200D_REF02(Element):
    """Payer Claim Control Number"""
    class Schema:
        json = {'title': 'Payer Claim Control Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_REF03(Element):
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


class L2200D_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200D_REF(Segment):
    """Payer Claim Control Number"""
    class Schema:
        json = {'title': 'Payer Claim Control Number',
         'usage': 'S',
         'description': 'xid=REF name=Payer Claim Control Number',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200D_REF01
    ref02: L2200D_REF02


class L2200D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['BLT']}]}}
        datatype = common.D_128
        codes = ['BLT']
        min_len = 2
        max_len = 3


class L2200D_REF02(Element):
    """Bill Type Identifier"""
    class Schema:
        json = {'title': 'Bill Type Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_REF03(Element):
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


class L2200D_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200D_REF(Segment):
    """Institutional Bill Type Identification"""
    class Schema:
        json = {'title': 'Institutional Bill Type Identification',
         'usage': 'S',
         'description': 'xid=REF name=Institutional Bill Type Identification',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200D_REF01
    ref02: L2200D_REF02


class L2200D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['EJ']}]}}
        datatype = common.D_128
        codes = ['EJ']
        min_len = 2
        max_len = 3


class L2200D_REF02(Element):
    """Patient Control Number"""
    class Schema:
        json = {'title': 'Patient Control Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_REF03(Element):
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


class L2200D_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200D_REF(Segment):
    """Patient Control Number"""
    class Schema:
        json = {'title': 'Patient Control Number',
         'usage': 'S',
         'description': 'xid=REF name=Patient Control Number',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200D_REF01
    ref02: L2200D_REF02


class L2200D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['XZ']}]}}
        datatype = common.D_128
        codes = ['XZ']
        min_len = 2
        max_len = 3


class L2200D_REF02(Element):
    """Pharmacy Prescription Number"""
    class Schema:
        json = {'title': 'Pharmacy Prescription Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_REF03(Element):
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


class L2200D_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200D_REF(Segment):
    """Pharmacy Prescription Number"""
    class Schema:
        json = {'title': 'Pharmacy Prescription Number',
         'usage': 'S',
         'description': 'xid=REF name=Pharmacy Prescription Number',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200D_REF01
    ref02: L2200D_REF02


class L2200D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['VV']}]}}
        datatype = common.D_128
        codes = ['VV']
        min_len = 2
        max_len = 3


class L2200D_REF02(Element):
    """Voucher Identifier"""
    class Schema:
        json = {'title': 'Voucher Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_REF03(Element):
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


class L2200D_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200D_REF(Segment):
    """Voucher Identifier"""
    class Schema:
        json = {'title': 'Voucher Identifier',
         'usage': 'S',
         'description': 'xid=REF name=Voucher Identifier',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200D_REF01
    ref02: L2200D_REF02


class L2200D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['D9']}]}}
        datatype = common.D_128
        codes = ['D9']
        min_len = 2
        max_len = 3


class L2200D_REF02(Element):
    """Clearinghouse Trace Number"""
    class Schema:
        json = {'title': 'Clearinghouse Trace Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200D_REF03(Element):
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


class L2200D_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200D_REF(Segment):
    """Claim Identification Number For Clearinghouses and Other Transmission Intermediaries"""
    class Schema:
        json = {'title': 'Claim Identification Number For Clearinghouses and Other '
                  'Transmission Intermediaries',
         'usage': 'S',
         'description': 'xid=REF name=Claim Identification Number For Clearinghouses '
                        'and Other Transmission Intermediaries',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200D_REF01
    ref02: L2200D_REF02


class L2200D_DTP01(Element):
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


class L2200D_DTP02(Element):
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


class L2200D_DTP03(Element):
    """Claim Service Period"""
    class Schema:
        json = {'title': 'Claim Service Period',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2200D_DTP(Segment):
    """Claim Service Date"""
    class Schema:
        json = {'title': 'Claim Service Date',
         'usage': 'S',
         'description': 'xid=DTP name=Claim Service Date',
         'position': 1200,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2200D_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2200D_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2200D_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2200D_DTP01
    dtp02: L2200D_DTP02
    dtp03: L2200D_DTP03


class L2220D_SVC01_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SVC01-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU',
                                      'WK']}]}}
        datatype = common.D_235
        codes = ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU', 'WK']
        min_len = 2
        max_len = 2


class L2220D_SVC01_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SVC01-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2220D_SVC01_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220D_SVC01_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220D_SVC01_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220D_SVC01_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220D_SVC01_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=SVC01-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2220D_SVC01_08(Element):
    """Product/Service ID"""
    class Schema:
        json = {'title': 'Product/Service ID',
         'usage': 'N',
         'description': 'xid=SVC01-08 data_ele=234',
         'sequence': 8,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2220D_SVC01(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'R',
         'description': 'xid=SVC01 name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'svc01_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SVC01-01 data_ele=235',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD', 'ER', 'HC',
                                                                  'HP', 'IV', 'N4',
                                                                  'NU', 'WK']}]}},
                        'svc01_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SVC01-02 data_ele=234',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'svc01_03': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-03 data_ele=1339',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_04': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-04 data_ele=1339',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_05': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-05 data_ele=1339',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_06': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-06 data_ele=1339',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_07': {'title': 'Description',
                                     'usage': 'N',
                                     'description': 'xid=SVC01-07 data_ele=352',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/352'}},
                        'svc01_08': {'title': 'Product/Service ID',
                                     'usage': 'N',
                                     'description': 'xid=SVC01-08 data_ele=234',
                                     'sequence': 8,
                                     'type': {'$ref': '#/$common/234'}}},
         'required': ['svc01_01', 'svc01_02']}
    svc01_01: L2220D_SVC01_01
    svc01_02: L2220D_SVC01_02
    svc01_03: L2220D_SVC01_03 | None
    svc01_04: L2220D_SVC01_04 | None
    svc01_05: L2220D_SVC01_05 | None
    svc01_06: L2220D_SVC01_06 | None


class L2220D_SVC02(Element):
    """Line Item Charge Amount"""
    class Schema:
        json = {'title': 'Line Item Charge Amount',
         'usage': 'R',
         'description': 'xid=SVC02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220D_SVC03(Element):
    """Line Item Payment Amount"""
    class Schema:
        json = {'title': 'Line Item Payment Amount',
         'usage': 'R',
         'description': 'xid=SVC03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220D_SVC04(Element):
    """Revenue Code"""
    class Schema:
        json = {'title': 'Revenue Code',
         'usage': 'S',
         'description': 'xid=SVC04 data_ele=234',
         'sequence': 4,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2220D_SVC05(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=SVC05 data_ele=380',
         'sequence': 5,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2220D_SVC06(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'N',
         'description': 'xid=SVC06 name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 6,
         'syntax': []}


class L2220D_SVC07(Element):
    """Units of Service Count"""
    class Schema:
        json = {'title': 'Units of Service Count',
         'usage': 'R',
         'description': 'xid=SVC07 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2220D_SVC(Segment):
    """Service Line Information"""
    class Schema:
        json = {'title': 'Service Line Information',
         'usage': 'R',
         'description': 'xid=SVC name=Service Line Information',
         'position': 1800,
         'type': 'object',
         'properties': {'xid': {'literal': 'SVC'},
                        'svc01': {'$ref': '#/$elements/L2220D_SVC01'},
                        'svc02': {'$ref': '#/$elements/L2220D_SVC02'},
                        'svc03': {'$ref': '#/$elements/L2220D_SVC03'},
                        'svc04': {'$ref': '#/$elements/L2220D_SVC04'},
                        'svc07': {'$ref': '#/$elements/L2220D_SVC07'}},
         'required': ['svc01', 'svc02', 'svc03', 'svc07']}
        segment_name = 'SVC'
    svc01: L2220D_SVC01
    svc02: L2220D_SVC02
    svc03: L2220D_SVC03
    svc04: L2220D_SVC04 | None
    svc07: L2220D_SVC07


class L2220D_STC01_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC01-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220D_STC01_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220D_STC01_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC01-03 data_ele=98',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['03', '13', '17', '1E', '1G', '1H', '1I', '1O',
                                      '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W',
                                      '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E',
                                      '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36',
                                      '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I',
                                      '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q',
                                      '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y',
                                      '3Z', '40', '43', '44', '4A', '4B', '4C', '4D',
                                      '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M',
                                      '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V',
                                      '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D',
                                      '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L',
                                      '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T',
                                      '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A',
                                      '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I',
                                      '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q',
                                      '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71',
                                      '72', '73', '74', '77', '7C', '80', '82', '84',
                                      '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ',
                                      'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9',
                                      'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI',
                                      'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ',
                                      'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD',
                                      'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP',
                                      'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE',
                                      'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY',
                                      'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL',
                                      'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5',
                                      'ZZ']}]}}
        datatype = common.D_98
        codes = ['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ']
        min_len = 2
        max_len = 3


class L2220D_STC01_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC01-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2220D_STC01(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'R',
         'description': 'xid=STC01 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'stc01_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/98'},
                                                        {'enum': ['03', '13', '17',
                                                                  '1E', '1G', '1H',
                                                                  '1I', '1O', '1P',
                                                                  '1Q', '1R', '1S',
                                                                  '1T', '1U', '1V',
                                                                  '1W', '1X', '1Y',
                                                                  '1Z', '28', '2A',
                                                                  '2B', '2D', '2E',
                                                                  '2I', '2K', '2P',
                                                                  '2Q', '2S', '2Z',
                                                                  '30', '36', '3A',
                                                                  '3C', '3D', '3E',
                                                                  '3F', '3G', '3H',
                                                                  '3I', '3J', '3K',
                                                                  '3L', '3M', '3N',
                                                                  '3O', '3P', '3Q',
                                                                  '3R', '3S', '3T',
                                                                  '3U', '3V', '3W',
                                                                  '3X', '3Y', '3Z',
                                                                  '40', '43', '44',
                                                                  '4A', '4B', '4C',
                                                                  '4D', '4E', '4F',
                                                                  '4G', '4H', '4I',
                                                                  '4J', '4L', '4M',
                                                                  '4N', '4O', '4P',
                                                                  '4Q', '4R', '4S',
                                                                  '4U', '4V', '4W',
                                                                  '4X', '4Y', '4Z',
                                                                  '5A', '5B', '5C',
                                                                  '5D', '5E', '5F',
                                                                  '5G', '5H', '5I',
                                                                  '5J', '5K', '5L',
                                                                  '5M', '5N', '5O',
                                                                  '5P', '5Q', '5R',
                                                                  '5S', '5T', '5U',
                                                                  '5V', '5W', '5X',
                                                                  '5Y', '5Z', '61',
                                                                  '6A', '6B', '6C',
                                                                  '6D', '6E', '6F',
                                                                  '6G', '6H', '6I',
                                                                  '6J', '6K', '6L',
                                                                  '6M', '6N', '6O',
                                                                  '6P', '6Q', '6R',
                                                                  '6S', '6U', '6V',
                                                                  '6W', '6X', '6Y',
                                                                  '71', '72', '73',
                                                                  '74', '77', '7C',
                                                                  '80', '82', '84',
                                                                  '85', '87', '95',
                                                                  'CK', 'CZ', 'D2',
                                                                  'DD', 'DJ', 'DK',
                                                                  'DN', 'DO', 'DQ',
                                                                  'E1', 'E2', 'E7',
                                                                  'E9', 'FA', 'FD',
                                                                  'FE', 'G0', 'G3',
                                                                  'GB', 'GD', 'GI',
                                                                  'GJ', 'GK', 'GM',
                                                                  'GY', 'HF', 'HH',
                                                                  'I3', 'IJ', 'IL',
                                                                  'IN', 'LI', 'LR',
                                                                  'MR', 'MSC', 'OB',
                                                                  'OD', 'OX', 'P0',
                                                                  'P2', 'P3', 'P4',
                                                                  'P6', 'P7', 'PRP',
                                                                  'PT', 'PV', 'PW',
                                                                  'QA', 'QB', 'QC',
                                                                  'QD', 'QE', 'QH',
                                                                  'QK', 'QL', 'QN',
                                                                  'QO', 'QS', 'QV',
                                                                  'QY', 'RC', 'RW',
                                                                  'S4', 'SEP', 'SJ',
                                                                  'SU', 'T4', 'TL',
                                                                  'TQ', 'TT', 'TTP',
                                                                  'TU', 'UH', 'X3',
                                                                  'X4', 'X5',
                                                                  'ZZ']}]}},
                        'stc01_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc01_01', 'stc01_02']}
    stc01_01: L2220D_STC01_01
    stc01_02: L2220D_STC01_02
    stc01_03: L2220D_STC01_03 | None
    stc01_04: L2220D_STC01_04 | None


class L2220D_STC02(Element):
    """Status Information Effective Date"""
    class Schema:
        json = {'title': 'Status Information Effective Date',
         'usage': 'R',
         'description': 'xid=STC02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2220D_STC03(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'N',
         'description': 'xid=STC03 data_ele=306',
         'sequence': 3,
         'type': {'$ref': '#/$common/306'}}
        datatype = common.D_306
        min_len = 1
        max_len = 2


class L2220D_STC04(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220D_STC05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220D_STC06(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC06 data_ele=373',
         'sequence': 6,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2220D_STC07(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'N',
         'description': 'xid=STC07 data_ele=591',
         'sequence': 7,
         'type': {'$ref': '#/$common/591'}}
        datatype = common.D_591
        min_len = 3
        max_len = 3


class L2220D_STC08(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2220D_STC09(Element):
    """Check Number"""
    class Schema:
        json = {'title': 'Check Number',
         'usage': 'N',
         'description': 'xid=STC09 data_ele=429',
         'sequence': 9,
         'type': {'$ref': '#/$common/429'}}
        datatype = common.D_429
        min_len = 1
        max_len = 16


class L2220D_STC10_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC10-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220D_STC10_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220D_STC10_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC10-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2220D_STC10_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC10-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2220D_STC10(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC10 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'stc10_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc10_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc10_01', 'stc10_02']}
    stc10_01: L2220D_STC10_01
    stc10_02: L2220D_STC10_02
    stc10_03: L2220D_STC10_03 | None
    stc10_04: L2220D_STC10_04 | None


class L2220D_STC11_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC11-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220D_STC11_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220D_STC11_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC11-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2220D_STC11_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC11-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2220D_STC11(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC11 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'stc11_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc11_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc11_01', 'stc11_02']}
    stc11_01: L2220D_STC11_01
    stc11_02: L2220D_STC11_02
    stc11_03: L2220D_STC11_03 | None
    stc11_04: L2220D_STC11_04 | None


class L2220D_STC12(Element):
    """Free-form Message Text"""
    class Schema:
        json = {'title': 'Free-form Message Text',
         'usage': 'N',
         'description': 'xid=STC12 data_ele=933',
         'sequence': 12,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2220D_STC(Segment):
    """Service Line Status Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Line Status Information',
                   'usage': 'R',
                   'description': 'xid=STC name=Service Line Status Information',
                   'position': 1900,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'STC'},
                                  'stc01': {'$ref': '#/$elements/L2220D_STC01'},
                                  'stc02': {'$ref': '#/$elements/L2220D_STC02'},
                                  'stc10': {'$ref': '#/$elements/L2220D_STC10'},
                                  'stc11': {'$ref': '#/$elements/L2220D_STC11'}},
                   'required': ['stc01', 'stc02']}}
        segment_name = 'STC'
    stc01: L2220D_STC01
    stc02: L2220D_STC02
    stc10: L2220D_STC10 | None
    stc11: L2220D_STC11 | None


class L2220D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['FJ']}]}}
        datatype = common.D_128
        codes = ['FJ']
        min_len = 2
        max_len = 3


class L2220D_REF02(Element):
    """Line Item Control Number"""
    class Schema:
        json = {'title': 'Line Item Control Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2220D_REF03(Element):
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


class L2220D_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2220D_REF(Segment):
    """Service Line Item Identification"""
    class Schema:
        json = {'title': 'Service Line Item Identification',
         'usage': 'S',
         'description': 'xid=REF name=Service Line Item Identification',
         'position': 2000,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2220D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2220D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2220D_REF01
    ref02: L2220D_REF02


class L2220D_DTP01(Element):
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


class L2220D_DTP02(Element):
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


class L2220D_DTP03(Element):
    """Service Line Date"""
    class Schema:
        json = {'title': 'Service Line Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2220D_DTP(Segment):
    """Service Line Date"""
    class Schema:
        json = {'title': 'Service Line Date',
         'usage': 'R',
         'description': 'xid=DTP name=Service Line Date',
         'position': 2100,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2220D_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2220D_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2220D_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2220D_DTP01
    dtp02: L2220D_DTP02
    dtp03: L2220D_DTP03


class L2220D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Line Information',
                   'usage': 'S',
                   'description': 'xid=2220D name=Service Line Information type=None',
                   'position': 1800,
                   'type': 'object',
                   'properties': {'svc': {'$ref': '#/$segments/L2220D_SVC'},
                                  'stc': {'$ref': '#/$segments/L2220D_STC'},
                                  'ref': {'$ref': '#/$segments/L2220D_REF'},
                                  'dtp': {'$ref': '#/$segments/L2220D_DTP'}},
                   'required': ['svc', 'stc', 'dtp']}}
    svc: L2220D_SVC
    stc: list[L2220D_STC]
    ref: L2220D_REF | None
    dtp: L2220D_DTP


class L2200D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Status Tracking Number',
                   'usage': 'S',
                   'description': 'xid=2200D name=Claim Status Tracking Number '
                                  'type=None',
                   'position': 900,
                   'type': 'object',
                   'properties': {'trn': {'$ref': '#/$segments/L2200D_TRN'},
                                  'stc': {'$ref': '#/$segments/L2200D_STC'},
                                  'ref': {'$ref': '#/$segments/L2200D_REF'},
                                  'dtp': {'$ref': '#/$segments/L2200D_DTP'},
                                  'l2220d': {'$ref': '#/$segments/L2220D'}},
                   'required': ['trn', 'stc']}}
    trn: L2200D_TRN
    stc: list[L2200D_STC]
    ref: L2200D_REF | None
    ref: L2200D_REF | None
    ref: L2200D_REF | None
    ref: L2200D_REF | None
    ref: L2200D_REF | None
    ref: L2200D_REF | None
    dtp: L2200D_DTP | None
    l2220d: list[L2220D] | None


class L2000D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Level',
                   'usage': 'S',
                   'description': 'xid=2000D name=Subscriber Level type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000D_HL'},
                                  'l2100d': {'$ref': '#/$segments/L2100D'},
                                  'l2200d': {'$ref': '#/$segments/L2200D'}},
                   'required': ['hl', 'l2100d']}}
    hl: L2000D_HL
    l2100d: list[L2100D]
    l2200d: list[L2200D] | None


class TABLE2AREA5(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table2 - Area5',
                   'usage': 'S',
                   'description': 'xid=TABLE2AREA5 name=Table2 - Area5 type=wrapper',
                   'position': 150,
                   'type': 'object',
                   'properties': {'l2000d': {'$ref': '#/$segments/L2000D'}}}}
    l2000d: list[L2000D] | None


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
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['23']}]}}
        datatype = common.D_735
        codes = ['23']
        min_len = 1
        max_len = 2


class L2000E_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'N',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'$ref': '#/$common/736'}}
        datatype = common.D_736
        min_len = 1
        max_len = 1


class L2000E_HL(Segment):
    """Dependent Level"""
    class Schema:
        json = {'title': 'Dependent Level',
         'usage': 'R',
         'description': 'xid=HL name=Dependent Level',
         'position': 100,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000E_HL01'},
                        'hl02': {'$ref': '#/$elements/L2000E_HL02'},
                        'hl03': {'$ref': '#/$elements/L2000E_HL03'}},
         'required': ['hl01', 'hl02', 'hl03']}
        segment_name = 'HL'
    hl01: L2000E_HL01
    hl02: L2000E_HL02
    hl03: L2000E_HL03


class L2100E_NM101(Element):
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


class L2100E_NM102(Element):
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


class L2100E_NM103(Element):
    """Patient Last Name"""
    class Schema:
        json = {'title': 'Patient Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100E_NM104(Element):
    """Patient First Name"""
    class Schema:
        json = {'title': 'Patient First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100E_NM105(Element):
    """Patient Middle Name or Initial"""
    class Schema:
        json = {'title': 'Patient Middle Name or Initial',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100E_NM106(Element):
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


class L2100E_NM107(Element):
    """Patient Name Suffix"""
    class Schema:
        json = {'title': 'Patient Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100E_NM108(Element):
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


class L2100E_NM109(Element):
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


class L2100E_NM110(Element):
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


class L2100E_NM111(Element):
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


class L2100E_NM112(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM112 data_ele=1035',
         'sequence': 12,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100E_NM1(Segment):
    """Dependent Name"""
    class Schema:
        json = {'title': 'Dependent Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Dependent Name',
         'position': 500,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100E_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100E_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100E_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100E_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100E_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100E_NM107'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2100E_NM101
    nm102: L2100E_NM102
    nm103: L2100E_NM103
    nm104: L2100E_NM104 | None
    nm105: L2100E_NM105 | None
    nm107: L2100E_NM107 | None


class L2100E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Name',
                   'usage': 'R',
                   'description': 'xid=2100E name=Dependent Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100E_NM1'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100E_NM1


class L2200E_TRN01(Element):
    """Trace Type Code"""
    class Schema:
        json = {'title': 'Trace Type Code',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/481'}, {'enum': ['2']}]}}
        datatype = common.D_481
        codes = ['2']
        min_len = 1
        max_len = 2


class L2200E_TRN02(Element):
    """Referenced Transaction Trace Number"""
    class Schema:
        json = {'title': 'Referenced Transaction Trace Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_TRN03(Element):
    """Originating Company Identifier"""
    class Schema:
        json = {'title': 'Originating Company Identifier',
         'usage': 'N',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class L2200E_TRN04(Element):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'N',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_TRN(Segment):
    """Claim Status Tracking Number"""
    class Schema:
        json = {'title': 'Claim Status Tracking Number',
         'usage': 'R',
         'description': 'xid=TRN name=Claim Status Tracking Number',
         'position': 900,
         'type': 'object',
         'properties': {'xid': {'literal': 'TRN'},
                        'trn01': {'$ref': '#/$elements/L2200E_TRN01'},
                        'trn02': {'$ref': '#/$elements/L2200E_TRN02'}},
         'required': ['trn01', 'trn02']}
        segment_name = 'TRN'
    trn01: L2200E_TRN01
    trn02: L2200E_TRN02


class L2200E_STC01_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC01-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200E_STC01_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200E_STC01_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC01-03 data_ele=98',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['03', '13', '17', '1E', '1G', '1H', '1I', '1O',
                                      '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W',
                                      '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E',
                                      '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36',
                                      '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I',
                                      '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q',
                                      '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y',
                                      '3Z', '40', '43', '44', '4A', '4B', '4C', '4D',
                                      '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M',
                                      '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V',
                                      '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D',
                                      '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L',
                                      '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T',
                                      '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A',
                                      '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I',
                                      '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q',
                                      '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71',
                                      '72', '73', '74', '77', '7C', '80', '82', '84',
                                      '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ',
                                      'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9',
                                      'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI',
                                      'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ',
                                      'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD',
                                      'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP',
                                      'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE',
                                      'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY',
                                      'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL',
                                      'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5',
                                      'ZZ']}]}}
        datatype = common.D_98
        codes = ['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ']
        min_len = 2
        max_len = 3


class L2200E_STC01_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC01-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2200E_STC01(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'R',
         'description': 'xid=STC01 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'stc01_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/98'},
                                                        {'enum': ['03', '13', '17',
                                                                  '1E', '1G', '1H',
                                                                  '1I', '1O', '1P',
                                                                  '1Q', '1R', '1S',
                                                                  '1T', '1U', '1V',
                                                                  '1W', '1X', '1Y',
                                                                  '1Z', '28', '2A',
                                                                  '2B', '2D', '2E',
                                                                  '2I', '2K', '2P',
                                                                  '2Q', '2S', '2Z',
                                                                  '30', '36', '3A',
                                                                  '3C', '3D', '3E',
                                                                  '3F', '3G', '3H',
                                                                  '3I', '3J', '3K',
                                                                  '3L', '3M', '3N',
                                                                  '3O', '3P', '3Q',
                                                                  '3R', '3S', '3T',
                                                                  '3U', '3V', '3W',
                                                                  '3X', '3Y', '3Z',
                                                                  '40', '43', '44',
                                                                  '4A', '4B', '4C',
                                                                  '4D', '4E', '4F',
                                                                  '4G', '4H', '4I',
                                                                  '4J', '4L', '4M',
                                                                  '4N', '4O', '4P',
                                                                  '4Q', '4R', '4S',
                                                                  '4U', '4V', '4W',
                                                                  '4X', '4Y', '4Z',
                                                                  '5A', '5B', '5C',
                                                                  '5D', '5E', '5F',
                                                                  '5G', '5H', '5I',
                                                                  '5J', '5K', '5L',
                                                                  '5M', '5N', '5O',
                                                                  '5P', '5Q', '5R',
                                                                  '5S', '5T', '5U',
                                                                  '5V', '5W', '5X',
                                                                  '5Y', '5Z', '61',
                                                                  '6A', '6B', '6C',
                                                                  '6D', '6E', '6F',
                                                                  '6G', '6H', '6I',
                                                                  '6J', '6K', '6L',
                                                                  '6M', '6N', '6O',
                                                                  '6P', '6Q', '6R',
                                                                  '6S', '6U', '6V',
                                                                  '6W', '6X', '6Y',
                                                                  '71', '72', '73',
                                                                  '74', '77', '7C',
                                                                  '80', '82', '84',
                                                                  '85', '87', '95',
                                                                  'CK', 'CZ', 'D2',
                                                                  'DD', 'DJ', 'DK',
                                                                  'DN', 'DO', 'DQ',
                                                                  'E1', 'E2', 'E7',
                                                                  'E9', 'FA', 'FD',
                                                                  'FE', 'G0', 'G3',
                                                                  'GB', 'GD', 'GI',
                                                                  'GJ', 'GK', 'GM',
                                                                  'GY', 'HF', 'HH',
                                                                  'I3', 'IJ', 'IL',
                                                                  'IN', 'LI', 'LR',
                                                                  'MR', 'MSC', 'OB',
                                                                  'OD', 'OX', 'P0',
                                                                  'P2', 'P3', 'P4',
                                                                  'P6', 'P7', 'PRP',
                                                                  'PT', 'PV', 'PW',
                                                                  'QA', 'QB', 'QC',
                                                                  'QD', 'QE', 'QH',
                                                                  'QK', 'QL', 'QN',
                                                                  'QO', 'QS', 'QV',
                                                                  'QY', 'RC', 'RW',
                                                                  'S4', 'SEP', 'SJ',
                                                                  'SU', 'T4', 'TL',
                                                                  'TQ', 'TT', 'TTP',
                                                                  'TU', 'UH', 'X3',
                                                                  'X4', 'X5',
                                                                  'ZZ']}]}},
                        'stc01_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc01_01', 'stc01_02']}
    stc01_01: L2200E_STC01_01
    stc01_02: L2200E_STC01_02
    stc01_03: L2200E_STC01_03 | None
    stc01_04: L2200E_STC01_04 | None


class L2200E_STC02(Element):
    """Status Information Effective Date"""
    class Schema:
        json = {'title': 'Status Information Effective Date',
         'usage': 'R',
         'description': 'xid=STC02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200E_STC03(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'N',
         'description': 'xid=STC03 data_ele=306',
         'sequence': 3,
         'type': {'$ref': '#/$common/306'}}
        datatype = common.D_306
        min_len = 1
        max_len = 2


class L2200E_STC04(Element):
    """Total Claim Charge Amount"""
    class Schema:
        json = {'title': 'Total Claim Charge Amount',
         'usage': 'S',
         'description': 'xid=STC04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200E_STC05(Element):
    """Claim Payment Amount"""
    class Schema:
        json = {'title': 'Claim Payment Amount',
         'usage': 'S',
         'description': 'xid=STC05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200E_STC06(Element):
    """Adjudication Finalized Date"""
    class Schema:
        json = {'title': 'Adjudication Finalized Date',
         'usage': 'S',
         'description': 'xid=STC06 data_ele=373',
         'sequence': 6,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200E_STC07(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'N',
         'description': 'xid=STC07 data_ele=591',
         'sequence': 7,
         'type': {'$ref': '#/$common/591'}}
        datatype = common.D_591
        min_len = 3
        max_len = 3


class L2200E_STC08(Element):
    """Remittance Date"""
    class Schema:
        json = {'title': 'Remittance Date',
         'usage': 'S',
         'description': 'xid=STC08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2200E_STC09(Element):
    """Remittance Trace Number"""
    class Schema:
        json = {'title': 'Remittance Trace Number',
         'usage': 'S',
         'description': 'xid=STC09 data_ele=429',
         'sequence': 9,
         'type': {'$ref': '#/$common/429'}}
        datatype = common.D_429
        min_len = 1
        max_len = 16


class L2200E_STC10_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC10-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200E_STC10_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200E_STC10_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC10-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200E_STC10_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC10-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2200E_STC10(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC10 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'stc10_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc10_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc10_01', 'stc10_02']}
    stc10_01: L2200E_STC10_01
    stc10_02: L2200E_STC10_02
    stc10_03: L2200E_STC10_03 | None
    stc10_04: L2200E_STC10_04 | None


class L2200E_STC11_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC11-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200E_STC11_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2200E_STC11_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC11-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2200E_STC11_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC11-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2200E_STC11(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC11 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'stc11_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc11_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc11_01', 'stc11_02']}
    stc11_01: L2200E_STC11_01
    stc11_02: L2200E_STC11_02
    stc11_03: L2200E_STC11_03 | None
    stc11_04: L2200E_STC11_04 | None


class L2200E_STC12(Element):
    """Free-form Message Text"""
    class Schema:
        json = {'title': 'Free-form Message Text',
         'usage': 'N',
         'description': 'xid=STC12 data_ele=933',
         'sequence': 12,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2200E_STC(Segment):
    """Claim Level Status Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Level Status Information',
                   'usage': 'R',
                   'description': 'xid=STC name=Claim Level Status Information',
                   'position': 1000,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'STC'},
                                  'stc01': {'$ref': '#/$elements/L2200E_STC01'},
                                  'stc02': {'$ref': '#/$elements/L2200E_STC02'},
                                  'stc04': {'$ref': '#/$elements/L2200E_STC04'},
                                  'stc05': {'$ref': '#/$elements/L2200E_STC05'},
                                  'stc06': {'$ref': '#/$elements/L2200E_STC06'},
                                  'stc08': {'$ref': '#/$elements/L2200E_STC08'},
                                  'stc09': {'$ref': '#/$elements/L2200E_STC09'},
                                  'stc10': {'$ref': '#/$elements/L2200E_STC10'},
                                  'stc11': {'$ref': '#/$elements/L2200E_STC11'}},
                   'required': ['stc01', 'stc02']}}
        segment_name = 'STC'
    stc01: L2200E_STC01
    stc02: L2200E_STC02
    stc04: L2200E_STC04 | None
    stc05: L2200E_STC05 | None
    stc06: L2200E_STC06 | None
    stc08: L2200E_STC08 | None
    stc09: L2200E_STC09 | None
    stc10: L2200E_STC10 | None
    stc11: L2200E_STC11 | None


class L2200E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['1K']}]}}
        datatype = common.D_128
        codes = ['1K']
        min_len = 2
        max_len = 3


class L2200E_REF02(Element):
    """Payer Claim Control Number"""
    class Schema:
        json = {'title': 'Payer Claim Control Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_REF03(Element):
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


class L2200E_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200E_REF(Segment):
    """Payer Claim Control Number"""
    class Schema:
        json = {'title': 'Payer Claim Control Number',
         'usage': 'S',
         'description': 'xid=REF name=Payer Claim Control Number',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200E_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200E_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200E_REF01
    ref02: L2200E_REF02


class L2200E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['BLT']}]}}
        datatype = common.D_128
        codes = ['BLT']
        min_len = 2
        max_len = 3


class L2200E_REF02(Element):
    """Bill Type Identifier"""
    class Schema:
        json = {'title': 'Bill Type Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_REF03(Element):
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


class L2200E_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200E_REF(Segment):
    """Institutional Bill Type Identification"""
    class Schema:
        json = {'title': 'Institutional Bill Type Identification',
         'usage': 'S',
         'description': 'xid=REF name=Institutional Bill Type Identification',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200E_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200E_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200E_REF01
    ref02: L2200E_REF02


class L2200E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['EJ']}]}}
        datatype = common.D_128
        codes = ['EJ']
        min_len = 2
        max_len = 3


class L2200E_REF02(Element):
    """Patient Control Number"""
    class Schema:
        json = {'title': 'Patient Control Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_REF03(Element):
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


class L2200E_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200E_REF(Segment):
    """Patient Control Number"""
    class Schema:
        json = {'title': 'Patient Control Number',
         'usage': 'S',
         'description': 'xid=REF name=Patient Control Number',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200E_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200E_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200E_REF01
    ref02: L2200E_REF02


class L2200E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['XZ']}]}}
        datatype = common.D_128
        codes = ['XZ']
        min_len = 2
        max_len = 3


class L2200E_REF02(Element):
    """Pharmacy Prescription Number"""
    class Schema:
        json = {'title': 'Pharmacy Prescription Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_REF03(Element):
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


class L2200E_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200E_REF(Segment):
    """Pharmacy Prescription Number"""
    class Schema:
        json = {'title': 'Pharmacy Prescription Number',
         'usage': 'S',
         'description': 'xid=REF name=Pharmacy Prescription Number',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200E_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200E_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200E_REF01
    ref02: L2200E_REF02


class L2200E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['VV']}]}}
        datatype = common.D_128
        codes = ['VV']
        min_len = 2
        max_len = 3


class L2200E_REF02(Element):
    """Voucher Identifier"""
    class Schema:
        json = {'title': 'Voucher Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_REF03(Element):
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


class L2200E_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200E_REF(Segment):
    """Voucher Identifier"""
    class Schema:
        json = {'title': 'Voucher Identifier',
         'usage': 'S',
         'description': 'xid=REF name=Voucher Identifier',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200E_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200E_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200E_REF01
    ref02: L2200E_REF02


class L2200E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['D9']}]}}
        datatype = common.D_128
        codes = ['D9']
        min_len = 2
        max_len = 3


class L2200E_REF02(Element):
    """Clearinghouse Trace Number"""
    class Schema:
        json = {'title': 'Clearinghouse Trace Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2200E_REF03(Element):
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


class L2200E_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2200E_REF(Segment):
    """Claim Identification Number For Clearinghouses and Other Transmission Intermediaries"""
    class Schema:
        json = {'title': 'Claim Identification Number For Clearinghouses and Other '
                  'Transmission Intermediaries',
         'usage': 'S',
         'description': 'xid=REF name=Claim Identification Number For Clearinghouses '
                        'and Other Transmission Intermediaries',
         'position': 1100,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2200E_REF01'},
                        'ref02': {'$ref': '#/$elements/L2200E_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2200E_REF01
    ref02: L2200E_REF02


class L2200E_DTP01(Element):
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


class L2200E_DTP02(Element):
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


class L2200E_DTP03(Element):
    """Claim Service Period"""
    class Schema:
        json = {'title': 'Claim Service Period',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2200E_DTP(Segment):
    """Claim Service Date"""
    class Schema:
        json = {'title': 'Claim Service Date',
         'usage': 'S',
         'description': 'xid=DTP name=Claim Service Date',
         'position': 1200,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2200E_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2200E_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2200E_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2200E_DTP01
    dtp02: L2200E_DTP02
    dtp03: L2200E_DTP03


class L2220E_SVC01_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SVC01-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU',
                                      'WK']}]}}
        datatype = common.D_235
        codes = ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU', 'WK']
        min_len = 2
        max_len = 2


class L2220E_SVC01_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SVC01-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2220E_SVC01_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220E_SVC01_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220E_SVC01_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220E_SVC01_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC01-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2220E_SVC01_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=SVC01-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2220E_SVC01_08(Element):
    """Product/Service ID"""
    class Schema:
        json = {'title': 'Product/Service ID',
         'usage': 'N',
         'description': 'xid=SVC01-08 data_ele=234',
         'sequence': 8,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2220E_SVC01(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'R',
         'description': 'xid=SVC01 name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'svc01_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SVC01-01 data_ele=235',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD', 'ER', 'HC',
                                                                  'HP', 'IV', 'N4',
                                                                  'NU', 'WK']}]}},
                        'svc01_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SVC01-02 data_ele=234',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'svc01_03': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-03 data_ele=1339',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_04': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-04 data_ele=1339',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_05': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-05 data_ele=1339',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_06': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-06 data_ele=1339',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_07': {'title': 'Description',
                                     'usage': 'N',
                                     'description': 'xid=SVC01-07 data_ele=352',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/352'}},
                        'svc01_08': {'title': 'Product/Service ID',
                                     'usage': 'N',
                                     'description': 'xid=SVC01-08 data_ele=234',
                                     'sequence': 8,
                                     'type': {'$ref': '#/$common/234'}}},
         'required': ['svc01_01', 'svc01_02']}
    svc01_01: L2220E_SVC01_01
    svc01_02: L2220E_SVC01_02
    svc01_03: L2220E_SVC01_03 | None
    svc01_04: L2220E_SVC01_04 | None
    svc01_05: L2220E_SVC01_05 | None
    svc01_06: L2220E_SVC01_06 | None


class L2220E_SVC02(Element):
    """Line Item Charge Amount"""
    class Schema:
        json = {'title': 'Line Item Charge Amount',
         'usage': 'R',
         'description': 'xid=SVC02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220E_SVC03(Element):
    """Line Item Payment Amount"""
    class Schema:
        json = {'title': 'Line Item Payment Amount',
         'usage': 'R',
         'description': 'xid=SVC03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220E_SVC04(Element):
    """Revenue Code"""
    class Schema:
        json = {'title': 'Revenue Code',
         'usage': 'S',
         'description': 'xid=SVC04 data_ele=234',
         'sequence': 4,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2220E_SVC05(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=SVC05 data_ele=380',
         'sequence': 5,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2220E_SVC06(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'N',
         'description': 'xid=SVC06 name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 6,
         'syntax': []}


class L2220E_SVC07(Element):
    """Units of Service Count"""
    class Schema:
        json = {'title': 'Units of Service Count',
         'usage': 'R',
         'description': 'xid=SVC07 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2220E_SVC(Segment):
    """Service Line Information"""
    class Schema:
        json = {'title': 'Service Line Information',
         'usage': 'R',
         'description': 'xid=SVC name=Service Line Information',
         'position': 1800,
         'type': 'object',
         'properties': {'xid': {'literal': 'SVC'},
                        'svc01': {'$ref': '#/$elements/L2220E_SVC01'},
                        'svc02': {'$ref': '#/$elements/L2220E_SVC02'},
                        'svc03': {'$ref': '#/$elements/L2220E_SVC03'},
                        'svc04': {'$ref': '#/$elements/L2220E_SVC04'},
                        'svc07': {'$ref': '#/$elements/L2220E_SVC07'}},
         'required': ['svc01', 'svc02', 'svc03', 'svc07']}
        segment_name = 'SVC'
    svc01: L2220E_SVC01
    svc02: L2220E_SVC02
    svc03: L2220E_SVC03
    svc04: L2220E_SVC04 | None
    svc07: L2220E_SVC07


class L2220E_STC01_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC01-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220E_STC01_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC01-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220E_STC01_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC01-03 data_ele=98',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['03', '13', '17', '1E', '1G', '1H', '1I', '1O',
                                      '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W',
                                      '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E',
                                      '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36',
                                      '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I',
                                      '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q',
                                      '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y',
                                      '3Z', '40', '43', '44', '4A', '4B', '4C', '4D',
                                      '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M',
                                      '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V',
                                      '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D',
                                      '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L',
                                      '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T',
                                      '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A',
                                      '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I',
                                      '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q',
                                      '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71',
                                      '72', '73', '74', '77', '7C', '80', '82', '84',
                                      '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ',
                                      'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9',
                                      'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI',
                                      'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ',
                                      'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD',
                                      'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP',
                                      'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE',
                                      'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY',
                                      'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL',
                                      'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5',
                                      'ZZ']}]}}
        datatype = common.D_98
        codes = ['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ']
        min_len = 2
        max_len = 3


class L2220E_STC01_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC01-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2220E_STC01(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'R',
         'description': 'xid=STC01 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'stc01_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC01-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc01_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/98'},
                                                        {'enum': ['03', '13', '17',
                                                                  '1E', '1G', '1H',
                                                                  '1I', '1O', '1P',
                                                                  '1Q', '1R', '1S',
                                                                  '1T', '1U', '1V',
                                                                  '1W', '1X', '1Y',
                                                                  '1Z', '28', '2A',
                                                                  '2B', '2D', '2E',
                                                                  '2I', '2K', '2P',
                                                                  '2Q', '2S', '2Z',
                                                                  '30', '36', '3A',
                                                                  '3C', '3D', '3E',
                                                                  '3F', '3G', '3H',
                                                                  '3I', '3J', '3K',
                                                                  '3L', '3M', '3N',
                                                                  '3O', '3P', '3Q',
                                                                  '3R', '3S', '3T',
                                                                  '3U', '3V', '3W',
                                                                  '3X', '3Y', '3Z',
                                                                  '40', '43', '44',
                                                                  '4A', '4B', '4C',
                                                                  '4D', '4E', '4F',
                                                                  '4G', '4H', '4I',
                                                                  '4J', '4L', '4M',
                                                                  '4N', '4O', '4P',
                                                                  '4Q', '4R', '4S',
                                                                  '4U', '4V', '4W',
                                                                  '4X', '4Y', '4Z',
                                                                  '5A', '5B', '5C',
                                                                  '5D', '5E', '5F',
                                                                  '5G', '5H', '5I',
                                                                  '5J', '5K', '5L',
                                                                  '5M', '5N', '5O',
                                                                  '5P', '5Q', '5R',
                                                                  '5S', '5T', '5U',
                                                                  '5V', '5W', '5X',
                                                                  '5Y', '5Z', '61',
                                                                  '6A', '6B', '6C',
                                                                  '6D', '6E', '6F',
                                                                  '6G', '6H', '6I',
                                                                  '6J', '6K', '6L',
                                                                  '6M', '6N', '6O',
                                                                  '6P', '6Q', '6R',
                                                                  '6S', '6U', '6V',
                                                                  '6W', '6X', '6Y',
                                                                  '71', '72', '73',
                                                                  '74', '77', '7C',
                                                                  '80', '82', '84',
                                                                  '85', '87', '95',
                                                                  'CK', 'CZ', 'D2',
                                                                  'DD', 'DJ', 'DK',
                                                                  'DN', 'DO', 'DQ',
                                                                  'E1', 'E2', 'E7',
                                                                  'E9', 'FA', 'FD',
                                                                  'FE', 'G0', 'G3',
                                                                  'GB', 'GD', 'GI',
                                                                  'GJ', 'GK', 'GM',
                                                                  'GY', 'HF', 'HH',
                                                                  'I3', 'IJ', 'IL',
                                                                  'IN', 'LI', 'LR',
                                                                  'MR', 'MSC', 'OB',
                                                                  'OD', 'OX', 'P0',
                                                                  'P2', 'P3', 'P4',
                                                                  'P6', 'P7', 'PRP',
                                                                  'PT', 'PV', 'PW',
                                                                  'QA', 'QB', 'QC',
                                                                  'QD', 'QE', 'QH',
                                                                  'QK', 'QL', 'QN',
                                                                  'QO', 'QS', 'QV',
                                                                  'QY', 'RC', 'RW',
                                                                  'S4', 'SEP', 'SJ',
                                                                  'SU', 'T4', 'TL',
                                                                  'TQ', 'TT', 'TTP',
                                                                  'TU', 'UH', 'X3',
                                                                  'X4', 'X5',
                                                                  'ZZ']}]}},
                        'stc01_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC01-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc01_01', 'stc01_02']}
    stc01_01: L2220E_STC01_01
    stc01_02: L2220E_STC01_02
    stc01_03: L2220E_STC01_03 | None
    stc01_04: L2220E_STC01_04 | None


class L2220E_STC02(Element):
    """Status Information Effective Date"""
    class Schema:
        json = {'title': 'Status Information Effective Date',
         'usage': 'R',
         'description': 'xid=STC02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2220E_STC03(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'N',
         'description': 'xid=STC03 data_ele=306',
         'sequence': 3,
         'type': {'$ref': '#/$common/306'}}
        datatype = common.D_306
        min_len = 1
        max_len = 2


class L2220E_STC04(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220E_STC05(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=STC05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2220E_STC06(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC06 data_ele=373',
         'sequence': 6,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2220E_STC07(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'N',
         'description': 'xid=STC07 data_ele=591',
         'sequence': 7,
         'type': {'$ref': '#/$common/591'}}
        datatype = common.D_591
        min_len = 3
        max_len = 3


class L2220E_STC08(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=STC08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2220E_STC09(Element):
    """Check Number"""
    class Schema:
        json = {'title': 'Check Number',
         'usage': 'N',
         'description': 'xid=STC09 data_ele=429',
         'sequence': 9,
         'type': {'$ref': '#/$common/429'}}
        datatype = common.D_429
        min_len = 1
        max_len = 16


class L2220E_STC10_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC10-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220E_STC10_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC10-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220E_STC10_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC10-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2220E_STC10_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC10-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2220E_STC10(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC10 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 10,
         'syntax': [],
         'type': 'object',
         'properties': {'stc10_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC10-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc10_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc10_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC10-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc10_01', 'stc10_02']}
    stc10_01: L2220E_STC10_01
    stc10_02: L2220E_STC10_02
    stc10_03: L2220E_STC10_03 | None
    stc10_04: L2220E_STC10_04 | None


class L2220E_STC11_01(Element):
    """Health Care Claim Status Category Code"""
    class Schema:
        json = {'title': 'Health Care Claim Status Category Code',
         'usage': 'R',
         'description': 'xid=STC11-01 data_ele=1271',
         'sequence': 1,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220E_STC11_02(Element):
    """Status Code"""
    class Schema:
        json = {'title': 'Status Code',
         'usage': 'R',
         'description': 'xid=STC11-02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2220E_STC11_03(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'S',
         'description': 'xid=STC11-03 data_ele=98',
         'sequence': 3,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2220E_STC11_04(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'S',
         'description': 'xid=STC11-04 data_ele=1270',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['RX']}]}}
        datatype = common.D_1270
        codes = ['RX']
        min_len = 1
        max_len = 3


class L2220E_STC11(Composite):
    class Schema:
        json = {'title': 'Health Care Claim Status',
         'usage': 'S',
         'description': 'xid=STC11 name=Health Care Claim Status refdes= data_ele=C043',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'stc11_01': {'title': 'Health Care Claim Status Category Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-01 data_ele=1271',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_02': {'title': 'Status Code',
                                     'usage': 'R',
                                     'description': 'xid=STC11-02 data_ele=1271',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1271'}},
                        'stc11_03': {'title': 'Entity Identifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-03 data_ele=98',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/98'}},
                        'stc11_04': {'title': 'Code List Qualifier Code',
                                     'usage': 'S',
                                     'description': 'xid=STC11-04 data_ele=1270',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1270'},
                                                        {'enum': ['RX']}]}}},
         'required': ['stc11_01', 'stc11_02']}
    stc11_01: L2220E_STC11_01
    stc11_02: L2220E_STC11_02
    stc11_03: L2220E_STC11_03 | None
    stc11_04: L2220E_STC11_04 | None


class L2220E_STC12(Element):
    """Free-form Message Text"""
    class Schema:
        json = {'title': 'Free-form Message Text',
         'usage': 'N',
         'description': 'xid=STC12 data_ele=933',
         'sequence': 12,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2220E_STC(Segment):
    """Service Line Status Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Line Status Information',
                   'usage': 'R',
                   'description': 'xid=STC name=Service Line Status Information',
                   'position': 1900,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'STC'},
                                  'stc01': {'$ref': '#/$elements/L2220E_STC01'},
                                  'stc02': {'$ref': '#/$elements/L2220E_STC02'},
                                  'stc10': {'$ref': '#/$elements/L2220E_STC10'},
                                  'stc11': {'$ref': '#/$elements/L2220E_STC11'}},
                   'required': ['stc01', 'stc02']}}
        segment_name = 'STC'
    stc01: L2220E_STC01
    stc02: L2220E_STC02
    stc10: L2220E_STC10 | None
    stc11: L2220E_STC11 | None


class L2220E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['FJ']}]}}
        datatype = common.D_128
        codes = ['FJ']
        min_len = 2
        max_len = 3


class L2220E_REF02(Element):
    """Line Item Control Number"""
    class Schema:
        json = {'title': 'Line Item Control Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2220E_REF03(Element):
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


class L2220E_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2220E_REF(Segment):
    """Service Line Item Identification"""
    class Schema:
        json = {'title': 'Service Line Item Identification',
         'usage': 'S',
         'description': 'xid=REF name=Service Line Item Identification',
         'position': 2000,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2220E_REF01'},
                        'ref02': {'$ref': '#/$elements/L2220E_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2220E_REF01
    ref02: L2220E_REF02


class L2220E_DTP01(Element):
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


class L2220E_DTP02(Element):
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


class L2220E_DTP03(Element):
    """Service Line Date"""
    class Schema:
        json = {'title': 'Service Line Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2220E_DTP(Segment):
    """Service Line Date"""
    class Schema:
        json = {'title': 'Service Line Date',
         'usage': 'R',
         'description': 'xid=DTP name=Service Line Date',
         'position': 2100,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2220E_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2220E_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2220E_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2220E_DTP01
    dtp02: L2220E_DTP02
    dtp03: L2220E_DTP03


class L2220E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Line Information',
                   'usage': 'S',
                   'description': 'xid=2220E name=Service Line Information type=None',
                   'position': 1800,
                   'type': 'object',
                   'properties': {'svc': {'$ref': '#/$segments/L2220E_SVC'},
                                  'stc': {'$ref': '#/$segments/L2220E_STC'},
                                  'ref': {'$ref': '#/$segments/L2220E_REF'},
                                  'dtp': {'$ref': '#/$segments/L2220E_DTP'}},
                   'required': ['svc', 'stc', 'dtp']}}
    svc: L2220E_SVC
    stc: list[L2220E_STC]
    ref: L2220E_REF | None
    dtp: L2220E_DTP


class L2200E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Status Tracking Number',
                   'usage': 'R',
                   'description': 'xid=2200E name=Claim Status Tracking Number '
                                  'type=None',
                   'position': 900,
                   'type': 'object',
                   'properties': {'trn': {'$ref': '#/$segments/L2200E_TRN'},
                                  'stc': {'$ref': '#/$segments/L2200E_STC'},
                                  'ref': {'$ref': '#/$segments/L2200E_REF'},
                                  'dtp': {'$ref': '#/$segments/L2200E_DTP'},
                                  'l2220e': {'$ref': '#/$segments/L2220E'}},
                   'required': ['trn', 'stc']}}
    trn: L2200E_TRN
    stc: list[L2200E_STC]
    ref: L2200E_REF | None
    ref: L2200E_REF | None
    ref: L2200E_REF | None
    ref: L2200E_REF | None
    ref: L2200E_REF | None
    ref: L2200E_REF | None
    dtp: L2200E_DTP | None
    l2220e: list[L2220E] | None


class L2000E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Dependent Level',
                   'usage': 'S',
                   'description': 'xid=2000E name=Dependent Level type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000E_HL'},
                                  'l2100e': {'$ref': '#/$segments/L2100E'},
                                  'l2200e': {'$ref': '#/$segments/L2200E'}},
                   'required': ['hl', 'l2100e', 'l2200e']}}
    hl: L2000E_HL
    l2100e: list[L2100E]
    l2200e: list[L2200E]


class TABLE2AREA6(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table2 - Area6',
                   'usage': 'S',
                   'description': 'xid=TABLE2AREA6 name=Table2 - Area6 type=wrapper',
                   'position': 160,
                   'type': 'object',
                   'properties': {'l2000e': {'$ref': '#/$segments/L2000E'}}}}
    l2000e: list[L2000E] | None


class DETAIL(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table2 - Detail',
                   'usage': 'R',
                   'description': 'xid=DETAIL name=Table2 - Detail type=wrapper',
                   'position': 120,
                   'type': 'object',
                   'properties': {'l2000a': {'$ref': '#/$segments/L2000A'},
                                  'table2area4': {'$ref': '#/$segments/TABLE2AREA4'},
                                  'table2area5': {'$ref': '#/$segments/TABLE2AREA5'},
                                  'table2area6': {'$ref': '#/$segments/TABLE2AREA6'}},
                   'required': ['l2000a']}}
    l2000a: list[L2000A]
    table2area4: list[TABLE2AREA4] | None
    table2area5: list[TABLE2AREA5] | None
    table2area6: list[TABLE2AREA6] | None


class ST_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Transaction Set Header',
                   'usage': 'R',
                   'description': 'xid=ST_LOOP name=Transaction Set Header '
                                  'type=explicit',
                   'position': 200,
                   'type': 'object',
                   'properties': {'st': {'$ref': '#/$segments/ST_LOOP_ST'},
                                  'header': {'$ref': '#/$segments/HEADER'},
                                  'detail': {'$ref': '#/$segments/DETAIL'}},
                   'required': ['st', 'header', 'detail']}}
    st: ST_LOOP_ST
    header: list[HEADER]
    detail: list[DETAIL]


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Footer',
                   'usage': 'N',
                   'description': 'xid=FOOTER name=Footer type=wrapper',
                   'position': 170},
         'maxItems': 1}


class TABLE2AREA3_SE01(Element):
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


class TABLE2AREA3_SE02(Element):
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


class TABLE2AREA3_SE(Segment):
    """Transaction Set Trailer"""
    class Schema:
        json = {'title': 'Transaction Set Trailer',
         'usage': 'R',
         'description': 'xid=SE name=Transaction Set Trailer',
         'position': 2700,
         'type': 'object',
         'properties': {'xid': {'literal': 'SE'},
                        'se01': {'$ref': '#/$elements/TABLE2AREA3_SE01'},
                        'se02': {'$ref': '#/$elements/TABLE2AREA3_SE02'}},
         'required': ['se01', 'se02']}
        segment_name = 'SE'
    se01: TABLE2AREA3_SE01
    se02: TABLE2AREA3_SE02


class TABLE2AREA3(Loop):
    class Schema:
        json = {'title': 'Table2 - Area3',
         'usage': 'R',
         'description': 'xid=TABLE2AREA3 name=Table2 - Area3 type=wrapper',
         'position': 130,
         'type': 'object',
         'properties': {'se': {'$ref': '#/$segments/TABLE2AREA3_SE'}},
         'required': ['se']}
    se: TABLE2AREA3_SE


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
         'position': 300,
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
                   'position': 200,
                   'type': 'object',
                   'properties': {'gs': {'$ref': '#/$segments/GS_LOOP_GS'},
                                  'st_loop': {'$ref': '#/$segments/ST_LOOP'},
                                  'table2area3': {'$ref': '#/$segments/TABLE2AREA3'},
                                  'ge': {'$ref': '#/$segments/GS_LOOP_GE'}},
                   'required': ['gs', 'st_loop', 'table2area3', 'ge']}}
    gs: GS_LOOP_GS
    st_loop: list[ST_LOOP]
    table2area3: TABLE2AREA3
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
         'position': 200,
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
         'position': 300,
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
                   'position': 10,
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


class MSG277A1(Message):
    """HIPAA Health Care Information Status Notification 005010X212 277A1"""
    class Schema:
        json = {'title': 'HIPAA Health Care Information Status Notification 005010X212 277A1',
         'description': 'xid=277A1 name=HIPAA Health Care Information Status '
                        'Notification 005010X212 277A1',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
