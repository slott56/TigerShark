"""
834.4010.X095.A1
Created 2023-03-25 09:22:28.390195
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
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['BE']}]}}
        datatype = common.D_479
        codes = ['BE']
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
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['004010X095A1']}]}}
        datatype = common.D_480
        codes = ['004010X095A1']
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
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['834']}]}}
        datatype = common.D_143
        codes = ['834']
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


class HEADER_BGN01(Element):
    """Transaction Set Purpose Code"""
    class Schema:
        json = {'title': 'Transaction Set Purpose Code',
         'usage': 'R',
         'description': 'xid=BGN01 data_ele=353',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/353'}, {'enum': ['00', '15', '22']}]}}
        datatype = common.D_353
        codes = ['00', '15', '22']
        min_len = 2
        max_len = 2


class HEADER_BGN02(Element):
    """Transaction Set Identifier Code"""
    class Schema:
        json = {'title': 'Transaction Set Identifier Code',
         'usage': 'R',
         'description': 'xid=BGN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_BGN03(Element):
    """Transaction Set Creation Date"""
    class Schema:
        json = {'title': 'Transaction Set Creation Date',
         'usage': 'R',
         'description': 'xid=BGN03 data_ele=373',
         'sequence': 3,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BGN04(Element):
    """Transaction Set Creation Time"""
    class Schema:
        json = {'title': 'Transaction Set Creation Time',
         'usage': 'R',
         'description': 'xid=BGN04 data_ele=337',
         'sequence': 4,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_BGN05(Element):
    """Time Zone Code"""
    class Schema:
        json = {'title': 'Time Zone Code',
         'usage': 'S',
         'description': 'xid=BGN05 data_ele=623',
         'sequence': 5,
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
    """Transaction Set Identifier Code"""
    class Schema:
        json = {'title': 'Transaction Set Identifier Code',
         'usage': 'S',
         'description': 'xid=BGN06 data_ele=127',
         'sequence': 6,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_BGN07(Element):
    """Transaction Type Code"""
    class Schema:
        json = {'title': 'Transaction Type Code',
         'usage': 'N',
         'description': 'xid=BGN07 data_ele=640',
         'sequence': 7,
         'type': {'$ref': '#/$common/640'}}
        datatype = common.D_640
        min_len = 2
        max_len = 2


class HEADER_BGN08(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'R',
         'description': 'xid=BGN08 data_ele=306',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/306'}, {'enum': ['2', '4']}]}}
        datatype = common.D_306
        codes = ['2', '4']
        min_len = 1
        max_len = 2


class HEADER_BGN09(Element):
    """Security Level Code"""
    class Schema:
        json = {'title': 'Security Level Code',
         'usage': 'N',
         'description': 'xid=BGN09 data_ele=786',
         'sequence': 9,
         'type': {'$ref': '#/$common/786'}}
        datatype = common.D_786
        min_len = 2
        max_len = 2


class HEADER_BGN(Segment):
    """Beginning Segment"""
    class Schema:
        json = {'title': 'Beginning Segment',
         'usage': 'R',
         'description': 'xid=BGN name=Beginning Segment',
         'position': 20,
         'syntax': ['C0504'],
         'type': 'object',
         'properties': {'xid': {'literal': 'BGN'},
                        'bgn01': {'$ref': '#/$elements/HEADER_BGN01'},
                        'bgn02': {'$ref': '#/$elements/HEADER_BGN02'},
                        'bgn03': {'$ref': '#/$elements/HEADER_BGN03'},
                        'bgn04': {'$ref': '#/$elements/HEADER_BGN04'},
                        'bgn05': {'$ref': '#/$elements/HEADER_BGN05'},
                        'bgn06': {'$ref': '#/$elements/HEADER_BGN06'},
                        'bgn08': {'$ref': '#/$elements/HEADER_BGN08'}},
         'required': ['bgn01', 'bgn02', 'bgn03', 'bgn04', 'bgn08']}
        segment_name = 'BGN'
    bgn01: HEADER_BGN01
    bgn02: HEADER_BGN02
    bgn03: HEADER_BGN03
    bgn04: HEADER_BGN04
    bgn05: HEADER_BGN05 | None
    bgn06: HEADER_BGN06 | None
    bgn08: HEADER_BGN08


class HEADER_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['38']}]}}
        datatype = common.D_128
        codes = ['38']
        min_len = 2
        max_len = 3


class HEADER_REF02(Element):
    """Master Policy Number"""
    class Schema:
        json = {'title': 'Master Policy Number',
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
    """Transaction Set Policy Number"""
    class Schema:
        json = {'title': 'Transaction Set Policy Number',
         'usage': 'S',
         'description': 'xid=REF name=Transaction Set Policy Number',
         'position': 30,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                        'ref02': {'$ref': '#/$elements/HEADER_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02


class HEADER_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['007', '303', '382', '388']}]}}
        datatype = common.D_374
        codes = ['007', '303', '382', '388']
        min_len = 3
        max_len = 3


class HEADER_DTP02(Element):
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


class HEADER_DTP03(Element):
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


class HEADER_DTP(Segment):
    """File Effective Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'File Effective Date',
                   'usage': 'S',
                   'description': 'xid=DTP name=File Effective Date',
                   'position': 40,
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


class L1000A_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['P5']}]}}
        datatype = common.D_98
        codes = ['P5']
        min_len = 2
        max_len = 3


class L1000A_N102(Element):
    """Plan Sponsor Name"""
    class Schema:
        json = {'title': 'Plan Sponsor Name',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000A_N103(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['FI', 'ZZ']
        min_len = 1
        max_len = 2


class L1000A_N104(Element):
    """Sponsor Identifier"""
    class Schema:
        json = {'title': 'Sponsor Identifier',
         'usage': 'R',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000A_N105(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L1000A_N106(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L1000A_N1(Segment):
    """Sponsor Name"""
    class Schema:
        json = {'title': 'Sponsor Name',
         'usage': 'R',
         'description': 'xid=N1 name=Sponsor Name',
         'position': 70,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000A_N101'},
                        'n102': {'$ref': '#/$elements/L1000A_N102'},
                        'n103': {'$ref': '#/$elements/L1000A_N103'},
                        'n104': {'$ref': '#/$elements/L1000A_N104'}},
         'required': ['n101', 'n103', 'n104']}
        segment_name = 'N1'
    n101: L1000A_N101
    n102: L1000A_N102 | None
    n103: L1000A_N103
    n104: L1000A_N104


class L1000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Sponsor Name',
                   'usage': 'R',
                   'description': 'xid=1000A name=Sponsor Name type=None',
                   'position': 70,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000A_N1'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000A_N1


class L1000B_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['IN']}]}}
        datatype = common.D_98
        codes = ['IN']
        min_len = 2
        max_len = 3


class L1000B_N102(Element):
    """Insurer Name"""
    class Schema:
        json = {'title': 'Insurer Name',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000B_N103(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'XV']}]}}
        datatype = common.D_66
        codes = ['FI', 'XV']
        min_len = 1
        max_len = 2


class L1000B_N104(Element):
    """Insurer Identification Code"""
    class Schema:
        json = {'title': 'Insurer Identification Code',
         'usage': 'R',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000B_N105(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L1000B_N106(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L1000B_N1(Segment):
    """Payer"""
    class Schema:
        json = {'title': 'Payer',
         'usage': 'R',
         'description': 'xid=N1 name=Payer',
         'position': 70,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000B_N101'},
                        'n102': {'$ref': '#/$elements/L1000B_N102'},
                        'n103': {'$ref': '#/$elements/L1000B_N103'},
                        'n104': {'$ref': '#/$elements/L1000B_N104'}},
         'required': ['n101', 'n103', 'n104']}
        segment_name = 'N1'
    n101: L1000B_N101
    n102: L1000B_N102 | None
    n103: L1000B_N103
    n104: L1000B_N104


class L1000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer',
                   'usage': 'R',
                   'description': 'xid=1000B name=Payer type=None',
                   'position': 70,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000B_N1'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000B_N1


class L1000C_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['BO', 'TV']}]}}
        datatype = common.D_98
        codes = ['BO', 'TV']
        min_len = 2
        max_len = 3


class L1000C_N102(Element):
    """TPA or Broker Name"""
    class Schema:
        json = {'title': 'TPA or Broker Name',
         'usage': 'R',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000C_N103(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['94', 'FI', 'XV']}]}}
        datatype = common.D_66
        codes = ['94', 'FI', 'XV']
        min_len = 1
        max_len = 2


class L1000C_N104(Element):
    """TPA or Broker Identification Code"""
    class Schema:
        json = {'title': 'TPA or Broker Identification Code',
         'usage': 'R',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1000C_N105(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L1000C_N106(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L1000C_N1(Segment):
    """TPA/Broker Name"""
    class Schema:
        json = {'title': 'TPA/Broker Name',
         'usage': 'R',
         'description': 'xid=N1 name=TPA/Broker Name',
         'position': 70,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000C_N101'},
                        'n102': {'$ref': '#/$elements/L1000C_N102'},
                        'n103': {'$ref': '#/$elements/L1000C_N103'},
                        'n104': {'$ref': '#/$elements/L1000C_N104'}},
         'required': ['n101', 'n102', 'n103', 'n104']}
        segment_name = 'N1'
    n101: L1000C_N101
    n102: L1000C_N102
    n103: L1000C_N103
    n104: L1000C_N104


class L1100C_ACT01(Element):
    """TPA or Broker Account Number"""
    class Schema:
        json = {'title': 'TPA or Broker Account Number',
         'usage': 'R',
         'description': 'xid=ACT01 data_ele=508',
         'sequence': 1,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class L1100C_ACT02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'N',
         'description': 'xid=ACT02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1100C_ACT03(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'N',
         'description': 'xid=ACT03 data_ele=66',
         'sequence': 3,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L1100C_ACT04(Element):
    """Identification Code"""
    class Schema:
        json = {'title': 'Identification Code',
         'usage': 'N',
         'description': 'xid=ACT04 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1100C_ACT05(Element):
    """Account Number Qualifier"""
    class Schema:
        json = {'title': 'Account Number Qualifier',
         'usage': 'N',
         'description': 'xid=ACT05 data_ele=569',
         'sequence': 5,
         'type': {'$ref': '#/$common/569'}}
        datatype = common.D_569
        min_len = 1
        max_len = 3


class L1100C_ACT06(Element):
    """TPA or Broker Account Number"""
    class Schema:
        json = {'title': 'TPA or Broker Account Number',
         'usage': 'S',
         'description': 'xid=ACT06 data_ele=508',
         'sequence': 6,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class L1100C_ACT07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=ACT07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L1100C_ACT08(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'N',
         'description': 'xid=ACT08 data_ele=107',
         'sequence': 8,
         'type': {'$ref': '#/$common/107'}}
        datatype = common.D_107
        min_len = 1
        max_len = 2


class L1100C_ACT09(Element):
    """Benefit Status Code"""
    class Schema:
        json = {'title': 'Benefit Status Code',
         'usage': 'N',
         'description': 'xid=ACT09 data_ele=1216',
         'sequence': 9,
         'type': {'$ref': '#/$common/1216'}}
        datatype = common.D_1216
        min_len = 1
        max_len = 1


class L1100C_ACT(Segment):
    """TPA/Broker Account Information"""
    class Schema:
        json = {'title': 'TPA/Broker Account Information',
         'usage': 'R',
         'description': 'xid=ACT name=TPA/Broker Account Information',
         'position': 120,
         'syntax': ['P0304', 'C0506', 'C0705'],
         'type': 'object',
         'properties': {'xid': {'literal': 'ACT'},
                        'act01': {'$ref': '#/$elements/L1100C_ACT01'},
                        'act06': {'$ref': '#/$elements/L1100C_ACT06'}},
         'required': ['act01']}
        segment_name = 'ACT'
    act01: L1100C_ACT01
    act06: L1100C_ACT06 | None


class L1100C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'TPA/Broker Account Information',
                   'usage': 'S',
                   'description': 'xid=1100C name=TPA/Broker Account Information '
                                  'type=None',
                   'position': 120,
                   'type': 'object',
                   'properties': {'act': {'$ref': '#/$segments/L1100C_ACT'}},
                   'required': ['act']},
         'maxItems': 1}
    act: L1100C_ACT


class L1000C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'TPA/Broker Name',
                   'usage': 'S',
                   'description': 'xid=1000C name=TPA/Broker Name type=None',
                   'position': 70,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000C_N1'},
                                  'l1100c': {'$ref': '#/$segments/L1100C'}},
                   'required': ['n1']},
         'maxItems': 2}
    n1: L1000C_N1
    l1100c: list[L1100C] | None


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 1 - Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Table 1 - Header type=wrapper',
                   'position': 10,
                   'type': 'object',
                   'properties': {'bgn': {'$ref': '#/$segments/HEADER_BGN'},
                                  'ref': {'$ref': '#/$segments/HEADER_REF'},
                                  'dtp': {'$ref': '#/$segments/HEADER_DTP'},
                                  'l1000a': {'$ref': '#/$segments/L1000A'},
                                  'l1000b': {'$ref': '#/$segments/L1000B'},
                                  'l1000c': {'$ref': '#/$segments/L1000C'}},
                   'required': ['bgn', 'l1000a', 'l1000b']},
         'maxItems': 1}
    bgn: HEADER_BGN
    ref: HEADER_REF | None
    dtp: list[HEADER_DTP] | None
    l1000a: list[L1000A]
    l1000b: list[L1000B]
    l1000c: list[L1000C] | None


