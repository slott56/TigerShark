"""
835.5010.X221.A1
Created 2023-03-25 09:22:28.615166
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
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['HP']}]}}
        datatype = common.D_479
        codes = ['HP']
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
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['005010X221A1']}]}}
        datatype = common.D_480
        codes = ['005010X221A1']
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
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['835']}]}}
        datatype = common.D_143
        codes = ['835']
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
    """Implementation Convention Reference"""
    class Schema:
        json = {'title': 'Implementation Convention Reference',
         'usage': 'N',
         'description': 'xid=ST03 data_ele=1705',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/1705'}, {'enum': ['005010X221A1']}]}}
        datatype = common.D_1705
        codes = ['005010X221A1']
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
                        'st02': {'$ref': '#/$elements/ST_LOOP_ST02'}},
         'required': ['st01', 'st02']}
        segment_name = 'ST'
    st01: ST_LOOP_ST01
    st02: ST_LOOP_ST02


class HEADER_BPR01(Element):
    """Transaction Handling Code"""
    class Schema:
        json = {'title': 'Transaction Handling Code',
         'usage': 'R',
         'description': 'xid=BPR01 data_ele=305',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/305'},
                            {'enum': ['C', 'D', 'H', 'I', 'P', 'U', 'X']}]}}
        datatype = common.D_305
        codes = ['C', 'D', 'H', 'I', 'P', 'U', 'X']
        min_len = 1
        max_len = 2


class HEADER_BPR02(Element):
    """Total Actual Provider Payment Amount"""
    class Schema:
        json = {'title': 'Total Actual Provider Payment Amount',
         'usage': 'R',
         'description': 'xid=BPR02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class HEADER_BPR03(Element):
    """Credit or Debit Flag Code"""
    class Schema:
        json = {'title': 'Credit or Debit Flag Code',
         'usage': 'R',
         'description': 'xid=BPR03 data_ele=478',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/478'}, {'enum': ['C', 'D']}]}}
        datatype = common.D_478
        codes = ['C', 'D']
        min_len = 1
        max_len = 1


class HEADER_BPR04(Element):
    """Payment Method Code"""
    class Schema:
        json = {'title': 'Payment Method Code',
         'usage': 'R',
         'description': 'xid=BPR04 data_ele=591',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/591'},
                            {'enum': ['ACH', 'BOP', 'CHK', 'FWT', 'NON']}]}}
        datatype = common.D_591
        codes = ['ACH', 'BOP', 'CHK', 'FWT', 'NON']
        min_len = 3
        max_len = 3


class HEADER_BPR05(Element):
    """Payment Format Code"""
    class Schema:
        json = {'title': 'Payment Format Code',
         'usage': 'S',
         'description': 'xid=BPR05 data_ele=812',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/812'}, {'enum': ['CCP', 'CTX']}]}}
        datatype = common.D_812
        codes = ['CCP', 'CTX']
        min_len = 1
        max_len = 10


class HEADER_BPR06(Element):
    """Depository Financial Institution (DFI) Identification Number Qualifier"""
    class Schema:
        json = {'title': 'Depository Financial Institution (DFI) Identification Number '
                  'Qualifier',
         'usage': 'S',
         'description': 'xid=BPR06 data_ele=506',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/506'}, {'enum': ['01', '04']}]}}
        datatype = common.D_506
        codes = ['01', '04']
        min_len = 2
        max_len = 2


class HEADER_BPR07(Element):
    """Sender DFI Identifier"""
    class Schema:
        json = {'title': 'Sender DFI Identifier',
         'usage': 'S',
         'description': 'xid=BPR07 data_ele=507',
         'sequence': 7,
         'type': {'$ref': '#/$common/507'}}
        datatype = common.D_507
        min_len = 3
        max_len = 12


class HEADER_BPR08(Element):
    """Account Number Qualifier"""
    class Schema:
        json = {'title': 'Account Number Qualifier',
         'usage': 'S',
         'description': 'xid=BPR08 data_ele=569',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/569'}, {'enum': ['DA']}]}}
        datatype = common.D_569
        codes = ['DA']
        min_len = 1
        max_len = 3


class HEADER_BPR09(Element):
    """Sender Bank Account Number"""
    class Schema:
        json = {'title': 'Sender Bank Account Number',
         'usage': 'S',
         'description': 'xid=BPR09 data_ele=508',
         'sequence': 9,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class HEADER_BPR10(Element):
    """Payer Identifier"""
    class Schema:
        json = {'title': 'Payer Identifier',
         'usage': 'S',
         'description': 'xid=BPR10 data_ele=509',
         'sequence': 10,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class HEADER_BPR11(Element):
    """Originating Company Supplemental Code"""
    class Schema:
        json = {'title': 'Originating Company Supplemental Code',
         'usage': 'S',
         'description': 'xid=BPR11 data_ele=510',
         'sequence': 11,
         'type': {'$ref': '#/$common/510'}}
        datatype = common.D_510
        min_len = 9
        max_len = 9


class HEADER_BPR12(Element):
    """Depository Financial Institution (DFI) Identification Number Qualifier"""
    class Schema:
        json = {'title': 'Depository Financial Institution (DFI) Identification Number '
                  'Qualifier',
         'usage': 'S',
         'description': 'xid=BPR12 data_ele=506',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/506'}, {'enum': ['01', '04']}]}}
        datatype = common.D_506
        codes = ['01', '04']
        min_len = 2
        max_len = 2


class HEADER_BPR13(Element):
    """Receiver or Provider Bank ID Number"""
    class Schema:
        json = {'title': 'Receiver or Provider Bank ID Number',
         'usage': 'S',
         'description': 'xid=BPR13 data_ele=507',
         'sequence': 13,
         'type': {'$ref': '#/$common/507'}}
        datatype = common.D_507
        min_len = 3
        max_len = 12


class HEADER_BPR14(Element):
    """Account Number Qualifier"""
    class Schema:
        json = {'title': 'Account Number Qualifier',
         'usage': 'S',
         'description': 'xid=BPR14 data_ele=569',
         'sequence': 14,
         'type': {'allOf': [{'$ref': '#/$common/569'}, {'enum': ['DA', 'SG']}]}}
        datatype = common.D_569
        codes = ['DA', 'SG']
        min_len = 1
        max_len = 3


class HEADER_BPR15(Element):
    """Receiver or Provider Account Number"""
    class Schema:
        json = {'title': 'Receiver or Provider Account Number',
         'usage': 'S',
         'description': 'xid=BPR15 data_ele=508',
         'sequence': 15,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class HEADER_BPR16(Element):
    """Check Issue or EFT Effective Date"""
    class Schema:
        json = {'title': 'Check Issue or EFT Effective Date',
         'usage': 'R',
         'description': 'xid=BPR16 data_ele=373',
         'sequence': 16,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_BPR17(Element):
    """Business Function Code"""
    class Schema:
        json = {'title': 'Business Function Code',
         'usage': 'N',
         'description': 'xid=BPR17 data_ele=1048',
         'sequence': 17,
         'type': {'$ref': '#/$common/1048'}}
        datatype = common.D_1048
        min_len = 1
        max_len = 3


class HEADER_BPR18(Element):
    """(DFI) ID Number Qualifier"""
    class Schema:
        json = {'title': '(DFI) ID Number Qualifier',
         'usage': 'N',
         'description': 'xid=BPR18 data_ele=506',
         'sequence': 18,
         'type': {'$ref': '#/$common/506'}}
        datatype = common.D_506
        min_len = 2
        max_len = 2


class HEADER_BPR19(Element):
    """(DFI) Identification Number"""
    class Schema:
        json = {'title': '(DFI) Identification Number',
         'usage': 'N',
         'description': 'xid=BPR19 data_ele=507',
         'sequence': 19,
         'type': {'$ref': '#/$common/507'}}
        datatype = common.D_507
        min_len = 3
        max_len = 12


class HEADER_BPR20(Element):
    """Account Number Qualifier"""
    class Schema:
        json = {'title': 'Account Number Qualifier',
         'usage': 'N',
         'description': 'xid=BPR20 data_ele=569',
         'sequence': 20,
         'type': {'$ref': '#/$common/569'}}
        datatype = common.D_569
        min_len = 1
        max_len = 3


class HEADER_BPR21(Element):
    """Account Number"""
    class Schema:
        json = {'title': 'Account Number',
         'usage': 'N',
         'description': 'xid=BPR21 data_ele=508',
         'sequence': 21,
         'type': {'$ref': '#/$common/508'}}
        datatype = common.D_508
        min_len = 1
        max_len = 35


class HEADER_BPR(Segment):
    """Financial Information"""
    class Schema:
        json = {'title': 'Financial Information',
         'usage': 'R',
         'description': 'xid=BPR name=Financial Information',
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
         'required': ['bpr01', 'bpr02', 'bpr03', 'bpr04', 'bpr16']}
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
    bpr10: HEADER_BPR10 | None
    bpr11: HEADER_BPR11 | None
    bpr12: HEADER_BPR12 | None
    bpr13: HEADER_BPR13 | None
    bpr14: HEADER_BPR14 | None
    bpr15: HEADER_BPR15 | None
    bpr16: HEADER_BPR16


class HEADER_TRN01(Element):
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


class HEADER_TRN02(Element):
    """Check or EFT Trace Number"""
    class Schema:
        json = {'title': 'Check or EFT Trace Number',
         'usage': 'R',
         'description': 'xid=TRN02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_TRN03(Element):
    """Payer Identifier"""
    class Schema:
        json = {'title': 'Payer Identifier',
         'usage': 'R',
         'description': 'xid=TRN03 data_ele=509',
         'sequence': 3,
         'type': {'$ref': '#/$common/509'}}
        datatype = common.D_509
        min_len = 10
        max_len = 10


class HEADER_TRN04(Element):
    """Originating Company Supplemental Code"""
    class Schema:
        json = {'title': 'Originating Company Supplemental Code',
         'usage': 'S',
         'description': 'xid=TRN04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class HEADER_TRN(Segment):
    """Reassociation Trace Number"""
    class Schema:
        json = {'title': 'Reassociation Trace Number',
         'usage': 'R',
         'description': 'xid=TRN name=Reassociation Trace Number',
         'position': 400,
         'type': 'object',
         'properties': {'xid': {'literal': 'TRN'},
                        'trn01': {'$ref': '#/$elements/HEADER_TRN01'},
                        'trn02': {'$ref': '#/$elements/HEADER_TRN02'},
                        'trn03': {'$ref': '#/$elements/HEADER_TRN03'},
                        'trn04': {'$ref': '#/$elements/HEADER_TRN04'}},
         'required': ['trn01', 'trn02', 'trn03']}
        segment_name = 'TRN'
    trn01: HEADER_TRN01
    trn02: HEADER_TRN02
    trn03: HEADER_TRN03
    trn04: HEADER_TRN04 | None


class HEADER_CUR01(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=CUR01 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PR']}]}}
        datatype = common.D_98
        codes = ['PR']
        min_len = 2
        max_len = 3


class HEADER_CUR02(Element):
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


class HEADER_CUR03(Element):
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


class HEADER_CUR04(Element):
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


class HEADER_CUR05(Element):
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


class HEADER_CUR06(Element):
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


class HEADER_CUR07(Element):
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


class HEADER_CUR08(Element):
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


class HEADER_CUR09(Element):
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


class HEADER_CUR10(Element):
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


class HEADER_CUR11(Element):
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


class HEADER_CUR12(Element):
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


class HEADER_CUR13(Element):
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


class HEADER_CUR14(Element):
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


class HEADER_CUR15(Element):
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


class HEADER_CUR16(Element):
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


class HEADER_CUR17(Element):
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


class HEADER_CUR18(Element):
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


class HEADER_CUR19(Element):
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


class HEADER_CUR20(Element):
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


class HEADER_CUR21(Element):
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


class HEADER_CUR(Segment):
    """Foreign Currency Information"""
    class Schema:
        json = {'title': 'Foreign Currency Information',
         'usage': 'S',
         'description': 'xid=CUR name=Foreign Currency Information',
         'position': 500,
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
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['EV']}]}}
        datatype = common.D_128
        codes = ['EV']
        min_len = 2
        max_len = 3


class HEADER_REF02(Element):
    """Receiver Identifier"""
    class Schema:
        json = {'title': 'Receiver Identifier',
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


class HEADER_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class HEADER_REF(Segment):
    """Receiver Identification"""
    class Schema:
        json = {'title': 'Receiver Identification',
         'usage': 'S',
         'description': 'xid=REF name=Receiver Identification',
         'position': 600,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                        'ref02': {'$ref': '#/$elements/HEADER_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02


class HEADER_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['F2']}]}}
        datatype = common.D_128
        codes = ['F2']
        min_len = 2
        max_len = 3


class HEADER_REF02(Element):
    """Version Identification Code"""
    class Schema:
        json = {'title': 'Version Identification Code',
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


class HEADER_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class HEADER_REF(Segment):
    """Version Identification"""
    class Schema:
        json = {'title': 'Version Identification',
         'usage': 'S',
         'description': 'xid=REF name=Version Identification',
         'position': 600,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                        'ref02': {'$ref': '#/$elements/HEADER_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02


class HEADER_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['405']}]}}
        datatype = common.D_374
        codes = ['405']
        min_len = 3
        max_len = 3


class HEADER_DTM02(Element):
    """Production Date"""
    class Schema:
        json = {'title': 'Production Date',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class HEADER_DTM03(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class HEADER_DTM04(Element):
    """Time Code"""
    class Schema:
        json = {'title': 'Time Code',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class HEADER_DTM05(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class HEADER_DTM06(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class HEADER_DTM(Segment):
    """Production Date"""
    class Schema:
        json = {'title': 'Production Date',
         'usage': 'S',
         'description': 'xid=DTM name=Production Date',
         'position': 700,
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
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PR']}]}}
        datatype = common.D_98
        codes = ['PR']
        min_len = 2
        max_len = 3


class L1000A_N102(Element):
    """Payer Name"""
    class Schema:
        json = {'title': 'Payer Name',
         'usage': 'R',
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
         'usage': 'S',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['XV']}]}}
        datatype = common.D_66
        codes = ['XV']
        min_len = 1
        max_len = 2


class L1000A_N104(Element):
    """Payer Identifier"""
    class Schema:
        json = {'title': 'Payer Identifier',
         'usage': 'S',
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
    """Payer Identification"""
    class Schema:
        json = {'title': 'Payer Identification',
         'usage': 'R',
         'description': 'xid=N1 name=Payer Identification',
         'position': 800,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000A_N101'},
                        'n102': {'$ref': '#/$elements/L1000A_N102'},
                        'n103': {'$ref': '#/$elements/L1000A_N103'},
                        'n104': {'$ref': '#/$elements/L1000A_N104'}},
         'required': ['n101', 'n102']}
        segment_name = 'N1'
    n101: L1000A_N101
    n102: L1000A_N102
    n103: L1000A_N103 | None
    n104: L1000A_N104 | None


class L1000A_N301(Element):
    """Payer Address Line"""
    class Schema:
        json = {'title': 'Payer Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000A_N302(Element):
    """Payer Address Line"""
    class Schema:
        json = {'title': 'Payer Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000A_N3(Segment):
    """Payer Address"""
    class Schema:
        json = {'title': 'Payer Address',
         'usage': 'R',
         'description': 'xid=N3 name=Payer Address',
         'position': 1000,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L1000A_N301'},
                        'n302': {'$ref': '#/$elements/L1000A_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L1000A_N301
    n302: L1000A_N302 | None


class L1000A_N401(Element):
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


class L1000A_N402(Element):
    """Payer State Code"""
    class Schema:
        json = {'title': 'Payer State Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L1000A_N403(Element):
    """Payer Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Payer Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L1000A_N404(Element):
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


