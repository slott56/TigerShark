"""
276.4010.X093.A1
Created 2023-05-19 10:17:35.840291
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
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['HN', 'HR'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010X093A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['276'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title('Hierarchical Structure Code'), Usage('R'), Position(1), Enumerated(*['0010'])]
    
    bht02: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(2), Enumerated(*['13'])]
    
    bht03: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(3)]
    
    bht04: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title('Time'), Usage('N'), Position(5)]
    
    bht06: Annotated[D_640, Title('Transaction Type Code'), Usage('N'), Position(6)]


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
    """Payer Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Payer Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['21', 'AD', 'FI', 'NI', 'PI', 'PP', 'XV'])]
    
    nm109: Annotated[D_67, Title('Payer Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100A_PER(Segment):
    """Payer Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Payer Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['ED', 'EM', 'TE'])]
    
    per04: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EX'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EX', 'FX'])]
    
    per08: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100A(Loop):
    
    nm1: Annotated[L2100A_NM1, Title('Payer Name'), Usage('R'), Position(50), Required(True)]
    
    per: Annotated[L2100A_PER, Title('Payer Contact Information'), Usage('S'), Position(80), Required(True)]


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
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['41'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Information Receiver Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Information Receiver First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Information Receiver Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Information Receiver Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['46', 'FI', 'XX'])]
    
    nm109: Annotated[D_67, Title('Information Receiver Identification Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100B(Loop):
    
    nm1: Annotated[L2100B_NM1, Title('Information Receiver Name'), Usage('R'), Position(50), Required(True)]


class L2000C_HL(Segment):
    """Service Provider Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['19'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2100C_NM1(Segment):
    """Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['1P'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Provider Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['FI', 'SV', 'XX'])]
    
    nm109: Annotated[D_67, Title('Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100C(Loop):
    
    nm1: Annotated[L2100C_NM1, Title('Provider Name'), Usage('R'), Position(50), Required(True)]


class L2000D_HL(Segment):
    """Subscriber Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['22'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0', '1'])]


class L2000D_DMG(Segment):
    """Subscriber Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Subscriber Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Subscriber Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2100D_NM1(Segment):
    """Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL', 'QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Subscriber Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Subscriber First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Subscriber Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Subscriber Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Subscriber Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', 'MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Subscriber Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100D(Loop):
    
    nm1: Annotated[L2100D_NM1, Title('Subscriber Name'), Usage('R'), Position(50), Required(True)]


class L2200D_TRN(Segment):
    """Claim Submitter Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200D_C040(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Payer Claim Identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1K'])]
    
    ref02: Annotated[D_127, Title('Payer Claim Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_C040(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Institutional Bill Type Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BLT'])]
    
    ref02: Annotated[D_127, Title('Bill Type Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_C040(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Medical Record Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title('Medical Record Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_C040(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Group Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['LU'])]
    
    ref02: Annotated[D_127, Title('Group Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_AMT(Segment):
    """Claim Submitted Charges"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T3'])]
    
    amt02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2200D_DTP(Segment):
    """Claim Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['232'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['RD8'])]
    
    dtp03: Annotated[D_1251, Title('Claim Service Period'), Usage('R'), Position(3)]


class L2210D_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svc01_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'CI', 'HC', 'ID', 'IV', 'N1', 'N2', 'N3', 'N4', 'ND', 'NH', 'NU', 'RB'])]
    
    svc01_02: Annotated[D_234, Title('Service Identification Code'), Usage('R'), Position(2)]
    
    svc01_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svc01_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svc01_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svc01_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svc01_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2210D_C003(Composite):
    """Composite Medical Procedure Identifier"""
    pass


class L2210D_SVC(Segment):
    """Service Line Information"""
    _segment_name = 'SVC'
    
    c003: Annotated[L2210D_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    svc02: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    svc03: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(3)]
    
    svc04: Annotated[D_234, Title('Revenue Code'), Usage('S'), Position(4)]
    
    svc05: Annotated[D_380, Title('Quantity'), Usage('N'), Position(5)]
    
    svc07: Annotated[D_380, Title('Original Units of Service Count'), Usage('S'), Position(7)]


class L2210D_C040(Composite):
    """Reference Identifier"""
    pass


class L2210D_REF(Segment):
    """Service Line Item Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['FJ'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2210D_DTP(Segment):
    """Service Line Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Line Date'), Usage('R'), Position(3)]


class L2210D(Loop):
    
    svc: Annotated[L2210D_SVC, Title('Service Line Information'), Usage('R'), Position(130), Required(True)]
    
    ref: Annotated[L2210D_REF, Title('Service Line Item Identification'), Usage('S'), Position(140), Required(True)]
    
    dtp: Annotated[L2210D_DTP, Title('Service Line Date'), Usage('R'), Position(150), Required(True)]


class L2200D(Loop):
    
    trn: Annotated[L2200D_TRN, Title('Claim Submitter Trace Number'), Usage('R'), Position(90), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Payer Claim Identification Number'), Usage('S'), Position(100), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Institutional Bill Type Identification'), Usage('S'), Position(100), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Medical Record Identification'), Usage('S'), Position(100), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Group Number'), Usage('S'), Position(100), Required(True)]
    
    amt: Annotated[L2200D_AMT, Title('Claim Submitted Charges'), Usage('S'), Position(110), Required(True)]
    
    dtp: Annotated[L2200D_DTP, Title('Claim Service Date'), Usage('S'), Position(120), Required(True)]
    ItemL2210D: TypeAlias = Annotated[L2210D, Title('Service Line Information'), Usage('S'), Position(130), Required(True)]
    l2210d: Annotated[list[ItemL2210D], MinItems(1)]


class L2000E_HL(Segment):
    """Dependent Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['23'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('N'), Position(4)]


class L2000E_DMG(Segment):
    """Dependent Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Patient Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Patient Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2100E_NM1(Segment):
    """Dependent Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Patient Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Patient First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Patient Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Patient Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Patient Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Patient Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100E(Loop):
    
    nm1: Annotated[L2100E_NM1, Title('Dependent Name'), Usage('R'), Position(50), Required(True)]


class L2200E_TRN(Segment):
    """Claim Submitter Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200E_C040(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Payer Claim Identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1K'])]
    
    ref02: Annotated[D_127, Title('Payer Claim Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_C040(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Institutional Bill Type Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BLT'])]
    
    ref02: Annotated[D_127, Title('Bill Type Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_C040(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Medical Record Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title('Medical Record Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_AMT(Segment):
    """Claim Submitted Charges"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T3'])]
    
    amt02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2200E_DTP(Segment):
    """Claim Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['232'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['RD8'])]
    
    dtp03: Annotated[D_1251, Title('Claim Service Period'), Usage('R'), Position(3)]


class L2210E_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svc01_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'CI', 'HC', 'ID', 'IV', 'N1', 'N2', 'N3', 'N4', 'ND', 'NH', 'NU', 'RB'])]
    
    svc01_02: Annotated[D_234, Title('Service Identification Code'), Usage('R'), Position(2)]
    
    svc01_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svc01_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svc01_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svc01_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svc01_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2210E_C003(Composite):
    """Composite Medical Procedure Identifier"""
    pass


class L2210E_SVC(Segment):
    """Service Line Information"""
    _segment_name = 'SVC'
    
    c003: Annotated[L2210E_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    svc02: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    svc03: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(3)]
    
    svc04: Annotated[D_234, Title('Revenue Code'), Usage('S'), Position(4)]
    
    svc05: Annotated[D_380, Title('Quantity'), Usage('N'), Position(5)]
    
    svc07: Annotated[D_380, Title('Original Units of Service Count'), Usage('S'), Position(7)]


class L2210E_C040(Composite):
    """Reference Identifier"""
    pass


class L2210E_REF(Segment):
    """Service Line Item Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['FJ'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2210E_DTP(Segment):
    """Service Line Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2210E(Loop):
    
    svc: Annotated[L2210E_SVC, Title('Service Line Information'), Usage('R'), Position(130), Required(True)]
    
    ref: Annotated[L2210E_REF, Title('Service Line Item Identification'), Usage('S'), Position(140), Required(True)]
    
    dtp: Annotated[L2210E_DTP, Title('Service Line Date'), Usage('S'), Position(150), Required(True)]


class L2200E(Loop):
    
    trn: Annotated[L2200E_TRN, Title('Claim Submitter Trace Number'), Usage('R'), Position(90), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Payer Claim Identification Number'), Usage('S'), Position(100), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Institutional Bill Type Identification'), Usage('S'), Position(100), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Medical Record Identification'), Usage('S'), Position(100), Required(True)]
    
    amt: Annotated[L2200E_AMT, Title('Claim Submitted Charges'), Usage('S'), Position(110), Required(True)]
    
    dtp: Annotated[L2200E_DTP, Title('Claim Service Date'), Usage('S'), Position(120), Required(True)]
    ItemL2210E: TypeAlias = Annotated[L2210E, Title('Service Line Information'), Usage('S'), Position(130), Required(True)]
    l2210e: Annotated[list[ItemL2210E], MinItems(1)]


class L2000E(Loop):
    
    hl: Annotated[L2000E_HL, Title('Dependent Level'), Usage('R'), Position(10), Required(True)]
    
    dmg: Annotated[L2000E_DMG, Title('Dependent Demographic Information'), Usage('R'), Position(40), Required(True)]
    ItemL2100E: TypeAlias = Annotated[L2100E, Title('Dependent Name'), Usage('R'), Position(50), Required(True)]
    l2100e: Annotated[list[ItemL2100E], MinItems(1)]
    ItemL2200E: TypeAlias = Annotated[L2200E, Title('Claim Submitter Trace Number'), Usage('R'), Position(90), Required(True)]
    l2200e: Annotated[list[ItemL2200E], MinItems(1)]


class L2000D(Loop):
    
    hl: Annotated[L2000D_HL, Title('Subscriber Level'), Usage('R'), Position(10), Required(True)]
    
    dmg: Annotated[L2000D_DMG, Title('Subscriber Demographic Information'), Usage('S'), Position(40), Required(True)]
    ItemL2100D: TypeAlias = Annotated[L2100D, Title('Subscriber Name'), Usage('R'), Position(50), Required(True)]
    l2100d: Annotated[list[ItemL2100D], MinItems(1)]
    ItemL2200D: TypeAlias = Annotated[L2200D, Title('Claim Submitter Trace Number'), Usage('S'), Position(90), Required(True)]
    l2200d: Annotated[list[ItemL2200D], MinItems(1)]
    ItemL2000E: TypeAlias = Annotated[L2000E, Title('Dependent Level'), Usage('S'), Position(100), Required(True)]
    l2000e: Annotated[list[ItemL2000E], MinItems(1)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title('Service Provider Level'), Usage('R'), Position(10), Required(True)]
    ItemL2100C: TypeAlias = Annotated[L2100C, Title('Provider Name'), Usage('R'), Position(50), Required(True)]
    l2100c: Annotated[list[ItemL2100C], MinItems(1)]
    ItemL2000D: TypeAlias = Annotated[L2000D, Title('Subscriber Level'), Usage('R'), Position(60), Required(True)]
    l2000d: Annotated[list[ItemL2000D], MinItems(1)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title('Information Receiver Level'), Usage('R'), Position(10), Required(True)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title('Information Receiver Name'), Usage('R'), Position(50), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Service Provider Level'), Usage('R'), Position(60), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Information Source Level'), Usage('R'), Position(10), Required(True)]
    ItemL2100A: TypeAlias = Annotated[L2100A, Title('Payer Name'), Usage('R'), Position(50), Required(True)]
    l2100a: Annotated[list[ItemL2100A], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Information Receiver Level'), Usage('R'), Position(60), Required(True)]
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
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(270), Required(True)]


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


class MSG276(Message):
    """HIPAA Health Care Claim Status Request X093A1-276"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
