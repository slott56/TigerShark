"""
835.4010.X091.A1
Created 2023-05-12 20:25:34.364183
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
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['004010X091A1']}]}}
        datatype = common.D_480
        codes = ['004010X091A1']
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


class HEADER_BPR01(Element):
    """Transaction Handling Code"""
    class Schema:
        json = {'title': 'Transaction Handling Code',
         'usage': 'R',
         'description': 'xid=BPR01 data_ele=305',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
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
         'position': 12,
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
         'position': 13,
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
         'position': 14,
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
         'position': 15,
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
         'position': 16,
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
         'position': 17,
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
         'position': 18,
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
         'position': 19,
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
         'position': 20,
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
         'position': 21,
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
         'position': 20,
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
                        'bpr16': {'$ref': '#/$elements/HEADER_BPR16'},
                        'bpr17': {'$ref': '#/$elements/HEADER_BPR17'},
                        'bpr18': {'$ref': '#/$elements/HEADER_BPR18'},
                        'bpr19': {'$ref': '#/$elements/HEADER_BPR19'},
                        'bpr20': {'$ref': '#/$elements/HEADER_BPR20'},
                        'bpr21': {'$ref': '#/$elements/HEADER_BPR21'}},
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
    bpr17: HEADER_BPR17 | None
    bpr18: HEADER_BPR18 | None
    bpr19: HEADER_BPR19 | None
    bpr20: HEADER_BPR20 | None
    bpr21: HEADER_BPR21 | None


class HEADER_TRN01(Element):
    """Trace Type Code"""
    class Schema:
        json = {'title': 'Trace Type Code',
         'usage': 'R',
         'description': 'xid=TRN01 data_ele=481',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 40,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/100'}}
        datatype = common.D_100
        min_len = 3
        max_len = 3


class HEADER_CUR03(Element):
    """Exchange Rate"""
    class Schema:
        json = {'title': 'Exchange Rate',
         'usage': 'S',
         'description': 'xid=CUR03 data_ele=280',
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
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
         'position': 12,
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
         'position': 13,
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
         'position': 14,
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
         'position': 15,
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
         'position': 16,
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
         'position': 17,
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
         'position': 18,
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
         'position': 19,
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
         'position': 20,
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
         'position': 21,
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
         'position': 50,
         'type': 'object',
         'properties': {'xid': {'literal': 'CUR'},
                        'cur01': {'$ref': '#/$elements/HEADER_CUR01'},
                        'cur02': {'$ref': '#/$elements/HEADER_CUR02'},
                        'cur03': {'$ref': '#/$elements/HEADER_CUR03'},
                        'cur04': {'$ref': '#/$elements/HEADER_CUR04'},
                        'cur05': {'$ref': '#/$elements/HEADER_CUR05'},
                        'cur06': {'$ref': '#/$elements/HEADER_CUR06'},
                        'cur07': {'$ref': '#/$elements/HEADER_CUR07'},
                        'cur08': {'$ref': '#/$elements/HEADER_CUR08'},
                        'cur09': {'$ref': '#/$elements/HEADER_CUR09'},
                        'cur10': {'$ref': '#/$elements/HEADER_CUR10'},
                        'cur11': {'$ref': '#/$elements/HEADER_CUR11'},
                        'cur12': {'$ref': '#/$elements/HEADER_CUR12'},
                        'cur13': {'$ref': '#/$elements/HEADER_CUR13'},
                        'cur14': {'$ref': '#/$elements/HEADER_CUR14'},
                        'cur15': {'$ref': '#/$elements/HEADER_CUR15'},
                        'cur16': {'$ref': '#/$elements/HEADER_CUR16'},
                        'cur17': {'$ref': '#/$elements/HEADER_CUR17'},
                        'cur18': {'$ref': '#/$elements/HEADER_CUR18'},
                        'cur19': {'$ref': '#/$elements/HEADER_CUR19'},
                        'cur20': {'$ref': '#/$elements/HEADER_CUR20'},
                        'cur21': {'$ref': '#/$elements/HEADER_CUR21'}},
         'required': ['cur01', 'cur02']}
        segment_name = 'CUR'
    cur01: HEADER_CUR01
    cur02: HEADER_CUR02
    cur03: HEADER_CUR03 | None
    cur04: HEADER_CUR04 | None
    cur05: HEADER_CUR05 | None
    cur06: HEADER_CUR06 | None
    cur07: HEADER_CUR07 | None
    cur08: HEADER_CUR08 | None
    cur09: HEADER_CUR09 | None
    cur10: HEADER_CUR10 | None
    cur11: HEADER_CUR11 | None
    cur12: HEADER_CUR12 | None
    cur13: HEADER_CUR13 | None
    cur14: HEADER_CUR14 | None
    cur15: HEADER_CUR15 | None
    cur16: HEADER_CUR16 | None
    cur17: HEADER_CUR17 | None
    cur18: HEADER_CUR18 | None
    cur19: HEADER_CUR19 | None
    cur20: HEADER_CUR20 | None
    cur21: HEADER_CUR21 | None


class HEADER_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
    """Receiver Identification"""
    class Schema:
        json = {'title': 'Receiver Identification',
         'usage': 'S',
         'description': 'xid=REF name=Receiver Identification',
         'position': 60,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                        'ref02': {'$ref': '#/$elements/HEADER_REF02'},
                        'ref03': {'$ref': '#/$elements/HEADER_REF03'},
                        'c040': {'$ref': '#/$elements/HEADER_C040'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02
    ref03: HEADER_REF03 | None


class HEADER_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
    """Version Identification"""
    class Schema:
        json = {'title': 'Version Identification',
         'usage': 'S',
         'description': 'xid=REF name=Version Identification',
         'position': 60,
         'type': 'object',
         'properties': {'xid': {'literal': 'REF'},
                        'ref01': {'$ref': '#/$elements/HEADER_REF01'},
                        'ref02': {'$ref': '#/$elements/HEADER_REF02'},
                        'ref03': {'$ref': '#/$elements/HEADER_REF03'},
                        'c040': {'$ref': '#/$elements/HEADER_C040'}},
         'required': ['ref01', 'ref02']}
        segment_name = 'REF'
    ref01: HEADER_REF01
    ref02: HEADER_REF02
    ref03: HEADER_REF03 | None


class HEADER_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'DTM'},
                        'dtm01': {'$ref': '#/$elements/HEADER_DTM01'},
                        'dtm02': {'$ref': '#/$elements/HEADER_DTM02'},
                        'dtm03': {'$ref': '#/$elements/HEADER_DTM03'},
                        'dtm04': {'$ref': '#/$elements/HEADER_DTM04'},
                        'dtm05': {'$ref': '#/$elements/HEADER_DTM05'},
                        'dtm06': {'$ref': '#/$elements/HEADER_DTM06'}},
         'required': ['dtm01', 'dtm02']}
        segment_name = 'DTM'
    dtm01: HEADER_DTM01
    dtm02: HEADER_DTM02
    dtm03: HEADER_DTM03 | None
    dtm04: HEADER_DTM04 | None
    dtm05: HEADER_DTM05 | None
    dtm06: HEADER_DTM06 | None


class L1000A_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PR']}]}}
        datatype = common.D_98
        codes = ['PR']
        min_len = 2
        max_len = 3


class L1000A_N102(Element):
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


class L1000A_N103(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'S',
         'description': 'xid=N103 data_ele=66',
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 80,
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1000A_N101'},
                        'n102': {'$ref': '#/$elements/L1000A_N102'},
                        'n103': {'$ref': '#/$elements/L1000A_N103'},
                        'n104': {'$ref': '#/$elements/L1000A_N104'},
                        'n105': {'$ref': '#/$elements/L1000A_N105'},
                        'n106': {'$ref': '#/$elements/L1000A_N106'}},
         'required': ['n101']}
        segment_name = 'N1'
    n101: L1000A_N101
    n102: L1000A_N102 | None
    n103: L1000A_N103 | None
    n104: L1000A_N104 | None
    n105: L1000A_N105 | None
    n106: L1000A_N106 | None


class L1000A_N301(Element):
    """Payer Address Line"""
    class Schema:
        json = {'title': 'Payer Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
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
         'position': 2,
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
         'position': 100,
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
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L1000A_N402(Element):
    """Payer State Code"""
    class Schema:
        json = {'title': 'Payer State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L1000A_N403(Element):
    """Payer Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Payer Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
         'type': {'$ref': '#/$common/116'}}
        datatype = common.D_116
        min_len = 3
        max_len = 15