class L2000_INS01(Element):
    """Insured Indicator"""
    class Schema:
        json = {'title': 'Insured Indicator',
         'usage': 'R',
         'description': 'xid=INS01 data_ele=1073',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1073'}, {'enum': ['N', 'Y']}]}}
        datatype = common.D_1073
        codes = ['N', 'Y']
        min_len = 1
        max_len = 1


class L2000_INS02(Element):
    """Individual Relationship Code"""
    class Schema:
        json = {'title': 'Individual Relationship Code',
         'usage': 'R',
         'description': 'xid=INS02 data_ele=1069',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1069'},
                            {'enum': ['01', '03', '04', '05', '06', '07', '08', '09',
                                      '10', '11', '12', '13', '14', '15', '17', '18',
                                      '19', '23', '24', '25', '26', '31', '32', '33',
                                      '38', '48', '49', '53']}]}}
        datatype = common.D_1069
        codes = ['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '17', '18', '19', '23', '24', '25', '26', '31', '32', '33', '38', '48', '49', '53']
        min_len = 2
        max_len = 2


class L2000_INS03(Element):
    """Maintenance Type Code"""
    class Schema:
        json = {'title': 'Maintenance Type Code',
         'usage': 'R',
         'description': 'xid=INS03 data_ele=875',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/875'},
                            {'enum': ['001', '021', '024', '025', '030']}]}}
        datatype = common.D_875
        codes = ['001', '021', '024', '025', '030']
        min_len = 3
        max_len = 3


class L2000_INS04(Element):
    """Maintenance Reason Code"""
    class Schema:
        json = {'title': 'Maintenance Reason Code',
         'usage': 'S',
         'description': 'xid=INS04 data_ele=1203',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1203'},
                            {'enum': ['01', '02', '03', '04', '05', '06', '07', '08',
                                      '09', '10', '11', '14', '15', '16', '17', '18',
                                      '20', '21', '22', '25', '26', '27', '28', '29',
                                      '31', '32', '33', '37', '38', '39', '40', '41',
                                      '43', 'AI', 'XN', 'XT']}]}}
        datatype = common.D_1203
        codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '14', '15', '16', '17', '18', '20', '21', '22', '25', '26', '27', '28', '29', '31', '32', '33', '37', '38', '39', '40', '41', '43', 'AI', 'XN', 'XT']
        min_len = 2
        max_len = 3


class L2000_INS05(Element):
    """Benefit Status Code"""
    class Schema:
        json = {'title': 'Benefit Status Code',
         'usage': 'R',
         'description': 'xid=INS05 data_ele=1216',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1216'},
                            {'enum': ['A', 'C', 'S', 'T']}]}}
        datatype = common.D_1216
        codes = ['A', 'C', 'S', 'T']
        min_len = 1
        max_len = 1


class L2000_INS06(Element):
    """Medicare Plan Code"""
    class Schema:
        json = {'title': 'Medicare Plan Code',
         'usage': 'S',
         'description': 'xid=INS06 data_ele=1218',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1218'},
                            {'enum': ['A', 'B', 'C', 'D', 'E']}]}}
        datatype = common.D_1218
        codes = ['A', 'B', 'C', 'D', 'E']
        min_len = 1
        max_len = 1


class L2000_INS07(Element):
    """Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event Code"""
    class Schema:
        json = {'title': 'Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying '
                  'Event Code',
         'usage': 'S',
         'description': 'xid=INS07 data_ele=1219',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/1219'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7', '8']}]}}
        datatype = common.D_1219
        codes = ['1', '2', '3', '4', '5', '6', '7', '8']
        min_len = 1
        max_len = 2


class L2000_INS08(Element):
    """Employment Status Code"""
    class Schema:
        json = {'title': 'Employment Status Code',
         'usage': 'S',
         'description': 'xid=INS08 data_ele=584',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/584'},
                            {'enum': ['AO', 'AU', 'FT', 'L1', 'PT', 'RT', 'TE']}]}}
        datatype = common.D_584
        codes = ['AO', 'AU', 'FT', 'L1', 'PT', 'RT', 'TE']
        min_len = 2
        max_len = 2


class L2000_INS09(Element):
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


class L2000_INS10(Element):
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


class L2000_INS11(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'S',
         'description': 'xid=INS11 data_ele=1250',
         'sequence': 11,
         'type': {'allOf': [{'$ref': '#/$common/1250'}, {'enum': ['D8']}]}}
        datatype = common.D_1250
        codes = ['D8']
        min_len = 2
        max_len = 3


class L2000_INS12(Element):
    """Insured Individual Death Date"""
    class Schema:
        json = {'title': 'Insured Individual Death Date',
         'usage': 'S',
         'description': 'xid=INS12 data_ele=1251',
         'sequence': 12,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000_INS13(Element):
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


class L2000_INS14(Element):
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


class L2000_INS15(Element):
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


class L2000_INS16(Element):
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


class L2000_INS17(Element):
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


class L2000_INS(Segment):
    """Member Level Detail"""
    class Schema:
        json = {'title': 'Member Level Detail',
         'usage': 'R',
         'description': 'xid=INS name=Member Level Detail',
         'position': 10,
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
    ins17: L2000_INS17 | None


class L2000_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['0F']}]}}
        datatype = common.D_128
        codes = ['0F']
        min_len = 2
        max_len = 3


class L2000_REF02(Element):
    """Subscriber Identifier"""
    class Schema:
        json = {'title': 'Subscriber Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000_REF03(Element):
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


class L2000_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000_REF(Segment):
    """Subscriber Number"""
    class Schema:
        json = {'title': 'Subscriber Number',
         'usage': 'R',
         'description': 'xid=REF name=Subscriber Number',
         'position': 20,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2000_REF01'},
                        'ref02': {'$ref': '#/$elements/L2000_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2000_REF01
    ref02: L2000_REF02


class L2000_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['1L']}]}}
        datatype = common.D_128
        codes = ['1L']
        min_len = 2
        max_len = 3


class L2000_REF02(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000_REF03(Element):
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


class L2000_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000_REF(Segment):
    """Member Policy Number"""
    class Schema:
        json = {'title': 'Member Policy Number',
         'usage': 'S',
         'description': 'xid=REF name=Member Policy Number',
         'position': 20,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2000_REF01'},
                        'ref02': {'$ref': '#/$elements/L2000_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2000_REF01
    ref02: L2000_REF02


class L2000_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['17', '23', '3H', '6O', 'DX', 'F6', 'Q4',
                                      'ZZ']}]}}
        datatype = common.D_128
        codes = ['17', '23', '3H', '6O', 'DX', 'F6', 'Q4', 'ZZ']
        min_len = 2
        max_len = 3


class L2000_REF02(Element):
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


class L2000_REF03(Element):
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


class L2000_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000_REF(Segment):
    """Member Identification Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Identification Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Member Identification Number',
                   'position': 20,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2000_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2000_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2000_REF01
    ref02: L2000_REF02


class L2000_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['QQ']}]}}
        datatype = common.D_128
        codes = ['QQ']
        min_len = 2
        max_len = 3


class L2000_REF02(Element):
    """Prior Coverage Month Count"""
    class Schema:
        json = {'title': 'Prior Coverage Month Count',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000_REF03(Element):
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


class L2000_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2000_REF(Segment):
    """Prior Coverage Months"""
    class Schema:
        json = {'title': 'Prior Coverage Months',
         'usage': 'S',
         'description': 'xid=REF name=Prior Coverage Months',
         'position': 20,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2000_REF01'},
                        'ref02': {'$ref': '#/$elements/L2000_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2000_REF01
    ref02: L2000_REF02


class L2000_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['286', '296', '297', '300', '301', '303', '336',
                                      '337', '338', '339', '340', '341', '350', '351',
                                      '356', '357', '383', '393', '394', '473',
                                      '474']}]}}
        datatype = common.D_374
        codes = ['286', '296', '297', '300', '301', '303', '336', '337', '338', '339', '340', '341', '350', '351', '356', '357', '383', '393', '394', '473', '474']
        min_len = 3
        max_len = 3


class L2000_DTP02(Element):
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


class L2000_DTP03(Element):
    """Status Information Effective Date"""
    class Schema:
        json = {'title': 'Status Information Effective Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2000_DTP(Segment):
    """Member Level Dates"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Level Dates',
                   'usage': 'S',
                   'description': 'xid=DTP name=Member Level Dates',
                   'position': 25,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2000_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2000_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2000_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 20}
        segment_name = 'DTP'
    dtp01: L2000_DTP01
    dtp02: L2000_DTP02
    dtp03: L2000_DTP03


class L2100A_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['74', 'IL']}]}}
        datatype = common.D_98
        codes = ['74', 'IL']
        min_len = 2
        max_len = 3


class L2100A_NM102(Element):
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


class L2100A_NM103(Element):
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


