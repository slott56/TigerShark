"""
270.4010.X092.A1
Created 2023-05-19 10:17:35.821155
"""
from .base import *
from .common import *


class ISA_LOOP_ISA(Segment):
    """Interchange Control Header"""
    _segment_name = 'ISA'
    
    isa01: Annotated[I01, Title('Authorization Information Qualifier'), Usage('R'), Position(1), Enumerated(*['00', '03'])]
    
    isa02: Annotated[I02, Title('Authorization Information'), Usage('R'), Position(2)]
    
    isa03: Annotated[I03, Title('Security Information Qualifier'), Usage('R'), Position(3), Enumerated(*['00', '01'])]
    
    isa04: Annotated[I04, Title('Security Information'), Usage('R'), Position(4)]
    
    isa05: Annotated[I05, Title('Interchange ID Qualifier'), Usage('R'), Position(5), Enumerated(*['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ'])]
    
    isa06: Annotated[I06, Title('Interchange Sender ID'), Usage('R'), Position(6)]
    
    isa07: Annotated[I05, Title('Interchange ID Qualifier'), Usage('R'), Position(7), Enumerated(*['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ'])]
    
    isa08: Annotated[I07, Title('Interchange Receiver ID'), Usage('R'), Position(8)]
    
    isa09: Annotated[I08, Title('Interchange Date'), Usage('R'), Position(9)]
    
    isa10: Annotated[I09, Title('Interchange Time'), Usage('R'), Position(10)]
    
    isa11: Annotated[I10, Title('Interchange Control Standards Identifier'), Usage('R'), Position(11), Enumerated(*['U'])]
    
    isa12: Annotated[I11, Title('Interchange Control Version Number'), Usage('R'), Position(12), Enumerated(*['00401'])]
    
    isa13: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(13)]
    
    isa14: Annotated[I13, Title('Acknowledgment Requested'), Usage('R'), Position(14), Enumerated(*['0', '1'])]
    
    isa15: Annotated[I14, Title('Usage Indicator'), Usage('R'), Position(15), Enumerated(*['P', 'T'])]
    
    isa16: Annotated[I15, Title('Component Element Separator'), Usage('R'), Position(16)]


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    _segment_name = 'GS'
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['HS'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010X092A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['270'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title('Hierarchical Structure Code'), Usage('R'), Position(1), Enumerated(*['0022'])]
    
    bht02: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(2), Enumerated(*['01', '13', '36'])]
    
    bht03: Annotated[D_127, Title('Submitter Transaction Identifier'), Usage('S'), Position(3)]
    
    bht04: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title('Transaction Set Creation Time'), Usage('R'), Position(5)]
    
    bht06: Annotated[D_640, Title('Transaction Type Code'), Usage('S'), Position(6), Enumerated(*['RT', 'RU'])]


class HEADER(Loop):
    
    bht: Annotated[HEADER_BHT, Title('Beginning of Hierarchical Transaction'), Usage('R'), Position(20), Required(True)]


