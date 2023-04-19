"""
837.4010.X097.A1
Created 2023-03-25 09:22:29.053471
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
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['HC']}]}}
        datatype = common.D_479
        codes = ['HC']
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
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['004010X097A1']}]}}
        datatype = common.D_480
        codes = ['004010X097A1']
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
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['837']}]}}
        datatype = common.D_143
        codes = ['837']
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
         'position': 5,
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
         'type': {'allOf': [{'$ref': '#/$common/1005'}, {'enum': ['0019']}]}}
        datatype = common.D_1005
        codes = ['0019']
        min_len = 4
        max_len = 4


class HEADER_BHT02(Element):
    """Transaction Set Purpose Code"""
    class Schema:
        json = {'title': 'Transaction Set Purpose Code',
         'usage': 'R',
         'description': 'xid=BHT02 data_ele=353',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/353'}, {'enum': ['00', '18']}]}}
        datatype = common.D_353
        codes = ['00', '18']
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
    """Claim or Encounter Identifier"""
    class Schema:
        json = {'title': 'Claim or Encounter Identifier',
         'usage': 'R',
         'description': 'xid=BHT06 data_ele=640',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/640'}, {'enum': ['CH', 'RP']}]}}
        datatype = common.D_640
        codes = ['CH', 'RP']
        min_len = 2
        max_len = 2


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    class Schema:
        json = {'title': 'Beginning of Hierarchical Transaction',
         'usage': 'R',
         'description': 'xid=BHT name=Beginning of Hierarchical Transaction',
         'position': 10,
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


class HEADER_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['87']}]}}
        datatype = common.D_128
        codes = ['87']
        min_len = 2
        max_len = 3


class HEADER_REF02(Element):
    """Transmission Type Code"""
    class Schema:
        json = {'title': 'Transmission Type Code',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_REF03(Element):
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


class HEADER_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class HEADER_REF(Segment):
    """Transmission Type Identification"""
    class Schema:
        json = {'title': 'Transmission Type Identification',
         'usage': 'R',
         'description': 'xid=REF name=Transmission Type Identification',
         'position': 15,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                        'ref02': {'$ref': '#/$elements/HEADER_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02


class L1000A_NM101(Element):
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


class L1000A_NM102(Element):
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


class L1000A_NM103(Element):
    """Submitter Last or Organization Name"""
    class Schema:
        json = {'title': 'Submitter Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L1000A_NM104(Element):
    """Submitter First Name"""
    class Schema:
        json = {'title': 'Submitter First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L1000A_NM105(Element):
    """Submitter Middle Name"""
    class Schema:
        json = {'title': 'Submitter Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L1000A_NM106(Element):
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


class L1000A_NM107(Element):
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


class L1000A_NM108(Element):
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


class L1000A_NM109(Element):
    """Submitter Identifier"""
    class Schema:
        json = {'title': 'Submitter Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000A_NM110(Element):
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


class L1000A_NM111(Element):
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


class L1000A_NM1(Segment):
    """Submitter Name"""
    class Schema:
        json = {'title': 'Submitter Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Submitter Name',
         'position': 20,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L1000A_NM101'},
                        'nm102': {'$ref': '#/$elements/L1000A_NM102'},
                        'nm103': {'$ref': '#/$elements/L1000A_NM103'},
                        'nm104': {'$ref': '#/$elements/L1000A_NM104'},
                        'nm105': {'$ref': '#/$elements/L1000A_NM105'},
                        'nm108': {'$ref': '#/$elements/L1000A_NM108'},
                        'nm109': {'$ref': '#/$elements/L1000A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L1000A_NM101
    nm102: L1000A_NM102
    nm103: L1000A_NM103
    nm104: L1000A_NM104 | None
    nm105: L1000A_NM105 | None
    nm108: L1000A_NM108
    nm109: L1000A_NM109


class L1000A_PER01(Element):
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


class L1000A_PER02(Element):
    """Submitter Contact Name"""
    class Schema:
        json = {'title': 'Submitter Contact Name',
         'usage': 'R',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000A_PER03(Element):
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


class L1000A_PER04(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000A_PER05(Element):
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


class L1000A_PER06(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000A_PER07(Element):
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


class L1000A_PER08(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000A_PER09(Element):
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


class L1000A_PER(Segment):
    """Submitter Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Submitter Contact Information',
                   'usage': 'R',
                   'description': 'xid=PER name=Submitter Contact Information',
                   'position': 45,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L1000A_PER01'},
                                  'per02': {'$ref': '#/$elements/L1000A_PER02'},
                                  'per03': {'$ref': '#/$elements/L1000A_PER03'},
                                  'per04': {'$ref': '#/$elements/L1000A_PER04'},
                                  'per05': {'$ref': '#/$elements/L1000A_PER05'},
                                  'per06': {'$ref': '#/$elements/L1000A_PER06'},
                                  'per07': {'$ref': '#/$elements/L1000A_PER07'},
                                  'per08': {'$ref': '#/$elements/L1000A_PER08'}},
                   'required': ['per01', 'per02', 'per03', 'per04']},
         'maxItems': 2}
        segment_name = 'PER'
    per01: L1000A_PER01
    per02: L1000A_PER02
    per03: L1000A_PER03
    per04: L1000A_PER04
    per05: L1000A_PER05 | None
    per06: L1000A_PER06 | None
    per07: L1000A_PER07 | None
    per08: L1000A_PER08 | None


class L1000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Submitter Name',
                   'usage': 'R',
                   'description': 'xid=1000A name=Submitter Name type=None',
                   'position': 20,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L1000A_NM1'},
                                  'per': {'$ref': '#/$segments/L1000A_PER'}},
                   'required': ['nm1', 'per']},
         'maxItems': 1}
    nm1: L1000A_NM1
    per: list[L1000A_PER]


class L1000B_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['40']}]}}
        datatype = common.D_98
        codes = ['40']
        min_len = 2
        max_len = 3


class L1000B_NM102(Element):
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


class L1000B_NM103(Element):
    """Receiver Name"""
    class Schema:
        json = {'title': 'Receiver Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L1000B_NM104(Element):
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


class L1000B_NM105(Element):
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


class L1000B_NM106(Element):
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


class L1000B_NM107(Element):
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


class L1000B_NM108(Element):
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


class L1000B_NM109(Element):
    """Receiver Primary Identifier"""
    class Schema:
        json = {'title': 'Receiver Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000B_NM110(Element):
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


class L1000B_NM111(Element):
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


class L1000B_NM1(Segment):
    """Receiver Name"""
    class Schema:
        json = {'title': 'Receiver Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Receiver Name',
         'position': 20,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L1000B_NM101'},
                        'nm102': {'$ref': '#/$elements/L1000B_NM102'},
                        'nm103': {'$ref': '#/$elements/L1000B_NM103'},
                        'nm108': {'$ref': '#/$elements/L1000B_NM108'},
                        'nm109': {'$ref': '#/$elements/L1000B_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L1000B_NM101
    nm102: L1000B_NM102
    nm103: L1000B_NM103
    nm108: L1000B_NM108
    nm109: L1000B_NM109


class L1000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Receiver Name',
                   'usage': 'R',
                   'description': 'xid=1000B name=Receiver Name type=None',
                   'position': 20,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L1000B_NM1'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L1000B_NM1


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 1 - Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Table 1 - Header type=wrapper',
                   'position': 10,
                   'type': 'object',
                   'properties': {'bht': {'$ref': '#/$segments/HEADER_BHT'},
                                  'ref': {'$ref': '#/$segments/HEADER_REF'},
                                  'l1000a': {'$ref': '#/$segments/L1000A'},
                                  'l1000b': {'$ref': '#/$segments/L1000B'}},
                   'required': ['bht', 'ref', 'l1000a', 'l1000b']},
         'maxItems': 1}
    bht: HEADER_BHT
    ref: HEADER_REF
    l1000a: list[L1000A]
    l1000b: list[L1000B]


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
    """Billing/Pay-To Provider Hierarchical Level"""
    class Schema:
        json = {'title': 'Billing/Pay-To Provider Hierarchical Level',
         'usage': 'R',
         'description': 'xid=HL name=Billing/Pay-To Provider Hierarchical Level',
         'position': 1,
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


class L2000A_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['BI', 'PT']}]}}
        datatype = common.D_1221
        codes = ['BI', 'PT']
        min_len = 1
        max_len = 3


class L2000A_PRV02(Element):
    """Referefence Identification Qualifier"""
    class Schema:
        json = {'title': 'Referefence Identification Qualifier',
         'usage': 'R',
         'description': 'xid=PRV02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['ZZ']}]}}
        datatype = common.D_128
        codes = ['ZZ']
        min_len = 2
        max_len = 3


class L2000A_PRV03(Element):
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


class L2000A_PRV04(Element):
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


class L2000A_PRV05(Element):
    """Provider Specialty Information"""
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=PRV05 data_ele=C035',
         'sequence': 5,
         'type': {'$ref': '#/$common/C035'}}
        datatype = common.C035


class L2000A_PRV06(Element):
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


class L2000A_PRV(Segment):
    """Billing/Pay-To Provider Specialty Information"""
    class Schema:
        json = {'title': 'Billing/Pay-To Provider Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Billing/Pay-To Provider Specialty Information',
         'position': 3,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2000A_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2000A_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2000A_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2000A_PRV01
    prv02: L2000A_PRV02
    prv03: L2000A_PRV03


class L2000A_CUR01(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=CUR01 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['85']}]}}
        datatype = common.D_98
        codes = ['85']
        min_len = 2
        max_len = 3


class L2000A_CUR02(Element):
    """Currency Code"""
    class Schema:
        json = {'title': 'Currency Code',
         'usage': 'R',
         'description': 'xid=CUR02 data_ele=100',
         'sequence': 2,
         'type': {'$ref': '#/$common/100'}}
        datatype = common.D_100
        codes = common.currency
        min_len = 3
        max_len = 3


class L2000A_CUR03(Element):
    """Exchange Rate"""
    class Schema:
        json = {'title': 'Exchange Rate',
         'usage': 'N',
         'description': 'xid=CUR03 data_ele=280',
         'sequence': 3,
         'type': {'$ref': '#/$common/280'}}
        datatype = common.D_280
        min_len = 4
        max_len = 10