class L2100A_NM104(Element):
    """Subscriber First Name"""
    class Schema:
        json = {'title': 'Subscriber First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100A_NM105(Element):
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


class L2100A_NM106(Element):
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


class L2100A_NM107(Element):
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


class L2100A_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100A_NM109(Element):
    """Subscriber Identifier"""
    class Schema:
        json = {'title': 'Subscriber Identifier',
         'usage': 'S',
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
    """Member Name"""
    class Schema:
        json = {'title': 'Member Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Member Name',
         'position': 30,
         'syntax': ['P0809', 'C1110'],
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
                        'nm109': {'$ref': '#/$elements/L2100A_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm104']}
        segment_name = 'NM1'
    nm101: L2100A_NM101
    nm102: L2100A_NM102
    nm103: L2100A_NM103
    nm104: L2100A_NM104
    nm105: L2100A_NM105 | None
    nm106: L2100A_NM106 | None
    nm107: L2100A_NM107 | None
    nm108: L2100A_NM108 | None
    nm109: L2100A_NM109 | None


class L2100A_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['IP']}]}}
        datatype = common.D_366
        codes = ['IP']
        min_len = 2
        max_len = 2


class L2100A_PER02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'N',
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
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100A_PER04(Element):
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


class L2100A_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100A_PER06(Element):
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


class L2100A_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100A_PER08(Element):
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
    """Member Communications Numbers"""
    class Schema:
        json = {'title': 'Member Communications Numbers',
         'usage': 'S',
         'description': 'xid=PER name=Member Communications Numbers',
         'position': 40,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100A_PER01'},
                        'per03': {'$ref': '#/$elements/L2100A_PER03'},
                        'per04': {'$ref': '#/$elements/L2100A_PER04'},
                        'per05': {'$ref': '#/$elements/L2100A_PER05'},
                        'per06': {'$ref': '#/$elements/L2100A_PER06'},
                        'per07': {'$ref': '#/$elements/L2100A_PER07'},
                        'per08': {'$ref': '#/$elements/L2100A_PER08'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100A_PER01
    per03: L2100A_PER03
    per04: L2100A_PER04
    per05: L2100A_PER05 | None
    per06: L2100A_PER06 | None
    per07: L2100A_PER07 | None
    per08: L2100A_PER08 | None


class L2100A_N301(Element):
    """Subscriber Address Line"""
    class Schema:
        json = {'title': 'Subscriber Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100A_N302(Element):
    """Subscriber Address Line"""
    class Schema:
        json = {'title': 'Subscriber Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100A_N3(Segment):
    """Member Residence Street Address"""
    class Schema:
        json = {'title': 'Member Residence Street Address',
         'usage': 'S',
         'description': 'xid=N3 name=Member Residence Street Address',
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100A_N301'},
                        'n302': {'$ref': '#/$elements/L2100A_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100A_N301
    n302: L2100A_N302 | None


class L2100A_N401(Element):
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


class L2100A_N402(Element):
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


class L2100A_N403(Element):
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


class L2100A_N404(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'S',
         'description': 'xid=N404 data_ele=26',
         'sequence': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L2100A_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['60', 'CY']}]}}
        datatype = common.D_309
        codes = ['60', 'CY']
        min_len = 1
        max_len = 2


class L2100A_N406(Element):
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


class L2100A_N4(Segment):
    """Member Residence City, State, Zip Code"""
    class Schema:
        json = {'title': 'Member Residence City, State, Zip Code',
         'usage': 'S',
         'description': 'xid=N4 name=Member Residence City, State, Zip Code',
         'position': 60,
         'syntax': ['C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100A_N401'},
                        'n402': {'$ref': '#/$elements/L2100A_N402'},
                        'n403': {'$ref': '#/$elements/L2100A_N403'},
                        'n404': {'$ref': '#/$elements/L2100A_N404'},
                        'n405': {'$ref': '#/$elements/L2100A_N405'},
                        'n406': {'$ref': '#/$elements/L2100A_N406'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2100A_N401
    n402: L2100A_N402
    n403: L2100A_N403
    n404: L2100A_N404 | None
    n405: L2100A_N405 | None
    n406: L2100A_N406 | None


class L2100A_DMG01(Element):
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


class L2100A_DMG02(Element):
    """Member Birth Date"""
    class Schema:
        json = {'title': 'Member Birth Date',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100A_DMG03(Element):
    """Gender Code"""
    class Schema:
        json = {'title': 'Gender Code',
         'usage': 'R',
         'description': 'xid=DMG03 data_ele=1068',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2100A_DMG04(Element):
    """Marital Status Code"""
    class Schema:
        json = {'title': 'Marital Status Code',
         'usage': 'S',
         'description': 'xid=DMG04 data_ele=1067',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1067'},
                            {'enum': ['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X']}]}}
        datatype = common.D_1067
        codes = ['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X']
        min_len = 1
        max_len = 1


class L2100A_DMG05(Element):
    """Race or Ethnicity Code"""
    class Schema:
        json = {'title': 'Race or Ethnicity Code',
         'usage': 'S',
         'description': 'xid=DMG05 data_ele=1109',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1109'},
                            {'enum': ['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                      'I', 'J', 'N', 'O', 'P', 'Z']}]}}
        datatype = common.D_1109
        codes = ['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'N', 'O', 'P', 'Z']
        min_len = 1
        max_len = 1


class L2100A_DMG06(Element):
    """Citizenship Status Code"""
    class Schema:
        json = {'title': 'Citizenship Status Code',
         'usage': 'S',
         'description': 'xid=DMG06 data_ele=1066',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1066'},
                            {'enum': ['1', '2', '3', '4', '5', '6', '7']}]}}
        datatype = common.D_1066
        codes = ['1', '2', '3', '4', '5', '6', '7']
        min_len = 1
        max_len = 2


class L2100A_DMG07(Element):
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


class L2100A_DMG08(Element):
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


class L2100A_DMG09(Element):
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


class L2100A_DMG(Segment):
    """Member Demographics"""
    class Schema:
        json = {'title': 'Member Demographics',
         'usage': 'S',
         'description': 'xid=DMG name=Member Demographics',
         'position': 80,
         'syntax': ['P0102'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2100A_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2100A_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2100A_DMG03'},
                        'dmg04': {'$ref': '#/$elements/L2100A_DMG04'},
                        'dmg05': {'$ref': '#/$elements/L2100A_DMG05'},
                        'dmg06': {'$ref': '#/$elements/L2100A_DMG06'}},
         'required': ['dmg01', 'dmg02', 'dmg03']}
        segment_name = 'DMG'
    dmg01: L2100A_DMG01
    dmg02: L2100A_DMG02
    dmg03: L2100A_DMG03
    dmg04: L2100A_DMG04 | None
    dmg05: L2100A_DMG05 | None
    dmg06: L2100A_DMG06 | None


class L2100A_ICM01(Element):
    """Frequency Code"""
    class Schema:
        json = {'title': 'Frequency Code',
         'usage': 'R',
         'description': 'xid=ICM01 data_ele=594',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/594'},
                            {'enum': ['1', '2', '3', '4', '6', '7', '8', '9', 'B', 'C',
                                      'H', 'Q', 'S', 'U']}]}}
        datatype = common.D_594
        codes = ['1', '2', '3', '4', '6', '7', '8', '9', 'B', 'C', 'H', 'Q', 'S', 'U']
        min_len = 1
        max_len = 1


class L2100A_ICM02(Element):
    """Wage Amount"""
    class Schema:
        json = {'title': 'Wage Amount',
         'usage': 'R',
         'description': 'xid=ICM02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100A_ICM03(Element):
    """Work Hours Count"""
    class Schema:
        json = {'title': 'Work Hours Count',
         'usage': 'S',
         'description': 'xid=ICM03 data_ele=380',
         'sequence': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100A_ICM04(Element):
    """Location Identification Code"""
    class Schema:
        json = {'title': 'Location Identification Code',
         'usage': 'S',
         'description': 'xid=ICM04 data_ele=310',
         'sequence': 4,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L2100A_ICM05(Element):
    """Salary Grade Code"""
    class Schema:
        json = {'title': 'Salary Grade Code',
         'usage': 'S',
         'description': 'xid=ICM05 data_ele=1214',
         'sequence': 5,
         'type': {'$ref': '#/$common/1214'}}
        datatype = common.D_1214
        min_len = 1
        max_len = 5


class L2100A_ICM06(Element):
    """Currency Code"""
    class Schema:
        json = {'title': 'Currency Code',
         'usage': 'N',
         'description': 'xid=ICM06 data_ele=100',
         'sequence': 6,
         'type': {'$ref': '#/$common/100'}}
        datatype = common.D_100
        min_len = 3
        max_len = 3


class L2100A_ICM(Segment):
    """Member Income"""
    class Schema:
        json = {'title': 'Member Income',
         'usage': 'S',
         'description': 'xid=ICM name=Member Income',
         'position': 110,
         'type': 'object',
         'properties': {'xid': {'literal': 'ICM'},
                        'icm01': {'$ref': '#/$elements/L2100A_ICM01'},
                        'icm02': {'$ref': '#/$elements/L2100A_ICM02'},
                        'icm03': {'$ref': '#/$elements/L2100A_ICM03'},
                        'icm04': {'$ref': '#/$elements/L2100A_ICM04'},
                        'icm05': {'$ref': '#/$elements/L2100A_ICM05'}},
         'required': ['icm01', 'icm02']}
        segment_name = 'ICM'
    icm01: L2100A_ICM01
    icm02: L2100A_ICM02
    icm03: L2100A_ICM03 | None
    icm04: L2100A_ICM04 | None
    icm05: L2100A_ICM05 | None


class L2100A_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['B9', 'C1', 'D2', 'P3']}]}}
        datatype = common.D_522
        codes = ['B9', 'C1', 'D2', 'P3']
        min_len = 1
        max_len = 3


class L2100A_AMT02(Element):
    """Contract Amount"""
    class Schema:
        json = {'title': 'Contract Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100A_AMT03(Element):
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


class L2100A_AMT(Segment):
    """Member Policy Amounts"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Policy Amounts',
                   'usage': 'S',
                   'description': 'xid=AMT name=Member Policy Amounts',
                   'position': 120,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2100A_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2100A_AMT02'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 4}
        segment_name = 'AMT'
    amt01: L2100A_AMT01
    amt02: L2100A_AMT02


class L2100A_HLH01(Element):
    """Health Related Code"""
    class Schema:
        json = {'title': 'Health Related Code',
         'usage': 'S',
         'description': 'xid=HLH01 data_ele=1212',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1212'},
                            {'enum': ['N', 'S', 'T', 'U', 'X']}]}}
        datatype = common.D_1212
        codes = ['N', 'S', 'T', 'U', 'X']
        min_len = 1
        max_len = 1


class L2100A_HLH02(Element):
    """Member Height"""
    class Schema:
        json = {'title': 'Member Height',
         'usage': 'S',
         'description': 'xid=HLH02 data_ele=65',
         'sequence': 2,
         'type': {'$ref': '#/$common/65'}}
        datatype = common.D_65
        min_len = 1
        max_len = 8


class L2100A_HLH03(Element):
    """Member Weight"""
    class Schema:
        json = {'title': 'Member Weight',
         'usage': 'S',
         'description': 'xid=HLH03 data_ele=81',
         'sequence': 3,
         'type': {'$ref': '#/$common/81'}}
        datatype = common.D_81
        min_len = 1
        max_len = 10


class L2100A_HLH04(Element):
    """Weight"""
    class Schema:
        json = {'title': 'Weight',
         'usage': 'N',
         'description': 'xid=HLH04 data_ele=81',
         'sequence': 4,
         'type': {'$ref': '#/$common/81'}}
        datatype = common.D_81
        min_len = 1
        max_len = 10


class L2100A_HLH05(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=HLH05 data_ele=352',
         'sequence': 5,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100A_HLH06(Element):
    """Current Health Condition Code"""
    class Schema:
        json = {'title': 'Current Health Condition Code',
         'usage': 'N',
         'description': 'xid=HLH06 data_ele=1213',
         'sequence': 6,
         'type': {'$ref': '#/$common/1213'}}
        datatype = common.D_1213
        min_len = 1
        max_len = 1


class L2100A_HLH07(Element):
    """Description"""
    class Schema:
        json = {'title': 'Description',
         'usage': 'N',
         'description': 'xid=HLH07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100A_HLH(Segment):
    """Member Health Information"""
    class Schema:
        json = {'title': 'Member Health Information',
         'usage': 'S',
         'description': 'xid=HLH name=Member Health Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'HLH'},
                        'hlh01': {'$ref': '#/$elements/L2100A_HLH01'},
                        'hlh02': {'$ref': '#/$elements/L2100A_HLH02'},
                        'hlh03': {'$ref': '#/$elements/L2100A_HLH03'}}}
        segment_name = 'HLH'
    hlh01: L2100A_HLH01 | None
    hlh02: L2100A_HLH02 | None
    hlh03: L2100A_HLH03 | None


class L2100A_LUI01(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=LUI01 data_ele=66',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['LD', 'LE']}]}}
        datatype = common.D_66
        codes = ['LD', 'LE']
        min_len = 1
        max_len = 2


class L2100A_LUI02(Element):
    """Language Code"""
    class Schema:
        json = {'title': 'Language Code',
         'usage': 'S',
         'description': 'xid=LUI02 data_ele=67',
         'sequence': 2,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100A_LUI03(Element):
    """Language Description"""
    class Schema:
        json = {'title': 'Language Description',
         'usage': 'S',
         'description': 'xid=LUI03 data_ele=352',
         'sequence': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100A_LUI04(Element):
    """Language Use Indicator"""
    class Schema:
        json = {'title': 'Language Use Indicator',
         'usage': 'S',
         'description': 'xid=LUI04 data_ele=1303',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/1303'}, {'enum': ['5', '7', '8']}]}}
        datatype = common.D_1303
        codes = ['5', '7', '8']
        min_len = 1
        max_len = 2


class L2100A_LUI05(Element):
    """Language Proficiency Indicator"""
    class Schema:
        json = {'title': 'Language Proficiency Indicator',
         'usage': 'N',
         'description': 'xid=LUI05 data_ele=1476',
         'sequence': 5,
         'type': {'$ref': '#/$common/1476'}}
        datatype = common.D_1476
        min_len = 1
        max_len = 1


class L2100A_LUI(Segment):
    """Member Language"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Language',
                   'usage': 'S',
                   'description': 'xid=LUI name=Member Language',
                   'position': 150,
                   'syntax': ['P0102', 'L040203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'LUI'},
                                  'lui01': {'$ref': '#/$elements/L2100A_LUI01'},
                                  'lui02': {'$ref': '#/$elements/L2100A_LUI02'},
                                  'lui03': {'$ref': '#/$elements/L2100A_LUI03'},
                                  'lui04': {'$ref': '#/$elements/L2100A_LUI04'}}},
         'maxItems': 5}
        segment_name = 'LUI'
    lui01: L2100A_LUI01 | None
    lui02: L2100A_LUI02 | None
    lui03: L2100A_LUI03 | None
    lui04: L2100A_LUI04 | None


class L2100A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Name',
                   'usage': 'R',
                   'description': 'xid=2100A name=Member Name type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100A_NM1'},
                                  'per': {'$ref': '#/$segments/L2100A_PER'},
                                  'n3': {'$ref': '#/$segments/L2100A_N3'},
                                  'n4': {'$ref': '#/$segments/L2100A_N4'},
                                  'dmg': {'$ref': '#/$segments/L2100A_DMG'},
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
    icm: L2100A_ICM | None
    amt: list[L2100A_AMT] | None
    hlh: L2100A_HLH | None
    lui: list[L2100A_LUI] | None


class L2100B_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['70']}]}}
        datatype = common.D_98
        codes = ['70']
        min_len = 2
        max_len = 3


