"""
830.4010.PS
Created 2023-05-12 20:25:34.217061
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
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['PS']}]}}
        datatype = common.D_479
        codes = ['PS']
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
         'description': 'xid=GS04 data_ele=29',
         'position': 4,
         'type': {'$ref': '#/$common/29'}}
        datatype = common.D_29
        min_len = 6
        max_len = 8


class GS_LOOP_GS05(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'R',
         'description': 'xid=GS05 data_ele=30',
         'position': 5,
         'type': {'$ref': '#/$common/30'}}
        datatype = common.D_30
        min_len = 4
        max_len = 4


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
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['004010']}]}}
        datatype = common.D_480
        codes = ['004010']
        min_len = 1
        max_len = 12


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    class Schema:
        json = {'title': 'Functional Group Header',
         'usage': 'R',
         'description': 'xid=GS name=Functional Group Header',
         'position': 20,
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
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['830']}]}}
        datatype = common.D_143
        codes = ['830']
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
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'ST'},
                        'st01': {'$ref': '#/$elements/ST_LOOP_ST01'},
                        'st02': {'$ref': '#/$elements/ST_LOOP_ST02'}},
         'required': ['st01', 'st02']}
        segment_name = 'ST'
    st01: ST_LOOP_ST01
    st02: ST_LOOP_ST02


class HEADER_BFR01(Element):
    """Transaction Purpose Code"""
    class Schema:
        json = {'title': 'Transaction Purpose Code',
         'usage': 'R',
         'description': 'xid=BFR01 data_ele=353',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/353'}, {'enum': ['05']}]}}
        datatype = common.D_353
        codes = ['05']
        min_len = 2
        max_len = 2


class HEADER_BFR02(Element):
    """Forecast Order Number"""
    class Schema:
        json = {'title': 'Forecast Order Number',
         'usage': 'S',
         'description': 'xid=BFR02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_BFR03(Element):
    """Release Number"""
    class Schema:
        json = {'title': 'Release Number',
         'usage': 'R',
         'description': 'xid=BFR03 data_ele=328',
         'position': 3,
         'type': {'$ref': '#/$common/328'}}
        datatype = common.D_328
        min_len = 1
        max_len = 30


class HEADER_BFR04(Element):
    """Schedule Type Qualifier"""
    class Schema:
        json = {'title': 'Schedule Type Qualifier',
         'usage': 'R',
         'description': 'xid=BFR04 data_ele=675',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/675'}, {'enum': ['DL', 'SH']}]}}
        datatype = common.D_675
        codes = ['DL', 'SH']
        min_len = 2
        max_len = 2


class HEADER_BFR05(Element):
    """Schedule Quantity Qualifier"""
    class Schema:
        json = {'title': 'Schedule Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=BFR05 data_ele=676',
         'position': 5,
         'type': {'allOf': [{'$ref': '#/$common/676'}, {'enum': ['C', 'A']}]}}
        datatype = common.D_676
        codes = ['C', 'A']
        min_len = 1
        max_len = 1


class HEADER_BFR06(Element):
    """Horizon Start Date"""
    class Schema:
        json = {'title': 'Horizon Start Date',
         'usage': 'R',
         'description': 'xid=BFR06 data_ele=373',
         'position': 6,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BFR07(Element):
    """Horizon End Date"""
    class Schema:
        json = {'title': 'Horizon End Date',
         'usage': 'R',
         'description': 'xid=BFR07 data_ele=373',
         'position': 7,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BFR08(Element):
    """Generation Date"""
    class Schema:
        json = {'title': 'Generation Date',
         'usage': 'R',
         'description': 'xid=BFR08 data_ele=373',
         'position': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BFR09(Element):
    """Fordcast Updated Date"""
    class Schema:
        json = {'title': 'Fordcast Updated Date',
         'usage': 'S',
         'description': 'xid=BFR09 data_ele=373',
         'position': 9,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BFR10(Element):
    """Contract Number"""
    class Schema:
        json = {'title': 'Contract Number',
         'usage': 'S',
         'description': 'xid=BFR10 data_ele=367',
         'position': 10,
         'type': {'$ref': '#/$common/367'}}
        datatype = common.D_367


class HEADER_BFR11(Element):
    """Purchase Order Number"""
    class Schema:
        json = {'title': 'Purchase Order Number',
         'usage': 'S',
         'description': 'xid=BFR11 data_ele=324',
         'position': 11,
         'type': {'$ref': '#/$common/324'}}
        datatype = common.D_324
        min_len = 1
        max_len = 22


class HEADER_BFR(Segment):
    """Planning Schedule"""
    class Schema:
        json = {'title': 'Planning Schedule',
         'usage': 'R',
         'description': 'xid=BFR name=Planning Schedule',
         'position': 10,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'BFR'},
                        'bfr01': {'$ref': '#/$elements/HEADER_BFR01'},
                        'bfr02': {'$ref': '#/$elements/HEADER_BFR02'},
                        'bfr03': {'$ref': '#/$elements/HEADER_BFR03'},
                        'bfr04': {'$ref': '#/$elements/HEADER_BFR04'},
                        'bfr05': {'$ref': '#/$elements/HEADER_BFR05'},
                        'bfr06': {'$ref': '#/$elements/HEADER_BFR06'},
                        'bfr07': {'$ref': '#/$elements/HEADER_BFR07'},
                        'bfr08': {'$ref': '#/$elements/HEADER_BFR08'},
                        'bfr09': {'$ref': '#/$elements/HEADER_BFR09'},
                        'bfr10': {'$ref': '#/$elements/HEADER_BFR10'},
                        'bfr11': {'$ref': '#/$elements/HEADER_BFR11'}},
         'required': ['bfr01', 'bfr03', 'bfr04', 'bfr05', 'bfr06', 'bfr07', 'bfr08']}
        segment_name = 'BFR'
    bfr01: HEADER_BFR01
    bfr02: HEADER_BFR02 | None
    bfr03: HEADER_BFR03
    bfr04: HEADER_BFR04
    bfr05: HEADER_BFR05
    bfr06: HEADER_BFR06
    bfr07: HEADER_BFR07
    bfr08: HEADER_BFR08
    bfr09: HEADER_BFR09 | None
    bfr10: HEADER_BFR10 | None
    bfr11: HEADER_BFR11 | None


class N1_LOOP_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['SU', 'ST', 'MI', 'SF']}]}}
        datatype = common.D_98
        codes = ['SU', 'ST', 'MI', 'SF']
        min_len = 2
        max_len = 3


class N1_LOOP_N102(Element):
    """Payer Name"""
    class Schema:
        json = {'title': 'Payer Name',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class N1_LOOP_N103(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=N103 data_ele=66',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['1', '92']}]}}
        datatype = common.D_66
        codes = ['1', '92']
        min_len = 1
        max_len = 2


class N1_LOOP_N104(Element):
    """Payer Identifier"""
    class Schema:
        json = {'title': 'Payer Identifier',
         'usage': 'S',
         'description': 'xid=N104 data_ele=67',
         'position': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class N1_LOOP_N105(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'position': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class N1_LOOP_N106(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'position': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class N1_LOOP_N1(Segment):
    """Payer Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer Identification',
                   'usage': 'R',
                   'description': 'xid=N1 name=Payer Identification',
                   'position': 230,
                   'syntax': ['R0203', 'P0304'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'N1'},
                                  'n101': {'$ref': '#/$elements/N1_LOOP_N101'},
                                  'n102': {'$ref': '#/$elements/N1_LOOP_N102'},
                                  'n103': {'$ref': '#/$elements/N1_LOOP_N103'},
                                  'n104': {'$ref': '#/$elements/N1_LOOP_N104'},
                                  'n105': {'$ref': '#/$elements/N1_LOOP_N105'},
                                  'n106': {'$ref': '#/$elements/N1_LOOP_N106'}},
                   'required': ['n101']},
         'maxItems': 3}
        segment_name = 'N1'
    n101: N1_LOOP_N101
    n102: N1_LOOP_N102 | None
    n103: N1_LOOP_N103 | None
    n104: N1_LOOP_N104 | None
    n105: N1_LOOP_N105 | None
    n106: N1_LOOP_N106 | None


