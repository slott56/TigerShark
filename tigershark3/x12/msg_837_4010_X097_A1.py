"""
837.4010.X097.A1
Created 2023-05-19 10:17:36.144023
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
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['HC'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010X097A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['837'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title('Hierarchical Structure Code'), Usage('R'), Position(1), Enumerated(*['0019'])]
    
    bht02: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(2), Enumerated(*['00', '18'])]
    
    bht03: Annotated[D_127, Title('Originator Application Transaction Identifier'), Usage('R'), Position(3)]
    
    bht04: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title('Transaction Set Creation Time'), Usage('R'), Position(5)]
    
    bht06: Annotated[D_640, Title('Claim or Encounter Identifier'), Usage('R'), Position(6), Enumerated(*['CH', 'RP'])]


class HEADER_C040(Composite):
    """Reference Identifier"""
    pass


class HEADER_REF(Segment):
    """Transmission Type Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['87'])]
    
    ref02: Annotated[D_127, Title('Transmission Type Code'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L1000A_NM1(Segment):
    """Submitter Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['41'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Submitter Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Submitter First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Submitter Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['46'])]
    
    nm109: Annotated[D_67, Title('Submitter Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L1000A_PER(Segment):
    """Submitter Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Submitter Contact Name'), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['ED', 'EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L1000A(Loop):
    
    nm1: Annotated[L1000A_NM1, Title('Submitter Name'), Usage('R'), Position(20), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000A_PER, Title('Submitter Contact Information'), Usage('R'), Position(45), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]


class L1000B_NM1(Segment):
    """Receiver Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['40'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Receiver Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['46'])]
    
    nm109: Annotated[D_67, Title('Receiver Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L1000B(Loop):
    
    nm1: Annotated[L1000B_NM1, Title('Receiver Name'), Usage('R'), Position(20), Required(True)]


class HEADER(Loop):
    
    bht: Annotated[HEADER_BHT, Title('Beginning of Hierarchical Transaction'), Usage('R'), Position(10), Required(True)]
    
    ref: Annotated[HEADER_REF, Title('Transmission Type Identification'), Usage('R'), Position(15), Required(True)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title('Submitter Name'), Usage('R'), Position(20), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title('Receiver Name'), Usage('R'), Position(20), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]


class L2000A_HL(Segment):
    """Billing/Pay-To Provider Hierarchical Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('N'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['20'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2000A_PRV(Segment):
    """Billing/Pay-To Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['BI', 'PT'])]
    
    prv02: Annotated[D_128, Title('Referefence Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv05: Annotated[C035, Title('Provider Specialty Information'), Usage('N'), Position(5)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2000A_CUR(Segment):
    """Foreign Currency Information"""
    _segment_name = 'CUR'
    
    cur01: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['85'])]
    
    cur02: Annotated[D_100, Title('Currency Code'), Usage('R'), Position(2), Enumerated(*currency)]
    
    cur03: Annotated[D_280, Title('Exchange Rate'), Usage('N'), Position(3)]
    
    cur04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    cur05: Annotated[D_100, Title('Currency Code'), Usage('N'), Position(5)]
    
    cur06: Annotated[D_669, Title('Currency Market/Exchange Code'), Usage('N'), Position(6)]
    
    cur07: Annotated[D_374, Title('Date/Time Qualifier'), Usage('N'), Position(7)]
    
    cur08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    cur09: Annotated[D_337, Title('Time'), Usage('N'), Position(9)]
    
    cur10: Annotated[D_374, Title('Date/Time Qualifier'), Usage('N'), Position(10)]
    
    cur11: Annotated[D_373, Title('Date'), Usage('N'), Position(11)]
    
    cur12: Annotated[D_337, Title('Time'), Usage('N'), Position(12)]
    
    cur13: Annotated[D_374, Title('Date/Time Qualifier'), Usage('N'), Position(13)]
    
    cur14: Annotated[D_373, Title('Date'), Usage('N'), Position(14)]
    
    cur15: Annotated[D_337, Title('Time'), Usage('N'), Position(15)]
    
    cur16: Annotated[D_374, Title('Date/Time Qualifier'), Usage('N'), Position(16)]
    
    cur17: Annotated[D_373, Title('Date'), Usage('N'), Position(17)]
    
    cur18: Annotated[D_337, Title('Time'), Usage('N'), Position(18)]
    
    cur19: Annotated[D_374, Title('Date/Time Qualifier'), Usage('N'), Position(19)]
    
    cur20: Annotated[D_373, Title('Date'), Usage('N'), Position(20)]
    
    cur21: Annotated[D_337, Title('Time'), Usage('N'), Position(21)]


class L2010AA_NM1(Segment):
    """Billing Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['85'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Billing Provider Last or Organizational Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Billing Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Billing Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Billing Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Billing Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010AA_N3(Segment):
    """Billing Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Billing Provider Address 1'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Billing Provider Address 2'), Usage('S'), Position(2)]


class L2010AA_N4(Segment):
    """Billing Provider City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Billing Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Billing Provider State or Province Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Billing Provider Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Billing Provider Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010AA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010AA_REF(Segment):
    """Billing Provider Secondary Identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Billing Provider Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010AA_REF(Segment):
    """Claim Submitter Credit/Debit Card Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['06', '8U', 'EM', 'IJ', 'LU', 'RB', 'ST', 'TT'])]
    
    ref02: Annotated[D_127, Title('Billing Provider Credit Card Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AA(Loop):
    
    nm1: Annotated[L2010AA_NM1, Title('Billing Provider Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010AA_N3, Title('Billing Provider Address'), Usage('R'), Position(25), Required(True)]
    
    n4: Annotated[L2010AA_N4, Title('Billing Provider City/State/ZIP Code'), Usage('R'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010AA_REF, Title('Billing Provider Secondary Identification Number'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    ItemRef: TypeAlias = Annotated[L2010AA_REF, Title('Claim Submitter Credit/Debit Card Information'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(8)]


class L2010AB_NM1(Segment):
    """Pay-To Provider's Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['87'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Pay-To Provider Last or Organizational Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Pay-To Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Pay-To Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Pay-To Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Pay-To Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010AB_N3(Segment):
    """Pay-To Provider's Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Pay-To Provider Address 1'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Pay-To Provider Address 2'), Usage('S'), Position(2)]


class L2010AB_N4(Segment):
    """Pay-To Provider City/State/ZIP"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Pay-To Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Pay-To Provider State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Pay-To Provider Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Pay-To Provider Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010AB_C040(Composite):
    """Reference Identifier"""
    pass


class L2010AB_REF(Segment):
    """Pay-To Provider Secondary Identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Pay-To Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AB(Loop):
    
    nm1: Annotated[L2010AB_NM1, Title("Pay-To Provider's Name"), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010AB_N3, Title("Pay-To Provider's Address"), Usage('R'), Position(25), Required(True)]
    
    n4: Annotated[L2010AB_N4, Title('Pay-To Provider City/State/ZIP'), Usage('R'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010AB_REF, Title('Pay-To Provider Secondary Identification Number'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2000B_HL(Segment):
    """Subscriber Hierarchical Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['22'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0', '1'])]


class L2000B_SBR(Segment):
    """Subscriber Information"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['P', 'S', 'T'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('S'), Position(2), Enumerated(*['18'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Insured Group Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('R'), Position(6), Enumerated(*['1', '6'])]
    
    sbr07: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['09', '11', '12', '13', '14', '15', '16', '17', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB', 'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ'])]


class L2010BA_NM1(Segment):
    """Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Subscriber Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Subscriber First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Subscriber Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Subscriber Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Subscriber Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010BA_N3(Segment):
    """Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Subscriber Address 1'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Subscriber Address 2'), Usage('S'), Position(2)]


class L2010BA_N4(Segment):
    """Subscriber City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Subscriber City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Subscriber State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Subscriber Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010BA_DMG(Segment):
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


class L2010BA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010BA_REF(Segment):
    """Subscriber Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Subscriber Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010BA_REF(Segment):
    """Property and Casualty Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['Y4'])]
    
    ref02: Annotated[D_127, Title('Property Casualty Claim Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BA(Loop):
    
    nm1: Annotated[L2010BA_NM1, Title('Subscriber Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010BA_N3, Title('Subscriber Address'), Usage('S'), Position(25), Required(True)]
    
    n4: Annotated[L2010BA_N4, Title('Subscriber City/State/ZIP Code'), Usage('S'), Position(30), Required(True)]
    
    dmg: Annotated[L2010BA_DMG, Title('Subscriber Demographic Information'), Usage('S'), Position(32), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010BA_REF, Title('Subscriber Secondary Identification'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]
    
    ref: Annotated[L2010BA_REF, Title('Property and Casualty Claim Number'), Usage('S'), Position(35), Required(True)]


class L2010BB_NM1(Segment):
    """Payer Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Payer Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Payer Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010BB_N3(Segment):
    """Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Payer Address 1'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Payer Address 2'), Usage('S'), Position(2)]


class L2010BB_N4(Segment):
    """Payer City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Payer State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Payer Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Payer Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010BB_C040(Composite):
    """Reference Identifier"""
    pass


class L2010BB_REF(Segment):
    """Payer Secondary Identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Payer Secondary Identification Number'), Usage('R'), Position(1), Enumerated(*['2U', 'FY', 'NF', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Payer Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BB(Loop):
    
    nm1: Annotated[L2010BB_NM1, Title('Payer Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010BB_N3, Title('Payer Address'), Usage('S'), Position(25), Required(True)]
    
    n4: Annotated[L2010BB_N4, Title('Payer City/State/ZIP Code'), Usage('S'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010BB_REF, Title('Payer Secondary Identification Number'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2010BC_NM1(Segment):
    """Credit/Debit Card Holder Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Location Qualifier'), Usage('R'), Position(1), Enumerated(*['AO'])]
    
    nm102: Annotated[D_1065, Title('Loop Identifier Code'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Credit or Debit Card Holder Last or Organizational Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Entity Type Qualifier'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Credit or Debit Card Holder Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Credit or Debit Card Holder Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['MI'])]
    
    nm109: Annotated[D_67, Title('Credit or Debit Card Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010BC_C040(Composite):
    """Reference Identifier"""
    pass


class L2010BC_REF(Segment):
    """Credit/Debit Card Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BB'])]
    
    ref02: Annotated[D_127, Title('Credit or Debit Card Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BC(Loop):
    
    nm1: Annotated[L2010BC_NM1, Title('Credit/Debit Card Holder Name'), Usage('R'), Position(15), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010BC_REF, Title('Credit/Debit Card Information'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2300_C023(Composite):
    """Place of Service Code"""
    
    clm05_01: Annotated[D_1331, Title('Facility Type Code'), Usage('R'), Position(1), Enumerated(*pos)]
    
    clm05_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('N'), Position(2)]
    
    clm05_03: Annotated[D_1325, Title('Claim Submission Reason Code'), Usage('R'), Position(3)]


class L2300_C024(Composite):
    """Related Causes Information"""
    
    clm11_01: Annotated[D_1362, Title('Related Causes Code'), Usage('R'), Position(1), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_02: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(2), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_03: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(3), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_04: Annotated[D_156, Title('Auto Accident State or Province Code'), Usage('S'), Position(4), Enumerated(*states)]
    
    clm11_05: Annotated[D_26, Title('Country Code'), Usage('S'), Position(5), Enumerated(*country)]


class L2300_CLM(Segment):
    """Claim Information"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title('Patient Account Number'), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title('Non-Institutional Claim Type Code'), Usage('N'), Position(4)]
    
    c023: Annotated[L2300_C023, Title('Place of Service Code'), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title('Provider or Supplier Signature Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]
    
    clm07: Annotated[D_1359, Title('Medicare Assignment Code'), Usage('S'), Position(7), Enumerated(*['A', 'C', 'P'])]
    
    clm08: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(8), Enumerated(*['N', 'Y'])]
    
    clm09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['N', 'Y'])]
    
    clm10: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('N'), Position(10)]
    
    c024: Annotated[L2300_C024, Title('Related Causes Information'), Usage('S'), Position(11), Required(True)]
    
    clm12: Annotated[D_1366, Title('Special Program Indicator'), Usage('S'), Position(12), Enumerated(*['01', '02', '03', '05'])]
    
    clm13: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title('Level of Service Code'), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title('Claim Status Code'), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(18)]
    
    clm19: Annotated[D_1383, Title('Predetermination of Benefits Code'), Usage('S'), Position(19), Enumerated(*['PB'])]
    
    clm20: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(20), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])]


class L2300_DTP(Segment):
    """Date - Admission"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Related Hospitalization Admission Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Discharge"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Discharge or End Of Care Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Referral"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['330'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Referral Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Accident"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['439'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Accident Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Appliance Placement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['452'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Orthodontic Banding Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Service"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2300_DN1(Segment):
    """Orthodontic Total Months of Treatment"""
    _segment_name = 'DN1'
    
    dn101: Annotated[D_380, Title('Orthodontic Treatment Months Count'), Usage('S'), Position(1)]
    
    dn102: Annotated[D_380, Title('Orthodontic Treatment Months Remaining Count'), Usage('S'), Position(2)]
    
    dn103: Annotated[D_1073, Title('Question Response'), Usage('S'), Position(3), Enumerated(*['Y'])]
    
    dn104: Annotated[D_352, Title('Description'), Usage('N'), Position(4)]


class L2300_DN2(Segment):
    """Tooth Status"""
    _segment_name = 'DN2'
    
    dn201: Annotated[D_127, Title('Tooth Number'), Usage('R'), Position(1)]
    
    dn202: Annotated[D_1368, Title('Tooth Status Code'), Usage('R'), Position(2), Enumerated(*['E', 'I', 'M'])]
    
    dn203: Annotated[D_380, Title('Quantity'), Usage('N'), Position(3)]
    
    dn204: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(4)]
    
    dn205: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(5)]


class L2300_C002(Composite):
    """Actions Indicated"""
    pass


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['B4', 'DA', 'DG', 'EB', 'OB', 'OZ', 'P6', 'RB', 'RR'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2300_AMT(Segment):
    """Patient Amount Paid"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Patient Amount Paid'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Credit/Debit Card - Maximum Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['MA'])]
    
    amt02: Annotated[D_782, Title('Credit or Debit Card Maximum Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Predetermination Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G3'])]
    
    ref02: Annotated[D_127, Title('Predetermination of Benefits Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Service Authorization Exception Code"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['4N'])]
    
    ref02: Annotated[D_127, Title('Service Authorization Exception Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7'])]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Original Reference Number (ICN/DCN)"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title('Claim Original Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Claim Identification Number for Clearinghouses and Other Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Value Added Network Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_NTE(Segment):
    """Claim Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD'])]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2310A_NM1(Segment):
    """Referring Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Referring Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Referring Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Referring Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Referring Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Referring Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310A_PRV(Segment):
    """Referring Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['RF'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310A_C040(Composite):
    """Reference Identifier"""
    pass


class L2310A_REF(Segment):
    """Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Referring Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title('Referring Provider Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310A_PRV, Title('Referring Provider Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title('Referring Provider Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310B_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310B_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310B_C040(Composite):
    """Reference Identifier"""
    pass


class L2310B_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title('Rendering Provider Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310B_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310C_NM1(Segment):
    """Service Facility Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['FA'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310C_C040(Composite):
    """Reference Identifier"""
    pass


class L2310C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5'])]
    
    ref02: Annotated[D_127, Title('Laboratory or Facility Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title('Service Facility Location'), Usage('R'), Position(250), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title('Service Facility Location Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310D_NM1(Segment):
    """Assistant Surgeon Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DD'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Assistant Last or Organazation Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Assistant Surgeon First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Assistant Surgeon Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Assistant Surgeon Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Assistant Surgeon Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310D_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310D_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AS'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310D_C040(Composite):
    """Reference Identifier"""
    pass


class L2310D_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Assistant Surgeon Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310D(Loop):
    
    nm1: Annotated[L2310D_NM1, Title('Assistant Surgeon Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310D_PRV, Title('Assistant Surgeon Specialty Information'), Usage('S'), Position(255), Required(True)]
    
    ref: Annotated[L2310D_REF, Title('Assistant Surgeon Secondary Identification'), Usage('S'), Position(271), Required(True)]


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['P', 'S', 'T'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '18', '19', '20', '21', '22', '29', '76'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Policy Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['09', '11', '12', '13', '14', '15', '16', '17', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB', 'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """Claim Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Claim Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Payer Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['D'])]
    
    amt02: Annotated[D_782, Title('Payer Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Approved Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AAE'])]
    
    amt02: Annotated[D_782, Title('Approved Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Allowed Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B6'])]
    
    amt02: Annotated[D_782, Title('Allowed Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Responsibility Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F2'])]
    
    amt02: Annotated[D_782, Title('Patient Responsibility Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Covered Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AU'])]
    
    amt02: Annotated[D_782, Title('Covered Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Discount Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    amt02: Annotated[D_782, Title('Other Payer Discount Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Other Payer Patient Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_DMG(Segment):
    """Other Insured Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Other Insured Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Other Insured Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2320_OI(Segment):
    """Other Insurance Coverage Information"""
    _segment_name = 'OI'
    
    oi01: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(1)]
    
    oi02: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(2)]
    
    oi03: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(3), Enumerated(*['N', 'Y'])]
    
    oi04: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('N'), Position(4)]
    
    oi05: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(5)]
    
    oi06: Annotated[D_1363, Title('Release of Information'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Insured Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Insured First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Insured Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Insured Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', 'MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Other Insured Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title("Other Insured's Address 1"), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title("Other Insured's Address 2"), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """Other Subscriber City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Insured City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Insured State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Insured Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title("Other Insured's Country"), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2330A_C040(Composite):
    """Reference Identifier"""
    pass


class L2330A_REF(Segment):
    """Other Subscriber Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Insured Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    
    n3: Annotated[L2330A_N3, Title('Other Subscriber Address'), Usage('S'), Position(332), Required(True)]
    
    n4: Annotated[L2330A_N4, Title('Other Subscriber City/State/ZIP Code'), Usage('S'), Position(340), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330A_REF, Title('Other Subscriber Secondary Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330B_NM1(Segment):
    """Other Payer Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330B_PER(Segment):
    """Other Payer Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Other Payer Contact Name'), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['ED', 'EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2330B_DTP(Segment):
    """Claim Paid Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Date Claim Paid'), Usage('R'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Secondary Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'D8', 'F8', 'FY', 'NF', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Other Payer Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Claim Adjustment Indicator"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['T4'])]
    
    ref02: Annotated[D_127, Title('Other Payer Claim Adjustment Indicator'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    ItemPer: TypeAlias = Annotated[L2330B_PER, Title('Other Payer Contact Information'), Usage('S'), Position(345), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]
    
    dtp: Annotated[L2330B_DTP, Title('Claim Paid Date'), Usage('S'), Position(350), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Secondary Identifier'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Claim Adjustment Indicator'), Usage('S'), Position(355), Required(True)]


class L2330C_NM1(Segment):
    """Other Payer Patient Information"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Patient Last Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['MI'])]
    
    nm109: Annotated[D_67, Title('Other Payer Patient Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330C_C040(Composite):
    """Reference Identifier"""
    pass


class L2330C_REF(Segment):
    """Other Payer Patient Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Payer Patient Primary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title('Other Payer Patient Information'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title('Other Payer Patient Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330D_NM1(Segment):
    """Other Payer Referring Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330D_C040(Composite):
    """Reference Identifier"""
    pass


class L2330D_REF(Segment):
    """Other Payer Referring Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Other Payer Referring Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title('Other Payer Referring Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title('Other Payer Referring Provider Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330E_NM1(Segment):
    """Other Payer Rendering Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330E_C040(Composite):
    """Reference Identifier"""
    pass


class L2330E_REF(Segment):
    """Other Payer Rendering Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Other Payer Rendering Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title('Other Payer Rendering Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title('Other Payer Rendering Provider Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title('Other Subscriber Information'), Usage('R'), Position(290), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title('Claim Adjustment'), Usage('S'), Position(295), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Payer Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Approved Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Allowed Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Patient Responsibility Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Covered Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Discount Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Patient Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    dmg: Annotated[L2320_DMG, Title('Other Insured Demographic Information'), Usage('S'), Position(305), Required(True)]
    
    oi: Annotated[L2320_OI, Title('Other Insurance Coverage Information'), Usage('R'), Position(310), Required(True)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title('Other Payer Patient Information'), Usage('S'), Position(325), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(1)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title('Other Payer Referring Provider'), Usage('S'), Position(325), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title('Other Payer Rendering Provider'), Usage('S'), Position(325), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]


class L2400_LX(Segment):
    """Line Counter"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Line Counter'), Usage('R'), Position(1)]


class L2400_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    sv301_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD'])]
    
    sv301_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv301_03: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(3)]
    
    sv301_04: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(4)]
    
    sv301_05: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(5)]
    
    sv301_06: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(6)]
    
    sv301_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2400_C006(Composite):
    """Oral Cavity Designation"""
    
    sv304_01: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('R'), Position(1), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_02: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(2), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_03: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(3), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_04: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(4), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_05: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(5), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]


class L2400_C004(Composite):
    """Composite Diagnosis Code Pointer"""
    pass


class L2400_SV3(Segment):
    """Dental Service"""
    _segment_name = 'SV3'
    
    c003: Annotated[L2400_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    sv302: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    sv303: Annotated[D_1331, Title('Facility Type Code'), Usage('S'), Position(3), Enumerated(*pos)]
    
    c006: Annotated[L2400_C006, Title('Oral Cavity Designation'), Usage('S'), Position(4), Required(True)]
    
    sv305: Annotated[D_1358, Title('Prosthesis, Crown, or Inlay Code'), Usage('S'), Position(5), Enumerated(*['I', 'R'])]
    
    sv306: Annotated[D_380, Title('Procedure Count'), Usage('R'), Position(6)]
    
    sv307: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    sv308: Annotated[D_1327, Title('Copay Status Code'), Usage('N'), Position(8)]
    
    sv309: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(9)]
    
    sv310: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(10)]


class L2400_C005(Composite):
    """Tooth Surface"""
    
    too03_01: Annotated[D_1369, Title('Tooth Surface Code'), Usage('R'), Position(1), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_02: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(2), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_03: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(3), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_04: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(4), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_05: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(5), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]


class L2400_TOO(Segment):
    """Tooth Information"""
    _segment_name = 'TOO'
    
    too01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['JP'])]
    
    too02: Annotated[D_1271, Title('Tooth Code'), Usage('S'), Position(2)]
    
    c005: Annotated[L2400_C005, Title('Tooth Surface'), Usage('S'), Position(3), Required(True)]


class L2400_DTP(Segment):
    """Date - Service"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Prior Placement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['441'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Prior Placement Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Appliance Placement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['452'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Orthodontic Banding Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Replacement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['446'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Replacement Date'), Usage('R'), Position(3)]


class L2400_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_QTY(Segment):
    """Anesthesia Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['BF', 'EM', 'HM', 'HO', 'HP', 'P3', 'P4', 'P5', 'SG'])]
    
    qty02: Annotated[D_380, Title('Anesthesia Unit Count'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-Form Message'), Usage('N'), Position(4)]


class L2400_C040(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Service Predetermination Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G3'])]
    
    ref02: Annotated[D_127, Title('Predetermination of Benefits Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_C040(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_C040(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Line Item Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['6R'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Approved Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AAE'])]
    
    amt02: Annotated[D_782, Title('Approved Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Sales Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T'])]
    
    amt02: Annotated[D_782, Title('Sales Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_NTE(Segment):
    """Line Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1)]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2420A_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420A_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420A_C040(Composite):
    """Reference Identifier"""
    pass


class L2420A_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title('Rendering Provider Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420A_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(505), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420A_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(525), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2420B_NM1(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Other Payer Referral Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420B_C040(Composite):
    """Reference Identifier"""
    pass


class L2420B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(500), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420B_REF, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(525), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2420C_NM1(Segment):
    """Assistant Surgeon Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DD'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Assistant Surgeon Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Assistant Surgeon First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Assistant Surgeon Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Assistant Surgeon Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Assistant Surgeon Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420C_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420C_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AS'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420C_C040(Composite):
    """Reference Identifier"""
    pass


class L2420C_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'LU', 'TJ', 'X4', 'X5'])]
    
    ref02: Annotated[D_127, Title('Assistant Surgeon Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title('Assistant Surgeon Name'), Usage('S'), Position(500), Required(True)]
    
    prv: Annotated[L2420C_PRV, Title('Assistant Surgeon Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420C_REF, Title('Assistant Surgeon Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2430_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svd03_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'ZZ'])]
    
    svd03_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]


class L2430_SVD(Segment):
    """Line Adjudication Information"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title('Service Line Paid Amount'), Usage('R'), Position(2)]
    
    c003: Annotated[L2430_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(4)]
    
    svd05: Annotated[D_380, Title('Paid Service Unit Count'), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title('Bundled or Unbundled Line Number'), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """Service Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2430_DTP(Segment):
    """Line Adjudication Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title('Line Adjudication Information'), Usage('R'), Position(540), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title('Service Adjustment'), Usage('S'), Position(545), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    
    dtp: Annotated[L2430_DTP, Title('Line Adjudication Date'), Usage('R'), Position(550), Required(True)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title('Line Counter'), Usage('R'), Position(365), Required(True)]
    
    sv3: Annotated[L2400_SV3, Title('Dental Service'), Usage('R'), Position(380), Required(True)]
    ItemToo: TypeAlias = Annotated[L2400_TOO, Title('Tooth Information'), Usage('S'), Position(382), Required(True)]
    too: Annotated[list[ItemToo], MaxItems(32)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Service'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Prior Placement'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Appliance Placement'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Replacement'), Usage('S'), Position(455), Required(True)]
    ItemQty: TypeAlias = Annotated[L2400_QTY, Title('Anesthesia Quantity'), Usage('S'), Position(460), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(5)]
    
    ref: Annotated[L2400_REF, Title('Service Predetermination Identification'), Usage('S'), Position(470), Required(True)]
    ItemRef: TypeAlias = Annotated[L2400_REF, Title('Prior Authorization or Referral Number'), Usage('S'), Position(470), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2400_REF, Title('Line Item Control Number'), Usage('S'), Position(470), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Approved Amount'), Usage('S'), Position(475), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Sales Tax Amount'), Usage('S'), Position(475), Required(True)]
    ItemNte: TypeAlias = Annotated[L2400_NTE, Title('Line Note'), Usage('S'), Position(485), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(10)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title('Rendering Provider Name'), Usage('S'), Position(500), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(500), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title('Assistant Surgeon Name'), Usage('S'), Position(500)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title('Line Adjudication Information'), Usage('S'), Position(540), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(25)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title('Claim Information'), Usage('R'), Position(130), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Admission'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Discharge'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Referral'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Accident'), Usage('S'), Position(135), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2300_DTP, Title('Date - Appliance Placement'), Usage('S'), Position(135), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(5)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Service'), Usage('S'), Position(135), Required(True)]
    
    dn1: Annotated[L2300_DN1, Title('Orthodontic Total Months of Treatment'), Usage('S'), Position(145)]
    ItemDn2: TypeAlias = Annotated[L2300_DN2, Title('Tooth Status'), Usage('S'), Position(150), Required(True)]
    dn2: Annotated[list[ItemDn2], MaxItems(35)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title('Claim Supplemental Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    amt: Annotated[L2300_AMT, Title('Patient Amount Paid'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Credit/Debit Card - Maximum Amount'), Usage('S'), Position(175), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Predetermination Identification'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2300_REF, Title('Service Authorization Exception Code'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Original Reference Number (ICN/DCN)'), Usage('S'), Position(180), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Prior Authorization or Referral Number'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2300_REF, Title('Claim Identification Number for Clearinghouses and Other Transmission Intermediaries'), Usage('S'), Position(180), Required(True)]
    ItemNte: TypeAlias = Annotated[L2300_NTE, Title('Claim Note'), Usage('S'), Position(190), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(20)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title('Referring Provider Name'), Usage('S'), Position(250), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(2)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title('Rendering Provider Name'), Usage('S'), Position(250), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title('Service Facility Location'), Usage('S'), Position(250), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310D: TypeAlias = Annotated[L2310D, Title('Assistant Surgeon Name'), Usage('S'), Position(250), Required(True)]
    l2310d: Annotated[list[ItemL2310D], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title('Other Subscriber Information'), Usage('S'), Position(290), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title('Line Counter'), Usage('R'), Position(365), Required(True)]
    l2400: Annotated[list[ItemL2400], MinItems(50)]


class L2000C_HL(Segment):
    """Patient Hierarchical Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['23'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0'])]


class L2000C_PAT(Segment):
    """Patient Information"""
    _segment_name = 'PAT'
    
    pat01: Annotated[D_1069, Title("Patient's Relationship to Insured"), Usage('R'), Position(1), Enumerated(*['01', '19', '20', '22', '29', '41', '53', '76'])]
    
    pat02: Annotated[D_1384, Title('Patient Location Code'), Usage('N'), Position(2)]
    
    pat03: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(3)]
    
    pat04: Annotated[D_1220, Title('Student Status Code'), Usage('S'), Position(4), Enumerated(*['F', 'N', 'P'])]
    
    pat05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    pat06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]
    
    pat07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(7)]
    
    pat08: Annotated[D_81, Title('Weight'), Usage('N'), Position(8)]
    
    pat09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2010CA_NM1(Segment):
    """Patient Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Patient Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Patient First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Patient Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Patient Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Patient Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010CA_N3(Segment):
    """Patient Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title("Patient's Address 1"), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title("Patient's Address 2"), Usage('S'), Position(2)]


class L2010CA_N4(Segment):
    """Patient City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Patient City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Patient State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Patient Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Patient Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010CA_DMG(Segment):
    """Patient Demographic Information"""
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


class L2010CA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010CA_REF(Segment):
    """Patient Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Patient Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010CA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010CA_REF(Segment):
    """Property and Casualty Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['Y4'])]
    
    ref02: Annotated[D_127, Title('Property Casualty Claim Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010CA(Loop):
    
    nm1: Annotated[L2010CA_NM1, Title('Patient Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010CA_N3, Title('Patient Address'), Usage('R'), Position(25), Required(True)]
    
    n4: Annotated[L2010CA_N4, Title('Patient City/State/ZIP Code'), Usage('R'), Position(30), Required(True)]
    
    dmg: Annotated[L2010CA_DMG, Title('Patient Demographic Information'), Usage('R'), Position(32), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010CA_REF, Title('Patient Secondary Identification'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2010CA_REF, Title('Property and Casualty Claim Number'), Usage('S'), Position(35), Required(True)]


class L2300_C023(Composite):
    """Place of Service Code"""
    
    clm05_01: Annotated[D_1331, Title('Facility Type Code'), Usage('R'), Position(1), Enumerated(*pos)]
    
    clm05_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('N'), Position(2)]
    
    clm05_03: Annotated[D_1325, Title('Claim Submission Reason Code'), Usage('R'), Position(3)]


class L2300_C024(Composite):
    """Related Causes Information"""
    
    clm11_01: Annotated[D_1362, Title('Related Causes Code'), Usage('R'), Position(1), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_02: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(2), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_03: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(3), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_04: Annotated[D_156, Title('Auto Accident State or Province Code'), Usage('S'), Position(4), Enumerated(*states)]
    
    clm11_05: Annotated[D_26, Title('Country Code'), Usage('S'), Position(5), Enumerated(*country)]


class L2300_CLM(Segment):
    """Claim Information"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title('Patient Account Number'), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title('Non-Institutional Claim Type Code'), Usage('N'), Position(4)]
    
    c023: Annotated[L2300_C023, Title('Place of Service Code'), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title('Provider or Supplier Signature Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]
    
    clm07: Annotated[D_1359, Title('Medicare Assignment Code'), Usage('S'), Position(7), Enumerated(*['A', 'C', 'P'])]
    
    clm08: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(8), Enumerated(*['N', 'Y'])]
    
    clm09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['N', 'Y'])]
    
    clm10: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('N'), Position(10)]
    
    c024: Annotated[L2300_C024, Title('Related Causes Information'), Usage('S'), Position(11), Required(True)]
    
    clm12: Annotated[D_1366, Title('Special Program Indicator'), Usage('S'), Position(12), Enumerated(*['01', '02', '03', '05'])]
    
    clm13: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title('Level of Service Code'), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title('Claim Status Code'), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(18)]
    
    clm19: Annotated[D_1383, Title('Predetermination of Benefits Code'), Usage('S'), Position(19), Enumerated(*['PB'])]
    
    clm20: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(20), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])]