class L2100B_NM102(Element):
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


class L2100B_NM103(Element):
    """Prior Incorrect Insured Last Name"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100B_NM104(Element):
    """Prior Incorrect Insured First Name"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100B_NM105(Element):
    """Prior Incorrect Insured Middle Name"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100B_NM106(Element):
    """Prior Incorrect Insured Name Prefix"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured Name Prefix',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100B_NM107(Element):
    """Prior Incorrect Insured Name Suffix"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured Name Suffix',
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
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100B_NM109(Element):
    """Prior Incorrect Insured Identifier"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured Identifier',
         'usage': 'S',
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
    """Incorrect Member Name"""
    class Schema:
        json = {'title': 'Incorrect Member Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Incorrect Member Name',
         'position': 30,
         'syntax': ['P0809', 'C1110'],
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
         'required': ['nm101', 'nm102', 'nm103', 'nm104']}
        segment_name = 'NM1'
    nm101: L2100B_NM101
    nm102: L2100B_NM102
    nm103: L2100B_NM103
    nm104: L2100B_NM104
    nm105: L2100B_NM105 | None
    nm106: L2100B_NM106 | None
    nm107: L2100B_NM107 | None
    nm108: L2100B_NM108 | None
    nm109: L2100B_NM109 | None


class L2100B_DMG01(Element):
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


class L2100B_DMG02(Element):
    """Prior Incorrect Insured Birth Date"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured Birth Date',
         'usage': 'R',
         'description': 'xid=DMG02 data_ele=1251',
         'sequence': 2,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100B_DMG03(Element):
    """Prior Incorrect Insured Gender Code"""
    class Schema:
        json = {'title': 'Prior Incorrect Insured Gender Code',
         'usage': 'R',
         'description': 'xid=DMG03 data_ele=1068',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1068'}, {'enum': ['F', 'M', 'U']}]}}
        datatype = common.D_1068
        codes = ['F', 'M', 'U']
        min_len = 1
        max_len = 1


class L2100B_DMG04(Element):
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


class L2100B_DMG05(Element):
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


class L2100B_DMG06(Element):
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


class L2100B_DMG07(Element):
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


class L2100B_DMG08(Element):
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


class L2100B_DMG09(Element):
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


class L2100B_DMG(Segment):
    """Incorrect Member Demographics"""
    class Schema:
        json = {'title': 'Incorrect Member Demographics',
         'usage': 'S',
         'description': 'xid=DMG name=Incorrect Member Demographics',
         'position': 80,
         'syntax': ['P0102'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DMG'},
                        'dmg01': {'$ref': '#/$elements/L2100B_DMG01'},
                        'dmg02': {'$ref': '#/$elements/L2100B_DMG02'},
                        'dmg03': {'$ref': '#/$elements/L2100B_DMG03'}},
         'required': ['dmg01', 'dmg02', 'dmg03']}
        segment_name = 'DMG'
    dmg01: L2100B_DMG01
    dmg02: L2100B_DMG02
    dmg03: L2100B_DMG03


class L2100B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Incorrect Member Name',
                   'usage': 'S',
                   'description': 'xid=2100B name=Incorrect Member Name type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100B_NM1'},
                                  'dmg': {'$ref': '#/$segments/L2100B_DMG'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100B_NM1
    dmg: L2100B_DMG | None


class L2100C_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['31']}]}}
        datatype = common.D_98
        codes = ['31']
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


class L2100C_NM104(Element):
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


class L2100C_NM105(Element):
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


class L2100C_NM108(Element):
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


class L2100C_NM109(Element):
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
    """Member Mailing Address"""
    class Schema:
        json = {'title': 'Member Mailing Address',
         'usage': 'R',
         'description': 'xid=NM1 name=Member Mailing Address',
         'position': 30,
         'syntax': ['P0809', 'C1110'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100C_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100C_NM102'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100C_NM101
    nm102: L2100C_NM102


class L2100C_N301(Element):
    """Subscriber Address Line"""
    class Schema:
        json = {'title': 'Subscriber Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100C_N302(Element):
    """Subscriber Address Line"""
    class Schema:
        json = {'title': 'Subscriber Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100C_N3(Segment):
    """Member Mail Street Address"""
    class Schema:
        json = {'title': 'Member Mail Street Address',
         'usage': 'S',
         'description': 'xid=N3 name=Member Mail Street Address',
         'position': 50,
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
         'usage': 'R',
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
         'usage': 'R',
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
         'usage': 'R',
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
    """Member Mail City, State, Zip"""
    class Schema:
        json = {'title': 'Member Mail City, State, Zip',
         'usage': 'S',
         'description': 'xid=N4 name=Member Mail City, State, Zip',
         'position': 60,
         'syntax': ['C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100C_N401'},
                        'n402': {'$ref': '#/$elements/L2100C_N402'},
                        'n403': {'$ref': '#/$elements/L2100C_N403'},
                        'n404': {'$ref': '#/$elements/L2100C_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2100C_N401
    n402: L2100C_N402
    n403: L2100C_N403
    n404: L2100C_N404 | None


class L2100C(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Mailing Address',
                   'usage': 'S',
                   'description': 'xid=2100C name=Member Mailing Address type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100C_NM1'},
                                  'n3': {'$ref': '#/$segments/L2100C_N3'},
                                  'n4': {'$ref': '#/$segments/L2100C_N4'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100C_NM1
    n3: L2100C_N3 | None
    n4: L2100C_N4 | None


class L2100D_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['ES']}]}}
        datatype = common.D_98
        codes = ['ES']
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
    """Insured Employer Name"""
    class Schema:
        json = {'title': 'Insured Employer Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100D_NM104(Element):
    """Insured Employer First Name"""
    class Schema:
        json = {'title': 'Insured Employer First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100D_NM105(Element):
    """Insured Employer Middle Name"""
    class Schema:
        json = {'title': 'Insured Employer Middle Name',
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
    """Insured Employer Name Suffix"""
    class Schema:
        json = {'title': 'Insured Employer Name Suffix',
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
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['ZZ']}]}}
        datatype = common.D_66
        codes = ['ZZ']
        min_len = 1
        max_len = 2


class L2100D_NM109(Element):
    """Insured Employer Identifier"""
    class Schema:
        json = {'title': 'Insured Employer Identifier',
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
    """Member Employer"""
    class Schema:
        json = {'title': 'Member Employer',
         'usage': 'R',
         'description': 'xid=NM1 name=Member Employer',
         'position': 30,
         'syntax': ['P0809', 'C1110'],
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


class L2100D_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['EP']}]}}
        datatype = common.D_366
        codes = ['EP']
        min_len = 2
        max_len = 2


class L2100D_PER02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'N',
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
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100D_PER04(Element):
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


class L2100D_PER05(Element):
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


class L2100D_PER06(Element):
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


class L2100D_PER07(Element):
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


class L2100D_PER08(Element):
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
    """Member Employer Communications Numbers"""
    class Schema:
        json = {'title': 'Member Employer Communications Numbers',
         'usage': 'S',
         'description': 'xid=PER name=Member Employer Communications Numbers',
         'position': 40,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100D_PER01'},
                        'per03': {'$ref': '#/$elements/L2100D_PER03'},
                        'per04': {'$ref': '#/$elements/L2100D_PER04'},
                        'per05': {'$ref': '#/$elements/L2100D_PER05'},
                        'per06': {'$ref': '#/$elements/L2100D_PER06'},
                        'per07': {'$ref': '#/$elements/L2100D_PER07'},
                        'per08': {'$ref': '#/$elements/L2100D_PER08'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100D_PER01
    per03: L2100D_PER03
    per04: L2100D_PER04
    per05: L2100D_PER05 | None
    per06: L2100D_PER06 | None
    per07: L2100D_PER07 | None
    per08: L2100D_PER08 | None


class L2100D_N301(Element):
    """Insured Employer Address Line"""
    class Schema:
        json = {'title': 'Insured Employer Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100D_N302(Element):
    """Insured Employer Address Line"""
    class Schema:
        json = {'title': 'Insured Employer Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100D_N3(Segment):
    """Member Employer Street Address"""
    class Schema:
        json = {'title': 'Member Employer Street Address',
         'usage': 'S',
         'description': 'xid=N3 name=Member Employer Street Address',
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100D_N301'},
                        'n302': {'$ref': '#/$elements/L2100D_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100D_N301
    n302: L2100D_N302 | None


class L2100D_N401(Element):
    """Insured Employer City Name"""
    class Schema:
        json = {'title': 'Insured Employer City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100D_N402(Element):
    """Insured Employer State Code"""
    class Schema:
        json = {'title': 'Insured Employer State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100D_N403(Element):
    """Insured Employer Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Insured Employer Postal Zone or ZIP Code',
         'usage': 'R',
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
    """Member Employer City, State, Zip"""
    class Schema:
        json = {'title': 'Member Employer City, State, Zip',
         'usage': 'S',
         'description': 'xid=N4 name=Member Employer City, State, Zip',
         'position': 60,
         'syntax': ['C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100D_N401'},
                        'n402': {'$ref': '#/$elements/L2100D_N402'},
                        'n403': {'$ref': '#/$elements/L2100D_N403'},
                        'n404': {'$ref': '#/$elements/L2100D_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2100D_N401
    n402: L2100D_N402
    n403: L2100D_N403
    n404: L2100D_N404 | None


class L2100D(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Employer',
                   'usage': 'S',
                   'description': 'xid=2100D name=Member Employer type=None',
                   'position': 30,
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
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['M8']}]}}
        datatype = common.D_98
        codes = ['M8']
        min_len = 2
        max_len = 3