class N1_LOOP_PER01(Element):
    """ContactFunction Code"""
    class Schema:
        json = {'title': 'ContactFunction Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['EX']}]}}
        datatype = common.D_366
        codes = ['EX']
        min_len = 2
        max_len = 2


class N1_LOOP_PER02(Element):
    """ContactFunction Code"""
    class Schema:
        json = {'title': 'ContactFunction Code',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class N1_LOOP_PER03(Element):
    """ContactFunction Code"""
    class Schema:
        json = {'title': 'ContactFunction Code',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'$ref': '#/$common/365'}}
        datatype = common.D_365
        min_len = 2
        max_len = 2


class N1_LOOP_PER04(Element):
    """ContactFunction Code"""
    class Schema:
        json = {'title': 'ContactFunction Code',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class N1_LOOP_PER(Segment):
    """Administrative Communications Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Administrative Communications Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Administrative Communications '
                                  'Information',
                   'position': 280,
                   'syntax': ['P0304'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/N1_LOOP_PER01'},
                                  'per02': {'$ref': '#/$elements/N1_LOOP_PER02'},
                                  'per03': {'$ref': '#/$elements/N1_LOOP_PER03'},
                                  'per04': {'$ref': '#/$elements/N1_LOOP_PER04'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: N1_LOOP_PER01
    per02: N1_LOOP_PER02 | None
    per03: N1_LOOP_PER03 | None
    per04: N1_LOOP_PER04 | None


class N1_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Supplier',
                   'usage': 'R',
                   'description': 'xid=N1_LOOP name=Supplier type=wrapper',
                   'position': 230,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/N1_LOOP_N1'},
                                  'per': {'$ref': '#/$segments/N1_LOOP_PER'}},
                   'required': ['n1']},
         'maxItems': 200}
    n1: list[N1_LOOP_N1]
    per: list[N1_LOOP_PER] | None


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 1 - Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Table 1 - Header type=wrapper',
                   'position': 10,
                   'type': 'object',
                   'properties': {'bfr': {'$ref': '#/$segments/HEADER_BFR'},
                                  'n1_loop': {'$ref': '#/$segments/N1_LOOP'}},
                   'required': ['bfr', 'n1_loop']}}
    bfr: HEADER_BFR
    n1_loop: list[N1_LOOP]


class LIN_LOOP_LIN01(Element):
    """Assigned Identification"""
    class Schema:
        json = {'title': 'Assigned Identification',
         'usage': 'N',
         'description': 'xid=LIN01 data_ele=350',
         'position': 1,
         'type': {'$ref': '#/$common/350'}}
        datatype = common.D_350
        min_len = 1
        max_len = 20


class LIN_LOOP_LIN02(Element):
    """Buyer Part Number"""
    class Schema:
        json = {'title': 'Buyer Part Number',
         'usage': 'R',
         'description': 'xid=LIN02 data_ele=235',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/235'}, {'enum': ['BP']}]}}
        datatype = common.D_235
        codes = ['BP']
        min_len = 2
        max_len = 2


class LIN_LOOP_LIN03(Element):
    """Product/Service Id"""
    class Schema:
        json = {'title': 'Product/Service Id',
         'usage': 'S',
         'description': 'xid=LIN03 data_ele=234',
         'position': 3,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class LIN_LOOP_LIN04(Element):
    """Product/Service Id Qualifier"""
    class Schema:
        json = {'title': 'Product/Service Id Qualifier',
         'usage': 'S',
         'description': 'xid=LIN04 data_ele=235',
         'position': 4,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY',
                                      'VP']}]}}
        datatype = common.D_235
        codes = ['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY', 'VP']
        min_len = 2
        max_len = 2


class LIN_LOOP_LIN05(Element):
    """Product/Service Id"""
    class Schema:
        json = {'title': 'Product/Service Id',
         'usage': 'S',
         'description': 'xid=LIN05 data_ele=234',
         'position': 5,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class LIN_LOOP_LIN06(Element):
    """Product/Service Id Qualifier"""
    class Schema:
        json = {'title': 'Product/Service Id Qualifier',
         'usage': 'S',
         'description': 'xid=LIN06 data_ele=235',
         'position': 6,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY',
                                      'VP']}]}}
        datatype = common.D_235
        codes = ['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY', 'VP']
        min_len = 2
        max_len = 2


class LIN_LOOP_LIN07(Element):
    """Product/Service Id"""
    class Schema:
        json = {'title': 'Product/Service Id',
         'usage': 'S',
         'description': 'xid=LIN07 data_ele=234',
         'position': 7,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class LIN_LOOP_LIN08(Element):
    """Product/Service Id Qualifier"""
    class Schema:
        json = {'title': 'Product/Service Id Qualifier',
         'usage': 'S',
         'description': 'xid=LIN08 data_ele=235',
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY',
                                      'VP']}]}}
        datatype = common.D_235
        codes = ['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY', 'VP']
        min_len = 2
        max_len = 2


class LIN_LOOP_LIN(Segment):
    """Item Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Item Identification',
                   'usage': 'R',
                   'description': 'xid=LIN name=Item Identification',
                   'position': 10,
                   'syntax': ['P0405'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'LIN'},
                                  'lin01': {'$ref': '#/$elements/LIN_LOOP_LIN01'},
                                  'lin02': {'$ref': '#/$elements/LIN_LOOP_LIN02'},
                                  'lin03': {'$ref': '#/$elements/LIN_LOOP_LIN03'},
                                  'lin04': {'$ref': '#/$elements/LIN_LOOP_LIN04'},
                                  'lin05': {'$ref': '#/$elements/LIN_LOOP_LIN05'},
                                  'lin06': {'$ref': '#/$elements/LIN_LOOP_LIN06'},
                                  'lin07': {'$ref': '#/$elements/LIN_LOOP_LIN07'},
                                  'lin08': {'$ref': '#/$elements/LIN_LOOP_LIN08'}},
                   'required': ['lin02']}}
        segment_name = 'LIN'
    lin01: LIN_LOOP_LIN01 | None
    lin02: LIN_LOOP_LIN02
    lin03: LIN_LOOP_LIN03 | None
    lin04: LIN_LOOP_LIN04 | None
    lin05: LIN_LOOP_LIN05 | None
    lin06: LIN_LOOP_LIN06 | None
    lin07: LIN_LOOP_LIN07 | None
    lin08: LIN_LOOP_LIN08 | None