class L1000A_N404(Element):
    """Country Code"""
    class Schema:
        json = {'title': 'Country Code',
         'usage': 'N',
         'description': 'xid=N404 data_ele=26',
         'position': 4,
         'type': {'$ref': '#/$common/26'}}
        datatype = common.D_26
        min_len = 2
        max_len = 3


class L1000A_N405(Element):
    """Location Qualifier"""
    class Schema:
        json = {'title': 'Location Qualifier',
         'usage': 'N',
         'description': 'xid=N405 data_ele=309',
         'position': 5,
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
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L1000A_N4(Segment):
    """Payer City, State, ZIP Code"""
    class Schema:
        json = {'title': 'Payer City, State, ZIP Code',
         'usage': 'R',
         'description': 'xid=N4 name=Payer City, State, ZIP Code',
         'position': 110,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L1000A_N401'},
                        'n402': {'$ref': '#/$elements/L1000A_N402'},
                        'n403': {'$ref': '#/$elements/L1000A_N403'},
                        'n404': {'$ref': '#/$elements/L1000A_N404'},
                        'n405': {'$ref': '#/$elements/L1000A_N405'},
                        'n406': {'$ref': '#/$elements/L1000A_N406'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L1000A_N401
    n402: L1000A_N402
    n403: L1000A_N403
    n404: L1000A_N404 | None
    n405: L1000A_N405 | None
    n406: L1000A_N406 | None


class L1000A_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L1000A_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L1000A_REF(Segment):
    """Additional Payer Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Payer Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Additional Payer Identification',
                   'position': 120,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L1000A_REF01'},
                                  'ref02': {'$ref': '#/$elements/L1000A_REF02'},
                                  'ref03': {'$ref': '#/$elements/L1000A_REF03'},
                                  'c040': {'$ref': '#/$elements/L1000A_C040'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 4}
        segment_name = 'REF'
    ref01: L1000A_REF01
    ref02: L1000A_REF02
    ref03: L1000A_REF03 | None


class L1000A_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
         'type': {'$ref': '#/$common/443'}}
        datatype = common.D_443
        min_len = 1
        max_len = 20


class L1000A_PER(Segment):
    """Payer Contact Information"""
    class Schema:
        json = {'title': 'Payer Contact Information',
         'usage': 'S',
         'description': 'xid=PER name=Payer Contact Information',
         'position': 130,
         'type': 'object',
         'properties': {'xid': {'literal': 'PER'},
                        'per01': {'$ref': '#/$elements/L1000A_PER01'},
                        'per02': {'$ref': '#/$elements/L1000A_PER02'},
                        'per03': {'$ref': '#/$elements/L1000A_PER03'},
                        'per04': {'$ref': '#/$elements/L1000A_PER04'},
                        'per05': {'$ref': '#/$elements/L1000A_PER05'},
                        'per06': {'$ref': '#/$elements/L1000A_PER06'},
                        'per07': {'$ref': '#/$elements/L1000A_PER07'},
                        'per08': {'$ref': '#/$elements/L1000A_PER08'},
                        'per09': {'$ref': '#/$elements/L1000A_PER09'}},
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
    per09: L1000A_PER09 | None


class L1000A(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payer Identification',
                   'usage': 'R',
                   'description': 'xid=1000A name=Payer Identification type=None',
                   'position': 80,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000A_N1'},
                                  'n3': {'$ref': '#/$segments/L1000A_N3'},
                                  'n4': {'$ref': '#/$segments/L1000A_N4'},
                                  'ref': {'$ref': '#/$segments/L1000A_REF'},
                                  'per': {'$ref': '#/$segments/L1000A_PER'}},
                   'required': ['n1', 'n3', 'n4']},
         'maxItems': 1}
    n1: L1000A_N1
    n3: L1000A_N3
    n4: L1000A_N4
    ref: list[L1000A_REF] | None
    per: L1000A_PER | None


class L1000B_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['PE']}]}}
        datatype = common.D_98
        codes = ['PE']
        min_len = 2
        max_len = 3


class L1000B_N102(Element):
    """Payee Name"""
    class Schema:
        json = {'title': 'Payee Name',
         'usage': 'S',
         'description': 'xid=N102 data_ele=93',
         'position': 2,
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
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['FI', 'XX']}]}}
        datatype = common.D_66
        codes = ['FI', 'XX']
        min_len = 1
        max_len = 2


class L1000B_N104(Element):
    """Payee Identification Code"""
    class Schema:
        json = {'title': 'Payee Identification Code',
         'usage': 'R',
         'description': 'xid=N104 data_ele=67',
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 80,
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


class L1000B_N301(Element):
    """Payee Address Line"""
    class Schema:
        json = {'title': 'Payee Address Line',
         'usage': 'R',
         'description': 'xid=N301 data_ele=166',
         'position': 1,
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
         'position': 2,
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
         'position': 100,
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
         'position': 1,
         'type': {'$ref': '#/$common/19'}}
        datatype = common.D_19
        min_len = 2
        max_len = 30


class L1000B_N402(Element):
    """Payee State Code"""
    class Schema:
        json = {'title': 'Payee State Code',
         'usage': 'R',
         'description': 'xid=N402 data_ele=156',
         'position': 2,
         'type': {'$ref': '#/$common/156'}}
        datatype = common.D_156
        codes = common.states
        min_len = 2
        max_len = 2


class L1000B_N403(Element):
    """Payee Postal Zone or ZIP Code"""
    class Schema:
        json = {'title': 'Payee Postal Zone or ZIP Code',
         'usage': 'R',
         'description': 'xid=N403 data_ele=116',
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
         'type': {'$ref': '#/$common/310'}}
        datatype = common.D_310
        min_len = 1
        max_len = 30


class L1000B_N4(Segment):
    """Payee City, State, ZIP Code"""
    class Schema:
        json = {'title': 'Payee City, State, ZIP Code',
         'usage': 'S',
         'description': 'xid=N4 name=Payee City, State, ZIP Code',
         'position': 110,
         'type': 'object',
         'properties': {'xid': {'literal': 'N4'},
                        'n401': {'$ref': '#/$elements/L1000B_N401'},
                        'n402': {'$ref': '#/$elements/L1000B_N402'},
                        'n403': {'$ref': '#/$elements/L1000B_N403'},
                        'n404': {'$ref': '#/$elements/L1000B_N404'},
                        'n405': {'$ref': '#/$elements/L1000B_N405'},
                        'n406': {'$ref': '#/$elements/L1000B_N406'}},
         'required': ['n401', 'n402', 'n403']}
        segment_name = 'N4'
    n401: L1000B_N401
    n402: L1000B_N402
    n403: L1000B_N403
    n404: L1000B_N404 | None
    n405: L1000B_N405 | None
    n406: L1000B_N406 | None


class L1000B_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['0B', '1A', '1B', '1C', '1D', '1E', '1F', '1G',
                                      '1H', 'D3', 'G2', 'N5', 'PQ', 'TJ']}]}}
        datatype = common.D_128
        codes = ['0B', '1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', 'D3', 'G2', 'N5', 'PQ', 'TJ']
        min_len = 2
        max_len = 3


class L1000B_REF02(Element):
    """Additional Payee Identifier"""
    class Schema:
        json = {'title': 'Additional Payee Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
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
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L1000B_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L1000B_REF(Segment):
    """Payee Additional Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payee Additional Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Payee Additional Identification',
                   'position': 120,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L1000B_REF01'},
                                  'ref02': {'$ref': '#/$elements/L1000B_REF02'},
                                  'ref03': {'$ref': '#/$elements/L1000B_REF03'},
                                  'c040': {'$ref': '#/$elements/L1000B_C040'}},
                   'required': ['ref01', 'ref02']}}
        segment_name = 'REF'
    ref01: L1000B_REF01
    ref02: L1000B_REF02
    ref03: L1000B_REF03 | None