class L2100E_NM102(Element):
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


class L2100E_NM103(Element):
    """School Name"""
    class Schema:
        json = {'title': 'School Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100E_NM104(Element):
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


class L2100E_NM105(Element):
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


class L2100E_NM1(Segment):
    """Member School"""
    class Schema:
        json = {'title': 'Member School',
         'usage': 'R',
         'description': 'xid=NM1 name=Member School',
         'position': 30,
         'syntax': ['P0809', 'C1110'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100E_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100E_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100E_NM103'}},
         'required': ['nm101', 'nm102', 'nm103']}
        segment_name = 'NM1'
    nm101: L2100E_NM101
    nm102: L2100E_NM102
    nm103: L2100E_NM103


class L2100E_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['SK']}]}}
        datatype = common.D_366
        codes = ['SK']
        min_len = 2
        max_len = 2


class L2100E_PER02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100E_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100E_PER04(Element):
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


class L2100E_PER05(Element):
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


class L2100E_PER06(Element):
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


class L2100E_PER07(Element):
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


class L2100E_PER08(Element):
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


class L2100E_PER09(Element):
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


class L2100E_PER(Segment):
    """Member School Communications Numbers"""
    class Schema:
        json = {'title': 'Member School Communications Numbers',
         'usage': 'S',
         'description': 'xid=PER name=Member School Communications Numbers',
         'position': 40,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100E_PER01'},
                        'per03': {'$ref': '#/$elements/L2100E_PER03'},
                        'per04': {'$ref': '#/$elements/L2100E_PER04'},
                        'per05': {'$ref': '#/$elements/L2100E_PER05'},
                        'per06': {'$ref': '#/$elements/L2100E_PER06'},
                        'per07': {'$ref': '#/$elements/L2100E_PER07'},
                        'per08': {'$ref': '#/$elements/L2100E_PER08'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100E_PER01
    per03: L2100E_PER03
    per04: L2100E_PER04
    per05: L2100E_PER05 | None
    per06: L2100E_PER06 | None
    per07: L2100E_PER07 | None
    per08: L2100E_PER08 | None


class L2100E_N301(Element):
    """School Address Line"""
    class Schema:
        json = {'title': 'School Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100E_N302(Element):
    """School Address Line"""
    class Schema:
        json = {'title': 'School Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100E_N3(Segment):
    """Member School Street Address"""
    class Schema:
        json = {'title': 'Member School Street Address',
         'usage': 'S',
         'description': 'xid=N3 name=Member School Street Address',
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100E_N301'},
                        'n302': {'$ref': '#/$elements/L2100E_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100E_N301
    n302: L2100E_N302 | None


class L2100E_N401(Element):
    """School City Name"""
    class Schema:
        json = {'title': 'School City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100E_N402(Element):
    """School State Code"""
    class Schema:
        json = {'title': 'School State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100E_N403(Element):
    """School Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'School Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100E_N404(Element):
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


class L2100E_N405(Element):
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


class L2100E_N406(Element):
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


class L2100E_N4(Segment):
    """Member School City, State, Zip"""
    class Schema:
        json = {'title': 'Member School City, State, Zip',
         'usage': 'S',
         'description': 'xid=N4 name=Member School City, State, Zip',
         'position': 60,
         'syntax': ['C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100E_N401'},
                        'n402': {'$ref': '#/$elements/L2100E_N402'},
                        'n403': {'$ref': '#/$elements/L2100E_N403'},
                        'n404': {'$ref': '#/$elements/L2100E_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2100E_N401
    n402: L2100E_N402
    n403: L2100E_N403
    n404: L2100E_N404 | None


class L2100E(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member School',
                   'usage': 'S',
                   'description': 'xid=2100E name=Member School type=None',
                   'position': 30,
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
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['S3']}]}}
        datatype = common.D_98
        codes = ['S3']
        min_len = 2
        max_len = 3


class L2100F_NM102(Element):
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


class L2100F_NM103(Element):
    """Custodial Parent Last Name"""
    class Schema:
        json = {'title': 'Custodial Parent Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100F_NM104(Element):
    """Custodial Parent First Name"""
    class Schema:
        json = {'title': 'Custodial Parent First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100F_NM105(Element):
    """Custodial Parent Middle Name"""
    class Schema:
        json = {'title': 'Custodial Parent Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100F_NM106(Element):
    """Custodial Parent Name Prefix"""
    class Schema:
        json = {'title': 'Custodial Parent Name Prefix',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100F_NM107(Element):
    """Custodial Parent Name Suffix"""
    class Schema:
        json = {'title': 'Custodial Parent Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100F_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100F_NM109(Element):
    """Custodial Parent Identifier"""
    class Schema:
        json = {'title': 'Custodial Parent Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100F_NM110(Element):
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


class L2100F_NM111(Element):
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


class L2100F_NM1(Segment):
    """Custodial Parent"""
    class Schema:
        json = {'title': 'Custodial Parent',
         'usage': 'R',
         'description': 'xid=NM1 name=Custodial Parent',
         'position': 30,
         'syntax': ['P0809', 'C1110'],
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
                        'nm109': {'$ref': '#/$elements/L2100F_NM109'}},
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


class L2100F_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['PQ']}]}}
        datatype = common.D_366
        codes = ['PQ']
        min_len = 2
        max_len = 2


class L2100F_PER02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100F_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100F_PER04(Element):
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


class L2100F_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100F_PER06(Element):
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


class L2100F_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100F_PER08(Element):
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


class L2100F_PER09(Element):
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


class L2100F_PER(Segment):
    """Custodial Parent Communications Numbers"""
    class Schema:
        json = {'title': 'Custodial Parent Communications Numbers',
         'usage': 'S',
         'description': 'xid=PER name=Custodial Parent Communications Numbers',
         'position': 40,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100F_PER01'},
                        'per03': {'$ref': '#/$elements/L2100F_PER03'},
                        'per04': {'$ref': '#/$elements/L2100F_PER04'},
                        'per05': {'$ref': '#/$elements/L2100F_PER05'},
                        'per06': {'$ref': '#/$elements/L2100F_PER06'},
                        'per07': {'$ref': '#/$elements/L2100F_PER07'},
                        'per08': {'$ref': '#/$elements/L2100F_PER08'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100F_PER01
    per03: L2100F_PER03
    per04: L2100F_PER04
    per05: L2100F_PER05 | None
    per06: L2100F_PER06 | None
    per07: L2100F_PER07 | None
    per08: L2100F_PER08 | None


class L2100F_N301(Element):
    """Custodial Parent Address Line"""
    class Schema:
        json = {'title': 'Custodial Parent Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100F_N302(Element):
    """Custodial Parent Address Line"""
    class Schema:
        json = {'title': 'Custodial Parent Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100F_N3(Segment):
    """Custodial Parent Street Address"""
    class Schema:
        json = {'title': 'Custodial Parent Street Address',
         'usage': 'S',
         'description': 'xid=N3 name=Custodial Parent Street Address',
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100F_N301'},
                        'n302': {'$ref': '#/$elements/L2100F_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100F_N301
    n302: L2100F_N302 | None


class L2100F_N401(Element):
    """Custodial Parent City Name"""
    class Schema:
        json = {'title': 'Custodial Parent City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100F_N402(Element):
    """Custodial Parent State Code"""
    class Schema:
        json = {'title': 'Custodial Parent State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100F_N403(Element):
    """Custodial Parent Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Custodial Parent Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100F_N404(Element):
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


class L2100F_N405(Element):
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


class L2100F_N406(Element):
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


class L2100F_N4(Segment):
    """Custodial Parent City, State, Zip"""
    class Schema:
        json = {'title': 'Custodial Parent City, State, Zip',
         'usage': 'S',
         'description': 'xid=N4 name=Custodial Parent City, State, Zip',
         'position': 60,
         'syntax': ['C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100F_N401'},
                        'n402': {'$ref': '#/$elements/L2100F_N402'},
                        'n403': {'$ref': '#/$elements/L2100F_N403'},
                        'n404': {'$ref': '#/$elements/L2100F_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2100F_N401
    n402: L2100F_N402
    n403: L2100F_N403
    n404: L2100F_N404 | None


class L2100F(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Custodial Parent',
                   'usage': 'S',
                   'description': 'xid=2100F name=Custodial Parent type=None',
                   'position': 30,
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
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['E1', 'EI', 'EXS', 'GD', 'J6', 'QD']}]}}
        datatype = common.D_98
        codes = ['E1', 'EI', 'EXS', 'GD', 'J6', 'QD']
        min_len = 2
        max_len = 3


class L2100G_NM102(Element):
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


class L2100G_NM103(Element):
    """Responsible Party Last or Organization Name"""
    class Schema:
        json = {'title': 'Responsible Party Last or Organization Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100G_NM104(Element):
    """Responsible Party First Name"""
    class Schema:
        json = {'title': 'Responsible Party First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100G_NM105(Element):
    """Responsible Party Middle Name"""
    class Schema:
        json = {'title': 'Responsible Party Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100G_NM106(Element):
    """Responsible Party Name Prefix"""
    class Schema:
        json = {'title': 'Responsible Party Name Prefix',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2100G_NM107(Element):
    """Responsible Party Suffix Name"""
    class Schema:
        json = {'title': 'Responsible Party Suffix Name',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100G_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'ZZ']}]}}
        datatype = common.D_66
        codes = ['34', 'ZZ']
        min_len = 1
        max_len = 2


class L2100G_NM109(Element):
    """Responsible Party Identifier"""
    class Schema:
        json = {'title': 'Responsible Party Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100G_NM110(Element):
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


class L2100G_NM111(Element):
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


class L2100G_NM1(Segment):
    """Responsible Person"""
    class Schema:
        json = {'title': 'Responsible Person',
         'usage': 'R',
         'description': 'xid=NM1 name=Responsible Person',
         'position': 30,
         'syntax': ['P0809', 'C1110'],
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
                        'nm109': {'$ref': '#/$elements/L2100G_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm104']}
        segment_name = 'NM1'
    nm101: L2100G_NM101
    nm102: L2100G_NM102
    nm103: L2100G_NM103
    nm104: L2100G_NM104
    nm105: L2100G_NM105 | None
    nm106: L2100G_NM106 | None
    nm107: L2100G_NM107 | None
    nm108: L2100G_NM108 | None
    nm109: L2100G_NM109 | None


class L2100G_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['RP']}]}}
        datatype = common.D_366
        codes = ['RP']
        min_len = 2
        max_len = 2


class L2100G_PER02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100G_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100G_PER04(Element):
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


class L2100G_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100G_PER06(Element):
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


class L2100G_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2100G_PER08(Element):
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


class L2100G_PER09(Element):
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


class L2100G_PER(Segment):
    """Responsible Person Communications Numbers"""
    class Schema:
        json = {'title': 'Responsible Person Communications Numbers',
         'usage': 'S',
         'description': 'xid=PER name=Responsible Person Communications Numbers',
         'position': 40,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L2100G_PER01'},
                        'per03': {'$ref': '#/$elements/L2100G_PER03'},
                        'per04': {'$ref': '#/$elements/L2100G_PER04'},
                        'per05': {'$ref': '#/$elements/L2100G_PER05'},
                        'per06': {'$ref': '#/$elements/L2100G_PER06'},
                        'per07': {'$ref': '#/$elements/L2100G_PER07'},
                        'per08': {'$ref': '#/$elements/L2100G_PER08'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L2100G_PER01
    per03: L2100G_PER03
    per04: L2100G_PER04
    per05: L2100G_PER05 | None
    per06: L2100G_PER06 | None
    per07: L2100G_PER07 | None
    per08: L2100G_PER08 | None


class L2100G_N301(Element):
    """Responsible Party Address Line"""
    class Schema:
        json = {'title': 'Responsible Party Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100G_N302(Element):
    """Responsible Party Address Line"""
    class Schema:
        json = {'title': 'Responsible Party Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L2100G_N3(Segment):
    """Responsible Person Street Address"""
    class Schema:
        json = {'title': 'Responsible Person Street Address',
         'usage': 'S',
         'description': 'xid=N3 name=Responsible Person Street Address',
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L2100G_N301'},
                        'n302': {'$ref': '#/$elements/L2100G_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L2100G_N301
    n302: L2100G_N302 | None


class L2100G_N401(Element):
    """Responsible Party City Name"""
    class Schema:
        json = {'title': 'Responsible Party City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2100G_N402(Element):
    """Responsible Party State Code"""
    class Schema:
        json = {'title': 'Responsible Party State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2100G_N403(Element):
    """Responsible Party Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Responsible Party Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2100G_N404(Element):
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


class L2100G_N405(Element):
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


class L2100G_N406(Element):
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


class L2100G_N4(Segment):
    """Responsible Person City, State, Zip"""
    class Schema:
        json = {'title': 'Responsible Person City, State, Zip',
         'usage': 'S',
         'description': 'xid=N4 name=Responsible Person City, State, Zip',
         'position': 60,
         'syntax': ['C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2100G_N401'},
                        'n402': {'$ref': '#/$elements/L2100G_N402'},
                        'n403': {'$ref': '#/$elements/L2100G_N403'},
                        'n404': {'$ref': '#/$elements/L2100G_N404'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2100G_N401
    n402: L2100G_N402
    n403: L2100G_N403
    n404: L2100G_N404 | None


class L2100G(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Responsible Person',
                   'usage': 'S',
                   'description': 'xid=2100G name=Responsible Person type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'nm1': {'$ref': '#/$segments/L2100G_NM1'},
                                  'per': {'$ref': '#/$segments/L2100G_PER'},
                                  'n3': {'$ref': '#/$segments/L2100G_N3'},
                                  'n4': {'$ref': '#/$segments/L2100G_N4'}},
                   'required': ['nm1']},
         'maxItems': 1}
    nm1: L2100G_NM1
    per: L2100G_PER | None
    n3: L2100G_N3 | None
    n4: L2100G_N4 | None


class L2200_DSB01(Element):
    """Disability Type Code"""
    class Schema:
        json = {'title': 'Disability Type Code',
         'usage': 'R',
         'description': 'xid=DSB01 data_ele=1146',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1146'},
                            {'enum': ['1', '2', '3', '4']}]}}
        datatype = common.D_1146
        codes = ['1', '2', '3', '4']
        min_len = 1
        max_len = 1


class L2200_DSB02(Element):
    """Quantity"""
    class Schema:
        json = {'title': 'Quantity',
         'usage': 'N',
         'description': 'xid=DSB02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2200_DSB03(Element):
    """Occupation Code"""
    class Schema:
        json = {'title': 'Occupation Code',
         'usage': 'N',
         'description': 'xid=DSB03 data_ele=1149',
         'sequence': 3,
         'type': {'$ref': '#/$common/1149'}}
        datatype = common.D_1149
        min_len = 4
        max_len = 6


class L2200_DSB04(Element):
    """Work Intensity Code"""
    class Schema:
        json = {'title': 'Work Intensity Code',
         'usage': 'N',
         'description': 'xid=DSB04 data_ele=1154',
         'sequence': 4,
         'type': {'$ref': '#/$common/1154'}}
        datatype = common.D_1154
        min_len = 1
        max_len = 1


class L2200_DSB05(Element):
    """Product Option Code"""
    class Schema:
        json = {'title': 'Product Option Code',
         'usage': 'N',
         'description': 'xid=DSB05 data_ele=1161',
         'sequence': 5,
         'type': {'$ref': '#/$common/1161'}}
        datatype = common.D_1161
        min_len = 1
        max_len = 2


class L2200_DSB06(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=DSB06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2200_DSB07(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'S',
         'description': 'xid=DSB07 data_ele=235',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/235'}, {'enum': ['DX']}]}}
        datatype = common.D_235
        codes = ['DX']
        min_len = 2
        max_len = 2


class L2200_DSB08(Element):
    """Diagnosis Code"""
    class Schema:
        json = {'title': 'Diagnosis Code',
         'usage': 'S',
         'description': 'xid=DSB08 data_ele=1137',
         'sequence': 8,
         'type': {'$ref': '#/$common/1137'}}
        datatype = common.D_1137
        min_len = 1
        max_len = 15


class L2200_DSB(Segment):
    """Disability Information"""
    class Schema:
        json = {'title': 'Disability Information',
         'usage': 'R',
         'description': 'xid=DSB name=Disability Information',
         'position': 200,
         'syntax': ['P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DSB'},
                        'dsb01': {'$ref': '#/$elements/L2200_DSB01'},
                        'dsb07': {'$ref': '#/$elements/L2200_DSB07'},
                        'dsb08': {'$ref': '#/$elements/L2200_DSB08'}},
         'required': ['dsb01']}
        segment_name = 'DSB'
    dsb01: L2200_DSB01
    dsb07: L2200_DSB07 | None
    dsb08: L2200_DSB08 | None


class L2200_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['360', '361']}]}}
        datatype = common.D_374
        codes = ['360', '361']
        min_len = 3
        max_len = 3


class L2200_DTP02(Element):
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


class L2200_DTP03(Element):
    """Disability Eligibility Date"""
    class Schema:
        json = {'title': 'Disability Eligibility Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2200_DTP(Segment):
    """Disability Eligibility Dates"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Disability Eligibility Dates',
                   'usage': 'S',
                   'description': 'xid=DTP name=Disability Eligibility Dates',
                   'position': 210,
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
         'items': {'title': 'Disability Information',
                   'usage': 'S',
                   'description': 'xid=2200 name=Disability Information type=None',
                   'position': 200,
                   'type': 'object',
                   'properties': {'dsb': {'$ref': '#/$segments/L2200_DSB'},
                                  'dtp': {'$ref': '#/$segments/L2200_DTP'}},
                   'required': ['dsb']},
         'maxItems': 1}
    dsb: L2200_DSB
    dtp: list[L2200_DTP] | None


class L2300_HD01(Element):
    """Maintenance Type Code"""
    class Schema:
        json = {'title': 'Maintenance Type Code',
         'usage': 'R',
         'description': 'xid=HD01 data_ele=875',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/875'},
                            {'enum': ['001', '002', '021', '024', '025', '026', '030',
                                      '032']}]}}
        datatype = common.D_875
        codes = ['001', '002', '021', '024', '025', '026', '030', '032']
        min_len = 3
        max_len = 3


class L2300_HD02(Element):
    """Maintenance Reason Code"""
    class Schema:
        json = {'title': 'Maintenance Reason Code',
         'usage': 'N',
         'description': 'xid=HD02 data_ele=1203',
         'sequence': 2,
         'type': {'$ref': '#/$common/1203'}}
        datatype = common.D_1203
        min_len = 2
        max_len = 3


class L2300_HD03(Element):
    """Insurance Line Code"""
    class Schema:
        json = {'title': 'Insurance Line Code',
         'usage': 'R',
         'description': 'xid=HD03 data_ele=1205',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1205'},
                            {'enum': ['AG', 'AH', 'AJ', 'AK', 'HE', 'MM', 'UR', 'DCP',
                                      'DEN', 'EPO', 'FAC', 'HE', 'HLT', 'HMO', 'LTC',
                                      'LTD', 'MM', 'MOD', 'PDG', 'POS', 'PPO', 'PRA',
                                      'STD', 'UR', 'VIS']}]}}
        datatype = common.D_1205
        codes = ['AG', 'AH', 'AJ', 'AK', 'HE', 'MM', 'UR', 'DCP', 'DEN', 'EPO', 'FAC', 'HE', 'HLT', 'HMO', 'LTC', 'LTD', 'MM', 'MOD', 'PDG', 'POS', 'PPO', 'PRA', 'STD', 'UR', 'VIS']
        min_len = 2
        max_len = 3


class L2300_HD04(Element):
    """Plan Coverage Description"""
    class Schema:
        json = {'title': 'Plan Coverage Description',
         'usage': 'S',
         'description': 'xid=HD04 data_ele=1204',
         'sequence': 4,
         'type': {'$ref': '#/$common/1204'}}
        datatype = common.D_1204
        min_len = 1
        max_len = 50


class L2300_HD05(Element):
    """Coverage Level Code"""
    class Schema:
        json = {'title': 'Coverage Level Code',
         'usage': 'S',
         'description': 'xid=HD05 data_ele=1207',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1207'},
                            {'enum': ['CHD', 'DEP', 'E1D', 'E2D', 'E3D', 'E5D', 'E6D',
                                      'E7D', 'E8D', 'E9D', 'ECH', 'EMP', 'ESP', 'FAM',
                                      'IND', 'SPC', 'SPO', 'TWO']}]}}
        datatype = common.D_1207
        codes = ['CHD', 'DEP', 'E1D', 'E2D', 'E3D', 'E5D', 'E6D', 'E7D', 'E8D', 'E9D', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO', 'TWO']
        min_len = 3
        max_len = 3


class L2300_HD06(Element):
    """Count"""
    class Schema:
        json = {'title': 'Count',
         'usage': 'N',
         'description': 'xid=HD06 data_ele=609',
         'sequence': 6,
         'type': {'$ref': '#/$common/609'}}
        datatype = common.D_609
        min_len = 1
        max_len = 9


class L2300_HD07(Element):
    """Count"""
    class Schema:
        json = {'title': 'Count',
         'usage': 'N',
         'description': 'xid=HD07 data_ele=609',
         'sequence': 7,
         'type': {'$ref': '#/$common/609'}}
        datatype = common.D_609
        min_len = 1
        max_len = 9


class L2300_HD08(Element):
    """Underwriting Decision Code"""
    class Schema:
        json = {'title': 'Underwriting Decision Code',
         'usage': 'N',
         'description': 'xid=HD08 data_ele=1209',
         'sequence': 8,
         'type': {'$ref': '#/$common/1209'}}
        datatype = common.D_1209
        min_len = 1
        max_len = 1


class L2300_HD09(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=HD09 data_ele=1073',
         'sequence': 9,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_HD10(Element):
    """Drug House Code"""
    class Schema:
        json = {'title': 'Drug House Code',
         'usage': 'N',
         'description': 'xid=HD10 data_ele=1211',
         'sequence': 10,
         'type': {'$ref': '#/$common/1211'}}
        datatype = common.D_1211
        min_len = 2
        max_len = 3


class L2300_HD11(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=HD11 data_ele=1073',
         'sequence': 11,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2300_HD(Segment):
    """Health Coverage"""
    class Schema:
        json = {'title': 'Health Coverage',
         'usage': 'R',
         'description': 'xid=HD name=Health Coverage',
         'position': 260,
         'type': 'object',
         'properties': {'xid': {'literal': 'HD'},
                        'hd01': {'$ref': '#/$elements/L2300_HD01'},
                        'hd03': {'$ref': '#/$elements/L2300_HD03'},
                        'hd04': {'$ref': '#/$elements/L2300_HD04'},
                        'hd05': {'$ref': '#/$elements/L2300_HD05'}},
         'required': ['hd01', 'hd03']}
        segment_name = 'HD'
    hd01: L2300_HD01
    hd03: L2300_HD03
    hd04: L2300_HD04 | None
    hd05: L2300_HD05 | None


class L2300_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['303', '348', '349', '543']}]}}
        datatype = common.D_374
        codes = ['303', '348', '349', '543']
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
    """Coverage Period"""
    class Schema:
        json = {'title': 'Coverage Period',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2300_DTP(Segment):
    """Health Coverage Dates"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Health Coverage Dates',
                   'usage': 'R',
                   'description': 'xid=DTP name=Health Coverage Dates',
                   'position': 270,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTP'},
                                  'dtp01': {'$ref': '#/$elements/L2300_DTP01'},
                                  'dtp02': {'$ref': '#/$elements/L2300_DTP02'},
                                  'dtp03': {'$ref': '#/$elements/L2300_DTP03'}},
                   'required': ['dtp01', 'dtp02', 'dtp03']},
         'maxItems': 4}
        segment_name = 'DTP'
    dtp01: L2300_DTP01
    dtp02: L2300_DTP02
    dtp03: L2300_DTP03


class L2300_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['B9', 'C1', 'D2', 'P3']}]}}
        datatype = common.D_522
        codes = ['B9', 'C1', 'D2', 'P3']
        min_len = 1
        max_len = 3


class L2300_AMT02(Element):
    """Contract Amount"""
    class Schema:
        json = {'title': 'Contract Amount',
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
    """Health Coverage Policy"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Health Coverage Policy',
                   'usage': 'S',
                   'description': 'xid=AMT name=Health Coverage Policy',
                   'position': 280,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2300_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2300_AMT02'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 4}
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
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['17', '1L', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['17', '1L', 'ZZ']
        min_len = 2
        max_len = 3


class L2300_REF02(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
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
    """Health Coverage Policy Number"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Health Coverage Policy Number',
                   'usage': 'S',
                   'description': 'xid=REF name=Health Coverage Policy Number',
                   'position': 290,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2300_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2300_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 2}
        segment_name = 'REF'
    ref01: L2300_REF01
    ref02: L2300_REF02


class L2300_IDC01(Element):
    """Plan Coverage Description"""
    class Schema:
        json = {'title': 'Plan Coverage Description',
         'usage': 'R',
         'description': 'xid=IDC01 data_ele=1204',
         'sequence': 1,
         'type': {'$ref': '#/$common/1204'}}
        datatype = common.D_1204
        min_len = 1
        max_len = 50


class L2300_IDC02(Element):
    """Identification Card Type Code"""
    class Schema:
        json = {'title': 'Identification Card Type Code',
         'usage': 'R',
         'description': 'xid=IDC02 data_ele=1215',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1215'}, {'enum': ['D', 'H', 'P']}]}}
        datatype = common.D_1215
        codes = ['D', 'H', 'P']
        min_len = 1
        max_len = 1


class L2300_IDC03(Element):
    """Identification Card Count"""
    class Schema:
        json = {'title': 'Identification Card Count',
         'usage': 'S',
         'description': 'xid=IDC03 data_ele=380',
         'sequence': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2300_IDC04(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'S',
         'description': 'xid=IDC04 data_ele=306',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/306'}, {'enum': ['1', '2', 'RX']}]}}
        datatype = common.D_306
        codes = ['1', '2', 'RX']
        min_len = 1
        max_len = 2


class L2300_IDC(Segment):
    """Identification Card"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Identification Card',
                   'usage': 'S',
                   'description': 'xid=IDC name=Identification Card',
                   'position': 300,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'IDC'},
                                  'idc01': {'$ref': '#/$elements/L2300_IDC01'},
                                  'idc02': {'$ref': '#/$elements/L2300_IDC02'},
                                  'idc03': {'$ref': '#/$elements/L2300_IDC03'},
                                  'idc04': {'$ref': '#/$elements/L2300_IDC04'}},
                   'required': ['idc01', 'idc02']},
         'maxItems': 10}
        segment_name = 'IDC'
    idc01: L2300_IDC01
    idc02: L2300_IDC02
    idc03: L2300_IDC03 | None
    idc04: L2300_IDC04 | None


class L2310_LX01(Element):
    """Assigned Number"""
    class Schema:
        json = {'title': 'Assigned Number',
         'usage': 'R',
         'description': 'xid=LX01 data_ele=554',
         'sequence': 1,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2310_LX(Segment):
    """Provider Information"""
    class Schema:
        json = {'title': 'Provider Information',
         'usage': 'R',
         'description': 'xid=LX name=Provider Information',
         'position': 310,
         'type': 'object',
         'properties': {'xid': {'literal': 'LX'},
                        'lx01': {'$ref': '#/$elements/L2310_LX01'}},
         'required': ['lx01']}
        segment_name = 'LX'
    lx01: L2310_LX01


class L2310_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'},
                            {'enum': ['3D', 'OD', 'P3', 'QA', 'QN', 'Y2']}]}}
        datatype = common.D_98
        codes = ['3D', 'OD', 'P3', 'QA', 'QN', 'Y2']
        min_len = 2
        max_len = 3


class L2310_NM102(Element):
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


class L2310_NM103(Element):
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


class L2310_NM104(Element):
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


class L2310_NM105(Element):
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


class L2310_NM106(Element):
    """Provider Name Prefix"""
    class Schema:
        json = {'title': 'Provider Name Prefix',
         'usage': 'S',
         'description': 'xid=NM106 data_ele=1038',
         'sequence': 6,
         'type': {'$ref': '#/$common/1038'}}
        datatype = common.D_1038
        min_len = 1
        max_len = 10


class L2310_NM107(Element):
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


class L2310_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['34', 'FI', 'SV', 'XX']}]}}
        datatype = common.D_66
        codes = ['34', 'FI', 'SV', 'XX']
        min_len = 1
        max_len = 2


