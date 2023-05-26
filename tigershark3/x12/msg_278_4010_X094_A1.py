"""
278.4010.X094.A1
Created 2023-05-19 10:17:35.918200
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
    
    isa12: Annotated[I11, Title('Interchange Control Version Number'), Usage('R'), Position(12)]
    
    isa13: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(13)]
    
    isa14: Annotated[I13, Title('Acknowledgment Requested'), Usage('R'), Position(14), Enumerated(*['0', '1'])]
    
    isa15: Annotated[I14, Title('Usage Indicator'), Usage('R'), Position(15), Enumerated(*['P', 'T'])]
    
    isa16: Annotated[I15, Title('Component Element Separator'), Usage('R'), Position(16)]


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    _segment_name = 'GS'
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['HI'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010X094A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['278'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title('Hierarchical Structure Code'), Usage('R'), Position(1), Enumerated(*['0078'])]
    
    bht02: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(2), Enumerated(*['13'])]
    
    bht03: Annotated[D_127, Title('Submitter Transaction Identifier'), Usage('R'), Position(3)]
    
    bht04: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title('Transaction Set Creation Time'), Usage('R'), Position(5)]
    
    bht06: Annotated[D_640, Title('Transaction Type Code'), Usage('N'), Position(6)]


class HEADER(Loop):
    
    bht: Annotated[HEADER_BHT, Title('Beginning of Hierarchical Transaction'), Usage('R'), Position(20), Required(True)]


class L2000A_HL(Segment):
    """Utilization Management Organization (UMO) Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('N'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['20'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2010A_NM1(Segment):
    """Utilization Management Organizational (UMO) Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['X3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Utilization Management Organization (UMO) Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Utilization Management Organization (UMO) First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Utilization Management Organization (UMO) Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Utilization Management Organization (UMO) Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', '46', 'PI', 'XV', 'XX'])]
    
    nm109: Annotated[D_67, Title('Utilization Management Organization (UMO) Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010A(Loop):
    
    nm1: Annotated[L2010A_NM1, Title('Utilization Management Organizational (UMO) Name'), Usage('R'), Position(170), Required(True)]


class L2000B_HL(Segment):
    """Requester Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['21'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2010B_NM1(Segment):
    """Requester Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['1P', 'FA'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Requester Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Requester First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Requester Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Requester Name Suffix '), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', '46', 'XX'])]
    
    nm109: Annotated[D_67, Title('Requester Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010B_C040(Composite):
    """Reference Identifier"""
    pass


class L2010B_REF(Segment):
    """Requester Supplemental Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1G', '1J', 'CT', 'EI', 'N5', 'N7', 'SY', 'ZH'])]
    
    ref02: Annotated[D_127, Title('Requester Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010B_N3(Segment):
    """Requester Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Requester Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Requester Address Line'), Usage('S'), Position(2)]


class L2010B_N4(Segment):
    """Requester City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Requester City Name'), Usage('S'), Position(1)]
    
    n402: Annotated[D_156, Title('Requester State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Requester Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Requester Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010B_PER(Segment):
    """Requester Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Requester Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Requester Contact Communication Number'), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Requester Contact Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Requester Contact Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2010B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2010B_PRV(Segment):
    """Requester Provider Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AD', 'AS', 'AT', 'CO', 'CV', 'OP', 'OR', 'OT', 'PC', 'PE', 'RF'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2010B(Loop):
    
    nm1: Annotated[L2010B_NM1, Title('Requester Name'), Usage('R'), Position(170), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010B_REF, Title('Requester Supplemental Identification'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(8)]
    
    n3: Annotated[L2010B_N3, Title('Requester Address'), Usage('S'), Position(200), Required(True)]
    
    n4: Annotated[L2010B_N4, Title('Requester City/State/ZIP Code'), Usage('S'), Position(210)]
    
    per: Annotated[L2010B_PER, Title('Requester Contact Information'), Usage('S'), Position(220), Required(True)]
    
    prv: Annotated[L2010B_PRV, Title('Requester Provider Information'), Usage('S'), Position(240), Required(True)]


class L2000C_HL(Segment):
    """Subscriber Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['22'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2000C_TRN(Segment):
    """Patient Event Tracking Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Patient Event Tracking Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Trace Assigning Entity Identifier'), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title('Trace Assigning Entity Additional Identifier'), Usage('S'), Position(4)]


class L2000C_DTP(Segment):
    """Accident Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['439'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Accident Date'), Usage('R'), Position(3)]


class L2000C_DTP(Segment):
    """Last Menstrual Period Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['484'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Menstrual Period Date'), Usage('R'), Position(3)]


class L2000C_DTP(Segment):
    """Estimated Date of Birth"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['ABC'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Estimated Birth Date'), Usage('R'), Position(3)]


class L2000C_DTP(Segment):
    """Onset of Current Symptoms or Illness Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['431'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Onset Date'), Usage('R'), Position(3)]


class L2000C_C022(Composite):
    """Diagnosis 1"""
    
    hi01_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF', 'BJ', 'BK'])]
    
    hi01_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 2"""
    
    hi02_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF', 'BJ'])]
    
    hi02_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 3"""
    
    hi03_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi03_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 4"""
    
    hi04_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi04_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 5"""
    
    hi05_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi05_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 6"""
    
    hi06_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi06_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi06_4: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 7"""
    
    hi07_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi07_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 8"""
    
    hi08_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi08_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title('DIagnosis Date'), Usage('S'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 9"""
    
    hi09_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi09_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 10"""
    
    hi10_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi10_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 11"""
    
    hi11_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi11_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_C022(Composite):
    """Diagnosis 12"""
    
    hi12_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi12_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000C_HI(Segment):
    """Subscriber Diagnosis"""
    _segment_name = 'HI'
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 1'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 2'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 3'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 4'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 5'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 6'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 7'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 8'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 9'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 10'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 11'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2000C_C022, Title('Diagnosis 12'), Usage('S'), Position(12), Required(True)]


class L2000C_C002(Composite):
    """Actions Indicated"""
    pass


class L2000C_PWK(Segment):
    """Additional Patient Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', '48', '55', '59', '77', 'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR', 'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4', 'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX', 'VO'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Attachment Description'), Usage('S'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2010CA_NM1(Segment):
    """Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Subscriber Last Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Subscriber First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Subscriber Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Subscriber Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Subscriber Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010CA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010CA_REF(Segment):
    """Subscriber Supplemental Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1L', '1W', '6P', 'A6', 'EJ', 'F6', 'HJ', 'IG', 'N6', 'NQ', 'SY'])]
    
    ref02: Annotated[D_127, Title('Subscriber Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010CA_DMG(Segment):
    """Subscriber Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Subscriber Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Subscriber Gender Code'), Usage('S'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2010CA(Loop):
    
    nm1: Annotated[L2010CA_NM1, Title('Subscriber Name'), Usage('R'), Position(170), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010CA_REF, Title('Subscriber Supplemental Identification'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(9)]
    
    dmg: Annotated[L2010CA_DMG, Title('Subscriber Demographic Information'), Usage('S'), Position(250), Required(True)]


class L2000D_HL(Segment):
    """Dependent Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['23'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2000D_TRN(Segment):
    """Patient Event Tracking Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Patient Event Tracking Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Trace Assigning Entity Identifier'), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title('Trace Assigning Entity Additional Identifier'), Usage('S'), Position(4)]


class L2000D_DTP(Segment):
    """Accident Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['439'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Accident Date'), Usage('R'), Position(3)]


class L2000D_DTP(Segment):
    """Last Menstrual Period Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['484'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Menstrual Period Date'), Usage('R'), Position(3)]


class L2000D_DTP(Segment):
    """Estimated Date of Birth"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['ABC'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Estimated Birth Date'), Usage('R'), Position(3)]


class L2000D_DTP(Segment):
    """Onset of Current Symptoms or Illness Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['431'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Onset Date'), Usage('R'), Position(3)]


class L2000D_C022(Composite):
    """Diagnosis 1"""
    
    hi01_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF', 'BJ', 'BK'])]
    
    hi01_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 2"""
    
    hi02_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF', 'BJ'])]
    
    hi02_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 3"""
    
    hi03_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi03_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 4"""
    
    hi04_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi04_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 5"""
    
    hi05_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi05_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 6"""
    
    hi06_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi06_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 7"""
    
    hi07_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi07_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 8"""
    
    hi08_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi08_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 9"""
    
    hi09_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi09_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 10"""
    
    hi10_01: Annotated[D_1270, Title('DIagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi10_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 11"""
    
    hi11_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi11_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_C022(Composite):
    """Diagnosis 12"""
    
    hi12_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi12_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title('Diagnosis Date'), Usage('S'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2000D_HI(Segment):
    """Dependent Diagnosis"""
    _segment_name = 'HI'
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 1'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 2'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 3'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 4'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 5'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 6'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 7'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 8'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 9'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 10'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 11'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2000D_C022, Title('Diagnosis 12'), Usage('S'), Position(12), Required(True)]


class L2000D_C002(Composite):
    """Actions Indicated"""
    pass


class L2000D_PWK(Segment):
    """Additional Patient Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', '48', '55', '59', '77', 'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR', 'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4', 'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX', 'VO'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Attachment Description'), Usage('S'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2010DA_NM1(Segment):
    """Dependent Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Dependent Last Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Dependent First Name '), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Dependent  Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Dependent Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010DA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010DA_REF(Segment):
    """Dependent Supplemental Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['A6', 'EJ', 'SY'])]
    
    ref02: Annotated[D_127, Title('Dependent Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010DA_DMG(Segment):
    """Dependent Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Dependent Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Dependent Gender Code'), Usage('S'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2010DA_INS(Segment):
    """Dependent Relationship"""
    _segment_name = 'INS'
    
    ins01: Annotated[D_1073, Title('Insured Indicator'), Usage('R'), Position(1), Enumerated(*['N'])]
    
    ins02: Annotated[D_1069, Title('Relationship to Insured Code'), Usage('R'), Position(2), Enumerated(*['01', '04', '05', '07', '09', '10', '15', '17', '19', '20', '21', '22', '23', '24', '29', '32', '33', '34', '36', '39', '40', '41', '43', '53', 'G8'])]
    
    ins03: Annotated[D_875, Title('Maintenance Type Code'), Usage('N'), Position(3)]
    
    ins04: Annotated[D_1203, Title('Maintenance Reason Code'), Usage('N'), Position(4)]
    
    ins05: Annotated[D_1216, Title('Benefit Status Code'), Usage('N'), Position(5)]
    
    ins06: Annotated[D_1218, Title('Medicare Plan Code'), Usage('N'), Position(6)]
    
    ins07: Annotated[D_1219, Title('Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event Code'), Usage('N'), Position(7)]
    
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


class L2010DA(Loop):
    
    nm1: Annotated[L2010DA_NM1, Title('Dependent Name'), Usage('R'), Position(170), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010DA_REF, Title('Dependent Supplemental Identification'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]
    
    dmg: Annotated[L2010DA_DMG, Title('Dependent Demographic Information'), Usage('S'), Position(250), Required(True)]
    
    ins: Annotated[L2010DA_INS, Title('Dependent Relationship'), Usage('S'), Position(260), Required(True)]


class L2000E_HL(Segment):
    """Service Provider Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['19'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2000E_MSG(Segment):
    """Message Text"""
    _segment_name = 'MSG'
    
    msg01: Annotated[D_933, Title('Free Form Message Text'), Usage('R'), Position(1)]
    
    msg02: Annotated[D_934, Title('Printer Carriage Control Code'), Usage('N'), Position(2)]
    
    msg03: Annotated[D_1470, Title('Number'), Usage('N'), Position(3)]


class L2010E_NM1(Segment):
    """Service Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['1T', 'FA', 'SJ'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Service Provider Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Service Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Service Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Service Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['24', '34', '46', 'XX'])]
    
    nm109: Annotated[D_67, Title('Service Provider Idenifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010E_C040(Composite):
    """Reference Identifier"""
    pass


class L2010E_REF(Segment):
    """Service Provider Supplemental Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1G', '1J', 'EI', 'N5', 'N7', 'SY', 'ZH'])]
    
    ref02: Annotated[D_127, Title('Service Provider Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010E_N3(Segment):
    """Service Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Service Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Service Provider Address Line'), Usage('S'), Position(2)]


class L2010E_N4(Segment):
    """Service Provider City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Service Provider City Name'), Usage('S'), Position(1)]
    
    n402: Annotated[D_156, Title('Service Provider State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Service Provider Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Service Provider Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010E_PER(Segment):
    """Service Provider Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Service Provider Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Service Provider Contact Communication Number'), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Service Provider Contact Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Service Provider Contact Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2010E_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2010E_PRV(Segment):
    """Service Provider Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AD', 'AS', 'AT', 'CO', 'CV', 'OP', 'OR', 'OT', 'PC', 'PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2010E(Loop):
    
    nm1: Annotated[L2010E_NM1, Title('Service Provider Name'), Usage('R'), Position(170), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010E_REF, Title('Service Provider Supplemental Identification'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(7)]
    
    n3: Annotated[L2010E_N3, Title('Service Provider Address'), Usage('S'), Position(200), Required(True)]
    
    n4: Annotated[L2010E_N4, Title('Service Provider City/State/ZIP Code'), Usage('S'), Position(210)]
    
    per: Annotated[L2010E_PER, Title('Service Provider Contact Information'), Usage('S'), Position(220), Required(True)]
    
    prv: Annotated[L2010E_PRV, Title('Service Provider Information'), Usage('S'), Position(240), Required(True)]


class L2000F_HL(Segment):
    """Service Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['SS'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0'])]


class L2000F_TRN(Segment):
    """Service Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Service Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Trace Assigning Entity Identifier'), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title('Trace Assigning Entity Additional Identifier'), Usage('S'), Position(4)]


class L2000F_C023(Composite):
    """Health Care Service Location Information"""
    
    um04_01: Annotated[D_1331, Title('Facility Type Code'), Usage('R'), Position(1)]
    
    um04_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('R'), Position(2), Enumerated(*['A', 'B'])]
    
    um04_03: Annotated[D_1325, Title('Claim Frequency Type Code'), Usage('N'), Position(3)]


class L2000F_C024(Composite):
    """Related Causes Information"""
    
    um05_01: Annotated[D_1362, Title('Related Causes Code'), Usage('R'), Position(1), Enumerated(*['AA', 'AP', 'EM'])]
    
    um05_02: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(2), Enumerated(*['AP', 'EM'])]
    
    um05_03: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(3), Enumerated(*['AP'])]
    
    um05_04: Annotated[D_156, Title('State Code'), Usage('S'), Position(4), Enumerated(*states)]
    
    um05_05: Annotated[D_26, Title('Country Code'), Usage('S'), Position(5), Enumerated(*country)]


class L2000F_UM(Segment):
    """Health Care Services Review Information"""
    _segment_name = 'UM'
    
    um01: Annotated[D_1525, Title('Request Category Code'), Usage('R'), Position(1), Enumerated(*['AR', 'HS', 'SC'])]
    
    um02: Annotated[D_1322, Title('Certification Type Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', 'I', 'R', 'S'])]
    
    um03: Annotated[D_1365, Title('Service Type Code'), Usage('S'), Position(3), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '12', '14', '15', '16', '17', '18', '20', '21', '23', '24', '25', '26', '27', '28', '33', '34', '35', '36', '37', '38', '39', '40', '42', '44', '45', '46', '48', '50', '51', '52', '53', '54', '56', '57', '58', '59', '61', '62', '63', '64', '65', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '82', '83', '84', '85', '86', '93', '94', '95', '98', '99', 'A0', 'A1', 'A2', 'A3', 'A4', 'A6', 'A7', 'A8', 'A9', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AI', 'AJ', 'AK', 'AL', 'AR', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BS'])]
    
    c023: Annotated[L2000F_C023, Title('Health Care Service Location Information'), Usage('S'), Position(4), Required(True)]
    
    c024: Annotated[L2000F_C024, Title('Related Causes Information'), Usage('S'), Position(5), Required(True)]
    
    um06: Annotated[D_1338, Title('Level of Service Code'), Usage('S'), Position(6), Enumerated(*['03', 'U'])]
    
    um07: Annotated[D_1213, Title('Current Health Condition Code'), Usage('S'), Position(7), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', 'F', 'G', 'P'])]
    
    um08: Annotated[D_923, Title('Prognosis Code'), Usage('S'), Position(8), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8'])]
    
    um09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['A', 'I', 'M', 'O', 'Y'])]
    
    um10: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(10), Enumerated(*['1', '2', '3', '4', '7', '8', '10', '11', '15', '16', '17'])]


class L2000F_C040(Composite):
    """Reference Identifier"""
    pass


class L2000F_REF(Segment):
    """Previous Certification Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BB'])]
    
    ref02: Annotated[D_127, Title('Previous Certification Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2000F_DTP(Segment):
    """Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Service Date'), Usage('R'), Position(3)]


class L2000F_DTP(Segment):
    """Admission Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Admission Date'), Usage('R'), Position(3)]


class L2000F_DTP(Segment):
    """Discharge Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Discharge Date'), Usage('R'), Position(3)]


class L2000F_DTP(Segment):
    """Surgery Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['456'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Surgery Date'), Usage('R'), Position(3)]


class L2000F_C022(Composite):
    """Procedure Code 1"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi01_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi01_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 2"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi02_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi02_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 3"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi03_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi03_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 4"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi04_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi04_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 5"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi05_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi05_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 6"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi06_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi06_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 7"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi07_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi07_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 8"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi08_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi08_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 9"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi09_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi09_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 10"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi10_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi10_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 11"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi11_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi11_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 12"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi12_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi12_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_HI(Segment):
    """Procedures"""
    _segment_name = 'HI'
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 1'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 2'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 3'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 4'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 5'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 6'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 7'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 8'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 9'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 10'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 11'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 12'), Usage('S'), Position(12), Required(True)]


class L2000F_HSD(Segment):
    """Health Care Services Delivery"""
    _segment_name = 'HSD'
    
    hsd01: Annotated[D_673, Title('Quantity Qualifier'), Usage('S'), Position(1), Enumerated(*['DY', 'FL', 'HS', 'MN', 'VS'])]
    
    hsd02: Annotated[D_380, Title('Service Unit Count'), Usage('S'), Position(2)]
    
    hsd03: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(3), Enumerated(*['DA', 'MO', 'WK'])]
    
    hsd04: Annotated[D_1167, Title('Sample Selection Modulus'), Usage('S'), Position(4)]
    
    hsd05: Annotated[D_615, Title('Time Period Qualifier'), Usage('S'), Position(5), Enumerated(*['6', '7', '21', '26', '27', '34', '35'])]
    
    hsd06: Annotated[D_616, Title('Period Count'), Usage('S'), Position(6)]
    
    hsd07: Annotated[D_678, Title('Ship,Delivery or Calendar Pattern Code'), Usage('S'), Position(7), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'SA', 'SB', 'SC', 'SD', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ', 'T', 'U', 'V', 'W', 'X', 'Y'])]
    
    hsd08: Annotated[D_679, Title('Delivery Pattern Time Code'), Usage('S'), Position(8), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Y'])]


class L2000F_CRC(Segment):
    """Patient Condition Information"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Condition Code Category'), Usage('R'), Position(1), Enumerated(*['07', '08', '11', '75', '76', '77'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]


class L2000F_CL1(Segment):
    """Institutional Claim Code"""
    _segment_name = 'CL1'
    
    cl101: Annotated[D_1315, Title('Admission Type Code'), Usage('S'), Position(1)]
    
    cl102: Annotated[D_1314, Title('Admission Source Code'), Usage('S'), Position(2)]
    
    cl103: Annotated[D_1352, Title('Patient Status Code'), Usage('S'), Position(3)]
    
    cl104: Annotated[D_1345, Title('Nursing Home Residential Status Code'), Usage('S'), Position(4), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9'])]


class L2000F_CR1(Segment):
    """Ambulance Transport Information"""
    _segment_name = 'CR1'
    
    cr101: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(1), Enumerated(*['KG', 'LB'])]
    
    cr102: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(2)]
    
    cr103: Annotated[D_1316, Title('Ambulance Transport Code'), Usage('R'), Position(3), Enumerated(*['I', 'R', 'T', 'X'])]
    
    cr104: Annotated[D_1317, Title('Ambulance Transport Reason Code'), Usage('R'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr105: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(5), Enumerated(*['DH', 'DK'])]
    
    cr106: Annotated[D_380, Title('Transport Distance'), Usage('S'), Position(6)]
    
    cr107: Annotated[D_166, Title('Ambulance Trip Origin Address'), Usage('S'), Position(7)]
    
    cr108: Annotated[D_166, Title('Ambulance Trip Destination Address'), Usage('S'), Position(8)]
    
    cr109: Annotated[D_352, Title('Round Trip Purpose Description'), Usage('S'), Position(9)]
    
    cr110: Annotated[D_352, Title('Stretcher Purpose Description'), Usage('S'), Position(10)]


class L2000F_CR2(Segment):
    """Spinal Manipulation Service Information"""
    _segment_name = 'CR2'
    
    cr201: Annotated[D_609, Title('Treatment Series Number'), Usage('S'), Position(1)]
    
    cr202: Annotated[D_380, Title('Treatment Count'), Usage('S'), Position(2)]
    
    cr203: Annotated[D_1367, Title('Subluxation Level Code'), Usage('S'), Position(3), Enumerated(*['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO', 'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA', 'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9'])]
    
    cr204: Annotated[D_1367, Title('Subluxation Level Code'), Usage('S'), Position(4), Enumerated(*['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO', 'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA', 'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9'])]
    
    cr205: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(5), Enumerated(*['DA', 'MO', 'WK', 'YR'])]
    
    cr206: Annotated[D_380, Title('Treatment Period Count'), Usage('S'), Position(6)]
    
    cr207: Annotated[D_380, Title('Monthly Treatment Count'), Usage('S'), Position(7)]
    
    cr208: Annotated[D_1342, Title('Patient Condition Code'), Usage('S'), Position(8), Enumerated(*['A', 'C', 'D', 'E', 'F', 'G', 'M'])]
    
    cr209: Annotated[D_1073, Title('Complication Indicator'), Usage('S'), Position(9), Enumerated(*['N', 'Y'])]
    
    cr210: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(10)]
    
    cr211: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(11)]
    
    cr212: Annotated[D_1073, Title('X-ray Availability Indicator'), Usage('R'), Position(12), Enumerated(*['N', 'Y'])]


class L2000F_CR5(Segment):
    """Home Oxygen Therapy Information"""
    _segment_name = 'CR5'
    
    cr501: Annotated[D_1322, Title('Certification Type Code'), Usage('N'), Position(1)]
    
    cr502: Annotated[D_380, Title('Quantity'), Usage('N'), Position(2)]
    
    cr503: Annotated[D_1348, Title('Oxygen Equipment Type Code'), Usage('S'), Position(3), Enumerated(*['A', 'B', 'C', 'D', 'E', 'O'])]
    
    cr504: Annotated[D_1348, Title('Oxygen Equipment Type Code'), Usage('S'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E', 'O'])]
    
    cr505: Annotated[D_352, Title('Equipment Reason Description'), Usage('S'), Position(5)]
    
    cr506: Annotated[D_380, Title('Oxygen Flow Rate'), Usage('R'), Position(6)]
    
    cr507: Annotated[D_380, Title('Daily Oxygen Use Count'), Usage('S'), Position(7)]
    
    cr508: Annotated[D_380, Title('Oxygen Use Period Hour Count'), Usage('S'), Position(8)]
    
    cr509: Annotated[D_352, Title('Respiratory Therapist Order Text'), Usage('S'), Position(9)]
    
    cr510: Annotated[D_380, Title('Arterial Blood Gas Quantity'), Usage('S'), Position(10)]
    
    cr511: Annotated[D_380, Title('Oxygen Saturation Quantity'), Usage('S'), Position(11)]
    
    cr512: Annotated[D_1349, Title('Oxygen Test Condition Code'), Usage('R'), Position(12), Enumerated(*['E', 'N', 'O', 'R', 'S', 'W', 'X'])]
    
    cr513: Annotated[D_1350, Title('Oxygen Test Findings Code'), Usage('S'), Position(13), Enumerated(*['1', '2', '3'])]
    
    cr514: Annotated[D_1350, Title('Oxygen Test Findings Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3'])]
    
    cr515: Annotated[D_1350, Title('Oxygen Test Findings Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3'])]
    
    cr516: Annotated[D_380, Title('Portable Oxygen System Flow Rate'), Usage('S'), Position(16)]
    
    cr517: Annotated[D_1382, Title('Oxygen Delivery System Code'), Usage('R'), Position(17), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr518: Annotated[D_1348, Title('Oxygen Equipment Type Code'), Usage('S'), Position(18), Enumerated(*['A', 'B', 'C', 'D', 'E', 'O'])]


class L2000F_CR6(Segment):
    """Home Health Care Information"""
    _segment_name = 'CR6'
    
    cr601: Annotated[D_923, Title('Prognosis Code'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8'])]
    
    cr602: Annotated[D_373, Title('Service From Date'), Usage('R'), Position(2)]
    
    cr603: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['RD8'])]
    
    cr604: Annotated[D_1251, Title('Home Health Certification Period'), Usage('S'), Position(4)]
    
    cr605: Annotated[D_373, Title('Date'), Usage('N'), Position(5)]
    
    cr606: Annotated[D_1073, Title('Skilled Nursing Facility Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'U', 'Y'])]
    
    cr607: Annotated[D_1073, Title('Medicare Coverage Indicator'), Usage('R'), Position(7), Enumerated(*['N', 'U', 'Y'])]
    
    cr608: Annotated[D_1322, Title('Certification Type Code'), Usage('R'), Position(8), Enumerated(*['1', '2', '3', '4', 'I', 'R', 'S'])]
    
    cr609: Annotated[D_373, Title('Surgery Date'), Usage('S'), Position(9)]
    
    cr610: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(10), Enumerated(*['HC', 'ID'])]
    
    cr611: Annotated[D_1137, Title('Surgical Procedure Code'), Usage('S'), Position(11)]
    
    cr612: Annotated[D_373, Title('Physician Order Date'), Usage('S'), Position(12)]
    
    cr613: Annotated[D_373, Title('Last Visit Date'), Usage('S'), Position(13)]
    
    cr614: Annotated[D_373, Title('Physician Contact Date'), Usage('S'), Position(14)]
    
    cr615: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(15), Enumerated(*['RD8'])]
    
    cr616: Annotated[D_1251, Title('Last Admission Period'), Usage('S'), Position(16)]
    
    cr617: Annotated[D_1384, Title('Patient Discharge Facility Type Code'), Usage('S'), Position(17), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M', 'O', 'P', 'R', 'S', 'T'])]
    
    cr618: Annotated[D_373, Title('Date'), Usage('N'), Position(18)]
    
    cr619: Annotated[D_373, Title('Date'), Usage('N'), Position(19)]
    
    cr620: Annotated[D_373, Title('Date'), Usage('N'), Position(20)]
    
    cr621: Annotated[D_373, Title('Date'), Usage('N'), Position(21)]


class L2000F_C002(Composite):
    """Actions Indicated"""
    pass


class L2000F_PWK(Segment):
    """Additional Service Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', '48', '55', '59', '77', 'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR', 'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4', 'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX', 'VO'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Attachment Description'), Usage('S'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2000F_MSG(Segment):
    """Message Text"""
    _segment_name = 'MSG'
    
    msg01: Annotated[D_933, Title('Free Form Message Text'), Usage('R'), Position(1)]
    
    msg02: Annotated[D_934, Title('Printer Carriage Control Code'), Usage('N'), Position(2)]
    
    msg03: Annotated[D_1470, Title('Number'), Usage('N'), Position(3)]


class L2000F(Loop):
    
    hl: Annotated[L2000F_HL, Title('Service Level'), Usage('R'), Position(10), Required(True)]
    ItemTrn: TypeAlias = Annotated[L2000F_TRN, Title('Service Trace Number'), Usage('S'), Position(20), Required(True)]
    trn: Annotated[list[ItemTrn], MaxItems(2)]
    
    um: Annotated[L2000F_UM, Title('Health Care Services Review Information'), Usage('R'), Position(40), Required(True)]
    
    ref: Annotated[L2000F_REF, Title('Previous Certification Identification'), Usage('S'), Position(60), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Service Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Admission Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Discharge Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Surgery Date'), Usage('S'), Position(70), Required(True)]
    
    hi: Annotated[L2000F_HI, Title('Procedures'), Usage('S'), Position(80), Required(True)]
    
    hsd: Annotated[L2000F_HSD, Title('Health Care Services Delivery'), Usage('S'), Position(90)]
    ItemCrc: TypeAlias = Annotated[L2000F_CRC, Title('Patient Condition Information'), Usage('S'), Position(100), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(6)]
    
    cl1: Annotated[L2000F_CL1, Title('Institutional Claim Code'), Usage('S'), Position(110)]
    
    cr1: Annotated[L2000F_CR1, Title('Ambulance Transport Information'), Usage('S'), Position(120), Required(True)]
    
    cr2: Annotated[L2000F_CR2, Title('Spinal Manipulation Service Information'), Usage('S'), Position(130), Required(True)]
    
    cr5: Annotated[L2000F_CR5, Title('Home Oxygen Therapy Information'), Usage('S'), Position(140), Required(True)]
    
    cr6: Annotated[L2000F_CR6, Title('Home Health Care Information'), Usage('S'), Position(150), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2000F_PWK, Title('Additional Service Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    msg: Annotated[L2000F_MSG, Title('Message Text'), Usage('S'), Position(160), Required(True)]


class L2000E(Loop):
    
    hl: Annotated[L2000E_HL, Title('Service Provider Level'), Usage('R'), Position(10), Required(True)]
    
    msg: Annotated[L2000E_MSG, Title('Message Text'), Usage('S'), Position(160), Required(True)]
    ItemL2010E: TypeAlias = Annotated[L2010E, Title('Service Provider Name'), Usage('R'), Position(170), Required(True)]
    l2010e: Annotated[list[ItemL2010E], MinItems(3)]
    ItemL2000F: TypeAlias = Annotated[L2000F, Title('Service Level'), Usage('R'), Position(180), Required(True)]
    l2000f: Annotated[list[ItemL2000F], MinItems(1)]


class L2000D(Loop):
    
    hl: Annotated[L2000D_HL, Title('Dependent Level'), Usage('R'), Position(10), Required(True)]
    ItemTrn: TypeAlias = Annotated[L2000D_TRN, Title('Patient Event Tracking Number'), Usage('S'), Position(20), Required(True)]
    trn: Annotated[list[ItemTrn], MaxItems(2)]
    
    dtp: Annotated[L2000D_DTP, Title('Accident Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000D_DTP, Title('Last Menstrual Period Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000D_DTP, Title('Estimated Date of Birth'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000D_DTP, Title('Onset of Current Symptoms or Illness Date'), Usage('S'), Position(70), Required(True)]
    
    hi: Annotated[L2000D_HI, Title('Dependent Diagnosis'), Usage('S'), Position(80), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2000D_PWK, Title('Additional Patient Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    ItemL2010Da: TypeAlias = Annotated[L2010DA, Title('Dependent Name'), Usage('R'), Position(170), Required(True)]
    l2010da: Annotated[list[ItemL2010Da], MinItems(1)]
    ItemL2000E: TypeAlias = Annotated[L2000E, Title('Service Provider Level'), Usage('R'), Position(180), Required(True)]
    l2000e: Annotated[list[ItemL2000E], MinItems(1)]


class L2000E_HL(Segment):
    """Service Provider Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['19'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2000E_MSG(Segment):
    """Message Text"""
    _segment_name = 'MSG'
    
    msg01: Annotated[D_933, Title('Free Form Message Text'), Usage('R'), Position(1)]
    
    msg02: Annotated[D_934, Title('Printer Carriage Control Code'), Usage('N'), Position(2)]
    
    msg03: Annotated[D_1470, Title('Number'), Usage('N'), Position(3)]


class L2010E_NM1(Segment):
    """Service Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['1T', 'FA', 'SJ'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Service Provider Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Service Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Service Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Service Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['24', '34', '46', 'XX'])]
    
    nm109: Annotated[D_67, Title('Service Provider Idenifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010E_C040(Composite):
    """Reference Identifier"""
    pass


class L2010E_REF(Segment):
    """Service Provider Supplemental Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1G', '1J', 'EI', 'N5', 'N7', 'SY', 'ZH'])]
    
    ref02: Annotated[D_127, Title('Service Provider Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010E_N3(Segment):
    """Service Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Service Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Service Provider Address Line'), Usage('S'), Position(2)]


class L2010E_N4(Segment):
    """Service Provider City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Service Provider City Name'), Usage('S'), Position(1)]
    
    n402: Annotated[D_156, Title('Service Provider State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Service Provider Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Service Provider Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010E_PER(Segment):
    """Service Provider Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Service Provider Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Service Provider Contact Communication Number'), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Service Provider Contact Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Service Provider Contact Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2010E_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2010E_PRV(Segment):
    """Service Provider Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AD', 'AS', 'AT', 'CO', 'CV', 'OP', 'OR', 'OT', 'PC', 'PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2010E(Loop):
    
    nm1: Annotated[L2010E_NM1, Title('Service Provider Name'), Usage('R'), Position(170), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010E_REF, Title('Service Provider Supplemental Identification'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(7)]
    
    n3: Annotated[L2010E_N3, Title('Service Provider Address'), Usage('S'), Position(200), Required(True)]
    
    n4: Annotated[L2010E_N4, Title('Service Provider City/State/ZIP Code'), Usage('S'), Position(210)]
    
    per: Annotated[L2010E_PER, Title('Service Provider Contact Information'), Usage('S'), Position(220), Required(True)]
    
    prv: Annotated[L2010E_PRV, Title('Service Provider Information'), Usage('S'), Position(240), Required(True)]


class L2000F_HL(Segment):
    """Service Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['SS'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0'])]


class L2000F_TRN(Segment):
    """Service Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Service Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Trace Assigning Entity Identifier'), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title('Trace Assigning Entity Additional Identifier'), Usage('S'), Position(4)]


class L2000F_C023(Composite):
    """Health Care Service Location Information"""
    
    um04_01: Annotated[D_1331, Title('Facility Type Code'), Usage('R'), Position(1)]
    
    um04_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('R'), Position(2), Enumerated(*['A', 'B'])]
    
    um04_03: Annotated[D_1325, Title('Claim Frequency Type Code'), Usage('N'), Position(3)]


class L2000F_C024(Composite):
    """Related Causes Information"""
    
    um05_01: Annotated[D_1362, Title('Related Causes Code'), Usage('R'), Position(1), Enumerated(*['AA', 'AP', 'EM'])]
    
    um05_02: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(2), Enumerated(*['AP', 'EM'])]
    
    um05_03: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(3), Enumerated(*['AP'])]
    
    um05_04: Annotated[D_156, Title('State Code'), Usage('S'), Position(4), Enumerated(*states)]
    
    um05_05: Annotated[D_26, Title('Country Code'), Usage('S'), Position(5), Enumerated(*country)]


class L2000F_UM(Segment):
    """Health Care Services Review Information"""
    _segment_name = 'UM'
    
    um01: Annotated[D_1525, Title('Request Category Code'), Usage('R'), Position(1), Enumerated(*['AR', 'HS', 'SC'])]
    
    um02: Annotated[D_1322, Title('Certification Type Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', 'I', 'R', 'S'])]
    
    um03: Annotated[D_1365, Title('Service Type Code'), Usage('S'), Position(3), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '12', '14', '15', '16', '17', '18', '20', '21', '23', '24', '25', '26', '27', '28', '33', '34', '35', '36', '37', '38', '39', '40', '42', '44', '45', '46', '48', '50', '51', '52', '53', '54', '56', '57', '58', '59', '61', '62', '63', '64', '65', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '82', '83', '84', '85', '86', '93', '94', '95', '98', '99', 'A0', 'A1', 'A2', 'A3', 'A4', 'A6', 'A7', 'A8', 'A9', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AI', 'AJ', 'AK', 'AL', 'AR', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BS'])]
    
    c023: Annotated[L2000F_C023, Title('Health Care Service Location Information'), Usage('S'), Position(4), Required(True)]
    
    c024: Annotated[L2000F_C024, Title('Related Causes Information'), Usage('S'), Position(5), Required(True)]
    
    um06: Annotated[D_1338, Title('Level of Service Code'), Usage('S'), Position(6), Enumerated(*['03', 'U'])]
    
    um07: Annotated[D_1213, Title('Current Health Condition Code'), Usage('S'), Position(7), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', 'F', 'G', 'P'])]
    
    um08: Annotated[D_923, Title('Prognosis Code'), Usage('S'), Position(8), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8'])]
    
    um09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['A', 'I', 'M', 'O', 'Y'])]
    
    um10: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(10), Enumerated(*['1', '2', '3', '4', '7', '8', '10', '11', '15', '16', '17'])]


class L2000F_C040(Composite):
    """Reference Identifier"""
    pass


class L2000F_REF(Segment):
    """Previous Certification Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BB'])]
    
    ref02: Annotated[D_127, Title('Previous Certification Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2000F_DTP(Segment):
    """Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Service Date'), Usage('R'), Position(3)]


class L2000F_DTP(Segment):
    """Admission Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Admission Date'), Usage('R'), Position(3)]


class L2000F_DTP(Segment):
    """Discharge Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Discharge Date'), Usage('R'), Position(3)]


class L2000F_DTP(Segment):
    """Surgery Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['456'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Proposed or Actual Surgery Date'), Usage('R'), Position(3)]


class L2000F_C022(Composite):
    """Procedure Code 1"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi01_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi01_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 2"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi02_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi02_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 3"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi03_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi03_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 4"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi04_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi04_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 5"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi05_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi05_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 6"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi06_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi06_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 7"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi07_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi07_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 8"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi08_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi08_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 9"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi09_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi09_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 10"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi10_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi10_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 11"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi11_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi11_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_C022(Composite):
    """Procedure Code 12"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ABR', 'BO', 'BQ', 'JP', 'NDC', 'ZZ'])]
    
    hi12_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8', 'RD8'])]
    
    hi12_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Procedure Monetary Amount'), Usage('S'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Procedure Quantity'), Usage('S'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version, Release, or Industry Identifier'), Usage('S'), Position(7)]


class L2000F_HI(Segment):
    """Procedures"""
    _segment_name = 'HI'
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 1'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 2'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 3'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 4'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 5'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 6'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 7'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 8'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 9'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 10'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 11'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2000F_C022, Title('Procedure Code 12'), Usage('S'), Position(12), Required(True)]


class L2000F_HSD(Segment):
    """Health Care Services Delivery"""
    _segment_name = 'HSD'
    
    hsd01: Annotated[D_673, Title('Quantity Qualifier'), Usage('S'), Position(1), Enumerated(*['DY', 'FL', 'HS', 'MN', 'VS'])]
    
    hsd02: Annotated[D_380, Title('Service Unit Count'), Usage('S'), Position(2)]
    
    hsd03: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(3), Enumerated(*['DA', 'MO', 'WK'])]
    
    hsd04: Annotated[D_1167, Title('Sample Selection Modulus'), Usage('S'), Position(4)]
    
    hsd05: Annotated[D_615, Title('Time Period Qualifier'), Usage('S'), Position(5), Enumerated(*['6', '7', '21', '26', '27', '34', '35'])]
    
    hsd06: Annotated[D_616, Title('Period Count'), Usage('S'), Position(6)]
    
    hsd07: Annotated[D_678, Title('Ship,Delivery or Calendar Pattern Code'), Usage('S'), Position(7), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'SA', 'SB', 'SC', 'SD', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ', 'T', 'U', 'V', 'W', 'X', 'Y'])]
    
    hsd08: Annotated[D_679, Title('Delivery Pattern Time Code'), Usage('S'), Position(8), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Y'])]


class L2000F_CRC(Segment):
    """Patient Condition Information"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Condition Code Category'), Usage('R'), Position(1), Enumerated(*['07', '08', '11', '75', '76', '77'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '30', '31', '35', '37', '39', '40', '41', '42', '43', '44', '45', '46', '60', '9D', '9H', '9J', '9K', 'IH', 'LB', 'SL'])]


class L2000F_CL1(Segment):
    """Institutional Claim Code"""
    _segment_name = 'CL1'
    
    cl101: Annotated[D_1315, Title('Admission Type Code'), Usage('S'), Position(1)]
    
    cl102: Annotated[D_1314, Title('Admission Source Code'), Usage('S'), Position(2)]
    
    cl103: Annotated[D_1352, Title('Patient Status Code'), Usage('S'), Position(3)]
    
    cl104: Annotated[D_1345, Title('Nursing Home Residential Status Code'), Usage('S'), Position(4), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9'])]


class L2000F_CR1(Segment):
    """Ambulance Transport Information"""
    _segment_name = 'CR1'
    
    cr101: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(1), Enumerated(*['KG', 'LB'])]
    
    cr102: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(2)]
    
    cr103: Annotated[D_1316, Title('Ambulance Transport Code'), Usage('R'), Position(3), Enumerated(*['I', 'R', 'T', 'X'])]
    
    cr104: Annotated[D_1317, Title('Ambulance Transport Reason Code'), Usage('R'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr105: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(5), Enumerated(*['DH', 'DK'])]
    
    cr106: Annotated[D_380, Title('Transport Distance'), Usage('S'), Position(6)]
    
    cr107: Annotated[D_166, Title('Ambulance Trip Origin Address'), Usage('S'), Position(7)]
    
    cr108: Annotated[D_166, Title('Ambulance Trip Destination Address'), Usage('S'), Position(8)]
    
    cr109: Annotated[D_352, Title('Round Trip Purpose Description'), Usage('S'), Position(9)]
    
    cr110: Annotated[D_352, Title('Stretcher Purpose Description'), Usage('S'), Position(10)]


class L2000F_CR2(Segment):
    """Spinal Manipulation Service Information"""
    _segment_name = 'CR2'
    
    cr201: Annotated[D_609, Title('Treatment Series Number'), Usage('S'), Position(1)]
    
    cr202: Annotated[D_380, Title('Treatment Count'), Usage('S'), Position(2)]
    
    cr203: Annotated[D_1367, Title('Subluxation Level Code'), Usage('S'), Position(3), Enumerated(*['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO', 'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA', 'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9'])]
    
    cr204: Annotated[D_1367, Title('Subluxation Level Code'), Usage('S'), Position(4), Enumerated(*['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CO', 'IL', 'L1', 'L2', 'L3', 'L4', 'L5', 'OC', 'SA', 'T1', 'T10', 'T11', 'T12', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9'])]
    
    cr205: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(5), Enumerated(*['DA', 'MO', 'WK', 'YR'])]
    
    cr206: Annotated[D_380, Title('Treatment Period Count'), Usage('S'), Position(6)]
    
    cr207: Annotated[D_380, Title('Monthly Treatment Count'), Usage('S'), Position(7)]
    
    cr208: Annotated[D_1342, Title('Patient Condition Code'), Usage('S'), Position(8), Enumerated(*['A', 'C', 'D', 'E', 'F', 'G', 'M'])]
    
    cr209: Annotated[D_1073, Title('Complication Indicator'), Usage('S'), Position(9), Enumerated(*['N', 'Y'])]
    
    cr210: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(10)]
    
    cr211: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(11)]
    
    cr212: Annotated[D_1073, Title('X-ray Availability Indicator'), Usage('R'), Position(12), Enumerated(*['N', 'Y'])]


class L2000F_CR5(Segment):
    """Home Oxygen Therapy Information"""
    _segment_name = 'CR5'
    
    cr501: Annotated[D_1322, Title('Certification Type Code'), Usage('N'), Position(1)]
    
    cr502: Annotated[D_380, Title('Quantity'), Usage('N'), Position(2)]
    
    cr503: Annotated[D_1348, Title('Oxygen Equipment Type Code'), Usage('S'), Position(3), Enumerated(*['A', 'B', 'C', 'D', 'E', 'O'])]
    
    cr504: Annotated[D_1348, Title('Oxygen Equipment Type Code'), Usage('S'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E', 'O'])]
    
    cr505: Annotated[D_352, Title('Equipment Reason Description'), Usage('S'), Position(5)]
    
    cr506: Annotated[D_380, Title('Oxygen Flow Rate'), Usage('R'), Position(6)]
    
    cr507: Annotated[D_380, Title('Daily Oxygen Use Count'), Usage('S'), Position(7)]
    
    cr508: Annotated[D_380, Title('Oxygen Use Period Hour Count'), Usage('S'), Position(8)]
    
    cr509: Annotated[D_352, Title('Respiratory Therapist Order Text'), Usage('S'), Position(9)]
    
    cr510: Annotated[D_380, Title('Arterial Blood Gas Quantity'), Usage('S'), Position(10)]
    
    cr511: Annotated[D_380, Title('Oxygen Saturation Quantity'), Usage('S'), Position(11)]
    
    cr512: Annotated[D_1349, Title('Oxygen Test Condition Code'), Usage('R'), Position(12), Enumerated(*['E', 'N', 'O', 'R', 'S', 'W', 'X'])]
    
    cr513: Annotated[D_1350, Title('Oxygen Test Findings Code'), Usage('S'), Position(13), Enumerated(*['1', '2', '3'])]
    
    cr514: Annotated[D_1350, Title('Oxygen Test Findings Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3'])]
    
    cr515: Annotated[D_1350, Title('Oxygen Test Findings Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3'])]
    
    cr516: Annotated[D_380, Title('Portable Oxygen System Flow Rate'), Usage('S'), Position(16)]
    
    cr517: Annotated[D_1382, Title('Oxygen Delivery System Code'), Usage('R'), Position(17), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr518: Annotated[D_1348, Title('Oxygen Equipment Type Code'), Usage('S'), Position(18), Enumerated(*['A', 'B', 'C', 'D', 'E', 'O'])]


class L2000F_CR6(Segment):
    """Home Health Care Information"""
    _segment_name = 'CR6'
    
    cr601: Annotated[D_923, Title('Prognosis Code'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8'])]
    
    cr602: Annotated[D_373, Title('Service From Date'), Usage('R'), Position(2)]
    
    cr603: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['RD8'])]
    
    cr604: Annotated[D_1251, Title('Home Health Certification Period'), Usage('S'), Position(4)]
    
    cr605: Annotated[D_373, Title('Date'), Usage('N'), Position(5)]
    
    cr606: Annotated[D_1073, Title('Skilled Nursing Facility Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'U', 'Y'])]
    
    cr607: Annotated[D_1073, Title('Medicare Coverage Indicator'), Usage('R'), Position(7), Enumerated(*['N', 'U', 'Y'])]
    
    cr608: Annotated[D_1322, Title('Certification Type Code'), Usage('R'), Position(8), Enumerated(*['1', '2', '3', '4', 'I', 'R', 'S'])]
    
    cr609: Annotated[D_373, Title('Surgery Date'), Usage('S'), Position(9)]
    
    cr610: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(10), Enumerated(*['HC', 'ID'])]
    
    cr611: Annotated[D_1137, Title('Surgical Procedure Code'), Usage('S'), Position(11)]
    
    cr612: Annotated[D_373, Title('Physician Order Date'), Usage('S'), Position(12)]
    
    cr613: Annotated[D_373, Title('Last Visit Date'), Usage('S'), Position(13)]
    
    cr614: Annotated[D_373, Title('Physician Contact Date'), Usage('S'), Position(14)]
    
    cr615: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(15), Enumerated(*['RD8'])]
    
    cr616: Annotated[D_1251, Title('Last Admission Period'), Usage('S'), Position(16)]
    
    cr617: Annotated[D_1384, Title('Patient Discharge Facility Type Code'), Usage('S'), Position(17), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M', 'O', 'P', 'R', 'S', 'T'])]
    
    cr618: Annotated[D_373, Title('Date'), Usage('N'), Position(18)]
    
    cr619: Annotated[D_373, Title('Date'), Usage('N'), Position(19)]
    
    cr620: Annotated[D_373, Title('Date'), Usage('N'), Position(20)]
    
    cr621: Annotated[D_373, Title('Date'), Usage('N'), Position(21)]


class L2000F_C002(Composite):
    """Actions Indicated"""
    pass


class L2000F_PWK(Segment):
    """Additional Service Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', '48', '55', '59', '77', 'A3', 'A4', 'AM', 'AS', 'AT', 'B2', 'B3', 'BR', 'BS', 'BT', 'CB', 'CK', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'FM', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'P4', 'P5', 'P6', 'P7', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'QC', 'QR', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX', 'VO'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Attachment Description'), Usage('S'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2000F_MSG(Segment):
    """Message Text"""
    _segment_name = 'MSG'
    
    msg01: Annotated[D_933, Title('Free Form Message Text'), Usage('R'), Position(1)]
    
    msg02: Annotated[D_934, Title('Printer Carriage Control Code'), Usage('N'), Position(2)]
    
    msg03: Annotated[D_1470, Title('Number'), Usage('N'), Position(3)]


class L2000F(Loop):
    
    hl: Annotated[L2000F_HL, Title('Service Level'), Usage('R'), Position(10), Required(True)]
    ItemTrn: TypeAlias = Annotated[L2000F_TRN, Title('Service Trace Number'), Usage('S'), Position(20), Required(True)]
    trn: Annotated[list[ItemTrn], MaxItems(2)]
    
    um: Annotated[L2000F_UM, Title('Health Care Services Review Information'), Usage('R'), Position(40), Required(True)]
    
    ref: Annotated[L2000F_REF, Title('Previous Certification Identification'), Usage('S'), Position(60), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Service Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Admission Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Discharge Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000F_DTP, Title('Surgery Date'), Usage('S'), Position(70), Required(True)]
    
    hi: Annotated[L2000F_HI, Title('Procedures'), Usage('S'), Position(80), Required(True)]
    
    hsd: Annotated[L2000F_HSD, Title('Health Care Services Delivery'), Usage('S'), Position(90)]
    ItemCrc: TypeAlias = Annotated[L2000F_CRC, Title('Patient Condition Information'), Usage('S'), Position(100), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(6)]
    
    cl1: Annotated[L2000F_CL1, Title('Institutional Claim Code'), Usage('S'), Position(110)]
    
    cr1: Annotated[L2000F_CR1, Title('Ambulance Transport Information'), Usage('S'), Position(120), Required(True)]
    
    cr2: Annotated[L2000F_CR2, Title('Spinal Manipulation Service Information'), Usage('S'), Position(130), Required(True)]
    
    cr5: Annotated[L2000F_CR5, Title('Home Oxygen Therapy Information'), Usage('S'), Position(140), Required(True)]
    
    cr6: Annotated[L2000F_CR6, Title('Home Health Care Information'), Usage('S'), Position(150), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2000F_PWK, Title('Additional Service Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    msg: Annotated[L2000F_MSG, Title('Message Text'), Usage('S'), Position(160), Required(True)]


class L2000E(Loop):
    
    hl: Annotated[L2000E_HL, Title('Service Provider Level'), Usage('R'), Position(10), Required(True)]
    
    msg: Annotated[L2000E_MSG, Title('Message Text'), Usage('S'), Position(160), Required(True)]
    ItemL2010E: TypeAlias = Annotated[L2010E, Title('Service Provider Name'), Usage('R'), Position(170), Required(True)]
    l2010e: Annotated[list[ItemL2010E], MinItems(3)]
    ItemL2000F: TypeAlias = Annotated[L2000F, Title('Service Level'), Usage('R'), Position(180), Required(True)]
    l2000f: Annotated[list[ItemL2000F], MinItems(1)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title('Subscriber Level'), Usage('R'), Position(10), Required(True)]
    ItemTrn: TypeAlias = Annotated[L2000C_TRN, Title('Patient Event Tracking Number'), Usage('S'), Position(20), Required(True)]
    trn: Annotated[list[ItemTrn], MaxItems(2)]
    
    dtp: Annotated[L2000C_DTP, Title('Accident Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000C_DTP, Title('Last Menstrual Period Date'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000C_DTP, Title('Estimated Date of Birth'), Usage('S'), Position(70), Required(True)]
    
    dtp: Annotated[L2000C_DTP, Title('Onset of Current Symptoms or Illness Date'), Usage('S'), Position(70), Required(True)]
    
    hi: Annotated[L2000C_HI, Title('Subscriber Diagnosis'), Usage('S'), Position(80), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2000C_PWK, Title('Additional Patient Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    ItemL2010Ca: TypeAlias = Annotated[L2010CA, Title('Subscriber Name'), Usage('R'), Position(170), Required(True)]
    l2010ca: Annotated[list[ItemL2010Ca], MinItems(1)]
    ItemL2000D: TypeAlias = Annotated[L2000D, Title('Dependent Level'), Usage('S'), Position(180), Required(True)]
    l2000d: Annotated[list[ItemL2000D], MinItems(1)]
    ItemL2000E: TypeAlias = Annotated[L2000E, Title('Service Provider Level'), Usage('R'), Position(181), Required(True)]
    l2000e: Annotated[list[ItemL2000E], MinItems(1)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title('Requester Level'), Usage('R'), Position(10), Required(True)]
    ItemL2010B: TypeAlias = Annotated[L2010B, Title('Requester Name'), Usage('R'), Position(170), Required(True)]
    l2010b: Annotated[list[ItemL2010B], MinItems(1)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Subscriber Level'), Usage('R'), Position(180), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Utilization Management Organization (UMO) Level'), Usage('R'), Position(10), Required(True)]
    ItemL2010A: TypeAlias = Annotated[L2010A, Title('Utilization Management Organizational (UMO) Name'), Usage('R'), Position(170), Required(True)]
    l2010a: Annotated[list[ItemL2010A], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Requester Level'), Usage('R'), Position(180), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class DETAIL(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title('Utilization Management Organization (UMO) Level'), Usage('R'), Position(10), Required(True)]
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
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(280), Required(True)]


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


class MSG278(Message):
    """HIPAA Health Care Services Review: Request X094A1-278"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