class L2300_DTP(Segment):
    """Date - Admission"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Related Hospitalization Admission Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Discharge"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Discharge or End Of Care Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Referral"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['330'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Referral Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Accident"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['439'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Accident Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Appliance Placement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['452'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Orthodontic Banding Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Service"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2300_DN1(Segment):
    """Orthodontic Total Months of Treatment"""
    _segment_name = 'DN1'
    
    dn101: Annotated[D_380, Title('Orthodontic Treatment Months Count'), Usage('S'), Position(1)]
    
    dn102: Annotated[D_380, Title('Orthodontic Treatment Months Remaining Count'), Usage('S'), Position(2)]
    
    dn103: Annotated[D_1073, Title('Question Response'), Usage('S'), Position(3), Enumerated(*['Y'])]
    
    dn104: Annotated[D_352, Title('Description'), Usage('N'), Position(4)]


class L2300_DN2(Segment):
    """Tooth Status"""
    _segment_name = 'DN2'
    
    dn201: Annotated[D_127, Title('Tooth Number'), Usage('R'), Position(1)]
    
    dn202: Annotated[D_1368, Title('Tooth Status Code'), Usage('R'), Position(2), Enumerated(*['E', 'I', 'M'])]
    
    dn203: Annotated[D_380, Title('Quantity'), Usage('N'), Position(3)]
    
    dn204: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(4)]
    
    dn205: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(5)]


class L2300_C002(Composite):
    """Actions Indicated"""
    pass


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['B4', 'DA', 'DG', 'EB', 'OB', 'OZ', 'P6', 'RB', 'RR'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2300_AMT(Segment):
    """Patient Amount Paid"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Patient Amount Paid'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Credit/Debit Card - Maximum Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['MA'])]
    
    amt02: Annotated[D_782, Title('Credit or Debit Card Maximum Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Predetermination Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G3'])]
    
    ref02: Annotated[D_127, Title('Predetermination of Benefits Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Service Authorization Exception Code"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['4N'])]
    
    ref02: Annotated[D_127, Title('Service Authorization Exception Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7'])]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Original Reference Number (ICN/DCN)"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title('Claim Original Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Claim Identification Number for Clearinghouses and Other Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Value Added Network Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_NTE(Segment):
    """Claim Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD'])]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2310A_NM1(Segment):
    """Referring Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Referring Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Referring Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Referring Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Referring Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Referring Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310A_PRV(Segment):
    """Referring Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['RF'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310A_C040(Composite):
    """Reference Identifier"""
    pass


class L2310A_REF(Segment):
    """Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Referring Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title('Referring Provider Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310A_PRV, Title('Referring Provider Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title('Referring Provider Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310B_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310B_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310B_C040(Composite):
    """Reference Identifier"""
    pass


class L2310B_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title('Rendering Provider Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310B_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310C_NM1(Segment):
    """Service Facility Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['FA'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310C_C040(Composite):
    """Reference Identifier"""
    pass


class L2310C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5'])]
    
    ref02: Annotated[D_127, Title('Laboratory or Facility Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title('Service Facility Location'), Usage('R'), Position(250), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title('Service Facility Location Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310D_NM1(Segment):
    """Assistant Surgeon Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DD'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Assistant Last or Organazation Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Assistant Surgeon First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Assistant Surgeon Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Assistant Surgeon Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Assistant Surgeon Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310D_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310D_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AS'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310D_C040(Composite):
    """Reference Identifier"""
    pass


class L2310D_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5'])]
    
    ref02: Annotated[D_127, Title('Assistant Surgeon Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310D(Loop):
    
    nm1: Annotated[L2310D_NM1, Title('Assistant Surgeon Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310D_PRV, Title('Assistant Surgeon Specialty Information'), Usage('S'), Position(255), Required(True)]
    
    ref: Annotated[L2310D_REF, Title('Assistant Surgeon Secondary Identification'), Usage('S'), Position(271), Required(True)]


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['P', 'S', 'T'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '18', '19', '20', '21', '22', '29', '76'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Policy Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['09', '11', '12', '13', '14', '15', '16', '17', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MB', 'MC', 'MH', 'OF', 'SA', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """Claim Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Claim Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Payer Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['D'])]
    
    amt02: Annotated[D_782, Title('Payer Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Approved Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AAE'])]
    
    amt02: Annotated[D_782, Title('Approved Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Allowed Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B6'])]
    
    amt02: Annotated[D_782, Title('Allowed Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Responsibility Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F2'])]
    
    amt02: Annotated[D_782, Title('Patient Responsibility Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Covered Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AU'])]
    
    amt02: Annotated[D_782, Title('Covered Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Discount Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    amt02: Annotated[D_782, Title('Other Payer Discount Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Patient Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Other Payer Patient Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_DMG(Segment):
    """Other Insured Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Other Insured Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Other Insured Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2320_OI(Segment):
    """Other Insurance Coverage Information"""
    _segment_name = 'OI'
    
    oi01: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(1)]
    
    oi02: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(2)]
    
    oi03: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(3), Enumerated(*['N', 'Y'])]
    
    oi04: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('N'), Position(4)]
    
    oi05: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(5)]
    
    oi06: Annotated[D_1363, Title('Release of Information'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Insured Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Insured First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Insured Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Insured Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', 'MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Other Insured Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title("Other Insured's Address 1"), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title("Other Insured's Address 2"), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """Other Subscriber City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Insured City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Insured State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Insured Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title("Other Insured's Country"), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2330A_C040(Composite):
    """Reference Identifier"""
    pass


class L2330A_REF(Segment):
    """Other Subscriber Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Insured Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    
    n3: Annotated[L2330A_N3, Title('Other Subscriber Address'), Usage('S'), Position(332), Required(True)]
    
    n4: Annotated[L2330A_N4, Title('Other Subscriber City/State/ZIP Code'), Usage('S'), Position(340), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330A_REF, Title('Other Subscriber Secondary Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330B_NM1(Segment):
    """Other Payer Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330B_PER(Segment):
    """Other Payer Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Other Payer Contact Name'), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['ED', 'EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2330B_DTP(Segment):
    """Claim Paid Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Date Claim Paid'), Usage('R'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Secondary Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'D8', 'F8', 'FY', 'NF', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Other Payer Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Claim Adjustment Indicator"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['T4'])]
    
    ref02: Annotated[D_127, Title('Other Payer Claim Adjustment Indicator'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    ItemPer: TypeAlias = Annotated[L2330B_PER, Title('Other Payer Contact Information'), Usage('S'), Position(345), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]
    
    dtp: Annotated[L2330B_DTP, Title('Claim Paid Date'), Usage('S'), Position(350), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Secondary Identifier'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Claim Adjustment Indicator'), Usage('S'), Position(355), Required(True)]


class L2330C_NM1(Segment):
    """Other Payer Patient Information"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Patient Last Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['MI'])]
    
    nm109: Annotated[D_67, Title('Other Payer Patient Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330C_C040(Composite):
    """Reference Identifier"""
    pass


class L2330C_REF(Segment):
    """Other Payer Patient Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Payer Patient Primary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title('Other Payer Patient Information'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title('Other Payer Patient Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330D_NM1(Segment):
    """Other Payer Referring Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330D_C040(Composite):
    """Reference Identifier"""
    pass


class L2330D_REF(Segment):
    """Other Payer Referring Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Other Payer Referring Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title('Other Payer Referring Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title('Other Payer Referring Provider Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330E_NM1(Segment):
    """Other Payer Rendering Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330E_C040(Composite):
    """Reference Identifier"""
    pass


class L2330E_REF(Segment):
    """Other Payer Rendering Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Other Payer Rendering Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title('Other Payer Rendering Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title('Other Payer Rendering Provider Identification'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title('Other Subscriber Information'), Usage('R'), Position(290), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title('Claim Adjustment'), Usage('S'), Position(295), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Payer Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Approved Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Allowed Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Patient Responsibility Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Covered Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Discount Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Patient Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    dmg: Annotated[L2320_DMG, Title('Other Insured Demographic Information'), Usage('S'), Position(305), Required(True)]
    
    oi: Annotated[L2320_OI, Title('Other Insurance Coverage Information'), Usage('R'), Position(310), Required(True)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title('Other Payer Patient Information'), Usage('S'), Position(325), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(1)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title('Other Payer Referring Provider'), Usage('S'), Position(325), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title('Other Payer Rendering Provider'), Usage('S'), Position(325), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]


class L2400_LX(Segment):
    """Line Counter"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Line Counter'), Usage('R'), Position(1)]


class L2400_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    sv301_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD'])]
    
    sv301_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv301_03: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(3)]
    
    sv301_04: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(4)]
    
    sv301_05: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(5)]
    
    sv301_06: Annotated[D_1339, Title('Procedure Code Modifier'), Usage('S'), Position(6)]
    
    sv301_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2400_C006(Composite):
    """Oral Cavity Designation"""
    
    sv304_01: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('R'), Position(1), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_02: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(2), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_03: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(3), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_04: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(4), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]
    
    sv304_05: Annotated[D_1361, Title('Oral Cavity Designation Code'), Usage('S'), Position(5), Enumerated(*['L', 'R', '00', '01', '02', '09', '10', '20', '30', '40'])]


class L2400_C004(Composite):
    """Composite Diagnosis Code Pointer"""
    pass


class L2400_SV3(Segment):
    """Dental Service"""
    _segment_name = 'SV3'
    
    c003: Annotated[L2400_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    sv302: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    sv303: Annotated[D_1331, Title('Facility Type Code'), Usage('S'), Position(3), Enumerated(*pos)]
    
    c006: Annotated[L2400_C006, Title('Oral Cavity Designation'), Usage('S'), Position(4), Required(True)]
    
    sv305: Annotated[D_1358, Title('Prosthesis, Crown, or Inlay Code'), Usage('S'), Position(5), Enumerated(*['I', 'R'])]
    
    sv306: Annotated[D_380, Title('Procedure Count'), Usage('R'), Position(6)]
    
    sv307: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    sv308: Annotated[D_1327, Title('Copay Status Code'), Usage('N'), Position(8)]
    
    sv309: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(9)]
    
    sv310: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(10)]


class L2400_C005(Composite):
    """Tooth Surface"""
    
    too03_01: Annotated[D_1369, Title('Tooth Surface Code'), Usage('R'), Position(1), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_02: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(2), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_03: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(3), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_04: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(4), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]
    
    too03_05: Annotated[D_1369, Title('Tooth Surface Code'), Usage('S'), Position(5), Enumerated(*['B', 'D', 'F', 'I', 'L', 'M', 'O'])]


class L2400_TOO(Segment):
    """Tooth Information"""
    _segment_name = 'TOO'
    
    too01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['JP'])]
    
    too02: Annotated[D_1271, Title('Tooth Code'), Usage('S'), Position(2)]
    
    c005: Annotated[L2400_C005, Title('Tooth Surface'), Usage('S'), Position(3), Required(True)]


class L2400_DTP(Segment):
    """Date - Service"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Prior Placement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['441'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Prior Placement Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Appliance Placement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['452'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Orthodontic Banding Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Replacement"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['446'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Replacement Date'), Usage('R'), Position(3)]


class L2400_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_QTY(Segment):
    """Anesthesia Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['BF', 'EM', 'HM', 'HO', 'HP', 'P3', 'P4', 'P5', 'SG'])]
    
    qty02: Annotated[D_380, Title('Anesthesia Unit Count'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-Form Message'), Usage('N'), Position(4)]


class L2400_C040(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Service Predetermination Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G3'])]
    
    ref02: Annotated[D_127, Title('Predetermination of Benefits Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_C040(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_C040(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Line Item Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['6R'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Approved Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AAE'])]
    
    amt02: Annotated[D_782, Title('Approved Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Sales Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T'])]
    
    amt02: Annotated[D_782, Title('Sales Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_NTE(Segment):
    """Line Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1)]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2420A_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420A_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420A_C040(Composite):
    """Reference Identifier"""
    pass


class L2420A_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'EI', 'G2', 'G5', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title('Rendering Provider Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420A_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(505), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420A_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(525), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2420B_NM1(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Other Payer Referral Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420B_C040(Composite):
    """Reference Identifier"""
    pass


class L2420B_REF(Segment):
    """Other Payer Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(500), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420B_REF, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(525), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2420C_NM1(Segment):
    """Assistant Surgeon Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DD'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Assistant Surgeon Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Assistant Surgeon First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Assistant Surgeon Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Assistant Surgeon Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Assistant Surgeon Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420C_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420C_PRV(Segment):
    """Assistant Surgeon Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AS'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420C_C040(Composite):
    """Reference Identifier"""
    pass


class L2420C_REF(Segment):
    """Assistant Surgeon Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1H', 'G2', 'LU', 'TJ', 'X4', 'X5'])]
    
    ref02: Annotated[D_127, Title('Assistant Surgeon Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title('Assistant Surgeon Name'), Usage('S'), Position(500), Required(True)]
    
    prv: Annotated[L2420C_PRV, Title('Assistant Surgeon Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420C_REF, Title('Assistant Surgeon Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2430_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svd03_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'ZZ'])]
    
    svd03_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]


class L2430_SVD(Segment):
    """Line Adjudication Information"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title('Service Line Paid Amount'), Usage('R'), Position(2)]
    
    c003: Annotated[L2430_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(4)]
    
    svd05: Annotated[D_380, Title('Paid Service Unit Count'), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title('Bundled or Unbundled Line Number'), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """Service Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2430_DTP(Segment):
    """Line Adjudication Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title('Line Adjudication Information'), Usage('R'), Position(540), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title('Service Adjustment'), Usage('S'), Position(545), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    
    dtp: Annotated[L2430_DTP, Title('Line Adjudication Date'), Usage('R'), Position(550), Required(True)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title('Line Counter'), Usage('R'), Position(365), Required(True)]
    
    sv3: Annotated[L2400_SV3, Title('Dental Service'), Usage('R'), Position(380), Required(True)]
    ItemToo: TypeAlias = Annotated[L2400_TOO, Title('Tooth Information'), Usage('S'), Position(382), Required(True)]
    too: Annotated[list[ItemToo], MaxItems(32)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Service'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Prior Placement'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Appliance Placement'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Replacement'), Usage('S'), Position(455), Required(True)]
    ItemQty: TypeAlias = Annotated[L2400_QTY, Title('Anesthesia Quantity'), Usage('S'), Position(460), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(5)]
    
    ref: Annotated[L2400_REF, Title('Service Predetermination Identification'), Usage('S'), Position(470), Required(True)]
    ItemRef: TypeAlias = Annotated[L2400_REF, Title('Prior Authorization or Referral Number'), Usage('S'), Position(470), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2400_REF, Title('Line Item Control Number'), Usage('S'), Position(470), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Approved Amount'), Usage('S'), Position(475), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Sales Tax Amount'), Usage('S'), Position(475), Required(True)]
    ItemNte: TypeAlias = Annotated[L2400_NTE, Title('Line Note'), Usage('S'), Position(485), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(10)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title('Rendering Provider Name'), Usage('S'), Position(500), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(500), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title('Assistant Surgeon Name'), Usage('S'), Position(500)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title('Line Adjudication Information'), Usage('S'), Position(540), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(25)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title('Claim Information'), Usage('R'), Position(130), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Admission'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Discharge'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Referral'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Accident'), Usage('S'), Position(135), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2300_DTP, Title('Date - Appliance Placement'), Usage('S'), Position(135), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(5)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Service'), Usage('S'), Position(135), Required(True)]
    
    dn1: Annotated[L2300_DN1, Title('Orthodontic Total Months of Treatment'), Usage('S'), Position(145)]
    ItemDn2: TypeAlias = Annotated[L2300_DN2, Title('Tooth Status'), Usage('S'), Position(150), Required(True)]
    dn2: Annotated[list[ItemDn2], MaxItems(35)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title('Claim Supplemental Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    amt: Annotated[L2300_AMT, Title('Patient Amount Paid'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Credit/Debit Card - Maximum Amount'), Usage('S'), Position(175), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Predetermination Identification'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2300_REF, Title('Service Authorization Exception Code'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Original Reference Number (ICN/DCN)'), Usage('S'), Position(180), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Prior Authorization or Referral Number'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2300_REF, Title('Claim Identification Number for Clearinghouses and Other Transmission Intermediaries'), Usage('S'), Position(180), Required(True)]
    ItemNte: TypeAlias = Annotated[L2300_NTE, Title('Claim Note'), Usage('S'), Position(190), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(20)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title('Referring Provider Name'), Usage('S'), Position(250), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(2)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title('Rendering Provider Name'), Usage('S'), Position(250), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title('Service Facility Location'), Usage('S'), Position(250), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310D: TypeAlias = Annotated[L2310D, Title('Assistant Surgeon Name'), Usage('S'), Position(250), Required(True)]
    l2310d: Annotated[list[ItemL2310D], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title('Other Subscriber Information'), Usage('S'), Position(290), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title('Line Counter'), Usage('R'), Position(365), Required(True)]
    l2400: Annotated[list[ItemL2400], MinItems(50)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title('Patient Hierarchical Level'), Usage('R'), Position(1), Required(True)]
    
    pat: Annotated[L2000C_PAT, Title('Patient Information'), Usage('R'), Position(7), Required(True)]
    ItemL2010Ca: TypeAlias = Annotated[L2010CA, Title('Patient Name'), Usage('R'), Position(15), Required(True)]
    l2010ca: Annotated[list[ItemL2010Ca], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title('Claim Information'), Usage('R'), Position(130), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(100)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title('Subscriber Hierarchical Level'), Usage('R'), Position(1), Required(True)]
    
    sbr: Annotated[L2000B_SBR, Title('Subscriber Information'), Usage('R'), Position(5), Required(True)]
    ItemL2010Ba: TypeAlias = Annotated[L2010BA, Title('Subscriber Name'), Usage('R'), Position(15), Required(True)]
    l2010ba: Annotated[list[ItemL2010Ba], MinItems(1)]
    ItemL2010Bb: TypeAlias = Annotated[L2010BB, Title('Payer Name'), Usage('R'), Position(15), Required(True)]
    l2010bb: Annotated[list[ItemL2010Bb], MinItems(1)]
    ItemL2010Bc: TypeAlias = Annotated[L2010BC, Title('Credit/Debit Card Holder Name'), Usage('S'), Position(15), Required(True)]
    l2010bc: Annotated[list[ItemL2010Bc], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title('Claim Information'), Usage('S'), Position(130), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(100)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Patient Hierarchical Level'), Usage('S'), Position(140), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Billing/Pay-To Provider Hierarchical Level'), Usage('R'), Position(1), Required(True)]
    
    prv: Annotated[L2000A_PRV, Title('Billing/Pay-To Provider Specialty Information'), Usage('S'), Position(3), Required(True)]
    
    cur: Annotated[L2000A_CUR, Title('Foreign Currency Information'), Usage('S'), Position(10), Required(True)]
    ItemL2010Aa: TypeAlias = Annotated[L2010AA, Title('Billing Provider Name'), Usage('R'), Position(15), Required(True)]
    l2010aa: Annotated[list[ItemL2010Aa], MinItems(1)]
    ItemL2010Ab: TypeAlias = Annotated[L2010AB, Title("Pay-To Provider's Name"), Usage('S'), Position(15), Required(True)]
    l2010ab: Annotated[list[ItemL2010Ab], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Subscriber Hierarchical Level'), Usage('R'), Position(20), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class DETAIL(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title('Billing/Pay-To Provider Hierarchical Level'), Usage('R'), Position(1), Required(True)]
    l2000a: Annotated[list[ItemL2000A], MinItems(1)]


class FOOTER(Loop):
    pass


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(5), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Table 1 - Header'), Usage('R'), Position(10), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('S'), Position(20), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('N'), Position(30)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(555), Required(True)]


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


class MSG837(Message):
    """HIPAA Health Care Claim: Dental X097A1-837"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