class L1000A_N405(Element):
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


class L1000A_N406(Element):
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


class L1000A_N407(Element):
    """Country Subdivision Code"""
    class Schema:
        json = {'title': 'Country Subdivision Code',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'sequence': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L1000A_N4(Segment):
    """Payer City, State, ZIP Code"""
    class Schema:
        json = {'title': 'Payer City, State, ZIP Code',
         'usage': 'R',
         'description': 'xid=N4 name=Payer City, State, ZIP Code',
         'position': 1100,
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


class L1000A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['2U', 'EO', 'HI', 'NF']}]}}
        datatype = common.D_128
        codes = ['2U', 'EO', 'HI', 'NF']
        min_len = 2
        max_len = 3


class L1000A_REF02(Element):
    """Additional Payer Identifier"""
    class Schema:
        json = {'title': 'Additional Payer Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L1000A_REF03(Element):
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


class L1000A_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L1000A_REF(Segment):
    """Additional Payer Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Payer Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Additional Payer Identification',
                   'position': 1200,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L1000A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L1000A_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 4}
        segment_name = 'REF'
    ref01: L1000A_REF01
    ref02: L1000A_REF02


class L1000A_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['CX']}]}}
        datatype = common.D_366
        codes = ['CX']
        min_len = 2
        max_len = 2


class L1000A_PER02(Element):
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


class L1000A_PER03(Element):
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


class L1000A_PER04(Element):
    """Payer Contact Communication Number"""
    class Schema:
        json = {'title': 'Payer Contact Communication Number',
         'usage': 'S',
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
                            {'enum': ['EM', 'EX', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L1000A_PER06(Element):
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


class L1000A_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EX']}]}}
        datatype = common.D_365
        codes = ['EX']
        min_len = 2
        max_len = 2


class L1000A_PER08(Element):
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
    """Payer Business Contact Information"""
    class Schema:
        json = {'title': 'Payer Business Contact Information',
         'usage': 'S',
         'description': 'xid=PER name=Payer Business Contact Information',
         'position': 1300,
         'syntax': ['P0304', 'P0506', 'P0708'],
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
         'required': ['per01']}
        segment_name = 'PER'
    per01: L1000A_PER01
    per02: L1000A_PER02 | None
    per03: L1000A_PER03 | None
    per04: L1000A_PER04 | None
    per05: L1000A_PER05 | None
    per06: L1000A_PER06 | None
    per07: L1000A_PER07 | None
    per08: L1000A_PER08 | None


class L1000A_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['BL']}]}}
        datatype = common.D_366
        codes = ['BL']
        min_len = 2
        max_len = 2


class L1000A_PER02(Element):
    """Payer Technical Contact Name"""
    class Schema:
        json = {'title': 'Payer Technical Contact Name',
         'usage': 'S',
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
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'TE', 'UR']}]}}
        datatype = common.D_365
        codes = ['EM', 'TE', 'UR']
        min_len = 2
        max_len = 2


class L1000A_PER04(Element):
    """Payer Contact Communication Number"""
    class Schema:
        json = {'title': 'Payer Contact Communication Number',
         'usage': 'S',
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
                            {'enum': ['EM', 'EX', 'FX', 'TE', 'UR']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'TE', 'UR']
        min_len = 2
        max_len = 2


class L1000A_PER06(Element):
    """Payer Technical Contact Communication Number"""
    class Schema:
        json = {'title': 'Payer Technical Contact Communication Number',
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
                            {'enum': ['EM', 'EX', 'FX', 'UR']}]}}
        datatype = common.D_365
        codes = ['EM', 'EX', 'FX', 'UR']
        min_len = 2
        max_len = 2


class L1000A_PER08(Element):
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
    """Payer Technical Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer Technical Contact Information',
                   'usage': 'R',
                   'description': 'xid=PER name=Payer Technical Contact Information',
                   'position': 1300,
                   'syntax': ['P0304', 'P0506', 'P0708'],
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
                   'required': ['per01']}}
        segment_name = 'PER'
    per01: L1000A_PER01
    per02: L1000A_PER02 | None
    per03: L1000A_PER03 | None
    per04: L1000A_PER04 | None
    per05: L1000A_PER05 | None
    per06: L1000A_PER06 | None
    per07: L1000A_PER07 | None
    per08: L1000A_PER08 | None


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


class L1000A_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['UR']}]}}
        datatype = common.D_365
        codes = ['UR']
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
         'usage': 'N',
         'description': 'xid=PER05 data_ele=365',
         'sequence': 5,
         'type': {'$ref': '#/$common/365'}}
        datatype = common.D_365
        min_len = 2
        max_len = 2


class L1000A_PER06(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'N',
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
         'usage': 'N',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'$ref': '#/$common/365'}}
        datatype = common.D_365
        min_len = 2
        max_len = 2


class L1000A_PER08(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'N',
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
    """Payer WEB Site"""
    class Schema:
        json = {'title': 'Payer WEB Site',
         'usage': 'S',
         'description': 'xid=PER name=Payer WEB Site',
         'position': 1300,
         'syntax': ['P0304', 'P0506', 'P0708'],
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L1000A_PER01'},
                        'per03': {'$ref': '#/$elements/L1000A_PER03'},
                        'per04': {'$ref': '#/$elements/L1000A_PER04'}},
         'required': ['per01', 'per03', 'per04']}
        segment_name = 'PER'
    per01: L1000A_PER01
    per03: L1000A_PER03
    per04: L1000A_PER04


class L1000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer Identification',
                   'usage': 'R',
                   'description': 'xid=1000A name=Payer Identification type=None',
                   'position': 800,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000A_N1'},
                                  'n3': {'$ref': '#/$segments/L1000A_N3'},
                                  'n4': {'$ref': '#/$segments/L1000A_N4'},
                                  'ref': {'$ref': '#/$segments/L1000A_REF'},
                                  'per': {'$ref': '#/$segments/L1000A_PER'}},
                   'required': ['n1', 'n3', 'n4', 'per']},
         'maxItems': 1}
    n1: L1000A_N1
    n3: L1000A_N3
    n4: L1000A_N4
    ref: list[L1000A_REF] | None
    per: L1000A_PER
    per: list[L1000A_PER]
    per: L1000A_PER


class L1000B_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PE']}]}}
        datatype = common.D_98
        codes = ['PE']
        min_len = 2
        max_len = 3


class L1000B_N102(Element):
    """Payee Name"""
    class Schema:
        json = {'title': 'Payee Name',
         'usage': 'R',
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
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'XV', 'XX']}]}}
        datatype = common.D_66
        codes = ['FI', 'XV', 'XX']
        min_len = 1
        max_len = 2


class L1000B_N104(Element):
    """Payee Identification Code"""
    class Schema:
        json = {'title': 'Payee Identification Code',
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
    """Payee Identification"""
    class Schema:
        json = {'title': 'Payee Identification',
         'usage': 'R',
         'description': 'xid=N1 name=Payee Identification',
         'position': 800,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000B_N101'},
                        'n102': {'$ref': '#/$elements/L1000B_N102'},
                        'n103': {'$ref': '#/$elements/L1000B_N103'},
                        'n104': {'$ref': '#/$elements/L1000B_N104'}},
         'required': ['n101', 'n102', 'n103', 'n104']}
        segment_name = 'N1'
    n101: L1000B_N101
    n102: L1000B_N102
    n103: L1000B_N103
    n104: L1000B_N104


class L1000B_N301(Element):
    """Payee Address Line"""
    class Schema:
        json = {'title': 'Payee Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'sequence': 1,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000B_N302(Element):
    """Payee Address Line"""
    class Schema:
        json = {'title': 'Payee Address Line',
         'usage': 'S',
         'description': 'xid=N302 data_ele=166',
         'sequence': 2,
         'type': {'$ref': '#/$common/166'}}
        datatype = common.D_166
        min_len = 1
        max_len = 55


class L1000B_N3(Segment):
    """Payee Address"""
    class Schema:
        json = {'title': 'Payee Address',
         'usage': 'S',
         'description': 'xid=N3 name=Payee Address',
         'position': 1000,
         'type': 'object',
         'properties': {'xid': {'literal': 'N3'},
                        'n301': {'$ref': '#/$elements/L1000B_N301'},
                        'n302': {'$ref': '#/$elements/L1000B_N302'}},
         'required': ['n301']}
        segment_name = 'N3'
    n301: L1000B_N301
    n302: L1000B_N302 | None


class L1000B_N401(Element):
    """Payee City Name"""
    class Schema:
        json = {'title': 'Payee City Name',
         'usage': 'R',
         'description': 'xid=N401 data_ele=19',
         'sequence': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L1000B_N402(Element):
    """Payee State Code"""
    class Schema:
        json = {'title': 'Payee State Code',
         'usage': 'S',
         'description': 'xid=N402 data_ele=156',
         'sequence': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L1000B_N403(Element):
    """Payee Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Payee Postal Zone or ZIP Code',
         'usage': 'S',
         'description': 'xid=N403 data_ele=116',
         'sequence': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L1000B_N404(Element):
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


class L1000B_N405(Element):
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


class L1000B_N406(Element):
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


class L1000B_N407(Element):
    """Country Subdivision Code"""
    class Schema:
        json = {'title': 'Country Subdivision Code',
         'usage': 'S',
         'description': 'xid=N407 data_ele=1715',
         'sequence': 7,
         'type': {'$ref': '#/$common/1715'}}
        datatype = common.D_1715
        min_len = 1
        max_len = 3


class L1000B_N4(Segment):
    """Payee City, State, ZIP Code"""
    class Schema:
        json = {'title': 'Payee City, State, ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Payee City, State, ZIP Code',
         'position': 1100,
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


class L1000B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', 'D3', 'PQ', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', 'D3', 'PQ', 'TJ']
        min_len = 2
        max_len = 3


class L1000B_REF02(Element):
    """Additional Payee Identifier"""
    class Schema:
        json = {'title': 'Additional Payee Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L1000B_REF03(Element):
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


class L1000B_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L1000B_REF(Segment):
    """Payee Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payee Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Payee Additional Identification',
                   'position': 1200,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L1000B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L1000B_REF02'}},
                   'required': ['ref01', 'ref02']}}
        segment_name = 'REF'
    ref01: L1000B_REF01
    ref02: L1000B_REF02


class L1000B_RDM01(Element):
    """Report Transmission Code"""
    class Schema:
        json = {'title': 'Report Transmission Code',
         'usage': 'R',
         'description': 'xid=RDM01 data_ele=756',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/756'},
                            {'enum': ['BM', 'EM', 'FT', 'OL']}]}}
        datatype = common.D_756
        codes = ['BM', 'EM', 'FT', 'OL']
        min_len = 1
        max_len = 2