class LIN_LOOP_UIT01(Element):
    """Composite Unit of Measure"""
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'R',
         'description': 'xid=UIT01 data_ele=355',
         'position': 1,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class LIN_LOOP_UIT(Segment):
    """Unit Detail"""
    class Schema:
        json = {'title': 'Unit Detail',
         'usage': 'R',
         'description': 'xid=UIT name=Unit Detail',
         'position': 20,
         'syntax': ['C0302'],
         'type': 'object',
         'properties': {'xid': {'literal': 'UIT'},
                        'uit01': {'$ref': '#/$elements/LIN_LOOP_UIT01'}},
         'required': ['uit01']}
        segment_name = 'UIT'
    uit01: LIN_LOOP_UIT01


class LIN_LOOP_PID01(Element):
    """Item Descripton Type"""
    class Schema:
        json = {'title': 'Item Descripton Type',
         'usage': 'R',
         'description': 'xid=PID01 data_ele=349',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/349'}, {'enum': ['F']}]}}
        datatype = common.D_349
        codes = ['F']
        min_len = 1
        max_len = 1


class LIN_LOOP_PID02(Element):
    """Product/Process Characteristic Code"""
    class Schema:
        json = {'title': 'Product/Process Characteristic Code',
         'usage': 'S',
         'description': 'xid=PID02 data_ele=750',
         'position': 2,
         'type': {'$ref': '#/$common/750'}}
        datatype = common.D_750
        min_len = 2
        max_len = 3


class LIN_LOOP_PID03(Element):
    """Product/Process Characteristic Code"""
    class Schema:
        json = {'title': 'Product/Process Characteristic Code',
         'usage': 'S',
         'description': 'xid=PID03 data_ele=559',
         'position': 3,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class LIN_LOOP_PID04(Element):
    """Product/Process Characteristic Code"""
    class Schema:
        json = {'title': 'Product/Process Characteristic Code',
         'usage': 'S',
         'description': 'xid=PID04 data_ele=751',
         'position': 4,
         'type': {'$ref': '#/$common/751'}}
        datatype = common.D_751
        min_len = 1
        max_len = 12


class LIN_LOOP_PID05(Element):
    """Product/Process Characteristic Code"""
    class Schema:
        json = {'title': 'Product/Process Characteristic Code',
         'usage': 'S',
         'description': 'xid=PID05 data_ele=352',
         'position': 5,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class LIN_LOOP_PID(Segment):
    """Product/Item Description"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Product/Item Description',
                   'usage': 'S',
                   'description': 'xid=PID name=Product/Item Description',
                   'position': 30,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PID'},
                                  'pid01': {'$ref': '#/$elements/LIN_LOOP_PID01'},
                                  'pid02': {'$ref': '#/$elements/LIN_LOOP_PID02'},
                                  'pid03': {'$ref': '#/$elements/LIN_LOOP_PID03'},
                                  'pid04': {'$ref': '#/$elements/LIN_LOOP_PID04'},
                                  'pid05': {'$ref': '#/$elements/LIN_LOOP_PID05'}},
                   'required': ['pid01']},
         'maxItems': 1000}
        segment_name = 'PID'
    pid01: LIN_LOOP_PID01
    pid02: LIN_LOOP_PID02 | None
    pid03: LIN_LOOP_PID03 | None
    pid04: LIN_LOOP_PID04 | None
    pid05: LIN_LOOP_PID05 | None


class LIN_LOOP_ATH01(Element):
    """Resource Authorization Code"""
    class Schema:
        json = {'title': 'Resource Authorization Code',
         'usage': 'R',
         'description': 'xid=ATH01 data_ele=672',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/672'}, {'enum': ['FI', 'MT', 'PQ']}]}}
        datatype = common.D_672
        codes = ['FI', 'MT', 'PQ']
        min_len = 2
        max_len = 2


class LIN_LOOP_ATH02(Element):
    """Resource Authorization Date"""
    class Schema:
        json = {'title': 'Resource Authorization Date',
         'usage': 'S',
         'description': 'xid=ATH02 data_ele=373',
         'position': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class LIN_LOOP_ATH03(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'S',
         'description': 'xid=ATH03 data_ele=380',
         'position': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class LIN_LOOP_ATH04(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=ATH04 data_ele=380',
         'position': 4,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class LIN_LOOP_ATH05(Element):
    """Cumulative Start Date"""
    class Schema:
        json = {'title': 'Cumulative Start Date',
         'usage': 'S',
         'description': 'xid=ATH05 data_ele=373',
         'position': 5,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class LIN_LOOP_ATH(Segment):
    """Resource Authorization"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Resource Authorization',
                   'usage': 'S',
                   'description': 'xid=ATH name=Resource Authorization',
                   'position': 230,
                   'syntax': ['R0203', 'C0305', 'C0405'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'ATH'},
                                  'ath01': {'$ref': '#/$elements/LIN_LOOP_ATH01'},
                                  'ath02': {'$ref': '#/$elements/LIN_LOOP_ATH02'},
                                  'ath03': {'$ref': '#/$elements/LIN_LOOP_ATH03'},
                                  'ath04': {'$ref': '#/$elements/LIN_LOOP_ATH04'},
                                  'ath05': {'$ref': '#/$elements/LIN_LOOP_ATH05'}},
                   'required': ['ath01']},
         'maxItems': 20}
        segment_name = 'ATH'
    ath01: LIN_LOOP_ATH01
    ath02: LIN_LOOP_ATH02 | None
    ath03: LIN_LOOP_ATH03 | None
    ath04: LIN_LOOP_ATH04 | None
    ath05: LIN_LOOP_ATH05 | None