class L1000B(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Payee Identification',
                   'usage': 'R',
                   'description': 'xid=1000B name=Payee Identification type=None',
                   'position': 80,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1000B_N1'},
                                  'n3': {'$ref': '#/$segments/L1000B_N3'},
                                  'n4': {'$ref': '#/$segments/L1000B_N4'},
                                  'ref': {'$ref': '#/$segments/L1000B_REF'}},
                   'required': ['n1']},
         'maxItems': 1}
    n1: L1000B_N1
    n3: L1000B_N3 | None
    n4: L1000B_N4 | None
    ref: list[L1000B_REF] | None


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 1 - Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Table 1 - Header type=wrapper',
                   'position': 15,
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
         'position': 1,
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
         'position': 3,
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
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS306(Element):
    """Total Covered Charge Amount"""
    class Schema:
        json = {'title': 'Total Covered Charge Amount',
         'usage': 'S',
         'description': 'xid=TS306 data_ele=782',
         'position': 6,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS307(Element):
    """Total Noncovered Charge Amount"""
    class Schema:
        json = {'title': 'Total Noncovered Charge Amount',
         'usage': 'S',
         'description': 'xid=TS307 data_ele=782',
         'position': 7,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS308(Element):
    """Total Denied Charge Amount"""
    class Schema:
        json = {'title': 'Total Denied Charge Amount',
         'usage': 'S',
         'description': 'xid=TS308 data_ele=782',
         'position': 8,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS309(Element):
    """Total Provider Payment Amount"""
    class Schema:
        json = {'title': 'Total Provider Payment Amount',
         'usage': 'S',
         'description': 'xid=TS309 data_ele=782',
         'position': 9,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS310(Element):
    """Total Interest Amount"""
    class Schema:
        json = {'title': 'Total Interest Amount',
         'usage': 'S',
         'description': 'xid=TS310 data_ele=782',
         'position': 10,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS311(Element):
    """Total Contractual Adjustment Amount"""
    class Schema:
        json = {'title': 'Total Contractual Adjustment Amount',
         'usage': 'S',
         'description': 'xid=TS311 data_ele=782',
         'position': 11,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS312(Element):
    """Total Gramm-Rudman Reduction Amount"""
    class Schema:
        json = {'title': 'Total Gramm-Rudman Reduction Amount',
         'usage': 'S',
         'description': 'xid=TS312 data_ele=782',
         'position': 12,
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
         'position': 13,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS314(Element):
    """Total Blood Deductible Amount"""
    class Schema:
        json = {'title': 'Total Blood Deductible Amount',
         'usage': 'S',
         'description': 'xid=TS314 data_ele=782',
         'position': 14,
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
         'position': 15,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS316(Element):
    """Total Coinsurance Amount"""
    class Schema:
        json = {'title': 'Total Coinsurance Amount',
         'usage': 'S',
         'description': 'xid=TS316 data_ele=782',
         'position': 16,
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
         'position': 17,
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
         'position': 18,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2000_TS319(Element):
    """Total Deductible Amount"""
    class Schema:
        json = {'title': 'Total Deductible Amount',
         'usage': 'S',
         'description': 'xid=TS319 data_ele=782',
         'position': 19,
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
         'position': 20,
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
         'position': 21,
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
         'position': 22,
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
         'position': 23,
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
         'position': 24,
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
         'position': 5,
         'type': 'object',
         'properties': {'xid': {'literal': 'TS3'},
                        'ts301': {'$ref': '#/$elements/L2000_TS301'},
                        'ts302': {'$ref': '#/$elements/L2000_TS302'},
                        'ts303': {'$ref': '#/$elements/L2000_TS303'},
                        'ts304': {'$ref': '#/$elements/L2000_TS304'},
                        'ts305': {'$ref': '#/$elements/L2000_TS305'},
                        'ts306': {'$ref': '#/$elements/L2000_TS306'},
                        'ts307': {'$ref': '#/$elements/L2000_TS307'},
                        'ts308': {'$ref': '#/$elements/L2000_TS308'},
                        'ts309': {'$ref': '#/$elements/L2000_TS309'},
                        'ts310': {'$ref': '#/$elements/L2000_TS310'},
                        'ts311': {'$ref': '#/$elements/L2000_TS311'},
                        'ts312': {'$ref': '#/$elements/L2000_TS312'},
                        'ts313': {'$ref': '#/$elements/L2000_TS313'},
                        'ts314': {'$ref': '#/$elements/L2000_TS314'},
                        'ts315': {'$ref': '#/$elements/L2000_TS315'},
                        'ts316': {'$ref': '#/$elements/L2000_TS316'},
                        'ts317': {'$ref': '#/$elements/L2000_TS317'},
                        'ts318': {'$ref': '#/$elements/L2000_TS318'},
                        'ts319': {'$ref': '#/$elements/L2000_TS319'},
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
    ts306: L2000_TS306 | None
    ts307: L2000_TS307 | None
    ts308: L2000_TS308 | None
    ts309: L2000_TS309 | None
    ts310: L2000_TS310 | None
    ts311: L2000_TS311 | None
    ts312: L2000_TS312 | None
    ts313: L2000_TS313 | None
    ts314: L2000_TS314 | None
    ts315: L2000_TS315 | None
    ts316: L2000_TS316 | None
    ts317: L2000_TS317 | None
    ts318: L2000_TS318 | None
    ts319: L2000_TS319 | None
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
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
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
         'position': 12,
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
         'position': 13,
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
         'position': 14,
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
         'position': 15,
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
         'position': 16,
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
         'position': 17,
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
         'position': 18,
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
         'position': 19,
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
         'position': 7,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/1029'}}
        datatype = common.D_1029
        codes = common.claim_status
        min_len = 1
        max_len = 2


class L2100_CLP03(Element):
    """Total Claim Charge Amount"""
    class Schema:
        json = {'title': 'Total Claim Charge Amount',
         'usage': 'R',
         'description': 'xid=CLP03 data_ele=782',
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
         'type': {'allOf': [{'$ref': '#/$common/1032'},
                            {'enum': ['12', '13', '14', '15', '16', 'AM', 'CH', 'DS',
                                      'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA',
                                      'WC', 'ZZ']}]}}
        datatype = common.D_1032
        codes = ['12', '13', '14', '15', '16', 'AM', 'CH', 'DS', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ']
        min_len = 1
        max_len = 2


class L2100_CLP07(Element):
    """Payer Claim Control Number"""
    class Schema:
        json = {'title': 'Payer Claim Control Number',
         'usage': 'S',
         'description': 'xid=CLP07 data_ele=127',
         'position': 7,
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
         'position': 8,
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
         'position': 9,
         'type': {'allOf': [{'$ref': '#/$common/1325'},
                            {'enum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                      'K', 'L', 'M', 'N', 'O', 'X', 'Y', 'Z']}]}}
        datatype = common.D_1325
        codes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'X', 'Y', 'Z']
        min_len = 1
        max_len = 1


class L2100_CLP10(Element):
    """Patient Status Code"""
    class Schema:
        json = {'title': 'Patient Status Code',
         'usage': 'N',
         'description': 'xid=CLP10 data_ele=1352',
         'position': 10,
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
         'position': 11,
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
         'position': 12,
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
         'position': 13,
         'type': {'$ref': '#/$common/954'}}
        datatype = common.D_954
        min_len = 1
        max_len = 10


class L2100_CLP(Segment):
    """Claim Payment Information"""
    class Schema:
        json = {'title': 'Claim Payment Information',
         'usage': 'R',
         'description': 'xid=CLP name=Claim Payment Information',
         'position': 10,
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
                        'clp10': {'$ref': '#/$elements/L2100_CLP10'},
                        'clp11': {'$ref': '#/$elements/L2100_CLP11'},
                        'clp12': {'$ref': '#/$elements/L2100_CLP12'},
                        'clp13': {'$ref': '#/$elements/L2100_CLP13'}},
         'required': ['clp01', 'clp02', 'clp03', 'clp04', 'clp06']}
        segment_name = 'CLP'
    clp01: L2100_CLP01
    clp02: L2100_CLP02
    clp03: L2100_CLP03
    clp04: L2100_CLP04
    clp05: L2100_CLP05 | None
    clp06: L2100_CLP06
    clp07: L2100_CLP07 | None
    clp08: L2100_CLP08 | None
    clp09: L2100_CLP09 | None
    clp10: L2100_CLP10 | None
    clp11: L2100_CLP11 | None
    clp12: L2100_CLP12 | None
    clp13: L2100_CLP13 | None


class L2100_CAS01(Element):
    """Claim Adjustment Group Code"""
    class Schema:
        json = {'title': 'Claim Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'CR', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'CR', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2100_CAS02(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=CAS02 data_ele=1034',
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
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
         'position': 12,
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
         'position': 13,
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
         'position': 14,
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
         'position': 15,
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
         'position': 16,
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
         'position': 17,
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
         'position': 18,
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
         'position': 19,
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
                   'position': 20,
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
         'position': 1,
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
         'position': 2,
         'type': {'allOf': [{'$ref': '#/$common/1065'}, {'enum': ['1']}]}}
        datatype = common.D_1065
        codes = ['1']
        min_len = 1
        max_len = 1


class L2100_NM103(Element):
    """Patient Last Name"""
    class Schema:
        json = {'title': 'Patient Last Name',
         'usage': 'R',
         'description': 'xid=NM103 data_ele=1035',
         'position': 3,
         'type': {'$ref': '#/$common/1035'}}
        datatype = common.D_1035
        min_len = 1
        max_len = 60


class L2100_NM104(Element):
    """Patient First Name"""
    class Schema:
        json = {'title': 'Patient First Name',
         'usage': 'R',
         'description': 'xid=NM104 data_ele=1036',
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100_NM105(Element):
    """Patient Middle Name"""
    class Schema:
        json = {'title': 'Patient Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100_NM1(Segment):
    """Patient Name"""
    class Schema:
        json = {'title': 'Patient Name',
         'usage': 'R',
         'description': 'xid=NM1 name=Patient Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100_NM111'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm104']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103
    nm104: L2100_NM104
    nm105: L2100_NM105 | None
    nm106: L2100_NM106 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108 | None
    nm109: L2100_NM109 | None
    nm110: L2100_NM110 | None
    nm111: L2100_NM111 | None


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100_NM105(Element):
    """Subscriber Middle Name"""
    class Schema:
        json = {'title': 'Subscriber Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
         'type': {'allOf': [{'$ref': '#/$common/66'}, {'enum': ['34', 'HN', 'MI']}]}}
        datatype = common.D_66
        codes = ['34', 'HN', 'MI']
        min_len = 1
        max_len = 2


class L2100_NM109(Element):
    """Subscriber Identifier"""
    class Schema:
        json = {'title': 'Subscriber Identifier',
         'usage': 'R',
         'description': 'xid=NM109 data_ele=67',
         'position': 9,
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
         'position': 10,
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
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100_NM1(Segment):
    """Insured Name"""
    class Schema:
        json = {'title': 'Insured Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Insured Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100_NM111'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm106: L2100_NM106 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108
    nm109: L2100_NM109
    nm110: L2100_NM110 | None
    nm111: L2100_NM111 | None


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100_NM1(Segment):
    """Corrected Patient/Insured Name"""
    class Schema:
        json = {'title': 'Corrected Patient/Insured Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Corrected Patient/Insured Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100_NM111'}},
         'required': ['nm101', 'nm102']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm106: L2100_NM106 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108 | None
    nm109: L2100_NM109 | None
    nm110: L2100_NM110 | None
    nm111: L2100_NM111 | None


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
         'type': {'$ref': '#/$common/1036'}}
        datatype = common.D_1036
        min_len = 1
        max_len = 35


class L2100_NM105(Element):
    """Rendering Provider Middle Name"""
    class Schema:
        json = {'title': 'Rendering Provider Middle Name',
         'usage': 'S',
         'description': 'xid=NM105 data_ele=1037',
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100_NM1(Segment):
    """Service Provider Name"""
    class Schema:
        json = {'title': 'Service Provider Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Service Provider Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100_NM111'}},
         'required': ['nm101', 'nm102', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103 | None
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm106: L2100_NM106 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108
    nm109: L2100_NM109
    nm110: L2100_NM110 | None
    nm111: L2100_NM111 | None


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100_NM1(Segment):
    """Crossover Carrier Name"""
    class Schema:
        json = {'title': 'Crossover Carrier Name',
         'usage': 'S',
         'description': 'xid=NM1 name=Crossover Carrier Name',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'NM1'},
                        'nm101': {'$ref': '#/$elements/L2100_NM101'},
                        'nm102': {'$ref': '#/$elements/L2100_NM102'},
                        'nm103': {'$ref': '#/$elements/L2100_NM103'},
                        'nm104': {'$ref': '#/$elements/L2100_NM104'},
                        'nm105': {'$ref': '#/$elements/L2100_NM105'},
                        'nm106': {'$ref': '#/$elements/L2100_NM106'},
                        'nm107': {'$ref': '#/$elements/L2100_NM107'},
                        'nm108': {'$ref': '#/$elements/L2100_NM108'},
                        'nm109': {'$ref': '#/$elements/L2100_NM109'},
                        'nm110': {'$ref': '#/$elements/L2100_NM110'},
                        'nm111': {'$ref': '#/$elements/L2100_NM111'}},
         'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm106: L2100_NM106 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108
    nm109: L2100_NM109
    nm110: L2100_NM110 | None
    nm111: L2100_NM111 | None


class L2100_NM101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=NM101 data_ele=98',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L2100_NM1(Segment):
    """Corrected Priority Payer Name"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Corrected Priority Payer Name',
                   'usage': 'S',
                   'description': 'xid=NM1 name=Corrected Priority Payer Name',
                   'position': 30,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'NM1'},
                                  'nm101': {'$ref': '#/$elements/L2100_NM101'},
                                  'nm102': {'$ref': '#/$elements/L2100_NM102'},
                                  'nm103': {'$ref': '#/$elements/L2100_NM103'},
                                  'nm104': {'$ref': '#/$elements/L2100_NM104'},
                                  'nm105': {'$ref': '#/$elements/L2100_NM105'},
                                  'nm106': {'$ref': '#/$elements/L2100_NM106'},
                                  'nm107': {'$ref': '#/$elements/L2100_NM107'},
                                  'nm108': {'$ref': '#/$elements/L2100_NM108'},
                                  'nm109': {'$ref': '#/$elements/L2100_NM109'},
                                  'nm110': {'$ref': '#/$elements/L2100_NM110'},
                                  'nm111': {'$ref': '#/$elements/L2100_NM111'}},
                   'required': ['nm101', 'nm102', 'nm103', 'nm108', 'nm109']},
         'maxItems': 2}
        segment_name = 'NM1'
    nm101: L2100_NM101
    nm102: L2100_NM102
    nm103: L2100_NM103
    nm104: L2100_NM104 | None
    nm105: L2100_NM105 | None
    nm106: L2100_NM106 | None
    nm107: L2100_NM107 | None
    nm108: L2100_NM108
    nm109: L2100_NM109
    nm110: L2100_NM110 | None
    nm111: L2100_NM111 | None


class L2100_MIA01(Element):
    """Covered Days or Visits Count"""
    class Schema:
        json = {'title': 'Covered Days or Visits Count',
         'usage': 'R',
         'description': 'xid=MIA01 data_ele=380',
         'position': 1,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_MIA02(Element):
    """PPS Operating Outlier Amount"""
    class Schema:
        json = {'title': 'PPS Operating Outlier Amount',
         'usage': 'S',
         'description': 'xid=MIA02 data_ele=380',
         'position': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_MIA03(Element):
    """Lifetime Psychiatric Days Count"""
    class Schema:
        json = {'title': 'Lifetime Psychiatric Days Count',
         'usage': 'S',
         'description': 'xid=MIA03 data_ele=380',
         'position': 3,
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
         'position': 4,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA05(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MIA05 data_ele=127',
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
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
         'position': 12,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA13(Element):
    """PPS-Capital IME Amount"""
    class Schema:
        json = {'title': 'PPS-Capital IME Amount',
         'usage': 'S',
         'description': 'xid=MIA13 data_ele=782',
         'position': 13,
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
         'position': 14,
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
         'position': 15,
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
         'position': 16,
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
         'position': 17,
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
         'position': 18,
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
         'position': 19,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MIA20(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MIA20 data_ele=127',
         'position': 20,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA21(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MIA21 data_ele=127',
         'position': 21,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA22(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MIA22 data_ele=127',
         'position': 22,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MIA23(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MIA23 data_ele=127',
         'position': 23,
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
         'position': 24,
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
         'position': 33,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/782'}}
        datatype = common.D_782
        min_len = 1
        max_len = 18


class L2100_MOA03(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MOA03 data_ele=127',
         'position': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA04(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MOA04 data_ele=127',
         'position': 4,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA05(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MOA05 data_ele=127',
         'position': 5,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA06(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MOA06 data_ele=127',
         'position': 6,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        codes = common.remark_code
        min_len = 1
        max_len = 50


class L2100_MOA07(Element):
    """Remark Code"""
    class Schema:
        json = {'title': 'Remark Code',
         'usage': 'S',
         'description': 'xid=MOA07 data_ele=127',
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 35,
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
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1L', '1W', '9A', '9C', 'A6', 'BB', 'CE', 'EA',
                                      'F8', 'G1', 'G3', 'IG', 'SY']}]}}
        datatype = common.D_128
        codes = ['1L', '1W', '9A', '9C', 'A6', 'BB', 'CE', 'EA', 'F8', 'G1', 'G3', 'IG', 'SY']
        min_len = 2
        max_len = 3


class L2100_REF02(Element):
    """Other Claim Related Identifier"""
    class Schema:
        json = {'title': 'Other Claim Related Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
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
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100_REF(Segment):
    """Other Claim Related Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Other Claim Related Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Other Claim Related Identification',
                   'position': 40,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2100_REF03'},
                                  'c040': {'$ref': '#/$elements/L2100_C040'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 5}
        segment_name = 'REF'
    ref01: L2100_REF01
    ref02: L2100_REF02
    ref03: L2100_REF03 | None


class L2100_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1A', '1B', '1C', '1D', '1G', '1H', 'D3',
                                      'G2']}]}}
        datatype = common.D_128
        codes = ['1A', '1B', '1C', '1D', '1G', '1H', 'D3', 'G2']
        min_len = 2
        max_len = 3


class L2100_REF02(Element):
    """Rendering Provider Secondary Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Secondary Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
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
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2100_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2100_REF(Segment):
    """Rendering Provider Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Identification',
                   'position': 40,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2100_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2100_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2100_REF03'},
                                  'c040': {'$ref': '#/$elements/L2100_C040'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 10}
        segment_name = 'REF'
    ref01: L2100_REF01
    ref02: L2100_REF02
    ref03: L2100_REF03 | None


class L2100_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/374'},
                            {'enum': ['036', '050', '232', '233']}]}}
        datatype = common.D_374
        codes = ['036', '050', '232', '233']
        min_len = 3
        max_len = 3


class L2100_DTM02(Element):
    """Claim Date"""
    class Schema:
        json = {'title': 'Claim Date',
         'usage': 'R',
         'description': 'xid=DTM02 data_ele=373',
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
         'type': {'$ref': '#/$common/1251'}}
        datatype = common.D_1251
        min_len = 1
        max_len = 35


class L2100_DTM(Segment):
    """Claim Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Claim Date',
                   'usage': 'S',
                   'description': 'xid=DTM name=Claim Date',
                   'position': 50,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTM'},
                                  'dtm01': {'$ref': '#/$elements/L2100_DTM01'},
                                  'dtm02': {'$ref': '#/$elements/L2100_DTM02'},
                                  'dtm03': {'$ref': '#/$elements/L2100_DTM03'},
                                  'dtm04': {'$ref': '#/$elements/L2100_DTM04'},
                                  'dtm05': {'$ref': '#/$elements/L2100_DTM05'},
                                  'dtm06': {'$ref': '#/$elements/L2100_DTM06'}},
                   'required': ['dtm01', 'dtm02']},
         'maxItems': 4}
        segment_name = 'DTM'
    dtm01: L2100_DTM01
    dtm02: L2100_DTM02
    dtm03: L2100_DTM03 | None
    dtm04: L2100_DTM04 | None
    dtm05: L2100_DTM05 | None
    dtm06: L2100_DTM06 | None


class L2100_PER01(Element):
    """Contact Function Code"""
    class Schema:
        json = {'title': 'Contact Function Code',
         'usage': 'R',
         'description': 'xid=PER01 data_ele=366',
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L2100_PER03(Element):
    """Communication Number Qualifier"""
    class Schema:
        json = {'title': 'Communication Number Qualifier',
         'usage': 'S',
         'description': 'xid=PER03 data_ele=365',
         'position': 3,
         'type': {'allOf': [{'$ref': '#/$common/365'}, {'enum': ['EM', 'FX', 'TE']}]}}
        datatype = common.D_365
        codes = ['EM', 'FX', 'TE']
        min_len = 2
        max_len = 2


class L2100_PER04(Element):
    """Claim Contact Communications Number"""
    class Schema:
        json = {'title': 'Claim Contact Communications Number',
         'usage': 'S',
         'description': 'xid=PER04 data_ele=364',
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
                   'position': 60,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PER'},
                                  'per01': {'$ref': '#/$elements/L2100_PER01'},
                                  'per02': {'$ref': '#/$elements/L2100_PER02'},
                                  'per03': {'$ref': '#/$elements/L2100_PER03'},
                                  'per04': {'$ref': '#/$elements/L2100_PER04'},
                                  'per05': {'$ref': '#/$elements/L2100_PER05'},
                                  'per06': {'$ref': '#/$elements/L2100_PER06'},
                                  'per07': {'$ref': '#/$elements/L2100_PER07'},
                                  'per08': {'$ref': '#/$elements/L2100_PER08'},
                                  'per09': {'$ref': '#/$elements/L2100_PER09'}},
                   'required': ['per01']},
         'maxItems': 3}
        segment_name = 'PER'
    per01: L2100_PER01
    per02: L2100_PER02 | None
    per03: L2100_PER03 | None
    per04: L2100_PER04 | None
    per05: L2100_PER05 | None
    per06: L2100_PER06 | None
    per07: L2100_PER07 | None
    per08: L2100_PER08 | None
    per09: L2100_PER09 | None


class L2100_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['I', 'T', 'AU', 'D8', 'DY', 'F5', 'NL', 'T2',
                                      'ZK', 'ZL', 'ZM', 'ZN', 'ZO', 'ZZ']}]}}
        datatype = common.D_522
        codes = ['I', 'T', 'AU', 'D8', 'DY', 'F5', 'NL', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO', 'ZZ']
        min_len = 1
        max_len = 3


class L2100_AMT02(Element):
    """Claim Supplemental Information Amount"""
    class Schema:
        json = {'title': 'Claim Supplemental Information Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'position': 2,
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
         'position': 3,
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
                   'position': 62,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2100_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2100_AMT02'},
                                  'amt03': {'$ref': '#/$elements/L2100_AMT03'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 14}
        segment_name = 'AMT'
    amt01: L2100_AMT01
    amt02: L2100_AMT02
    amt03: L2100_AMT03 | None


class L2100_QTY01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=QTY01 data_ele=673',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['CA', 'CD', 'LA', 'LE', 'NA', 'NE', 'NR', 'OU',
                                      'PS', 'VS', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']}]}}
        datatype = common.D_673
        codes = ['CA', 'CD', 'LA', 'LE', 'NA', 'NE', 'NR', 'OU', 'PS', 'VS', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']
        min_len = 2
        max_len = 2


class L2100_QTY02(Element):
    """Claim Supplemental Information Quantity"""
    class Schema:
        json = {'title': 'Claim Supplemental Information Quantity',
         'usage': 'R',
         'description': 'xid=QTY02 data_ele=380',
         'position': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2100_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 3,
         'syntax': []}


class L2100_QTY04(Element):
    """Free-Form Message"""
    class Schema:
        json = {'title': 'Free-Form Message',
         'usage': 'N',
         'description': 'xid=QTY04 data_ele=61',
         'position': 4,
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
                   'position': 64,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'QTY'},
                                  'qty01': {'$ref': '#/$elements/L2100_QTY01'},
                                  'qty02': {'$ref': '#/$elements/L2100_QTY02'},
                                  'c001': {'$ref': '#/$elements/L2100_C001'},
                                  'qty04': {'$ref': '#/$elements/L2100_QTY04'}},
                   'required': ['qty01', 'qty02']},
         'maxItems': 15}
        segment_name = 'QTY'
    qty01: L2100_QTY01
    qty02: L2100_QTY02
    qty04: L2100_QTY04 | None


class L2110_SVC01_01(Element):
    """Product or Service ID Qualifier"""
    class Schema:
        json = {'title': 'Product or Service ID Qualifier',
         'usage': 'R',
         'description': 'xid=SVC01-01 data_ele=235',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'ER', 'HC', 'ID', 'IV', 'N4', 'NU', 'RB',
                                      'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'ER', 'HC', 'ID', 'IV', 'N4', 'NU', 'RB', 'ZZ']
        min_len = 2
        max_len = 2


class L2110_SVC01_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SVC01-02 data_ele=234',
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
         'type': {'$ref': '#/$common/1339'}}
        datatype = common.D_1339
        min_len = 2
        max_len = 2


class L2110_SVC01_07(Element):
    """Procedure Code Description"""
    class Schema:
        json = {'title': 'Procedure Code Description',
         'usage': 'S',
         'description': 'xid=SVC01-07 data_ele=352',
         'position': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'R',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 1,
         'syntax': [],
         'type': 'object',
         'properties': {'svc01_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SVC01-01 data_ele=235',
                                     'position': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD', 'ER', 'HC',
                                                                  'ID', 'IV', 'N4',
                                                                  'NU', 'RB',
                                                                  'ZZ']}]}},
                        'svc01_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SVC01-02 data_ele=234',
                                     'position': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'svc01_03': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-03 data_ele=1339',
                                     'position': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_04': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-04 data_ele=1339',
                                     'position': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_05': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-05 data_ele=1339',
                                     'position': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_06': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-06 data_ele=1339',
                                     'position': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc01_07': {'title': 'Procedure Code Description',
                                     'usage': 'S',
                                     'description': 'xid=SVC01-07 data_ele=352',
                                     'position': 7,
                                     'type': {'$ref': '#/$common/352'}}},
         'required': ['svc01_01', 'svc01_02']}
    svc01_01: L2110_SVC01_01
    svc01_02: L2110_SVC01_02
    svc01_03: L2110_SVC01_03 | None
    svc01_04: L2110_SVC01_04 | None
    svc01_05: L2110_SVC01_05 | None
    svc01_06: L2110_SVC01_06 | None
    svc01_07: L2110_SVC01_07 | None


class L2110_SVC02(Element):
    """Line Item Charge Amount"""
    class Schema:
        json = {'title': 'Line Item Charge Amount',
         'usage': 'R',
         'description': 'xid=SVC02 data_ele=782',
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/235'},
                            {'enum': ['AD', 'ER', 'HC', 'ID', 'IV', 'N4', 'NU', 'RB',
                                      'ZZ']}]}}
        datatype = common.D_235
        codes = ['AD', 'ER', 'HC', 'ID', 'IV', 'N4', 'NU', 'RB', 'ZZ']
        min_len = 2
        max_len = 2


class L2110_SVC06_02(Element):
    """Procedure Code"""
    class Schema:
        json = {'title': 'Procedure Code',
         'usage': 'R',
         'description': 'xid=SVC06-02 data_ele=234',
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110_C003(Composite):
    class Schema:
        json = {'title': 'Composite Medical Procedure Identifier',
         'usage': 'S',
         'description': 'xid=None name=Composite Medical Procedure Identifier refdes= '
                        'data_ele=C003',
         'sequence': 6,
         'syntax': [],
         'type': 'object',
         'properties': {'svc06_01': {'title': 'Product or Service ID Qualifier',
                                     'usage': 'R',
                                     'description': 'xid=SVC06-01 data_ele=235',
                                     'position': 1,
                                     'type': {'allOf': [{'$ref': '#/$common/235'},
                                                        {'enum': ['AD', 'ER', 'HC',
                                                                  'ID', 'IV', 'N4',
                                                                  'NU', 'RB',
                                                                  'ZZ']}]}},
                        'svc06_02': {'title': 'Procedure Code',
                                     'usage': 'R',
                                     'description': 'xid=SVC06-02 data_ele=234',
                                     'position': 2,
                                     'type': {'$ref': '#/$common/234'}},
                        'svc06_03': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-03 data_ele=1339',
                                     'position': 3,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_04': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-04 data_ele=1339',
                                     'position': 4,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_05': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-05 data_ele=1339',
                                     'position': 5,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_06': {'title': 'Procedure Modifier',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-06 data_ele=1339',
                                     'position': 6,
                                     'type': {'$ref': '#/$common/1339'}},
                        'svc06_07': {'title': 'Procedure Code Description',
                                     'usage': 'S',
                                     'description': 'xid=SVC06-07 data_ele=352',
                                     'position': 7,
                                     'type': {'$ref': '#/$common/352'}}},
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
         'position': 7,
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
         'position': 70,
         'type': 'object',
         'properties': {'xid': {'literal': 'SVC'},
                        'c003': {'$ref': '#/$elements/L2110_C003'},
                        'svc02': {'$ref': '#/$elements/L2110_SVC02'},
                        'svc03': {'$ref': '#/$elements/L2110_SVC03'},
                        'svc04': {'$ref': '#/$elements/L2110_SVC04'},
                        'svc05': {'$ref': '#/$elements/L2110_SVC05'},
                        'svc07': {'$ref': '#/$elements/L2110_SVC07'}},
         'required': ['c003', 'svc02', 'svc03']}
        segment_name = 'SVC'
    c003: L2110_C003
    svc02: L2110_SVC02
    svc03: L2110_SVC03
    svc04: L2110_SVC04 | None
    svc05: L2110_SVC05 | None
    c003: L2110_C003
    svc07: L2110_SVC07 | None


class L2110_DTM01(Element):
    """Date Time Qualifier"""
    class Schema:
        json = {'title': 'Date Time Qualifier',
         'usage': 'R',
         'description': 'xid=DTM01 data_ele=374',
         'position': 1,
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
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
                   'position': 80,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'DTM'},
                                  'dtm01': {'$ref': '#/$elements/L2110_DTM01'},
                                  'dtm02': {'$ref': '#/$elements/L2110_DTM02'},
                                  'dtm03': {'$ref': '#/$elements/L2110_DTM03'},
                                  'dtm04': {'$ref': '#/$elements/L2110_DTM04'},
                                  'dtm05': {'$ref': '#/$elements/L2110_DTM05'},
                                  'dtm06': {'$ref': '#/$elements/L2110_DTM06'}},
                   'required': ['dtm01', 'dtm02']},
         'maxItems': 3}
        segment_name = 'DTM'
    dtm01: L2110_DTM01
    dtm02: L2110_DTM02
    dtm03: L2110_DTM03 | None
    dtm04: L2110_DTM04 | None
    dtm05: L2110_DTM05 | None
    dtm06: L2110_DTM06 | None


class L2110_CAS01(Element):
    """Claim Adjustment Group Code"""
    class Schema:
        json = {'title': 'Claim Adjustment Group Code',
         'usage': 'R',
         'description': 'xid=CAS01 data_ele=1033',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/1033'},
                            {'enum': ['CO', 'CR', 'OA', 'PI', 'PR']}]}}
        datatype = common.D_1033
        codes = ['CO', 'CR', 'OA', 'PI', 'PR']
        min_len = 1
        max_len = 2


class L2110_CAS02(Element):
    """Adjustment Reason Code"""
    class Schema:
        json = {'title': 'Adjustment Reason Code',
         'usage': 'R',
         'description': 'xid=CAS02 data_ele=1034',
         'position': 2,
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
         'position': 3,
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
         'position': 4,
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
         'position': 5,
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
         'position': 6,
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
         'position': 7,
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
         'position': 8,
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
         'position': 9,
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
         'position': 10,
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
         'position': 11,
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
         'position': 12,
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
         'position': 13,
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
         'position': 14,
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
         'position': 15,
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
         'position': 16,
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
         'position': 17,
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
         'position': 18,
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
         'position': 19,
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
                   'position': 90,
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
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1S', '6R', 'BB', 'E9', 'G1', 'G3', 'LU',
                                      'RB']}]}}
        datatype = common.D_128
        codes = ['1S', '6R', 'BB', 'E9', 'G1', 'G3', 'LU', 'RB']
        min_len = 2
        max_len = 3


class L2110_REF02(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
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
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110_REF(Segment):
    """Service Identification"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Service Identification',
                   'usage': 'S',
                   'description': 'xid=REF name=Service Identification',
                   'position': 100,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2110_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2110_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2110_REF03'},
                                  'c040': {'$ref': '#/$elements/L2110_C040'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 7}
        segment_name = 'REF'
    ref01: L2110_REF01
    ref02: L2110_REF02
    ref03: L2110_REF03 | None


class L2110_REF01(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=REF01 data_ele=128',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/128'},
                            {'enum': ['1A', '1B', '1C', '1D', '1G', '1H', '1J', 'HPI',
                                      'SY', 'TJ']}]}}
        datatype = common.D_128
        codes = ['1A', '1B', '1C', '1D', '1G', '1H', '1J', 'HPI', 'SY', 'TJ']
        min_len = 2
        max_len = 3


class L2110_REF02(Element):
    """Rendering Provider Identifier"""
    class Schema:
        json = {'title': 'Rendering Provider Identifier',
         'usage': 'R',
         'description': 'xid=REF02 data_ele=127',
         'position': 2,
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
         'position': 3,
         'type': {'$ref': '#/$common/352'}}
        datatype = common.D_352
        min_len = 1
        max_len = 80


class L2110_C040(Composite):
    class Schema:
        json = {'title': 'Reference Identifier',
         'usage': 'N',
         'description': 'xid=None name=Reference Identifier refdes= data_ele=C040',
         'sequence': 4,
         'syntax': []}


class L2110_REF(Segment):
    """Rendering Provider Information"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Rendering Provider Information',
                   'usage': 'S',
                   'description': 'xid=REF name=Rendering Provider Information',
                   'position': 100,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'REF'},
                                  'ref01': {'$ref': '#/$elements/L2110_REF01'},
                                  'ref02': {'$ref': '#/$elements/L2110_REF02'},
                                  'ref03': {'$ref': '#/$elements/L2110_REF03'},
                                  'c040': {'$ref': '#/$elements/L2110_C040'}},
                   'required': ['ref01', 'ref02']},
         'maxItems': 10}
        segment_name = 'REF'
    ref01: L2110_REF01
    ref02: L2110_REF02
    ref03: L2110_REF03 | None


class L2110_AMT01(Element):
    """Amount Qualifier Code"""
    class Schema:
        json = {'title': 'Amount Qualifier Code',
         'usage': 'R',
         'description': 'xid=AMT01 data_ele=522',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/522'},
                            {'enum': ['B6', 'DY', 'KH', 'NE', 'T', 'T2', 'ZK', 'ZL',
                                      'ZM', 'ZN', 'ZO']}]}}
        datatype = common.D_522
        codes = ['B6', 'DY', 'KH', 'NE', 'T', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']
        min_len = 1
        max_len = 3


class L2110_AMT02(Element):
    """Service Supplemental Amount"""
    class Schema:
        json = {'title': 'Service Supplemental Amount',
         'usage': 'R',
         'description': 'xid=AMT02 data_ele=782',
         'position': 2,
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
         'position': 3,
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
                   'position': 110,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'AMT'},
                                  'amt01': {'$ref': '#/$elements/L2110_AMT01'},
                                  'amt02': {'$ref': '#/$elements/L2110_AMT02'},
                                  'amt03': {'$ref': '#/$elements/L2110_AMT03'}},
                   'required': ['amt01', 'amt02']},
         'maxItems': 12}
        segment_name = 'AMT'
    amt01: L2110_AMT01
    amt02: L2110_AMT02
    amt03: L2110_AMT03 | None


class L2110_QTY01(Element):
    """Quantity Qualifier"""
    class Schema:
        json = {'title': 'Quantity Qualifier',
         'usage': 'R',
         'description': 'xid=QTY01 data_ele=673',
         'position': 1,
         'type': {'allOf': [{'$ref': '#/$common/673'},
                            {'enum': ['NE', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']}]}}
        datatype = common.D_673
        codes = ['NE', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO']
        min_len = 2
        max_len = 2


class L2110_QTY02(Element):
    """Service Supplemental Quantity Count"""
    class Schema:
        json = {'title': 'Service Supplemental Quantity Count',
         'usage': 'R',
         'description': 'xid=QTY02 data_ele=380',
         'position': 2,
         'type': {'$ref': '#/$common/380'}}
        datatype = common.D_380
        min_len = 1
        max_len = 15


class L2110_C001(Composite):
    class Schema:
        json = {'title': 'Composite Unit of Measure',
         'usage': 'N',
         'description': 'xid=None name=Composite Unit of Measure refdes= data_ele=C001',
         'sequence': 3,
         'syntax': []}


class L2110_QTY04(Element):
    """Free-Form Message"""
    class Schema:
        json = {'title': 'Free-Form Message',
         'usage': 'N',
         'description': 'xid=QTY04 data_ele=61',
         'position': 4,
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
                   'position': 120,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'QTY'},
                                  'qty01': {'$ref': '#/$elements/L2110_QTY01'},
                                  'qty02': {'$ref': '#/$elements/L2110_QTY02'},
                                  'c001': {'$ref': '#/$elements/L2110_C001'},
                                  'qty04': {'$ref': '#/$elements/L2110_QTY04'}},
                   'required': ['qty01', 'qty02']},
         'maxItems': 6}
        segment_name = 'QTY'
    qty01: L2110_QTY01
    qty02: L2110_QTY02
    qty04: L2110_QTY04 | None


class L2110_LQ01(Element):
    """Code List Qualifier Code"""
    class Schema:
        json = {'title': 'Code List Qualifier Code',
         'usage': 'R',
         'description': 'xid=LQ01 data_ele=1270',
         'position': 1,
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
         'position': 2,
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
                   'position': 130,
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
                   'position': 70,
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
                   'position': 10,
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
    nm1: list[L2100_NM1]
    mia: L2100_MIA | None
    moa: L2100_MOA | None
    ref: list[L2100_REF] | None
    ref: list[L2100_REF] | None
    dtm: list[L2100_DTM] | None
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
                   'position': 3,
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
         'items': {'title': 'Table 2 - Detail',
                   'usage': 'S',
                   'description': 'xid=DETAIL name=Table 2 - Detail type=wrapper',
                   'position': 20,
                   'type': 'object',
                   'properties': {'l2000': {'$ref': '#/$segments/L2000'}}}}
    l2000: list[L2000] | None


class FOOTER_PLB01(Element):
    """Provider Identifier"""
    class Schema:
        json = {'title': 'Provider Identifier',
         'usage': 'R',
         'description': 'xid=PLB01 data_ele=127',
         'position': 1,
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
         'position': 2,
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
         'position': 1,
         'type': {'$ref': '#/$common/426'}}
        datatype = common.D_426
        min_len = 2
        max_len = 2


class FOOTER_PLB03_02(Element):
    """Provider Adjustment Identifier"""
    class Schema:
        json = {'title': 'Provider Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=PLB03-02 data_ele=127',
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_C042(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'R',
         'description': 'xid=None name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 3,
         'syntax': [],
         'type': 'object',
         'properties': {'plb03_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB03-01 data_ele=426',
                                     'position': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb03_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB03-02 data_ele=127',
                                     'position': 2,
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
         'position': 4,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_C042(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=None name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 5,
         'syntax': [],
         'type': 'object',
         'properties': {'plb05_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB05-01 data_ele=426',
                                     'position': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb05_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB05-02 data_ele=127',
                                     'position': 2,
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
         'position': 6,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_C042(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=None name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 7,
         'syntax': [],
         'type': 'object',
         'properties': {'plb07_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB07-01 data_ele=426',
                                     'position': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb07_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB07-02 data_ele=127',
                                     'position': 2,
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
         'position': 8,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_C042(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=None name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 9,
         'syntax': [],
         'type': 'object',
         'properties': {'plb09_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB09-01 data_ele=426',
                                     'position': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb09_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB09-02 data_ele=127',
                                     'position': 2,
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
         'position': 10,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_C042(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=None name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 11,
         'syntax': [],
         'type': 'object',
         'properties': {'plb11_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB11-01 data_ele=426',
                                     'position': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb11_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB11-02 data_ele=127',
                                     'position': 2,
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
         'position': 12,
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
         'position': 1,
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
         'position': 2,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class FOOTER_C042(Composite):
    class Schema:
        json = {'title': 'Adjustment Identifier',
         'usage': 'S',
         'description': 'xid=None name=Adjustment Identifier refdes= data_ele=C042',
         'sequence': 13,
         'syntax': [],
         'type': 'object',
         'properties': {'plb13_01': {'title': 'Adjustment Reason Code',
                                     'usage': 'R',
                                     'description': 'xid=PLB13-01 data_ele=426',
                                     'position': 1,
                                     'type': {'$ref': '#/$common/426'}},
                        'plb13_02': {'title': 'Provider Adjustment Identifier',
                                     'usage': 'S',
                                     'description': 'xid=PLB13-02 data_ele=127',
                                     'position': 2,
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
         'position': 14,
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
                   'position': 10,
                   'type': 'object',
                   'properties': {'xid': {'literal': 'PLB'},
                                  'plb01': {'$ref': '#/$elements/FOOTER_PLB01'},
                                  'plb02': {'$ref': '#/$elements/FOOTER_PLB02'},
                                  'c042': {'$ref': '#/$elements/FOOTER_C042'},
                                  'plb04': {'$ref': '#/$elements/FOOTER_PLB04'},
                                  'plb06': {'$ref': '#/$elements/FOOTER_PLB06'},
                                  'plb08': {'$ref': '#/$elements/FOOTER_PLB08'},
                                  'plb10': {'$ref': '#/$elements/FOOTER_PLB10'},
                                  'plb12': {'$ref': '#/$elements/FOOTER_PLB12'},
                                  'plb14': {'$ref': '#/$elements/FOOTER_PLB14'}},
                   'required': ['plb01', 'plb02', 'c042', 'plb04']}}
        segment_name = 'PLB'
    plb01: FOOTER_PLB01
    plb02: FOOTER_PLB02
    c042: FOOTER_C042
    plb04: FOOTER_PLB04
    c042: FOOTER_C042
    plb06: FOOTER_PLB06 | None
    c042: FOOTER_C042
    plb08: FOOTER_PLB08 | None
    c042: FOOTER_C042
    plb10: FOOTER_PLB10 | None
    c042: FOOTER_C042
    plb12: FOOTER_PLB12 | None
    c042: FOOTER_C042
    plb14: FOOTER_PLB14 | None


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 3 - Footer',
                   'usage': 'S',
                   'description': 'xid=FOOTER name=Table 3 - Footer type=wrapper',
                   'position': 30,
                   'type': 'object',
                   'properties': {'plb': {'$ref': '#/$segments/FOOTER_PLB'}}}}
    plb: list[FOOTER_PLB] | None


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
         'position': 50,
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


class MSG835(Message):
    """HIPAA Health Care Claim Payment/Advice X091-835"""
    class Schema:
        json = {'title': 'HIPAA Health Care Claim Payment/Advice X091-835',
         'description': 'xid=835 name=HIPAA Health Care Claim Payment/Advice X091-835',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