class L2000A_HL(Segment):
    """Information Source Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('N'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['20'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2100A_NM1(Segment):
    """Information Source Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['2B', '36', 'GP', 'P5', 'PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Information Source Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Information Source First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Information Source Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Information Source Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '46', 'FI', 'NI', 'PI', 'XV', 'XX'])]
    
    nm109: Annotated[D_67, Title('Information Source Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100A(Loop):
    
    nm1: Annotated[L2100A_NM1, Title('Information Source Name'), Usage('R'), Position(30), Required(True)]


class L2000B_HL(Segment):
    """Information Receiver Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['21'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2100B_NM1(Segment):
    """Information Receiver Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['1P', '2B', '36', '80', 'FA', 'GP', 'P5', 'PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Information Receiver Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Information Receiver First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Information Receiver Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Information Receiver Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'FI', 'PI', 'PP', 'SV', 'XV', 'XX'])]
    
    nm109: Annotated[D_67, Title('Information Receiver Identification Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100B_C040(Composite):
    """Reference Identifier"""
    pass


class L2100B_REF(Segment):
    """Information Receiver Additional Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1C', '1D', '1J', '4A', 'CT', 'EL', 'EO', 'JD', 'N5', 'N7', 'Q4', 'SY', 'TJ', 'HPI'])]
    
    ref02: Annotated[D_127, Title('Information Receiver Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('License Number State Code'), Usage('S'), Position(3), Enumerated(*states)]


class L2100B_N3(Segment):
    """Information Receiver Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Information Receiver Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Information Receiver Additional Address Line'), Usage('S'), Position(2)]


class L2100B_N4(Segment):
    """Information Receiver City/State/Zip Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Information Receiver City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Information Receiver State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Information Receiver Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2100B_PER(Segment):
    """Information Receiver Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Information Receiver Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(3), Enumerated(*['ED', 'EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Information Receiver Communication Number'), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Information Receiver Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Information Receiver Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2100B_PRV(Segment):
    """Information Receiver Provider Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB', 'SK', 'SU'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Receiver Provider Specialty Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2100B(Loop):
    
    nm1: Annotated[L2100B_NM1, Title('Information Receiver Name'), Usage('R'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2100B_REF, Title('Information Receiver Additional Identification'), Usage('S'), Position(40), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(9)]
    
    n3: Annotated[L2100B_N3, Title('Information Receiver Address'), Usage('S'), Position(60), Required(True)]
    
    n4: Annotated[L2100B_N4, Title('Information Receiver City/State/Zip Code'), Usage('S'), Position(70), Required(True)]
    ItemPer: TypeAlias = Annotated[L2100B_PER, Title('Information Receiver Contact Information'), Usage('S'), Position(80), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(3)]
    
    prv: Annotated[L2100B_PRV, Title('Information Receiver Provider Information'), Usage('S'), Position(90), Required(True)]


class L2000C_HL(Segment):
    """Subscriber Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['22'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0', '1'])]


class L2000C_TRN(Segment):
    """Subscriber Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Trace Assigning Entity Identifier'), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title('Trace Assigning Entity Additional Identifier'), Usage('S'), Position(4)]


class L2100C_NM1(Segment):
    """Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Subscriber Last Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Subscriber First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Subscriber Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Subscriber Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Subscriber Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100C_C040(Composite):
    """Reference Identifier"""
    pass


class L2100C_REF(Segment):
    """Subscriber Additional Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['18', '1L', '1W', '49', '6P', 'A6', 'CT', 'EA', 'EJ', 'F6', 'GH', 'HJ', 'IG', 'N6', 'NQ', 'SY'])]
    
    ref02: Annotated[D_127, Title('Subscriber Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2100C_N3(Segment):
    """Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Subscriber Address Line 1'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Subscriber Address Line 2'), Usage('S'), Position(2)]


class L2100C_N4(Segment):
    """Subscriber City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Subscriber City Name'), Usage('S'), Position(1)]
    
    n402: Annotated[D_156, Title('Subscriber State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Subscriber Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2100C_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2100C_PRV(Segment):
    """Provider Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB', 'SK', 'SU'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['9K', 'D3', 'EI', 'HPI', 'SY', 'TJ', 'ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Identifier'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2100C_DMG(Segment):
    """Subscriber Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Subscriber Birth Date'), Usage('S'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Subscriber Gender Code'), Usage('S'), Position(3), Enumerated(*['F', 'M'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2100C_INS(Segment):
    """Subscriber Relationship"""
    _segment_name = 'INS'
    
    ins01: Annotated[D_1073, Title('Insured Indicator'), Usage('R'), Position(1), Enumerated(*['Y'])]
    
    ins02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['18'])]
    
    ins03: Annotated[D_875, Title('Maintenance Type Code'), Usage('N'), Position(3)]
    
    ins04: Annotated[D_1203, Title('Maintenance Reason Code'), Usage('N'), Position(4)]
    
    ins05: Annotated[D_1216, Title('Benefit Status Code'), Usage('N'), Position(5)]
    
    ins06: Annotated[D_1218, Title('Medicare Plan Code'), Usage('N'), Position(6)]
    
    ins07: Annotated[D_1219, Title('Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying'), Usage('N'), Position(7)]
    
    ins08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    ins09: Annotated[D_1220, Title('Student Status Code'), Usage('N'), Position(9)]
    
    ins10: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(10)]
    
    ins11: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(11)]
    
    ins12: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(12)]
    
    ins13: Annotated[D_1165, Title('Confidentiality Code'), Usage('N'), Position(13)]
    
    ins14: Annotated[D_19, Title('City Name'), Usage('N'), Position(14)]
    
    ins15: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(15)]
    
    ins16: Annotated[D_26, Title('Country Code'), Usage('N'), Position(16)]
    
    ins17: Annotated[D_1470, Title('Birth Sequence Number'), Usage('R'), Position(17)]


class L2100C_DTP(Segment):
    """Subscriber Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['102', '307', '435', '472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Date Time Period'), Usage('R'), Position(3)]


class L2110C_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    eq02_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ'])]
    
    eq02_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    eq02_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    eq02_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    eq02_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    eq02_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    eq02_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2110C_EQ(Segment):
    """Subscriber Eligibility or Benefit Inquiry Information"""
    _segment_name = 'EQ'
    
    eq01: Annotated[D_1365, Title('Service Type Code'), Usage('S'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BP', 'BQ', 'BR', 'BS'])]
    
    c003: Annotated[L2110C_C003, Title('Composite Medical Procedure Identifier'), Usage('S'), Position(2), Required(True)]
    
    eq03: Annotated[D_1207, Title('Benefit Coverage Level Code'), Usage('S'), Position(3), Enumerated(*['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO'])]
    
    eq04: Annotated[D_1336, Title('Insurance Type Code'), Usage('S'), Position(4), Enumerated(*['AP', 'C1', 'CO', 'GP', 'HM', 'HN', 'IP', 'MA', 'MB', 'MC', 'PR', 'PS', 'SP', 'WC'])]


class L2110C_AMT(Segment):
    """Subscriber Spend Down Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['R'])]
    
    amt02: Annotated[D_782, Title('Spend Down Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2110C_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2110C_III(Segment):
    """Subscriber Eligibility or Benefit Additional Inquiry Information"""
    _segment_name = 'III'
    
    iii01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF', 'BK', 'ZZ'])]
    
    iii02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    iii03: Annotated[D_1136, Title('Code Category'), Usage('N'), Position(3)]
    
    iii04: Annotated[D_933, Title('Free-Form Message Text'), Usage('N'), Position(4)]
    
    iii05: Annotated[D_380, Title('Quantity'), Usage('N'), Position(5)]
    
    iii07: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(7)]
    
    iii08: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(8)]
    
    iii09: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(9)]


class L2110C_C040(Composite):
    """Reference Identifier"""
    pass


class L2110C_REF(Segment):
    """Subscriber Additional Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2110C_DTP(Segment):
    """Subscriber Eligibility/Benefit Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['307', '435', '472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Date Time Period'), Usage('R'), Position(3)]


class L2110C(Loop):
    
    eq: Annotated[L2110C_EQ, Title('Subscriber Eligibility or Benefit Inquiry Information'), Usage('R'), Position(130)]
    
    amt: Annotated[L2110C_AMT, Title('Subscriber Spend Down Amount'), Usage('S'), Position(135), Required(True)]
    ItemIii: TypeAlias = Annotated[L2110C_III, Title('Subscriber Eligibility or Benefit Additional Inquiry Information'), Usage('S'), Position(170), Required(True)]
    iii: Annotated[list[ItemIii], MaxItems(10)]
    
    ref: Annotated[L2110C_REF, Title('Subscriber Additional Information'), Usage('S'), Position(190), Required(True)]
    
    dtp: Annotated[L2110C_DTP, Title('Subscriber Eligibility/Benefit Date'), Usage('S'), Position(200), Required(True)]


class L2100C(Loop):
    
    nm1: Annotated[L2100C_NM1, Title('Subscriber Name'), Usage('R'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2100C_REF, Title('Subscriber Additional Identification'), Usage('S'), Position(40), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(9)]
    
    n3: Annotated[L2100C_N3, Title('Subscriber Address'), Usage('S'), Position(60), Required(True)]
    
    n4: Annotated[L2100C_N4, Title('Subscriber City/State/ZIP Code'), Usage('S'), Position(70)]
    
    prv: Annotated[L2100C_PRV, Title('Provider Information'), Usage('S'), Position(90), Required(True)]
    
    dmg: Annotated[L2100C_DMG, Title('Subscriber Demographic Information'), Usage('S'), Position(100)]
    
    ins: Annotated[L2100C_INS, Title('Subscriber Relationship'), Usage('S'), Position(110), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2100C_DTP, Title('Subscriber Date'), Usage('S'), Position(120), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    ItemL2110C: TypeAlias = Annotated[L2110C, Title('Subscriber Eligibility or Benefit Inquiry Information'), Usage('S'), Position(130), Required(True)]
    l2110c: Annotated[list[ItemL2110C], MinItems(99)]


class L2000D_HL(Segment):
    """Dependent Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['23'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0'])]


class L2000D_TRN(Segment):
    """Dependent Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Trace Assigning Entity Identifier'), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title('Trace Assigning Entity Additional Identifier'), Usage('S'), Position(4)]


class L2100D_NM1(Segment):
    """Dependent Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['03'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Dependent Last Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Dependent First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Dependent Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Dependent Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100D_C040(Composite):
    """Reference Identifier"""
    pass


class L2100D_REF(Segment):
    """Dependent Additional Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['18', '1L', '6P', 'A6', 'CT', 'EA', 'EJ', 'F6', 'GH', 'HJ', 'IF', 'IG', 'N6', 'SY'])]
    
    ref02: Annotated[D_127, Title('Dependent Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2100D_N3(Segment):
    """Dependent Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Dependent Address Line 1'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Dependent Address Line 2'), Usage('S'), Position(2)]


class L2100D_N4(Segment):
    """Dependent City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Dependent City Name'), Usage('S'), Position(1)]
    
    n402: Annotated[D_156, Title('Dependent State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Dependent Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2100D_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2100D_PRV(Segment):
    """Provider Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AD', 'AT', 'BI', 'CO', 'CV', 'H', 'HH', 'LA', 'OT', 'P1', 'P2', 'PC', 'PE', 'R', 'RF', 'SB', 'SK', 'SU'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['9K', 'D3', 'EI', 'HPI', 'SY', 'TJ', 'ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Identifier'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2100D_DMG(Segment):
    """Dependent Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Dependent Birth Date'), Usage('S'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Dependent Gender Code'), Usage('S'), Position(3), Enumerated(*['F', 'M'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2100D_INS(Segment):
    """Dependent Relationship"""
    _segment_name = 'INS'
    
    ins01: Annotated[D_1073, Title('Insured Indicator'), Usage('R'), Position(1), Enumerated(*['N'])]
    
    ins02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '19', '34'])]
    
    ins03: Annotated[D_875, Title('Maintenance Type Code'), Usage('N'), Position(3)]
    
    ins04: Annotated[D_1203, Title('Maintenance Reason Code'), Usage('N'), Position(4)]
    
    ins05: Annotated[D_1216, Title('Benefit Status Code'), Usage('N'), Position(5)]
    
    ins06: Annotated[D_1218, Title('Medicare Plan Code'), Usage('N'), Position(6)]
    
    ins07: Annotated[D_1219, Title('Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying'), Usage('N'), Position(7)]
    
    ins08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    ins09: Annotated[D_1220, Title('Student Status Code'), Usage('N'), Position(9)]
    
    ins10: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(10)]
    
    ins11: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(11)]
    
    ins12: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(12)]
    
    ins13: Annotated[D_1165, Title('Confidentiality Code'), Usage('N'), Position(13)]
    
    ins14: Annotated[D_19, Title('City Name'), Usage('N'), Position(14)]
    
    ins15: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(15)]
    
    ins16: Annotated[D_26, Title('Country Code'), Usage('N'), Position(16)]
    
    ins17: Annotated[D_1470, Title('Birth Sequence Number'), Usage('S'), Position(17)]


class L2100D_DTP(Segment):
    """Dependent Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['102', '307', '435', '472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Date Time Period'), Usage('R'), Position(3)]


class L2110D_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    eq02_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'CJ', 'HC', 'ID', 'IV', 'N4', 'ZZ'])]
    
    eq02_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    eq02_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    eq02_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    eq02_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    eq02_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    eq02_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2110D_EQ(Segment):
    """Dependent Eligibility or Benefit Inquiry Information"""
    _segment_name = 'EQ'
    
    eq01: Annotated[D_1365, Title('Service Type Code'), Usage('S'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BP', 'BQ', 'BR', 'BS'])]
    
    c003: Annotated[L2110D_C003, Title('Composite Medical Procedure Identifier'), Usage('S'), Position(2), Required(True)]
    
    eq03: Annotated[D_1207, Title('Benefit Coverage Level Code'), Usage('S'), Position(3), Enumerated(*['CHD', 'DEP', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO'])]
    
    eq04: Annotated[D_1336, Title('Insurance Type Code'), Usage('S'), Position(4), Enumerated(*['AP', 'C1', 'CO', 'GP', 'HM', 'IP', 'MA', 'MB', 'MC', 'PR', 'PS', 'SP', 'WC'])]


class L2110D_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2110D_III(Segment):
    """Dependent Eligibility or Benefit Additional Inquiry Information"""
    _segment_name = 'III'
    
    iii01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF', 'BK', 'ZZ'])]
    
    iii02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    iii03: Annotated[D_1136, Title('Code Category'), Usage('N'), Position(3)]
    
    iii04: Annotated[D_933, Title('Free-Form Message Text'), Usage('N'), Position(4)]
    
    iii05: Annotated[D_380, Title('Quantity'), Usage('N'), Position(5)]
    
    iii07: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(7)]
    
    iii08: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(8)]
    
    iii09: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(9)]


class L2110D_C040(Composite):
    """Reference Identifier"""
    pass


class L2110D_REF(Segment):
    """Dependent Additional Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2110D_DTP(Segment):
    """Dependent Eligibility/Benefit Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['307', '435', '472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Date Time Period'), Usage('R'), Position(3)]


class L2110D(Loop):
    
    eq: Annotated[L2110D_EQ, Title('Dependent Eligibility or Benefit Inquiry Information'), Usage('R'), Position(130)]
    ItemIii: TypeAlias = Annotated[L2110D_III, Title('Dependent Eligibility or Benefit Additional Inquiry Information'), Usage('S'), Position(170), Required(True)]
    iii: Annotated[list[ItemIii], MaxItems(10)]
    
    ref: Annotated[L2110D_REF, Title('Dependent Additional Information'), Usage('S'), Position(190), Required(True)]
    
    dtp: Annotated[L2110D_DTP, Title('Dependent Eligibility/Benefit Date'), Usage('S'), Position(200), Required(True)]


class L2100D(Loop):
    
    nm1: Annotated[L2100D_NM1, Title('Dependent Name'), Usage('R'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2100D_REF, Title('Dependent Additional Identification'), Usage('S'), Position(40), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(9)]
    
    n3: Annotated[L2100D_N3, Title('Dependent Address'), Usage('S'), Position(60), Required(True)]
    
    n4: Annotated[L2100D_N4, Title('Dependent City/State/ZIP Code'), Usage('S'), Position(70)]
    
    prv: Annotated[L2100D_PRV, Title('Provider Information'), Usage('S'), Position(90), Required(True)]
    
    dmg: Annotated[L2100D_DMG, Title('Dependent Demographic Information'), Usage('S'), Position(100)]
    
    ins: Annotated[L2100D_INS, Title('Dependent Relationship'), Usage('S'), Position(110), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2100D_DTP, Title('Dependent Date'), Usage('S'), Position(120), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    ItemL2110D: TypeAlias = Annotated[L2110D, Title('Dependent Eligibility or Benefit Inquiry Information'), Usage('R'), Position(130), Required(True)]
    l2110d: Annotated[list[ItemL2110D], MinItems(99)]


class L2000D(Loop):
    
    hl: Annotated[L2000D_HL, Title('Dependent Level'), Usage('R'), Position(10), Required(True)]
    ItemTrn: TypeAlias = Annotated[L2000D_TRN, Title('Dependent Trace Number'), Usage('S'), Position(20), Required(True)]
    trn: Annotated[list[ItemTrn], MaxItems(2)]
    ItemL2100D: TypeAlias = Annotated[L2100D, Title('Dependent Name'), Usage('R'), Position(30), Required(True)]
    l2100d: Annotated[list[ItemL2100D], MinItems(1)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title('Subscriber Level'), Usage('R'), Position(10), Required(True)]
    ItemTrn: TypeAlias = Annotated[L2000C_TRN, Title('Subscriber Trace Number'), Usage('S'), Position(20), Required(True)]
    trn: Annotated[list[ItemTrn], MaxItems(2)]
    ItemL2100C: TypeAlias = Annotated[L2100C, Title('Subscriber Name'), Usage('R'), Position(30), Required(True)]
    l2100c: Annotated[list[ItemL2100C], MinItems(1)]
    ItemL2000D: TypeAlias = Annotated[L2000D, Title('Dependent Level'), Usage('S'), Position(40), Required(True)]
    l2000d: Annotated[list[ItemL2000D], MinItems(1)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title('Information Receiver Level'), Usage('R'), Position(10), Required(True)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title('Information Receiver Name'), Usage('R'), Position(30), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Subscriber Level'), Usage('R'), Position(40), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Information Source Level'), Usage('R'), Position(10), Required(True)]
    ItemL2100A: TypeAlias = Annotated[L2100A, Title('Information Source Name'), Usage('R'), Position(30), Required(True)]
    l2100a: Annotated[list[ItemL2100A], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Information Receiver Level'), Usage('R'), Position(40), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class DETAIL(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title('Information Source Level'), Usage('R'), Position(10), Required(True)]
    l2000a: Annotated[list[ItemL2000A], MinItems(1)]


class FOOTER(Loop):
    pass


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(10), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Table 1 - Header'), Usage('R'), Position(15), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('S'), Position(20), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('N'), Position(30)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(210), Required(True)]


class GS_LOOP_GE(Segment):
    """Functional Group Trailer"""
    _segment_name = 'GE'
    
    ge01: Annotated[D_97, Title('Number of Transaction Sets Included'), Usage('R'), Position(1)]
    
    ge02: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(2)]


class GS_LOOP(Loop):
    
    gs: Annotated[GS_LOOP_GS, Title('Functional Group Header'), Usage('R'), Position(10), Required(True)]
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title('Transaction Set Header'), Usage('R'), Position(20), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
    
    ge: Annotated[GS_LOOP_GE, Title('Functional Group Trailer'), Usage('R'), Position(30), Required(True)]


class ISA_LOOP_TA1(Segment):
    """Interchange Acknowledgement"""
    _segment_name = 'TA1'
    
    ta101: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(1)]
    
    ta102: Annotated[I08, Title('Interchange Date'), Usage('R'), Position(2)]
    
    ta103: Annotated[I09, Title('Interchange Time'), Usage('R'), Position(3)]
    
    ta104: Annotated[I17, Title('Interchange Acknowledgement Code'), Usage('R'), Position(4), Enumerated(*['A', 'E', 'R'])]
    
    ta105: Annotated[I18, Title('Interchange Note Code'), Usage('R'), Position(5), Enumerated(*['000', '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031'])]


class ISA_LOOP_IEA(Segment):
    """Interchange Control Trailer"""
    _segment_name = 'IEA'
    
    iea01: Annotated[I16, Title('Number of Included Functional Groups'), Usage('R'), Position(1)]
    
    iea02: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(2)]


class ISA_LOOP(Loop):
    
    isa: Annotated[ISA_LOOP_ISA, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    ItemGs_Loop: TypeAlias = Annotated[GS_LOOP, Title('Functional Group Header'), Usage('R'), Position(20), Required(True)]
    gs_loop: Annotated[list[ItemGs_Loop], MinItems(1)]
    
    ta1: Annotated[ISA_LOOP_TA1, Title('Interchange Acknowledgement'), Usage('S'), Position(20), Required(True)]
    
    iea: Annotated[ISA_LOOP_IEA, Title('Interchange Control Trailer'), Usage('R'), Position(30), Required(True)]


class MSG270(Message):
    """HIPAA Health Care Eligibility Inquiry X092A1-270"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