class L2310_NM109(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2310_NM110(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'R',
         'description': 'xid=NM110 data_ele=706',
         'sequence': 10,
         'type': {'allOf': [{'$ref': '#/$common/706'}, {'enum': ['25', '26', '72']}]}}
        datatype = common.D_706
        codes = ['25', '26', '72']
        min_len = 2
        max_len = 2


class L2310_NM111(Element):
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


class L2310_NM1(Segment):
    """Provider Name"""
    class Schema:
        json = {'title': 'Provider Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Provider Name',
         'position': 320,
         'syntax': ['P0809', 'C1110'],
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
                        'nm110': {'$ref': '#/$elements/L2310_NM110'}},
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


class L2310_N401(Element):
    """Member City Name"""
    class Schema:
        json = {'title': 'Member City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L2310_N402(Element):
    """Member State Code"""
    class Schema:
        json = {'title': 'Member State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L2310_N403(Element):
    """Member Postal Zone or Zip Code"""
    class Schema:
        json = {'title': 'Member Postal Zone or Zip Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L2310_N404(Element):
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


class L2310_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'S',
         'description': 'xid=N405 data_ele=309',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/309'}, {'enum': ['60', 'CY', 'RJ']}]}}
        datatype = common.D_309
        codes = ['60', 'CY', 'RJ']
        min_len = 1
        max_len = 2


class L2310_N406(Element):
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


class L2310_N4(Segment):
    """Provider City, State, Zip Code"""
    class Schema:
        json = {'title': 'Provider City, State, Zip Code',
         'usage': 'S',
         'description': 'xid=N4 name=Provider City, State, Zip Code',
         'position': 360,
         'syntax': ['C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L2310_N401'},
                        'n402': {'$ref': '#/$elements/L2310_N402'},
                        'n403': {'$ref': '#/$elements/L2310_N403'},
                        'n404': {'$ref': '#/$elements/L2310_N404'},
                        'n405': {'$ref': '#/$elements/L2310_N405'},
                        'n406': {'$ref': '#/$elements/L2310_N406'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L2310_N401
    n402: L2310_N402
    n403: L2310_N403
    n404: L2310_N404 | None
    n405: L2310_N405 | None
    n406: L2310_N406 | None


class L2310_PER01(Element):
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


class L2310_PER02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'N',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2310_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2310_PER04(Element):
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


class L2310_PER05(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2310_PER06(Element):
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


class L2310_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'},
                            {'enum': ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'HP', 'TE', 'WP']
        min_len = 2
        max_len = 2


class L2310_PER08(Element):
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


class L2310_PER09(Element):
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


class L2310_PER(Segment):
    """Provider Communications Numbers"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Provider Communications Numbers',
                   'usage': 'S',
                   'description': 'xid=PER name=Provider Communications Numbers',
                   'position': 370,
                   'syntax': ['P0304', 'P0506', 'P0708'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2310_PER01'},
                                  'per03': {'$ref': '#/$elements/L2310_PER03'},
                                  'per04': {'$ref': '#/$elements/L2310_PER04'},
                                  'per05': {'$ref': '#/$elements/L2310_PER05'},
                                  'per06': {'$ref': '#/$elements/L2310_PER06'},
                                  'per07': {'$ref': '#/$elements/L2310_PER07'},
                                  'per08': {'$ref': '#/$elements/L2310_PER08'}},
                   'required': ['per01', 'per03', 'per04']},
         'maxItems': 2}
        segment_name = 'PER'
    per01: L2310_PER01
    per03: L2310_PER03
    per04: L2310_PER04
    per05: L2310_PER05 | None
    per06: L2310_PER06 | None
    per07: L2310_PER07 | None
    per08: L2310_PER08 | None


class L2310_PLA01(Element):
    """Action Code"""
    class Schema:
        json = {'title': 'Action Code',
         'usage': 'R',
         'description': 'xid=PLA01 data_ele=306',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/306'}, {'enum': ['2']}]}}
        datatype = common.D_306
        codes = ['2']
        min_len = 1
        max_len = 2


class L2310_PLA02(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=PLA02 data_ele=98',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['1P']}]}}
        datatype = common.D_98
        codes = ['1P']
        min_len = 2
        max_len = 3


class L2310_PLA03(Element):
    """Provider Effective Date"""
    class Schema:
        json = {'title': 'Provider Effective Date',
         'usage': 'R',
         'description': 'xid=PLA03 data_ele=373',
         'sequence': 3,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2310_PLA04(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=PLA04 data_ele=337',
         'sequence': 4,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2310_PLA05(Element):
    """Maintenance Reason Code"""
    class Schema:
        json = {'title': 'Maintenance Reason Code',
         'usage': 'R',
         'description': 'xid=PLA05 data_ele=1203',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/1203'},
                            {'enum': ['14', '22', '46', 'AA', 'AB', 'AC', 'AD', 'AE',
                                      'AF', 'AG', 'AH', 'AI', 'AJ']}]}}
        datatype = common.D_1203
        codes = ['14', '22', '46', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ']
        min_len = 2
        max_len = 3


class L2310_PLA(Segment):
    """PCP Change Reason"""
    class Schema:
        json = {'title': 'PCP Change Reason',
         'usage': 'S',
         'description': 'xid=PLA name=PCP Change Reason',
         'position': 395,
         'type': 'object',
         'properties': {'xid': {'literal': 'PLA'},
                        'pla01': {'$ref': '#/$elements/L2310_PLA01'},
                        'pla02': {'$ref': '#/$elements/L2310_PLA02'},
                        'pla03': {'$ref': '#/$elements/L2310_PLA03'},
                        'pla05': {'$ref': '#/$elements/L2310_PLA05'}},
         'required': ['pla01', 'pla02', 'pla03', 'pla05']}
        segment_name = 'PLA'
    pla01: L2310_PLA01
    pla02: L2310_PLA02
    pla03: L2310_PLA03
    pla05: L2310_PLA05


class L2310(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Provider Information',
                   'usage': 'S',
                   'description': 'xid=2310 name=Provider Information type=None',
                   'position': 310,
                   'type': 'object',
                   'properties': {'lx': {'$ref': '#/$segments/L2310_LX'},
                                  'nm1': {'$ref': '#/$segments/L2310_NM1'},
                                  'n4': {'$ref': '#/$segments/L2310_N4'},
                                  'per': {'$ref': '#/$segments/L2310_PER'},
                                  'pla': {'$ref': '#/$segments/L2310_PLA'}},
                   'required': ['lx', 'nm1']},
         'maxItems': 30}
    lx: L2310_LX
    nm1: L2310_NM1
    n4: L2310_N4 | None
    per: list[L2310_PER] | None
    pla: L2310_PLA | None


class L2320_COB01(Element):
    """Payer Responsibility Sequence Number Code"""
    class Schema:
        json = {'title': 'Payer Responsibility Sequence Number Code',
         'usage': 'R',
         'description': 'xid=COB01 data_ele=1138',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1138'},
                            {'enum': ['P', 'S', 'T', 'U']}]}}
        datatype = common.D_1138
        codes = ['P', 'S', 'T', 'U']
        min_len = 1
        max_len = 1


class L2320_COB02(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
         'usage': 'S',
         'description': 'xid=COB02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320_COB03(Element):
    """Coordination of Benefits Code"""
    class Schema:
        json = {'title': 'Coordination of Benefits Code',
         'usage': 'R',
         'description': 'xid=COB03 data_ele=1143',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1143'}, {'enum': ['1', '5', '6']}]}}
        datatype = common.D_1143
        codes = ['1', '5', '6']
        min_len = 1
        max_len = 1


class L2320_COB(Segment):
    """Coordination of Benefits"""
    class Schema:
        json = {'title': 'Coordination of Benefits',
         'usage': 'R',
         'description': 'xid=COB name=Coordination of Benefits',
         'position': 400,
         'type': 'object',
         'properties': {'xid': {'literal': 'COB'},
                        'cob01': {'$ref': '#/$elements/L2320_COB01'},
                        'cob02': {'$ref': '#/$elements/L2320_COB02'},
                        'cob03': {'$ref': '#/$elements/L2320_COB03'}},
         'required': ['cob01', 'cob03']}
        segment_name = 'COB'
    cob01: L2320_COB01
    cob02: L2320_COB02 | None
    cob03: L2320_COB03


class L2320_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['60', '6P', 'A6', 'SY', 'ZZ']}]}}
        datatype = common.D_128
        codes = ['60', '6P', 'A6', 'SY', 'ZZ']
        min_len = 2
        max_len = 3


class L2320_REF02(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2320_REF03(Element):
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


class L2320_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2320_REF(Segment):
    """Additional Coordination of Benefits Identifiers"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Coordination of Benefits Identifiers',
                   'usage': 'S',
                   'description': 'xid=REF name=Additional Coordination of Benefits '
                                  'Identifiers',
                   'position': 405,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2320_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2320_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2320_REF01
    ref02: L2320_REF02


class L2320_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['IN']}]}}
        datatype = common.D_98
        codes = ['IN']
        min_len = 2
        max_len = 3


class L2320_N102(Element):
    """Insurer Name"""
    class Schema:
        json = {'title': 'Insurer Name',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2320_N103(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'NI', 'XV']}]}}
        datatype = common.D_66
        codes = ['FI', 'NI', 'XV']
        min_len = 1
        max_len = 2