class L2000A_CUR04(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=CUR04 data_ele=98',
         'sequence': 4,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2000A_CUR05(Element):
    """Currency Code"""
    class Schema:
        json = {'title': 'Currency Code',
         'usage': 'N',
         'description': 'xid=CUR05 data_ele=100',
         'sequence': 5,
         'type': {'$ref': '#/$common/100'}}
        datatype = common.D_100
        min_len = 3
        max_len = 3


class L2000A_CUR06(Element):
    """Currency Market/Exchange Code"""
    class Schema:
        json = {'title': 'Currency Market/Exchange Code',
         'usage': 'N',
         'description': 'xid=CUR06 data_ele=669',
         'sequence': 6,
         'type': {'$ref': '#/$common/669'}}
        datatype = common.D_669
        min_len = 3
        max_len = 3


class L2000A_CUR07(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'N',
         'description': 'xid=CUR07 data_ele=374',
         'sequence': 7,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class L2000A_CUR08(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CUR08 data_ele=373',
         'sequence': 8,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000A_CUR09(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=CUR09 data_ele=337',
         'sequence': 9,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2000A_CUR10(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'N',
         'description': 'xid=CUR10 data_ele=374',
         'sequence': 10,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class L2000A_CUR11(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CUR11 data_ele=373',
         'sequence': 11,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000A_CUR12(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=CUR12 data_ele=337',
         'sequence': 12,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2000A_CUR13(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'N',
         'description': 'xid=CUR13 data_ele=374',
         'sequence': 13,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class L2000A_CUR14(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CUR14 data_ele=373',
         'sequence': 14,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000A_CUR15(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=CUR15 data_ele=337',
         'sequence': 15,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2000A_CUR16(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'N',
         'description': 'xid=CUR16 data_ele=374',
         'sequence': 16,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class L2000A_CUR17(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CUR17 data_ele=373',
         'sequence': 17,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000A_CUR18(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=CUR18 data_ele=337',
         'sequence': 18,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2000A_CUR19(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'N',
         'description': 'xid=CUR19 data_ele=374',
         'sequence': 19,
         'type': {'$ref': '#/$common/374'}}
        datatype = common.D_374
        min_len = 3
        max_len = 3


class L2000A_CUR20(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'N',
         'description': 'xid=CUR20 data_ele=373',
         'sequence': 20,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000A_CUR21(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=CUR21 data_ele=337',
         'sequence': 21,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2000A_CUR(Segment):
    """Foreign Currency Information"""
    class Schema:
        json = {'title': 'Foreign Currency Information',
         'usage': 'S',
         'description': 'xid=CUR name=Foreign Currency Information',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'CUR'},
                        'cur01': {'$ref': '#/$elements/L2000A_CUR01'},
                        'cur02': {'$ref': '#/$elements/L2000A_CUR02'}},
         'required': ['cur01', 'cur02']}
        segment_name = 'CUR'
    cur01: L2000A_CUR01
    cur02: L2000A_CUR02


class L2010AA_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['85']}]}}
        datatype = common.D_98
        codes = ['85']
        min_len = 2
        max_len = 3


class L2010AA_NM102(Element):
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


class L2010AA_NM103(Element):
    """Billing Provider Last or Organizational Name"""
    class Schema:
        json = {'title': 'Billing Provider Last or Organizational Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010AA_NM104(Element):
    """Billing Provider First Name"""
    class Schema:
        json = {'title': 'Billing Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010AA_NM105(Element):
    """Billing Provider Middle Name"""
    class Schema:
        json = {'title': 'Billing Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010AA_NM106(Element):
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


class L2010AA_NM107(Element):
    """Billing Provider Name Suffix"""
    class Schema:
        json = {'title': 'Billing Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010AA_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2010AA_NM109(Element):
    """Billing Provider Identifier"""
    class Schema:
        json = {'title': 'Billing Provider Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010AA_NM110(Element):
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


class L2010AA_NM111(Element):
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


class L2010AA_NM1(Segment):
    """Billing Provider Name"""
    class Schema:
        json = {'title': 'Billing Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Billing Provider Name',
         'position': 15,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010AA_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010AA_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010AA_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010AA_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010AA_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010AA_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010AA_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010AA_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2010AA_NM101
    nm102: L2010AA_NM102
    nm103: L2010AA_NM103
    nm104: L2010AA_NM104 | None
    nm105: L2010AA_NM105 | None
    nm107: L2010AA_NM107 | None
    nm108: L2010AA_NM108
    nm109: L2010AA_NM109


class L2010AA_N301(Element):
    """Billing Provider Address 1"""
    class Schema:
        json = {'title': 'Billing Provider Address 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010AA_N302(Element):
    """Billing Provider Address 2"""
    class Schema:
        json = {'title': 'Billing Provider Address 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010AA_N3(Segment):
    """Billing Provider Address"""
    class Schema:
        json = {'title': 'Billing Provider Address',
         'usage': 'R',
         'description': 'xid=N3 name=Billing Provider Address',
         'position': 25,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010AA_N301'},
                        'n302': {'$ref': '#/$elements/L2010AA_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010AA_N301
    n302: L2010AA_N302 | None


class L2010AA_N401(Element):
    """Billing Provider City Name"""
    class Schema:
        json = {'title': 'Billing Provider City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010AA_N402(Element):
    """Billing Provider State or Province Code"""
    class Schema:
        json = {'title': 'Billing Provider State or Province Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010AA_N403(Element):
    """Billing Provider Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Billing Provider Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010AA_N404(Element):
    """Billing Provider Country Code"""
    class Schema:
        json = {'title': 'Billing Provider Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010AA_N405(Element):
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


class L2010AA_N406(Element):
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


class L2010AA_N4(Segment):
    """Billing Provider City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Billing Provider City/State/ZIP Code',
         'usage': 'R',
         'description': 'xid=N4 name=Billing Provider City/State/ZIP Code',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010AA_N401'},
                        'n402': {'$ref': '#/$elements/L2010AA_N402'},
                        'n403': {'$ref': '#/$elements/L2010AA_N403'},
                        'n404': {'$ref': '#/$elements/L2010AA_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2010AA_N401
    n402: L2010AA_N402
    n403: L2010AA_N403
    n404: L2010AA_N404 | None


class L2010AA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2010AA_REF02(Element):
    """Billing Provider Additional Identifier"""
    class Schema:
        json = {'title': 'Billing Provider Additional Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010AA_REF03(Element):
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


class L2010AA_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010AA_REF(Segment):
    """Billing Provider Secondary Identification Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Billing Provider Secondary Identification Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Billing Provider Secondary '
                                  'Identification Number',
                   'position': 35,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010AA_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010AA_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2010AA_REF01
    ref02: L2010AA_REF02


class L2010AA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['06', '8U', 'EM', 'IJ', 'LU', 'RB', 'ST',
                                      'TT']}]}}
        datatype = common.D_128
        codes = ['06', '8U', 'EM', 'IJ', 'LU', 'RB', 'ST', 'TT']
        min_len = 2
        max_len = 3


class L2010AA_REF02(Element):
    """Billing Provider Credit Card Identifier"""
    class Schema:
        json = {'title': 'Billing Provider Credit Card Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010AA_REF03(Element):
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


class L2010AA_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010AA_REF(Segment):
    """Claim Submitter Credit/Debit Card Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Submitter Credit/Debit Card Information',
                   'usage': 'S',
                   'description': 'xid=REF name=Claim Submitter Credit/Debit Card '
                                  'Information',
                   'position': 35,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010AA_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010AA_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 8}
        segment_name = 'REF'
    ref01: L2010AA_REF01
    ref02: L2010AA_REF02


class L2010AA(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Billing Provider Name',
                   'usage': 'R',
                   'description': 'xid=2010AA name=Billing Provider Name type=None',
                   'position': 15,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010AA_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010AA_N3'},
                                  'n4': {'$ref': '#/$segments/L2010AA_N4'},
                                  'ref': {'$ref': '#/$segments/L2010AA_REF'}},
                   'required': ['nm1', 'n3', 'n4']},
         'maxItems': 1}
    nm1: L2010AA_NM1
    n3: L2010AA_N3
    n4: L2010AA_N4
    ref: list[L2010AA_REF] | None
    ref: list[L2010AA_REF] | None


class L2010AB_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['87']}]}}
        datatype = common.D_98
        codes = ['87']
        min_len = 2
        max_len = 3


class L2010AB_NM102(Element):
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


class L2010AB_NM103(Element):
    """Pay-To Provider Last or Organizational Name"""
    class Schema:
        json = {'title': 'Pay-To Provider Last or Organizational Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010AB_NM104(Element):
    """Pay-To Provider First Name"""
    class Schema:
        json = {'title': 'Pay-To Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010AB_NM105(Element):
    """Pay-To Provider Middle Name"""
    class Schema:
        json = {'title': 'Pay-To Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010AB_NM106(Element):
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


class L2010AB_NM107(Element):
    """Pay-To Provider Name Suffix"""
    class Schema:
        json = {'title': 'Pay-To Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010AB_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2010AB_NM109(Element):
    """Pay-To Provider Identifier"""
    class Schema:
        json = {'title': 'Pay-To Provider Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010AB_NM110(Element):
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


class L2010AB_NM111(Element):
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


class L2010AB_NM1(Segment):
    """Pay-To Provider's Name"""
    class Schema:
        json = {'title': "Pay-To Provider's Name",
         'usage': 'R',
         'description': "xid=NM1 name=Pay-To Provider's Name",
         'position': 15,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010AB_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010AB_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010AB_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010AB_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010AB_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010AB_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010AB_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010AB_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2010AB_NM101
    nm102: L2010AB_NM102
    nm103: L2010AB_NM103
    nm104: L2010AB_NM104 | None
    nm105: L2010AB_NM105 | None
    nm107: L2010AB_NM107 | None
    nm108: L2010AB_NM108
    nm109: L2010AB_NM109


class L2010AB_N301(Element):
    """Pay-To Provider Address 1"""
    class Schema:
        json = {'title': 'Pay-To Provider Address 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010AB_N302(Element):
    """Pay-To Provider Address 2"""
    class Schema:
        json = {'title': 'Pay-To Provider Address 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010AB_N3(Segment):
    """Pay-To Provider's Address"""
    class Schema:
        json = {'title': "Pay-To Provider's Address",
         'usage': 'R',
         'description': "xid=N3 name=Pay-To Provider's Address",
         'position': 25,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010AB_N301'},
                        'n302': {'$ref': '#/$elements/L2010AB_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010AB_N301
    n302: L2010AB_N302 | None


class L2010AB_N401(Element):
    """Pay-To Provider City Name"""
    class Schema:
        json = {'title': 'Pay-To Provider City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010AB_N402(Element):
    """Pay-To Provider State Code"""
    class Schema:
        json = {'title': 'Pay-To Provider State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010AB_N403(Element):
    """Pay-To Provider Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Pay-To Provider Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010AB_N404(Element):
    """Pay-To Provider Country Code"""
    class Schema:
        json = {'title': 'Pay-To Provider Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010AB_N405(Element):
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


class L2010AB_N406(Element):
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


class L2010AB_N4(Segment):
    """Pay-To Provider City/State/ZIP"""
    class Schema:
        json = {'title': 'Pay-To Provider City/State/ZIP',
         'usage': 'R',
         'description': 'xid=N4 name=Pay-To Provider City/State/ZIP',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010AB_N401'},
                        'n402': {'$ref': '#/$elements/L2010AB_N402'},
                        'n403': {'$ref': '#/$elements/L2010AB_N403'},
                        'n404': {'$ref': '#/$elements/L2010AB_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2010AB_N401
    n402: L2010AB_N402
    n403: L2010AB_N403
    n404: L2010AB_N404 | None


class L2010AB_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2010AB_REF02(Element):
    """Pay-To Provider Identifier"""
    class Schema:
        json = {'title': 'Pay-To Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010AB_REF03(Element):
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


class L2010AB_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010AB_REF(Segment):
    """Pay-To Provider Secondary Identification Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Pay-To Provider Secondary Identification Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Pay-To Provider Secondary '
                                  'Identification Number',
                   'position': 35,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010AB_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010AB_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2010AB_REF01
    ref02: L2010AB_REF02


class L2010AB(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': "Pay-To Provider's Name",
                   'usage': 'S',
                   'description': "xid=2010AB name=Pay-To Provider's Name type=None",
                   'position': 15,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010AB_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010AB_N3'},
                                  'n4': {'$ref': '#/$segments/L2010AB_N4'},
                                  'ref': {'$ref': '#/$segments/L2010AB_REF'}},
                   'required': ['nm1', 'n3', 'n4']},
         'maxItems': 1}
    nm1: L2010AB_NM1
    n3: L2010AB_N3
    n4: L2010AB_N4
    ref: list[L2010AB_REF] | None


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
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['22']}]}}
        datatype = common.D_735
        codes = ['22']
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
    """Subscriber Hierarchical Level"""
    class Schema:
        json = {'title': 'Subscriber Hierarchical Level',
         'usage': 'R',
         'description': 'xid=HL name=Subscriber Hierarchical Level',
         'position': 1,
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


class L2000B_SBR01(Element):
    """Payer Responsibility Sequence Number Code"""
    class Schema:
        json = {'title': 'Payer Responsibility Sequence Number Code',
         'usage': 'R',
         'description': 'xid=SBR01 data_ele=1138',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1138'}, {'enum': ['P', 'S', 'T']}]}}
        datatype = common.D_1138
        codes = ['P', 'S', 'T']
        min_len = 1
        max_len = 1


class L2000B_SBR02(Element):
    """Individual Relationship Code"""
    class Schema:
        json = {'title': 'Individual Relationship Code',
         'usage': 'S',
         'description': 'xid=SBR02 data_ele=1069',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'}, {'enum': ['18']}]}}
        datatype = common.D_1069
        codes = ['18']
        min_len = 2
        max_len = 2


class L2000B_SBR03(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
         'usage': 'S',
         'description': 'xid=SBR03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000B_SBR04(Element):
    """Insured Group Name"""
    class Schema:
        json = {'title': 'Insured Group Name',
         'usage': 'S',
         'description': 'xid=SBR04 data_ele=93',
         'sequence': 4,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2000B_SBR05(Element):
    """Insurance Type Code"""
    class Schema:
        json = {'title': 'Insurance Type Code',
         'usage': 'N',
         'description': 'xid=SBR05 data_ele=1336',
         'sequence': 5,
         'type': {'$ref': '#/$common/1336'}}
        datatype = common.D_1336
        min_len = 1
        max_len = 3


class L2000B_SBR06(Element):
    """Coordination of Benefits Code"""
    class Schema:
        json = {'title': 'Coordination of Benefits Code',
         'usage': 'R',
         'description': 'xid=SBR06 data_ele=1143',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1143'}, {'enum': ['1', '6']}]}}
        datatype = common.D_1143
        codes = ['1', '6']
        min_len = 1
        max_len = 1


class L2000B_SBR07(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=SBR07 data_ele=1073',
         'sequence': 7,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2000B_SBR08(Element):
    """Employment Status Code"""
    class Schema:
        json = {'title': 'Employment Status Code',
         'usage': 'N',
         'description': 'xid=SBR08 data_ele=584',
         'sequence': 8,
         'type': {'$ref': '#/$common/584'}}
        datatype = common.D_584
        min_len = 2
        max_len = 2


class L2000B_SBR09(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'S',
         'description': 'xid=SBR09 data_ele=1032',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/1032'},
                            {'enum': ['09', '11', '12', '13', '14', '15', '16', '17',
                                      'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB',
                                      'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ']}]}}
        datatype = common.D_1032
        codes = ['09', '11', '12', '13', '14', '15', '16', '17', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB', 'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ']
        min_len = 1
        max_len = 2


class L2000B_SBR(Segment):
    """Subscriber Information"""
    class Schema:
        json = {'title': 'Subscriber Information',
         'usage': 'R',
         'description': 'xid=SBR name=Subscriber Information',
         'position': 5,
         'type': 'object',
         'properties': {'xid': {'literal': 'SBR'},
                        'sbr01': {'$ref': '#/$elements/L2000B_SBR01'},
                        'sbr02': {'$ref': '#/$elements/L2000B_SBR02'},
                        'sbr03': {'$ref': '#/$elements/L2000B_SBR03'},
                        'sbr04': {'$ref': '#/$elements/L2000B_SBR04'},
                        'sbr06': {'$ref': '#/$elements/L2000B_SBR06'},
                        'sbr09': {'$ref': '#/$elements/L2000B_SBR09'}},
         'required': ['sbr01', 'sbr06']}
        segment_name = 'SBR'
    sbr01: L2000B_SBR01
    sbr02: L2000B_SBR02 | None
    sbr03: L2000B_SBR03 | None
    sbr04: L2000B_SBR04 | None
    sbr06: L2000B_SBR06
    sbr09: L2000B_SBR09 | None


class L2010BA_NM101(Element):
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


class L2010BA_NM102(Element):
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


class L2010BA_NM103(Element):
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


class L2010BA_NM104(Element):
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


class L2010BA_NM105(Element):
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


class L2010BA_NM106(Element):
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


class L2010BA_NM107(Element):
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


class L2010BA_NM108(Element):
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


class L2010BA_NM109(Element):
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


class L2010BA_NM110(Element):
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


class L2010BA_NM111(Element):
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


class L2010BA_NM1(Segment):
    """Subscriber Name"""
    class Schema:
        json = {'title': 'Subscriber Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Subscriber Name',
         'position': 15,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010BA_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010BA_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010BA_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010BA_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010BA_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010BA_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010BA_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010BA_NM109'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2010BA_NM101
    nm102: L2010BA_NM102
    nm103: L2010BA_NM103
    nm104: L2010BA_NM104 | None
    nm105: L2010BA_NM105 | None
    nm107: L2010BA_NM107 | None
    nm108: L2010BA_NM108 | None
    nm109: L2010BA_NM109 | None


class L2010BA_N301(Element):
    """Subscriber Address 1"""
    class Schema:
        json = {'title': 'Subscriber Address 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010BA_N302(Element):
    """Subscriber Address 2"""
    class Schema:
        json = {'title': 'Subscriber Address 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010BA_N3(Segment):
    """Subscriber Address"""
    class Schema:
        json = {'title': 'Subscriber Address',
         'usage': 'S',
         'description': 'xid=N3 name=Subscriber Address',
         'position': 25,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010BA_N301'},
                        'n302': {'$ref': '#/$elements/L2010BA_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010BA_N301
    n302: L2010BA_N302 | None


class L2010BA_N401(Element):
    """Subscriber City Name"""
    class Schema:
        json = {'title': 'Subscriber City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010BA_N402(Element):
    """Subscriber State Code"""
    class Schema:
        json = {'title': 'Subscriber State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010BA_N403(Element):
    """Subscriber Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Subscriber Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010BA_N404(Element):
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


class L2010BA_N405(Element):
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


class L2010BA_N406(Element):
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


class L2010BA_N4(Segment):
    """Subscriber City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Subscriber City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Subscriber City/State/ZIP Code',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010BA_N401'},
                        'n402': {'$ref': '#/$elements/L2010BA_N402'},
                        'n403': {'$ref': '#/$elements/L2010BA_N403'},
                        'n404': {'$ref': '#/$elements/L2010BA_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2010BA_N401
    n402: L2010BA_N402
    n403: L2010BA_N403
    n404: L2010BA_N404 | None


class L2010BA_DMG01(Element):
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


class L2010BA_DMG02(Element):
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


class L2010BA_DMG03(Element):
    """Subscriber Gender Code"""
    class Schema:
        json = {'title': 'Subscriber Gender Code',
         'usage': 'R',
         'description': 'xid=DMG03 data_ele=1068',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2010BA_DMG04(Element):
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


class L2010BA_DMG05(Element):
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


class L2010BA_DMG06(Element):
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


class L2010BA_DMG07(Element):
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


class L2010BA_DMG08(Element):
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


class L2010BA_DMG09(Element):
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


class L2010BA_DMG(Segment):
    """Subscriber Demographic Information"""
    class Schema:
        json = {'title': 'Subscriber Demographic Information',
         'usage': 'S',
         'description': 'xid=DMG name=Subscriber Demographic Information',
         'position': 32,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2010BA_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2010BA_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2010BA_DMG03'}},
         'required': ['dmg01', 'dmg02', 'dmg03']}
        segment_name = 'DMG'
    dmg01: L2010BA_DMG01
    dmg02: L2010BA_DMG02
    dmg03: L2010BA_DMG03


class L2010BA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1W', '23', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1W', '23', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2010BA_REF02(Element):
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


class L2010BA_REF03(Element):
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


class L2010BA_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010BA_REF(Segment):
    """Subscriber Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Subscriber Secondary Identification',
                   'position': 35,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010BA_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010BA_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 4}
        segment_name = 'REF'
    ref01: L2010BA_REF01
    ref02: L2010BA_REF02


class L2010BA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['Y4']}]}}
        datatype = common.D_128
        codes = ['Y4']
        min_len = 2
        max_len = 3


class L2010BA_REF02(Element):
    """Property Casualty Claim Number"""
    class Schema:
        json = {'title': 'Property Casualty Claim Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010BA_REF03(Element):
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


class L2010BA_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010BA_REF(Segment):
    """Property and Casualty Claim Number"""
    class Schema:
        json = {'title': 'Property and Casualty Claim Number',
         'usage': 'S',
         'description': 'xid=REF name=Property and Casualty Claim Number',
         'position': 35,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2010BA_REF01'},
                        'ref02': {'$ref': '#/$elements/L2010BA_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2010BA_REF01
    ref02: L2010BA_REF02


class L2010BA(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Name',
                   'usage': 'R',
                   'description': 'xid=2010BA name=Subscriber Name type=None',
                   'position': 15,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010BA_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010BA_N3'},
                                  'n4': {'$ref': '#/$segments/L2010BA_N4'},
                                  'dmg': {'$ref': '#/$segments/L2010BA_DMG'},
                                  'ref': {'$ref': '#/$segments/L2010BA_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010BA_NM1
    n3: L2010BA_N3 | None
    n4: L2010BA_N4 | None
    dmg: L2010BA_DMG | None
    ref: list[L2010BA_REF] | None
    ref: L2010BA_REF | None


class L2010BB_NM101(Element):
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


class L2010BB_NM102(Element):
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


class L2010BB_NM103(Element):
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


class L2010BB_NM104(Element):
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


class L2010BB_NM105(Element):
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


class L2010BB_NM106(Element):
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


class L2010BB_NM107(Element):
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


class L2010BB_NM108(Element):
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


class L2010BB_NM109(Element):
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


class L2010BB_NM110(Element):
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


class L2010BB_NM111(Element):
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


class L2010BB_NM1(Segment):
    """Payer Name"""
    class Schema:
        json = {'title': 'Payer Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Payer Name',
         'position': 15,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010BB_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010BB_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010BB_NM103'},
                        'nm108': {'$ref': '#/$elements/L2010BB_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010BB_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2010BB_NM101
    nm102: L2010BB_NM102
    nm103: L2010BB_NM103
    nm108: L2010BB_NM108
    nm109: L2010BB_NM109


class L2010BB_N301(Element):
    """Payer Address 1"""
    class Schema:
        json = {'title': 'Payer Address 1',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010BB_N302(Element):
    """Payer Address 2"""
    class Schema:
        json = {'title': 'Payer Address 2',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010BB_N3(Segment):
    """Payer Address"""
    class Schema:
        json = {'title': 'Payer Address',
         'usage': 'S',
         'description': 'xid=N3 name=Payer Address',
         'position': 25,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010BB_N301'},
                        'n302': {'$ref': '#/$elements/L2010BB_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010BB_N301
    n302: L2010BB_N302 | None


class L2010BB_N401(Element):
    """Payer City Name"""
    class Schema:
        json = {'title': 'Payer City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010BB_N402(Element):
    """Payer State Code"""
    class Schema:
        json = {'title': 'Payer State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010BB_N403(Element):
    """Payer Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Payer Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010BB_N404(Element):
    """Payer Country Code"""
    class Schema:
        json = {'title': 'Payer Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010BB_N405(Element):
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


class L2010BB_N406(Element):
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


class L2010BB_N4(Segment):
    """Payer City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Payer City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Payer City/State/ZIP Code',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010BB_N401'},
                        'n402': {'$ref': '#/$elements/L2010BB_N402'},
                        'n403': {'$ref': '#/$elements/L2010BB_N403'},
                        'n404': {'$ref': '#/$elements/L2010BB_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2010BB_N401
    n402: L2010BB_N402
    n403: L2010BB_N403
    n404: L2010BB_N404 | None


class L2010BB_REF01(Element):
    """Payer Secondary Identification Number"""
    class Schema:
        json = {'title': 'Payer Secondary Identification Number',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['2U', 'FY', 'NF', 'TJ']}]}}
        datatype = common.D_128
        codes = ['2U', 'FY', 'NF', 'TJ']
        min_len = 2
        max_len = 3


class L2010BB_REF02(Element):
    """Payer Additional Identifier"""
    class Schema:
        json = {'title': 'Payer Additional Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010BB_REF03(Element):
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


class L2010BB_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010BB_REF(Segment):
    """Payer Secondary Identification Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer Secondary Identification Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Payer Secondary Identification Number',
                   'position': 35,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010BB_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010BB_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2010BB_REF01
    ref02: L2010BB_REF02


class L2010BB(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer Name',
                   'usage': 'R',
                   'description': 'xid=2010BB name=Payer Name type=None',
                   'position': 15,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010BB_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010BB_N3'},
                                  'n4': {'$ref': '#/$segments/L2010BB_N4'},
                                  'ref': {'$ref': '#/$segments/L2010BB_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010BB_NM1
    n3: L2010BB_N3 | None
    n4: L2010BB_N4 | None
    ref: list[L2010BB_REF] | None


class L2010BC_NM101(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['AO']}]}}
        datatype = common.D_98
        codes = ['AO']
        min_len = 2
        max_len = 3


class L2010BC_NM102(Element):
    """Loop Identifier Code"""
    class Schema:
        json = {'title': 'Loop Identifier Code',
         'usage': 'R',
         'description': 'xid=NM102 data_ele=1065',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1', '2']}]}}
        datatype = common.D_1065
        codes = ['1', '2']
        min_len = 1
        max_len = 1


class L2010BC_NM103(Element):
    """Credit or Debit Card Holder Last or Organizational Name"""
    class Schema:
        json = {'title': 'Credit or Debit Card Holder Last or Organizational Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2010BC_NM104(Element):
    """Entity Type Qualifier"""
    class Schema:
        json = {'title': 'Entity Type Qualifier',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010BC_NM105(Element):
    """Credit or Debit Card Holder Middle Name"""
    class Schema:
        json = {'title': 'Credit or Debit Card Holder Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2010BC_NM106(Element):
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


class L2010BC_NM107(Element):
    """Credit or Debit Card Holder Name Suffix"""
    class Schema:
        json = {'title': 'Credit or Debit Card Holder Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2010BC_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['MI']}]}}
        datatype = common.D_66
        codes = ['MI']
        min_len = 1
        max_len = 2


class L2010BC_NM109(Element):
    """Credit or Debit Card Number"""
    class Schema:
        json = {'title': 'Credit or Debit Card Number',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2010BC_NM110(Element):
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


class L2010BC_NM111(Element):
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


class L2010BC_NM1(Segment):
    """Credit/Debit Card Holder Name"""
    class Schema:
        json = {'title': 'Credit/Debit Card Holder Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Credit/Debit Card Holder Name',
         'position': 15,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2010BC_NM101'},
                        'nm102': {'$ref': '#/$elements/L2010BC_NM102'},
                        'nm103': {'$ref': '#/$elements/L2010BC_NM103'},
                        'nm104': {'$ref': '#/$elements/L2010BC_NM104'},
                        'nm105': {'$ref': '#/$elements/L2010BC_NM105'},
                        'nm107': {'$ref': '#/$elements/L2010BC_NM107'},
                        'nm108': {'$ref': '#/$elements/L2010BC_NM108'},
                        'nm109': {'$ref': '#/$elements/L2010BC_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2010BC_NM101
    nm102: L2010BC_NM102
    nm103: L2010BC_NM103
    nm104: L2010BC_NM104 | None
    nm105: L2010BC_NM105 | None
    nm107: L2010BC_NM107 | None
    nm108: L2010BC_NM108
    nm109: L2010BC_NM109


class L2010BC_REF01(Element):
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


class L2010BC_REF02(Element):
    """Credit or Debit Card Authorization Number"""
    class Schema:
        json = {'title': 'Credit or Debit Card Authorization Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2010BC_REF03(Element):
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


class L2010BC_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2010BC_REF(Segment):
    """Credit/Debit Card Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Credit/Debit Card Information',
                   'usage': 'S',
                   'description': 'xid=REF name=Credit/Debit Card Information',
                   'position': 35,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010BC_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010BC_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2010BC_REF01
    ref02: L2010BC_REF02


class L2010BC(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Credit/Debit Card Holder Name',
                   'usage': 'S',
                   'description': 'xid=2010BC name=Credit/Debit Card Holder Name '
                                  'type=None',
                   'position': 15,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010BC_NM1'},
                                  'ref': {'$ref': '#/$segments/L2010BC_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2010BC_NM1
    ref: list[L2010BC_REF] | None


class L2300_CLM01(Element):
    """Patient Account Number"""
    class Schema:
        json = {'title': 'Patient Account Number',
         'usage': 'R',
         'description': 'xid=CLM01 data_ele=1028',
         'sequence': 1,
         'type': {'$ref': '#/$common/1028'}}
        datatype = common.D_1028
        min_len = 1
        max_len = 38


class L2300_CLM02(Element):
    """Total Claim Charge Amount"""
    class Schema:
        json = {'title': 'Total Claim Charge Amount',
         'usage': 'R',
         'description': 'xid=CLM02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300_CLM03(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'N',
         'description': 'xid=CLM03 data_ele=1032',
         'sequence': 3,
         'type': {'$ref': '#/$common/1032'}}
        datatype = common.D_1032
        min_len = 1
        max_len = 2


class L2300_CLM04(Element):
    """Non-Institutional Claim Type Code"""
    class Schema:
        json = {'title': 'Non-Institutional Claim Type Code',
         'usage': 'N',
         'description': 'xid=CLM04 data_ele=1343',
         'sequence': 4,
         'type': {'$ref': '#/$common/1343'}}
        datatype = common.D_1343
        min_len = 1
        max_len = 2


class L2300_CLM05_01(Element):
    """Facility Type Code"""
    class Schema:
        json = {'title': 'Facility Type Code',
         'usage': 'R',
         'description': 'xid=CLM05-01 data_ele=1331',
         'sequence': 1,
         'type': {'$ref': '#/$common/1331'}}
        datatype = common.D_1331
        codes = common.pos
        min_len = 1
        max_len = 2


class L2300_CLM05_02(Element):
    """Facility Code Qualifier"""
    class Schema:
        json = {'title': 'Facility Code Qualifier',
         'usage': 'N',
         'description': 'xid=CLM05-02 data_ele=1332',
         'sequence': 2,
         'type': {'$ref': '#/$common/1332'}}
        datatype = common.D_1332
        min_len = 1
        max_len = 2


class L2300_CLM05_03(Element):
    """Claim Submission Reason Code"""
    class Schema:
        json = {'title': 'Claim Submission Reason Code',
         'usage': 'R',
         'description': 'xid=CLM05-03 data_ele=1325',
         'sequence': 3,
         'type': {'$ref': '#/$common/1325'}}
        datatype = common.D_1325
        min_len = 1
        max_len = 1


class L2300_C023(Composite):
    class Schema:
        json = {'title': 'Place of Service Code',
         'usage': 'R',
         'description': 'xid=None name=Place of Service Code refdes= data_ele=C023',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'clm05_01': {'title': 'Facility Type Code',
                                     'usage': 'R',
                                     'description': 'xid=CLM05-01 data_ele=1331',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1331'}},
                        'clm05_02': {'title': 'Facility Code Qualifier',
                                     'usage': 'N',
                                     'description': 'xid=CLM05-02 data_ele=1332',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1332'}},
                        'clm05_03': {'title': 'Claim Submission Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=CLM05-03 data_ele=1325',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1325'}}},
         'required': ['clm05_01', 'clm05_03']}
    clm05_01: L2300_CLM05_01
    clm05_03: L2300_CLM05_03


class L2300_CLM06(Element):
    """Provider or Supplier Signature Indicator"""
    class Schema:
        json = {'title': 'Provider or Supplier Signature Indicator',
         'usage': 'R',
         'description': 'xid=CLM06 data_ele=1073',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2300_CLM07(Element):
    """Medicare Assignment Code"""
    class Schema:
        json = {'title': 'Medicare Assignment Code',
         'usage': 'S',
         'description': 'xid=CLM07 data_ele=1359',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/1359'}, {'enum': ['A', 'C', 'P']}]}}
        datatype = common.D_1359
        codes = ['A', 'C', 'P']
        min_len = 1
        max_len = 1


class L2300_CLM08(Element):
    """Benefits Assignment Certification Indicator"""
    class Schema:
        json = {'title': 'Benefits Assignment Certification Indicator',
         'usage': 'R',
         'description': 'xid=CLM08 data_ele=1073',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2300_CLM09(Element):
    """Release of Information Code"""
    class Schema:
        json = {'title': 'Release of Information Code',
         'usage': 'R',
         'description': 'xid=CLM09 data_ele=1363',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/1363'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1363
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2300_CLM10(Element):
    """Patient Signature Source Code"""
    class Schema:
        json = {'title': 'Patient Signature Source Code',
         'usage': 'N',
         'description': 'xid=CLM10 data_ele=1351',
         'sequence': 10,
         'type': {'$ref': '#/$common/1351'}}
        datatype = common.D_1351
        min_len = 1
        max_len = 1


class L2300_CLM11_01(Element):
    """Related Causes Code"""
    class Schema:
        json = {'title': 'Related Causes Code',
         'usage': 'R',
         'description': 'xid=CLM11-01 data_ele=1362',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1362'}, {'enum': ['AA', 'EM', 'OA']}]}}
        datatype = common.D_1362
        codes = ['AA', 'EM', 'OA']
        min_len = 2
        max_len = 3


class L2300_CLM11_02(Element):
    """Related Causes Code"""
    class Schema:
        json = {'title': 'Related Causes Code',
         'usage': 'S',
         'description': 'xid=CLM11-02 data_ele=1362',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1362'}, {'enum': ['AA', 'EM', 'OA']}]}}
        datatype = common.D_1362
        codes = ['AA', 'EM', 'OA']
        min_len = 2
        max_len = 3


class L2300_CLM11_03(Element):
    """Related Causes Code"""
    class Schema:
        json = {'title': 'Related Causes Code',
         'usage': 'S',
         'description': 'xid=CLM11-03 data_ele=1362',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1362'}, {'enum': ['AA', 'EM', 'OA']}]}}
        datatype = common.D_1362
        codes = ['AA', 'EM', 'OA']
        min_len = 2
        max_len = 3


class L2300_CLM11_04(Element):
    """Auto Accident State or Province Code"""
    class Schema:
        json = {'title': 'Auto Accident State or Province Code',
         'usage': 'S',
         'description': 'xid=CLM11-04 data_ele=156',
         'sequence': 4,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2300_CLM11_05(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'S',
         'description': 'xid=CLM11-05 data_ele=26',
         'sequence': 5,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2300_C024(Composite):
    class Schema:
        json = {'title': 'Related Causes Information',
         'usage': 'S',
         'description': 'xid=None name=Related Causes Information refdes= '
                        'data_ele=C024',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'clm11_01': {'title': 'Related Causes Code',
                                     'usage': 'R',
                                     'description': 'xid=CLM11-01 data_ele=1362',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1362'},
                                                        {'enum': ['AA', 'EM', 'OA']}]}},
                        'clm11_02': {'title': 'Related Causes Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-02 data_ele=1362',
                                     'sequence': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1362'},
                                                        {'enum': ['AA', 'EM', 'OA']}]}},
                        'clm11_03': {'title': 'Related Causes Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-03 data_ele=1362',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/1362'},
                                                        {'enum': ['AA', 'EM', 'OA']}]}},
                        'clm11_04': {'title': 'Auto Accident State or Province Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-04 data_ele=156',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/156'}},
                        'clm11_05': {'title': 'Country Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-05 data_ele=26',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/26'}}},
         'required': ['clm11_01']}
    clm11_01: L2300_CLM11_01
    clm11_02: L2300_CLM11_02 | None
    clm11_03: L2300_CLM11_03 | None
    clm11_04: L2300_CLM11_04 | None
    clm11_05: L2300_CLM11_05 | None


class L2300_CLM12(Element):
    """Special Program Indicator"""
    class Schema:
        json = {'title': 'Special Program Indicator',
         'usage': 'S',
         'description': 'xid=CLM12 data_ele=1366',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/1366'},
                            {'enum': ['01', '02', '03', '05']}]}}
        datatype = common.D_1366
        codes = ['01', '02', '03', '05']
        min_len = 2
        max_len = 3


class L2300_CLM13(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CLM13 data_ele=1073',
         'sequence': 13,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_CLM14(Element):
    """Level of Service Code"""
    class Schema:
        json = {'title': 'Level of Service Code',
         'usage': 'N',
         'description': 'xid=CLM14 data_ele=1338',
         'sequence': 14,
         'type': {'$ref': '#/$common/1338'}}
        datatype = common.D_1338
        min_len = 1
        max_len = 3


class L2300_CLM15(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CLM15 data_ele=1073',
         'sequence': 15,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_CLM16(Element):
    """Provider Agreement Code"""
    class Schema:
        json = {'title': 'Provider Agreement Code',
         'usage': 'N',
         'description': 'xid=CLM16 data_ele=1360',
         'sequence': 16,
         'type': {'$ref': '#/$common/1360'}}
        datatype = common.D_1360
        min_len = 1
        max_len = 1


class L2300_CLM17(Element):
    """Claim Status Code"""
    class Schema:
        json = {'title': 'Claim Status Code',
         'usage': 'N',
         'description': 'xid=CLM17 data_ele=1029',
         'sequence': 17,
         'type': {'$ref': '#/$common/1029'}}
        datatype = common.D_1029
        min_len = 1
        max_len = 2


class L2300_CLM18(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CLM18 data_ele=1073',
         'sequence': 18,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_CLM19(Element):
    """Predetermination of Benefits Code"""
    class Schema:
        json = {'title': 'Predetermination of Benefits Code',
         'usage': 'S',
         'description': 'xid=CLM19 data_ele=1383',
         'sequence': 19,
         'type': {'allOf': [{'$ref': '#/$common/1383'}, {'enum': ['PB']}]}}
        datatype = common.D_1383
        codes = ['PB']
        min_len = 2
        max_len = 2


class L2300_CLM20(Element):
    """Delay Reason Code"""
    class Schema:
        json = {'title': 'Delay Reason Code',
         'usage': 'S',
         'description': 'xid=CLM20 data_ele=1514',
         'sequence': 20,
         'type': {'allOf': [{'$ref': '#/$common/1514'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11']}]}}
        datatype = common.D_1514
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        min_len = 1
        max_len = 2


class L2300_CLM(Segment):
    """Claim Information"""
    class Schema:
        json = {'title': 'Claim Information',
         'usage': 'R',
         'description': 'xid=CLM name=Claim Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'CLM'},
                        'clm01': {'$ref': '#/$elements/L2300_CLM01'},
                        'clm02': {'$ref': '#/$elements/L2300_CLM02'},
                        'c023': {'$ref': '#/$elements/L2300_C023'},
                        'clm06': {'$ref': '#/$elements/L2300_CLM06'},
                        'clm07': {'$ref': '#/$elements/L2300_CLM07'},
                        'clm08': {'$ref': '#/$elements/L2300_CLM08'},
                        'clm09': {'$ref': '#/$elements/L2300_CLM09'},
                        'c024': {'$ref': '#/$elements/L2300_C024'},
                        'clm12': {'$ref': '#/$elements/L2300_CLM12'},
                        'clm19': {'$ref': '#/$elements/L2300_CLM19'},
                        'clm20': {'$ref': '#/$elements/L2300_CLM20'}},
         'required': ['clm01', 'clm02', 'c023', 'clm06', 'clm08', 'clm09']}
        segment_name = 'CLM'
    clm01: L2300_CLM01
    clm02: L2300_CLM02
    c023: L2300_C023
    clm06: L2300_CLM06
    clm07: L2300_CLM07 | None
    clm08: L2300_CLM08
    clm09: L2300_CLM09
    c024: L2300_C024 | None
    clm12: L2300_CLM12 | None
    clm19: L2300_CLM19 | None
    clm20: L2300_CLM20 | None


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Related Hospitalization Admission Date"""
    class Schema:
        json = {'title': 'Related Hospitalization Admission Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Admission"""
    class Schema:
        json = {'title': 'Date - Admission',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Admission',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Discharge or End Of Care Date"""
    class Schema:
        json = {'title': 'Discharge or End Of Care Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Discharge"""
    class Schema:
        json = {'title': 'Date - Discharge',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Discharge',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['330']}]}}
        datatype = common.D_374
        codes = ['330']
        min_len = 3
        max_len = 3


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Referral Date"""
    class Schema:
        json = {'title': 'Referral Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Referral"""
    class Schema:
        json = {'title': 'Date - Referral',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Referral',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
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


class L2300_DTP(Segment):
    """Date - Accident"""
    class Schema:
        json = {'title': 'Date - Accident',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Accident',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['452']}]}}
        datatype = common.D_374
        codes = ['452']
        min_len = 3
        max_len = 3


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Orthodontic Banding Date"""
    class Schema:
        json = {'title': 'Orthodontic Banding Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Appliance Placement"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Date - Appliance Placement',
                   'usage': 'S',
                   'description': 'xid=DTP name=Date - Appliance Placement',
                   'position': 135,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 5}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Service Date"""
    class Schema:
        json = {'title': 'Service Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Service"""
    class Schema:
        json = {'title': 'Date - Service',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Service',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DN101(Element):
    """Orthodontic Treatment Months Count"""
    class Schema:
        json = {'title': 'Orthodontic Treatment Months Count',
         'usage': 'S',
         'description': 'xid=DN101 data_ele=380',
         'sequence': 1,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_DN102(Element):
    """Orthodontic Treatment Months Remaining Count"""
    class Schema:
        json = {'title': 'Orthodontic Treatment Months Remaining Count',
         'usage': 'S',
         'description': 'xid=DN102 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_DN103(Element):
    """Question Response"""
    class Schema:
        json = {'title': 'Question Response',
         'usage': 'S',
         'description': 'xid=DN103 data_ele=1073',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['Y']}]}}
        datatype = common.D_1073
        codes = ['Y']
        min_len = 1
        max_len = 1


class L2300_DN104(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=DN104 data_ele=352',
         'sequence': 4,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_DN1(Segment):
    """Orthodontic Total Months of Treatment"""
    class Schema:
        json = {'title': 'Orthodontic Total Months of Treatment',
         'usage': 'S',
         'description': 'xid=DN1 name=Orthodontic Total Months of Treatment',
         'position': 145,
         'type': 'object',
         'properties': {'xid': {'literal': 'DN1'},
                        'dn101': {'$ref': '#/$elements/L2300_DN101'},
                        'dn102': {'$ref': '#/$elements/L2300_DN102'},
                        'dn103': {'$ref': '#/$elements/L2300_DN103'}}}
        segment_name = 'DN1'
    dn101: L2300_DN101 | None
    dn102: L2300_DN102 | None
    dn103: L2300_DN103 | None


class L2300_DN201(Element):
    """Tooth Number"""
    class Schema:
        json = {'title': 'Tooth Number',
         'usage': 'R',
         'description': 'xid=DN201 data_ele=127',
         'sequence': 1,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_DN202(Element):
    """Tooth Status Code"""
    class Schema:
        json = {'title': 'Tooth Status Code',
         'usage': 'R',
         'description': 'xid=DN202 data_ele=1368',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1368'}, {'enum': ['E', 'I', 'M']}]}}
        datatype = common.D_1368
        codes = ['E', 'I', 'M']
        min_len = 1
        max_len = 2


class L2300_DN203(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=DN203 data_ele=380',
         'sequence': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_DN204(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=DN204 data_ele=1250',
         'sequence': 4,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2300_DN205(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=DN205 data_ele=1251',
         'sequence': 5,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DN2(Segment):
    """Tooth Status"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Tooth Status',
                   'usage': 'S',
                   'description': 'xid=DN2 name=Tooth Status',
                   'position': 150,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DN2'},
                                  'dn201': {'$ref': '#/$elements/L2300_DN201'},
                                  'dn202': {'$ref': '#/$elements/L2300_DN202'}},
                   'required': ['dn201', 'dn202']},
         'maxItems': 35}
        segment_name = 'DN2'
    dn201: L2300_DN201
    dn202: L2300_DN202


class L2300_PWK01(Element):
    """Attachment Report Type Code"""
    class Schema:
        json = {'title': 'Attachment Report Type Code',
         'usage': 'R',
         'description': 'xid=PWK01 data_ele=755',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/755'},
                            {'enum': ['B4', 'DA', 'DG', 'EB', 'OB', 'OZ', 'P6', 'RB',
                                      'RR']}]}}
        datatype = common.D_755
        codes = ['B4', 'DA', 'DG', 'EB', 'OB', 'OZ', 'P6', 'RB', 'RR']
        min_len = 2
        max_len = 2


class L2300_PWK02(Element):
    """Attachment Transmission Code"""
    class Schema:
        json = {'title': 'Attachment Transmission Code',
         'usage': 'R',
         'description': 'xid=PWK02 data_ele=756',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/756'},
                            {'enum': ['AA', 'BM', 'EL', 'EM', 'FX']}]}}
        datatype = common.D_756
        codes = ['AA', 'BM', 'EL', 'EM', 'FX']
        min_len = 1
        max_len = 2


class L2300_PWK03(Element):
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


class L2300_PWK04(Element):
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


class L2300_PWK05(Element):
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


class L2300_PWK06(Element):
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


class L2300_PWK07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=PWK07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_C002(Composite):
    class Schema:
        json = {'title': 'Actions Indicated',
         'usage': 'N',
         'description': 'xid=None name=Actions Indicated refdes= data_ele=C002',
         'sequence': 8,
         'syntax': []}


class L2300_PWK09(Element):
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


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Supplemental Information',
                   'usage': 'S',
                   'description': 'xid=PWK name=Claim Supplemental Information',
                   'position': 155,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PWK'},
                                  'pwk01': {'$ref': '#/$elements/L2300_PWK01'},
                                  'pwk02': {'$ref': '#/$elements/L2300_PWK02'},
                                  'pwk05': {'$ref': '#/$elements/L2300_PWK05'},
                                  'pwk06': {'$ref': '#/$elements/L2300_PWK06'}},
                   'required': ['pwk01', 'pwk02']},
         'maxItems': 10}
        segment_name = 'PWK'
    pwk01: L2300_PWK01
    pwk02: L2300_PWK02
    pwk05: L2300_PWK05 | None
    pwk06: L2300_PWK06 | None


class L2300_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['F5']}]}}
        datatype = common.D_522
        codes = ['F5']
        min_len = 1
        max_len = 3


class L2300_AMT02(Element):
    """Patient Amount Paid"""
    class Schema:
        json = {'title': 'Patient Amount Paid',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300_AMT03(Element):
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


class L2300_AMT(Segment):
    """Patient Amount Paid"""
    class Schema:
        json = {'title': 'Patient Amount Paid',
         'usage': 'S',
         'description': 'xid=AMT name=Patient Amount Paid',
         'position': 175,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2300_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2300_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2300_AMT01
    amt02: L2300_AMT02


class L2300_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['MA']}]}}
        datatype = common.D_522
        codes = ['MA']
        min_len = 1
        max_len = 3


class L2300_AMT02(Element):
    """Credit or Debit Card Maximum Amount"""
    class Schema:
        json = {'title': 'Credit or Debit Card Maximum Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300_AMT03(Element):
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


class L2300_AMT(Segment):
    """Credit/Debit Card - Maximum Amount"""
    class Schema:
        json = {'title': 'Credit/Debit Card - Maximum Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Credit/Debit Card - Maximum Amount',
         'position': 175,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2300_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2300_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2300_AMT01
    amt02: L2300_AMT02


class L2300_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['G3']}]}}
        datatype = common.D_128
        codes = ['G3']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """Predetermination of Benefits Identifier"""
    class Schema:
        json = {'title': 'Predetermination of Benefits Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Predetermination Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Predetermination Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Predetermination Identification',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['4N']}]}}
        datatype = common.D_128
        codes = ['4N']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """Service Authorization Exception Code"""
    class Schema:
        json = {'title': 'Service Authorization Exception Code',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/127'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7']}]}}
        datatype = common.D_127
        codes = ['1', '2', '3', '4', '5', '6', '7']
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Service Authorization Exception Code"""
    class Schema:
        json = {'title': 'Service Authorization Exception Code',
         'usage': 'S',
         'description': 'xid=REF name=Service Authorization Exception Code',
         'position': 180,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2300_REF01'},
                        'ref02': {'$ref': '#/$elements/L2300_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['F8']}]}}
        datatype = common.D_128
        codes = ['F8']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """Claim Original Reference Number"""
    class Schema:
        json = {'title': 'Claim Original Reference Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Original Reference Number (ICN/DCN)"""
    class Schema:
        json = {'title': 'Original Reference Number (ICN/DCN)',
         'usage': 'S',
         'description': 'xid=REF name=Original Reference Number (ICN/DCN)',
         'position': 180,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2300_REF01'},
                        'ref02': {'$ref': '#/$elements/L2300_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
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


class L2300_REF02(Element):
    """Referral Number"""
    class Schema:
        json = {'title': 'Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Prior Authorization or Referral Number',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
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


class L2300_REF02(Element):
    """Value Added Network Trace Number"""
    class Schema:
        json = {'title': 'Value Added Network Trace Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Claim Identification Number for Clearinghouses and Other Transmission Intermediaries"""
    class Schema:
        json = {'title': 'Claim Identification Number for Clearinghouses and Other '
                  'Transmission Intermediaries',
         'usage': 'S',
         'description': 'xid=REF name=Claim Identification Number for Clearinghouses '
                        'and Other Transmission Intermediaries',
         'position': 180,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2300_REF01'},
                        'ref02': {'$ref': '#/$elements/L2300_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_NTE01(Element):
    """Note Reference Code"""
    class Schema:
        json = {'title': 'Note Reference Code',
         'usage': 'R',
         'description': 'xid=NTE01 data_ele=363',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/363'}, {'enum': ['ADD']}]}}
        datatype = common.D_363
        codes = ['ADD']
        min_len = 3
        max_len = 3


class L2300_NTE02(Element):
    """Claim Note Text"""
    class Schema:
        json = {'title': 'Claim Note Text',
         'usage': 'R',
         'description': 'xid=NTE02 data_ele=352',
         'sequence': 2,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_NTE(Segment):
    """Claim Note"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Note',
                   'usage': 'S',
                   'description': 'xid=NTE name=Claim Note',
                   'position': 190,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'NTE'},
                                  'nte01': {'$ref': '#/$elements/L2300_NTE01'},
                                  'nte02': {'$ref': '#/$elements/L2300_NTE02'}},
                   'required': ['nte01', 'nte02']},
         'maxItems': 20}
        segment_name = 'NTE'
    nte01: L2300_NTE01
    nte02: L2300_NTE02


class L2310A_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DN', 'P3']}]}}
        datatype = common.D_98
        codes = ['DN', 'P3']
        min_len = 2
        max_len = 3


class L2310A_NM102(Element):
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


class L2310A_NM103(Element):
    """Referring Provider Last Name"""
    class Schema:
        json = {'title': 'Referring Provider Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310A_NM104(Element):
    """Referring Provider First Name"""
    class Schema:
        json = {'title': 'Referring Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2310A_NM105(Element):
    """Referring Provider Middle Name"""
    class Schema:
        json = {'title': 'Referring Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2310A_NM106(Element):
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


class L2310A_NM107(Element):
    """Referring Provider Name Suffix"""
    class Schema:
        json = {'title': 'Referring Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2310A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310A_NM109(Element):
    """Referring Provider Identifier"""
    class Schema:
        json = {'title': 'Referring Provider Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310A_NM110(Element):
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


class L2310A_NM111(Element):
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


class L2310A_NM1(Segment):
    """Referring Provider Name"""
    class Schema:
        json = {'title': 'Referring Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Referring Provider Name',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2310A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2310A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2310A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2310A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2310A_NM101
    nm102: L2310A_NM102
    nm103: L2310A_NM103
    nm104: L2310A_NM104 | None
    nm105: L2310A_NM105 | None
    nm107: L2310A_NM107 | None
    nm108: L2310A_NM108 | None
    nm109: L2310A_NM109 | None


class L2310A_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['RF']}]}}
        datatype = common.D_1221
        codes = ['RF']
        min_len = 1
        max_len = 3


class L2310A_PRV02(Element):
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


class L2310A_PRV03(Element):
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


class L2310A_PRV04(Element):
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


class L2310A_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2310A_PRV06(Element):
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


class L2310A_PRV(Segment):
    """Referring Provider Specialty Information"""
    class Schema:
        json = {'title': 'Referring Provider Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Referring Provider Specialty Information',
         'position': 255,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2310A_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2310A_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2310A_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2310A_PRV01
    prv02: L2310A_PRV02
    prv03: L2310A_PRV03


class L2310A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2310A_REF02(Element):
    """Referring Provider Secondary Identifier"""
    class Schema:
        json = {'title': 'Referring Provider Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310A_REF03(Element):
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


class L2310A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310A_REF(Segment):
    """Referring Provider Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Referring Provider Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Referring Provider Secondary '
                                  'Identification',
                   'position': 271,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2310A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2310A_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2310A_REF01
    ref02: L2310A_REF02


class L2310A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Referring Provider Name',
                   'usage': 'S',
                   'description': 'xid=2310A name=Referring Provider Name type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310A_NM1'},
                                  'prv': {'$ref': '#/$segments/L2310A_PRV'},
                                  'ref': {'$ref': '#/$segments/L2310A_REF'}},
                   'required': ['nm1']},
         'maxItems': 2}
    nm1: L2310A_NM1
    prv: L2310A_PRV | None
    ref: list[L2310A_REF] | None


class L2310B_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['82']}]}}
        datatype = common.D_98
        codes = ['82']
        min_len = 2
        max_len = 3


class L2310B_NM102(Element):
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


class L2310B_NM103(Element):
    """Rendering Provider Last or Organization Name"""
    class Schema:
        json = {'title': 'Rendering Provider Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310B_NM104(Element):
    """Rendering Provider First Name"""
    class Schema:
        json = {'title': 'Rendering Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2310B_NM105(Element):
    """Rendering Provider Middle Name"""
    class Schema:
        json = {'title': 'Rendering Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2310B_NM106(Element):
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


class L2310B_NM107(Element):
    """Rendering Provider Name Suffix"""
    class Schema:
        json = {'title': 'Rendering Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2310B_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310B_NM109(Element):
    """Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310B_NM110(Element):
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


class L2310B_NM111(Element):
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


class L2310B_NM1(Segment):
    """Rendering Provider Name"""
    class Schema:
        json = {'title': 'Rendering Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Rendering Provider Name',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310B_NM103'},
                        'nm104': {'$ref': '#/$elements/L2310B_NM104'},
                        'nm105': {'$ref': '#/$elements/L2310B_NM105'},
                        'nm107': {'$ref': '#/$elements/L2310B_NM107'},
                        'nm108': {'$ref': '#/$elements/L2310B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310B_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2310B_NM101
    nm102: L2310B_NM102
    nm103: L2310B_NM103
    nm104: L2310B_NM104 | None
    nm105: L2310B_NM105 | None
    nm107: L2310B_NM107 | None
    nm108: L2310B_NM108
    nm109: L2310B_NM109


class L2310B_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['PE']}]}}
        datatype = common.D_1221
        codes = ['PE']
        min_len = 1
        max_len = 3


class L2310B_PRV02(Element):
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


class L2310B_PRV03(Element):
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


class L2310B_PRV04(Element):
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


class L2310B_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2310B_PRV06(Element):
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


class L2310B_PRV(Segment):
    """Rendering Provider Specialty Information"""
    class Schema:
        json = {'title': 'Rendering Provider Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Rendering Provider Specialty Information',
         'position': 255,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2310B_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2310B_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2310B_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2310B_PRV01
    prv02: L2310B_PRV02
    prv03: L2310B_PRV03


class L2310B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2310B_REF02(Element):
    """Rendering Provider Secondary Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310B_REF03(Element):
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


class L2310B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310B_REF(Segment):
    """Rendering Provider Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Secondary '
                                  'Identification',
                   'position': 271,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2310B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2310B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2310B_REF01
    ref02: L2310B_REF02


class L2310B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Name',
                   'usage': 'S',
                   'description': 'xid=2310B name=Rendering Provider Name type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310B_NM1'},
                                  'prv': {'$ref': '#/$segments/L2310B_PRV'},
                                  'ref': {'$ref': '#/$segments/L2310B_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2310B_NM1
    prv: L2310B_PRV | None
    ref: list[L2310B_REF] | None


class L2310C_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['FA']}]}}
        datatype = common.D_98
        codes = ['FA']
        min_len = 2
        max_len = 3


class L2310C_NM102(Element):
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


class L2310C_NM103(Element):
    """Laboratory or Facility Name"""
    class Schema:
        json = {'title': 'Laboratory or Facility Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310C_NM104(Element):
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


class L2310C_NM105(Element):
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


class L2310C_NM106(Element):
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


class L2310C_NM107(Element):
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


class L2310C_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310C_NM109(Element):
    """Laboratory or Facility Primary Identifier"""
    class Schema:
        json = {'title': 'Laboratory or Facility Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310C_NM110(Element):
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


class L2310C_NM111(Element):
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


class L2310C_NM1(Segment):
    """Service Facility Location"""
    class Schema:
        json = {'title': 'Service Facility Location',
         'usage': 'R',
         'description': 'xid=NM1 name=Service Facility Location',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310C_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310C_NM103'},
                        'nm108': {'$ref': '#/$elements/L2310C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310C_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2310C_NM101
    nm102: L2310C_NM102
    nm103: L2310C_NM103
    nm108: L2310C_NM108
    nm109: L2310C_NM109


class L2310C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'G2',
                                      'LU', 'TJ', 'X4', 'X5']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5']
        min_len = 2
        max_len = 3


class L2310C_REF02(Element):
    """Laboratory or Facility Secondary Identifier"""
    class Schema:
        json = {'title': 'Laboratory or Facility Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310C_REF03(Element):
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


class L2310C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Facility Location Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Service Facility Location Secondary '
                                  'Identification',
                   'position': 271,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2310C_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2310C_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2310C_REF01
    ref02: L2310C_REF02


class L2310C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Facility Location',
                   'usage': 'S',
                   'description': 'xid=2310C name=Service Facility Location type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310C_NM1'},
                                  'ref': {'$ref': '#/$segments/L2310C_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2310C_NM1
    ref: list[L2310C_REF] | None


class L2310D_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DD']}]}}
        datatype = common.D_98
        codes = ['DD']
        min_len = 2
        max_len = 3


class L2310D_NM102(Element):
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


class L2310D_NM103(Element):
    """Assistant Last or Organazation Name"""
    class Schema:
        json = {'title': 'Assistant Last or Organazation Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310D_NM104(Element):
    """Assistant Surgeon First Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2310D_NM105(Element):
    """Assistant Surgeon Middle Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2310D_NM106(Element):
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


class L2310D_NM107(Element):
    """Assistant Surgeon Name Suffix"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2310D_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310D_NM109(Element):
    """Assistant Surgeon Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310D_NM110(Element):
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


class L2310D_NM111(Element):
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


class L2310D_NM1(Segment):
    """Assistant Surgeon Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Assistant Surgeon Name',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310D_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310D_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310D_NM103'},
                        'nm104': {'$ref': '#/$elements/L2310D_NM104'},
                        'nm105': {'$ref': '#/$elements/L2310D_NM105'},
                        'nm107': {'$ref': '#/$elements/L2310D_NM107'},
                        'nm108': {'$ref': '#/$elements/L2310D_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310D_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2310D_NM101
    nm102: L2310D_NM102
    nm103: L2310D_NM103
    nm104: L2310D_NM104 | None
    nm105: L2310D_NM105 | None
    nm107: L2310D_NM107 | None
    nm108: L2310D_NM108
    nm109: L2310D_NM109


class L2310D_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['AS']}]}}
        datatype = common.D_1221
        codes = ['AS']
        min_len = 1
        max_len = 3


class L2310D_PRV02(Element):
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


class L2310D_PRV03(Element):
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


class L2310D_PRV04(Element):
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


class L2310D_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2310D_PRV06(Element):
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


class L2310D_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    class Schema:
        json = {'title': 'Assistant Surgeon Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Assistant Surgeon Specialty Information',
         'position': 255,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2310D_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2310D_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2310D_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2310D_PRV01
    prv02: L2310D_PRV02
    prv03: L2310D_PRV03


class L2310D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2310D_REF02(Element):
    """Assistant Surgeon Secondary Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310D_REF03(Element):
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


class L2310D_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310D_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identification',
         'usage': 'S',
         'description': 'xid=REF name=Assistant Surgeon Secondary Identification',
         'position': 271,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2310D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2310D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2310D_REF01
    ref02: L2310D_REF02


class L2310D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Assistant Surgeon Name',
                   'usage': 'S',
                   'description': 'xid=2310D name=Assistant Surgeon Name type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310D_NM1'},
                                  'prv': {'$ref': '#/$segments/L2310D_PRV'},
                                  'ref': {'$ref': '#/$segments/L2310D_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2310D_NM1
    prv: L2310D_PRV | None
    ref: L2310D_REF | None


class L2320_SBR01(Element):
    """Payer Responsibility Sequence Number Code"""
    class Schema:
        json = {'title': 'Payer Responsibility Sequence Number Code',
         'usage': 'R',
         'description': 'xid=SBR01 data_ele=1138',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1138'}, {'enum': ['P', 'S', 'T']}]}}
        datatype = common.D_1138
        codes = ['P', 'S', 'T']
        min_len = 1
        max_len = 1


class L2320_SBR02(Element):
    """Individual Relationship Code"""
    class Schema:
        json = {'title': 'Individual Relationship Code',
         'usage': 'R',
         'description': 'xid=SBR02 data_ele=1069',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'},
                            {'enum': ['01', '18', '19', '20', '21', '22', '29',
                                      '76']}]}}
        datatype = common.D_1069
        codes = ['01', '18', '19', '20', '21', '22', '29', '76']
        min_len = 2
        max_len = 2


class L2320_SBR03(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
         'usage': 'S',
         'description': 'xid=SBR03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320_SBR04(Element):
    """Policy Name"""
    class Schema:
        json = {'title': 'Policy Name',
         'usage': 'S',
         'description': 'xid=SBR04 data_ele=93',
         'sequence': 4,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2320_SBR05(Element):
    """Insurance Type Code"""
    class Schema:
        json = {'title': 'Insurance Type Code',
         'usage': 'N',
         'description': 'xid=SBR05 data_ele=1336',
         'sequence': 5,
         'type': {'$ref': '#/$common/1336'}}
        datatype = common.D_1336
        min_len = 1
        max_len = 3


class L2320_SBR06(Element):
    """Coordination of Benefits Code"""
    class Schema:
        json = {'title': 'Coordination of Benefits Code',
         'usage': 'N',
         'description': 'xid=SBR06 data_ele=1143',
         'sequence': 6,
         'type': {'$ref': '#/$common/1143'}}
        datatype = common.D_1143
        min_len = 1
        max_len = 1


class L2320_SBR07(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=SBR07 data_ele=1073',
         'sequence': 7,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2320_SBR08(Element):
    """Employment Status Code"""
    class Schema:
        json = {'title': 'Employment Status Code',
         'usage': 'N',
         'description': 'xid=SBR08 data_ele=584',
         'sequence': 8,
         'type': {'$ref': '#/$common/584'}}
        datatype = common.D_584
        min_len = 2
        max_len = 2


class L2320_SBR09(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'S',
         'description': 'xid=SBR09 data_ele=1032',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/1032'},
                            {'enum': ['09', '11', '12', '13', '14', '15', '16', '17',
                                      'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB',
                                      'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ']}]}}
        datatype = common.D_1032
        codes = ['09', '11', '12', '13', '14', '15', '16', '17', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB', 'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ']
        min_len = 1
        max_len = 2


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    class Schema:
        json = {'title': 'Other Subscriber Information',
         'usage': 'R',
         'description': 'xid=SBR name=Other Subscriber Information',
         'position': 290,
         'type': 'object',
         'properties': {'xid': {'literal': 'SBR'},
                        'sbr01': {'$ref': '#/$elements/L2320_SBR01'},
                        'sbr02': {'$ref': '#/$elements/L2320_SBR02'},
                        'sbr03': {'$ref': '#/$elements/L2320_SBR03'},
                        'sbr04': {'$ref': '#/$elements/L2320_SBR04'},
                        'sbr09': {'$ref': '#/$elements/L2320_SBR09'}},
         'required': ['sbr01', 'sbr02']}
        segment_name = 'SBR'
    sbr01: L2320_SBR01
    sbr02: L2320_SBR02
    sbr03: L2320_SBR03 | None
    sbr04: L2320_SBR04 | None
    sbr09: L2320_SBR09 | None


class L2320_CAS01(Element):
    """Claim Adjustment Group Code"""
    class Schema:
        json = {'title': 'Claim Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'CR', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'CR', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2320_CAS02(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=CAS02 data_ele=1034',
         'sequence': 2,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS03(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'R',
         'description': 'xid=CAS03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS04(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS04 data_ele=380',
         'sequence': 4,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS05(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS05 data_ele=1034',
         'sequence': 5,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS06(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS07(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS07 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS08(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS08 data_ele=1034',
         'sequence': 8,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS09(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS09 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS10(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS10 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS11(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS11 data_ele=1034',
         'sequence': 11,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS12(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS12 data_ele=782',
         'sequence': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS13(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS13 data_ele=380',
         'sequence': 13,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS14(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS14 data_ele=1034',
         'sequence': 14,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS15(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS15 data_ele=782',
         'sequence': 15,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS16(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS16 data_ele=380',
         'sequence': 16,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS17(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS17 data_ele=1034',
         'sequence': 17,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS18(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS18 data_ele=782',
         'sequence': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS19(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS19 data_ele=380',
         'sequence': 19,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS(Segment):
    """Claim Adjustment"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Adjustment',
                   'usage': 'S',
                   'description': 'xid=CAS name=Claim Adjustment',
                   'position': 295,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'CAS'},
                                  'cas01': {'$ref': '#/$elements/L2320_CAS01'},
                                  'cas02': {'$ref': '#/$elements/L2320_CAS02'},
                                  'cas03': {'$ref': '#/$elements/L2320_CAS03'},
                                  'cas04': {'$ref': '#/$elements/L2320_CAS04'},
                                  'cas05': {'$ref': '#/$elements/L2320_CAS05'},
                                  'cas06': {'$ref': '#/$elements/L2320_CAS06'},
                                  'cas07': {'$ref': '#/$elements/L2320_CAS07'},
                                  'cas08': {'$ref': '#/$elements/L2320_CAS08'},
                                  'cas09': {'$ref': '#/$elements/L2320_CAS09'},
                                  'cas10': {'$ref': '#/$elements/L2320_CAS10'},
                                  'cas11': {'$ref': '#/$elements/L2320_CAS11'},
                                  'cas12': {'$ref': '#/$elements/L2320_CAS12'},
                                  'cas13': {'$ref': '#/$elements/L2320_CAS13'},
                                  'cas14': {'$ref': '#/$elements/L2320_CAS14'},
                                  'cas15': {'$ref': '#/$elements/L2320_CAS15'},
                                  'cas16': {'$ref': '#/$elements/L2320_CAS16'},
                                  'cas17': {'$ref': '#/$elements/L2320_CAS17'},
                                  'cas18': {'$ref': '#/$elements/L2320_CAS18'},
                                  'cas19': {'$ref': '#/$elements/L2320_CAS19'}},
                   'required': ['cas01', 'cas02', 'cas03']},
         'maxItems': 5}
        segment_name = 'CAS'
    cas01: L2320_CAS01
    cas02: L2320_CAS02
    cas03: L2320_CAS03
    cas04: L2320_CAS04 | None
    cas05: L2320_CAS05 | None
    cas06: L2320_CAS06 | None
    cas07: L2320_CAS07 | None
    cas08: L2320_CAS08 | None
    cas09: L2320_CAS09 | None
    cas10: L2320_CAS10 | None
    cas11: L2320_CAS11 | None
    cas12: L2320_CAS12 | None
    cas13: L2320_CAS13 | None
    cas14: L2320_CAS14 | None
    cas15: L2320_CAS15 | None
    cas16: L2320_CAS16 | None
    cas17: L2320_CAS17 | None
    cas18: L2320_CAS18 | None
    cas19: L2320_CAS19 | None


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['D']}]}}
        datatype = common.D_522
        codes = ['D']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Payer Paid Amount"""
    class Schema:
        json = {'title': 'Payer Paid Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Payer Paid Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Payer Paid Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Payer Paid Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['AAE']}]}}
        datatype = common.D_522
        codes = ['AAE']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Approved Amount"""
    class Schema:
        json = {'title': 'Approved Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Approved Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Approved Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Approved Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['B6']}]}}
        datatype = common.D_522
        codes = ['B6']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Allowed Amount"""
    class Schema:
        json = {'title': 'Allowed Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Allowed Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Allowed Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Allowed Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['F2']}]}}
        datatype = common.D_522
        codes = ['F2']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Patient Responsibility Amount"""
    class Schema:
        json = {'title': 'Patient Responsibility Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Responsibility Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Patient Responsibility Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Patient '
                        'Responsibility Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['AU']}]}}
        datatype = common.D_522
        codes = ['AU']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Covered Amount"""
    class Schema:
        json = {'title': 'Covered Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Covered Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Covered Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Covered Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['D8']}]}}
        datatype = common.D_522
        codes = ['D8']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Other Payer Discount Amount"""
    class Schema:
        json = {'title': 'Other Payer Discount Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Discount Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Discount Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Discount Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['F5']}]}}
        datatype = common.D_522
        codes = ['F5']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Other Payer Patient Paid Amount"""
    class Schema:
        json = {'title': 'Other Payer Patient Paid Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Paid Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Patient Paid Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Patient Paid '
                        'Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_DMG01(Element):
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


class L2320_DMG02(Element):
    """Other Insured Birth Date"""
    class Schema:
        json = {'title': 'Other Insured Birth Date',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2320_DMG03(Element):
    """Other Insured Gender Code"""
    class Schema:
        json = {'title': 'Other Insured Gender Code',
         'usage': 'R',
         'description': 'xid=DMG03 data_ele=1068',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2320_DMG04(Element):
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


class L2320_DMG05(Element):
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


class L2320_DMG06(Element):
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


class L2320_DMG07(Element):
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


class L2320_DMG08(Element):
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


class L2320_DMG09(Element):
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


class L2320_DMG(Segment):
    """Other Insured Demographic Information"""
    class Schema:
        json = {'title': 'Other Insured Demographic Information',
         'usage': 'S',
         'description': 'xid=DMG name=Other Insured Demographic Information',
         'position': 305,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2320_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2320_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2320_DMG03'}},
         'required': ['dmg01', 'dmg02', 'dmg03']}
        segment_name = 'DMG'
    dmg01: L2320_DMG01
    dmg02: L2320_DMG02
    dmg03: L2320_DMG03


class L2320_OI01(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'N',
         'description': 'xid=OI01 data_ele=1032',
         'sequence': 1,
         'type': {'$ref': '#/$common/1032'}}
        datatype = common.D_1032
        min_len = 1
        max_len = 2


class L2320_OI02(Element):
    """Claim Submission Reason Code"""
    class Schema:
        json = {'title': 'Claim Submission Reason Code',
         'usage': 'N',
         'description': 'xid=OI02 data_ele=1383',
         'sequence': 2,
         'type': {'$ref': '#/$common/1383'}}
        datatype = common.D_1383
        min_len = 2
        max_len = 2


class L2320_OI03(Element):
    """Benefits Assignment Certification Indicator"""
    class Schema:
        json = {'title': 'Benefits Assignment Certification Indicator',
         'usage': 'R',
         'description': 'xid=OI03 data_ele=1073',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2320_OI04(Element):
    """Patient Signature Source Code"""
    class Schema:
        json = {'title': 'Patient Signature Source Code',
         'usage': 'N',
         'description': 'xid=OI04 data_ele=1351',
         'sequence': 4,
         'type': {'$ref': '#/$common/1351'}}
        datatype = common.D_1351
        min_len = 1
        max_len = 1


class L2320_OI05(Element):
    """Provider Agreement Code"""
    class Schema:
        json = {'title': 'Provider Agreement Code',
         'usage': 'N',
         'description': 'xid=OI05 data_ele=1360',
         'sequence': 5,
         'type': {'$ref': '#/$common/1360'}}
        datatype = common.D_1360
        min_len = 1
        max_len = 1


class L2320_OI06(Element):
    """Release of Information"""
    class Schema:
        json = {'title': 'Release of Information',
         'usage': 'R',
         'description': 'xid=OI06 data_ele=1363',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1363'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1363
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2320_OI(Segment):
    """Other Insurance Coverage Information"""
    class Schema:
        json = {'title': 'Other Insurance Coverage Information',
         'usage': 'R',
         'description': 'xid=OI name=Other Insurance Coverage Information',
         'position': 310,
         'type': 'object',
         'properties': {'xid': {'literal': 'OI'},
                        'oi03': {'$ref': '#/$elements/L2320_OI03'},
                        'oi06': {'$ref': '#/$elements/L2320_OI06'}},
         'required': ['oi03', 'oi06']}
        segment_name = 'OI'
    oi03: L2320_OI03
    oi06: L2320_OI06


class L2330A_NM101(Element):
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


class L2330A_NM102(Element):
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


class L2330A_NM103(Element):
    """Other Insured Last Name"""
    class Schema:
        json = {'title': 'Other Insured Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330A_NM104(Element):
    """Other Insured First Name"""
    class Schema:
        json = {'title': 'Other Insured First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2330A_NM105(Element):
    """Other Insured Middle Name"""
    class Schema:
        json = {'title': 'Other Insured Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2330A_NM106(Element):
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


class L2330A_NM107(Element):
    """Other Insured Name Suffix"""
    class Schema:
        json = {'title': 'Other Insured Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2330A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', 'MI', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['24', 'MI', 'ZZ']
        min_len = 1
        max_len = 2


class L2330A_NM109(Element):
    """Other Insured Identifier"""
    class Schema:
        json = {'title': 'Other Insured Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2330A_NM110(Element):
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


class L2330A_NM111(Element):
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


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    class Schema:
        json = {'title': 'Other Subscriber Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Subscriber Name',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2330A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2330A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2330A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2330A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2330A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2330A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm104', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2330A_NM101
    nm102: L2330A_NM102
    nm103: L2330A_NM103
    nm104: L2330A_NM104
    nm105: L2330A_NM105 | None
    nm107: L2330A_NM107 | None
    nm108: L2330A_NM108
    nm109: L2330A_NM109


class L2330A_N301(Element):
    """Other Insured's Address 1"""
    class Schema:
        json = {'title': "Other Insured's Address 1",
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2330A_N302(Element):
    """Other Insured's Address 2"""
    class Schema:
        json = {'title': "Other Insured's Address 2",
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    class Schema:
        json = {'title': 'Other Subscriber Address',
         'usage': 'S',
         'description': 'xid=N3 name=Other Subscriber Address',
         'position': 332,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2330A_N301'},
                        'n302': {'$ref': '#/$elements/L2330A_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2330A_N301
    n302: L2330A_N302 | None


class L2330A_N401(Element):
    """Other Insured City Name"""
    class Schema:
        json = {'title': 'Other Insured City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2330A_N402(Element):
    """Other Insured State Code"""
    class Schema:
        json = {'title': 'Other Insured State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2330A_N403(Element):
    """Other Insured Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Other Insured Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2330A_N404(Element):
    """Other Insured's Country"""
    class Schema:
        json = {'title': "Other Insured's Country",
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2330A_N405(Element):
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


class L2330A_N406(Element):
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


class L2330A_N4(Segment):
    """Other Subscriber City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Other Subscriber City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Other Subscriber City/State/ZIP Code',
         'position': 340,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2330A_N401'},
                        'n402': {'$ref': '#/$elements/L2330A_N402'},
                        'n403': {'$ref': '#/$elements/L2330A_N403'},
                        'n404': {'$ref': '#/$elements/L2330A_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2330A_N401
    n402: L2330A_N402
    n403: L2330A_N403
    n404: L2330A_N404 | None


class L2330A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1W', '23', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1W', '23', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2330A_REF02(Element):
    """Other Insured Additional Identifier"""
    class Schema:
        json = {'title': 'Other Insured Additional Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330A_REF03(Element):
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


class L2330A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330A_REF(Segment):
    """Other Subscriber Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Subscriber Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Subscriber Secondary '
                                  'Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330A_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330A_REF01
    ref02: L2330A_REF02


class L2330A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Subscriber Name',
                   'usage': 'R',
                   'description': 'xid=2330A name=Other Subscriber Name type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330A_NM1'},
                                  'n3': {'$ref': '#/$segments/L2330A_N3'},
                                  'n4': {'$ref': '#/$segments/L2330A_N4'},
                                  'ref': {'$ref': '#/$segments/L2330A_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330A_NM1
    n3: L2330A_N3 | None
    n4: L2330A_N4 | None
    ref: list[L2330A_REF] | None


class L2330B_NM101(Element):
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


class L2330B_NM102(Element):
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


class L2330B_NM103(Element):
    """Other Payer Last or Organization Name"""
    class Schema:
        json = {'title': 'Other Payer Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330B_NM104(Element):
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


class L2330B_NM105(Element):
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


class L2330B_NM106(Element):
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


class L2330B_NM107(Element):
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


class L2330B_NM108(Element):
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


class L2330B_NM109(Element):
    """Other Payer Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2330B_NM110(Element):
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


class L2330B_NM111(Element):
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


class L2330B_NM1(Segment):
    """Other Payer Name"""
    class Schema:
        json = {'title': 'Other Payer Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Name',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2330B_NM103'},
                        'nm108': {'$ref': '#/$elements/L2330B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2330B_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2330B_NM101
    nm102: L2330B_NM102
    nm103: L2330B_NM103
    nm108: L2330B_NM108
    nm109: L2330B_NM109


class L2330B_PER01(Element):
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


class L2330B_PER02(Element):
    """Other Payer Contact Name"""
    class Schema:
        json = {'title': 'Other Payer Contact Name',
         'usage': 'R',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2330B_PER03(Element):
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


class L2330B_PER04(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330B_PER05(Element):
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


class L2330B_PER06(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330B_PER07(Element):
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


class L2330B_PER08(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330B_PER09(Element):
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


class L2330B_PER(Segment):
    """Other Payer Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Other Payer Contact Information',
                   'position': 345,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2330B_PER01'},
                                  'per02': {'$ref': '#/$elements/L2330B_PER02'},
                                  'per03': {'$ref': '#/$elements/L2330B_PER03'},
                                  'per04': {'$ref': '#/$elements/L2330B_PER04'},
                                  'per05': {'$ref': '#/$elements/L2330B_PER05'},
                                  'per06': {'$ref': '#/$elements/L2330B_PER06'},
                                  'per07': {'$ref': '#/$elements/L2330B_PER07'},
                                  'per08': {'$ref': '#/$elements/L2330B_PER08'}},
                   'required': ['per01', 'per02', 'per03', 'per04']},
         'maxItems': 2}
        segment_name = 'PER'
    per01: L2330B_PER01
    per02: L2330B_PER02
    per03: L2330B_PER03
    per04: L2330B_PER04
    per05: L2330B_PER05 | None
    per06: L2330B_PER06 | None
    per07: L2330B_PER07 | None
    per08: L2330B_PER08 | None


class L2330B_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['573']}]}}
        datatype = common.D_374
        codes = ['573']
        min_len = 3
        max_len = 3


class L2330B_DTP02(Element):
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


class L2330B_DTP03(Element):
    """Date Claim Paid"""
    class Schema:
        json = {'title': 'Date Claim Paid',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2330B_DTP(Segment):
    """Claim Paid Date"""
    class Schema:
        json = {'title': 'Claim Paid Date',
         'usage': 'S',
         'description': 'xid=DTP name=Claim Paid Date',
         'position': 350,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2330B_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2330B_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2330B_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2330B_DTP01
    dtp02: L2330B_DTP02
    dtp03: L2330B_DTP03


class L2330B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['2U', 'D8', 'F8', 'FY', 'NF', 'TJ']}]}}
        datatype = common.D_128
        codes = ['2U', 'D8', 'F8', 'FY', 'NF', 'TJ']
        min_len = 2
        max_len = 3


class L2330B_REF02(Element):
    """Other Payer Secondary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330B_REF03(Element):
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


class L2330B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330B_REF(Segment):
    """Other Payer Secondary Identifier"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Secondary Identifier',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Secondary Identifier',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330B_REF01
    ref02: L2330B_REF02


class L2330B_REF01(Element):
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


class L2330B_REF02(Element):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330B_REF03(Element):
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


class L2330B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Prior Authorization or '
                                  'Referral Number',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2330B_REF01
    ref02: L2330B_REF02


class L2330B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['T4']}]}}
        datatype = common.D_128
        codes = ['T4']
        min_len = 2
        max_len = 3


class L2330B_REF02(Element):
    """Other Payer Claim Adjustment Indicator"""
    class Schema:
        json = {'title': 'Other Payer Claim Adjustment Indicator',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330B_REF03(Element):
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


class L2330B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330B_REF(Segment):
    """Other Payer Claim Adjustment Indicator"""
    class Schema:
        json = {'title': 'Other Payer Claim Adjustment Indicator',
         'usage': 'S',
         'description': 'xid=REF name=Other Payer Claim Adjustment Indicator',
         'position': 355,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2330B_REF01'},
                        'ref02': {'$ref': '#/$elements/L2330B_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2330B_REF01
    ref02: L2330B_REF02


class L2330B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Name',
                   'usage': 'R',
                   'description': 'xid=2330B name=Other Payer Name type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330B_NM1'},
                                  'per': {'$ref': '#/$segments/L2330B_PER'},
                                  'dtp': {'$ref': '#/$segments/L2330B_DTP'},
                                  'ref': {'$ref': '#/$segments/L2330B_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330B_NM1
    per: list[L2330B_PER] | None
    dtp: L2330B_DTP | None
    ref: list[L2330B_REF] | None
    ref: list[L2330B_REF] | None
    ref: L2330B_REF | None


class L2330C_NM101(Element):
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


class L2330C_NM102(Element):
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


class L2330C_NM103(Element):
    """Other Payer Patient Last Name"""
    class Schema:
        json = {'title': 'Other Payer Patient Last Name',
         'usage': 'N',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330C_NM104(Element):
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


class L2330C_NM105(Element):
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


class L2330C_NM106(Element):
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


class L2330C_NM107(Element):
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


class L2330C_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['MI']}]}}
        datatype = common.D_66
        codes = ['MI']
        min_len = 1
        max_len = 2


class L2330C_NM109(Element):
    """Other Payer Patient Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Patient Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2330C_NM110(Element):
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


class L2330C_NM111(Element):
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


class L2330C_NM1(Segment):
    """Other Payer Patient Information"""
    class Schema:
        json = {'title': 'Other Payer Patient Information',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Patient Information',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330C_NM102'},
                        'nm108': {'$ref': '#/$elements/L2330C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2330C_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2330C_NM101
    nm102: L2330C_NM102
    nm108: L2330C_NM108
    nm109: L2330C_NM109


class L2330C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1W', '23', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1W', '23', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2330C_REF02(Element):
    """Other Payer Patient Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Patient Primary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330C_REF03(Element):
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


class L2330C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330C_REF(Segment):
    """Other Payer Patient Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Patient Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Patient Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330C_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330C_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330C_REF01
    ref02: L2330C_REF02


class L2330C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Patient Information',
                   'usage': 'S',
                   'description': 'xid=2330C name=Other Payer Patient Information '
                                  'type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330C_NM1'},
                                  'ref': {'$ref': '#/$segments/L2330C_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330C_NM1
    ref: list[L2330C_REF] | None


class L2330D_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DN', 'P3']}]}}
        datatype = common.D_98
        codes = ['DN', 'P3']
        min_len = 2
        max_len = 3


class L2330D_NM102(Element):
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


class L2330D_NM103(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330D_NM104(Element):
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


class L2330D_NM105(Element):
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


class L2330D_NM106(Element):
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


class L2330D_NM107(Element):
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


class L2330D_NM108(Element):
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


class L2330D_NM109(Element):
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


class L2330D_NM110(Element):
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


class L2330D_NM111(Element):
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


class L2330D_NM1(Segment):
    """Other Payer Referring Provider"""
    class Schema:
        json = {'title': 'Other Payer Referring Provider',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Referring Provider',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330D_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330D_NM102'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2330D_NM101
    nm102: L2330D_NM102


class L2330D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2330D_REF02(Element):
    """Other Payer Referring Provider Identifier"""
    class Schema:
        json = {'title': 'Other Payer Referring Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330D_REF03(Element):
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


class L2330D_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330D_REF(Segment):
    """Other Payer Referring Provider Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Referring Provider Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Referring Provider '
                                  'Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330D_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330D_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330D_REF01
    ref02: L2330D_REF02


class L2330D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Referring Provider',
                   'usage': 'S',
                   'description': 'xid=2330D name=Other Payer Referring Provider '
                                  'type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330D_NM1'},
                                  'ref': {'$ref': '#/$segments/L2330D_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330D_NM1
    ref: list[L2330D_REF] | None


class L2330E_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['82']}]}}
        datatype = common.D_98
        codes = ['82']
        min_len = 2
        max_len = 3


class L2330E_NM102(Element):
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


class L2330E_NM103(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330E_NM104(Element):
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


class L2330E_NM105(Element):
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


class L2330E_NM106(Element):
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


class L2330E_NM107(Element):
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


class L2330E_NM108(Element):
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


class L2330E_NM109(Element):
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


class L2330E_NM110(Element):
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


class L2330E_NM111(Element):
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


class L2330E_NM1(Segment):
    """Other Payer Rendering Provider"""
    class Schema:
        json = {'title': 'Other Payer Rendering Provider',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Rendering Provider',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330E_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330E_NM102'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2330E_NM101
    nm102: L2330E_NM102


class L2330E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2330E_REF02(Element):
    """Other Payer Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Other Payer Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330E_REF03(Element):
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


class L2330E_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330E_REF(Segment):
    """Other Payer Rendering Provider Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Rendering Provider Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Rendering Provider '
                                  'Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330E_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330E_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330E_REF01
    ref02: L2330E_REF02


class L2330E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Rendering Provider',
                   'usage': 'S',
                   'description': 'xid=2330E name=Other Payer Rendering Provider '
                                  'type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330E_NM1'},
                                  'ref': {'$ref': '#/$segments/L2330E_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330E_NM1
    ref: list[L2330E_REF] | None


class L2320(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Subscriber Information',
                   'usage': 'S',
                   'description': 'xid=2320 name=Other Subscriber Information '
                                  'type=None',
                   'position': 290,
                   'type': 'object',
                   'properties': {'sbr': {'$ref': '#/$segments/L2320_SBR'},
                                  'cas': {'$ref': '#/$segments/L2320_CAS'},
                                  'amt': {'$ref': '#/$segments/L2320_AMT'},
                                  'dmg': {'$ref': '#/$segments/L2320_DMG'},
                                  'oi': {'$ref': '#/$segments/L2320_OI'},
                                  'l2330a': {'$ref': '#/$segments/L2330A'},
                                  'l2330b': {'$ref': '#/$segments/L2330B'},
                                  'l2330c': {'$ref': '#/$segments/L2330C'},
                                  'l2330d': {'$ref': '#/$segments/L2330D'},
                                  'l2330e': {'$ref': '#/$segments/L2330E'}},
                   'required': ['sbr', 'oi', 'l2330a', 'l2330b']},
         'maxItems': 10}
    sbr: L2320_SBR
    cas: list[L2320_CAS] | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    dmg: L2320_DMG | None
    oi: L2320_OI
    l2330a: list[L2330A]
    l2330b: list[L2330B]
    l2330c: list[L2330C] | None
    l2330d: list[L2330D] | None
    l2330e: list[L2330E] | None


class L2400_LX01(Element):
    """Line Counter"""
    class Schema:
        json = {'title': 'Line Counter',
         'usage': 'R',
         'description': 'xid=LX01 data_ele=554',
         'sequence': 1,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2400_LX(Segment):
    """Line Counter"""
    class Schema:
        json = {'title': 'Line Counter',
         'usage': 'R',
         'description': 'xid=LX name=Line Counter',
         'position': 365,
         'type': 'object',
         'properties': {'xid': {'literal': 'LX'},
                        'lx01': {'$ref': '#/$elements/L2400_LX01'}},
         'required': ['lx01']}
        segment_name = 'LX'
    lx01: L2400_LX01


class L2400_SV301_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SV301-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'}, {'enum': ['AD']}]}}
        datatype = common.D_235
        codes = ['AD']
        min_len = 2
        max_len = 2


class L2400_SV301_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SV301-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2400_SV301_03(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_04(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_05(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_06(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=SV301-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2400_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'R',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'sv301_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SV301-01 data_ele=235',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD']}]}},
                        'sv301_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SV301-02 data_ele=234',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'sv301_03': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-03 data_ele=1339',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_04': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-04 data_ele=1339',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_05': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-05 data_ele=1339',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_06': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-06 data_ele=1339',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_07': {'title': 'Description',
                                     'usage': 'N',
                                     'description': 'xid=SV301-07 data_ele=352',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/352'}}},
         'required': ['sv301_01', 'sv301_02']}
    sv301_01: L2400_SV301_01
    sv301_02: L2400_SV301_02
    sv301_03: L2400_SV301_03 | None
    sv301_04: L2400_SV301_04 | None
    sv301_05: L2400_SV301_05 | None
    sv301_06: L2400_SV301_06 | None


class L2400_SV302(Element):
    """Line Item Charge Amount"""
    class Schema:
        json = {'title': 'Line Item Charge Amount',
         'usage': 'R',
         'description': 'xid=SV302 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2400_SV303(Element):
    """Facility Type Code"""
    class Schema:
        json = {'title': 'Facility Type Code',
         'usage': 'S',
         'description': 'xid=SV303 data_ele=1331',
         'sequence': 3,
         'type': {'$ref': '#/$common/1331'}}
        datatype = common.D_1331
        codes = common.pos
        min_len = 1
        max_len = 2


class L2400_SV304_01(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'R',
         'description': 'xid=SV304-01 data_ele=1361',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_02(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-02 data_ele=1361',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_03(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-03 data_ele=1361',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_04(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-04 data_ele=1361',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_05(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-05 data_ele=1361',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_C006(Composite):
    class Schema:
        json = {'title': 'Oral Cavity Designation',
         'usage': 'S',
         'description': 'xid=None name=Oral Cavity Designation refdes= data_ele=C006',
         'sequence': 4,
         'syntax': [],
         'type': 'object',
         'properties': {'sv304_01': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'R',
                                     'description': 'xid=SV304-01 data_ele=1361',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_02': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-02 data_ele=1361',
                                     'sequence': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_03': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-03 data_ele=1361',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_04': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-04 data_ele=1361',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_05': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-05 data_ele=1361',
                                     'sequence': 5,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}}},
         'required': ['sv304_01']}
    sv304_01: L2400_SV304_01
    sv304_02: L2400_SV304_02 | None
    sv304_03: L2400_SV304_03 | None
    sv304_04: L2400_SV304_04 | None
    sv304_05: L2400_SV304_05 | None


class L2400_SV305(Element):
    """Prosthesis, Crown, or Inlay Code"""
    class Schema:
        json = {'title': 'Prosthesis, Crown, or Inlay Code',
         'usage': 'S',
         'description': 'xid=SV305 data_ele=1358',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1358'}, {'enum': ['I', 'R']}]}}
        datatype = common.D_1358
        codes = ['I', 'R']
        min_len = 1
        max_len = 1


class L2400_SV306(Element):
    """Procedure Count"""
    class Schema:
        json = {'title': 'Procedure Count',
         'usage': 'R',
         'description': 'xid=SV306 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2400_SV307(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=SV307 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2400_SV308(Element):
    """Copay Status Code"""
    class Schema:
        json = {'title': 'Copay Status Code',
         'usage': 'N',
         'description': 'xid=SV308 data_ele=1327',
         'sequence': 8,
         'type': {'$ref': '#/$common/1327'}}
        datatype = common.D_1327
        min_len = 1
        max_len = 1


class L2400_SV309(Element):
    """Provider Agreement Code"""
    class Schema:
        json = {'title': 'Provider Agreement Code',
         'usage': 'N',
         'description': 'xid=SV309 data_ele=1360',
         'sequence': 9,
         'type': {'$ref': '#/$common/1360'}}
        datatype = common.D_1360
        min_len = 1
        max_len = 1


class L2400_SV310(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=SV310 data_ele=1073',
         'sequence': 10,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2400_C004(Composite):
    class Schema:
        json = {'title': 'Composite Diagnosis Code Pointer',
         'usage': 'N',
         'description': 'xid=None name=Composite Diagnosis Code Pointer refdes= '
                        'data_ele=C004',
         'sequence': 11,
         'syntax': []}


class L2400_SV3(Segment):
    """Dental Service"""
    class Schema:
        json = {'title': 'Dental Service',
         'usage': 'R',
         'description': 'xid=SV3 name=Dental Service',
         'position': 380,
         'type': 'object',
         'properties': {'xid': {'literal': 'SV3'},
                        'c003': {'$ref': '#/$elements/L2400_C003'},
                        'sv302': {'$ref': '#/$elements/L2400_SV302'},
                        'sv303': {'$ref': '#/$elements/L2400_SV303'},
                        'c006': {'$ref': '#/$elements/L2400_C006'},
                        'sv305': {'$ref': '#/$elements/L2400_SV305'},
                        'sv306': {'$ref': '#/$elements/L2400_SV306'}},
         'required': ['c003', 'sv302', 'sv306']}
        segment_name = 'SV3'
    c003: L2400_C003
    sv302: L2400_SV302
    sv303: L2400_SV303 | None
    c006: L2400_C006 | None
    sv305: L2400_SV305 | None
    sv306: L2400_SV306


class L2400_TOO01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=TOO01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['JP']}]}}
        datatype = common.D_1270
        codes = ['JP']
        min_len = 1
        max_len = 3


class L2400_TOO02(Element):
    """Tooth Code"""
    class Schema:
        json = {'title': 'Tooth Code',
         'usage': 'S',
         'description': 'xid=TOO02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2400_TOO03_01(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'R',
         'description': 'xid=TOO03-01 data_ele=1369',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_02(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-02 data_ele=1369',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_03(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-03 data_ele=1369',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_04(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-04 data_ele=1369',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_05(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-05 data_ele=1369',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_C005(Composite):
    class Schema:
        json = {'title': 'Tooth Surface',
         'usage': 'S',
         'description': 'xid=None name=Tooth Surface refdes= data_ele=C005',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'too03_01': {'title': 'Tooth Surface Code',
                                     'usage': 'R',
                                     'description': 'xid=TOO03-01 data_ele=1369',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_02': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-02 data_ele=1369',
                                     'sequence': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_03': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-03 data_ele=1369',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_04': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-04 data_ele=1369',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_05': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-05 data_ele=1369',
                                     'sequence': 5,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}}},
         'required': ['too03_01']}
    too03_01: L2400_TOO03_01
    too03_02: L2400_TOO03_02 | None
    too03_03: L2400_TOO03_03 | None
    too03_04: L2400_TOO03_04 | None
    too03_05: L2400_TOO03_05 | None


class L2400_TOO(Segment):
    """Tooth Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Tooth Information',
                   'usage': 'S',
                   'description': 'xid=TOO name=Tooth Information',
                   'position': 382,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'TOO'},
                                  'too01': {'$ref': '#/$elements/L2400_TOO01'},
                                  'too02': {'$ref': '#/$elements/L2400_TOO02'},
                                  'c005': {'$ref': '#/$elements/L2400_C005'}},
                   'required': ['too01']},
         'maxItems': 32}
        segment_name = 'TOO'
    too01: L2400_TOO01
    too02: L2400_TOO02 | None
    c005: L2400_C005 | None


class L2400_DTP01(Element):
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


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Service Date"""
    class Schema:
        json = {'title': 'Service Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Service"""
    class Schema:
        json = {'title': 'Date - Service',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Service',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['441']}]}}
        datatype = common.D_374
        codes = ['441']
        min_len = 3
        max_len = 3


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Prior Placement Date"""
    class Schema:
        json = {'title': 'Prior Placement Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Prior Placement"""
    class Schema:
        json = {'title': 'Date - Prior Placement',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Prior Placement',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['452']}]}}
        datatype = common.D_374
        codes = ['452']
        min_len = 3
        max_len = 3


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Orthodontic Banding Date"""
    class Schema:
        json = {'title': 'Orthodontic Banding Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Appliance Placement"""
    class Schema:
        json = {'title': 'Date - Appliance Placement',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Appliance Placement',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['446']}]}}
        datatype = common.D_374
        codes = ['446']
        min_len = 3
        max_len = 3


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Replacement Date"""
    class Schema:
        json = {'title': 'Replacement Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Replacement"""
    class Schema:
        json = {'title': 'Date - Replacement',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Replacement',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_QTY01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=QTY01 data_ele=673',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['BF', 'EM', 'HM', 'HO', 'HP', 'P3', 'P4', 'P5',
                                      'SG']}]}}
        datatype = common.D_673
        codes = ['BF', 'EM', 'HM', 'HO', 'HP', 'P3', 'P4', 'P5', 'SG']
        min_len = 2
        max_len = 2


class L2400_QTY02(Element):
    """Anesthesia Unit Count"""
    class Schema:
        json = {'title': 'Anesthesia Unit Count',
         'usage': 'R',
         'description': 'xid=QTY02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2400_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 3,
         'syntax': []}


class L2400_QTY04(Element):
    """Free-Form Message"""
    class Schema:
        json = {'title': 'Free-Form Message',
         'usage': 'N',
         'description': 'xid=QTY04 data_ele=61',
         'sequence': 4,
         'type': {'$ref': '#/$common/61'}}
        datatype = common.D_61
        min_len = 1
        max_len = 30


class L2400_QTY(Segment):
    """Anesthesia Quantity"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Anesthesia Quantity',
                   'usage': 'S',
                   'description': 'xid=QTY name=Anesthesia Quantity',
                   'position': 460,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'QTY'},
                                  'qty01': {'$ref': '#/$elements/L2400_QTY01'},
                                  'qty02': {'$ref': '#/$elements/L2400_QTY02'}},
                   'required': ['qty01', 'qty02']},
         'maxItems': 5}
        segment_name = 'QTY'
    qty01: L2400_QTY01
    qty02: L2400_QTY02


class L2400_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['G3']}]}}
        datatype = common.D_128
        codes = ['G3']
        min_len = 2
        max_len = 3


class L2400_REF02(Element):
    """Predetermination of Benefits Identifier"""
    class Schema:
        json = {'title': 'Predetermination of Benefits Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2400_REF03(Element):
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


class L2400_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2400_REF(Segment):
    """Service Predetermination Identification"""
    class Schema:
        json = {'title': 'Service Predetermination Identification',
         'usage': 'S',
         'description': 'xid=REF name=Service Predetermination Identification',
         'position': 470,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2400_REF01'},
                        'ref02': {'$ref': '#/$elements/L2400_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2400_REF01
    ref02: L2400_REF02


class L2400_REF01(Element):
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


class L2400_REF02(Element):
    """Referral Number"""
    class Schema:
        json = {'title': 'Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2400_REF03(Element):
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


class L2400_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2400_REF(Segment):
    """Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Prior Authorization or Referral Number',
                   'position': 470,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2400_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2400_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2400_REF01
    ref02: L2400_REF02


class L2400_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['6R']}]}}
        datatype = common.D_128
        codes = ['6R']
        min_len = 2
        max_len = 3


class L2400_REF02(Element):
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


class L2400_REF03(Element):
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


class L2400_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2400_REF(Segment):
    """Line Item Control Number"""
    class Schema:
        json = {'title': 'Line Item Control Number',
         'usage': 'S',
         'description': 'xid=REF name=Line Item Control Number',
         'position': 470,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2400_REF01'},
                        'ref02': {'$ref': '#/$elements/L2400_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2400_REF01
    ref02: L2400_REF02


class L2400_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['AAE']}]}}
        datatype = common.D_522
        codes = ['AAE']
        min_len = 1
        max_len = 3


class L2400_AMT02(Element):
    """Approved Amount"""
    class Schema:
        json = {'title': 'Approved Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2400_AMT03(Element):
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


class L2400_AMT(Segment):
    """Approved Amount"""
    class Schema:
        json = {'title': 'Approved Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Approved Amount',
         'position': 475,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2400_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2400_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2400_AMT01
    amt02: L2400_AMT02


class L2400_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['T']}]}}
        datatype = common.D_522
        codes = ['T']
        min_len = 1
        max_len = 3


class L2400_AMT02(Element):
    """Sales Tax Amount"""
    class Schema:
        json = {'title': 'Sales Tax Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2400_AMT03(Element):
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


class L2400_AMT(Segment):
    """Sales Tax Amount"""
    class Schema:
        json = {'title': 'Sales Tax Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Sales Tax Amount',
         'position': 475,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2400_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2400_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2400_AMT01
    amt02: L2400_AMT02


class L2400_NTE01(Element):
    """Note Reference Code"""
    class Schema:
        json = {'title': 'Note Reference Code',
         'usage': 'R',
         'description': 'xid=NTE01 data_ele=363',
         'sequence': 1,
         'type': {'$ref': '#/$common/363'}}
        datatype = common.D_363
        min_len = 3
        max_len = 3


class L2400_NTE02(Element):
    """Claim Note Text"""
    class Schema:
        json = {'title': 'Claim Note Text',
         'usage': 'R',
         'description': 'xid=NTE02 data_ele=352',
         'sequence': 2,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2400_NTE(Segment):
    """Line Note"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Line Note',
                   'usage': 'S',
                   'description': 'xid=NTE name=Line Note',
                   'position': 485,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'NTE'},
                                  'nte01': {'$ref': '#/$elements/L2400_NTE01'},
                                  'nte02': {'$ref': '#/$elements/L2400_NTE02'}},
                   'required': ['nte01', 'nte02']},
         'maxItems': 10}
        segment_name = 'NTE'
    nte01: L2400_NTE01
    nte02: L2400_NTE02


class L2420A_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['82']}]}}
        datatype = common.D_98
        codes = ['82']
        min_len = 2
        max_len = 3


class L2420A_NM102(Element):
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


class L2420A_NM103(Element):
    """Rendering Provider Last or Organization Name"""
    class Schema:
        json = {'title': 'Rendering Provider Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2420A_NM104(Element):
    """Rendering Provider First Name"""
    class Schema:
        json = {'title': 'Rendering Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2420A_NM105(Element):
    """Rendering Provider Middle Name"""
    class Schema:
        json = {'title': 'Rendering Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2420A_NM106(Element):
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


class L2420A_NM107(Element):
    """Rendering Provider Name Suffix"""
    class Schema:
        json = {'title': 'Rendering Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2420A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2420A_NM109(Element):
    """Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2420A_NM110(Element):
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


class L2420A_NM111(Element):
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


class L2420A_NM1(Segment):
    """Rendering Provider Name"""
    class Schema:
        json = {'title': 'Rendering Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Rendering Provider Name',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2420A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2420A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2420A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2420A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2420A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2420A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2420A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2420A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2420A_NM101
    nm102: L2420A_NM102
    nm103: L2420A_NM103
    nm104: L2420A_NM104 | None
    nm105: L2420A_NM105 | None
    nm107: L2420A_NM107 | None
    nm108: L2420A_NM108
    nm109: L2420A_NM109


class L2420A_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['PE']}]}}
        datatype = common.D_1221
        codes = ['PE']
        min_len = 1
        max_len = 3


class L2420A_PRV02(Element):
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


class L2420A_PRV03(Element):
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


class L2420A_PRV04(Element):
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


class L2420A_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2420A_PRV06(Element):
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


class L2420A_PRV(Segment):
    """Rendering Provider Specialty Information"""
    class Schema:
        json = {'title': 'Rendering Provider Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Rendering Provider Specialty Information',
         'position': 505,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2420A_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2420A_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2420A_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2420A_PRV01
    prv02: L2420A_PRV02
    prv03: L2420A_PRV03


class L2420A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2420A_REF02(Element):
    """Rendering Provider Secondary Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2420A_REF03(Element):
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


class L2420A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2420A_REF(Segment):
    """Rendering Provider Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Secondary '
                                  'Identification',
                   'position': 525,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2420A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2420A_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2420A_REF01
    ref02: L2420A_REF02


class L2420A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Name',
                   'usage': 'S',
                   'description': 'xid=2420A name=Rendering Provider Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2420A_NM1'},
                                  'prv': {'$ref': '#/$segments/L2420A_PRV'},
                                  'ref': {'$ref': '#/$segments/L2420A_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2420A_NM1
    prv: L2420A_PRV | None
    ref: list[L2420A_REF] | None


class L2420B_NM101(Element):
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


class L2420B_NM102(Element):
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


class L2420B_NM103(Element):
    """Other Payer Last or Organization Name"""
    class Schema:
        json = {'title': 'Other Payer Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2420B_NM104(Element):
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


class L2420B_NM105(Element):
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


class L2420B_NM106(Element):
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


class L2420B_NM107(Element):
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


class L2420B_NM108(Element):
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


class L2420B_NM109(Element):
    """Other Payer Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Referral Number',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2420B_NM110(Element):
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


class L2420B_NM111(Element):
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


class L2420B_NM1(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Prior Authorization or Referral '
                        'Number',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2420B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2420B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2420B_NM103'},
                        'nm108': {'$ref': '#/$elements/L2420B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2420B_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2420B_NM101
    nm102: L2420B_NM102
    nm103: L2420B_NM103
    nm108: L2420B_NM108
    nm109: L2420B_NM109


class L2420B_REF01(Element):
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


class L2420B_REF02(Element):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2420B_REF03(Element):
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


class L2420B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2420B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Prior Authorization or '
                                  'Referral Number',
                   'position': 525,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2420B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2420B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2420B_REF01
    ref02: L2420B_REF02


class L2420B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=2420B name=Other Payer Prior Authorization or '
                                  'Referral Number type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2420B_NM1'},
                                  'ref': {'$ref': '#/$segments/L2420B_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2420B_NM1
    ref: list[L2420B_REF] | None


class L2420C_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DD']}]}}
        datatype = common.D_98
        codes = ['DD']
        min_len = 2
        max_len = 3


class L2420C_NM102(Element):
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


class L2420C_NM103(Element):
    """Assistant Surgeon Last or Organization Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2420C_NM104(Element):
    """Assistant Surgeon First Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2420C_NM105(Element):
    """Assistant Surgeon Middle Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2420C_NM106(Element):
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


class L2420C_NM107(Element):
    """Assistant Surgeon Name Suffix"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2420C_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2420C_NM109(Element):
    """Assistant Surgeon Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2420C_NM110(Element):
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


class L2420C_NM111(Element):
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


class L2420C_NM1(Segment):
    """Assistant Surgeon Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Assistant Surgeon Name',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2420C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2420C_NM102'},
                        'nm103': {'$ref': '#/$elements/L2420C_NM103'},
                        'nm104': {'$ref': '#/$elements/L2420C_NM104'},
                        'nm105': {'$ref': '#/$elements/L2420C_NM105'},
                        'nm107': {'$ref': '#/$elements/L2420C_NM107'},
                        'nm108': {'$ref': '#/$elements/L2420C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2420C_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2420C_NM101
    nm102: L2420C_NM102
    nm103: L2420C_NM103
    nm104: L2420C_NM104 | None
    nm105: L2420C_NM105 | None
    nm107: L2420C_NM107 | None
    nm108: L2420C_NM108
    nm109: L2420C_NM109


class L2420C_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['AS']}]}}
        datatype = common.D_1221
        codes = ['AS']
        min_len = 1
        max_len = 3


class L2420C_PRV02(Element):
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


class L2420C_PRV03(Element):
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


class L2420C_PRV04(Element):
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


class L2420C_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2420C_PRV06(Element):
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


class L2420C_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    class Schema:
        json = {'title': 'Assistant Surgeon Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Assistant Surgeon Specialty Information',
         'position': 505,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2420C_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2420C_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2420C_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2420C_PRV01
    prv02: L2420C_PRV02
    prv03: L2420C_PRV03


class L2420C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'LU', 'TJ', 'X4', 'X5']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'LU', 'TJ', 'X4', 'X5']
        min_len = 2
        max_len = 3


class L2420C_REF02(Element):
    """Assistant Surgeon Secondary Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2420C_REF03(Element):
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


class L2420C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2420C_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identification',
         'usage': 'S',
         'description': 'xid=REF name=Assistant Surgeon Secondary Identification',
         'position': 525,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2420C_REF01'},
                        'ref02': {'$ref': '#/$elements/L2420C_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2420C_REF01
    ref02: L2420C_REF02


class L2420C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Assistant Surgeon Name',
                   'usage': 'S',
                   'description': 'xid=2420C name=Assistant Surgeon Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2420C_NM1'},
                                  'prv': {'$ref': '#/$segments/L2420C_PRV'},
                                  'ref': {'$ref': '#/$segments/L2420C_REF'}}},
         'maxItems': 1}
    nm1: L2420C_NM1 | None
    prv: L2420C_PRV | None
    ref: L2420C_REF | None


class L2430_SVD01(Element):
    """Other Payer Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Primary Identifier',
         'usage': 'R',
         'description': 'xid=SVD01 data_ele=67',
         'sequence': 1,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2430_SVD02(Element):
    """Service Line Paid Amount"""
    class Schema:
        json = {'title': 'Service Line Paid Amount',
         'usage': 'R',
         'description': 'xid=SVD02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_SVD03_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SVD03-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'}, {'enum': ['AD', 'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'ZZ']
        min_len = 2
        max_len = 2


class L2430_SVD03_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SVD03-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2430_SVD03_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_07(Element):
    """Procedure Code Description"""
    class Schema:
        json = {'title': 'Procedure Code Description',
         'usage': 'S',
         'description': 'xid=SVD03-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2430_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'R',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'svd03_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SVD03-01 data_ele=235',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD', 'ZZ']}]}},
                        'svd03_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SVD03-02 data_ele=234',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'svd03_03': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-03 data_ele=1339',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_04': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-04 data_ele=1339',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_05': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-05 data_ele=1339',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_06': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-06 data_ele=1339',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_07': {'title': 'Procedure Code Description',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-07 data_ele=352',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/352'}}},
         'required': ['svd03_01', 'svd03_02']}
    svd03_01: L2430_SVD03_01
    svd03_02: L2430_SVD03_02
    svd03_03: L2430_SVD03_03 | None
    svd03_04: L2430_SVD03_04 | None
    svd03_05: L2430_SVD03_05 | None
    svd03_06: L2430_SVD03_06 | None
    svd03_07: L2430_SVD03_07 | None


class L2430_SVD04(Element):
    """Product/Service ID"""
    class Schema:
        json = {'title': 'Product/Service ID',
         'usage': 'N',
         'description': 'xid=SVD04 data_ele=234',
         'sequence': 4,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2430_SVD05(Element):
    """Paid Service Unit Count"""
    class Schema:
        json = {'title': 'Paid Service Unit Count',
         'usage': 'R',
         'description': 'xid=SVD05 data_ele=380',
         'sequence': 5,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_SVD06(Element):
    """Bundled or Unbundled Line Number"""
    class Schema:
        json = {'title': 'Bundled or Unbundled Line Number',
         'usage': 'S',
         'description': 'xid=SVD06 data_ele=554',
         'sequence': 6,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2430_SVD(Segment):
    """Line Adjudication Information"""
    class Schema:
        json = {'title': 'Line Adjudication Information',
         'usage': 'R',
         'description': 'xid=SVD name=Line Adjudication Information',
         'position': 540,
         'type': 'object',
         'properties': {'xid': {'literal': 'SVD'},
                        'svd01': {'$ref': '#/$elements/L2430_SVD01'},
                        'svd02': {'$ref': '#/$elements/L2430_SVD02'},
                        'c003': {'$ref': '#/$elements/L2430_C003'},
                        'svd05': {'$ref': '#/$elements/L2430_SVD05'},
                        'svd06': {'$ref': '#/$elements/L2430_SVD06'}},
         'required': ['svd01', 'svd02', 'c003', 'svd05']}
        segment_name = 'SVD'
    svd01: L2430_SVD01
    svd02: L2430_SVD02
    c003: L2430_C003
    svd05: L2430_SVD05
    svd06: L2430_SVD06 | None


class L2430_CAS01(Element):
    """Adjustment Group Code"""
    class Schema:
        json = {'title': 'Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'CR', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'CR', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2430_CAS02(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=CAS02 data_ele=1034',
         'sequence': 2,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS03(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'R',
         'description': 'xid=CAS03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS04(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS04 data_ele=380',
         'sequence': 4,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS05(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS05 data_ele=1034',
         'sequence': 5,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS06(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS07(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS07 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS08(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS08 data_ele=1034',
         'sequence': 8,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS09(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS09 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS10(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS10 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS11(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS11 data_ele=1034',
         'sequence': 11,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS12(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS12 data_ele=782',
         'sequence': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS13(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS13 data_ele=380',
         'sequence': 13,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS14(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS14 data_ele=1034',
         'sequence': 14,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS15(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS15 data_ele=782',
         'sequence': 15,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS16(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS16 data_ele=380',
         'sequence': 16,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS17(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS17 data_ele=1034',
         'sequence': 17,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS18(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS18 data_ele=782',
         'sequence': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS19(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS19 data_ele=380',
         'sequence': 19,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS(Segment):
    """Service Adjustment"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Adjustment',
                   'usage': 'S',
                   'description': 'xid=CAS name=Service Adjustment',
                   'position': 545,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'CAS'},
                                  'cas01': {'$ref': '#/$elements/L2430_CAS01'},
                                  'cas02': {'$ref': '#/$elements/L2430_CAS02'},
                                  'cas03': {'$ref': '#/$elements/L2430_CAS03'},
                                  'cas04': {'$ref': '#/$elements/L2430_CAS04'},
                                  'cas05': {'$ref': '#/$elements/L2430_CAS05'},
                                  'cas06': {'$ref': '#/$elements/L2430_CAS06'},
                                  'cas07': {'$ref': '#/$elements/L2430_CAS07'},
                                  'cas08': {'$ref': '#/$elements/L2430_CAS08'},
                                  'cas09': {'$ref': '#/$elements/L2430_CAS09'},
                                  'cas10': {'$ref': '#/$elements/L2430_CAS10'},
                                  'cas11': {'$ref': '#/$elements/L2430_CAS11'},
                                  'cas12': {'$ref': '#/$elements/L2430_CAS12'},
                                  'cas13': {'$ref': '#/$elements/L2430_CAS13'},
                                  'cas14': {'$ref': '#/$elements/L2430_CAS14'},
                                  'cas15': {'$ref': '#/$elements/L2430_CAS15'},
                                  'cas16': {'$ref': '#/$elements/L2430_CAS16'},
                                  'cas17': {'$ref': '#/$elements/L2430_CAS17'},
                                  'cas18': {'$ref': '#/$elements/L2430_CAS18'},
                                  'cas19': {'$ref': '#/$elements/L2430_CAS19'}},
                   'required': ['cas01', 'cas02', 'cas03']},
         'maxItems': 99}
        segment_name = 'CAS'
    cas01: L2430_CAS01
    cas02: L2430_CAS02
    cas03: L2430_CAS03
    cas04: L2430_CAS04 | None
    cas05: L2430_CAS05 | None
    cas06: L2430_CAS06 | None
    cas07: L2430_CAS07 | None
    cas08: L2430_CAS08 | None
    cas09: L2430_CAS09 | None
    cas10: L2430_CAS10 | None
    cas11: L2430_CAS11 | None
    cas12: L2430_CAS12 | None
    cas13: L2430_CAS13 | None
    cas14: L2430_CAS14 | None
    cas15: L2430_CAS15 | None
    cas16: L2430_CAS16 | None
    cas17: L2430_CAS17 | None
    cas18: L2430_CAS18 | None
    cas19: L2430_CAS19 | None


class L2430_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['573']}]}}
        datatype = common.D_374
        codes = ['573']
        min_len = 3
        max_len = 3


class L2430_DTP02(Element):
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


class L2430_DTP03(Element):
    """Adjudication or Payment Date"""
    class Schema:
        json = {'title': 'Adjudication or Payment Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2430_DTP(Segment):
    """Line Adjudication Date"""
    class Schema:
        json = {'title': 'Line Adjudication Date',
         'usage': 'R',
         'description': 'xid=DTP name=Line Adjudication Date',
         'position': 550,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2430_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2430_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2430_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2430_DTP01
    dtp02: L2430_DTP02
    dtp03: L2430_DTP03


class L2430(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Line Adjudication Information',
                   'usage': 'S',
                   'description': 'xid=2430 name=Line Adjudication Information '
                                  'type=None',
                   'position': 540,
                   'type': 'object',
                   'properties': {'svd': {'$ref': '#/$segments/L2430_SVD'},
                                  'cas': {'$ref': '#/$segments/L2430_CAS'},
                                  'dtp': {'$ref': '#/$segments/L2430_DTP'}},
                   'required': ['svd', 'dtp']},
         'maxItems': 25}
    svd: L2430_SVD
    cas: list[L2430_CAS] | None
    dtp: L2430_DTP


class L2400(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Line Counter',
                   'usage': 'R',
                   'description': 'xid=2400 name=Line Counter type=None',
                   'position': 365,
                   'type': 'object',
                   'properties': {'lx': {'$ref': '#/$segments/L2400_LX'},
                                  'sv3': {'$ref': '#/$segments/L2400_SV3'},
                                  'too': {'$ref': '#/$segments/L2400_TOO'},
                                  'dtp': {'$ref': '#/$segments/L2400_DTP'},
                                  'qty': {'$ref': '#/$segments/L2400_QTY'},
                                  'ref': {'$ref': '#/$segments/L2400_REF'},
                                  'amt': {'$ref': '#/$segments/L2400_AMT'},
                                  'nte': {'$ref': '#/$segments/L2400_NTE'},
                                  'l2420a': {'$ref': '#/$segments/L2420A'},
                                  'l2420b': {'$ref': '#/$segments/L2420B'},
                                  'l2420c': {'$ref': '#/$segments/L2420C'},
                                  'l2430': {'$ref': '#/$segments/L2430'}},
                   'required': ['lx', 'sv3']},
         'maxItems': 50}
    lx: L2400_LX
    sv3: L2400_SV3
    too: list[L2400_TOO] | None
    dtp: L2400_DTP | None
    dtp: L2400_DTP | None
    dtp: L2400_DTP | None
    dtp: L2400_DTP | None
    qty: list[L2400_QTY] | None
    ref: L2400_REF | None
    ref: list[L2400_REF] | None
    ref: L2400_REF | None
    amt: L2400_AMT | None
    amt: L2400_AMT | None
    nte: list[L2400_NTE] | None
    l2420a: list[L2420A] | None
    l2420b: list[L2420B] | None
    l2420c: list[L2420C] | None
    l2430: list[L2430] | None


class L2300(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Information',
                   'usage': 'S',
                   'description': 'xid=2300 name=Claim Information type=None',
                   'position': 130,
                   'type': 'object',
                   'properties': {'clm': {'$ref': '#/$segments/L2300_CLM'},
                                  'dtp': {'$ref': '#/$segments/L2300_DTP'},
                                  'dn1': {'$ref': '#/$segments/L2300_DN1'},
                                  'dn2': {'$ref': '#/$segments/L2300_DN2'},
                                  'pwk': {'$ref': '#/$segments/L2300_PWK'},
                                  'amt': {'$ref': '#/$segments/L2300_AMT'},
                                  'ref': {'$ref': '#/$segments/L2300_REF'},
                                  'nte': {'$ref': '#/$segments/L2300_NTE'},
                                  'l2310a': {'$ref': '#/$segments/L2310A'},
                                  'l2310b': {'$ref': '#/$segments/L2310B'},
                                  'l2310c': {'$ref': '#/$segments/L2310C'},
                                  'l2310d': {'$ref': '#/$segments/L2310D'},
                                  'l2320': {'$ref': '#/$segments/L2320'},
                                  'l2400': {'$ref': '#/$segments/L2400'}},
                   'required': ['clm', 'l2400']},
         'maxItems': 100}
    clm: L2300_CLM
    dtp: L2300_DTP | None
    dtp: L2300_DTP | None
    dtp: L2300_DTP | None
    dtp: L2300_DTP | None
    dtp: list[L2300_DTP] | None
    dtp: L2300_DTP | None
    dn1: L2300_DN1 | None
    dn2: list[L2300_DN2] | None
    pwk: list[L2300_PWK] | None
    amt: L2300_AMT | None
    amt: L2300_AMT | None
    ref: list[L2300_REF] | None
    ref: L2300_REF | None
    ref: L2300_REF | None
    ref: list[L2300_REF] | None
    ref: L2300_REF | None
    nte: list[L2300_NTE] | None
    l2310a: list[L2310A] | None
    l2310b: list[L2310B] | None
    l2310c: list[L2310C] | None
    l2310d: list[L2310D] | None
    l2320: list[L2320] | None
    l2400: list[L2400]


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
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['23']}]}}
        datatype = common.D_735
        codes = ['23']
        min_len = 1
        max_len = 2


class L2000C_HL04(Element):
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


class L2000C_HL(Segment):
    """Patient Hierarchical Level"""
    class Schema:
        json = {'title': 'Patient Hierarchical Level',
         'usage': 'R',
         'description': 'xid=HL name=Patient Hierarchical Level',
         'position': 1,
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


class L2000C_PAT01(Element):
    """Patient's Relationship to Insured"""
    class Schema:
        json = {'title': "Patient's Relationship to Insured",
         'usage': 'R',
         'description': 'xid=PAT01 data_ele=1069',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1069'},
                            {'enum': ['01', '19', '20', '22', '29', '41', '53',
                                      '76']}]}}
        datatype = common.D_1069
        codes = ['01', '19', '20', '22', '29', '41', '53', '76']
        min_len = 2
        max_len = 2


class L2000C_PAT02(Element):
    """Patient Location Code"""
    class Schema:
        json = {'title': 'Patient Location Code',
         'usage': 'N',
         'description': 'xid=PAT02 data_ele=1384',
         'sequence': 2,
         'type': {'$ref': '#/$common/1384'}}
        datatype = common.D_1384
        min_len = 1
        max_len = 1


class L2000C_PAT03(Element):
    """Employment Status Code"""
    class Schema:
        json = {'title': 'Employment Status Code',
         'usage': 'N',
         'description': 'xid=PAT03 data_ele=584',
         'sequence': 3,
         'type': {'$ref': '#/$common/584'}}
        datatype = common.D_584
        min_len = 2
        max_len = 2


class L2000C_PAT04(Element):
    """Student Status Code"""
    class Schema:
        json = {'title': 'Student Status Code',
         'usage': 'S',
         'description': 'xid=PAT04 data_ele=1220',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1220'}, {'enum': ['F', 'N', 'P']}]}}
        datatype = common.D_1220
        codes = ['F', 'N', 'P']
        min_len = 1
        max_len = 1


class L2000C_PAT05(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=PAT05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2000C_PAT06(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=PAT06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000C_PAT07(Element):
    """Unit or Basis for Measurement Code"""
    class Schema:
        json = {'title': 'Unit or Basis for Measurement Code',
         'usage': 'N',
         'description': 'xid=PAT07 data_ele=355',
         'sequence': 7,
         'type': {'$ref': '#/$common/355'}}
        datatype = common.D_355
        min_len = 2
        max_len = 2


class L2000C_PAT08(Element):
    """Weight"""
    class Schema:
        json = {'title': 'Weight',
         'usage': 'N',
         'description': 'xid=PAT08 data_ele=81',
         'sequence': 8,
         'type': {'$ref': '#/$common/81'}}
        datatype = common.D_81
        min_len = 1
        max_len = 10


class L2000C_PAT09(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=PAT09 data_ele=1073',
         'sequence': 9,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2000C_PAT(Segment):
    """Patient Information"""
    class Schema:
        json = {'title': 'Patient Information',
         'usage': 'R',
         'description': 'xid=PAT name=Patient Information',
         'position': 7,
         'type': 'object',
         'properties': {'xid': {'literal': 'PAT'},
                        'pat01': {'$ref': '#/$elements/L2000C_PAT01'},
                        'pat04': {'$ref': '#/$elements/L2000C_PAT04'}},
         'required': ['pat01']}
        segment_name = 'PAT'
    pat01: L2000C_PAT01
    pat04: L2000C_PAT04 | None


class L2010CA_NM101(Element):
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


class L2010CA_NM104(Element):
    """Patient First Name"""
    class Schema:
        json = {'title': 'Patient First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2010CA_NM105(Element):
    """Patient Middle Name"""
    class Schema:
        json = {'title': 'Patient Middle Name',
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


class L2010CA_NM108(Element):
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


class L2010CA_NM109(Element):
    """Patient Primary Identifier"""
    class Schema:
        json = {'title': 'Patient Primary Identifier',
         'usage': 'S',
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
    """Patient Name"""
    class Schema:
        json = {'title': 'Patient Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Patient Name',
         'position': 15,
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
         'required': ['nm101', 'nm102', 'nm103', 'nm104']}
        segment_name = 'NM1'
    nm101: L2010CA_NM101
    nm102: L2010CA_NM102
    nm103: L2010CA_NM103
    nm104: L2010CA_NM104
    nm105: L2010CA_NM105 | None
    nm107: L2010CA_NM107 | None
    nm108: L2010CA_NM108 | None
    nm109: L2010CA_NM109 | None


class L2010CA_N301(Element):
    """Patient's Address 1"""
    class Schema:
        json = {'title': "Patient's Address 1",
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010CA_N302(Element):
    """Patient's Address 2"""
    class Schema:
        json = {'title': "Patient's Address 2",
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2010CA_N3(Segment):
    """Patient Address"""
    class Schema:
        json = {'title': 'Patient Address',
         'usage': 'R',
         'description': 'xid=N3 name=Patient Address',
         'position': 25,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2010CA_N301'},
                        'n302': {'$ref': '#/$elements/L2010CA_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2010CA_N301
    n302: L2010CA_N302 | None


class L2010CA_N401(Element):
    """Patient City Name"""
    class Schema:
        json = {'title': 'Patient City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2010CA_N402(Element):
    """Patient State Code"""
    class Schema:
        json = {'title': 'Patient State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2010CA_N403(Element):
    """Patient Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Patient Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2010CA_N404(Element):
    """Patient Country Code"""
    class Schema:
        json = {'title': 'Patient Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2010CA_N405(Element):
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


class L2010CA_N406(Element):
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


class L2010CA_N4(Segment):
    """Patient City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Patient City/State/ZIP Code',
         'usage': 'R',
         'description': 'xid=N4 name=Patient City/State/ZIP Code',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2010CA_N401'},
                        'n402': {'$ref': '#/$elements/L2010CA_N402'},
                        'n403': {'$ref': '#/$elements/L2010CA_N403'},
                        'n404': {'$ref': '#/$elements/L2010CA_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2010CA_N401
    n402: L2010CA_N402
    n403: L2010CA_N403
    n404: L2010CA_N404 | None


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
    """Patient Birth Date"""
    class Schema:
        json = {'title': 'Patient Birth Date',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2010CA_DMG03(Element):
    """Patient Gender Code"""
    class Schema:
        json = {'title': 'Patient Gender Code',
         'usage': 'R',
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
    """Patient Demographic Information"""
    class Schema:
        json = {'title': 'Patient Demographic Information',
         'usage': 'R',
         'description': 'xid=DMG name=Patient Demographic Information',
         'position': 32,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2010CA_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2010CA_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2010CA_DMG03'}},
         'required': ['dmg01', 'dmg02', 'dmg03']}
        segment_name = 'DMG'
    dmg01: L2010CA_DMG01
    dmg02: L2010CA_DMG02
    dmg03: L2010CA_DMG03


class L2010CA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1W', '23', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1W', '23', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2010CA_REF02(Element):
    """Patient Secondary Identifier"""
    class Schema:
        json = {'title': 'Patient Secondary Identifier',
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
    """Patient Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Patient Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Patient Secondary Identification',
                   'position': 35,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2010CA_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2010CA_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2010CA_REF01
    ref02: L2010CA_REF02


class L2010CA_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['Y4']}]}}
        datatype = common.D_128
        codes = ['Y4']
        min_len = 2
        max_len = 3


class L2010CA_REF02(Element):
    """Property Casualty Claim Number"""
    class Schema:
        json = {'title': 'Property Casualty Claim Number',
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
    """Property and Casualty Claim Number"""
    class Schema:
        json = {'title': 'Property and Casualty Claim Number',
         'usage': 'S',
         'description': 'xid=REF name=Property and Casualty Claim Number',
         'position': 35,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2010CA_REF01'},
                        'ref02': {'$ref': '#/$elements/L2010CA_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2010CA_REF01
    ref02: L2010CA_REF02


class L2010CA(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Patient Name',
                   'usage': 'R',
                   'description': 'xid=2010CA name=Patient Name type=None',
                   'position': 15,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2010CA_NM1'},
                                  'n3': {'$ref': '#/$segments/L2010CA_N3'},
                                  'n4': {'$ref': '#/$segments/L2010CA_N4'},
                                  'dmg': {'$ref': '#/$segments/L2010CA_DMG'},
                                  'ref': {'$ref': '#/$segments/L2010CA_REF'}},
                   'required': ['nm1', 'n3', 'n4', 'dmg']},
         'maxItems': 1}
    nm1: L2010CA_NM1
    n3: L2010CA_N3
    n4: L2010CA_N4
    dmg: L2010CA_DMG
    ref: list[L2010CA_REF] | None
    ref: L2010CA_REF | None


class L2300_CLM01(Element):
    """Patient Account Number"""
    class Schema:
        json = {'title': 'Patient Account Number',
         'usage': 'R',
         'description': 'xid=CLM01 data_ele=1028',
         'sequence': 1,
         'type': {'$ref': '#/$common/1028'}}
        datatype = common.D_1028
        min_len = 1
        max_len = 38


class L2300_CLM02(Element):
    """Total Claim Charge Amount"""
    class Schema:
        json = {'title': 'Total Claim Charge Amount',
         'usage': 'R',
         'description': 'xid=CLM02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300_CLM03(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'N',
         'description': 'xid=CLM03 data_ele=1032',
         'sequence': 3,
         'type': {'$ref': '#/$common/1032'}}
        datatype = common.D_1032
        min_len = 1
        max_len = 2


class L2300_CLM04(Element):
    """Non-Institutional Claim Type Code"""
    class Schema:
        json = {'title': 'Non-Institutional Claim Type Code',
         'usage': 'N',
         'description': 'xid=CLM04 data_ele=1343',
         'sequence': 4,
         'type': {'$ref': '#/$common/1343'}}
        datatype = common.D_1343
        min_len = 1
        max_len = 2


class L2300_CLM05_01(Element):
    """Facility Type Code"""
    class Schema:
        json = {'title': 'Facility Type Code',
         'usage': 'R',
         'description': 'xid=CLM05-01 data_ele=1331',
         'sequence': 1,
         'type': {'$ref': '#/$common/1331'}}
        datatype = common.D_1331
        codes = common.pos
        min_len = 1
        max_len = 2


class L2300_CLM05_02(Element):
    """Facility Code Qualifier"""
    class Schema:
        json = {'title': 'Facility Code Qualifier',
         'usage': 'N',
         'description': 'xid=CLM05-02 data_ele=1332',
         'sequence': 2,
         'type': {'$ref': '#/$common/1332'}}
        datatype = common.D_1332
        min_len = 1
        max_len = 2


class L2300_CLM05_03(Element):
    """Claim Submission Reason Code"""
    class Schema:
        json = {'title': 'Claim Submission Reason Code',
         'usage': 'R',
         'description': 'xid=CLM05-03 data_ele=1325',
         'sequence': 3,
         'type': {'$ref': '#/$common/1325'}}
        datatype = common.D_1325
        min_len = 1
        max_len = 1


class L2300_C023(Composite):
    class Schema:
        json = {'title': 'Place of Service Code',
         'usage': 'R',
         'description': 'xid=None name=Place of Service Code refdes= data_ele=C023',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'clm05_01': {'title': 'Facility Type Code',
                                     'usage': 'R',
                                     'description': 'xid=CLM05-01 data_ele=1331',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/1331'}},
                        'clm05_02': {'title': 'Facility Code Qualifier',
                                     'usage': 'N',
                                     'description': 'xid=CLM05-02 data_ele=1332',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/1332'}},
                        'clm05_03': {'title': 'Claim Submission Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=CLM05-03 data_ele=1325',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1325'}}},
         'required': ['clm05_01', 'clm05_03']}
    clm05_01: L2300_CLM05_01
    clm05_03: L2300_CLM05_03


class L2300_CLM06(Element):
    """Provider or Supplier Signature Indicator"""
    class Schema:
        json = {'title': 'Provider or Supplier Signature Indicator',
         'usage': 'R',
         'description': 'xid=CLM06 data_ele=1073',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2300_CLM07(Element):
    """Medicare Assignment Code"""
    class Schema:
        json = {'title': 'Medicare Assignment Code',
         'usage': 'S',
         'description': 'xid=CLM07 data_ele=1359',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/1359'}, {'enum': ['A', 'C', 'P']}]}}
        datatype = common.D_1359
        codes = ['A', 'C', 'P']
        min_len = 1
        max_len = 1


class L2300_CLM08(Element):
    """Benefits Assignment Certification Indicator"""
    class Schema:
        json = {'title': 'Benefits Assignment Certification Indicator',
         'usage': 'R',
         'description': 'xid=CLM08 data_ele=1073',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2300_CLM09(Element):
    """Release of Information Code"""
    class Schema:
        json = {'title': 'Release of Information Code',
         'usage': 'R',
         'description': 'xid=CLM09 data_ele=1363',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/1363'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1363
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2300_CLM10(Element):
    """Patient Signature Source Code"""
    class Schema:
        json = {'title': 'Patient Signature Source Code',
         'usage': 'N',
         'description': 'xid=CLM10 data_ele=1351',
         'sequence': 10,
         'type': {'$ref': '#/$common/1351'}}
        datatype = common.D_1351
        min_len = 1
        max_len = 1


class L2300_CLM11_01(Element):
    """Related Causes Code"""
    class Schema:
        json = {'title': 'Related Causes Code',
         'usage': 'R',
         'description': 'xid=CLM11-01 data_ele=1362',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1362'}, {'enum': ['AA', 'EM', 'OA']}]}}
        datatype = common.D_1362
        codes = ['AA', 'EM', 'OA']
        min_len = 2
        max_len = 3


class L2300_CLM11_02(Element):
    """Related Causes Code"""
    class Schema:
        json = {'title': 'Related Causes Code',
         'usage': 'S',
         'description': 'xid=CLM11-02 data_ele=1362',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1362'}, {'enum': ['AA', 'EM', 'OA']}]}}
        datatype = common.D_1362
        codes = ['AA', 'EM', 'OA']
        min_len = 2
        max_len = 3


class L2300_CLM11_03(Element):
    """Related Causes Code"""
    class Schema:
        json = {'title': 'Related Causes Code',
         'usage': 'S',
         'description': 'xid=CLM11-03 data_ele=1362',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1362'}, {'enum': ['AA', 'EM', 'OA']}]}}
        datatype = common.D_1362
        codes = ['AA', 'EM', 'OA']
        min_len = 2
        max_len = 3


class L2300_CLM11_04(Element):
    """Auto Accident State or Province Code"""
    class Schema:
        json = {'title': 'Auto Accident State or Province Code',
         'usage': 'S',
         'description': 'xid=CLM11-04 data_ele=156',
         'sequence': 4,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2300_CLM11_05(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'S',
         'description': 'xid=CLM11-05 data_ele=26',
         'sequence': 5,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2300_C024(Composite):
    class Schema:
        json = {'title': 'Related Causes Information',
         'usage': 'S',
         'description': 'xid=None name=Related Causes Information refdes= '
                        'data_ele=C024',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'clm11_01': {'title': 'Related Causes Code',
                                     'usage': 'R',
                                     'description': 'xid=CLM11-01 data_ele=1362',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1362'},
                                                        {'enum': ['AA', 'EM', 'OA']}]}},
                        'clm11_02': {'title': 'Related Causes Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-02 data_ele=1362',
                                     'sequence': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1362'},
                                                        {'enum': ['AA', 'EM', 'OA']}]}},
                        'clm11_03': {'title': 'Related Causes Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-03 data_ele=1362',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/1362'},
                                                        {'enum': ['AA', 'EM', 'OA']}]}},
                        'clm11_04': {'title': 'Auto Accident State or Province Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-04 data_ele=156',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/156'}},
                        'clm11_05': {'title': 'Country Code',
                                     'usage': 'S',
                                     'description': 'xid=CLM11-05 data_ele=26',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/26'}}},
         'required': ['clm11_01']}
    clm11_01: L2300_CLM11_01
    clm11_02: L2300_CLM11_02 | None
    clm11_03: L2300_CLM11_03 | None
    clm11_04: L2300_CLM11_04 | None
    clm11_05: L2300_CLM11_05 | None


class L2300_CLM12(Element):
    """Special Program Indicator"""
    class Schema:
        json = {'title': 'Special Program Indicator',
         'usage': 'S',
         'description': 'xid=CLM12 data_ele=1366',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/1366'},
                            {'enum': ['01', '02', '03', '05']}]}}
        datatype = common.D_1366
        codes = ['01', '02', '03', '05']
        min_len = 2
        max_len = 3


class L2300_CLM13(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CLM13 data_ele=1073',
         'sequence': 13,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_CLM14(Element):
    """Level of Service Code"""
    class Schema:
        json = {'title': 'Level of Service Code',
         'usage': 'N',
         'description': 'xid=CLM14 data_ele=1338',
         'sequence': 14,
         'type': {'$ref': '#/$common/1338'}}
        datatype = common.D_1338
        min_len = 1
        max_len = 3


class L2300_CLM15(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CLM15 data_ele=1073',
         'sequence': 15,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_CLM16(Element):
    """Provider Agreement Code"""
    class Schema:
        json = {'title': 'Provider Agreement Code',
         'usage': 'N',
         'description': 'xid=CLM16 data_ele=1360',
         'sequence': 16,
         'type': {'$ref': '#/$common/1360'}}
        datatype = common.D_1360
        min_len = 1
        max_len = 1


class L2300_CLM17(Element):
    """Claim Status Code"""
    class Schema:
        json = {'title': 'Claim Status Code',
         'usage': 'N',
         'description': 'xid=CLM17 data_ele=1029',
         'sequence': 17,
         'type': {'$ref': '#/$common/1029'}}
        datatype = common.D_1029
        min_len = 1
        max_len = 2


class L2300_CLM18(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CLM18 data_ele=1073',
         'sequence': 18,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_CLM19(Element):
    """Predetermination of Benefits Code"""
    class Schema:
        json = {'title': 'Predetermination of Benefits Code',
         'usage': 'S',
         'description': 'xid=CLM19 data_ele=1383',
         'sequence': 19,
         'type': {'allOf': [{'$ref': '#/$common/1383'}, {'enum': ['PB']}]}}
        datatype = common.D_1383
        codes = ['PB']
        min_len = 2
        max_len = 2


class L2300_CLM20(Element):
    """Delay Reason Code"""
    class Schema:
        json = {'title': 'Delay Reason Code',
         'usage': 'S',
         'description': 'xid=CLM20 data_ele=1514',
         'sequence': 20,
         'type': {'allOf': [{'$ref': '#/$common/1514'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                      '11']}]}}
        datatype = common.D_1514
        codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        min_len = 1
        max_len = 2


class L2300_CLM(Segment):
    """Claim Information"""
    class Schema:
        json = {'title': 'Claim Information',
         'usage': 'R',
         'description': 'xid=CLM name=Claim Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'CLM'},
                        'clm01': {'$ref': '#/$elements/L2300_CLM01'},
                        'clm02': {'$ref': '#/$elements/L2300_CLM02'},
                        'c023': {'$ref': '#/$elements/L2300_C023'},
                        'clm06': {'$ref': '#/$elements/L2300_CLM06'},
                        'clm07': {'$ref': '#/$elements/L2300_CLM07'},
                        'clm08': {'$ref': '#/$elements/L2300_CLM08'},
                        'clm09': {'$ref': '#/$elements/L2300_CLM09'},
                        'c024': {'$ref': '#/$elements/L2300_C024'},
                        'clm12': {'$ref': '#/$elements/L2300_CLM12'},
                        'clm19': {'$ref': '#/$elements/L2300_CLM19'},
                        'clm20': {'$ref': '#/$elements/L2300_CLM20'}},
         'required': ['clm01', 'clm02', 'c023', 'clm06', 'clm08', 'clm09']}
        segment_name = 'CLM'
    clm01: L2300_CLM01
    clm02: L2300_CLM02
    c023: L2300_C023
    clm06: L2300_CLM06
    clm07: L2300_CLM07 | None
    clm08: L2300_CLM08
    clm09: L2300_CLM09
    c024: L2300_C024 | None
    clm12: L2300_CLM12 | None
    clm19: L2300_CLM19 | None
    clm20: L2300_CLM20 | None


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Related Hospitalization Admission Date"""
    class Schema:
        json = {'title': 'Related Hospitalization Admission Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Admission"""
    class Schema:
        json = {'title': 'Date - Admission',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Admission',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Discharge or End Of Care Date"""
    class Schema:
        json = {'title': 'Discharge or End Of Care Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Discharge"""
    class Schema:
        json = {'title': 'Date - Discharge',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Discharge',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['330']}]}}
        datatype = common.D_374
        codes = ['330']
        min_len = 3
        max_len = 3


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Referral Date"""
    class Schema:
        json = {'title': 'Referral Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Referral"""
    class Schema:
        json = {'title': 'Date - Referral',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Referral',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
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


class L2300_DTP(Segment):
    """Date - Accident"""
    class Schema:
        json = {'title': 'Date - Accident',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Accident',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['452']}]}}
        datatype = common.D_374
        codes = ['452']
        min_len = 3
        max_len = 3


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Orthodontic Banding Date"""
    class Schema:
        json = {'title': 'Orthodontic Banding Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Appliance Placement"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Date - Appliance Placement',
                   'usage': 'S',
                   'description': 'xid=DTP name=Date - Appliance Placement',
                   'position': 135,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 5}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DTP01(Element):
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


class L2300_DTP02(Element):
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


class L2300_DTP03(Element):
    """Service Date"""
    class Schema:
        json = {'title': 'Service Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Date - Service"""
    class Schema:
        json = {'title': 'Date - Service',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Service',
         'position': 135,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_DN101(Element):
    """Orthodontic Treatment Months Count"""
    class Schema:
        json = {'title': 'Orthodontic Treatment Months Count',
         'usage': 'S',
         'description': 'xid=DN101 data_ele=380',
         'sequence': 1,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_DN102(Element):
    """Orthodontic Treatment Months Remaining Count"""
    class Schema:
        json = {'title': 'Orthodontic Treatment Months Remaining Count',
         'usage': 'S',
         'description': 'xid=DN102 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_DN103(Element):
    """Question Response"""
    class Schema:
        json = {'title': 'Question Response',
         'usage': 'S',
         'description': 'xid=DN103 data_ele=1073',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['Y']}]}}
        datatype = common.D_1073
        codes = ['Y']
        min_len = 1
        max_len = 1


class L2300_DN104(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=DN104 data_ele=352',
         'sequence': 4,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_DN1(Segment):
    """Orthodontic Total Months of Treatment"""
    class Schema:
        json = {'title': 'Orthodontic Total Months of Treatment',
         'usage': 'S',
         'description': 'xid=DN1 name=Orthodontic Total Months of Treatment',
         'position': 145,
         'type': 'object',
         'properties': {'xid': {'literal': 'DN1'},
                        'dn101': {'$ref': '#/$elements/L2300_DN101'},
                        'dn102': {'$ref': '#/$elements/L2300_DN102'},
                        'dn103': {'$ref': '#/$elements/L2300_DN103'}}}
        segment_name = 'DN1'
    dn101: L2300_DN101 | None
    dn102: L2300_DN102 | None
    dn103: L2300_DN103 | None


class L2300_DN201(Element):
    """Tooth Number"""
    class Schema:
        json = {'title': 'Tooth Number',
         'usage': 'R',
         'description': 'xid=DN201 data_ele=127',
         'sequence': 1,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_DN202(Element):
    """Tooth Status Code"""
    class Schema:
        json = {'title': 'Tooth Status Code',
         'usage': 'R',
         'description': 'xid=DN202 data_ele=1368',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1368'}, {'enum': ['E', 'I', 'M']}]}}
        datatype = common.D_1368
        codes = ['E', 'I', 'M']
        min_len = 1
        max_len = 2


class L2300_DN203(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=DN203 data_ele=380',
         'sequence': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_DN204(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=DN204 data_ele=1250',
         'sequence': 4,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2300_DN205(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=DN205 data_ele=1251',
         'sequence': 5,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DN2(Segment):
    """Tooth Status"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Tooth Status',
                   'usage': 'S',
                   'description': 'xid=DN2 name=Tooth Status',
                   'position': 150,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DN2'},
                                  'dn201': {'$ref': '#/$elements/L2300_DN201'},
                                  'dn202': {'$ref': '#/$elements/L2300_DN202'}},
                   'required': ['dn201', 'dn202']},
         'maxItems': 35}
        segment_name = 'DN2'
    dn201: L2300_DN201
    dn202: L2300_DN202


class L2300_PWK01(Element):
    """Attachment Report Type Code"""
    class Schema:
        json = {'title': 'Attachment Report Type Code',
         'usage': 'R',
         'description': 'xid=PWK01 data_ele=755',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/755'},
                            {'enum': ['B4', 'DA', 'DG', 'EB', 'OB', 'OZ', 'P6', 'RB',
                                      'RR']}]}}
        datatype = common.D_755
        codes = ['B4', 'DA', 'DG', 'EB', 'OB', 'OZ', 'P6', 'RB', 'RR']
        min_len = 2
        max_len = 2


class L2300_PWK02(Element):
    """Attachment Transmission Code"""
    class Schema:
        json = {'title': 'Attachment Transmission Code',
         'usage': 'R',
         'description': 'xid=PWK02 data_ele=756',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/756'},
                            {'enum': ['AA', 'BM', 'EL', 'EM', 'FX']}]}}
        datatype = common.D_756
        codes = ['AA', 'BM', 'EL', 'EM', 'FX']
        min_len = 1
        max_len = 2


class L2300_PWK03(Element):
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


class L2300_PWK04(Element):
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


class L2300_PWK05(Element):
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


class L2300_PWK06(Element):
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


class L2300_PWK07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=PWK07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_C002(Composite):
    class Schema:
        json = {'title': 'Actions Indicated',
         'usage': 'N',
         'description': 'xid=None name=Actions Indicated refdes= data_ele=C002',
         'sequence': 8,
         'syntax': []}


class L2300_PWK09(Element):
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


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Supplemental Information',
                   'usage': 'S',
                   'description': 'xid=PWK name=Claim Supplemental Information',
                   'position': 155,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PWK'},
                                  'pwk01': {'$ref': '#/$elements/L2300_PWK01'},
                                  'pwk02': {'$ref': '#/$elements/L2300_PWK02'},
                                  'pwk05': {'$ref': '#/$elements/L2300_PWK05'},
                                  'pwk06': {'$ref': '#/$elements/L2300_PWK06'}},
                   'required': ['pwk01', 'pwk02']},
         'maxItems': 10}
        segment_name = 'PWK'
    pwk01: L2300_PWK01
    pwk02: L2300_PWK02
    pwk05: L2300_PWK05 | None
    pwk06: L2300_PWK06 | None


class L2300_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['F5']}]}}
        datatype = common.D_522
        codes = ['F5']
        min_len = 1
        max_len = 3


class L2300_AMT02(Element):
    """Patient Amount Paid"""
    class Schema:
        json = {'title': 'Patient Amount Paid',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300_AMT03(Element):
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


class L2300_AMT(Segment):
    """Patient Amount Paid"""
    class Schema:
        json = {'title': 'Patient Amount Paid',
         'usage': 'S',
         'description': 'xid=AMT name=Patient Amount Paid',
         'position': 175,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2300_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2300_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2300_AMT01
    amt02: L2300_AMT02


class L2300_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['MA']}]}}
        datatype = common.D_522
        codes = ['MA']
        min_len = 1
        max_len = 3


class L2300_AMT02(Element):
    """Credit or Debit Card Maximum Amount"""
    class Schema:
        json = {'title': 'Credit or Debit Card Maximum Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2300_AMT03(Element):
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


class L2300_AMT(Segment):
    """Credit/Debit Card - Maximum Amount"""
    class Schema:
        json = {'title': 'Credit/Debit Card - Maximum Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Credit/Debit Card - Maximum Amount',
         'position': 175,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2300_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2300_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2300_AMT01
    amt02: L2300_AMT02


class L2300_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['G3']}]}}
        datatype = common.D_128
        codes = ['G3']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """Predetermination of Benefits Identifier"""
    class Schema:
        json = {'title': 'Predetermination of Benefits Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Predetermination Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Predetermination Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Predetermination Identification',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['4N']}]}}
        datatype = common.D_128
        codes = ['4N']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """Service Authorization Exception Code"""
    class Schema:
        json = {'title': 'Service Authorization Exception Code',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/127'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7']}]}}
        datatype = common.D_127
        codes = ['1', '2', '3', '4', '5', '6', '7']
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Service Authorization Exception Code"""
    class Schema:
        json = {'title': 'Service Authorization Exception Code',
         'usage': 'S',
         'description': 'xid=REF name=Service Authorization Exception Code',
         'position': 180,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2300_REF01'},
                        'ref02': {'$ref': '#/$elements/L2300_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['F8']}]}}
        datatype = common.D_128
        codes = ['F8']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """Claim Original Reference Number"""
    class Schema:
        json = {'title': 'Claim Original Reference Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Original Reference Number (ICN/DCN)"""
    class Schema:
        json = {'title': 'Original Reference Number (ICN/DCN)',
         'usage': 'S',
         'description': 'xid=REF name=Original Reference Number (ICN/DCN)',
         'position': 180,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2300_REF01'},
                        'ref02': {'$ref': '#/$elements/L2300_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
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


class L2300_REF02(Element):
    """Referral Number"""
    class Schema:
        json = {'title': 'Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Prior Authorization or Referral Number',
                   'position': 180,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_REF01(Element):
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


class L2300_REF02(Element):
    """Value Added Network Trace Number"""
    class Schema:
        json = {'title': 'Value Added Network Trace Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2300_REF03(Element):
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


class L2300_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2300_REF(Segment):
    """Claim Identification Number for Clearinghouses and Other Transmission Intermediaries"""
    class Schema:
        json = {'title': 'Claim Identification Number for Clearinghouses and Other '
                  'Transmission Intermediaries',
         'usage': 'S',
         'description': 'xid=REF name=Claim Identification Number for Clearinghouses '
                        'and Other Transmission Intermediaries',
         'position': 180,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2300_REF01'},
                        'ref02': {'$ref': '#/$elements/L2300_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_NTE01(Element):
    """Note Reference Code"""
    class Schema:
        json = {'title': 'Note Reference Code',
         'usage': 'R',
         'description': 'xid=NTE01 data_ele=363',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/363'}, {'enum': ['ADD']}]}}
        datatype = common.D_363
        codes = ['ADD']
        min_len = 3
        max_len = 3


class L2300_NTE02(Element):
    """Claim Note Text"""
    class Schema:
        json = {'title': 'Claim Note Text',
         'usage': 'R',
         'description': 'xid=NTE02 data_ele=352',
         'sequence': 2,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2300_NTE(Segment):
    """Claim Note"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Note',
                   'usage': 'S',
                   'description': 'xid=NTE name=Claim Note',
                   'position': 190,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'NTE'},
                                  'nte01': {'$ref': '#/$elements/L2300_NTE01'},
                                  'nte02': {'$ref': '#/$elements/L2300_NTE02'}},
                   'required': ['nte01', 'nte02']},
         'maxItems': 20}
        segment_name = 'NTE'
    nte01: L2300_NTE01
    nte02: L2300_NTE02


class L2310A_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DN', 'P3']}]}}
        datatype = common.D_98
        codes = ['DN', 'P3']
        min_len = 2
        max_len = 3


class L2310A_NM102(Element):
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


class L2310A_NM103(Element):
    """Referring Provider Last Name"""
    class Schema:
        json = {'title': 'Referring Provider Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310A_NM104(Element):
    """Referring Provider First Name"""
    class Schema:
        json = {'title': 'Referring Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2310A_NM105(Element):
    """Referring Provider Middle Name"""
    class Schema:
        json = {'title': 'Referring Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2310A_NM106(Element):
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


class L2310A_NM107(Element):
    """Referring Provider Name Suffix"""
    class Schema:
        json = {'title': 'Referring Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2310A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310A_NM109(Element):
    """Referring Provider Identifier"""
    class Schema:
        json = {'title': 'Referring Provider Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310A_NM110(Element):
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


class L2310A_NM111(Element):
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


class L2310A_NM1(Segment):
    """Referring Provider Name"""
    class Schema:
        json = {'title': 'Referring Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Referring Provider Name',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2310A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2310A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2310A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2310A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2310A_NM101
    nm102: L2310A_NM102
    nm103: L2310A_NM103
    nm104: L2310A_NM104 | None
    nm105: L2310A_NM105 | None
    nm107: L2310A_NM107 | None
    nm108: L2310A_NM108 | None
    nm109: L2310A_NM109 | None


class L2310A_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['RF']}]}}
        datatype = common.D_1221
        codes = ['RF']
        min_len = 1
        max_len = 3


class L2310A_PRV02(Element):
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


class L2310A_PRV03(Element):
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


class L2310A_PRV04(Element):
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


class L2310A_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2310A_PRV06(Element):
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


class L2310A_PRV(Segment):
    """Referring Provider Specialty Information"""
    class Schema:
        json = {'title': 'Referring Provider Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Referring Provider Specialty Information',
         'position': 255,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2310A_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2310A_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2310A_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2310A_PRV01
    prv02: L2310A_PRV02
    prv03: L2310A_PRV03


class L2310A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2310A_REF02(Element):
    """Referring Provider Secondary Identifier"""
    class Schema:
        json = {'title': 'Referring Provider Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310A_REF03(Element):
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


class L2310A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310A_REF(Segment):
    """Referring Provider Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Referring Provider Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Referring Provider Secondary '
                                  'Identification',
                   'position': 271,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2310A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2310A_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2310A_REF01
    ref02: L2310A_REF02


class L2310A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Referring Provider Name',
                   'usage': 'S',
                   'description': 'xid=2310A name=Referring Provider Name type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310A_NM1'},
                                  'prv': {'$ref': '#/$segments/L2310A_PRV'},
                                  'ref': {'$ref': '#/$segments/L2310A_REF'}},
                   'required': ['nm1']},
         'maxItems': 2}
    nm1: L2310A_NM1
    prv: L2310A_PRV | None
    ref: list[L2310A_REF] | None


class L2310B_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['82']}]}}
        datatype = common.D_98
        codes = ['82']
        min_len = 2
        max_len = 3


class L2310B_NM102(Element):
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


class L2310B_NM103(Element):
    """Rendering Provider Last or Organization Name"""
    class Schema:
        json = {'title': 'Rendering Provider Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310B_NM104(Element):
    """Rendering Provider First Name"""
    class Schema:
        json = {'title': 'Rendering Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2310B_NM105(Element):
    """Rendering Provider Middle Name"""
    class Schema:
        json = {'title': 'Rendering Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2310B_NM106(Element):
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


class L2310B_NM107(Element):
    """Rendering Provider Name Suffix"""
    class Schema:
        json = {'title': 'Rendering Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2310B_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310B_NM109(Element):
    """Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310B_NM110(Element):
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


class L2310B_NM111(Element):
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


class L2310B_NM1(Segment):
    """Rendering Provider Name"""
    class Schema:
        json = {'title': 'Rendering Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Rendering Provider Name',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310B_NM103'},
                        'nm104': {'$ref': '#/$elements/L2310B_NM104'},
                        'nm105': {'$ref': '#/$elements/L2310B_NM105'},
                        'nm107': {'$ref': '#/$elements/L2310B_NM107'},
                        'nm108': {'$ref': '#/$elements/L2310B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310B_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2310B_NM101
    nm102: L2310B_NM102
    nm103: L2310B_NM103
    nm104: L2310B_NM104 | None
    nm105: L2310B_NM105 | None
    nm107: L2310B_NM107 | None
    nm108: L2310B_NM108
    nm109: L2310B_NM109


class L2310B_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['PE']}]}}
        datatype = common.D_1221
        codes = ['PE']
        min_len = 1
        max_len = 3


class L2310B_PRV02(Element):
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


class L2310B_PRV03(Element):
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


class L2310B_PRV04(Element):
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


class L2310B_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2310B_PRV06(Element):
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


class L2310B_PRV(Segment):
    """Rendering Provider Specialty Information"""
    class Schema:
        json = {'title': 'Rendering Provider Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Rendering Provider Specialty Information',
         'position': 255,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2310B_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2310B_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2310B_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2310B_PRV01
    prv02: L2310B_PRV02
    prv03: L2310B_PRV03


class L2310B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2310B_REF02(Element):
    """Rendering Provider Secondary Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310B_REF03(Element):
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


class L2310B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310B_REF(Segment):
    """Rendering Provider Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Secondary '
                                  'Identification',
                   'position': 271,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2310B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2310B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2310B_REF01
    ref02: L2310B_REF02


class L2310B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Name',
                   'usage': 'S',
                   'description': 'xid=2310B name=Rendering Provider Name type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310B_NM1'},
                                  'prv': {'$ref': '#/$segments/L2310B_PRV'},
                                  'ref': {'$ref': '#/$segments/L2310B_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2310B_NM1
    prv: L2310B_PRV | None
    ref: list[L2310B_REF] | None


class L2310C_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['FA']}]}}
        datatype = common.D_98
        codes = ['FA']
        min_len = 2
        max_len = 3


class L2310C_NM102(Element):
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


class L2310C_NM103(Element):
    """Laboratory or Facility Name"""
    class Schema:
        json = {'title': 'Laboratory or Facility Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310C_NM104(Element):
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


class L2310C_NM105(Element):
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


class L2310C_NM106(Element):
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


class L2310C_NM107(Element):
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


class L2310C_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310C_NM109(Element):
    """Laboratory or Facility Primary Identifier"""
    class Schema:
        json = {'title': 'Laboratory or Facility Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310C_NM110(Element):
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


class L2310C_NM111(Element):
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


class L2310C_NM1(Segment):
    """Service Facility Location"""
    class Schema:
        json = {'title': 'Service Facility Location',
         'usage': 'R',
         'description': 'xid=NM1 name=Service Facility Location',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310C_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310C_NM103'},
                        'nm108': {'$ref': '#/$elements/L2310C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310C_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2310C_NM101
    nm102: L2310C_NM102
    nm103: L2310C_NM103
    nm108: L2310C_NM108
    nm109: L2310C_NM109


class L2310C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'G2',
                                      'LU', 'TJ', 'X4', 'X5']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5']
        min_len = 2
        max_len = 3


class L2310C_REF02(Element):
    """Laboratory or Facility Secondary Identifier"""
    class Schema:
        json = {'title': 'Laboratory or Facility Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310C_REF03(Element):
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


class L2310C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Facility Location Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Service Facility Location Secondary '
                                  'Identification',
                   'position': 271,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2310C_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2310C_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2310C_REF01
    ref02: L2310C_REF02


class L2310C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Facility Location',
                   'usage': 'S',
                   'description': 'xid=2310C name=Service Facility Location type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310C_NM1'},
                                  'ref': {'$ref': '#/$segments/L2310C_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2310C_NM1
    ref: list[L2310C_REF] | None


class L2310D_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DD']}]}}
        datatype = common.D_98
        codes = ['DD']
        min_len = 2
        max_len = 3


class L2310D_NM102(Element):
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


class L2310D_NM103(Element):
    """Assistant Last or Organazation Name"""
    class Schema:
        json = {'title': 'Assistant Last or Organazation Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2310D_NM104(Element):
    """Assistant Surgeon First Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2310D_NM105(Element):
    """Assistant Surgeon Middle Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2310D_NM106(Element):
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


class L2310D_NM107(Element):
    """Assistant Surgeon Name Suffix"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2310D_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2310D_NM109(Element):
    """Assistant Surgeon Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310D_NM110(Element):
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


class L2310D_NM111(Element):
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


class L2310D_NM1(Segment):
    """Assistant Surgeon Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Assistant Surgeon Name',
         'position': 250,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2310D_NM101'},
                        'nm102': {'$ref': '#/$elements/L2310D_NM102'},
                        'nm103': {'$ref': '#/$elements/L2310D_NM103'},
                        'nm104': {'$ref': '#/$elements/L2310D_NM104'},
                        'nm105': {'$ref': '#/$elements/L2310D_NM105'},
                        'nm107': {'$ref': '#/$elements/L2310D_NM107'},
                        'nm108': {'$ref': '#/$elements/L2310D_NM108'},
                        'nm109': {'$ref': '#/$elements/L2310D_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2310D_NM101
    nm102: L2310D_NM102
    nm103: L2310D_NM103
    nm104: L2310D_NM104 | None
    nm105: L2310D_NM105 | None
    nm107: L2310D_NM107 | None
    nm108: L2310D_NM108
    nm109: L2310D_NM109


class L2310D_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['AS']}]}}
        datatype = common.D_1221
        codes = ['AS']
        min_len = 1
        max_len = 3


class L2310D_PRV02(Element):
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


class L2310D_PRV03(Element):
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


class L2310D_PRV04(Element):
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


class L2310D_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2310D_PRV06(Element):
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


class L2310D_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    class Schema:
        json = {'title': 'Assistant Surgeon Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Assistant Surgeon Specialty Information',
         'position': 255,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2310D_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2310D_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2310D_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2310D_PRV01
    prv02: L2310D_PRV02
    prv03: L2310D_PRV03


class L2310D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'G2',
                                      'LU', 'TJ', 'X4', 'X5']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5']
        min_len = 2
        max_len = 3


class L2310D_REF02(Element):
    """Assistant Surgeon Secondary Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2310D_REF03(Element):
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


class L2310D_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2310D_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identification',
         'usage': 'S',
         'description': 'xid=REF name=Assistant Surgeon Secondary Identification',
         'position': 271,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2310D_REF01'},
                        'ref02': {'$ref': '#/$elements/L2310D_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2310D_REF01
    ref02: L2310D_REF02


class L2310D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Assistant Surgeon Name',
                   'usage': 'S',
                   'description': 'xid=2310D name=Assistant Surgeon Name type=None',
                   'position': 250,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2310D_NM1'},
                                  'prv': {'$ref': '#/$segments/L2310D_PRV'},
                                  'ref': {'$ref': '#/$segments/L2310D_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2310D_NM1
    prv: L2310D_PRV | None
    ref: L2310D_REF | None


class L2320_SBR01(Element):
    """Payer Responsibility Sequence Number Code"""
    class Schema:
        json = {'title': 'Payer Responsibility Sequence Number Code',
         'usage': 'R',
         'description': 'xid=SBR01 data_ele=1138',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1138'}, {'enum': ['P', 'S', 'T']}]}}
        datatype = common.D_1138
        codes = ['P', 'S', 'T']
        min_len = 1
        max_len = 1


class L2320_SBR02(Element):
    """Individual Relationship Code"""
    class Schema:
        json = {'title': 'Individual Relationship Code',
         'usage': 'R',
         'description': 'xid=SBR02 data_ele=1069',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'},
                            {'enum': ['01', '18', '19', '20', '21', '22', '29',
                                      '76']}]}}
        datatype = common.D_1069
        codes = ['01', '18', '19', '20', '21', '22', '29', '76']
        min_len = 2
        max_len = 2


class L2320_SBR03(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
         'usage': 'S',
         'description': 'xid=SBR03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320_SBR04(Element):
    """Policy Name"""
    class Schema:
        json = {'title': 'Policy Name',
         'usage': 'S',
         'description': 'xid=SBR04 data_ele=93',
         'sequence': 4,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2320_SBR05(Element):
    """Insurance Type Code"""
    class Schema:
        json = {'title': 'Insurance Type Code',
         'usage': 'N',
         'description': 'xid=SBR05 data_ele=1336',
         'sequence': 5,
         'type': {'$ref': '#/$common/1336'}}
        datatype = common.D_1336
        min_len = 1
        max_len = 3


class L2320_SBR06(Element):
    """Coordination of Benefits Code"""
    class Schema:
        json = {'title': 'Coordination of Benefits Code',
         'usage': 'N',
         'description': 'xid=SBR06 data_ele=1143',
         'sequence': 6,
         'type': {'$ref': '#/$common/1143'}}
        datatype = common.D_1143
        min_len = 1
        max_len = 1


class L2320_SBR07(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=SBR07 data_ele=1073',
         'sequence': 7,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2320_SBR08(Element):
    """Employment Status Code"""
    class Schema:
        json = {'title': 'Employment Status Code',
         'usage': 'N',
         'description': 'xid=SBR08 data_ele=584',
         'sequence': 8,
         'type': {'$ref': '#/$common/584'}}
        datatype = common.D_584
        min_len = 2
        max_len = 2


class L2320_SBR09(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'S',
         'description': 'xid=SBR09 data_ele=1032',
         'sequence': 9,
         'type': {'allOf': [{'$ref': '#/$common/1032'},
                            {'enum': ['09', '11', '12', '13', '14', '15', '16', '17',
                                      'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB',
                                      'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ']}]}}
        datatype = common.D_1032
        codes = ['09', '11', '12', '13', '14', '15', '16', '17', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB', 'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ']
        min_len = 1
        max_len = 2


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    class Schema:
        json = {'title': 'Other Subscriber Information',
         'usage': 'R',
         'description': 'xid=SBR name=Other Subscriber Information',
         'position': 290,
         'type': 'object',
         'properties': {'xid': {'literal': 'SBR'},
                        'sbr01': {'$ref': '#/$elements/L2320_SBR01'},
                        'sbr02': {'$ref': '#/$elements/L2320_SBR02'},
                        'sbr03': {'$ref': '#/$elements/L2320_SBR03'},
                        'sbr04': {'$ref': '#/$elements/L2320_SBR04'},
                        'sbr09': {'$ref': '#/$elements/L2320_SBR09'}},
         'required': ['sbr01', 'sbr02']}
        segment_name = 'SBR'
    sbr01: L2320_SBR01
    sbr02: L2320_SBR02
    sbr03: L2320_SBR03 | None
    sbr04: L2320_SBR04 | None
    sbr09: L2320_SBR09 | None


class L2320_CAS01(Element):
    """Claim Adjustment Group Code"""
    class Schema:
        json = {'title': 'Claim Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'CR', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'CR', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2320_CAS02(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=CAS02 data_ele=1034',
         'sequence': 2,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS03(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'R',
         'description': 'xid=CAS03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS04(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS04 data_ele=380',
         'sequence': 4,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS05(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS05 data_ele=1034',
         'sequence': 5,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS06(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS07(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS07 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS08(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS08 data_ele=1034',
         'sequence': 8,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS09(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS09 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS10(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS10 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS11(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS11 data_ele=1034',
         'sequence': 11,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS12(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS12 data_ele=782',
         'sequence': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS13(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS13 data_ele=380',
         'sequence': 13,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS14(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS14 data_ele=1034',
         'sequence': 14,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS15(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS15 data_ele=782',
         'sequence': 15,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS16(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS16 data_ele=380',
         'sequence': 16,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS17(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS17 data_ele=1034',
         'sequence': 17,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2320_CAS18(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS18 data_ele=782',
         'sequence': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_CAS19(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS19 data_ele=380',
         'sequence': 19,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2320_CAS(Segment):
    """Claim Adjustment"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Adjustment',
                   'usage': 'S',
                   'description': 'xid=CAS name=Claim Adjustment',
                   'position': 295,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'CAS'},
                                  'cas01': {'$ref': '#/$elements/L2320_CAS01'},
                                  'cas02': {'$ref': '#/$elements/L2320_CAS02'},
                                  'cas03': {'$ref': '#/$elements/L2320_CAS03'},
                                  'cas04': {'$ref': '#/$elements/L2320_CAS04'},
                                  'cas05': {'$ref': '#/$elements/L2320_CAS05'},
                                  'cas06': {'$ref': '#/$elements/L2320_CAS06'},
                                  'cas07': {'$ref': '#/$elements/L2320_CAS07'},
                                  'cas08': {'$ref': '#/$elements/L2320_CAS08'},
                                  'cas09': {'$ref': '#/$elements/L2320_CAS09'},
                                  'cas10': {'$ref': '#/$elements/L2320_CAS10'},
                                  'cas11': {'$ref': '#/$elements/L2320_CAS11'},
                                  'cas12': {'$ref': '#/$elements/L2320_CAS12'},
                                  'cas13': {'$ref': '#/$elements/L2320_CAS13'},
                                  'cas14': {'$ref': '#/$elements/L2320_CAS14'},
                                  'cas15': {'$ref': '#/$elements/L2320_CAS15'},
                                  'cas16': {'$ref': '#/$elements/L2320_CAS16'},
                                  'cas17': {'$ref': '#/$elements/L2320_CAS17'},
                                  'cas18': {'$ref': '#/$elements/L2320_CAS18'},
                                  'cas19': {'$ref': '#/$elements/L2320_CAS19'}},
                   'required': ['cas01', 'cas02', 'cas03']},
         'maxItems': 5}
        segment_name = 'CAS'
    cas01: L2320_CAS01
    cas02: L2320_CAS02
    cas03: L2320_CAS03
    cas04: L2320_CAS04 | None
    cas05: L2320_CAS05 | None
    cas06: L2320_CAS06 | None
    cas07: L2320_CAS07 | None
    cas08: L2320_CAS08 | None
    cas09: L2320_CAS09 | None
    cas10: L2320_CAS10 | None
    cas11: L2320_CAS11 | None
    cas12: L2320_CAS12 | None
    cas13: L2320_CAS13 | None
    cas14: L2320_CAS14 | None
    cas15: L2320_CAS15 | None
    cas16: L2320_CAS16 | None
    cas17: L2320_CAS17 | None
    cas18: L2320_CAS18 | None
    cas19: L2320_CAS19 | None


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['D']}]}}
        datatype = common.D_522
        codes = ['D']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Payer Paid Amount"""
    class Schema:
        json = {'title': 'Payer Paid Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Payer Paid Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Payer Paid Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Payer Paid Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['AAE']}]}}
        datatype = common.D_522
        codes = ['AAE']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Approved Amount"""
    class Schema:
        json = {'title': 'Approved Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Approved Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Approved Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Approved Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['B6']}]}}
        datatype = common.D_522
        codes = ['B6']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Allowed Amount"""
    class Schema:
        json = {'title': 'Allowed Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Allowed Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Allowed Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Allowed Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['F2']}]}}
        datatype = common.D_522
        codes = ['F2']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Patient Responsibility Amount"""
    class Schema:
        json = {'title': 'Patient Responsibility Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Responsibility Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Patient Responsibility Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Patient '
                        'Responsibility Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['AU']}]}}
        datatype = common.D_522
        codes = ['AU']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Covered Amount"""
    class Schema:
        json = {'title': 'Covered Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Covered Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Covered Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Covered Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['D8']}]}}
        datatype = common.D_522
        codes = ['D8']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Other Payer Discount Amount"""
    class Schema:
        json = {'title': 'Other Payer Discount Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Discount Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Discount Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Discount Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['F5']}]}}
        datatype = common.D_522
        codes = ['F5']
        min_len = 1
        max_len = 3


class L2320_AMT02(Element):
    """Other Payer Patient Paid Amount"""
    class Schema:
        json = {'title': 'Other Payer Patient Paid Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2320_AMT03(Element):
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


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Paid Amount"""
    class Schema:
        json = {'title': 'Coordination of Benefits (COB) Patient Paid Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Coordination of Benefits (COB) Patient Paid '
                        'Amount',
         'position': 300,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2320_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2320_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2320_AMT01
    amt02: L2320_AMT02


class L2320_DMG01(Element):
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


class L2320_DMG02(Element):
    """Other Insured Birth Date"""
    class Schema:
        json = {'title': 'Other Insured Birth Date',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2320_DMG03(Element):
    """Other Insured Gender Code"""
    class Schema:
        json = {'title': 'Other Insured Gender Code',
         'usage': 'R',
         'description': 'xid=DMG03 data_ele=1068',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2320_DMG04(Element):
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


class L2320_DMG05(Element):
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


class L2320_DMG06(Element):
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


class L2320_DMG07(Element):
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


class L2320_DMG08(Element):
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


class L2320_DMG09(Element):
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


class L2320_DMG(Segment):
    """Other Insured Demographic Information"""
    class Schema:
        json = {'title': 'Other Insured Demographic Information',
         'usage': 'S',
         'description': 'xid=DMG name=Other Insured Demographic Information',
         'position': 305,
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2320_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2320_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2320_DMG03'}},
         'required': ['dmg01', 'dmg02', 'dmg03']}
        segment_name = 'DMG'
    dmg01: L2320_DMG01
    dmg02: L2320_DMG02
    dmg03: L2320_DMG03


class L2320_OI01(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'N',
         'description': 'xid=OI01 data_ele=1032',
         'sequence': 1,
         'type': {'$ref': '#/$common/1032'}}
        datatype = common.D_1032
        min_len = 1
        max_len = 2


class L2320_OI02(Element):
    """Claim Submission Reason Code"""
    class Schema:
        json = {'title': 'Claim Submission Reason Code',
         'usage': 'N',
         'description': 'xid=OI02 data_ele=1383',
         'sequence': 2,
         'type': {'$ref': '#/$common/1383'}}
        datatype = common.D_1383
        min_len = 2
        max_len = 2


class L2320_OI03(Element):
    """Benefits Assignment Certification Indicator"""
    class Schema:
        json = {'title': 'Benefits Assignment Certification Indicator',
         'usage': 'R',
         'description': 'xid=OI03 data_ele=1073',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2320_OI04(Element):
    """Patient Signature Source Code"""
    class Schema:
        json = {'title': 'Patient Signature Source Code',
         'usage': 'N',
         'description': 'xid=OI04 data_ele=1351',
         'sequence': 4,
         'type': {'$ref': '#/$common/1351'}}
        datatype = common.D_1351
        min_len = 1
        max_len = 1


class L2320_OI05(Element):
    """Provider Agreement Code"""
    class Schema:
        json = {'title': 'Provider Agreement Code',
         'usage': 'N',
         'description': 'xid=OI05 data_ele=1360',
         'sequence': 5,
         'type': {'$ref': '#/$common/1360'}}
        datatype = common.D_1360
        min_len = 1
        max_len = 1


class L2320_OI06(Element):
    """Release of Information"""
    class Schema:
        json = {'title': 'Release of Information',
         'usage': 'R',
         'description': 'xid=OI06 data_ele=1363',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1363'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1363
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2320_OI(Segment):
    """Other Insurance Coverage Information"""
    class Schema:
        json = {'title': 'Other Insurance Coverage Information',
         'usage': 'R',
         'description': 'xid=OI name=Other Insurance Coverage Information',
         'position': 310,
         'type': 'object',
         'properties': {'xid': {'literal': 'OI'},
                        'oi03': {'$ref': '#/$elements/L2320_OI03'},
                        'oi06': {'$ref': '#/$elements/L2320_OI06'}},
         'required': ['oi03', 'oi06']}
        segment_name = 'OI'
    oi03: L2320_OI03
    oi06: L2320_OI06


class L2330A_NM101(Element):
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


class L2330A_NM102(Element):
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


class L2330A_NM103(Element):
    """Other Insured Last Name"""
    class Schema:
        json = {'title': 'Other Insured Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330A_NM104(Element):
    """Other Insured First Name"""
    class Schema:
        json = {'title': 'Other Insured First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2330A_NM105(Element):
    """Other Insured Middle Name"""
    class Schema:
        json = {'title': 'Other Insured Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2330A_NM106(Element):
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


class L2330A_NM107(Element):
    """Other Insured Name Suffix"""
    class Schema:
        json = {'title': 'Other Insured Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2330A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', 'MI', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['24', 'MI', 'ZZ']
        min_len = 1
        max_len = 2


class L2330A_NM109(Element):
    """Other Insured Identifier"""
    class Schema:
        json = {'title': 'Other Insured Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2330A_NM110(Element):
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


class L2330A_NM111(Element):
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


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    class Schema:
        json = {'title': 'Other Subscriber Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Subscriber Name',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2330A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2330A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2330A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2330A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2330A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2330A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm104', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2330A_NM101
    nm102: L2330A_NM102
    nm103: L2330A_NM103
    nm104: L2330A_NM104
    nm105: L2330A_NM105 | None
    nm107: L2330A_NM107 | None
    nm108: L2330A_NM108
    nm109: L2330A_NM109


class L2330A_N301(Element):
    """Other Insured's Address 1"""
    class Schema:
        json = {'title': "Other Insured's Address 1",
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2330A_N302(Element):
    """Other Insured's Address 2"""
    class Schema:
        json = {'title': "Other Insured's Address 2",
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    class Schema:
        json = {'title': 'Other Subscriber Address',
         'usage': 'S',
         'description': 'xid=N3 name=Other Subscriber Address',
         'position': 332,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2330A_N301'},
                        'n302': {'$ref': '#/$elements/L2330A_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2330A_N301
    n302: L2330A_N302 | None


class L2330A_N401(Element):
    """Other Insured City Name"""
    class Schema:
        json = {'title': 'Other Insured City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2330A_N402(Element):
    """Other Insured State Code"""
    class Schema:
        json = {'title': 'Other Insured State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2330A_N403(Element):
    """Other Insured Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Other Insured Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2330A_N404(Element):
    """Other Insured's Country"""
    class Schema:
        json = {'title': "Other Insured's Country",
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        codes = common.country
        min_len = 2
        max_len = 3


class L2330A_N405(Element):
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


class L2330A_N406(Element):
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


class L2330A_N4(Segment):
    """Other Subscriber City/State/ZIP Code"""
    class Schema:
        json = {'title': 'Other Subscriber City/State/ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Other Subscriber City/State/ZIP Code',
         'position': 340,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2330A_N401'},
                        'n402': {'$ref': '#/$elements/L2330A_N402'},
                        'n403': {'$ref': '#/$elements/L2330A_N403'},
                        'n404': {'$ref': '#/$elements/L2330A_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2330A_N401
    n402: L2330A_N402
    n403: L2330A_N403
    n404: L2330A_N404 | None


class L2330A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1W', '23', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1W', '23', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2330A_REF02(Element):
    """Other Insured Additional Identifier"""
    class Schema:
        json = {'title': 'Other Insured Additional Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330A_REF03(Element):
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


class L2330A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330A_REF(Segment):
    """Other Subscriber Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Subscriber Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Subscriber Secondary '
                                  'Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330A_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330A_REF01
    ref02: L2330A_REF02


class L2330A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Subscriber Name',
                   'usage': 'R',
                   'description': 'xid=2330A name=Other Subscriber Name type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330A_NM1'},
                                  'n3': {'$ref': '#/$segments/L2330A_N3'},
                                  'n4': {'$ref': '#/$segments/L2330A_N4'},
                                  'ref': {'$ref': '#/$segments/L2330A_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330A_NM1
    n3: L2330A_N3 | None
    n4: L2330A_N4 | None
    ref: list[L2330A_REF] | None


class L2330B_NM101(Element):
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


class L2330B_NM102(Element):
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


class L2330B_NM103(Element):
    """Other Payer Last or Organization Name"""
    class Schema:
        json = {'title': 'Other Payer Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330B_NM104(Element):
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


class L2330B_NM105(Element):
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


class L2330B_NM106(Element):
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


class L2330B_NM107(Element):
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


class L2330B_NM108(Element):
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


class L2330B_NM109(Element):
    """Other Payer Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2330B_NM110(Element):
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


class L2330B_NM111(Element):
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


class L2330B_NM1(Segment):
    """Other Payer Name"""
    class Schema:
        json = {'title': 'Other Payer Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Name',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2330B_NM103'},
                        'nm108': {'$ref': '#/$elements/L2330B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2330B_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2330B_NM101
    nm102: L2330B_NM102
    nm103: L2330B_NM103
    nm108: L2330B_NM108
    nm109: L2330B_NM109


class L2330B_PER01(Element):
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


class L2330B_PER02(Element):
    """Other Payer Contact Name"""
    class Schema:
        json = {'title': 'Other Payer Contact Name',
         'usage': 'R',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2330B_PER03(Element):
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


class L2330B_PER04(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330B_PER05(Element):
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


class L2330B_PER06(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330B_PER07(Element):
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


class L2330B_PER08(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2330B_PER09(Element):
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


class L2330B_PER(Segment):
    """Other Payer Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Other Payer Contact Information',
                   'position': 345,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2330B_PER01'},
                                  'per02': {'$ref': '#/$elements/L2330B_PER02'},
                                  'per03': {'$ref': '#/$elements/L2330B_PER03'},
                                  'per04': {'$ref': '#/$elements/L2330B_PER04'},
                                  'per05': {'$ref': '#/$elements/L2330B_PER05'},
                                  'per06': {'$ref': '#/$elements/L2330B_PER06'},
                                  'per07': {'$ref': '#/$elements/L2330B_PER07'},
                                  'per08': {'$ref': '#/$elements/L2330B_PER08'}},
                   'required': ['per01', 'per02', 'per03', 'per04']},
         'maxItems': 2}
        segment_name = 'PER'
    per01: L2330B_PER01
    per02: L2330B_PER02
    per03: L2330B_PER03
    per04: L2330B_PER04
    per05: L2330B_PER05 | None
    per06: L2330B_PER06 | None
    per07: L2330B_PER07 | None
    per08: L2330B_PER08 | None


class L2330B_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['573']}]}}
        datatype = common.D_374
        codes = ['573']
        min_len = 3
        max_len = 3


class L2330B_DTP02(Element):
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


class L2330B_DTP03(Element):
    """Date Claim Paid"""
    class Schema:
        json = {'title': 'Date Claim Paid',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2330B_DTP(Segment):
    """Claim Paid Date"""
    class Schema:
        json = {'title': 'Claim Paid Date',
         'usage': 'S',
         'description': 'xid=DTP name=Claim Paid Date',
         'position': 350,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2330B_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2330B_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2330B_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2330B_DTP01
    dtp02: L2330B_DTP02
    dtp03: L2330B_DTP03


class L2330B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['2U', 'D8', 'F8', 'FY', 'NF', 'TJ']}]}}
        datatype = common.D_128
        codes = ['2U', 'D8', 'F8', 'FY', 'NF', 'TJ']
        min_len = 2
        max_len = 3


class L2330B_REF02(Element):
    """Other Payer Secondary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330B_REF03(Element):
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


class L2330B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330B_REF(Segment):
    """Other Payer Secondary Identifier"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Secondary Identifier',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Secondary Identifier',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330B_REF01
    ref02: L2330B_REF02


class L2330B_REF01(Element):
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


class L2330B_REF02(Element):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330B_REF03(Element):
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


class L2330B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Prior Authorization or '
                                  'Referral Number',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2330B_REF01
    ref02: L2330B_REF02


class L2330B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['T4']}]}}
        datatype = common.D_128
        codes = ['T4']
        min_len = 2
        max_len = 3


class L2330B_REF02(Element):
    """Other Payer Claim Adjustment Indicator"""
    class Schema:
        json = {'title': 'Other Payer Claim Adjustment Indicator',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330B_REF03(Element):
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


class L2330B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330B_REF(Segment):
    """Other Payer Claim Adjustment Indicator"""
    class Schema:
        json = {'title': 'Other Payer Claim Adjustment Indicator',
         'usage': 'S',
         'description': 'xid=REF name=Other Payer Claim Adjustment Indicator',
         'position': 355,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2330B_REF01'},
                        'ref02': {'$ref': '#/$elements/L2330B_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2330B_REF01
    ref02: L2330B_REF02


class L2330B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Name',
                   'usage': 'R',
                   'description': 'xid=2330B name=Other Payer Name type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330B_NM1'},
                                  'per': {'$ref': '#/$segments/L2330B_PER'},
                                  'dtp': {'$ref': '#/$segments/L2330B_DTP'},
                                  'ref': {'$ref': '#/$segments/L2330B_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330B_NM1
    per: list[L2330B_PER] | None
    dtp: L2330B_DTP | None
    ref: list[L2330B_REF] | None
    ref: list[L2330B_REF] | None
    ref: L2330B_REF | None


class L2330C_NM101(Element):
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


class L2330C_NM102(Element):
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


class L2330C_NM103(Element):
    """Other Payer Patient Last Name"""
    class Schema:
        json = {'title': 'Other Payer Patient Last Name',
         'usage': 'N',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330C_NM104(Element):
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


class L2330C_NM105(Element):
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


class L2330C_NM106(Element):
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


class L2330C_NM107(Element):
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


class L2330C_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['MI']}]}}
        datatype = common.D_66
        codes = ['MI']
        min_len = 1
        max_len = 2


class L2330C_NM109(Element):
    """Other Payer Patient Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Patient Primary Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2330C_NM110(Element):
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


class L2330C_NM111(Element):
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


class L2330C_NM1(Segment):
    """Other Payer Patient Information"""
    class Schema:
        json = {'title': 'Other Payer Patient Information',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Patient Information',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330C_NM102'},
                        'nm108': {'$ref': '#/$elements/L2330C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2330C_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2330C_NM101
    nm102: L2330C_NM102
    nm108: L2330C_NM108
    nm109: L2330C_NM109


class L2330C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1W', '23', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1W', '23', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2330C_REF02(Element):
    """Other Payer Patient Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Patient Primary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330C_REF03(Element):
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


class L2330C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330C_REF(Segment):
    """Other Payer Patient Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Patient Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Patient Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330C_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330C_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330C_REF01
    ref02: L2330C_REF02


class L2330C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Patient Information',
                   'usage': 'S',
                   'description': 'xid=2330C name=Other Payer Patient Information '
                                  'type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330C_NM1'},
                                  'ref': {'$ref': '#/$segments/L2330C_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330C_NM1
    ref: list[L2330C_REF] | None


class L2330D_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DN', 'P3']}]}}
        datatype = common.D_98
        codes = ['DN', 'P3']
        min_len = 2
        max_len = 3


class L2330D_NM102(Element):
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


class L2330D_NM103(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330D_NM104(Element):
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


class L2330D_NM105(Element):
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


class L2330D_NM106(Element):
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


class L2330D_NM107(Element):
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


class L2330D_NM108(Element):
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


class L2330D_NM109(Element):
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


class L2330D_NM110(Element):
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


class L2330D_NM111(Element):
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


class L2330D_NM1(Segment):
    """Other Payer Referring Provider"""
    class Schema:
        json = {'title': 'Other Payer Referring Provider',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Referring Provider',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330D_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330D_NM102'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2330D_NM101
    nm102: L2330D_NM102


class L2330D_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2330D_REF02(Element):
    """Other Payer Referring Provider Identifier"""
    class Schema:
        json = {'title': 'Other Payer Referring Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330D_REF03(Element):
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


class L2330D_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330D_REF(Segment):
    """Other Payer Referring Provider Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Referring Provider Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Referring Provider '
                                  'Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330D_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330D_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330D_REF01
    ref02: L2330D_REF02


class L2330D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Referring Provider',
                   'usage': 'S',
                   'description': 'xid=2330D name=Other Payer Referring Provider '
                                  'type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330D_NM1'},
                                  'ref': {'$ref': '#/$segments/L2330D_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330D_NM1
    ref: list[L2330D_REF] | None


class L2330E_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['82']}]}}
        datatype = common.D_98
        codes = ['82']
        min_len = 2
        max_len = 3


class L2330E_NM102(Element):
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


class L2330E_NM103(Element):
    """Name Last or Organization Name"""
    class Schema:
        json = {'title': 'Name Last or Organization Name',
         'usage': 'N',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2330E_NM104(Element):
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


class L2330E_NM105(Element):
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


class L2330E_NM106(Element):
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


class L2330E_NM107(Element):
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


class L2330E_NM108(Element):
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


class L2330E_NM109(Element):
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


class L2330E_NM110(Element):
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


class L2330E_NM111(Element):
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


class L2330E_NM1(Segment):
    """Other Payer Rendering Provider"""
    class Schema:
        json = {'title': 'Other Payer Rendering Provider',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Rendering Provider',
         'position': 325,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2330E_NM101'},
                        'nm102': {'$ref': '#/$elements/L2330E_NM102'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2330E_NM101
    nm102: L2330E_NM102


class L2330E_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2330E_REF02(Element):
    """Other Payer Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Other Payer Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2330E_REF03(Element):
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


class L2330E_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2330E_REF(Segment):
    """Other Payer Rendering Provider Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Rendering Provider Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Rendering Provider '
                                  'Identification',
                   'position': 355,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2330E_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2330E_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 3}
        segment_name = 'REF'
    ref01: L2330E_REF01
    ref02: L2330E_REF02


class L2330E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Rendering Provider',
                   'usage': 'S',
                   'description': 'xid=2330E name=Other Payer Rendering Provider '
                                  'type=None',
                   'position': 325,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2330E_NM1'},
                                  'ref': {'$ref': '#/$segments/L2330E_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2330E_NM1
    ref: list[L2330E_REF] | None


class L2320(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Subscriber Information',
                   'usage': 'S',
                   'description': 'xid=2320 name=Other Subscriber Information '
                                  'type=None',
                   'position': 290,
                   'type': 'object',
                   'properties': {'sbr': {'$ref': '#/$segments/L2320_SBR'},
                                  'cas': {'$ref': '#/$segments/L2320_CAS'},
                                  'amt': {'$ref': '#/$segments/L2320_AMT'},
                                  'dmg': {'$ref': '#/$segments/L2320_DMG'},
                                  'oi': {'$ref': '#/$segments/L2320_OI'},
                                  'l2330a': {'$ref': '#/$segments/L2330A'},
                                  'l2330b': {'$ref': '#/$segments/L2330B'},
                                  'l2330c': {'$ref': '#/$segments/L2330C'},
                                  'l2330d': {'$ref': '#/$segments/L2330D'},
                                  'l2330e': {'$ref': '#/$segments/L2330E'}},
                   'required': ['sbr', 'oi', 'l2330a', 'l2330b']},
         'maxItems': 10}
    sbr: L2320_SBR
    cas: list[L2320_CAS] | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    amt: L2320_AMT | None
    dmg: L2320_DMG | None
    oi: L2320_OI
    l2330a: list[L2330A]
    l2330b: list[L2330B]
    l2330c: list[L2330C] | None
    l2330d: list[L2330D] | None
    l2330e: list[L2330E] | None


class L2400_LX01(Element):
    """Line Counter"""
    class Schema:
        json = {'title': 'Line Counter',
         'usage': 'R',
         'description': 'xid=LX01 data_ele=554',
         'sequence': 1,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2400_LX(Segment):
    """Line Counter"""
    class Schema:
        json = {'title': 'Line Counter',
         'usage': 'R',
         'description': 'xid=LX name=Line Counter',
         'position': 365,
         'type': 'object',
         'properties': {'xid': {'literal': 'LX'},
                        'lx01': {'$ref': '#/$elements/L2400_LX01'}},
         'required': ['lx01']}
        segment_name = 'LX'
    lx01: L2400_LX01


class L2400_SV301_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SV301-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'}, {'enum': ['AD']}]}}
        datatype = common.D_235
        codes = ['AD']
        min_len = 2
        max_len = 2


class L2400_SV301_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SV301-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2400_SV301_03(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_04(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_05(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_06(Element):
    """Procedure Code Modifier"""
    class Schema:
        json = {'title': 'Procedure Code Modifier',
         'usage': 'S',
         'description': 'xid=SV301-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2400_SV301_07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=SV301-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2400_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'R',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'sv301_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SV301-01 data_ele=235',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD']}]}},
                        'sv301_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SV301-02 data_ele=234',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'sv301_03': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-03 data_ele=1339',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_04': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-04 data_ele=1339',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_05': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-05 data_ele=1339',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_06': {'title': 'Procedure Code Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SV301-06 data_ele=1339',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'sv301_07': {'title': 'Description',
                                     'usage': 'N',
                                     'description': 'xid=SV301-07 data_ele=352',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/352'}}},
         'required': ['sv301_01', 'sv301_02']}
    sv301_01: L2400_SV301_01
    sv301_02: L2400_SV301_02
    sv301_03: L2400_SV301_03 | None
    sv301_04: L2400_SV301_04 | None
    sv301_05: L2400_SV301_05 | None
    sv301_06: L2400_SV301_06 | None


class L2400_SV302(Element):
    """Line Item Charge Amount"""
    class Schema:
        json = {'title': 'Line Item Charge Amount',
         'usage': 'R',
         'description': 'xid=SV302 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2400_SV303(Element):
    """Facility Type Code"""
    class Schema:
        json = {'title': 'Facility Type Code',
         'usage': 'S',
         'description': 'xid=SV303 data_ele=1331',
         'sequence': 3,
         'type': {'$ref': '#/$common/1331'}}
        datatype = common.D_1331
        codes = common.pos
        min_len = 1
        max_len = 2


class L2400_SV304_01(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'R',
         'description': 'xid=SV304-01 data_ele=1361',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_02(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-02 data_ele=1361',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_03(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-03 data_ele=1361',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_04(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-04 data_ele=1361',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_SV304_05(Element):
    """Oral Cavity Designation Code"""
    class Schema:
        json = {'title': 'Oral Cavity Designation Code',
         'usage': 'S',
         'description': 'xid=SV304-05 data_ele=1361',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1361'},
                            {'enum': ['L', 'R', '00', '01', '02', '09', '10', '20',
                                      '30', '40']}]}}
        datatype = common.D_1361
        codes = ['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40']
        min_len = 1
        max_len = 3


class L2400_C006(Composite):
    class Schema:
        json = {'title': 'Oral Cavity Designation',
         'usage': 'S',
         'description': 'xid=None name=Oral Cavity Designation refdes= data_ele=C006',
         'sequence': 4,
         'syntax': [],
         'type': 'object',
         'properties': {'sv304_01': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'R',
                                     'description': 'xid=SV304-01 data_ele=1361',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_02': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-02 data_ele=1361',
                                     'sequence': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_03': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-03 data_ele=1361',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_04': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-04 data_ele=1361',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}},
                        'sv304_05': {'title': 'Oral Cavity Designation Code',
                                     'usage': 'S',
                                     'description': 'xid=SV304-05 data_ele=1361',
                                     'sequence': 5,
                                     'type': {'allOf': [{'$ref': '#/$common/1361'},
                                                        {'enum': ['L', 'R', '00', '01',
                                                                  '02', '09', '10',
                                                                  '20', '30',
                                                                  '40']}]}}},
         'required': ['sv304_01']}
    sv304_01: L2400_SV304_01
    sv304_02: L2400_SV304_02 | None
    sv304_03: L2400_SV304_03 | None
    sv304_04: L2400_SV304_04 | None
    sv304_05: L2400_SV304_05 | None


class L2400_SV305(Element):
    """Prosthesis, Crown, or Inlay Code"""
    class Schema:
        json = {'title': 'Prosthesis, Crown, or Inlay Code',
         'usage': 'S',
         'description': 'xid=SV305 data_ele=1358',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1358'}, {'enum': ['I', 'R']}]}}
        datatype = common.D_1358
        codes = ['I', 'R']
        min_len = 1
        max_len = 1


class L2400_SV306(Element):
    """Procedure Count"""
    class Schema:
        json = {'title': 'Procedure Count',
         'usage': 'R',
         'description': 'xid=SV306 data_ele=380',
         'sequence': 6,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2400_SV307(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=SV307 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2400_SV308(Element):
    """Copay Status Code"""
    class Schema:
        json = {'title': 'Copay Status Code',
         'usage': 'N',
         'description': 'xid=SV308 data_ele=1327',
         'sequence': 8,
         'type': {'$ref': '#/$common/1327'}}
        datatype = common.D_1327
        min_len = 1
        max_len = 1


class L2400_SV309(Element):
    """Provider Agreement Code"""
    class Schema:
        json = {'title': 'Provider Agreement Code',
         'usage': 'N',
         'description': 'xid=SV309 data_ele=1360',
         'sequence': 9,
         'type': {'$ref': '#/$common/1360'}}
        datatype = common.D_1360
        min_len = 1
        max_len = 1


class L2400_SV310(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=SV310 data_ele=1073',
         'sequence': 10,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2400_C004(Composite):
    class Schema:
        json = {'title': 'Composite Diagnosis Code Pointer',
         'usage': 'N',
         'description': 'xid=None name=Composite Diagnosis Code Pointer refdes= '
                        'data_ele=C004',
         'sequence': 11,
         'syntax': []}


class L2400_SV3(Segment):
    """Dental Service"""
    class Schema:
        json = {'title': 'Dental Service',
         'usage': 'R',
         'description': 'xid=SV3 name=Dental Service',
         'position': 380,
         'type': 'object',
         'properties': {'xid': {'literal': 'SV3'},
                        'c003': {'$ref': '#/$elements/L2400_C003'},
                        'sv302': {'$ref': '#/$elements/L2400_SV302'},
                        'sv303': {'$ref': '#/$elements/L2400_SV303'},
                        'c006': {'$ref': '#/$elements/L2400_C006'},
                        'sv305': {'$ref': '#/$elements/L2400_SV305'},
                        'sv306': {'$ref': '#/$elements/L2400_SV306'}},
         'required': ['c003', 'sv302', 'sv306']}
        segment_name = 'SV3'
    c003: L2400_C003
    sv302: L2400_SV302
    sv303: L2400_SV303 | None
    c006: L2400_C006 | None
    sv305: L2400_SV305 | None
    sv306: L2400_SV306


class L2400_TOO01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=TOO01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['JP']}]}}
        datatype = common.D_1270
        codes = ['JP']
        min_len = 1
        max_len = 3


class L2400_TOO02(Element):
    """Tooth Code"""
    class Schema:
        json = {'title': 'Tooth Code',
         'usage': 'S',
         'description': 'xid=TOO02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2400_TOO03_01(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'R',
         'description': 'xid=TOO03-01 data_ele=1369',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_02(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-02 data_ele=1369',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_03(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-03 data_ele=1369',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_04(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-04 data_ele=1369',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_TOO03_05(Element):
    """Tooth Surface Code"""
    class Schema:
        json = {'title': 'Tooth Surface Code',
         'usage': 'S',
         'description': 'xid=TOO03-05 data_ele=1369',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1369'},
                            {'enum': ['B', 'D', 'F', 'I', 'L', 'M', 'O']}]}}
        datatype = common.D_1369
        codes = ['B', 'D', 'F', 'I', 'L', 'M', 'O']
        min_len = 1
        max_len = 2


class L2400_C005(Composite):
    class Schema:
        json = {'title': 'Tooth Surface',
         'usage': 'S',
         'description': 'xid=None name=Tooth Surface refdes= data_ele=C005',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'too03_01': {'title': 'Tooth Surface Code',
                                     'usage': 'R',
                                     'description': 'xid=TOO03-01 data_ele=1369',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_02': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-02 data_ele=1369',
                                     'sequence': 2,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_03': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-03 data_ele=1369',
                                     'sequence': 3,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_04': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-04 data_ele=1369',
                                     'sequence': 4,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}},
                        'too03_05': {'title': 'Tooth Surface Code',
                                     'usage': 'S',
                                     'description': 'xid=TOO03-05 data_ele=1369',
                                     'sequence': 5,
                                     'type': {'allOf': [{'$ref': '#/$common/1369'},
                                                        {'enum': ['B', 'D', 'F', 'I',
                                                                  'L', 'M', 'O']}]}}},
         'required': ['too03_01']}
    too03_01: L2400_TOO03_01
    too03_02: L2400_TOO03_02 | None
    too03_03: L2400_TOO03_03 | None
    too03_04: L2400_TOO03_04 | None
    too03_05: L2400_TOO03_05 | None


class L2400_TOO(Segment):
    """Tooth Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Tooth Information',
                   'usage': 'S',
                   'description': 'xid=TOO name=Tooth Information',
                   'position': 382,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'TOO'},
                                  'too01': {'$ref': '#/$elements/L2400_TOO01'},
                                  'too02': {'$ref': '#/$elements/L2400_TOO02'},
                                  'c005': {'$ref': '#/$elements/L2400_C005'}},
                   'required': ['too01']},
         'maxItems': 32}
        segment_name = 'TOO'
    too01: L2400_TOO01
    too02: L2400_TOO02 | None
    c005: L2400_C005 | None


class L2400_DTP01(Element):
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


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Service Date"""
    class Schema:
        json = {'title': 'Service Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Service"""
    class Schema:
        json = {'title': 'Date - Service',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Service',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['441']}]}}
        datatype = common.D_374
        codes = ['441']
        min_len = 3
        max_len = 3


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Prior Placement Date"""
    class Schema:
        json = {'title': 'Prior Placement Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Prior Placement"""
    class Schema:
        json = {'title': 'Date - Prior Placement',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Prior Placement',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['452']}]}}
        datatype = common.D_374
        codes = ['452']
        min_len = 3
        max_len = 3


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Orthodontic Banding Date"""
    class Schema:
        json = {'title': 'Orthodontic Banding Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Appliance Placement"""
    class Schema:
        json = {'title': 'Date - Appliance Placement',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Appliance Placement',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['446']}]}}
        datatype = common.D_374
        codes = ['446']
        min_len = 3
        max_len = 3


class L2400_DTP02(Element):
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


class L2400_DTP03(Element):
    """Replacement Date"""
    class Schema:
        json = {'title': 'Replacement Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2400_DTP(Segment):
    """Date - Replacement"""
    class Schema:
        json = {'title': 'Date - Replacement',
         'usage': 'S',
         'description': 'xid=DTP name=Date - Replacement',
         'position': 455,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2400_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2400_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2400_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2400_DTP01
    dtp02: L2400_DTP02
    dtp03: L2400_DTP03


class L2400_QTY01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=QTY01 data_ele=673',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['BF', 'EM', 'HM', 'HO', 'HP', 'P3', 'P4', 'P5',
                                      'SG']}]}}
        datatype = common.D_673
        codes = ['BF', 'EM', 'HM', 'HO', 'HP', 'P3', 'P4', 'P5', 'SG']
        min_len = 2
        max_len = 2


class L2400_QTY02(Element):
    """Anesthesia Unit Count"""
    class Schema:
        json = {'title': 'Anesthesia Unit Count',
         'usage': 'R',
         'description': 'xid=QTY02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2400_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 3,
         'syntax': []}


class L2400_QTY04(Element):
    """Free-Form Message"""
    class Schema:
        json = {'title': 'Free-Form Message',
         'usage': 'N',
         'description': 'xid=QTY04 data_ele=61',
         'sequence': 4,
         'type': {'$ref': '#/$common/61'}}
        datatype = common.D_61
        min_len = 1
        max_len = 30


class L2400_QTY(Segment):
    """Anesthesia Quantity"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Anesthesia Quantity',
                   'usage': 'S',
                   'description': 'xid=QTY name=Anesthesia Quantity',
                   'position': 460,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'QTY'},
                                  'qty01': {'$ref': '#/$elements/L2400_QTY01'},
                                  'qty02': {'$ref': '#/$elements/L2400_QTY02'}},
                   'required': ['qty01', 'qty02']},
         'maxItems': 5}
        segment_name = 'QTY'
    qty01: L2400_QTY01
    qty02: L2400_QTY02


class L2400_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['G3']}]}}
        datatype = common.D_128
        codes = ['G3']
        min_len = 2
        max_len = 3


class L2400_REF02(Element):
    """Predetermination of Benefits Identifier"""
    class Schema:
        json = {'title': 'Predetermination of Benefits Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2400_REF03(Element):
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


class L2400_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2400_REF(Segment):
    """Service Predetermination Identification"""
    class Schema:
        json = {'title': 'Service Predetermination Identification',
         'usage': 'S',
         'description': 'xid=REF name=Service Predetermination Identification',
         'position': 470,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2400_REF01'},
                        'ref02': {'$ref': '#/$elements/L2400_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2400_REF01
    ref02: L2400_REF02


class L2400_REF01(Element):
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


class L2400_REF02(Element):
    """Referral Number"""
    class Schema:
        json = {'title': 'Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2400_REF03(Element):
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


class L2400_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2400_REF(Segment):
    """Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Prior Authorization or Referral Number',
                   'position': 470,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2400_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2400_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2400_REF01
    ref02: L2400_REF02


class L2400_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['6R']}]}}
        datatype = common.D_128
        codes = ['6R']
        min_len = 2
        max_len = 3


class L2400_REF02(Element):
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


class L2400_REF03(Element):
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


class L2400_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2400_REF(Segment):
    """Line Item Control Number"""
    class Schema:
        json = {'title': 'Line Item Control Number',
         'usage': 'S',
         'description': 'xid=REF name=Line Item Control Number',
         'position': 470,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2400_REF01'},
                        'ref02': {'$ref': '#/$elements/L2400_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2400_REF01
    ref02: L2400_REF02


class L2400_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['AAE']}]}}
        datatype = common.D_522
        codes = ['AAE']
        min_len = 1
        max_len = 3


class L2400_AMT02(Element):
    """Approved Amount"""
    class Schema:
        json = {'title': 'Approved Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2400_AMT03(Element):
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


class L2400_AMT(Segment):
    """Approved Amount"""
    class Schema:
        json = {'title': 'Approved Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Approved Amount',
         'position': 475,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2400_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2400_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2400_AMT01
    amt02: L2400_AMT02


class L2400_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'}, {'enum': ['T']}]}}
        datatype = common.D_522
        codes = ['T']
        min_len = 1
        max_len = 3


class L2400_AMT02(Element):
    """Sales Tax Amount"""
    class Schema:
        json = {'title': 'Sales Tax Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2400_AMT03(Element):
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


class L2400_AMT(Segment):
    """Sales Tax Amount"""
    class Schema:
        json = {'title': 'Sales Tax Amount',
         'usage': 'S',
         'description': 'xid=AMT name=Sales Tax Amount',
         'position': 475,
         'type': 'object',
         'properties': {'xid': {'literal': 'AMT'},
                        'amt01': {'$ref': '#/$elements/L2400_AMT01'},
                        'amt02': {'$ref': '#/$elements/L2400_AMT02'}},
         'required': ['amt01', 'amt02']}
        segment_name = 'AMT'
    amt01: L2400_AMT01
    amt02: L2400_AMT02


class L2400_NTE01(Element):
    """Note Reference Code"""
    class Schema:
        json = {'title': 'Note Reference Code',
         'usage': 'R',
         'description': 'xid=NTE01 data_ele=363',
         'sequence': 1,
         'type': {'$ref': '#/$common/363'}}
        datatype = common.D_363
        min_len = 3
        max_len = 3


class L2400_NTE02(Element):
    """Claim Note Text"""
    class Schema:
        json = {'title': 'Claim Note Text',
         'usage': 'R',
         'description': 'xid=NTE02 data_ele=352',
         'sequence': 2,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2400_NTE(Segment):
    """Line Note"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Line Note',
                   'usage': 'S',
                   'description': 'xid=NTE name=Line Note',
                   'position': 485,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'NTE'},
                                  'nte01': {'$ref': '#/$elements/L2400_NTE01'},
                                  'nte02': {'$ref': '#/$elements/L2400_NTE02'}},
                   'required': ['nte01', 'nte02']},
         'maxItems': 10}
        segment_name = 'NTE'
    nte01: L2400_NTE01
    nte02: L2400_NTE02


class L2420A_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['82']}]}}
        datatype = common.D_98
        codes = ['82']
        min_len = 2
        max_len = 3


class L2420A_NM102(Element):
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


class L2420A_NM103(Element):
    """Rendering Provider Last or Organization Name"""
    class Schema:
        json = {'title': 'Rendering Provider Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2420A_NM104(Element):
    """Rendering Provider First Name"""
    class Schema:
        json = {'title': 'Rendering Provider First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2420A_NM105(Element):
    """Rendering Provider Middle Name"""
    class Schema:
        json = {'title': 'Rendering Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2420A_NM106(Element):
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


class L2420A_NM107(Element):
    """Rendering Provider Name Suffix"""
    class Schema:
        json = {'title': 'Rendering Provider Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2420A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2420A_NM109(Element):
    """Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2420A_NM110(Element):
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


class L2420A_NM111(Element):
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


class L2420A_NM1(Segment):
    """Rendering Provider Name"""
    class Schema:
        json = {'title': 'Rendering Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Rendering Provider Name',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2420A_NM101'},
                        'nm102': {'$ref': '#/$elements/L2420A_NM102'},
                        'nm103': {'$ref': '#/$elements/L2420A_NM103'},
                        'nm104': {'$ref': '#/$elements/L2420A_NM104'},
                        'nm105': {'$ref': '#/$elements/L2420A_NM105'},
                        'nm107': {'$ref': '#/$elements/L2420A_NM107'},
                        'nm108': {'$ref': '#/$elements/L2420A_NM108'},
                        'nm109': {'$ref': '#/$elements/L2420A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2420A_NM101
    nm102: L2420A_NM102
    nm103: L2420A_NM103
    nm104: L2420A_NM104 | None
    nm105: L2420A_NM105 | None
    nm107: L2420A_NM107 | None
    nm108: L2420A_NM108
    nm109: L2420A_NM109


class L2420A_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['PE']}]}}
        datatype = common.D_1221
        codes = ['PE']
        min_len = 1
        max_len = 3


class L2420A_PRV02(Element):
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


class L2420A_PRV03(Element):
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


class L2420A_PRV04(Element):
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


class L2420A_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2420A_PRV06(Element):
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


class L2420A_PRV(Segment):
    """Rendering Provider Specialty Information"""
    class Schema:
        json = {'title': 'Rendering Provider Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Rendering Provider Specialty Information',
         'position': 505,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2420A_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2420A_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2420A_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2420A_PRV01
    prv02: L2420A_PRV02
    prv03: L2420A_PRV03


class L2420A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI',
                                      'G2', 'G5', 'LU', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2420A_REF02(Element):
    """Rendering Provider Secondary Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2420A_REF03(Element):
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


class L2420A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2420A_REF(Segment):
    """Rendering Provider Secondary Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Secondary Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Secondary '
                                  'Identification',
                   'position': 525,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2420A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2420A_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2420A_REF01
    ref02: L2420A_REF02


class L2420A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Name',
                   'usage': 'S',
                   'description': 'xid=2420A name=Rendering Provider Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2420A_NM1'},
                                  'prv': {'$ref': '#/$segments/L2420A_PRV'},
                                  'ref': {'$ref': '#/$segments/L2420A_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2420A_NM1
    prv: L2420A_PRV | None
    ref: list[L2420A_REF] | None


class L2420B_NM101(Element):
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


class L2420B_NM102(Element):
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


class L2420B_NM103(Element):
    """Other Payer Last or Organization Name"""
    class Schema:
        json = {'title': 'Other Payer Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2420B_NM104(Element):
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


class L2420B_NM105(Element):
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


class L2420B_NM106(Element):
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


class L2420B_NM107(Element):
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


class L2420B_NM108(Element):
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


class L2420B_NM109(Element):
    """Other Payer Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Referral Number',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2420B_NM110(Element):
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


class L2420B_NM111(Element):
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


class L2420B_NM1(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=NM1 name=Other Payer Prior Authorization or Referral '
                        'Number',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2420B_NM101'},
                        'nm102': {'$ref': '#/$elements/L2420B_NM102'},
                        'nm103': {'$ref': '#/$elements/L2420B_NM103'},
                        'nm108': {'$ref': '#/$elements/L2420B_NM108'},
                        'nm109': {'$ref': '#/$elements/L2420B_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2420B_NM101
    nm102: L2420B_NM102
    nm103: L2420B_NM103
    nm108: L2420B_NM108
    nm109: L2420B_NM109


class L2420B_REF01(Element):
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


class L2420B_REF02(Element):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'title': 'Other Payer Prior Authorization or Referral Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2420B_REF03(Element):
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


class L2420B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2420B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Payer Prior Authorization or '
                                  'Referral Number',
                   'position': 525,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2420B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2420B_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2420B_REF01
    ref02: L2420B_REF02


class L2420B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Payer Prior Authorization or Referral Number',
                   'usage': 'S',
                   'description': 'xid=2420B name=Other Payer Prior Authorization or '
                                  'Referral Number type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2420B_NM1'},
                                  'ref': {'$ref': '#/$segments/L2420B_REF'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2420B_NM1
    ref: list[L2420B_REF] | None


class L2420C_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['DD']}]}}
        datatype = common.D_98
        codes = ['DD']
        min_len = 2
        max_len = 3


class L2420C_NM102(Element):
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


class L2420C_NM103(Element):
    """Assistant Surgeon Last or Organization Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2420C_NM104(Element):
    """Assistant Surgeon First Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2420C_NM105(Element):
    """Assistant Surgeon Middle Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2420C_NM106(Element):
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


class L2420C_NM107(Element):
    """Assistant Surgeon Name Suffix"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2420C_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['24', '34', 'XX']}]}}
        datatype = common.D_66
        codes = ['24', '34', 'XX']
        min_len = 1
        max_len = 2


class L2420C_NM109(Element):
    """Assistant Surgeon Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2420C_NM110(Element):
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


class L2420C_NM111(Element):
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


class L2420C_NM1(Segment):
    """Assistant Surgeon Name"""
    class Schema:
        json = {'title': 'Assistant Surgeon Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Assistant Surgeon Name',
         'position': 500,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2420C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2420C_NM102'},
                        'nm103': {'$ref': '#/$elements/L2420C_NM103'},
                        'nm104': {'$ref': '#/$elements/L2420C_NM104'},
                        'nm105': {'$ref': '#/$elements/L2420C_NM105'},
                        'nm107': {'$ref': '#/$elements/L2420C_NM107'},
                        'nm108': {'$ref': '#/$elements/L2420C_NM108'},
                        'nm109': {'$ref': '#/$elements/L2420C_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2420C_NM101
    nm102: L2420C_NM102
    nm103: L2420C_NM103
    nm104: L2420C_NM104 | None
    nm105: L2420C_NM105 | None
    nm107: L2420C_NM107 | None
    nm108: L2420C_NM108
    nm109: L2420C_NM109


class L2420C_PRV01(Element):
    """Provider Code"""
    class Schema:
        json = {'title': 'Provider Code',
         'usage': 'R',
         'description': 'xid=PRV01 data_ele=1221',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1221'}, {'enum': ['AS']}]}}
        datatype = common.D_1221
        codes = ['AS']
        min_len = 1
        max_len = 3


class L2420C_PRV02(Element):
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


class L2420C_PRV03(Element):
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


class L2420C_PRV04(Element):
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


class L2420C_C035(Composite):
    class Schema:
        json = {'title': 'Provider Specialty Information',
         'usage': 'N',
         'description': 'xid=None name=Provider Specialty Information refdes= '
                        'data_ele=C035',
         'sequence': 5,
         'syntax': []}


class L2420C_PRV06(Element):
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


class L2420C_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    class Schema:
        json = {'title': 'Assistant Surgeon Specialty Information',
         'usage': 'S',
         'description': 'xid=PRV name=Assistant Surgeon Specialty Information',
         'position': 505,
         'type': 'object',
         'properties': {'xid': {'literal': 'PRV'},
                        'prv01': {'$ref': '#/$elements/L2420C_PRV01'},
                        'prv02': {'$ref': '#/$elements/L2420C_PRV02'},
                        'prv03': {'$ref': '#/$elements/L2420C_PRV03'}},
         'required': ['prv01', 'prv02', 'prv03']}
        segment_name = 'PRV'
    prv01: L2420C_PRV01
    prv02: L2420C_PRV02
    prv03: L2420C_PRV03


class L2420C_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'G2',
                                      'LU', 'TJ', 'X4', 'X5']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5']
        min_len = 2
        max_len = 3


class L2420C_REF02(Element):
    """Assistant Surgeon Secondary Identifier"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2420C_REF03(Element):
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


class L2420C_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2420C_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    class Schema:
        json = {'title': 'Assistant Surgeon Secondary Identification',
         'usage': 'S',
         'description': 'xid=REF name=Assistant Surgeon Secondary Identification',
         'position': 525,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2420C_REF01'},
                        'ref02': {'$ref': '#/$elements/L2420C_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2420C_REF01
    ref02: L2420C_REF02


class L2420C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Assistant Surgeon Name',
                   'usage': 'S',
                   'description': 'xid=2420C name=Assistant Surgeon Name type=None',
                   'position': 500,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2420C_NM1'},
                                  'prv': {'$ref': '#/$segments/L2420C_PRV'},
                                  'ref': {'$ref': '#/$segments/L2420C_REF'}}},
         'maxItems': 1}
    nm1: L2420C_NM1 | None
    prv: L2420C_PRV | None
    ref: L2420C_REF | None


class L2430_SVD01(Element):
    """Other Payer Primary Identifier"""
    class Schema:
        json = {'title': 'Other Payer Primary Identifier',
         'usage': 'R',
         'description': 'xid=SVD01 data_ele=67',
         'sequence': 1,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2430_SVD02(Element):
    """Service Line Paid Amount"""
    class Schema:
        json = {'title': 'Service Line Paid Amount',
         'usage': 'R',
         'description': 'xid=SVD02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_SVD03_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SVD03-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'}, {'enum': ['AD', 'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'ZZ']
        min_len = 2
        max_len = 2


class L2430_SVD03_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SVD03-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2430_SVD03_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVD03-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2430_SVD03_07(Element):
    """Procedure Code Description"""
    class Schema:
        json = {'title': 'Procedure Code Description',
         'usage': 'S',
         'description': 'xid=SVD03-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2430_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'R',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'svd03_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SVD03-01 data_ele=235',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD', 'ZZ']}]}},
                        'svd03_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SVD03-02 data_ele=234',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'svd03_03': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-03 data_ele=1339',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_04': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-04 data_ele=1339',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_05': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-05 data_ele=1339',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_06': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-06 data_ele=1339',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svd03_07': {'title': 'Procedure Code Description',
                                     'usage': 'S',
                                     'description': 'xid=SVD03-07 data_ele=352',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/352'}}},
         'required': ['svd03_01', 'svd03_02']}
    svd03_01: L2430_SVD03_01
    svd03_02: L2430_SVD03_02
    svd03_03: L2430_SVD03_03 | None
    svd03_04: L2430_SVD03_04 | None
    svd03_05: L2430_SVD03_05 | None
    svd03_06: L2430_SVD03_06 | None
    svd03_07: L2430_SVD03_07 | None


class L2430_SVD04(Element):
    """Product/Service ID"""
    class Schema:
        json = {'title': 'Product/Service ID',
         'usage': 'N',
         'description': 'xid=SVD04 data_ele=234',
         'sequence': 4,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2430_SVD05(Element):
    """Paid Service Unit Count"""
    class Schema:
        json = {'title': 'Paid Service Unit Count',
         'usage': 'R',
         'description': 'xid=SVD05 data_ele=380',
         'sequence': 5,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_SVD06(Element):
    """Bundled or Unbundled Line Number"""
    class Schema:
        json = {'title': 'Bundled or Unbundled Line Number',
         'usage': 'S',
         'description': 'xid=SVD06 data_ele=554',
         'sequence': 6,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2430_SVD(Segment):
    """Line Adjudication Information"""
    class Schema:
        json = {'title': 'Line Adjudication Information',
         'usage': 'R',
         'description': 'xid=SVD name=Line Adjudication Information',
         'position': 540,
         'type': 'object',
         'properties': {'xid': {'literal': 'SVD'},
                        'svd01': {'$ref': '#/$elements/L2430_SVD01'},
                        'svd02': {'$ref': '#/$elements/L2430_SVD02'},
                        'c003': {'$ref': '#/$elements/L2430_C003'},
                        'svd05': {'$ref': '#/$elements/L2430_SVD05'},
                        'svd06': {'$ref': '#/$elements/L2430_SVD06'}},
         'required': ['svd01', 'svd02', 'c003', 'svd05']}
        segment_name = 'SVD'
    svd01: L2430_SVD01
    svd02: L2430_SVD02
    c003: L2430_C003
    svd05: L2430_SVD05
    svd06: L2430_SVD06 | None


class L2430_CAS01(Element):
    """Adjustment Group Code"""
    class Schema:
        json = {'title': 'Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'CR', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'CR', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2430_CAS02(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=CAS02 data_ele=1034',
         'sequence': 2,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS03(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'R',
         'description': 'xid=CAS03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS04(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS04 data_ele=380',
         'sequence': 4,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS05(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS05 data_ele=1034',
         'sequence': 5,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS06(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS07(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS07 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS08(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS08 data_ele=1034',
         'sequence': 8,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS09(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS09 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS10(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS10 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS11(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS11 data_ele=1034',
         'sequence': 11,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS12(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS12 data_ele=782',
         'sequence': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS13(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS13 data_ele=380',
         'sequence': 13,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS14(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS14 data_ele=1034',
         'sequence': 14,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS15(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS15 data_ele=782',
         'sequence': 15,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS16(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS16 data_ele=380',
         'sequence': 16,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS17(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'S',
         'description': 'xid=CAS17 data_ele=1034',
         'sequence': 17,
         'type': {'$ref': '#/$common/1034'}}
        datatype = common.D_1034
        min_len = 1
        max_len = 5


class L2430_CAS18(Element):
    """Adjustment Amount"""
    class Schema:
        json = {'title': 'Adjustment Amount',
         'usage': 'S',
         'description': 'xid=CAS18 data_ele=782',
         'sequence': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2430_CAS19(Element):
    """Adjustment Quantity"""
    class Schema:
        json = {'title': 'Adjustment Quantity',
         'usage': 'S',
         'description': 'xid=CAS19 data_ele=380',
         'sequence': 19,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2430_CAS(Segment):
    """Service Adjustment"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Adjustment',
                   'usage': 'S',
                   'description': 'xid=CAS name=Service Adjustment',
                   'position': 545,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'CAS'},
                                  'cas01': {'$ref': '#/$elements/L2430_CAS01'},
                                  'cas02': {'$ref': '#/$elements/L2430_CAS02'},
                                  'cas03': {'$ref': '#/$elements/L2430_CAS03'},
                                  'cas04': {'$ref': '#/$elements/L2430_CAS04'},
                                  'cas05': {'$ref': '#/$elements/L2430_CAS05'},
                                  'cas06': {'$ref': '#/$elements/L2430_CAS06'},
                                  'cas07': {'$ref': '#/$elements/L2430_CAS07'},
                                  'cas08': {'$ref': '#/$elements/L2430_CAS08'},
                                  'cas09': {'$ref': '#/$elements/L2430_CAS09'},
                                  'cas10': {'$ref': '#/$elements/L2430_CAS10'},
                                  'cas11': {'$ref': '#/$elements/L2430_CAS11'},
                                  'cas12': {'$ref': '#/$elements/L2430_CAS12'},
                                  'cas13': {'$ref': '#/$elements/L2430_CAS13'},
                                  'cas14': {'$ref': '#/$elements/L2430_CAS14'},
                                  'cas15': {'$ref': '#/$elements/L2430_CAS15'},
                                  'cas16': {'$ref': '#/$elements/L2430_CAS16'},
                                  'cas17': {'$ref': '#/$elements/L2430_CAS17'},
                                  'cas18': {'$ref': '#/$elements/L2430_CAS18'},
                                  'cas19': {'$ref': '#/$elements/L2430_CAS19'}},
                   'required': ['cas01', 'cas02', 'cas03']},
         'maxItems': 99}
        segment_name = 'CAS'
    cas01: L2430_CAS01
    cas02: L2430_CAS02
    cas03: L2430_CAS03
    cas04: L2430_CAS04 | None
    cas05: L2430_CAS05 | None
    cas06: L2430_CAS06 | None
    cas07: L2430_CAS07 | None
    cas08: L2430_CAS08 | None
    cas09: L2430_CAS09 | None
    cas10: L2430_CAS10 | None
    cas11: L2430_CAS11 | None
    cas12: L2430_CAS12 | None
    cas13: L2430_CAS13 | None
    cas14: L2430_CAS14 | None
    cas15: L2430_CAS15 | None
    cas16: L2430_CAS16 | None
    cas17: L2430_CAS17 | None
    cas18: L2430_CAS18 | None
    cas19: L2430_CAS19 | None


class L2430_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['573']}]}}
        datatype = common.D_374
        codes = ['573']
        min_len = 3
        max_len = 3


class L2430_DTP02(Element):
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


class L2430_DTP03(Element):
    """Adjudication or Payment Date"""
    class Schema:
        json = {'title': 'Adjudication or Payment Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2430_DTP(Segment):
    """Line Adjudication Date"""
    class Schema:
        json = {'title': 'Line Adjudication Date',
         'usage': 'R',
         'description': 'xid=DTP name=Line Adjudication Date',
         'position': 550,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTP'},
                        'dtp01': {'$ref': '#/$elements/L2430_DTP01'},
                        'dtp02': {'$ref': '#/$elements/L2430_DTP02'},
                        'dtp03': {'$ref': '#/$elements/L2430_DTP03'}},
         'required': ['dtp01', 'dtp02', 'dtp03']}
        segment_name = 'DTP'
    dtp01: L2430_DTP01
    dtp02: L2430_DTP02
    dtp03: L2430_DTP03


class L2430(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Line Adjudication Information',
                   'usage': 'S',
                   'description': 'xid=2430 name=Line Adjudication Information '
                                  'type=None',
                   'position': 540,
                   'type': 'object',
                   'properties': {'svd': {'$ref': '#/$segments/L2430_SVD'},
                                  'cas': {'$ref': '#/$segments/L2430_CAS'},
                                  'dtp': {'$ref': '#/$segments/L2430_DTP'}},
                   'required': ['svd', 'dtp']},
         'maxItems': 25}
    svd: L2430_SVD
    cas: list[L2430_CAS] | None
    dtp: L2430_DTP


class L2400(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Line Counter',
                   'usage': 'R',
                   'description': 'xid=2400 name=Line Counter type=None',
                   'position': 365,
                   'type': 'object',
                   'properties': {'lx': {'$ref': '#/$segments/L2400_LX'},
                                  'sv3': {'$ref': '#/$segments/L2400_SV3'},
                                  'too': {'$ref': '#/$segments/L2400_TOO'},
                                  'dtp': {'$ref': '#/$segments/L2400_DTP'},
                                  'qty': {'$ref': '#/$segments/L2400_QTY'},
                                  'ref': {'$ref': '#/$segments/L2400_REF'},
                                  'amt': {'$ref': '#/$segments/L2400_AMT'},
                                  'nte': {'$ref': '#/$segments/L2400_NTE'},
                                  'l2420a': {'$ref': '#/$segments/L2420A'},
                                  'l2420b': {'$ref': '#/$segments/L2420B'},
                                  'l2420c': {'$ref': '#/$segments/L2420C'},
                                  'l2430': {'$ref': '#/$segments/L2430'}},
                   'required': ['lx', 'sv3']},
         'maxItems': 50}
    lx: L2400_LX
    sv3: L2400_SV3
    too: list[L2400_TOO] | None
    dtp: L2400_DTP | None
    dtp: L2400_DTP | None
    dtp: L2400_DTP | None
    dtp: L2400_DTP | None
    qty: list[L2400_QTY] | None
    ref: L2400_REF | None
    ref: list[L2400_REF] | None
    ref: L2400_REF | None
    amt: L2400_AMT | None
    amt: L2400_AMT | None
    nte: list[L2400_NTE] | None
    l2420a: list[L2420A] | None
    l2420b: list[L2420B] | None
    l2420c: list[L2420C] | None
    l2430: list[L2430] | None


class L2300(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Information',
                   'usage': 'R',
                   'description': 'xid=2300 name=Claim Information type=None',
                   'position': 130,
                   'type': 'object',
                   'properties': {'clm': {'$ref': '#/$segments/L2300_CLM'},
                                  'dtp': {'$ref': '#/$segments/L2300_DTP'},
                                  'dn1': {'$ref': '#/$segments/L2300_DN1'},
                                  'dn2': {'$ref': '#/$segments/L2300_DN2'},
                                  'pwk': {'$ref': '#/$segments/L2300_PWK'},
                                  'amt': {'$ref': '#/$segments/L2300_AMT'},
                                  'ref': {'$ref': '#/$segments/L2300_REF'},
                                  'nte': {'$ref': '#/$segments/L2300_NTE'},
                                  'l2310a': {'$ref': '#/$segments/L2310A'},
                                  'l2310b': {'$ref': '#/$segments/L2310B'},
                                  'l2310c': {'$ref': '#/$segments/L2310C'},
                                  'l2310d': {'$ref': '#/$segments/L2310D'},
                                  'l2320': {'$ref': '#/$segments/L2320'},
                                  'l2400': {'$ref': '#/$segments/L2400'}},
                   'required': ['clm', 'l2400']},
         'maxItems': 100}
    clm: L2300_CLM
    dtp: L2300_DTP | None
    dtp: L2300_DTP | None
    dtp: L2300_DTP | None
    dtp: L2300_DTP | None
    dtp: list[L2300_DTP] | None
    dtp: L2300_DTP | None
    dn1: L2300_DN1 | None
    dn2: list[L2300_DN2] | None
    pwk: list[L2300_PWK] | None
    amt: L2300_AMT | None
    amt: L2300_AMT | None
    ref: list[L2300_REF] | None
    ref: L2300_REF | None
    ref: L2300_REF | None
    ref: list[L2300_REF] | None
    ref: L2300_REF | None
    nte: list[L2300_NTE] | None
    l2310a: list[L2310A] | None
    l2310b: list[L2310B] | None
    l2310c: list[L2310C] | None
    l2310d: list[L2310D] | None
    l2320: list[L2320] | None
    l2400: list[L2400]


class L2000C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Patient Hierarchical Level',
                   'usage': 'S',
                   'description': 'xid=2000C name=Patient Hierarchical Level type=None',
                   'position': 140,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000C_HL'},
                                  'pat': {'$ref': '#/$segments/L2000C_PAT'},
                                  'l2010ca': {'$ref': '#/$segments/L2010CA'},
                                  'l2300': {'$ref': '#/$segments/L2300'}},
                   'required': ['hl', 'pat', 'l2010ca', 'l2300']}}
    hl: L2000C_HL
    pat: L2000C_PAT
    l2010ca: list[L2010CA]
    l2300: list[L2300]


class L2000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Subscriber Hierarchical Level',
                   'usage': 'R',
                   'description': 'xid=2000B name=Subscriber Hierarchical Level '
                                  'type=None',
                   'position': 20,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000B_HL'},
                                  'sbr': {'$ref': '#/$segments/L2000B_SBR'},
                                  'l2010ba': {'$ref': '#/$segments/L2010BA'},
                                  'l2010bb': {'$ref': '#/$segments/L2010BB'},
                                  'l2010bc': {'$ref': '#/$segments/L2010BC'},
                                  'l2300': {'$ref': '#/$segments/L2300'},
                                  'l2000c': {'$ref': '#/$segments/L2000C'}},
                   'required': ['hl', 'sbr', 'l2010ba', 'l2010bb']}}
    hl: L2000B_HL
    sbr: L2000B_SBR
    l2010ba: list[L2010BA]
    l2010bb: list[L2010BB]
    l2010bc: list[L2010BC] | None
    l2300: list[L2300] | None
    l2000c: list[L2000C] | None


class L2000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Billing/Pay-To Provider Hierarchical Level',
                   'usage': 'R',
                   'description': 'xid=2000A name=Billing/Pay-To Provider Hierarchical '
                                  'Level type=None',
                   'position': 1,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000A_HL'},
                                  'prv': {'$ref': '#/$segments/L2000A_PRV'},
                                  'cur': {'$ref': '#/$segments/L2000A_CUR'},
                                  'l2010aa': {'$ref': '#/$segments/L2010AA'},
                                  'l2010ab': {'$ref': '#/$segments/L2010AB'},
                                  'l2000b': {'$ref': '#/$segments/L2000B'}},
                   'required': ['hl', 'l2010aa', 'l2000b']}}
    hl: L2000A_HL
    prv: L2000A_PRV | None
    cur: L2000A_CUR | None
    l2010aa: list[L2010AA]
    l2010ab: list[L2010AB] | None
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
         'position': 555,
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


class MSG837(Message):
    """HIPAA Health Care Claim: Dental X097A1-837"""
    class Schema:
        json = {'title': 'HIPAA Health Care Claim: Dental X097A1-837',
         'description': 'xid=837 name=HIPAA Health Care Claim: Dental X097A1-837',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