class FST_LOOP_FST01(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'R',
         'description': 'xid=FST01 data_ele=380',
         'position': 1,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class FST_LOOP_FST02(Element):
    """Forecast Qualifier"""
    class Schema:
        json = {'title': 'Forecast Qualifier',
         'usage': 'R',
         'description': 'xid=FST02 data_ele=680',
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/680'},
                            {'enum': ['A', 'C', 'D', 'B', 'Z']}]}}
        datatype = common.D_680
        codes = ['A', 'C', 'D', 'B', 'Z']
        min_len = 1
        max_len = 1


class FST_LOOP_FST03(Element):
    """Forecast Timing Qualifier"""
    class Schema:
        json = {'title': 'Forecast Timing Qualifier',
         'usage': 'R',
         'description': 'xid=FST03 data_ele=681',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/681'},
                            {'enum': ['F', 'M', 'W', 'D', 'Z']}]}}
        datatype = common.D_681
        codes = ['F', 'M', 'W', 'D', 'Z']
        min_len = 1
        max_len = 1


class FST_LOOP_FST04(Element):
    """Forecast Schedule Date"""
    class Schema:
        json = {'title': 'Forecast Schedule Date',
         'usage': 'R',
         'description': 'xid=FST04 data_ele=373',
         'position': 4,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class FST_LOOP_FST(Segment):
    """Forecast Schedule"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Forecast Schedule',
                   'usage': 'R',
                   'description': 'xid=FST name=Forecast Schedule',
                   'position': 410,
                   'syntax': ['P0607', 'P0809'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'FST'},
                                  'fst01': {'$ref': '#/$elements/FST_LOOP_FST01'},
                                  'fst02': {'$ref': '#/$elements/FST_LOOP_FST02'},
                                  'fst03': {'$ref': '#/$elements/FST_LOOP_FST03'},
                                  'fst04': {'$ref': '#/$elements/FST_LOOP_FST04'}},
                   'required': ['fst01', 'fst02', 'fst03', 'fst04']},
         'maxItems': 1000}
        segment_name = 'FST'
    fst01: FST_LOOP_FST01
    fst02: FST_LOOP_FST02
    fst03: FST_LOOP_FST03
    fst04: FST_LOOP_FST04


class FST_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Forecast',
                   'usage': 'R',
                   'description': 'xid=FST_LOOP name=Forecast type=wrapper',
                   'position': 410,
                   'type': 'object',
                   'properties': {'fst': {'$ref': '#/$segments/FST_LOOP_FST'}},
                   'required': ['fst']}}
    fst: list[FST_LOOP_FST]


class SHP_LOOP_SHP01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=SHP01 data_ele=673',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'}, {'enum': ['01', '02']}]}}
        datatype = common.D_673
        codes = ['01', '02']
        min_len = 2
        max_len = 2


class SHP_LOOP_SHP02(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'R',
         'description': 'xid=SHP02 data_ele=380',
         'position': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class SHP_LOOP_SHP03(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'R',
         'description': 'xid=SHP03 data_ele=374',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['011', '050', '051']}]}}
        datatype = common.D_374
        codes = ['011', '050', '051']
        min_len = 3
        max_len = 3


class SHP_LOOP_SHP04(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'S',
         'description': 'xid=SHP04 data_ele=373',
         'position': 4,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class SHP_LOOP_SHP(Segment):
    """Shipped/Received Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Shipped/Received Information',
                   'usage': 'R',
                   'description': 'xid=SHP name=Shipped/Received Information',
                   'position': 470,
                   'syntax': ['C0102', 'L030405', 'C0403'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'SHP'},
                                  'shp01': {'$ref': '#/$elements/SHP_LOOP_SHP01'},
                                  'shp02': {'$ref': '#/$elements/SHP_LOOP_SHP02'},
                                  'shp03': {'$ref': '#/$elements/SHP_LOOP_SHP03'},
                                  'shp04': {'$ref': '#/$elements/SHP_LOOP_SHP04'}},
                   'required': ['shp01', 'shp02', 'shp03']},
         'maxItems': 99}
        segment_name = 'SHP'
    shp01: SHP_LOOP_SHP01
    shp02: SHP_LOOP_SHP02
    shp03: SHP_LOOP_SHP03
    shp04: SHP_LOOP_SHP04 | None