class L2320_N104(Element):
    """Insured Group or Policy Number"""
    class Schema:
        json = {'title': 'Insured Group or Policy Number',
         'usage': 'S',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2320_N105(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L2320_N106(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2320_N1(Segment):
    """Other Insurance Company Name"""
    class Schema:
        json = {'title': 'Other Insurance Company Name',
         'usage': 'S',
         'description': 'xid=N1 name=Other Insurance Company Name',
         'position': 410,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L2320_N101'},
                        'n102': {'$ref': '#/$elements/L2320_N102'},
                        'n103': {'$ref': '#/$elements/L2320_N103'},
                        'n104': {'$ref': '#/$elements/L2320_N104'}},
         'required': ['n101']}
        segment_name = 'N1'
    n101: L2320_N101
    n102: L2320_N102 | None
    n103: L2320_N103 | None
    n104: L2320_N104 | None


class L2320_DTP01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTP01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['344', '345']}]}}
        datatype = common.D_374
        codes = ['344', '345']
        min_len = 3
        max_len = 3


class L2320_DTP02(Element):
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


class L2320_DTP03(Element):
    """Coordination of Benefits Date"""
    class Schema:
        json = {'title': 'Coordination of Benefits Date',
         'usage': 'R',
         'description': 'xid=DTP03 data_ele=1251',
         'sequence': 3,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2320_DTP(Segment):
    """Coordination of Benefits Eligibility Dates"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Coordination of Benefits Eligibility Dates',
                   'usage': 'S',
                   'description': 'xid=DTP name=Coordination of Benefits Eligibility '
                                  'Dates',
                   'position': 450,
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


class L2320(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Coordination of Benefits',
                   'usage': 'S',
                   'description': 'xid=2320 name=Coordination of Benefits type=None',
                   'position': 400,
                   'type': 'object',
                   'properties': {'cob': {'$ref': '#/$segments/L2320_COB'},
                                  'ref': {'$ref': '#/$segments/L2320_REF'},
                                  'n1': {'$ref': '#/$segments/L2320_N1'},
                                  'dtp': {'$ref': '#/$segments/L2320_DTP'}},
                   'required': ['cob']},
         'maxItems': 5}
    cob: L2320_COB
    ref: list[L2320_REF] | None
    n1: L2320_N1 | None
    dtp: list[L2320_DTP] | None


class L2300(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Health Coverage',
                   'usage': 'S',
                   'description': 'xid=2300 name=Health Coverage type=None',
                   'position': 260,
                   'type': 'object',
                   'properties': {'hd': {'$ref': '#/$segments/L2300_HD'},
                                  'dtp': {'$ref': '#/$segments/L2300_DTP'},
                                  'amt': {'$ref': '#/$segments/L2300_AMT'},
                                  'ref': {'$ref': '#/$segments/L2300_REF'},
                                  'idc': {'$ref': '#/$segments/L2300_IDC'},
                                  'l2310': {'$ref': '#/$segments/L2310'},
                                  'l2320': {'$ref': '#/$segments/L2320'}},
                   'required': ['hd', 'dtp']},
         'maxItems': 99}
    hd: L2300_HD
    dtp: list[L2300_DTP]
    amt: list[L2300_AMT] | None
    ref: list[L2300_REF] | None
    idc: list[L2300_IDC] | None
    l2310: list[L2310] | None
    l2320: list[L2320] | None


class L2000(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Member Level Detail',
                   'usage': 'R',
                   'description': 'xid=2000 name=Member Level Detail type=None',
                   'position': 10,
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
                                  'l2200': {'$ref': '#/$segments/L2200'},
                                  'l2300': {'$ref': '#/$segments/L2300'}},
                   'required': ['ins', 'ref', 'l2100a']}}
    ins: L2000_INS
    ref: L2000_REF
    ref: L2000_REF
    ref: list[L2000_REF]
    ref: L2000_REF
    dtp: list[L2000_DTP] | None
    l2100a: list[L2100A]
    l2100b: list[L2100B] | None
    l2100c: list[L2100C] | None
    l2100d: list[L2100D] | None
    l2100e: list[L2100E] | None
    l2100f: list[L2100F] | None
    l2100g: list[L2100G] | None
    l2200: list[L2200] | None
    l2300: list[L2300] | None


class DETAIL(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 2 - Detail',
                   'usage': 'S',
                   'description': 'xid=DETAIL name=Table 2 - Detail type=wrapper',
                   'position': 20,
                   'type': 'object',
                   'properties': {'l2000': {'$ref': '#/$segments/L2000'}},
                   'required': ['l2000']}}
    l2000: list[L2000]


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
         'position': 690,
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


class MSG834(Message):
    """HIPAA Benefit Enrollment and Maintenance X095A1-834"""
    class Schema:
        json = {'title': 'HIPAA Benefit Enrollment and Maintenance X095A1-834',
         'description': 'xid=834 name=HIPAA Benefit Enrollment and Maintenance '
                        'X095A1-834',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