class L1000B_RDM02(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'S',
         'description': 'xid=RDM02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1000B_RDM03(Element):
    """Communication Number"""
    class Schema:
        json = {'title': 'Communication Number',
         'usage': 'S',
         'description': 'xid=RDM03 data_ele=364',
         'sequence': 3,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L1000B_RDM04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=RDM04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L1000B_RDM05(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=RDM05 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 5,
         'syntax': []}


class L1000B_RDM(Segment):
    """Remittance Delivery Method"""
    class Schema:
        json = {'title': 'Remittance Delivery Method',
         'usage': 'S',
         'description': 'xid=RDM name=Remittance Delivery Method',
         'position': 1400,
         'type': 'object',
         'properties': {'xid': {'literal': 'RDM'},
                        'rdm01': {'$ref': '#/$elements/L1000B_RDM01'},
                        'rdm02': {'$ref': '#/$elements/L1000B_RDM02'},
                        'rdm03': {'$ref': '#/$elements/L1000B_RDM03'}},
         'required': ['rdm01']}
        segment_name = 'RDM'
    rdm01: L1000B_RDM01
    rdm02: L1000B_RDM02 | None
    rdm03: L1000B_RDM03 | None


class L1000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payee Identification',
                   'usage': 'R',
                   'description': 'xid=1000B name=Payee Identification type=None',
                   'position': 1400,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000B_N1'},
                                  'n3': {'$ref': '#/$segments/L1000B_N3'},
                                  'n4': {'$ref': '#/$segments/L1000B_N4'},
                                  'ref': {'$ref': '#/$segments/L1000B_REF'},
                                  'rdm': {'$ref': '#/$segments/L1000B_RDM'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000B_N1
    n3: L1000B_N3 | None
    n4: L1000B_N4 | None
    ref: list[L1000B_REF] | None
    rdm: L1000B_RDM | None


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Header type=wrapper',
                   'position': 110,
                   'type': 'object',
                   'properties': {'bpr': {'$ref': '#/$segments/HEADER_BPR'},
                                  'trn': {'$ref': '#/$segments/HEADER_TRN'},
                                  'cur': {'$ref': '#/$segments/HEADER_CUR'},
                                  'ref': {'$ref': '#/$segments/HEADER_REF'},
                                  'dtm': {'$ref': '#/$segments/HEADER_DTM'},
                                  'l1000a': {'$ref': '#/$segments/L1000A'},
                                  'l1000b': {'$ref': '#/$segments/L1000B'}},
                   'required': ['bpr', 'trn', 'l1000a', 'l1000b']},
         'maxItems': 1}
    bpr: HEADER_BPR
    trn: HEADER_TRN
    cur: HEADER_CUR | None
    ref: HEADER_REF | None
    ref: HEADER_REF | None
    dtm: HEADER_DTM | None
    l1000a: list[L1000A]
    l1000b: list[L1000B]


class L2000_LX01(Element):
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


class L2000_LX(Segment):
    """Header Number"""
    class Schema:
        json = {'title': 'Header Number',
         'usage': 'R',
         'description': 'xid=LX name=Header Number',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'LX'},
                        'lx01': {'$ref': '#/$elements/L2000_LX01'}},
         'required': ['lx01']}
        segment_name = 'LX'
    lx01: L2000_LX01