class SHP_LOOP_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['SI']}]}}
        datatype = common.D_128
        codes = ['SI']
        min_len = 2
        max_len = 3


class SHP_LOOP_REF02(Element):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class SHP_LOOP_REF(Segment):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'S',
         'description': 'xid=REF name=Reference Identification',
         'position': 480,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/SHP_LOOP_REF01'},
                        'ref02': {'$ref': '#/$elements/SHP_LOOP_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: SHP_LOOP_REF01
    ref02: SHP_LOOP_REF02


class SHP_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Ship/RecInfo',
                   'usage': 'R',
                   'description': 'xid=SHP_LOOP name=Ship/RecInfo type=wrapper',
                   'position': 470,
                   'type': 'object',
                   'properties': {'shp': {'$ref': '#/$segments/SHP_LOOP_SHP'},
                                  'ref': {'$ref': '#/$segments/SHP_LOOP_REF'}},
                   'required': ['shp']}}
    shp: list[SHP_LOOP_SHP]
    ref: SHP_LOOP_REF | None


class LIN_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Line Item',
                   'usage': 'R',
                   'description': 'xid=LIN_LOOP name=Line Item type=None',
                   'position': 10,
                   'type': 'object',
                   'properties': {'lin': {'$ref': '#/$segments/LIN_LOOP_LIN'},
                                  'uit': {'$ref': '#/$segments/LIN_LOOP_UIT'},
                                  'pid': {'$ref': '#/$segments/LIN_LOOP_PID'},
                                  'ath': {'$ref': '#/$segments/LIN_LOOP_ATH'},
                                  'fst_loop': {'$ref': '#/$segments/FST_LOOP'},
                                  'shp_loop': {'$ref': '#/$segments/SHP_LOOP'}},
                   'required': ['lin', 'uit', 'fst_loop', 'shp_loop']}}
    lin: list[LIN_LOOP_LIN]
    uit: LIN_LOOP_UIT
    pid: list[LIN_LOOP_PID] | None
    ath: list[LIN_LOOP_ATH] | None
    fst_loop: list[FST_LOOP]
    shp_loop: list[SHP_LOOP]