class L2000_TS301(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
         'description': 'xid=TS301 data_ele=127',
         'sequence': 1,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2000_TS302(Element):
    """Facility Type Code"""
    class Schema:
        json = {'title': 'Facility Type Code',
         'usage': 'R',
         'description': 'xid=TS302 data_ele=1331',
         'sequence': 2,
         'type': {'$ref': '#/$common/1331'}}
        datatype = common.D_1331
        min_len = 1
        max_len = 2


class L2000_TS303(Element):
    """Fiscal Period Date"""
    class Schema:
        json = {'title': 'Fiscal Period Date',
         'usage': 'R',
         'description': 'xid=TS303 data_ele=373',
         'sequence': 3,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2000_TS304(Element):
    """Total Claim Count"""
    class Schema:
        json = {'title': 'Total Claim Count',
         'usage': 'R',
         'description': 'xid=TS304 data_ele=380',
         'sequence': 4,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS305(Element):
    """Total Claim Charge Amount"""
    class Schema:
        json = {'title': 'Total Claim Charge Amount',
         'usage': 'R',
         'description': 'xid=TS305 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS306(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS306 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS307(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS307 data_ele=782',
         'sequence': 7,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS308(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS308 data_ele=782',
         'sequence': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS309(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS309 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS310(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS310 data_ele=782',
         'sequence': 10,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS311(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS311 data_ele=782',
         'sequence': 11,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS312(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS312 data_ele=782',
         'sequence': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS313(Element):
    """Total MSP Payer Amount"""
    class Schema:
        json = {'title': 'Total MSP Payer Amount',
         'usage': 'S',
         'description': 'xid=TS313 data_ele=782',
         'sequence': 13,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS314(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS314 data_ele=782',
         'sequence': 14,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS315(Element):
    """Total Non-Lab Charge Amount"""
    class Schema:
        json = {'title': 'Total Non-Lab Charge Amount',
         'usage': 'S',
         'description': 'xid=TS315 data_ele=782',
         'sequence': 15,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS316(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS316 data_ele=782',
         'sequence': 16,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS317(Element):
    """Total HCPCS Reported Charge Amount"""
    class Schema:
        json = {'title': 'Total HCPCS Reported Charge Amount',
         'usage': 'S',
         'description': 'xid=TS317 data_ele=782',
         'sequence': 17,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS318(Element):
    """Total HCPCS Payable Amount"""
    class Schema:
        json = {'title': 'Total HCPCS Payable Amount',
         'usage': 'S',
         'description': 'xid=TS318 data_ele=782',
         'sequence': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS319(Element):
    """Monetary Amount"""
    class Schema:
        json = {'title': 'Monetary Amount',
         'usage': 'N',
         'description': 'xid=TS319 data_ele=782',
         'sequence': 19,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS320(Element):
    """Total Professional Component Amount"""
    class Schema:
        json = {'title': 'Total Professional Component Amount',
         'usage': 'S',
         'description': 'xid=TS320 data_ele=782',
         'sequence': 20,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS321(Element):
    """Total MSP Patient Liability Met Amount"""
    class Schema:
        json = {'title': 'Total MSP Patient Liability Met Amount',
         'usage': 'S',
         'description': 'xid=TS321 data_ele=782',
         'sequence': 21,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS322(Element):
    """Total Patient Reimbursement Amount"""
    class Schema:
        json = {'title': 'Total Patient Reimbursement Amount',
         'usage': 'S',
         'description': 'xid=TS322 data_ele=782',
         'sequence': 22,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS323(Element):
    """Total PIP Claim Count"""
    class Schema:
        json = {'title': 'Total PIP Claim Count',
         'usage': 'S',
         'description': 'xid=TS323 data_ele=380',
         'sequence': 23,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS324(Element):
    """Total PIP Adjustment Amount"""
    class Schema:
        json = {'title': 'Total PIP Adjustment Amount',
         'usage': 'S',
         'description': 'xid=TS324 data_ele=782',
         'sequence': 24,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS3(Segment):
    """Provider Summary Information"""
    class Schema:
        json = {'title': 'Provider Summary Information',
         'usage': 'S',
         'description': 'xid=TS3 name=Provider Summary Information',
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'TS3'},
                        'ts301': {'$ref': '#/$elements/L2000_TS301'},
                        'ts302': {'$ref': '#/$elements/L2000_TS302'},
                        'ts303': {'$ref': '#/$elements/L2000_TS303'},
                        'ts304': {'$ref': '#/$elements/L2000_TS304'},
                        'ts305': {'$ref': '#/$elements/L2000_TS305'},
                        'ts313': {'$ref': '#/$elements/L2000_TS313'},
                        'ts315': {'$ref': '#/$elements/L2000_TS315'},
                        'ts317': {'$ref': '#/$elements/L2000_TS317'},
                        'ts318': {'$ref': '#/$elements/L2000_TS318'},
                        'ts320': {'$ref': '#/$elements/L2000_TS320'},
                        'ts321': {'$ref': '#/$elements/L2000_TS321'},
                        'ts322': {'$ref': '#/$elements/L2000_TS322'},
                        'ts323': {'$ref': '#/$elements/L2000_TS323'},
                        'ts324': {'$ref': '#/$elements/L2000_TS324'}},
         'required': ['ts301', 'ts302', 'ts303', 'ts304', 'ts305']}
        segment_name = 'TS3'
    ts301: L2000_TS301
    ts302: L2000_TS302
    ts303: L2000_TS303
    ts304: L2000_TS304
    ts305: L2000_TS305
    ts313: L2000_TS313 | None
    ts315: L2000_TS315 | None
    ts317: L2000_TS317 | None
    ts318: L2000_TS318 | None
    ts320: L2000_TS320 | None
    ts321: L2000_TS321 | None
    ts322: L2000_TS322 | None
    ts323: L2000_TS323 | None
    ts324: L2000_TS324 | None


class L2000_TS201(Element):
    """Total DRG Amount"""
    class Schema:
        json = {'title': 'Total DRG Amount',
         'usage': 'S',
         'description': 'xid=TS201 data_ele=782',
         'sequence': 1,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS202(Element):
    """Total Federal Specific Amount"""
    class Schema:
        json = {'title': 'Total Federal Specific Amount',
         'usage': 'S',
         'description': 'xid=TS202 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS203(Element):
    """Total Hospital Specific Amount"""
    class Schema:
        json = {'title': 'Total Hospital Specific Amount',
         'usage': 'S',
         'description': 'xid=TS203 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS204(Element):
    """Total Disproportionate Share Amount"""
    class Schema:
        json = {'title': 'Total Disproportionate Share Amount',
         'usage': 'S',
         'description': 'xid=TS204 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS205(Element):
    """Total Capital Amount"""
    class Schema:
        json = {'title': 'Total Capital Amount',
         'usage': 'S',
         'description': 'xid=TS205 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS206(Element):
    """Total Indirect Medical Education Amount"""
    class Schema:
        json = {'title': 'Total Indirect Medical Education Amount',
         'usage': 'S',
         'description': 'xid=TS206 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS207(Element):
    """Total Outlier Day Count"""
    class Schema:
        json = {'title': 'Total Outlier Day Count',
         'usage': 'S',
         'description': 'xid=TS207 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS208(Element):
    """Total Day Outlier Amount"""
    class Schema:
        json = {'title': 'Total Day Outlier Amount',
         'usage': 'S',
         'description': 'xid=TS208 data_ele=782',
         'sequence': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS209(Element):
    """Total Cost Outlier Amount"""
    class Schema:
        json = {'title': 'Total Cost Outlier Amount',
         'usage': 'S',
         'description': 'xid=TS209 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS210(Element):
    """Average DRG Length of Stay"""
    class Schema:
        json = {'title': 'Average DRG Length of Stay',
         'usage': 'S',
         'description': 'xid=TS210 data_ele=380',
         'sequence': 10,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS211(Element):
    """Total Discharge Count"""
    class Schema:
        json = {'title': 'Total Discharge Count',
         'usage': 'S',
         'description': 'xid=TS211 data_ele=380',
         'sequence': 11,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS212(Element):
    """Total Cost Report Day Count"""
    class Schema:
        json = {'title': 'Total Cost Report Day Count',
         'usage': 'S',
         'description': 'xid=TS212 data_ele=380',
         'sequence': 12,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS213(Element):
    """Total Covered Day Count"""
    class Schema:
        json = {'title': 'Total Covered Day Count',
         'usage': 'S',
         'description': 'xid=TS213 data_ele=380',
         'sequence': 13,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS214(Element):
    """Total Noncovered Day Count"""
    class Schema:
        json = {'title': 'Total Noncovered Day Count',
         'usage': 'S',
         'description': 'xid=TS214 data_ele=380',
         'sequence': 14,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS215(Element):
    """Total MSP Pass-Through Amount"""
    class Schema:
        json = {'title': 'Total MSP Pass-Through Amount',
         'usage': 'S',
         'description': 'xid=TS215 data_ele=782',
         'sequence': 15,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS216(Element):
    """Average DRG weight"""
    class Schema:
        json = {'title': 'Average DRG weight',
         'usage': 'S',
         'description': 'xid=TS216 data_ele=380',
         'sequence': 16,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2000_TS217(Element):
    """Total PPS Capital FSP DRG Amount"""
    class Schema:
        json = {'title': 'Total PPS Capital FSP DRG Amount',
         'usage': 'S',
         'description': 'xid=TS217 data_ele=782',
         'sequence': 17,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS218(Element):
    """Total PPS Capital HSP DRG Amount"""
    class Schema:
        json = {'title': 'Total PPS Capital HSP DRG Amount',
         'usage': 'S',
         'description': 'xid=TS218 data_ele=782',
         'sequence': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS219(Element):
    """Total PPS DSH DRG Amount"""
    class Schema:
        json = {'title': 'Total PPS DSH DRG Amount',
         'usage': 'S',
         'description': 'xid=TS219 data_ele=782',
         'sequence': 19,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS2(Segment):
    """Provider Supplemental Summary Information"""
    class Schema:
        json = {'title': 'Provider Supplemental Summary Information',
         'usage': 'S',
         'description': 'xid=TS2 name=Provider Supplemental Summary Information',
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'TS2'},
                        'ts201': {'$ref': '#/$elements/L2000_TS201'},
                        'ts202': {'$ref': '#/$elements/L2000_TS202'},
                        'ts203': {'$ref': '#/$elements/L2000_TS203'},
                        'ts204': {'$ref': '#/$elements/L2000_TS204'},
                        'ts205': {'$ref': '#/$elements/L2000_TS205'},
                        'ts206': {'$ref': '#/$elements/L2000_TS206'},
                        'ts207': {'$ref': '#/$elements/L2000_TS207'},
                        'ts208': {'$ref': '#/$elements/L2000_TS208'},
                        'ts209': {'$ref': '#/$elements/L2000_TS209'},
                        'ts210': {'$ref': '#/$elements/L2000_TS210'},
                        'ts211': {'$ref': '#/$elements/L2000_TS211'},
                        'ts212': {'$ref': '#/$elements/L2000_TS212'},
                        'ts213': {'$ref': '#/$elements/L2000_TS213'},
                        'ts214': {'$ref': '#/$elements/L2000_TS214'},
                        'ts215': {'$ref': '#/$elements/L2000_TS215'},
                        'ts216': {'$ref': '#/$elements/L2000_TS216'},
                        'ts217': {'$ref': '#/$elements/L2000_TS217'},
                        'ts218': {'$ref': '#/$elements/L2000_TS218'},
                        'ts219': {'$ref': '#/$elements/L2000_TS219'}}}
        segment_name = 'TS2'
    ts201: L2000_TS201 | None
    ts202: L2000_TS202 | None
    ts203: L2000_TS203 | None
    ts204: L2000_TS204 | None
    ts205: L2000_TS205 | None
    ts206: L2000_TS206 | None
    ts207: L2000_TS207 | None
    ts208: L2000_TS208 | None
    ts209: L2000_TS209 | None
    ts210: L2000_TS210 | None
    ts211: L2000_TS211 | None
    ts212: L2000_TS212 | None
    ts213: L2000_TS213 | None
    ts214: L2000_TS214 | None
    ts215: L2000_TS215 | None
    ts216: L2000_TS216 | None
    ts217: L2000_TS217 | None
    ts218: L2000_TS218 | None
    ts219: L2000_TS219 | None


class L2100_CLP01(Element):
    """Patient Control Number"""
    class Schema:
        json = {'title': 'Patient Control Number',
         'usage': 'R',
         'description': 'xid=CLP01 data_ele=1028',
         'sequence': 1,
         'type': {'$ref': '#/$common/1028'}}
        datatype = common.D_1028
        min_len = 1
        max_len = 38


class L2100_CLP02(Element):
    """Claim Status Code"""
    class Schema:
        json = {'title': 'Claim Status Code',
         'usage': 'R',
         'description': 'xid=CLP02 data_ele=1029',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/1029'},
                            {'enum': ['1', '19', '2', '20', '21', '22', '23', '25', '3',
                                      '4']}]}}
        datatype = common.D_1029
        codes = ['1', '19', '2', '20', '21', '22', '23', '25', '3', '4']
        min_len = 1
        max_len = 2


class L2100_CLP03(Element):
    """Total Claim Charge Amount"""
    class Schema:
        json = {'title': 'Total Claim Charge Amount',
         'usage': 'R',
         'description': 'xid=CLP03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_CLP04(Element):
    """Claim Payment Amount"""
    class Schema:
        json = {'title': 'Claim Payment Amount',
         'usage': 'R',
         'description': 'xid=CLP04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_CLP05(Element):
    """Patient Responsibility Amount"""
    class Schema:
        json = {'title': 'Patient Responsibility Amount',
         'usage': 'S',
         'description': 'xid=CLP05 data_ele=782',
         'sequence': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_CLP06(Element):
    """Claim Filing Indicator Code"""
    class Schema:
        json = {'title': 'Claim Filing Indicator Code',
         'usage': 'R',
         'description': 'xid=CLP06 data_ele=1032',
         'sequence': 6,
         'type': {'allOf': [{'$ref': '#/$common/1032'},
                            {'enum': ['12', '13', '14', '15', '16', '17', 'AM', 'CH',
                                      'DS', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV',
                                      'VA', 'WC', 'ZZ']}]}}
        datatype = common.D_1032
        codes = ['12', '13', '14', '15', '16', '17', 'AM', 'CH', 'DS', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ']
        min_len = 1
        max_len = 2


class L2100_CLP07(Element):
    """Payer Claim Control Number"""
    class Schema:
        json = {'title': 'Payer Claim Control Number',
         'usage': 'R',
         'description': 'xid=CLP07 data_ele=127',
         'sequence': 7,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2100_CLP08(Element):
    """Facility Type Code"""
    class Schema:
        json = {'title': 'Facility Type Code',
         'usage': 'S',
         'description': 'xid=CLP08 data_ele=1331',
         'sequence': 8,
         'type': {'$ref': '#/$common/1331'}}
        datatype = common.D_1331
        min_len = 1
        max_len = 2


class L2100_CLP09(Element):
    """Claim Frequency Code"""
    class Schema:
        json = {'title': 'Claim Frequency Code',
         'usage': 'S',
         'description': 'xid=CLP09 data_ele=1325',
         'sequence': 9,
         'type': {'$ref': '#/$common/1325'}}
        datatype = common.D_1325
        min_len = 1
        max_len = 1


class L2100_CLP10(Element):
    """Patient Status Code"""
    class Schema:
        json = {'title': 'Patient Status Code',
         'usage': 'N',
         'description': 'xid=CLP10 data_ele=1352',
         'sequence': 10,
         'type': {'$ref': '#/$common/1352'}}
        datatype = common.D_1352
        min_len = 1
        max_len = 2


class L2100_CLP11(Element):
    """Diagnosis Related Group (DRG) Code"""
    class Schema:
        json = {'title': 'Diagnosis Related Group (DRG) Code',
         'usage': 'S',
         'description': 'xid=CLP11 data_ele=1354',
         'sequence': 11,
         'type': {'$ref': '#/$common/1354'}}
        datatype = common.D_1354
        min_len = 1
        max_len = 4


class L2100_CLP12(Element):
    """Diagnosis Related Group (DRG) Weight"""
    class Schema:
        json = {'title': 'Diagnosis Related Group (DRG) Weight',
         'usage': 'S',
         'description': 'xid=CLP12 data_ele=380',
         'sequence': 12,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_CLP13(Element):
    """Discharge Fraction"""
    class Schema:
        json = {'title': 'Discharge Fraction',
         'usage': 'S',
         'description': 'xid=CLP13 data_ele=954',
         'sequence': 13,
         'type': {'$ref': '#/$common/954'}}
        datatype = common.D_954
        min_len = 1
        max_len = 10


class L2100_CLP14(Element):
    """Yes/No Condition or Response Code"""
    class Schema:
        json = {'title': 'Yes/No Condition or Response Code',
         'usage': 'N',
         'description': 'xid=CLP14 data_ele=1073',
         'sequence': 14,
         'type': {'$ref': '#/$common/1073'}}
        datatype = common.D_1073
        min_len = 1
        max_len = 1


class L2100_CLP(Segment):
    """Claim Payment Information"""
    class Schema:
        json = {'title': 'Claim Payment Information',
         'usage': 'R',
         'description': 'xid=CLP name=Claim Payment Information',
         'position': 100,
         'type': 'object',
         'properties': {'xid': {'literal': 'CLP'},
                        'clp01': {'$ref': '#/$elements/L2100_CLP01'},
                        'clp02': {'$ref': '#/$elements/L2100_CLP02'},
                        'clp03': {'$ref': '#/$elements/L2100_CLP03'},
                        'clp04': {'$ref': '#/$elements/L2100_CLP04'},
                        'clp05': {'$ref': '#/$elements/L2100_CLP05'},
                        'clp06': {'$ref': '#/$elements/L2100_CLP06'},
                        'clp07': {'$ref': '#/$elements/L2100_CLP07'},
                        'clp08': {'$ref': '#/$elements/L2100_CLP08'},
                        'clp09': {'$ref': '#/$elements/L2100_CLP09'},
                        'clp11': {'$ref': '#/$elements/L2100_CLP11'},
                        'clp12': {'$ref': '#/$elements/L2100_CLP12'},
                        'clp13': {'$ref': '#/$elements/L2100_CLP13'}},
         'required': ['clp01', 'clp02', 'clp03', 'clp04', 'clp06', 'clp07']}
        segment_name = 'CLP'
    clp01: L2100_CLP01
    clp02: L2100_CLP02
    clp03: L2100_CLP03
    clp04: L2100_CLP04
    clp05: L2100_CLP05 | None
    clp06: L2100_CLP06
    clp07: L2100_CLP07
    clp08: L2100_CLP08 | None
    clp09: L2100_CLP09 | None
    clp11: L2100_CLP11 | None
    clp12: L2100_CLP12 | None
    clp13: L2100_CLP13 | None


class L2100_CAS01(Element):
    """Claim Adjustment Group Code"""
    class Schema:
        json = {'title': 'Claim Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2100_CAS02(Element):
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


class L2100_CAS03(Element):
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


class L2100_CAS04(Element):
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


class L2100_CAS05(Element):
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


class L2100_CAS06(Element):
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


class L2100_CAS07(Element):
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


class L2100_CAS08(Element):
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


class L2100_CAS09(Element):
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


class L2100_CAS10(Element):
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


class L2100_CAS11(Element):
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


class L2100_CAS12(Element):
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


class L2100_CAS13(Element):
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


class L2100_CAS14(Element):
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


class L2100_CAS15(Element):
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


class L2100_CAS16(Element):
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


class L2100_CAS17(Element):
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


class L2100_CAS18(Element):
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


class L2100_CAS19(Element):
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


class L2100_CAS(Segment):
    """Claim Adjustment"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Adjustment',
                   'usage': 'S',
                   'description': 'xid=CAS name=Claim Adjustment',
                   'position': 200,
                   'syntax': ['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008',
                              'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614',
                              'L171819', 'C1817', 'C1917'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'CAS'},
                                  'cas01': {'$ref': '#/$elements/L2100_CAS01'},
                                  'cas02': {'$ref': '#/$elements/L2100_CAS02'},
                                  'cas03': {'$ref': '#/$elements/L2100_CAS03'},
                                  'cas04': {'$ref': '#/$elements/L2100_CAS04'},
                                  'cas05': {'$ref': '#/$elements/L2100_CAS05'},
                                  'cas06': {'$ref': '#/$elements/L2100_CAS06'},
                                  'cas07': {'$ref': '#/$elements/L2100_CAS07'},
                                  'cas08': {'$ref': '#/$elements/L2100_CAS08'},
                                  'cas09': {'$ref': '#/$elements/L2100_CAS09'},
                                  'cas10': {'$ref': '#/$elements/L2100_CAS10'},
                                  'cas11': {'$ref': '#/$elements/L2100_CAS11'},
                                  'cas12': {'$ref': '#/$elements/L2100_CAS12'},
                                  'cas13': {'$ref': '#/$elements/L2100_CAS13'},
                                  'cas14': {'$ref': '#/$elements/L2100_CAS14'},
                                  'cas15': {'$ref': '#/$elements/L2100_CAS15'},
                                  'cas16': {'$ref': '#/$elements/L2100_CAS16'},
                                  'cas17': {'$ref': '#/$elements/L2100_CAS17'},
                                  'cas18': {'$ref': '#/$elements/L2100_CAS18'},
                                  'cas19': {'$ref': '#/$elements/L2100_CAS19'}},
                   'required': ['cas01', 'cas02', 'cas03']},
         'maxItems': 99}
        segment_name = 'CAS'
    cas01: L2100_CAS01
    cas02: L2100_CAS02
    cas03: L2100_CAS03
    cas04: L2100_CAS04 | None
    cas05: L2100_CAS05 | None
    cas06: L2100_CAS06 | None
    cas07: L2100_CAS07 | None
    cas08: L2100_CAS08 | None
    cas09: L2100_CAS09 | None
    cas10: L2100_CAS10 | None
    cas11: L2100_CAS11 | None
    cas12: L2100_CAS12 | None
    cas13: L2100_CAS13 | None
    cas14: L2100_CAS14 | None
    cas15: L2100_CAS15 | None
    cas16: L2100_CAS16 | None
    cas17: L2100_CAS17 | None
    cas18: L2100_CAS18 | None
    cas19: L2100_CAS19 | None


class L2100_NM101(Element):
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


class L2100_NM102(Element):
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


class L2100_NM103(Element):
    """Patient Last Name"""
    class Schema:
        json = {'title': 'Patient Last Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100_NM104(Element):
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


class L2100_NM105(Element):
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


class L2100_NM106(Element):
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


class L2100_NM107(Element):
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


class L2100_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['34', 'HN', 'II', 'MI', 'MR']}]}}
        datatype = common.D_66
        codes = ['34', 'HN', 'II', 'MI', 'MR']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
    """Patient Identifier"""
    class Schema:
        json = {'title': 'Patient Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100_NM110(Element):
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


class L2100_NM111(Element):
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


class L2100_NM112(Element):
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


class L2100_NM1(Segment):
    """Patient Name"""
    class Schema:
        json = {'title': 'Patient Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Patient Name',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108 | None
    nm109: L2100_NM109 | None


class L2100_NM101(Element):
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


class L2100_NM102(Element):
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


class L2100_NM103(Element):
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


class L2100_NM104(Element):
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


class L2100_NM105(Element):
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


class L2100_NM106(Element):
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


class L2100_NM107(Element):
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


class L2100_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'II', 'MI']}]}}
        datatype = common.D_66
        codes = ['FI', 'II', 'MI']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
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


class L2100_NM110(Element):
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


class L2100_NM111(Element):
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


class L2100_NM112(Element):
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


class L2100_NM1(Segment):
    """Insured Name"""
    class Schema:
        json = {'title': 'Insured Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Insured Name',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108
    nm109: L2100_NM109


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['74']}]}}
        datatype = common.D_98
        codes = ['74']
        min_len = 2
        max_len = 3


class L2100_NM102(Element):
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


class L2100_NM103(Element):
    """Corrected Patient or Insured Last Name"""
    class Schema:
        json = {'title': 'Corrected Patient or Insured Last Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100_NM104(Element):
    """Corrected Patient or Insured First Name"""
    class Schema:
        json = {'title': 'Corrected Patient or Insured First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100_NM105(Element):
    """Corrected Patient or Insured Middle Name"""
    class Schema:
        json = {'title': 'Corrected Patient or Insured Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100_NM106(Element):
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


class L2100_NM107(Element):
    """Corrected Patient or Insured Name Suffix"""
    class Schema:
        json = {'title': 'Corrected Patient or Insured Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['C']}]}}
        datatype = common.D_66
        codes = ['C']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
    """Corrected Insured Identification Indicator"""
    class Schema:
        json = {'title': 'Corrected Insured Identification Indicator',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100_NM110(Element):
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


class L2100_NM111(Element):
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


class L2100_NM112(Element):
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


class L2100_NM1(Segment):
    """Corrected Patient/Insured Name"""
    class Schema:
        json = {'title': 'Corrected Patient/Insured Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Corrected Patient/Insured Name',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108 | None
    nm109: L2100_NM109 | None


class L2100_NM101(Element):
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


class L2100_NM102(Element):
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


class L2100_NM103(Element):
    """Rendering Provider Last or Organization Name"""
    class Schema:
        json = {'title': 'Rendering Provider Last or Organization Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100_NM104(Element):
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


class L2100_NM105(Element):
    """Rendering Provider Middle Name or Initial"""
    class Schema:
        json = {'title': 'Rendering Provider Middle Name or Initial',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100_NM106(Element):
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


class L2100_NM107(Element):
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


class L2100_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['BD', 'BS', 'FI', 'MC', 'PC', 'SL', 'UP',
                                      'XX']}]}}
        datatype = common.D_66
        codes = ['BD', 'BS', 'FI', 'MC', 'PC', 'SL', 'UP', 'XX']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
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


class L2100_NM110(Element):
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


class L2100_NM111(Element):
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


class L2100_NM112(Element):
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


class L2100_NM1(Segment):
    """Service Provider Name"""
    class Schema:
        json = {'title': 'Service Provider Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Service Provider Name',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108
    nm109: L2100_NM109


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['TT']}]}}
        datatype = common.D_98
        codes = ['TT']
        min_len = 2
        max_len = 3


class L2100_NM102(Element):
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


class L2100_NM103(Element):
    """Coordination of Benefits Carrier Name"""
    class Schema:
        json = {'title': 'Coordination of Benefits Carrier Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100_NM104(Element):
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


class L2100_NM105(Element):
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


class L2100_NM106(Element):
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


class L2100_NM107(Element):
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


class L2100_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['AD', 'FI', 'NI', 'PI', 'PP', 'XV']}]}}
        datatype = common.D_66
        codes = ['AD', 'FI', 'NI', 'PI', 'PP', 'XV']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
    """Coordination of Benefits Carrier Identifier"""
    class Schema:
        json = {'title': 'Coordination of Benefits Carrier Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100_NM110(Element):
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


class L2100_NM111(Element):
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


class L2100_NM112(Element):
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


class L2100_NM1(Segment):
    """Crossover Carrier Name"""
    class Schema:
        json = {'title': 'Crossover Carrier Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Crossover Carrier Name',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103
    nm108: L2100_NM108
    nm109: L2100_NM109


class L2100_NM101(Element):
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


class L2100_NM102(Element):
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


class L2100_NM103(Element):
    """Corrected Priority Payer Name"""
    class Schema:
        json = {'title': 'Corrected Priority Payer Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100_NM104(Element):
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


class L2100_NM105(Element):
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


class L2100_NM106(Element):
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


class L2100_NM107(Element):
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


class L2100_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'R',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'},
                            {'enum': ['AD', 'FI', 'NI', 'PI', 'PP', 'XV']}]}}
        datatype = common.D_66
        codes = ['AD', 'FI', 'NI', 'PI', 'PP', 'XV']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
    """Corrected Priority Payer Identification Number"""
    class Schema:
        json = {'title': 'Corrected Priority Payer Identification Number',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100_NM110(Element):
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


class L2100_NM111(Element):
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


class L2100_NM112(Element):
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


class L2100_NM1(Segment):
    """Corrected Priority Payer Name"""
    class Schema:
        json = {'title': 'Corrected Priority Payer Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Corrected Priority Payer Name',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103
    nm108: L2100_NM108
    nm109: L2100_NM109


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['GB']}]}}
        datatype = common.D_98
        codes = ['GB']
        min_len = 2
        max_len = 3


class L2100_NM102(Element):
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


class L2100_NM103(Element):
    """Other Subscriber Last Name"""
    class Schema:
        json = {'title': 'Other Subscriber Last Name',
         'usage': 'S',
         'description': 'xid=NM103 data_ele=1035',
         'sequence': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100_NM104(Element):
    """Other Subscriber First Name"""
    class Schema:
        json = {'title': 'Other Subscriber First Name',
         'usage': 'S',
         'description': 'xid=NM104 data_ele=1036',
         'sequence': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100_NM105(Element):
    """Other Subscriber Middle Name or Initial"""
    class Schema:
        json = {'title': 'Other Subscriber Middle Name or Initial',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'sequence': 5,
         'type': {'$ref': '#/$common/1037'}}
        datatype = common.D_1037
        min_len = 1
        max_len = 25


class L2100_NM106(Element):
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


class L2100_NM107(Element):
    """Other Subscriber Name Suffix"""
    class Schema:
        json = {'title': 'Other Subscriber Name Suffix',
         'usage': 'S',
         'description': 'xid=NM107 data_ele=1039',
         'sequence': 7,
         'type': {'$ref': '#/$common/1039'}}
        datatype = common.D_1039
        min_len = 1
        max_len = 10


class L2100_NM108(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=NM108 data_ele=66',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'II', 'MI']}]}}
        datatype = common.D_66
        codes = ['FI', 'II', 'MI']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
    """Other Subscriber Identifier"""
    class Schema:
        json = {'title': 'Other Subscriber Identifier',
         'usage': 'S',
         'description': 'xid=NM109 data_ele=67',
         'sequence': 9,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L2100_NM110(Element):
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


class L2100_NM111(Element):
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


class L2100_NM112(Element):
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


class L2100_NM1(Segment):
    """Other Subscriber Name"""
    class Schema:
        json = {'title': 'Other Subscriber Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Other Subscriber Name',
         'position': 300,
         'syntax': ['P0809', 'C1110', 'C1203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108 | None
    nm109: L2100_NM109 | None


class L2100_MIA01(Element):
    """Covered Days or Visits Count"""
    class Schema:
        json = {'title': 'Covered Days or Visits Count',
         'usage': 'R',
         'description': 'xid=MIA01 data_ele=380',
         'sequence': 1,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_MIA02(Element):
    """PPS Operating Outlier Amount"""
    class Schema:
        json = {'title': 'PPS Operating Outlier Amount',
         'usage': 'S',
         'description': 'xid=MIA02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA03(Element):
    """Lifetime Psychiatric Days Count"""
    class Schema:
        json = {'title': 'Lifetime Psychiatric Days Count',
         'usage': 'S',
         'description': 'xid=MIA03 data_ele=380',
         'sequence': 3,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_MIA04(Element):
    """Claim DRG Amount"""
    class Schema:
        json = {'title': 'Claim DRG Amount',
         'usage': 'S',
         'description': 'xid=MIA04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA05(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MIA05 data_ele=127',
         'sequence': 5,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA06(Element):
    """Claim Disproportionate Share Amount"""
    class Schema:
        json = {'title': 'Claim Disproportionate Share Amount',
         'usage': 'S',
         'description': 'xid=MIA06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA07(Element):
    """Claim MSP Pass-through Amount"""
    class Schema:
        json = {'title': 'Claim MSP Pass-through Amount',
         'usage': 'S',
         'description': 'xid=MIA07 data_ele=782',
         'sequence': 7,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA08(Element):
    """Claim PPS Capital Amount"""
    class Schema:
        json = {'title': 'Claim PPS Capital Amount',
         'usage': 'S',
         'description': 'xid=MIA08 data_ele=782',
         'sequence': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA09(Element):
    """PPS-Capital FSP DRG Amount"""
    class Schema:
        json = {'title': 'PPS-Capital FSP DRG Amount',
         'usage': 'S',
         'description': 'xid=MIA09 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA10(Element):
    """PPS-Capital HSP DRG Amount"""
    class Schema:
        json = {'title': 'PPS-Capital HSP DRG Amount',
         'usage': 'S',
         'description': 'xid=MIA10 data_ele=782',
         'sequence': 10,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA11(Element):
    """PPS-Capital DSH DRG Amount"""
    class Schema:
        json = {'title': 'PPS-Capital DSH DRG Amount',
         'usage': 'S',
         'description': 'xid=MIA11 data_ele=782',
         'sequence': 11,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA12(Element):
    """Old Capital Amount"""
    class Schema:
        json = {'title': 'Old Capital Amount',
         'usage': 'S',
         'description': 'xid=MIA12 data_ele=782',
         'sequence': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA13(Element):
    """PPS-Capital IME amount"""
    class Schema:
        json = {'title': 'PPS-Capital IME amount',
         'usage': 'S',
         'description': 'xid=MIA13 data_ele=782',
         'sequence': 13,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA14(Element):
    """PPS-Operating Hospital Specific DRG Amount"""
    class Schema:
        json = {'title': 'PPS-Operating Hospital Specific DRG Amount',
         'usage': 'S',
         'description': 'xid=MIA14 data_ele=782',
         'sequence': 14,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA15(Element):
    """Cost Report Day Count"""
    class Schema:
        json = {'title': 'Cost Report Day Count',
         'usage': 'S',
         'description': 'xid=MIA15 data_ele=380',
         'sequence': 15,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_MIA16(Element):
    """PPS-Operating Federal Specific DRG Amount"""
    class Schema:
        json = {'title': 'PPS-Operating Federal Specific DRG Amount',
         'usage': 'S',
         'description': 'xid=MIA16 data_ele=782',
         'sequence': 16,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA17(Element):
    """Claim PPS Capital Outlier Amount"""
    class Schema:
        json = {'title': 'Claim PPS Capital Outlier Amount',
         'usage': 'S',
         'description': 'xid=MIA17 data_ele=782',
         'sequence': 17,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA18(Element):
    """Claim Indirect Teaching Amount"""
    class Schema:
        json = {'title': 'Claim Indirect Teaching Amount',
         'usage': 'S',
         'description': 'xid=MIA18 data_ele=782',
         'sequence': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA19(Element):
    """Nonpayable Professional Component Amount"""
    class Schema:
        json = {'title': 'Nonpayable Professional Component Amount',
         'usage': 'S',
         'description': 'xid=MIA19 data_ele=782',
         'sequence': 19,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA20(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MIA20 data_ele=127',
         'sequence': 20,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA21(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MIA21 data_ele=127',
         'sequence': 21,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA22(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MIA22 data_ele=127',
         'sequence': 22,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA23(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MIA23 data_ele=127',
         'sequence': 23,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA24(Element):
    """PPS-Capital Exception Amount"""
    class Schema:
        json = {'title': 'PPS-Capital Exception Amount',
         'usage': 'S',
         'description': 'xid=MIA24 data_ele=782',
         'sequence': 24,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA(Segment):
    """Inpatient Adjudication Information"""
    class Schema:
        json = {'title': 'Inpatient Adjudication Information',
         'usage': 'S',
         'description': 'xid=MIA name=Inpatient Adjudication Information',
         'position': 330,
         'type': 'object',
         'properties': {'xid': {'literal': 'MIA'},
                        'mia01': {'$ref': '#/$elements/L2100_MIA01'},
                        'mia02': {'$ref': '#/$elements/L2100_MIA02'},
                        'mia03': {'$ref': '#/$elements/L2100_MIA03'},
                        'mia04': {'$ref': '#/$elements/L2100_MIA04'},
                        'mia05': {'$ref': '#/$elements/L2100_MIA05'},
                        'mia06': {'$ref': '#/$elements/L2100_MIA06'},
                        'mia07': {'$ref': '#/$elements/L2100_MIA07'},
                        'mia08': {'$ref': '#/$elements/L2100_MIA08'},
                        'mia09': {'$ref': '#/$elements/L2100_MIA09'},
                        'mia10': {'$ref': '#/$elements/L2100_MIA10'},
                        'mia11': {'$ref': '#/$elements/L2100_MIA11'},
                        'mia12': {'$ref': '#/$elements/L2100_MIA12'},
                        'mia13': {'$ref': '#/$elements/L2100_MIA13'},
                        'mia14': {'$ref': '#/$elements/L2100_MIA14'},
                        'mia15': {'$ref': '#/$elements/L2100_MIA15'},
                        'mia16': {'$ref': '#/$elements/L2100_MIA16'},
                        'mia17': {'$ref': '#/$elements/L2100_MIA17'},
                        'mia18': {'$ref': '#/$elements/L2100_MIA18'},
                        'mia19': {'$ref': '#/$elements/L2100_MIA19'},
                        'mia20': {'$ref': '#/$elements/L2100_MIA20'},
                        'mia21': {'$ref': '#/$elements/L2100_MIA21'},
                        'mia22': {'$ref': '#/$elements/L2100_MIA22'},
                        'mia23': {'$ref': '#/$elements/L2100_MIA23'},
                        'mia24': {'$ref': '#/$elements/L2100_MIA24'}},
         'required': ['mia01']}
        segment_name = 'MIA'
    mia01: L2100_MIA01
    mia02: L2100_MIA02 | None
    mia03: L2100_MIA03 | None
    mia04: L2100_MIA04 | None
    mia05: L2100_MIA05 | None
    mia06: L2100_MIA06 | None
    mia07: L2100_MIA07 | None
    mia08: L2100_MIA08 | None
    mia09: L2100_MIA09 | None
    mia10: L2100_MIA10 | None
    mia11: L2100_MIA11 | None
    mia12: L2100_MIA12 | None
    mia13: L2100_MIA13 | None
    mia14: L2100_MIA14 | None
    mia15: L2100_MIA15 | None
    mia16: L2100_MIA16 | None
    mia17: L2100_MIA17 | None
    mia18: L2100_MIA18 | None
    mia19: L2100_MIA19 | None
    mia20: L2100_MIA20 | None
    mia21: L2100_MIA21 | None
    mia22: L2100_MIA22 | None
    mia23: L2100_MIA23 | None
    mia24: L2100_MIA24 | None


class L2100_MOA01(Element):
    """Reimbursement Rate"""
    class Schema:
        json = {'title': 'Reimbursement Rate',
         'usage': 'S',
         'description': 'xid=MOA01 data_ele=954',
         'sequence': 1,
         'type': {'$ref': '#/$common/954'}}
        datatype = common.D_954
        min_len = 1
        max_len = 10


class L2100_MOA02(Element):
    """Claim HCPCS Payable Amount"""
    class Schema:
        json = {'title': 'Claim HCPCS Payable Amount',
         'usage': 'S',
         'description': 'xid=MOA02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MOA03(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MOA03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA04(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MOA04 data_ele=127',
         'sequence': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA05(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MOA05 data_ele=127',
         'sequence': 5,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA06(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MOA06 data_ele=127',
         'sequence': 6,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA07(Element):
    """Claim Payment Remark Code"""
    class Schema:
        json = {'title': 'Claim Payment Remark Code',
         'usage': 'S',
         'description': 'xid=MOA07 data_ele=127',
         'sequence': 7,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA08(Element):
    """Claim ESRD Payment Amount"""
    class Schema:
        json = {'title': 'Claim ESRD Payment Amount',
         'usage': 'S',
         'description': 'xid=MOA08 data_ele=782',
         'sequence': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MOA09(Element):
    """Nonpayable Professional Component Amount"""
    class Schema:
        json = {'title': 'Nonpayable Professional Component Amount',
         'usage': 'S',
         'description': 'xid=MOA09 data_ele=782',
         'sequence': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MOA(Segment):
    """Outpatient Adjudication Information"""
    class Schema:
        json = {'title': 'Outpatient Adjudication Information',
         'usage': 'S',
         'description': 'xid=MOA name=Outpatient Adjudication Information',
         'position': 350,
         'type': 'object',
         'properties': {'xid': {'literal': 'MOA'},
                        'moa01': {'$ref': '#/$elements/L2100_MOA01'},
                        'moa02': {'$ref': '#/$elements/L2100_MOA02'},
                        'moa03': {'$ref': '#/$elements/L2100_MOA03'},
                        'moa04': {'$ref': '#/$elements/L2100_MOA04'},
                        'moa05': {'$ref': '#/$elements/L2100_MOA05'},
                        'moa06': {'$ref': '#/$elements/L2100_MOA06'},
                        'moa07': {'$ref': '#/$elements/L2100_MOA07'},
                        'moa08': {'$ref': '#/$elements/L2100_MOA08'},
                        'moa09': {'$ref': '#/$elements/L2100_MOA09'}}}
        segment_name = 'MOA'
    moa01: L2100_MOA01 | None
    moa02: L2100_MOA02 | None
    moa03: L2100_MOA03 | None
    moa04: L2100_MOA04 | None
    moa05: L2100_MOA05 | None
    moa06: L2100_MOA06 | None
    moa07: L2100_MOA07 | None
    moa08: L2100_MOA08 | None
    moa09: L2100_MOA09 | None


class L2100_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1L', '1W', '28', '6P', '9A', '9C', 'BB', 'CE',
                                      'EA', 'F8', 'G1', 'G3', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1L', '1W', '28', '6P', '9A', '9C', 'BB', 'CE', 'EA', 'F8', 'G1', 'G3', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2100_REF02(Element):
    """Other Claim Related Identifier"""
    class Schema:
        json = {'title': 'Other Claim Related Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2100_REF03(Element):
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


class L2100_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100_REF(Segment):
    """Other Claim Related Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Claim Related Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Claim Related Identification',
                   'position': 400,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2100_REF01
    ref02: L2100_REF02


class L2100_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J',
                                      'D3', 'G2', 'LU']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'D3', 'G2', 'LU']
        min_len = 2
        max_len = 3


class L2100_REF02(Element):
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


class L2100_REF03(Element):
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


class L2100_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100_REF(Segment):
    """Rendering Provider Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Identification',
                   'position': 400,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 10}
        segment_name = 'REF'
    ref01: L2100_REF01
    ref02: L2100_REF02


class L2100_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['232', '233']}]}}
        datatype = common.D_374
        codes = ['232', '233']
        min_len = 3
        max_len = 3


class L2100_DTM02(Element):
    """Claim Date"""
    class Schema:
        json = {'title': 'Claim Date',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2100_DTM03(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2100_DTM04(Element):
    """Time Code"""
    class Schema:
        json = {'title': 'Time Code',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L2100_DTM05(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2100_DTM06(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100_DTM(Segment):
    """Statement From or To Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Statement From or To Date',
                   'usage': 'S',
                   'description': 'xid=DTM name=Statement From or To Date',
                   'position': 500,
                   'syntax': ['R020305', 'C0403', 'P0506'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTM'},
                                  'dtm01': {'$ref': '#/$elements/L2100_DTM01'},
                                  'dtm02': {'$ref': '#/$elements/L2100_DTM02'}},
                   'required': ['dtm01', 'dtm02']},
         'maxItems': 2}
        segment_name = 'DTM'
    dtm01: L2100_DTM01
    dtm02: L2100_DTM02


class L2100_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['036']}]}}
        datatype = common.D_374
        codes = ['036']
        min_len = 3
        max_len = 3


class L2100_DTM02(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2100_DTM03(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2100_DTM04(Element):
    """Time Code"""
    class Schema:
        json = {'title': 'Time Code',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L2100_DTM05(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2100_DTM06(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100_DTM(Segment):
    """Coverage Expiration Date"""
    class Schema:
        json = {'title': 'Coverage Expiration Date',
         'usage': 'S',
         'description': 'xid=DTM name=Coverage Expiration Date',
         'position': 500,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/L2100_DTM01'},
                        'dtm02': {'$ref': '#/$elements/L2100_DTM02'}},
         'required': ['dtm01', 'dtm02']}
        segment_name = 'DTM'
    dtm01: L2100_DTM01
    dtm02: L2100_DTM02


class L2100_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['050']}]}}
        datatype = common.D_374
        codes = ['050']
        min_len = 3
        max_len = 3


class L2100_DTM02(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2100_DTM03(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2100_DTM04(Element):
    """Time Code"""
    class Schema:
        json = {'title': 'Time Code',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L2100_DTM05(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2100_DTM06(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100_DTM(Segment):
    """Claim Received Date"""
    class Schema:
        json = {'title': 'Claim Received Date',
         'usage': 'S',
         'description': 'xid=DTM name=Claim Received Date',
         'position': 500,
         'syntax': ['R020305', 'C0403', 'P0506'],
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/L2100_DTM01'},
                        'dtm02': {'$ref': '#/$elements/L2100_DTM02'}},
         'required': ['dtm01', 'dtm02']}
        segment_name = 'DTM'
    dtm01: L2100_DTM01
    dtm02: L2100_DTM02


class L2100_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/366'}, {'enum': ['CX']}]}}
        datatype = common.D_366
        codes = ['CX']
        min_len = 2
        max_len = 2


class L2100_PER02(Element):
    """Claim Contact Name"""
    class Schema:
        json = {'title': 'Claim Contact Name',
         'usage': 'S',
         'description': 'xid=PER02 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'R',
         'description': 'xid=PER03 data_ele=365',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100_PER04(Element):
    """Claim Contact Communications Number"""
    class Schema:
        json = {'title': 'Claim Contact Communications Number',
         'usage': 'R',
         'description': 'xid=PER04 data_ele=364',
         'sequence': 4,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100_PER05(Element):
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


class L2100_PER06(Element):
    """Claim Contact Communications Number"""
    class Schema:
        json = {'title': 'Claim Contact Communications Number',
         'usage': 'S',
         'description': 'xid=PER06 data_ele=364',
         'sequence': 6,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100_PER07(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER07 data_ele=365',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EX']}]}}
        datatype = common.D_365
        codes = ['EX']
        min_len = 2
        max_len = 2


class L2100_PER08(Element):
    """Communication Number Extension"""
    class Schema:
        json = {'title': 'Communication Number Extension',
         'usage': 'S',
         'description': 'xid=PER08 data_ele=364',
         'sequence': 8,
         'type': {'$ref': '#/$common/364'}}
        datatype = common.D_364
        min_len = 1
        max_len = 256


class L2100_PER09(Element):
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


class L2100_PER(Segment):
    """Claim Contact Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Contact Information',
                   'usage': 'S',
                   'description': 'xid=PER name=Claim Contact Information',
                   'position': 600,
                   'syntax': ['P0304', 'P0506', 'P0708'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2100_PER01'},
                                  'per02': {'$ref': '#/$elements/L2100_PER02'},
                                  'per03': {'$ref': '#/$elements/L2100_PER03'},
                                  'per04': {'$ref': '#/$elements/L2100_PER04'},
                                  'per05': {'$ref': '#/$elements/L2100_PER05'},
                                  'per06': {'$ref': '#/$elements/L2100_PER06'},
                                  'per07': {'$ref': '#/$elements/L2100_PER07'},
                                  'per08': {'$ref': '#/$elements/L2100_PER08'}},
                   'required': ['per01', 'per03', 'per04']},
         'maxItems': 2}
        segment_name = 'PER'
    per01: L2100_PER01
    per02: L2100_PER02 | None
    per03: L2100_PER03
    per04: L2100_PER04
    per05: L2100_PER05 | None
    per06: L2100_PER06 | None
    per07: L2100_PER07 | None
    per08: L2100_PER08 | None


class L2100_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['AU', 'D8', 'DY', 'F5', 'I', 'NL', 'T', 'T2',
                                      'ZK', 'ZL', 'ZM', 'ZN', 'ZO']}]}}
        datatype = common.D_522
        codes = ['AU', 'D8', 'DY', 'F5', 'I', 'NL', 'T', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']
        min_len = 1
        max_len = 3


class L2100_AMT02(Element):
    """Claim Supplemental Information Amount"""
    class Schema:
        json = {'title': 'Claim Supplemental Information Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_AMT03(Element):
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


class L2100_AMT(Segment):
    """Claim Supplemental Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Supplemental Information',
                   'usage': 'S',
                   'description': 'xid=AMT name=Claim Supplemental Information',
                   'position': 620,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2100_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2100_AMT02'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 13}
        segment_name = 'AMT'
    amt01: L2100_AMT01
    amt02: L2100_AMT02


class L2100_QTY01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=QTY01 data_ele=673',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['CA', 'CD', 'LA', 'LE', 'NE', 'NR', 'OU', 'PS',
                                      'VS', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']}]}}
        datatype = common.D_673
        codes = ['CA', 'CD', 'LA', 'LE', 'NE', 'NR', 'OU', 'PS', 'VS', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']
        min_len = 2
        max_len = 2


class L2100_QTY02(Element):
    """Claim Supplemental Information Quantity"""
    class Schema:
        json = {'title': 'Claim Supplemental Information Quantity',
         'usage': 'R',
         'description': 'xid=QTY02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_QTY03(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=QTY03 name=Composite Unit of Measure refdes= '
                        'data_ele=C001',
         'sequence': 3,
         'syntax': []}


class L2100_QTY04(Element):
    """Free-form Information"""
    class Schema:
        json = {'title': 'Free-form Information',
         'usage': 'N',
         'description': 'xid=QTY04 data_ele=61',
         'sequence': 4,
         'type': {'$ref': '#/$common/61'}}
        datatype = common.D_61
        min_len = 1
        max_len = 30


class L2100_QTY(Segment):
    """Claim Supplemental Information Quantity"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Supplemental Information Quantity',
                   'usage': 'S',
                   'description': 'xid=QTY name=Claim Supplemental Information '
                                  'Quantity',
                   'position': 640,
                   'syntax': ['E0204', 'R0204'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'QTY'},
                                  'qty01': {'$ref': '#/$elements/L2100_QTY01'},
                                  'qty02': {'$ref': '#/$elements/L2100_QTY02'}},
                   'required': ['qty01', 'qty02']},
         'maxItems': 14}
        segment_name = 'QTY'
    qty01: L2100_QTY01
    qty02: L2100_QTY02


class L2110_SVC01_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SVC01-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'N6', 'NU',
                                      'UI', 'WK']}]}}
        datatype = common.D_235
        codes = ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'N6', 'NU', 'UI', 'WK']
        min_len = 2
        max_len = 2


class L2110_SVC01_02(Element):
    """Adjudicated Procedure Code"""
    class Schema:
        json = {'title': 'Adjudicated Procedure Code',
         'usage': 'R',
         'description': 'xid=SVC01-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110_SVC01_03(Element):
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


class L2110_SVC01_04(Element):
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


class L2110_SVC01_05(Element):
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


class L2110_SVC01_06(Element):
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


class L2110_SVC01_07(Element):
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


class L2110_SVC01_08(Element):
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


class L2110_SVC01(Composite):
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
                                                                  'N6', 'NU', 'UI',
                                                                  'WK']}]}},
                        'svc01_02': {'title': 'Adjudicated Procedure Code',
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
    svc01_01: L2110_SVC01_01
    svc01_02: L2110_SVC01_02
    svc01_03: L2110_SVC01_03 | None
    svc01_04: L2110_SVC01_04 | None
    svc01_05: L2110_SVC01_05 | None
    svc01_06: L2110_SVC01_06 | None


class L2110_SVC02(Element):
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


class L2110_SVC03(Element):
    """Line Item Provider Payment Amount"""
    class Schema:
        json = {'title': 'Line Item Provider Payment Amount',
         'usage': 'R',
         'description': 'xid=SVC03 data_ele=782',
         'sequence': 3,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2110_SVC04(Element):
    """National Uniform Billing Committee Revenue Code"""
    class Schema:
        json = {'title': 'National Uniform Billing Committee Revenue Code',
         'usage': 'S',
         'description': 'xid=SVC04 data_ele=234',
         'sequence': 4,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110_SVC05(Element):
    """Units of Service Paid Count"""
    class Schema:
        json = {'title': 'Units of Service Paid Count',
         'usage': 'S',
         'description': 'xid=SVC05 data_ele=380',
         'sequence': 5,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110_SVC06_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SVC06-01 data_ele=235',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU',
                                      'WK']}]}}
        datatype = common.D_235
        codes = ['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU', 'WK']
        min_len = 2
        max_len = 2


class L2110_SVC06_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SVC06-02 data_ele=234',
         'sequence': 2,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110_SVC06_03(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC06-03 data_ele=1339',
         'sequence': 3,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110_SVC06_04(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC06-04 data_ele=1339',
         'sequence': 4,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110_SVC06_05(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC06-05 data_ele=1339',
         'sequence': 5,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110_SVC06_06(Element):
    """Procedure Modifier"""
    class Schema:
        json = {'title': 'Procedure Modifier',
         'usage': 'S',
         'description': 'xid=SVC06-06 data_ele=1339',
         'sequence': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110_SVC06_07(Element):
    """Procedure Code Description"""
    class Schema:
        json = {'title': 'Procedure Code Description',
         'usage': 'S',
         'description': 'xid=SVC06-07 data_ele=352',
         'sequence': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110_SVC06_08(Element):
    """Product/Service ID"""
    class Schema:
        json = {'title': 'Product/Service ID',
         'usage': 'N',
         'description': 'xid=SVC06-08 data_ele=234',
         'sequence': 8,
         'type': {'$ref': '#/$common/234'}}
        datatype = common.D_234
        min_len = 1
        max_len = 48


class L2110_SVC06(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'S',
         'description': 'xid=SVC06 name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 6,
         'syntax': [],
         'type': 'object',
         'properties': {'svc06_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SVC06-01 data_ele=235',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD', 'ER', 'HC',
                                                                  'HP', 'IV', 'N4',
                                                                  'NU', 'WK']}]}},
                        'svc06_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SVC06-02 data_ele=234',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'svc06_03': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-03 data_ele=1339',
                                     'sequence': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_04': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-04 data_ele=1339',
                                     'sequence': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_05': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-05 data_ele=1339',
                                     'sequence': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_06': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-06 data_ele=1339',
                                     'sequence': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_07': {'title': 'Procedure Code Description',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-07 data_ele=352',
                                     'sequence': 7,
                                     'type': {'$ref': '#/$common/352'}},
                        'svc06_08': {'title': 'Product/Service ID',
                                     'usage': 'N',
                                     'description': 'xid=SVC06-08 data_ele=234',
                                     'sequence': 8,
                                     'type': {'$ref': '#/$common/234'}}},
         'required': ['svc06_01', 'svc06_02']}
    svc06_01: L2110_SVC06_01
    svc06_02: L2110_SVC06_02
    svc06_03: L2110_SVC06_03 | None
    svc06_04: L2110_SVC06_04 | None
    svc06_05: L2110_SVC06_05 | None
    svc06_06: L2110_SVC06_06 | None
    svc06_07: L2110_SVC06_07 | None


class L2110_SVC07(Element):
    """Original Units of Service Count"""
    class Schema:
        json = {'title': 'Original Units of Service Count',
         'usage': 'S',
         'description': 'xid=SVC07 data_ele=380',
         'sequence': 7,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110_SVC(Segment):
    """Service Payment Information"""
    class Schema:
        json = {'title': 'Service Payment Information',
         'usage': 'R',
         'description': 'xid=SVC name=Service Payment Information',
         'position': 700,
         'type': 'object',
         'properties': {'xid': {'literal': 'SVC'},
                        'svc01': {'$ref': '#/$elements/L2110_SVC01'},
                        'svc02': {'$ref': '#/$elements/L2110_SVC02'},
                        'svc03': {'$ref': '#/$elements/L2110_SVC03'},
                        'svc04': {'$ref': '#/$elements/L2110_SVC04'},
                        'svc05': {'$ref': '#/$elements/L2110_SVC05'},
                        'svc06': {'$ref': '#/$elements/L2110_SVC06'},
                        'svc07': {'$ref': '#/$elements/L2110_SVC07'}},
         'required': ['svc01', 'svc02', 'svc03']}
        segment_name = 'SVC'
    svc01: L2110_SVC01
    svc02: L2110_SVC02
    svc03: L2110_SVC03
    svc04: L2110_SVC04 | None
    svc05: L2110_SVC05 | None
    svc06: L2110_SVC06 | None
    svc07: L2110_SVC07 | None


class L2110_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['150', '151', '472']}]}}
        datatype = common.D_374
        codes = ['150', '151', '472']
        min_len = 3
        max_len = 3


class L2110_DTM02(Element):
    """Service Date"""
    class Schema:
        json = {'title': 'Service Date',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L2110_DTM03(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=DTM03 data_ele=337',
         'sequence': 3,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L2110_DTM04(Element):
    """Time Code"""
    class Schema:
        json = {'title': 'Time Code',
         'usage': 'N',
         'description': 'xid=DTM04 data_ele=623',
         'sequence': 4,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L2110_DTM05(Element):
    """Date Time Period Format Qualifier"""
    class Schema:
        json = {'title': 'Date Time Period Format Qualifier',
         'usage': 'N',
         'description': 'xid=DTM05 data_ele=1250',
         'sequence': 5,
         'type': {'$ref': '#/$common/1250'}}
        datatype = common.D_1250
        min_len = 2
        max_len = 3


class L2110_DTM06(Element):
    """Date Time Period"""
    class Schema:
        json = {'title': 'Date Time Period',
         'usage': 'N',
         'description': 'xid=DTM06 data_ele=1251',
         'sequence': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2110_DTM(Segment):
    """Service Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Date',
                   'usage': 'S',
                   'description': 'xid=DTM name=Service Date',
                   'position': 800,
                   'syntax': ['R020305', 'C0403', 'P0506'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTM'},
                                  'dtm01': {'$ref': '#/$elements/L2110_DTM01'},
                                  'dtm02': {'$ref': '#/$elements/L2110_DTM02'}},
                   'required': ['dtm01', 'dtm02']},
         'maxItems': 2}
        segment_name = 'DTM'
    dtm01: L2110_DTM01
    dtm02: L2110_DTM02


class L2110_CAS01(Element):
    """Claim Adjustment Group Code"""
    class Schema:
        json = {'title': 'Claim Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2110_CAS02(Element):
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


class L2110_CAS03(Element):
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


class L2110_CAS04(Element):
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


class L2110_CAS05(Element):
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


class L2110_CAS06(Element):
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


class L2110_CAS07(Element):
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


class L2110_CAS08(Element):
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


class L2110_CAS09(Element):
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


class L2110_CAS10(Element):
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


class L2110_CAS11(Element):
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


class L2110_CAS12(Element):
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


class L2110_CAS13(Element):
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


class L2110_CAS14(Element):
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


class L2110_CAS15(Element):
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


class L2110_CAS16(Element):
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


class L2110_CAS17(Element):
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


class L2110_CAS18(Element):
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


class L2110_CAS19(Element):
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


class L2110_CAS(Segment):
    """Service Adjustment"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Adjustment',
                   'usage': 'S',
                   'description': 'xid=CAS name=Service Adjustment',
                   'position': 900,
                   'syntax': ['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008',
                              'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614',
                              'L171819', 'C1817', 'C1917'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'CAS'},
                                  'cas01': {'$ref': '#/$elements/L2110_CAS01'},
                                  'cas02': {'$ref': '#/$elements/L2110_CAS02'},
                                  'cas03': {'$ref': '#/$elements/L2110_CAS03'},
                                  'cas04': {'$ref': '#/$elements/L2110_CAS04'},
                                  'cas05': {'$ref': '#/$elements/L2110_CAS05'},
                                  'cas06': {'$ref': '#/$elements/L2110_CAS06'},
                                  'cas07': {'$ref': '#/$elements/L2110_CAS07'},
                                  'cas08': {'$ref': '#/$elements/L2110_CAS08'},
                                  'cas09': {'$ref': '#/$elements/L2110_CAS09'},
                                  'cas10': {'$ref': '#/$elements/L2110_CAS10'},
                                  'cas11': {'$ref': '#/$elements/L2110_CAS11'},
                                  'cas12': {'$ref': '#/$elements/L2110_CAS12'},
                                  'cas13': {'$ref': '#/$elements/L2110_CAS13'},
                                  'cas14': {'$ref': '#/$elements/L2110_CAS14'},
                                  'cas15': {'$ref': '#/$elements/L2110_CAS15'},
                                  'cas16': {'$ref': '#/$elements/L2110_CAS16'},
                                  'cas17': {'$ref': '#/$elements/L2110_CAS17'},
                                  'cas18': {'$ref': '#/$elements/L2110_CAS18'},
                                  'cas19': {'$ref': '#/$elements/L2110_CAS19'}},
                   'required': ['cas01', 'cas02', 'cas03']},
         'maxItems': 99}
        segment_name = 'CAS'
    cas01: L2110_CAS01
    cas02: L2110_CAS02
    cas03: L2110_CAS03
    cas04: L2110_CAS04 | None
    cas05: L2110_CAS05 | None
    cas06: L2110_CAS06 | None
    cas07: L2110_CAS07 | None
    cas08: L2110_CAS08 | None
    cas09: L2110_CAS09 | None
    cas10: L2110_CAS10 | None
    cas11: L2110_CAS11 | None
    cas12: L2110_CAS12 | None
    cas13: L2110_CAS13 | None
    cas14: L2110_CAS14 | None
    cas15: L2110_CAS15 | None
    cas16: L2110_CAS16 | None
    cas17: L2110_CAS17 | None
    cas18: L2110_CAS18 | None
    cas19: L2110_CAS19 | None


class L2110_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1S', 'APC', 'BB', 'E9', 'G1', 'G3', 'LU',
                                      'RB']}]}}
        datatype = common.D_128
        codes = ['1S', 'APC', 'BB', 'E9', 'G1', 'G3', 'LU', 'RB']
        min_len = 2
        max_len = 3


class L2110_REF02(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2110_REF03(Element):
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


class L2110_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110_REF(Segment):
    """Service Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Service Identification',
                   'position': 1000,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2110_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2110_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 8}
        segment_name = 'REF'
    ref01: L2110_REF01
    ref02: L2110_REF02


class L2110_REF01(Element):
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


class L2110_REF02(Element):
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


class L2110_REF03(Element):
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


class L2110_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110_REF(Segment):
    """Line Item Control Number"""
    class Schema:
        json = {'title': 'Line Item Control Number',
         'usage': 'S',
         'description': 'xid=REF name=Line Item Control Number',
         'position': 1000,
         'syntax': ['R0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/L2110_REF01'},
                        'ref02': {'$ref': '#/$elements/L2110_REF02'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: L2110_REF01
    ref02: L2110_REF02


class L2110_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J',
                                      'D3', 'G2', 'HPI', 'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'D3', 'G2', 'HPI', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2110_REF02(Element):
    """Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2110_REF03(Element):
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


class L2110_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110_REF(Segment):
    """Rendering Provider Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Information',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Information',
                   'position': 1000,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2110_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2110_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 10}
        segment_name = 'REF'
    ref01: L2110_REF01
    ref02: L2110_REF02


class L2110_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['0K']}]}}
        datatype = common.D_128
        codes = ['0K']
        min_len = 2
        max_len = 3


class L2110_REF02(Element):
    """Healthcare Policy Identification"""
    class Schema:
        json = {'title': 'Healthcare Policy Identification',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2110_REF03(Element):
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


class L2110_REF04(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=REF04 name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110_REF(Segment):
    """HealthCare Policy Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'HealthCare Policy Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=HealthCare Policy Identification',
                   'position': 1000,
                   'syntax': ['R0203'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2110_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2110_REF02'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2110_REF01
    ref02: L2110_REF02


class L2110_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['B6', 'KH', 'T', 'T2', 'ZK', 'ZL', 'ZM', 'ZN',
                                      'ZO']}]}}
        datatype = common.D_522
        codes = ['B6', 'KH', 'T', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']
        min_len = 1
        max_len = 3


class L2110_AMT02(Element):
    """Service Supplemental Amount"""
    class Schema:
        json = {'title': 'Service Supplemental Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'sequence': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2110_AMT03(Element):
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


class L2110_AMT(Segment):
    """Service Supplemental Amount"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Supplemental Amount',
                   'usage': 'S',
                   'description': 'xid=AMT name=Service Supplemental Amount',
                   'position': 1100,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2110_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2110_AMT02'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 9}
        segment_name = 'AMT'
    amt01: L2110_AMT01
    amt02: L2110_AMT02


class L2110_QTY01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=QTY01 data_ele=673',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['ZK', 'ZL', 'ZM', 'ZN', 'ZO']}]}}
        datatype = common.D_673
        codes = ['ZK', 'ZL', 'ZM', 'ZN', 'ZO']
        min_len = 2
        max_len = 2


class L2110_QTY02(Element):
    """Service Supplemental Quantity Count"""
    class Schema:
        json = {'title': 'Service Supplemental Quantity Count',
         'usage': 'R',
         'description': 'xid=QTY02 data_ele=380',
         'sequence': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110_QTY03(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=QTY03 name=Composite Unit of Measure refdes= '
                        'data_ele=C001',
         'sequence': 3,
         'syntax': []}


class L2110_QTY04(Element):
    """Free-form Information"""
    class Schema:
        json = {'title': 'Free-form Information',
         'usage': 'N',
         'description': 'xid=QTY04 data_ele=61',
         'sequence': 4,
         'type': {'$ref': '#/$common/61'}}
        datatype = common.D_61
        min_len = 1
        max_len = 30


class L2110_QTY(Segment):
    """Service Supplemental Quantity"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Supplemental Quantity',
                   'usage': 'S',
                   'description': 'xid=QTY name=Service Supplemental Quantity',
                   'position': 1200,
                   'syntax': ['E0204', 'R0204'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'QTY'},
                                  'qty01': {'$ref': '#/$elements/L2110_QTY01'},
                                  'qty02': {'$ref': '#/$elements/L2110_QTY02'}},
                   'required': ['qty01', 'qty02']},
         'maxItems': 6}
        segment_name = 'QTY'
    qty01: L2110_QTY01
    qty02: L2110_QTY02


class L2110_LQ01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=LQ01 data_ele=1270',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/1270'}, {'enum': ['HE', 'RX']}]}}
        datatype = common.D_1270
        codes = ['HE', 'RX']
        min_len = 1
        max_len = 3


class L2110_LQ02(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'R',
         'description': 'xid=LQ02 data_ele=1271',
         'sequence': 2,
         'type': {'$ref': '#/$common/1271'}}
        datatype = common.D_1271
        min_len = 1
        max_len = 30


class L2110_LQ(Segment):
    """Health Care Remark Codes"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Health Care Remark Codes',
                   'usage': 'S',
                   'description': 'xid=LQ name=Health Care Remark Codes',
                   'position': 1300,
                   'syntax': ['C0102'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'LQ'},
                                  'lq01': {'$ref': '#/$elements/L2110_LQ01'},
                                  'lq02': {'$ref': '#/$elements/L2110_LQ02'}},
                   'required': ['lq01', 'lq02']},
         'maxItems': 99}
        segment_name = 'LQ'
    lq01: L2110_LQ01
    lq02: L2110_LQ02


class L2110(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Payment Information',
                   'usage': 'S',
                   'description': 'xid=2110 name=Service Payment Information type=None',
                   'position': 700,
                   'type': 'object',
                   'properties': {'svc': {'$ref': '#/$segments/L2110_SVC'},
                                  'dtm': {'$ref': '#/$segments/L2110_DTM'},
                                  'cas': {'$ref': '#/$segments/L2110_CAS'},
                                  'ref': {'$ref': '#/$segments/L2110_REF'},
                                  'amt': {'$ref': '#/$segments/L2110_AMT'},
                                  'qty': {'$ref': '#/$segments/L2110_QTY'},
                                  'lq': {'$ref': '#/$segments/L2110_LQ'}},
                   'required': ['svc']},
         'maxItems': 999}
    svc: L2110_SVC
    dtm: list[L2110_DTM] | None
    cas: list[L2110_CAS] | None
    ref: list[L2110_REF] | None
    ref: L2110_REF | None
    ref: list[L2110_REF] | None
    ref: list[L2110_REF] | None
    amt: list[L2110_AMT] | None
    qty: list[L2110_QTY] | None
    lq: list[L2110_LQ] | None


class L2100(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Payment Information',
                   'usage': 'R',
                   'description': 'xid=2100 name=Claim Payment Information type=None',
                   'position': 100,
                   'type': 'object',
                   'properties': {'clp': {'$ref': '#/$segments/L2100_CLP'},
                                  'cas': {'$ref': '#/$segments/L2100_CAS'},
                                  'nm1': {'$ref': '#/$segments/L2100_NM1'},
                                  'mia': {'$ref': '#/$segments/L2100_MIA'},
                                  'moa': {'$ref': '#/$segments/L2100_MOA'},
                                  'ref': {'$ref': '#/$segments/L2100_REF'},
                                  'dtm': {'$ref': '#/$segments/L2100_DTM'},
                                  'per': {'$ref': '#/$segments/L2100_PER'},
                                  'amt': {'$ref': '#/$segments/L2100_AMT'},
                                  'qty': {'$ref': '#/$segments/L2100_QTY'},
                                  'l2110': {'$ref': '#/$segments/L2110'}},
                   'required': ['clp', 'nm1']}}
    clp: L2100_CLP
    cas: list[L2100_CAS] | None
    nm1: L2100_NM1
    nm1: L2100_NM1
    nm1: L2100_NM1
    nm1: L2100_NM1
    nm1: L2100_NM1
    nm1: L2100_NM1
    nm1: L2100_NM1
    mia: L2100_MIA | None
    moa: L2100_MOA | None
    ref: list[L2100_REF] | None
    ref: list[L2100_REF] | None
    dtm: list[L2100_DTM] | None
    dtm: L2100_DTM | None
    dtm: L2100_DTM | None
    per: list[L2100_PER] | None
    amt: list[L2100_AMT] | None
    qty: list[L2100_QTY] | None
    l2110: list[L2110] | None


class L2000(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Header Number',
                   'usage': 'S',
                   'description': 'xid=2000 name=Header Number type=None',
                   'position': 30,
                   'type': 'object',
                   'properties': {'lx': {'$ref': '#/$segments/L2000_LX'},
                                  'ts3': {'$ref': '#/$segments/L2000_TS3'},
                                  'ts2': {'$ref': '#/$segments/L2000_TS2'},
                                  'l2100': {'$ref': '#/$segments/L2100'}},
                   'required': ['lx', 'l2100']}}
    lx: L2000_LX
    ts3: L2000_TS3 | None
    ts2: L2000_TS2 | None
    l2100: list[L2100]


class DETAIL(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table2 - Detail',
                   'usage': 'S',
                   'description': 'xid=DETAIL name=Table2 - Detail type=wrapper',
                   'position': 120,
                   'type': 'object',
                   'properties': {'l2000': {'$ref': '#/$segments/L2000'}}}}
    l2000: list[L2000] | None


class FOOTER_PLB01(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
         'description': 'xid=PLB01 data_ele=127',
         'sequence': 1,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_PLB02(Element):
    """Fiscal Period Date"""
    class Schema:
        json = {'title': 'Fiscal Period Date',
         'usage': 'R',
         'description': 'xid=PLB02 data_ele=373',
         'sequence': 2,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class FOOTER_PLB03_01(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=PLB03-01 data_ele=426',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/426'},
                            {'enum': ['50', '51', '72', '90', 'AH', 'AM', 'AP', 'B2',
                                      'B3', 'BD', 'BN', 'C5', 'CR', 'CS', 'CT', 'CV',
                                      'CW', 'DM', 'E3', 'FB', 'FC', 'GO', 'HM', 'IP',
                                      'IR', 'IS', 'J1', 'L3', 'L6', 'LE', 'LS', 'OA',
                                      'OB', 'PI', 'PL', 'RA', 'RE', 'SL', 'TL', 'WO',
                                      'WU']}]}}
        datatype = common.D_426
        codes = ['50', '51', '72', '90', 'AH', 'AM', 'AP', 'B2', 'B3', 'BD', 'BN', 'C5', 'CR', 'CS', 'CT', 'CV', 'CW', 'DM', 'E3', 'FB', 'FC', 'GO', 'HM', 'IP', 'IR', 'IS', 'J1', 'L3', 'L6', 'LE', 'LS', 'OA', 'OB', 'PI', 'PL', 'RA', 'RE', 'SL', 'TL', 'WO', 'WU']
        min_len = 2
        max_len = 2


class FOOTER_PLB03_02(Element):
    """Provider Adjustment Identifier"""
    class Schema:
        json = {'title': 'Provider Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB03-02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_PLB03(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'R',
         'description': 'xid=PLB03 name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'plb03_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB03-01 data_ele=426',
                                     'sequence': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/426'},
                                                        {'enum': ['50', '51', '72',
                                                                  '90', 'AH', 'AM',
                                                                  'AP', 'B2', 'B3',
                                                                  'BD', 'BN', 'C5',
                                                                  'CR', 'CS', 'CT',
                                                                  'CV', 'CW', 'DM',
                                                                  'E3', 'FB', 'FC',
                                                                  'GO', 'HM', 'IP',
                                                                  'IR', 'IS', 'J1',
                                                                  'L3', 'L6', 'LE',
                                                                  'LS', 'OA', 'OB',
                                                                  'PI', 'PL', 'RA',
                                                                  'RE', 'SL', 'TL',
                                                                  'WO', 'WU']}]}},
                        'plb03_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB03-02 data_ele=127',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/127'}}},
         'required': ['plb03_01']}
    plb03_01: FOOTER_PLB03_01
    plb03_02: FOOTER_PLB03_02 | None


class FOOTER_PLB04(Element):
    """Provider Adjustment Amount"""
    class Schema:
        json = {'title': 'Provider Adjustment Amount',
         'usage': 'R',
         'description': 'xid=PLB04 data_ele=782',
         'sequence': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class FOOTER_PLB05_01(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=PLB05-01 data_ele=426',
         'sequence': 1,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class FOOTER_PLB05_02(Element):
    """Provider Adjustment Identifier"""
    class Schema:
        json = {'title': 'Provider Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB05-02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_PLB05(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB05 name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'plb05_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB05-01 data_ele=426',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb05_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB05-02 data_ele=127',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/127'}}},
         'required': ['plb05_01']}
    plb05_01: FOOTER_PLB05_01
    plb05_02: FOOTER_PLB05_02 | None


class FOOTER_PLB06(Element):
    """Provider Adjustment Amount"""
    class Schema:
        json = {'title': 'Provider Adjustment Amount',
         'usage': 'S',
         'description': 'xid=PLB06 data_ele=782',
         'sequence': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class FOOTER_PLB07_01(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=PLB07-01 data_ele=426',
         'sequence': 1,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class FOOTER_PLB07_02(Element):
    """Provider Adjustment Identifier"""
    class Schema:
        json = {'title': 'Provider Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB07-02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_PLB07(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB07 name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 7,
         'syntax': [],
         'type': 'object',
         'properties': {'plb07_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB07-01 data_ele=426',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb07_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB07-02 data_ele=127',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/127'}}},
         'required': ['plb07_01']}
    plb07_01: FOOTER_PLB07_01
    plb07_02: FOOTER_PLB07_02 | None


class FOOTER_PLB08(Element):
    """Provider Adjustment Amount"""
    class Schema:
        json = {'title': 'Provider Adjustment Amount',
         'usage': 'S',
         'description': 'xid=PLB08 data_ele=782',
         'sequence': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class FOOTER_PLB09_01(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=PLB09-01 data_ele=426',
         'sequence': 1,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class FOOTER_PLB09_02(Element):
    """Provider Adjustment Identifier"""
    class Schema:
        json = {'title': 'Provider Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB09-02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_PLB09(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB09 name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 9,
         'syntax': [],
         'type': 'object',
         'properties': {'plb09_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB09-01 data_ele=426',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb09_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB09-02 data_ele=127',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/127'}}},
         'required': ['plb09_01']}
    plb09_01: FOOTER_PLB09_01
    plb09_02: FOOTER_PLB09_02 | None


class FOOTER_PLB10(Element):
    """Provider Adjustment Amount"""
    class Schema:
        json = {'title': 'Provider Adjustment Amount',
         'usage': 'S',
         'description': 'xid=PLB10 data_ele=782',
         'sequence': 10,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class FOOTER_PLB11_01(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=PLB11-01 data_ele=426',
         'sequence': 1,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class FOOTER_PLB11_02(Element):
    """Provider Adjustment Identifier"""
    class Schema:
        json = {'title': 'Provider Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB11-02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_PLB11(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB11 name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'plb11_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB11-01 data_ele=426',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb11_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB11-02 data_ele=127',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/127'}}},
         'required': ['plb11_01']}
    plb11_01: FOOTER_PLB11_01
    plb11_02: FOOTER_PLB11_02 | None


class FOOTER_PLB12(Element):
    """Provider Adjustment Amount"""
    class Schema:
        json = {'title': 'Provider Adjustment Amount',
         'usage': 'S',
         'description': 'xid=PLB12 data_ele=782',
         'sequence': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class FOOTER_PLB13_01(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=PLB13-01 data_ele=426',
         'sequence': 1,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class FOOTER_PLB13_02(Element):
    """Provider Adjustment Identifier"""
    class Schema:
        json = {'title': 'Provider Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB13-02 data_ele=127',
         'sequence': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_PLB13(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB13 name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 13,
         'syntax': [],
         'type': 'object',
         'properties': {'plb13_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB13-01 data_ele=426',
                                     'sequence': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb13_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB13-02 data_ele=127',
                                     'sequence': 2,
                                     'type': {'$ref': '#/$common/127'}}},
         'required': ['plb13_01']}
    plb13_01: FOOTER_PLB13_01
    plb13_02: FOOTER_PLB13_02 | None


class FOOTER_PLB14(Element):
    """Provider Adjustment Amount"""
    class Schema:
        json = {'title': 'Provider Adjustment Amount',
         'usage': 'S',
         'description': 'xid=PLB14 data_ele=782',
         'sequence': 14,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class FOOTER_PLB(Segment):
    """Provider Adjustment"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Provider Adjustment',
                   'usage': 'S',
                   'description': 'xid=PLB name=Provider Adjustment',
                   'position': 100,
                   'syntax': ['P0506', 'P0708', 'P0910', 'P1112', 'P1314'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PLB'},
                                  'plb01': {'$ref': '#/$elements/FOOTER_PLB01'},
                                  'plb02': {'$ref': '#/$elements/FOOTER_PLB02'},
                                  'plb03': {'$ref': '#/$elements/FOOTER_PLB03'},
                                  'plb04': {'$ref': '#/$elements/FOOTER_PLB04'},
                                  'plb05': {'$ref': '#/$elements/FOOTER_PLB05'},
                                  'plb06': {'$ref': '#/$elements/FOOTER_PLB06'},
                                  'plb07': {'$ref': '#/$elements/FOOTER_PLB07'},
                                  'plb08': {'$ref': '#/$elements/FOOTER_PLB08'},
                                  'plb09': {'$ref': '#/$elements/FOOTER_PLB09'},
                                  'plb10': {'$ref': '#/$elements/FOOTER_PLB10'},
                                  'plb11': {'$ref': '#/$elements/FOOTER_PLB11'},
                                  'plb12': {'$ref': '#/$elements/FOOTER_PLB12'},
                                  'plb13': {'$ref': '#/$elements/FOOTER_PLB13'},
                                  'plb14': {'$ref': '#/$elements/FOOTER_PLB14'}},
                   'required': ['plb01', 'plb02', 'plb03', 'plb04']}}
        segment_name = 'PLB'
    plb01: FOOTER_PLB01
    plb02: FOOTER_PLB02
    plb03: FOOTER_PLB03
    plb04: FOOTER_PLB04
    plb05: FOOTER_PLB05 | None
    plb06: FOOTER_PLB06 | None
    plb07: FOOTER_PLB07 | None
    plb08: FOOTER_PLB08 | None
    plb09: FOOTER_PLB09 | None
    plb10: FOOTER_PLB10 | None
    plb11: FOOTER_PLB11 | None
    plb12: FOOTER_PLB12 | None
    plb13: FOOTER_PLB13 | None
    plb14: FOOTER_PLB14 | None


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Footer',
                   'usage': 'S',
                   'description': 'xid=FOOTER name=Footer type=wrapper',
                   'position': 130,
                   'type': 'object',
                   'properties': {'plb': {'$ref': '#/$segments/FOOTER_PLB'}}},
         'maxItems': 1}
    plb: list[FOOTER_PLB] | None


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
         'position': 200,
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
                   'position': 200,
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


class MSG835W1(Message):
    """HIPAA Health Care Claim Payment/Advice 005010X221A1 835W1"""
    class Schema:
        json = {'title': 'HIPAA Health Care Claim Payment/Advice 005010X221A1 835W1',
         'description': 'xid=835W1 name=HIPAA Health Care Claim Payment/Advice '
                        '005010X221A1 835W1',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