class DETAIL(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 2 - Detail',
                   'usage': 'R',
                   'description': 'xid=DETAIL name=Table 2 - Detail type=explicit',
                   'position': 10,
                   'type': 'object',
                   'properties': {'lin_loop': {'$ref': '#/$segments/LIN_LOOP'}},
                   'required': ['lin_loop']}}
    lin_loop: list[LIN_LOOP]


class FOOTER_CTT01(Element):
    """Number of Line Items"""
    class Schema:
        json = {'title': 'Number of Line Items',
         'usage': 'R',
         'description': 'xid=CTT01 data_ele=354',
         'position': 1,
         'type': {'$ref': '#/$common/354'}}
        datatype = common.D_354
        min_len = 1
        max_len = 6


class FOOTER_CTT02(Element):
    """Hash Total"""
    class Schema:
        json = {'title': 'Hash Total',
         'usage': 'S',
         'description': 'xid=CTT02 data_ele=347',
         'position': 2,
         'type': {'$ref': '#/$common/347'}}
        datatype = common.D_347


class FOOTER_CTT(Segment):
    """Transaction Totals"""
    class Schema:
        json = {'title': 'Transaction Totals',
         'usage': 'S',
         'description': 'xid=CTT name=Transaction Totals',
         'position': 10,
         'syntax': ['P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'CTT'},
                        'ctt01': {'$ref': '#/$elements/FOOTER_CTT01'},
                        'ctt02': {'$ref': '#/$elements/FOOTER_CTT02'}},
         'required': ['ctt01']}
        segment_name = 'CTT'
    ctt01: FOOTER_CTT01
    ctt02: FOOTER_CTT02 | None


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 3 - Footer',
                   'usage': 'R',
                   'description': 'xid=FOOTER name=Table 3 - Footer type=wrapper',
                   'position': 10,
                   'type': 'object',
                   'properties': {'ctt': {'$ref': '#/$segments/FOOTER_CTT'}}},
         'maxItems': 1}
    ctt: FOOTER_CTT | None


class ST_LOOP_SE01(Element):
    """Transaction Segment Count"""
    class Schema:
        json = {'title': 'Transaction Segment Count',
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
         'position': 20,
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
                   'required': ['st', 'header', 'detail', 'footer', 'se']}}
    st: ST_LOOP_ST
    header: list[HEADER]
    detail: list[DETAIL]
    footer: list[FOOTER]
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
         'position': 40,
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
                                  'iea': {'$ref': '#/$segments/ISA_LOOP_IEA'}},
                   'required': ['isa', 'gs_loop', 'iea']}}
    isa: ISA_LOOP_ISA
    gs_loop: list[GS_LOOP]
    iea: ISA_LOOP_IEA


class MSG830(Message):
    """Forecast with Release capability - 830"""
    class Schema:
        json = {'title': 'Forecast with Release capability - 830',
         'description': 'xid=830 name=Forecast with Release capability - 830',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
