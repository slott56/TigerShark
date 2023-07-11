"""
837.4010.X096.A1
Created 2023-05-19 10:17:36.094624
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
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010X096A1'])]


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
    """Transaction Type Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['87'])]
    
    ref02: Annotated[D_127, Title('Transmission Type Code'), Usage('R'), Position(2), Enumerated(*['004010X096DA1', '004010X096A1'])]
    
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
    """Submitter EDI Contact Information"""
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
    ItemPer: TypeAlias = Annotated[L1000A_PER, Title('Submitter EDI Contact Information'), Usage('R'), Position(45), Required(True)]
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
    
    nm108: Annotated[D_66, Title('Information Receiver Identification Number'), Usage('R'), Position(8), Enumerated(*['46'])]
    
    nm109: Annotated[D_67, Title('Receiver Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L1000B(Loop):
    
    nm1: Annotated[L1000B_NM1, Title('Receiver Name'), Usage('R'), Position(20), Required(True)]


class HEADER(Loop):
    
    bht: Annotated[HEADER_BHT, Title('Beginning of Hierarchical Transaction'), Usage('R'), Position(10), Required(True)]
    
    ref: Annotated[HEADER_REF, Title('Transaction Type Identification'), Usage('R'), Position(15), Required(True)]
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


class L2000A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2000A_PRV(Segment):
    """Billing/Pay-To Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['BI', 'PT'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4), Enumerated(*states)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2000A_CUR(Segment):
    """Foreign Currency Information"""
    _segment_name = 'CUR'
    
    cur01: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['85'])]
    
    cur02: Annotated[D_100, Title('Currency Code'), Usage('R'), Position(2), Enumerated(*currency)]
    
    cur03: Annotated[D_280, Title('Exchange Rate'), Usage('N'), Position(3)]
    
    cur04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    cur05: Annotated[D_100, Title('Currency Code'), Usage('N'), Position(5), Enumerated(*currency)]
    
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
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Billing Provider Last or Organizational Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Billing Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010AA_N3(Segment):
    """Billing Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Billing Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Billing Provider Address Line'), Usage('S'), Position(2)]


class L2010AA_N4(Segment):
    """Billing Provider City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Billing Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Billing Provider State or Province Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Billing Provider Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010AA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010AA_REF(Segment):
    """Billing Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'B3', 'BQ', 'EI', 'FH', 'G2', 'G5', 'LU', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Billing Provider Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010AA_REF(Segment):
    """Credit/Debit Card Billing Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['06', '8U', 'EM', 'IJ', 'LU', 'RB', 'ST', 'TT'])]
    
    ref02: Annotated[D_127, Title('Billing Provider Credit Card Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AA_PER(Segment):
    """Billing Provider Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Billing Provider Contact Name'), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2010AA(Loop):
    
    nm1: Annotated[L2010AA_NM1, Title('Billing Provider Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010AA_N3, Title('Billing Provider Address'), Usage('R'), Position(25), Required(True)]
    
    n4: Annotated[L2010AA_N4, Title('Billing Provider City/State/ZIP Code'), Usage('R'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010AA_REF, Title('Billing Provider Secondary Identification'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(8)]
    ItemRef: TypeAlias = Annotated[L2010AA_REF, Title('Credit/Debit Card Billing Information'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(8)]
    ItemPer: TypeAlias = Annotated[L2010AA_PER, Title('Billing Provider Contact Information'), Usage('S'), Position(40), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]


class L2010AB_NM1(Segment):
    """Pay-To Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['87'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Pay-to Provider Last or Organizational Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Pay-to Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010AB_N3(Segment):
    """Pay-To Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Pay-to Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Pay-to Provider Address Line'), Usage('S'), Position(2)]


class L2010AB_N4(Segment):
    """Pay-To Provider City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Pay-to Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Pay-to Provider State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Pay-to Provider Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Pay-to Provider Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010AB_C040(Composite):
    """Reference Identifier"""
    pass


class L2010AB_REF(Segment):
    """Pay-To Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'B3', 'BQ', 'EI', 'FH', 'G2', 'G5', 'LU', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Pay-to Provider Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AB(Loop):
    
    nm1: Annotated[L2010AB_NM1, Title('Pay-To Provider Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010AB_N3, Title('Pay-To Provider Address'), Usage('R'), Position(25), Required(True)]
    
    n4: Annotated[L2010AB_N4, Title('Pay-To Provider City/State/ZIP Code'), Usage('R'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010AB_REF, Title('Pay-To Provider Secondary Identification'), Usage('S'), Position(35), Required(True)]
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
    
    sbr02: Annotated[D_1069, Title('Patients Relationship to Insured'), Usage('S'), Position(2), Enumerated(*['18'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Insured Group Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['09', '10', '11', '12', '13', '14', '15', '16', 'AM', 'BL', 'CH', 'CI', 'DS', 'HM', 'LI', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


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
    
    n301: Annotated[D_166, Title('Subscriber Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Subscriber Address Line'), Usage('S'), Position(2)]


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
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7), Enumerated(*country)]
    
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
    """Credit/Debit Card Account Holder Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['AO'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Credit or Debit Card Holder Last or Organizational Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Credit or Debit Card Holder First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Credit or Debit Card Holder Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Credit or Debit Card Holder Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['MI'])]
    
    nm109: Annotated[D_67, Title('Credit or Debit Card Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010BB_C040(Composite):
    """Reference Identifier"""
    pass


class L2010BB_REF(Segment):
    """Credit/Debit Card Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['AB', 'BB'])]
    
    ref02: Annotated[D_127, Title('Credit or Debit Card Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BB(Loop):
    
    nm1: Annotated[L2010BB_NM1, Title('Credit/Debit Card Account Holder Name'), Usage('R'), Position(15), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010BB_REF, Title('Credit/Debit Card Information'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2010BC_NM1(Segment):
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


class L2010BC_N3(Segment):
    """Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Payer Address Line'), Usage('S'), Position(2)]


class L2010BC_N4(Segment):
    """Payer City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Payer State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Payer Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Payer Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010BC_C040(Composite):
    """Reference Identifier"""
    pass


class L2010BC_REF(Segment):
    """Payer Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'FY', 'NF', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Payer Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BC(Loop):
    
    nm1: Annotated[L2010BC_NM1, Title('Payer Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010BC_N3, Title('Payer Address'), Usage('S'), Position(25), Required(True)]
    
    n4: Annotated[L2010BC_N4, Title('Payer City/State/ZIP Code'), Usage('S'), Position(30), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010BC_REF, Title('Payer Secondary Identification'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2010BD_NM1(Segment):
    """Responsible Party Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QD'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Responsible Party Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Responsible Party First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Responsible Party Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Responsible Party Suffix Name'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2010BD_N3(Segment):
    """Responsible Party Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Responsible Party Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Responsible Party Address Line'), Usage('S'), Position(2)]


class L2010BD_N4(Segment):
    """Responsible Party City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Responsible Party City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Responsible Party State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Responsible Party Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Responsible Party Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2010BD(Loop):
    
    nm1: Annotated[L2010BD_NM1, Title('Responsible Party Name'), Usage('R'), Position(15), Required(True)]
    
    n3: Annotated[L2010BD_N3, Title('Responsible Party Address'), Usage('R'), Position(25), Required(True)]
    
    n4: Annotated[L2010BD_N4, Title('Responsible Party City/State/ZIP Code'), Usage('R'), Position(30), Required(True)]


class L2300_C023(Composite):
    """Type of Bill"""
    
    clm05_01: Annotated[D_1331, Title('Facility Type Code'), Usage('R'), Position(1)]
    
    clm05_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('R'), Position(2), Enumerated(*['A'])]
    
    clm05_03: Annotated[D_1325, Title('Claim Frequency Code'), Usage('R'), Position(3), Enumerated(*['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'X', 'Y', 'Z '])]


class L2300_C024(Composite):
    """Property and Casualty Related Causes Codes"""
    pass


class L2300_CLM(Segment):
    """Claim Information"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title('Patient Account Number'), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title('Non-Institutional Claim Type Code'), Usage('N'), Position(4)]
    
    c023: Annotated[L2300_C023, Title('Type of Bill'), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title('Provider or Supplier Signature Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]
    
    clm07: Annotated[D_1359, Title('Medicare Assignment Code'), Usage('S'), Position(7), Enumerated(*['A', 'C'])]
    
    clm08: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(8), Enumerated(*['N', 'Y'])]
    
    clm09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['A', 'I', 'M', 'N', 'O', 'Y'])]
    
    clm10: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('N'), Position(10)]
    
    clm12: Annotated[D_1366, Title('Special Program Indicator'), Usage('N'), Position(12), Enumerated(*['01', '02', '03', '05', '07', '08', '09'])]
    
    clm13: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title('Level of Service Code'), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title('Claim Status Code'), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title('Explanation of Benefits Indicator'), Usage('R'), Position(18), Enumerated(*['N', 'Y'])]
    
    clm19: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(19)]
    
    clm20: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(20), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])]


class L2300_DTP(Segment):
    """Discharge Hour"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['TM'])]
    
    dtp03: Annotated[D_1251, Title('Discharge Hour'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Statement Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['434'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Statement From or To Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Admission Date/Hour"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['DT'])]
    
    dtp03: Annotated[D_1251, Title('Admission Date and Hour'), Usage('R'), Position(3)]


class L2300_CL1(Segment):
    """Institutional Claim Code"""
    _segment_name = 'CL1'
    
    cl101: Annotated[D_1315, Title('Admission Type Code'), Usage('S'), Position(1)]
    
    cl102: Annotated[D_1314, Title('Admission Source Code'), Usage('S'), Position(2)]
    
    cl103: Annotated[D_1352, Title('Patient Status Code'), Usage('S'), Position(3)]
    
    cl104: Annotated[D_1345, Title('Nursing Home Residential Status Code'), Usage('N'), Position(4)]


class L2300_C002(Composite):
    """Actions Indicated"""
    pass


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['AS', 'B2', 'B3', 'B4', 'CT', 'DA', 'DG', 'DS', 'EB', 'MT', 'NN', 'OB', 'OZ', 'PN', 'PO', 'PZ', 'RB', 'RR', 'RT'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Attachment Description'), Usage('S'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2300_CN1(Segment):
    """Contract Information"""
    _segment_name = 'CN1'
    
    cn101: Annotated[D_1166, Title('Contract Type Code'), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '09'])]
    
    cn102: Annotated[D_782, Title('Contract Amount'), Usage('S'), Position(2)]
    
    cn103: Annotated[D_332, Title('Contract Percentage'), Usage('S'), Position(3)]
    
    cn104: Annotated[D_127, Title('Contract Code'), Usage('S'), Position(4)]
    
    cn105: Annotated[D_338, Title('Terms Discount Percentage'), Usage('S'), Position(5)]
    
    cn106: Annotated[D_799, Title('Contract Version Identifier'), Usage('S'), Position(6)]


class L2300_AMT(Segment):
    """Payer Estimated Amount Due"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['C5'])]
    
    amt02: Annotated[D_782, Title('Estimated Claim Due Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Patient Estimated Amount Due"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F3'])]
    
    amt02: Annotated[D_782, Title('Patient Responsibility Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Patient Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Patient Amount Paid'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Credit/Debit Card Maximum Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['MA'])]
    
    amt02: Annotated[D_782, Title('Credit or Debit Card Maximum Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Adjusted Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9C'])]
    
    ref02: Annotated[D_127, Title('Adjusted Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9A'])]
    
    ref02: Annotated[D_127, Title('Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Claim Identification Number For Clearinghouses and Other Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Value Added Network Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Document Identification Code"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['DD'])]
    
    ref02: Annotated[D_127, Title('Document Control Identifier'), Usage('R'), Position(2)]
    
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
    """Investigational Device Exemption Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['LX'])]
    
    ref02: Annotated[D_127, Title('Investigational Device Exemption Identifier'), Usage('R'), Position(2)]
    
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
    """Peer Review Organization (PRO) Approval Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G4'])]
    
    ref02: Annotated[D_127, Title('Peer Review Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Medical Record Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title('Medical Record Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Demonstration Project Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['P4'])]
    
    ref02: Annotated[D_127, Title('Demonstration Project Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2300_K3(Segment):
    """File Information"""
    _segment_name = 'K3'
    
    k301: Annotated[D_449, Title('Fixed Format Information'), Usage('R'), Position(1)]
    
    k302: Annotated[D_1333, Title('Record Format Code'), Usage('N'), Position(2)]


class L2300_NTE(Segment):
    """Claim Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ALG', 'DCP', 'DGN', 'DME', 'MED', 'NTR', 'ODT', 'RHB', 'RLH', 'RNH', 'SET', 'SFM', 'SPT', 'UPI'])]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2300_NTE(Segment):
    """Billing Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD'])]
    
    nte02: Annotated[D_352, Title('Billing Note Text'), Usage('R'), Position(2)]


class L2300_CR6(Segment):
    """Home Health Care Information"""
    _segment_name = 'CR6'
    
    cr601: Annotated[D_923, Title('Prognosis Indicator'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8'])]
    
    cr602: Annotated[D_373, Title('Service From Date'), Usage('R'), Position(2)]
    
    cr603: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['RD8'])]
    
    cr604: Annotated[D_1251, Title('Home Health Certification Period'), Usage('S'), Position(4)]
    
    cr605: Annotated[D_373, Title('Diagnosis Date'), Usage('R'), Position(5)]
    
    cr606: Annotated[D_1073, Title('Skilled Nursing Facility Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'U', 'Y'])]
    
    cr607: Annotated[D_1073, Title('Medicare Coverage Indicator'), Usage('R'), Position(7), Enumerated(*['N', 'Y'])]
    
    cr608: Annotated[D_1322, Title('Certification Type Indicator'), Usage('R'), Position(8), Enumerated(*['I', 'R', 'S'])]
    
    cr609: Annotated[D_373, Title('Surgery Date'), Usage('S'), Position(9)]
    
    cr610: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(10), Enumerated(*['HC', 'ID'])]
    
    cr611: Annotated[D_1137, Title('Surgical Procedure Code'), Usage('S'), Position(11)]
    
    cr612: Annotated[D_373, Title('Physician Order Date'), Usage('S'), Position(12)]
    
    cr613: Annotated[D_373, Title('Last Visit Date'), Usage('S'), Position(13)]
    
    cr614: Annotated[D_373, Title('Physician Contact Date'), Usage('S'), Position(14)]
    
    cr615: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(15), Enumerated(*['RD8'])]
    
    cr616: Annotated[D_1251, Title('Last Admission Period'), Usage('S'), Position(16)]
    
    cr617: Annotated[D_1384, Title('Patient Discharge Facility Type Code'), Usage('R'), Position(17), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M', 'O', 'R', 'S', 'T'])]
    
    cr618: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(18)]
    
    cr619: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(19)]
    
    cr620: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(20)]
    
    cr621: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(21)]


class L2300_CRC(Segment):
    """Home Health Functional Limitations"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['75'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Functional Limitation Code'), Usage('R'), Position(3), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc04: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(4), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc05: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(5), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc06: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(6), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc07: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(7), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]


class L2300_CRC(Segment):
    """Home Health Activities Permitted"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Certification Condition Indicator'), Usage('R'), Position(1), Enumerated(*['76'])]
    
    crc02: Annotated[D_1073, Title(' Functional Limitation Code'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Activities Permitted Code'), Usage('R'), Position(3), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc04: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(4), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc05: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(5), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc06: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(6), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc07: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(7), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]


class L2300_CRC(Segment):
    """Home Health Mental Status"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Certification Condition Indicator'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    crc02: Annotated[D_1073, Title('Functional Limitation Code'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Mental Status Code'), Usage('R'), Position(3), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc04: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(4), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc05: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(5), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc06: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(6), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc07: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(7), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BK'])]
    
    hi01_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BJ', 'ZZ'])]
    
    hi02_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BN'])]
    
    hi03_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Principal, Admitting, E-Code and Patient Reason for Visit Diagnosis Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['DR'])]
    
    hi01_02: Annotated[D_1271, Title('Diagnosis Related Group (DRG) Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Diagnosis Related Group (DRG) Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi01_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi02_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi03_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi04_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi05_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi06_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi07_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi08_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi09_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi10_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi11_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi12_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Other Diagnosis Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BP', 'BR'])]
    
    hi01_02: Annotated[D_1271, Title('Principal Procedure Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Principal Procedure Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi01_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi02_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi03_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi04_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi05_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi06_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi07_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi08_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi09_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi10_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi11_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi12_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Other Procedure Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi01_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi01_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi02_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi02_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi03_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi03_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi04_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi04_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi05_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi05_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi06_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi06_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi07_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi07_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi08_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi08_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi09_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi09_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi10_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi10_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi11_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi11_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi12_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi12_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Occurrence Span Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi01_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi02_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi03_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi04_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi05_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi06_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi07_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi08_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi09_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi10_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi11_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi12_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Occurrence Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi01_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi02_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi03_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi04_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi05_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi06_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('n Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi07_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi08_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi09_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi10_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi11_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi12_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Value Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi01_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi02_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi03_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi04_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi05_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi06_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi07_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi08_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi09_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi10_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi11_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi12_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Condition Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi01_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi02_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi03_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi04_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi05_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi06_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi07_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi08_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi09_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi10_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi11_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi12_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Treatment Code Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C001(Composite):
    """Composite Unit of Measure"""
    
    qty03_01: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(1), Enumerated(*['DA'])]
    
    qty03_02: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(2)]
    
    qty03_03: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(3)]
    
    qty03_04: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(4)]
    
    qty03_05: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(5)]
    
    qty03_06: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(6)]
    
    qty03_07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(7)]
    
    qty03_08: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(8)]
    
    qty03_09: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(9)]
    
    qty03_10: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(10)]
    
    qty03_11: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(11)]
    
    qty03_12: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(12)]
    
    qty03_13: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(13)]
    
    qty03_14: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(14)]
    
    qty03_15: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(15)]


class L2300_QTY(Segment):
    """Claim Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['CA', 'CD', 'LA', 'NA'])]
    
    qty02: Annotated[D_380, Title('Claim Days Count'), Usage('R'), Position(2)]
    
    c001: Annotated[L2300_C001, Title('Composite Unit of Measure'), Usage('R'), Position(3), Required(True)]
    
    qty04: Annotated[D_61, Title('Free-Form Message'), Usage('N'), Position(4)]


class L2300_HCP(Segment):
    """Claim Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repricing Organization Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved DRG Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Repriced Approved Revenue Code'), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(9), Enumerated(*['HC'])]
    
    hcp10: Annotated[D_234, Title('Repriced Approved HCPCS Code'), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title('Repriced Approved Service Unit Count'), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Rejection Message'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Reason Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2305_CR7(Segment):
    """Home Health Care Plan Information"""
    _segment_name = 'CR7'
    
    cr701: Annotated[D_921, Title('Discipline Type Code'), Usage('R'), Position(1), Enumerated(*['AI', 'MS', 'OT', 'PT', 'SN', 'ST'])]
    
    cr702: Annotated[D_1470, Title('Visits Prior to Recertification Date Count'), Usage('R'), Position(2)]
    
    cr703: Annotated[D_1470, Title('Total Visits Projected This Certification Count'), Usage('R'), Position(3)]


class L2305_HSD(Segment):
    """Health Care Services Delivery"""
    _segment_name = 'HSD'
    
    hsd01: Annotated[D_673, Title('Visits'), Usage('S'), Position(1), Enumerated(*['VS'])]
    
    hsd02: Annotated[D_380, Title('Number of Visits'), Usage('S'), Position(2)]
    
    hsd03: Annotated[D_355, Title('Frequency Period'), Usage('S'), Position(3), Enumerated(*['DA', 'MO', 'Q1', 'WK'])]
    
    hsd04: Annotated[D_1167, Title('Frequency Count'), Usage('S'), Position(4)]
    
    hsd05: Annotated[D_615, Title('Duration of Visits Units'), Usage('S'), Position(5), Enumerated(*['7', '35'])]
    
    hsd06: Annotated[D_616, Title('Duration of Visits, Number of Units'), Usage('S'), Position(6)]
    
    hsd07: Annotated[D_678, Title('Ship, Delivery or Calendar Pattern Code'), Usage('S'), Position(7), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'N', 'O', 'S', 'SA', 'SB', 'SC', 'SD', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ', 'W'])]
    
    hsd08: Annotated[D_679, Title('Delivery Pattern Time Code'), Usage('S'), Position(8), Enumerated(*['D', 'E', 'F'])]


class L2305(Loop):
    
    cr7: Annotated[L2305_CR7, Title('Home Health Care Plan Information'), Usage('R'), Position(242), Required(True)]
    ItemHsd: TypeAlias = Annotated[L2305_HSD, Title('Health Care Services Delivery'), Usage('S'), Position(243)]
    hsd: Annotated[list[ItemHsd], MaxItems(12)]


class L2310A_NM1(Segment):
    """Attending Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['71'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Attending Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Attending Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Attending Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Attending Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Attending Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310A_PRV(Segment):
    """Attending Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AT', 'SU'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4), Enumerated(*states)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310A_C040(Composite):
    """Reference Identifier"""
    pass


class L2310A_REF(Segment):
    """Attending Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Attending Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title('Attending Physician Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310A_PRV, Title('Attending Physician Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title('Attending Physician Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310B_NM1(Segment):
    """Operating Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Operating Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Operating Physician First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Operating Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Operating Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Operating Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310B_PRV(Segment):
    """Operating Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OP'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310B_C040(Composite):
    """Reference Identifier"""
    pass


class L2310B_REF(Segment):
    """Operating Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Operating Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title('Operating Physician Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310B_PRV, Title('Operating Physician Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title('Operating Physician Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310C_NM1(Segment):
    """Other Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['73'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Other Physician Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310C_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310C_PRV(Segment):
    """Other Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OT', 'PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310C_C040(Composite):
    """Reference Identifier"""
    pass


class L2310C_REF(Segment):
    """Other Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Other Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title('Other Provider Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310C_PRV, Title('Other Provider Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title('Other Provider Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310E_NM1(Segment):
    """Service Facility Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['FA'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310E_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310E_PRV(Segment):
    """Service Facility Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['RP'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310E_N3(Segment):
    """Service Facility Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('S'), Position(2)]


class L2310E_N4(Segment):
    """Service Facility City/State/Zip Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Laboratory or Facility City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Laboratory or Facility State or Province Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Laboratory or Facility Postal Zone or Zip Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Laboratory/Facility Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2310E_C040(Composite):
    """Reference Identifier"""
    pass


class L2310E_REF(Segment):
    """Service Facility Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'EI', 'FH', 'G2', 'G5', 'LU', 'N5', 'X5'])]
    
    ref02: Annotated[D_127, Title('Laboratory or Facility Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310E(Loop):
    
    nm1: Annotated[L2310E_NM1, Title('Service Facility Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310E_PRV, Title('Service Facility Specialty Information'), Usage('S'), Position(255), Required(True)]
    
    n3: Annotated[L2310E_N3, Title('Service Facility Address'), Usage('R'), Position(265), Required(True)]
    
    n4: Annotated[L2310E_N4, Title('Service Facility City/State/Zip Code'), Usage('R'), Position(270), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310E_REF, Title('Service Facility Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['P', 'S', 'T'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '04', '05', '07', '10', '15', '17', '18', '19', '20', '21', '22', '23', '24', '29', '32', '33', '36', '39', '40', '41', '43', '53', 'G8'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Other Insured Group Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['09', '10', '11', '12', '13', '14', '15', '16', 'AM', 'BL', 'CH', 'CI', 'DS', 'HM', 'LI', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """Claim Level Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Claim Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2320_AMT(Segment):
    """Payer Prior Payment"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['C4'])]
    
    amt02: Annotated[D_782, Title('Other Payer Patient Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Allowed Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B6'])]
    
    amt02: Annotated[D_782, Title('Allowed Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Submitted Charges"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T3'])]
    
    amt02: Annotated[D_782, Title('Coordination of Benefits Total Submitted Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Diagnostic Related Group (DRG) Outlier Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    amt02: Annotated[D_782, Title('Claim DRG Outlier Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Medicare Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['N1'])]
    
    amt02: Annotated[D_782, Title('Total Medicare Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Medicare Paid Amount - 100%"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['KF'])]
    
    amt02: Annotated[D_782, Title('Medicare Paid at 100% Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Medicare Paid Amount - 80%"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['PG'])]
    
    amt02: Annotated[D_782, Title('Medicare Paid at 80% Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Medicare A Trust Fund Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AA'])]
    
    amt02: Annotated[D_782, Title('Paid From Part A Medicare Trust Fund Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Medicare B Trust Fund Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B1'])]
    
    amt02: Annotated[D_782, Title('Paid From Part B Medicare Trust Fund Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Non-Covered Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['A8'])]
    
    amt02: Annotated[D_782, Title('Non-Covered Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Denied Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['YT'])]
    
    amt02: Annotated[D_782, Title('Claim Total Denied Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_DMG(Segment):
    """Other Subscriber Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Other Insured Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Other Insured Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('nicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7), Enumerated(*country)]
    
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
    
    oi06: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(6), Enumerated(*['A', 'I', 'M', 'N', 'O', 'Y'])]


class L2320_MIA(Segment):
    """Medicare Inpatient Adjudication Information"""
    _segment_name = 'MIA'
    
    mia01: Annotated[D_380, Title('Covered Days or Visits Count'), Usage('R'), Position(1)]
    
    mia02: Annotated[D_380, Title('Lifetime Reserve Days Count'), Usage('S'), Position(2)]
    
    mia03: Annotated[D_380, Title('Lifetime Psychiatric Days Count'), Usage('S'), Position(3)]
    
    mia04: Annotated[D_782, Title('Claim DRG Amount'), Usage('S'), Position(4)]
    
    mia05: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(5), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia06: Annotated[D_782, Title('Claim Disproportionate Share Amount'), Usage('S'), Position(6)]
    
    mia07: Annotated[D_782, Title('Claim MSP Pass-through Amount'), Usage('S'), Position(7)]
    
    mia08: Annotated[D_782, Title('Claim PPS Capital Amount'), Usage('S'), Position(8)]
    
    mia09: Annotated[D_782, Title('PPS-Capital FSP DRG Amount'), Usage('S'), Position(9)]
    
    mia10: Annotated[D_782, Title('PPS-Capital HSP DRG Amount'), Usage('S'), Position(10)]
    
    mia11: Annotated[D_782, Title('PPS-Capital DSH DRG Amount'), Usage('S'), Position(11)]
    
    mia12: Annotated[D_782, Title('Old Capital Amount'), Usage('S'), Position(12)]
    
    mia13: Annotated[D_782, Title('PPS-Capital IME Amount'), Usage('S'), Position(13)]
    
    mia14: Annotated[D_782, Title('PPS-Operating Hospital Specific DRG Amount'), Usage('S'), Position(14)]
    
    mia15: Annotated[D_380, Title('Cost Report Day Count'), Usage('S'), Position(15)]
    
    mia16: Annotated[D_782, Title('PPS-Operating Federal Specific DRG Amount'), Usage('S'), Position(16)]
    
    mia17: Annotated[D_782, Title('Claim PPS Capital Outlier Amount'), Usage('S'), Position(17)]
    
    mia18: Annotated[D_782, Title('Claim Indirect Teaching Amount'), Usage('S'), Position(18)]
    
    mia19: Annotated[D_782, Title('Nonpayable Professional Component Amount'), Usage('S'), Position(19)]
    
    mia20: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(20), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia21: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(21), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia22: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(22), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia23: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(23), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia24: Annotated[D_782, Title('PPS-Capital Exception Amount'), Usage('S'), Position(24)]


class L2320_MOA(Segment):
    """Medicare Outpatient Adjudication Information"""
    _segment_name = 'MOA'
    
    moa01: Annotated[D_954, Title('Reimbursement Rate'), Usage('S'), Position(1)]
    
    moa02: Annotated[D_782, Title('Claim HCPCS Payable Amount'), Usage('S'), Position(2)]
    
    moa03: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(3), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa04: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(4), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa05: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(5), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa06: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(6), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa07: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(7), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa08: Annotated[D_782, Title('Claim ESRD Payment Amount'), Usage('S'), Position(8)]
    
    moa09: Annotated[D_782, Title('Nonpayable Professional Component Amount'), Usage('S'), Position(9)]


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Insured Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Insured First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Insured Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('fix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Insured Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Other Insured Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Insured Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Insured Address Line'), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """Other Subscriber City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Insured City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Insured State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Insured Postal Zone or Zip Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Subscriber Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2330A_C040(Composite):
    """Reference Identifier"""
    pass


class L2330A_REF(Segment):
    """Other Subscriber Secondary Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Insured Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    
    n3: Annotated[L2330A_N3, Title('Other Subscriber Address'), Usage('S'), Position(332), Required(True)]
    
    n4: Annotated[L2330A_N4, Title('Other Subscriber City/State/ZIP Code'), Usage('S'), Position(340), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330A_REF, Title('Other Subscriber Secondary Information'), Usage('S'), Position(355), Required(True)]
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


class L2330B_N3(Segment):
    """Other Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Payer Address Line'), Usage('S'), Position(2)]


class L2330B_N4(Segment):
    """Other Payer City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Payer State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Payer Postal Zone or Zip Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Payer Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2330B_DTP(Segment):
    """Claim Adjudication Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Secondary Identification and Reference Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'F8', 'FY', 'NF', 'TJ'])]
    
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


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    
    n3: Annotated[L2330B_N3, Title('Other Payer Address'), Usage('S'), Position(332), Required(True)]
    
    n4: Annotated[L2330B_N4, Title('Other Payer City/State/ZIP Code'), Usage('S'), Position(340), Required(True)]
    
    dtp: Annotated[L2330B_DTP, Title('Claim Adjudication Date'), Usage('S'), Position(350), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Secondary Identification and Reference Number'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(355), Required(True)]


class L2330C_NM1(Segment):
    """Other Payer Patient Information"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['EI', 'MI'])]
    
    nm109: Annotated[D_67, Title('Other Payer Patient Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330C_C040(Composite):
    """Reference Identifier"""
    pass


class L2330C_REF(Segment):
    """Other Payer identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Payer Patient Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title('Other Payer Patient Information'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title('Other Payer identification Number'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330D_NM1(Segment):
    """Other Payer Attending Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['71'])]
    
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
    """Other Payer Attending Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5'])]
    
    ref02: Annotated[D_127, Title('Other Payer Attending Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title('Other Payer Attending Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title('Other Payer Attending Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330E_NM1(Segment):
    """Other Payer Operating Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
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
    """Other Payer Operating Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5'])]
    
    ref02: Annotated[D_127, Title('Other Payer Operating Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title('Other Payer Operating Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title('Other Payer Operating Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330F_NM1(Segment):
    """Other Payer Other Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['73'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('fier Code'), Usage('N'), Position(11)]


class L2330F_C040(Composite):
    """Reference Identifier"""
    pass


class L2330F_REF(Segment):
    """Other Payer Other Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Payer Other Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('on'), Usage('N'), Position(3)]


class L2330F(Loop):
    
    nm1: Annotated[L2330F_NM1, Title('Other Payer Other Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330F_REF, Title('Other Payer Other Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330H_NM1(Segment):
    """Other Payer Service Facility Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['FA'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('ode Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330H_C040(Composite):
    """Reference Identifier"""
    pass


class L2330H_REF(Segment):
    """Other Payer Service Facility Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1B', '1C', '1D', 'EI', 'G2', 'LU', 'N5'])]
    
    ref02: Annotated[D_127, Title('Other Payer Service Facility Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330H(Loop):
    
    nm1: Annotated[L2330H_NM1, Title('Other Payer Service Facility Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330H_REF, Title('Other Payer Service Facility Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title('Other Subscriber Information'), Usage('R'), Position(290), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title('Claim Level Adjustment'), Usage('S'), Position(295), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title('Payer Prior Payment'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Allowed Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Submitted Charges'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Diagnostic Related Group (DRG) Outlier Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Medicare Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Medicare Paid Amount - 100%'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Medicare Paid Amount - 80%'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Medicare A Trust Fund Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Medicare B Trust Fund Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Non-Covered Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Denied Amount'), Usage('S'), Position(300), Required(True)]
    
    dmg: Annotated[L2320_DMG, Title('Other Subscriber Demographic Information'), Usage('S'), Position(305), Required(True)]
    
    oi: Annotated[L2320_OI, Title('Other Insurance Coverage Information'), Usage('R'), Position(310), Required(True)]
    
    mia: Annotated[L2320_MIA, Title('Medicare Inpatient Adjudication Information'), Usage('S'), Position(315), Required(True)]
    
    moa: Annotated[L2320_MOA, Title('Medicare Outpatient Adjudication Information'), Usage('S'), Position(320)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title('Other Payer Patient Information'), Usage('S'), Position(325), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(1)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title('Other Payer Attending Provider'), Usage('S'), Position(325), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title('Other Payer Operating Provider'), Usage('S'), Position(325), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]
    ItemL2330F: TypeAlias = Annotated[L2330F, Title('Other Payer Other Provider'), Usage('S'), Position(325), Required(True)]
    l2330f: Annotated[list[ItemL2330F], MinItems(1)]
    ItemL2330H: TypeAlias = Annotated[L2330H, Title('Other Payer Service Facility Provider'), Usage('S'), Position(325), Required(True)]
    l2330h: Annotated[list[ItemL2330H], MinItems(1)]


class L2400_LX(Segment):
    """Service Line Number"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]


class L2400_C003(Composite):
    """Service Line Procedure Code"""
    
    sv202_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['HC', 'IV', 'N4', 'ZZ'])]
    
    sv202_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv202_03: Annotated[D_1339, Title('HCPCS Modifier 1'), Usage('S'), Position(3)]
    
    sv202_04: Annotated[D_1339, Title('HCPCS Modifier 2'), Usage('S'), Position(4)]
    
    sv202_05: Annotated[D_1339, Title('HCPCS Modifier 3'), Usage('S'), Position(5)]
    
    sv202_06: Annotated[D_1339, Title('HCPCS Modifier 4'), Usage('S'), Position(6)]
    
    sv202_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2400_SV2(Segment):
    """Institutional Service Line"""
    _segment_name = 'SV2'
    
    sv201: Annotated[D_234, Title('Service Line Revenue Code'), Usage('R'), Position(1)]
    
    c003: Annotated[L2400_C003, Title('Service Line Procedure Code'), Usage('S'), Position(2), Required(True)]
    
    sv203: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(3)]
    
    sv204: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(4), Enumerated(*['DA', 'F2', 'UN'])]
    
    sv205: Annotated[D_380, Title('Service Unit Count'), Usage('R'), Position(5)]
    
    sv206: Annotated[D_1371, Title('Service Line Rate'), Usage('S'), Position(6)]
    
    sv207: Annotated[D_782, Title('Line Item Denied Charge or Non-Covered Charge Amount'), Usage('S'), Position(7)]
    
    sv208: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(8)]
    
    sv209: Annotated[D_1345, Title('Status Code'), Usage('N'), Position(9)]
    
    sv210: Annotated[D_1337, Title('Level of Care Code'), Usage('N'), Position(10)]


class L2400_C002(Composite):
    """Actions Indicated"""
    pass


class L2400_PWK(Segment):
    """Line Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['AS', 'B2', 'B3', 'B4', 'CT', 'DA', 'DG', 'DS', 'EB', 'MT', 'NN', 'OB', 'OZ', 'PN', 'PO', 'PZ', 'RB', 'RR', 'RT'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'AB', 'AD', 'AF', 'AG', 'BM', 'EL', 'EM', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2400_DTP(Segment):
    """Service Line Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Assessment Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['866'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Assessment Date'), Usage('R'), Position(3)]


class L2400_AMT(Segment):
    """Service Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['GT'])]
    
    amt02: Annotated[D_782, Title('Service Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Facility Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['N8'])]
    
    amt02: Annotated[D_782, Title('Facility Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_HCP(Segment):
    """Line Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repriced Organizational Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved Ambulatory Patient Group Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Ambulatory Patient Group Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Repriced Approved Revenue Code'), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product/ Service ID Qualifier'), Usage('S'), Position(9), Enumerated(*['HC'])]
    
    hcp10: Annotated[D_234, Title('Procedure Code'), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title('Repricing Approved Service Unit Count'), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Reject Reason Code'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2410_LIN(Segment):
    """Drug Identification"""
    _segment_name = 'LIN'
    
    lin01: Annotated[D_350, Title('Assigned Identification'), Usage('N'), Position(1)]
    
    lin02: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('R'), Position(2), Enumerated(*['N4'])]
    
    lin03: Annotated[D_234, Title('Product/Service ID'), Usage('R'), Position(3)]
    
    lin04: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(4), Enumerated(*['N4'])]
    
    lin05: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(5)]
    
    lin06: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(6), Enumerated(*['N4'])]
    
    lin07: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(7)]
    
    lin08: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(8), Enumerated(*['N4'])]
    
    lin09: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(9)]
    
    lin10: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(10), Enumerated(*['N4'])]
    
    lin11: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(11)]
    
    lin12: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(12), Enumerated(*['N4'])]
    
    lin13: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(13)]
    
    lin14: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(14), Enumerated(*['N4'])]
    
    lin15: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(15)]
    
    lin16: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(16), Enumerated(*['N4'])]
    
    lin17: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(17)]
    
    lin18: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(18), Enumerated(*['N4'])]
    
    lin19: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(19)]
    
    lin20: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(20), Enumerated(*['N4'])]
    
    lin21: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(21)]
    
    lin22: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(22), Enumerated(*['N4'])]
    
    lin23: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(23)]
    
    lin24: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(24), Enumerated(*['N4'])]
    
    lin25: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(25)]
    
    lin26: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(26), Enumerated(*['N4'])]
    
    lin27: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(27)]
    
    lin28: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(28), Enumerated(*['N4'])]
    
    lin29: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(29)]
    
    lin30: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(30), Enumerated(*['N4'])]
    
    lin31: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(31)]


class L2410_C001(Composite):
    """Composite Unit of Measure"""
    
    ctp05_01: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(1), Enumerated(*['F2', 'GR', 'ML', 'UN'])]
    
    ctp05_02: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(2)]
    
    ctp05_03: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(3)]
    
    ctp05_04: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(4)]
    
    ctp05_05: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(5)]
    
    ctp05_06: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(6)]
    
    ctp05_07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(7)]
    
    ctp05_08: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(8)]
    
    ctp05_09: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(9)]
    
    ctp05_10: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(10)]
    
    ctp05_11: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(11)]
    
    ctp05_12: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(12)]
    
    ctp05_13: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(13)]
    
    ctp05_14: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(14)]
    
    ctp05_15: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(15)]


class L2410_CTP(Segment):
    """Drug Pricing"""
    _segment_name = 'CTP'
    
    ctp01: Annotated[D_687, Title('Class of Trade Code'), Usage('N'), Position(1)]
    
    ctp02: Annotated[D_236, Title('Price Identifier Code'), Usage('N'), Position(2)]
    
    ctp03: Annotated[D_212, Title('Unit Price'), Usage('R'), Position(3)]
    
    ctp04: Annotated[D_380, Title('Quantity'), Usage('R'), Position(4)]
    
    c001: Annotated[L2410_C001, Title('Composite Unit of Measure'), Usage('R'), Position(5), Required(True)]
    
    ctp06: Annotated[D_648, Title('Price Multiplier Qualifier'), Usage('N'), Position(6)]
    
    ctp07: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(7)]
    
    ctp08: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]
    
    ctp09: Annotated[D_639, Title('Basis of Unit Price Code'), Usage('N'), Position(9)]
    
    ctp10: Annotated[D_499, Title('Condition Value'), Usage('N'), Position(10)]
    
    ctp11: Annotated[D_289, Title('Multiple Price Quantity'), Usage('N'), Position(11)]


class L2410_C040(Composite):
    """Reference Identifier"""
    pass


class L2410_REF(Segment):
    """Prescription Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['XZ'])]
    
    ref02: Annotated[D_127, Title('Reference Identification'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2410(Loop):
    
    lin: Annotated[L2410_LIN, Title('Drug Identification'), Usage('S'), Position(494), Syntax(['P0405', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425', 'P2627', 'P2829', 'P3031']), Required(True)]
    
    ctp: Annotated[L2410_CTP, Title('Drug Pricing'), Usage('S'), Position(495), Syntax(['P0405', 'C0607', 'C0902', 'C1002', 'C1103']), Required(True)]
    
    ref: Annotated[L2410_REF, Title('Prescription Number'), Usage('S'), Position(496), Required(True)]


class L2420A_NM1(Segment):
    """Attending Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['71'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Attending Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Attending Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Attending Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Attending Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Attending Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420A_PRV(Segment):
    """Attending Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AT'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420A_C040(Composite):
    """Reference Identifier"""
    pass


class L2420A_REF(Segment):
    """Attending Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Attending Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title('Attending Physician Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420A_PRV, Title('Attending Physician Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420A_REF, Title('Attending Physician Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2420B_NM1(Segment):
    """Operating Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Operating Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Operating Physician First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Operating Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Operating Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Operating Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420B_PRV(Segment):
    """Operating Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OP'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420B_C040(Composite):
    """Reference Identifier"""
    pass


class L2420B_REF(Segment):
    """Operating Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Operating Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title('Operating Physician Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420B_PRV, Title('Operating Physician Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420B_REF, Title('Operating Physician Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2420C_NM1(Segment):
    """Other Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['73'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Other Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420C_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420C_PRV(Segment):
    """Other Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OT', 'PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420C_C040(Composite):
    """Reference Identifier"""
    pass


class L2420C_REF(Segment):
    """Other Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Other Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title('Other Provider Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420C_PRV, Title('Other Provider Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420C_REF, Title('Other Provider Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2430_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svd03_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['HC', 'IV', 'ZZ'])]
    
    svd03_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]


class L2430_SVD(Segment):
    """Service Line Adjudication Information"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title('Payer Identifier'), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title('Service Line Paid Amount'), Usage('R'), Position(2)]
    
    c003: Annotated[L2430_C003, Title('Composite Medical Procedure Identifier'), Usage('S'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title('Service Line Revenue Code'), Usage('R'), Position(4)]
    
    svd05: Annotated[D_380, Title('Adjustment Quantity'), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title('Bundled or Unbundled Line Number'), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """Service Line Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Claim Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2430_DTP(Segment):
    """Service Adjudication Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Service Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title('Service Line Adjudication Information'), Usage('R'), Position(540), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title('Service Line Adjustment'), Usage('S'), Position(545), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    
    dtp: Annotated[L2430_DTP, Title('Service Adjudication Date'), Usage('S'), Position(550), Required(True)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title('Service Line Number'), Usage('R'), Position(365), Required(True)]
    
    sv2: Annotated[L2400_SV2, Title('Institutional Service Line'), Usage('R'), Position(375), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2400_PWK, Title('Line Supplemental Information'), Usage('S'), Position(420), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(5)]
    
    dtp: Annotated[L2400_DTP, Title('Service Line Date'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Assessment Date'), Usage('S'), Position(455), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Service Tax Amount'), Usage('S'), Position(475), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Facility Tax Amount'), Usage('S'), Position(475), Required(True)]
    
    hcp: Annotated[L2400_HCP, Title('Line Pricing/Repricing Information'), Usage('S'), Position(492), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2410: TypeAlias = Annotated[L2410, Title('Drug Identification'), Usage('S'), Position(494)]
    l2410: Annotated[list[ItemL2410], MinItems(25)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title('Attending Physician Name'), Usage('S'), Position(500), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title('Operating Physician Name'), Usage('S'), Position(500), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title('Other Provider Name'), Usage('S'), Position(500), Required(True)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title('Service Line Adjudication Information'), Usage('S'), Position(540), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(25)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title('Claim Information'), Usage('R'), Position(130), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Discharge Hour'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Statement Dates'), Usage('R'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Admission Date/Hour'), Usage('S'), Position(135), Required(True)]
    
    cl1: Annotated[L2300_CL1, Title('Institutional Claim Code'), Usage('S'), Position(140)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title('Claim Supplemental Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    cn1: Annotated[L2300_CN1, Title('Contract Information'), Usage('S'), Position(160), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Payer Estimated Amount Due'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Patient Estimated Amount Due'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Patient Paid Amount'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Credit/Debit Card Maximum Amount'), Usage('S'), Position(175), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Adjusted Repriced Claim Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Repriced Claim Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Claim Identification Number For Clearinghouses and Other Transmission Intermediaries'), Usage('S'), Position(180), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Document Identification Code'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2300_REF, Title('Original Reference Number (ICN/DCN)'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Investigational Device Exemption Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Service Authorization Exception Code'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Peer Review Organization (PRO) Approval Number'), Usage('S'), Position(180), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Prior Authorization or Referral Number'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2300_REF, Title('Medical Record Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Demonstration Project Identifier'), Usage('S'), Position(180), Required(True)]
    ItemK3: TypeAlias = Annotated[L2300_K3, Title('File Information'), Usage('S'), Position(185), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    ItemNte: TypeAlias = Annotated[L2300_NTE, Title('Claim Note'), Usage('S'), Position(190), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(10)]
    
    nte: Annotated[L2300_NTE, Title('Billing Note'), Usage('S'), Position(190), Required(True)]
    
    cr6: Annotated[L2300_CR6, Title('Home Health Care Information'), Usage('S'), Position(216), Required(True)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Home Health Functional Limitations'), Usage('S'), Position(220), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Home Health Activities Permitted'), Usage('S'), Position(220), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Home Health Mental Status'), Usage('S'), Position(220), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(2)]
    
    hi: Annotated[L2300_HI, Title('Principal, Admitting, E-Code and Patient Reason for Visit Diagnosis Information'), Usage('S'), Position(231), Required(True)]
    
    hi: Annotated[L2300_HI, Title('Diagnosis Related Group (DRG) Information'), Usage('S'), Position(231), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Other Diagnosis Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hi: Annotated[L2300_HI, Title('Principal Procedure Information'), Usage('S'), Position(231), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Other Procedure Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Occurrence Span Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Occurrence Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Value Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Condition Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Treatment Code Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemQty: TypeAlias = Annotated[L2300_QTY, Title('Claim Quantity'), Usage('S'), Position(240), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(4)]
    
    hcp: Annotated[L2300_HCP, Title('Claim Pricing/Repricing Information'), Usage('S'), Position(241), Required(True)]
    ItemL2305: TypeAlias = Annotated[L2305, Title('Home Health Care Plan Information'), Usage('S'), Position(242), Required(True)]
    l2305: Annotated[list[ItemL2305], MinItems(6)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title('Attending Physician Name'), Usage('S'), Position(250), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(1)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title('Operating Physician Name'), Usage('S'), Position(250), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title('Other Provider Name'), Usage('S'), Position(250), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310E: TypeAlias = Annotated[L2310E, Title('Service Facility Name'), Usage('S'), Position(250), Required(True)]
    l2310e: Annotated[list[ItemL2310E], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title('Other Subscriber Information'), Usage('S'), Position(290), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title('Service Line Number'), Usage('R'), Position(365), Required(True)]
    l2400: Annotated[list[ItemL2400], MinItems(999)]


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
    
    pat01: Annotated[D_1069, Title('Patients Relationship to Insured'), Usage('R'), Position(1), Enumerated(*['01', '04', '05', '07', '10', '15', '17', '19', '20', '21', '22', '23', '24', '29', '32', '33', '36', '39', '40', '41', '43', '53', 'G8'])]
    
    pat02: Annotated[D_1384, Title('Patient Location Code'), Usage('N'), Position(2)]
    
    pat03: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(3)]
    
    pat04: Annotated[D_1220, Title('Student Status Code'), Usage('N'), Position(4)]
    
    pat05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    pat06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]
    
    pat07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(7)]
    
    pat08: Annotated[D_81, Title('Patient Weight'), Usage('N'), Position(8)]
    
    pat09: Annotated[D_1073, Title('Pregnancy Indicator'), Usage('N'), Position(9)]


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
    
    n301: Annotated[D_166, Title('Patient Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Patient Address Line'), Usage('S'), Position(2)]


class L2010CA_N4(Segment):
    """Patient City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Patient City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Patient State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Patient Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
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
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7), Enumerated(*country)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]


class L2010CA_C040(Composite):
    """Reference Identifier"""
    pass


class L2010CA_REF(Segment):
    """Patient Secondary Identification Number"""
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
    ItemRef: TypeAlias = Annotated[L2010CA_REF, Title('Patient Secondary Identification Number'), Usage('S'), Position(35), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2010CA_REF, Title('Property and Casualty Claim Number'), Usage('S'), Position(35), Required(True)]


class L2300_C023(Composite):
    """Type of Bill"""
    
    clm05_01: Annotated[D_1331, Title('Facility Type Code'), Usage('R'), Position(1)]
    
    clm05_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('R'), Position(2), Enumerated(*['A'])]
    
    clm05_03: Annotated[D_1325, Title('Claim Frequency Code'), Usage('R'), Position(3), Enumerated(*['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'X', 'Y', 'Z '])]


class L2300_C024(Composite):
    """Property and Casualty Related Causes Codes"""
    pass


class L2300_CLM(Segment):
    """Claim Information"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title('Patient Account Number'), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title('Non-Institutional Claim Type Code'), Usage('N'), Position(4)]
    
    c023: Annotated[L2300_C023, Title('Type of Bill'), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title('Provider or Supplier Signature Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]
    
    clm07: Annotated[D_1359, Title('Medicare Assignment Code'), Usage('S'), Position(7), Enumerated(*['A', 'C'])]
    
    clm08: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(8), Enumerated(*['N', 'Y'])]
    
    clm09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['A', 'I', 'M', 'N', 'O', 'Y'])]
    
    clm10: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('N'), Position(10)]
    
    clm12: Annotated[D_1366, Title('Special Program Indicator'), Usage('N'), Position(12), Enumerated(*['01', '02', '03', '05', '07', '08', '09'])]
    
    clm13: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title('Level of Service Code'), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title('Claim Status Code'), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title('Explanation of Benefits Indicator'), Usage('R'), Position(18), Enumerated(*['N', 'Y'])]
    
    clm19: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(19)]
    
    clm20: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(20), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])]


class L2300_DTP(Segment):
    """Discharge Hour"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['TM'])]
    
    dtp03: Annotated[D_1251, Title('Discharge Hour'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Statement Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['434'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Statement From or To Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Admission Date/Hour"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['DT'])]
    
    dtp03: Annotated[D_1251, Title('Admission Date and Hour'), Usage('R'), Position(3)]


class L2300_CL1(Segment):
    """Institutional Claim Code"""
    _segment_name = 'CL1'
    
    cl101: Annotated[D_1315, Title('Admission Type Code'), Usage('S'), Position(1)]
    
    cl102: Annotated[D_1314, Title('Admission Source Code'), Usage('S'), Position(2)]
    
    cl103: Annotated[D_1352, Title('Patient Status Code'), Usage('S'), Position(3)]
    
    cl104: Annotated[D_1345, Title('Nursing Home Residential Status Code'), Usage('N'), Position(4)]


class L2300_C002(Composite):
    """Actions Indicated"""
    pass


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['AS', 'B2', 'B3', 'B4', 'CT', 'DA', 'DG', 'DS', 'EB', 'MT', 'NN', 'OB', 'OZ', 'PN', 'PO', 'PZ', 'RB', 'RR', 'RT'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Attachment Description'), Usage('S'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2300_CN1(Segment):
    """Contract Information"""
    _segment_name = 'CN1'
    
    cn101: Annotated[D_1166, Title('Contract Type Code'), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '09'])]
    
    cn102: Annotated[D_782, Title('Contract Amount'), Usage('S'), Position(2)]
    
    cn103: Annotated[D_332, Title('Contract Percentage'), Usage('S'), Position(3)]
    
    cn104: Annotated[D_127, Title('Contract Code'), Usage('S'), Position(4)]
    
    cn105: Annotated[D_338, Title('Terms Discount Percentage'), Usage('S'), Position(5)]
    
    cn106: Annotated[D_799, Title('Contract Version Identifier'), Usage('S'), Position(6)]


class L2300_AMT(Segment):
    """Payer Estimated Amount Due"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['C5'])]
    
    amt02: Annotated[D_782, Title('Estimated Claim Due Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Patient Estimated Amount Due"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F3'])]
    
    amt02: Annotated[D_782, Title('Patient Responsibility Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Patient Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Patient Amount Paid'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_AMT(Segment):
    """Credit/Debit Card Maximum Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['MA'])]
    
    amt02: Annotated[D_782, Title('Credit or Debit Card Maximum Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Adjusted Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9C'])]
    
    ref02: Annotated[D_127, Title('Adjusted Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9A'])]
    
    ref02: Annotated[D_127, Title('Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Claim Identification Number For Clearinghouses and Other Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Value Added Network Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Document Identification Code"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['DD'])]
    
    ref02: Annotated[D_127, Title('Document Control Identifier'), Usage('R'), Position(2)]
    
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
    """Investigational Device Exemption Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['LX'])]
    
    ref02: Annotated[D_127, Title('Investigational Device Exemption Identifier'), Usage('R'), Position(2)]
    
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
    """Peer Review Organization (PRO) Approval Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G4'])]
    
    ref02: Annotated[D_127, Title('Peer Review Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Prior Authorization or Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F', 'G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Medical Record Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title('Medical Record Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C040(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Demonstration Project Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['P4'])]
    
    ref02: Annotated[D_127, Title('Demonstration Project Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2300_K3(Segment):
    """File Information"""
    _segment_name = 'K3'
    
    k301: Annotated[D_449, Title('Fixed Format Information'), Usage('R'), Position(1)]
    
    k302: Annotated[D_1333, Title('Record Format Code'), Usage('N'), Position(2)]


class L2300_NTE(Segment):
    """Claim Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ALG', 'DCP', 'DGN', 'DME', 'MED', 'NTR', 'ODT', 'RHB', 'RLH', 'RNH', 'SET', 'SFM', 'SPT', 'UPI'])]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2300_NTE(Segment):
    """Billing Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD'])]
    
    nte02: Annotated[D_352, Title('Billing Note Text'), Usage('R'), Position(2)]


class L2300_CR6(Segment):
    """Home Health Care Information"""
    _segment_name = 'CR6'
    
    cr601: Annotated[D_923, Title('Prognosis Indicator'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8'])]
    
    cr602: Annotated[D_373, Title('Service From Date'), Usage('R'), Position(2)]
    
    cr603: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['RD8'])]
    
    cr604: Annotated[D_1251, Title('Home Health Certification Period'), Usage('S'), Position(4)]
    
    cr605: Annotated[D_373, Title('Diagnosis Date'), Usage('R'), Position(5)]
    
    cr606: Annotated[D_1073, Title('Skilled Nursing Facility Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'U', 'Y'])]
    
    cr607: Annotated[D_1073, Title('Medicare Coverage Indicator'), Usage('R'), Position(7), Enumerated(*['N', 'Y'])]
    
    cr608: Annotated[D_1322, Title('Certification Type Indicator'), Usage('R'), Position(8), Enumerated(*['I', 'R', 'S'])]
    
    cr609: Annotated[D_373, Title('Surgery Date'), Usage('S'), Position(9)]
    
    cr610: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(10), Enumerated(*['HC', 'ID'])]
    
    cr611: Annotated[D_1137, Title('Surgical Procedure Code'), Usage('S'), Position(11)]
    
    cr612: Annotated[D_373, Title('Physician Order Date'), Usage('S'), Position(12)]
    
    cr613: Annotated[D_373, Title('Last Visit Date'), Usage('S'), Position(13)]
    
    cr614: Annotated[D_373, Title('Physician Contact Date'), Usage('S'), Position(14)]
    
    cr615: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(15), Enumerated(*['RD8'])]
    
    cr616: Annotated[D_1251, Title('Last Admission Period'), Usage('S'), Position(16)]
    
    cr617: Annotated[D_1384, Title('Patient Discharge Facility Type Code'), Usage('R'), Position(17), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M', 'O', 'R', 'S', 'T'])]
    
    cr618: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(18)]
    
    cr619: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(19)]
    
    cr620: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(20)]
    
    cr621: Annotated[D_373, Title('Diagnosis Date'), Usage('S'), Position(21)]


class L2300_CRC(Segment):
    """Home Health Functional Limitations"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['75'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Functional Limitation Code'), Usage('R'), Position(3), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc04: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(4), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc05: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(5), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc06: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(6), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]
    
    crc07: Annotated[D_1321, Title('Functional Limitation Code'), Usage('S'), Position(7), Enumerated(*['AA', 'AL', 'BL', 'CO', 'DY', 'EL', 'HL', 'LB', 'OL', 'PA', 'SL'])]


class L2300_CRC(Segment):
    """Home Health Activities Permitted"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Certification Condition Indicator'), Usage('R'), Position(1), Enumerated(*['76'])]
    
    crc02: Annotated[D_1073, Title(' Functional Limitation Code'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Activities Permitted Code'), Usage('R'), Position(3), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc04: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(4), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc05: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(5), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc06: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(6), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]
    
    crc07: Annotated[D_1321, Title('Activities Permitted Code'), Usage('S'), Position(7), Enumerated(*['BR', 'CA', 'CB', 'CR', 'EP', 'IH', 'NR', 'PW', 'TR', 'UT', 'WA', 'WR'])]


class L2300_CRC(Segment):
    """Home Health Mental Status"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Certification Condition Indicator'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    crc02: Annotated[D_1073, Title('Functional Limitation Code'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Mental Status Code'), Usage('R'), Position(3), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc04: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(4), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc05: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(5), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc06: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(6), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]
    
    crc07: Annotated[D_1321, Title('Mental Status Code'), Usage('S'), Position(7), Enumerated(*['AG', 'CM', 'DI', 'DP', 'FO', 'LE', 'MC', 'OT'])]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BK'])]
    
    hi01_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BJ', 'ZZ'])]
    
    hi02_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BN'])]
    
    hi03_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Principal, Admitting, E-Code and Patient Reason for Visit Diagnosis Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['DR'])]
    
    hi01_02: Annotated[D_1271, Title('Diagnosis Related Group (DRG) Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Diagnosis Related Group (DRG) Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi01_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi02_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi03_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi04_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi05_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi06_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi07_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi08_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi09_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi10_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi11_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BF'])]
    
    hi12_02: Annotated[D_1271, Title('Other Diagnosis'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Other Diagnosis Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BP', 'BR'])]
    
    hi01_02: Annotated[D_1271, Title('Principal Procedure Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_C022(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Principal Procedure Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi01_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi02_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi03_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi04_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi05_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi06_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi07_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi08_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi09_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi10_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi11_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'BQ'])]
    
    hi12_02: Annotated[D_1271, Title('Procedure Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title('Procedure Date'), Usage('S'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Other Procedure Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi01_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi01_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi02_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi02_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi03_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi03_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi04_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi04_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi05_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi05_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi06_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi06_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi07_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi07_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi08_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi08_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi09_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi09_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi10_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi10_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi11_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi11_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi12_02: Annotated[D_1271, Title('Occurrence Span Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi12_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Occurrence Span Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi01_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi02_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi03_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi04_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi05_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi06_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi07_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi08_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi09_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi10_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi11_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi12_02: Annotated[D_1271, Title('Occurrence Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title('Occurrence or Occurrence Span Code Associated Date'), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Occurrence Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi01_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi02_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi03_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi04_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi05_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi06_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('n Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi07_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi08_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi09_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi10_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi11_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi12_02: Annotated[D_1271, Title('Value Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Value Code Associated Amount'), Usage('R'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Value Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi01_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi02_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi03_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi04_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi05_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi06_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi07_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi08_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi09_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi10_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi11_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi12_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Condition Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi01_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi02_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi03_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi04_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi05_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi06_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi07_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi08_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi09_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi10_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi11_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_C022(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi12_02: Annotated[D_1271, Title('Treatment Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]


class L2300_HI(Segment):
    """Treatment Code Information"""
    _segment_name = 'HI'
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    c022: Annotated[L2300_C022, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_C001(Composite):
    """Composite Unit of Measure"""
    
    qty03_01: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(1), Enumerated(*['DA'])]
    
    qty03_02: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(2)]
    
    qty03_03: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(3)]
    
    qty03_04: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(4)]
    
    qty03_05: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(5)]
    
    qty03_06: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(6)]
    
    qty03_07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(7)]
    
    qty03_08: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(8)]
    
    qty03_09: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(9)]
    
    qty03_10: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(10)]
    
    qty03_11: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(11)]
    
    qty03_12: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(12)]
    
    qty03_13: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(13)]
    
    qty03_14: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(14)]
    
    qty03_15: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(15)]


class L2300_QTY(Segment):
    """Claim Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['CA', 'CD', 'LA', 'NA'])]
    
    qty02: Annotated[D_380, Title('Claim Days Count'), Usage('R'), Position(2)]
    
    c001: Annotated[L2300_C001, Title('Composite Unit of Measure'), Usage('R'), Position(3), Required(True)]
    
    qty04: Annotated[D_61, Title('Free-Form Message'), Usage('N'), Position(4)]


class L2300_HCP(Segment):
    """Claim Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repricing Organization Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved DRG Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Repriced Approved Revenue Code'), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(9), Enumerated(*['HC'])]
    
    hcp10: Annotated[D_234, Title('Repriced Approved HCPCS Code'), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title('Repriced Approved Service Unit Count'), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Rejection Message'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Reason Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2305_CR7(Segment):
    """Home Health Care Plan Information"""
    _segment_name = 'CR7'
    
    cr701: Annotated[D_921, Title('Discipline Type Code'), Usage('R'), Position(1), Enumerated(*['AI', 'MS', 'OT', 'PT', 'SN', 'ST'])]
    
    cr702: Annotated[D_1470, Title('Visits Prior to Recertification Date Count'), Usage('R'), Position(2)]
    
    cr703: Annotated[D_1470, Title('Total Visits Projected This Certification Count'), Usage('R'), Position(3)]


class L2305_HSD(Segment):
    """Health Care Services Delivery"""
    _segment_name = 'HSD'
    
    hsd01: Annotated[D_673, Title('Visits'), Usage('S'), Position(1), Enumerated(*['VS'])]
    
    hsd02: Annotated[D_380, Title('Number of Visits'), Usage('S'), Position(2)]
    
    hsd03: Annotated[D_355, Title('Frequency Period'), Usage('S'), Position(3), Enumerated(*['DA', 'MO', 'Q1', 'WK'])]
    
    hsd04: Annotated[D_1167, Title('Frequency Count'), Usage('S'), Position(4)]
    
    hsd05: Annotated[D_615, Title('Duration of Visits Units'), Usage('S'), Position(5), Enumerated(*['7', '35'])]
    
    hsd06: Annotated[D_616, Title('Duration of Visits, Number of Units'), Usage('S'), Position(6)]
    
    hsd07: Annotated[D_678, Title('Ship, Delivery or Calendar Pattern Code'), Usage('S'), Position(7), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'N', 'O', 'S', 'SA', 'SB', 'SC', 'SD', 'SG', 'SL', 'SP', 'SX', 'SY', 'SZ', 'W'])]
    
    hsd08: Annotated[D_679, Title('Delivery Pattern Time Code'), Usage('S'), Position(8), Enumerated(*['D', 'E', 'F'])]


class L2305(Loop):
    
    cr7: Annotated[L2305_CR7, Title('Home Health Care Plan Information'), Usage('R'), Position(242), Required(True)]
    ItemHsd: TypeAlias = Annotated[L2305_HSD, Title('Health Care Services Delivery'), Usage('S'), Position(243)]
    hsd: Annotated[list[ItemHsd], MaxItems(12)]


class L2310A_NM1(Segment):
    """Attending Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['71'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Attending Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Attending Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Attending Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Attending Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Attending Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310A_PRV(Segment):
    """Attending Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AT', 'SU'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4), Enumerated(*states)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310A_C040(Composite):
    """Reference Identifier"""
    pass


class L2310A_REF(Segment):
    """Attending Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Attending Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title('Attending Physician Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310A_PRV, Title('Attending Physician Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title('Attending Physician Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310B_NM1(Segment):
    """Operating Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Operating Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Operating Physician First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Operating Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Operating Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Operating Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310B_PRV(Segment):
    """Operating Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OP'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310B_C040(Composite):
    """Reference Identifier"""
    pass


class L2310B_REF(Segment):
    """Operating Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Operating Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title('Operating Physician Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310B_PRV, Title('Operating Physician Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title('Operating Physician Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310C_NM1(Segment):
    """Other Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['73'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Other Physician Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310C_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310C_PRV(Segment):
    """Other Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OT', 'PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310C_C040(Composite):
    """Reference Identifier"""
    pass


class L2310C_REF(Segment):
    """Other Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Other Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title('Other Provider Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310C_PRV, Title('Other Provider Specialty Information'), Usage('S'), Position(255), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title('Other Provider Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2310E_NM1(Segment):
    """Service Facility Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['FA'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2310E_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2310E_PRV(Segment):
    """Service Facility Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['RP'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310E_N3(Segment):
    """Service Facility Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('S'), Position(2)]


class L2310E_N4(Segment):
    """Service Facility City/State/Zip Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Laboratory or Facility City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Laboratory or Facility State or Province Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Laboratory or Facility Postal Zone or Zip Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Laboratory/Facility Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2310E_C040(Composite):
    """Reference Identifier"""
    pass


class L2310E_REF(Segment):
    """Service Facility Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'EI', 'FH', 'G2', 'G5', 'LU', 'N5', 'X5'])]
    
    ref02: Annotated[D_127, Title('Laboratory or Facility Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310E(Loop):
    
    nm1: Annotated[L2310E_NM1, Title('Service Facility Name'), Usage('R'), Position(250), Required(True)]
    
    prv: Annotated[L2310E_PRV, Title('Service Facility Specialty Information'), Usage('S'), Position(255), Required(True)]
    
    n3: Annotated[L2310E_N3, Title('Service Facility Address'), Usage('R'), Position(265), Required(True)]
    
    n4: Annotated[L2310E_N4, Title('Service Facility City/State/Zip Code'), Usage('R'), Position(270), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310E_REF, Title('Service Facility Secondary Identification'), Usage('S'), Position(271), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['P', 'S', 'T'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '04', '05', '07', '10', '15', '17', '18', '19', '20', '21', '22', '23', '24', '29', '32', '33', '36', '39', '40', '41', '43', '53', 'G8'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Other Insured Group Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['09', '10', '11', '12', '13', '14', '15', '16', 'AM', 'BL', 'CH', 'CI', 'DS', 'HM', 'LI', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """Claim Level Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Claim Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2320_AMT(Segment):
    """Payer Prior Payment"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['C4'])]
    
    amt02: Annotated[D_782, Title('Other Payer Patient Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Allowed Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B6'])]
    
    amt02: Annotated[D_782, Title('Allowed Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Submitted Charges"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T3'])]
    
    amt02: Annotated[D_782, Title('Coordination of Benefits Total Submitted Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Diagnostic Related Group (DRG) Outlier Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    amt02: Annotated[D_782, Title('Claim DRG Outlier Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Medicare Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['N1'])]
    
    amt02: Annotated[D_782, Title('Total Medicare Paid Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Medicare Paid Amount - 100%"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['KF'])]
    
    amt02: Annotated[D_782, Title('Medicare Paid at 100% Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Medicare Paid Amount - 80%"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['PG'])]
    
    amt02: Annotated[D_782, Title('Medicare Paid at 80% Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Medicare A Trust Fund Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AA'])]
    
    amt02: Annotated[D_782, Title('Paid From Part A Medicare Trust Fund Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Medicare B Trust Fund Paid Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B1'])]
    
    amt02: Annotated[D_782, Title('Paid From Part B Medicare Trust Fund Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Non-Covered Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['A8'])]
    
    amt02: Annotated[D_782, Title('Non-Covered Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Coordination of Benefits (COB) Total Denied Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['YT'])]
    
    amt02: Annotated[D_782, Title('Claim Total Denied Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_DMG(Segment):
    """Other Subscriber Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Other Insured Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Other Insured Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg05: Annotated[D_1109, Title('nicity Code'), Usage('N'), Position(5)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7), Enumerated(*country)]
    
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
    
    oi06: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(6), Enumerated(*['A', 'I', 'M', 'N', 'O', 'Y'])]


class L2320_MIA(Segment):
    """Medicare Inpatient Adjudication Information"""
    _segment_name = 'MIA'
    
    mia01: Annotated[D_380, Title('Covered Days or Visits Count'), Usage('R'), Position(1)]
    
    mia02: Annotated[D_380, Title('Lifetime Reserve Days Count'), Usage('S'), Position(2)]
    
    mia03: Annotated[D_380, Title('Lifetime Psychiatric Days Count'), Usage('S'), Position(3)]
    
    mia04: Annotated[D_782, Title('Claim DRG Amount'), Usage('S'), Position(4)]
    
    mia05: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(5), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia06: Annotated[D_782, Title('Claim Disproportionate Share Amount'), Usage('S'), Position(6)]
    
    mia07: Annotated[D_782, Title('Claim MSP Pass-through Amount'), Usage('S'), Position(7)]
    
    mia08: Annotated[D_782, Title('Claim PPS Capital Amount'), Usage('S'), Position(8)]
    
    mia09: Annotated[D_782, Title('PPS-Capital FSP DRG Amount'), Usage('S'), Position(9)]
    
    mia10: Annotated[D_782, Title('PPS-Capital HSP DRG Amount'), Usage('S'), Position(10)]
    
    mia11: Annotated[D_782, Title('PPS-Capital DSH DRG Amount'), Usage('S'), Position(11)]
    
    mia12: Annotated[D_782, Title('Old Capital Amount'), Usage('S'), Position(12)]
    
    mia13: Annotated[D_782, Title('PPS-Capital IME Amount'), Usage('S'), Position(13)]
    
    mia14: Annotated[D_782, Title('PPS-Operating Hospital Specific DRG Amount'), Usage('S'), Position(14)]
    
    mia15: Annotated[D_380, Title('Cost Report Day Count'), Usage('S'), Position(15)]
    
    mia16: Annotated[D_782, Title('PPS-Operating Federal Specific DRG Amount'), Usage('S'), Position(16)]
    
    mia17: Annotated[D_782, Title('Claim PPS Capital Outlier Amount'), Usage('S'), Position(17)]
    
    mia18: Annotated[D_782, Title('Claim Indirect Teaching Amount'), Usage('S'), Position(18)]
    
    mia19: Annotated[D_782, Title('Nonpayable Professional Component Amount'), Usage('S'), Position(19)]
    
    mia20: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(20), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia21: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(21), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia22: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(22), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia23: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(23), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    mia24: Annotated[D_782, Title('PPS-Capital Exception Amount'), Usage('S'), Position(24)]


class L2320_MOA(Segment):
    """Medicare Outpatient Adjudication Information"""
    _segment_name = 'MOA'
    
    moa01: Annotated[D_954, Title('Reimbursement Rate'), Usage('S'), Position(1)]
    
    moa02: Annotated[D_782, Title('Claim HCPCS Payable Amount'), Usage('S'), Position(2)]
    
    moa03: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(3), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa04: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(4), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa05: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(5), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa06: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(6), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa07: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(7), Enumerated(*['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36', 'M37', 'M38', 'M39', 'M40', 'M41', 'M42', 'M43', 'M44', 'M45', 'M46', 'M47', 'M48', 'M49', 'M50', 'M51', 'M52', 'M53', 'M54', 'M55', 'M56', 'M57', 'M58', 'M59', 'M60', 'M61', 'M62', 'M63', 'M64', 'M65', 'M66', 'M67', 'M68', 'M69', 'M70', 'M71', 'M72', 'M73', 'M74', 'M75', 'M76', 'M77', 'M78', 'M79', 'M80', 'M81', 'M82', 'M83', 'M84', 'M85', 'M86', 'M87', 'M88', 'M89', 'M90', 'M91', 'M92', 'M93', 'M94', 'M95', 'M96', 'M97', 'M98', 'M99', 'M100', 'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110', 'M111', 'M112', 'M113', 'M114', 'M115', 'M116', 'M117', 'M118', 'M119', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M131', 'M132', 'M133', 'M134', 'M135', 'M136', 'M137', 'M138', 'M139', 'M140', 'M141', 'M142', 'M143', 'M144', 'MA01', 'MA02', 'MA03', 'MA04', 'MA05', 'MA06', 'MA07', 'MA08', 'MA09', 'MA10', 'MA11', 'MA12', 'MA13', 'MA14', 'MA15', 'MA16', 'MA17', 'MA18', 'MA19', 'MA20', 'MA21', 'MA22', 'MA23', 'MA24', 'MA25', 'MA26', 'MA27', 'MA28', 'MA29', 'MA30', 'MA31', 'MA32', 'MA33', 'MA34', 'MA35', 'MA36', 'MA37', 'MA38', 'MA39', 'MA40', 'MA41', 'MA42', 'MA43', 'MA44', 'MA45', 'MA46', 'MA47', 'MA48', 'MA49', 'MA50', 'MA51', 'MA52', 'MA53', 'MA54', 'MA55', 'MA56', 'MA57', 'MA58', 'MA59', 'MA60', 'MA61', 'MA62', 'MA63', 'MA64', 'MA65', 'MA66', 'MA67', 'MA68', 'MA69', 'MA70', 'MA71', 'MA72', 'MA73', 'MA74', 'MA75', 'MA76', 'MA77', 'MA78', 'MA79', 'MA80', 'MA81', 'MA82', 'MA83', 'MA84', 'MA85', 'MA86', 'MA87', 'MA88', 'MA89', 'MA90', 'MA91', 'MA92', 'MA93', 'MA94', 'MA95', 'MA96', 'MA97', 'MA98', 'MA99', 'MA100', 'MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107', 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115', 'MA116', 'MA117', 'MA118', 'MA119', 'MA120', 'MA121', 'MA122', 'MA123', 'MA124', 'MA125', 'MA126', 'MA127', 'MA128', 'MA129', 'MA130', 'MA131', 'MA132', 'MA133', 'MA134', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24', 'N25', 'N26', 'N27', 'N28', 'N29', 'N30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'N46', 'N47', 'N48', 'N49', 'N50', 'N51', 'N52', 'N53', 'N54', 'N55', 'N56', 'N57', 'N58', 'N59', 'N60', 'N61', 'N62', 'N63', 'N64', 'N65', 'N66', 'N67', 'N68', 'N69', 'N70', 'N71', 'N72', 'N73', 'N74', 'N75', 'N76', 'N77', 'N78', 'N79', 'N80', 'N81', 'N82', 'N83', 'N84', 'N85', 'N86', 'N87', 'N88', 'N89', 'N90', 'N91', 'N92', 'N93', 'N94', 'N95', 'N96', 'N97', 'N98', 'N99', 'N100', 'N101', 'N102', 'N103', 'N104', 'N105', 'N106', 'N107', 'N108', 'N109', 'N110', 'N111', 'N112', 'N113', 'N114', 'N115', 'N116', 'N117', 'N118', 'N119', 'N120', 'N121', 'N122', 'N123', 'N124', 'N125', 'N126', 'N127', 'N128', 'N129', 'N130', 'N131', 'N132', 'N133', 'N134', 'N135', 'N136', 'N137', 'N138', 'N139', 'N140', 'N141', 'N142', 'N143', 'N144', 'N145', 'N146', 'N147', 'N148', 'N149', 'N150', 'N151', 'N152', 'N153', 'N154', 'N155', 'N156 '])]
    
    moa08: Annotated[D_782, Title('Claim ESRD Payment Amount'), Usage('S'), Position(8)]
    
    moa09: Annotated[D_782, Title('Nonpayable Professional Component Amount'), Usage('S'), Position(9)]


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Insured Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Insured First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Insured Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('fix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Insured Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['MI', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Other Insured Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Insured Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Insured Address Line'), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """Other Subscriber City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Insured City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Insured State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Insured Postal Zone or Zip Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Subscriber Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2330A_C040(Composite):
    """Reference Identifier"""
    pass


class L2330A_REF(Segment):
    """Other Subscriber Secondary Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', '23', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Insured Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    
    n3: Annotated[L2330A_N3, Title('Other Subscriber Address'), Usage('S'), Position(332), Required(True)]
    
    n4: Annotated[L2330A_N4, Title('Other Subscriber City/State/ZIP Code'), Usage('S'), Position(340), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330A_REF, Title('Other Subscriber Secondary Information'), Usage('S'), Position(355), Required(True)]
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


class L2330B_N3(Segment):
    """Other Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Payer Address Line'), Usage('S'), Position(2)]


class L2330B_N4(Segment):
    """Other Payer City/State/ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Payer State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Payer Postal Zone or Zip Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Payer Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L2330B_DTP(Segment):
    """Claim Adjudication Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2330B_C040(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Secondary Identification and Reference Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'F8', 'FY', 'NF', 'TJ'])]
    
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


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    
    n3: Annotated[L2330B_N3, Title('Other Payer Address'), Usage('S'), Position(332), Required(True)]
    
    n4: Annotated[L2330B_N4, Title('Other Payer City/State/ZIP Code'), Usage('S'), Position(340), Required(True)]
    
    dtp: Annotated[L2330B_DTP, Title('Claim Adjudication Date'), Usage('S'), Position(350), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Secondary Identification and Reference Number'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Prior Authorization or Referral Number'), Usage('S'), Position(355), Required(True)]


class L2330C_NM1(Segment):
    """Other Payer Patient Information"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['EI', 'MI'])]
    
    nm109: Annotated[D_67, Title('Other Payer Patient Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330C_C040(Composite):
    """Reference Identifier"""
    pass


class L2330C_REF(Segment):
    """Other Payer identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Payer Patient Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title('Other Payer Patient Information'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title('Other Payer identification Number'), Usage('S'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330D_NM1(Segment):
    """Other Payer Attending Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['71'])]
    
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
    """Other Payer Attending Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5'])]
    
    ref02: Annotated[D_127, Title('Other Payer Attending Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title('Other Payer Attending Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title('Other Payer Attending Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330E_NM1(Segment):
    """Other Payer Operating Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
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
    """Other Payer Operating Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5'])]
    
    ref02: Annotated[D_127, Title('Other Payer Operating Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title('Other Payer Operating Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title('Other Payer Operating Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330F_NM1(Segment):
    """Other Payer Other Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['73'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('fier Code'), Usage('N'), Position(11)]


class L2330F_C040(Composite):
    """Reference Identifier"""
    pass


class L2330F_REF(Segment):
    """Other Payer Other Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Payer Other Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('on'), Usage('N'), Position(3)]


class L2330F(Loop):
    
    nm1: Annotated[L2330F_NM1, Title('Other Payer Other Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330F_REF, Title('Other Payer Other Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330H_NM1(Segment):
    """Other Payer Service Facility Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['FA'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('ode Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2330H_C040(Composite):
    """Reference Identifier"""
    pass


class L2330H_REF(Segment):
    """Other Payer Service Facility Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1B', '1C', '1D', 'EI', 'G2', 'LU', 'N5'])]
    
    ref02: Annotated[D_127, Title('Other Payer Service Facility Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330H(Loop):
    
    nm1: Annotated[L2330H_NM1, Title('Other Payer Service Facility Provider'), Usage('R'), Position(325), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330H_REF, Title('Other Payer Service Facility Provider Identification'), Usage('R'), Position(355), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title('Other Subscriber Information'), Usage('R'), Position(290), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title('Claim Level Adjustment'), Usage('S'), Position(295), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title('Payer Prior Payment'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Allowed Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Submitted Charges'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Diagnostic Related Group (DRG) Outlier Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Medicare Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Medicare Paid Amount - 100%'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Medicare Paid Amount - 80%'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Medicare A Trust Fund Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Medicare B Trust Fund Paid Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Non-Covered Amount'), Usage('S'), Position(300), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Denied Amount'), Usage('S'), Position(300), Required(True)]
    
    dmg: Annotated[L2320_DMG, Title('Other Subscriber Demographic Information'), Usage('S'), Position(305), Required(True)]
    
    oi: Annotated[L2320_OI, Title('Other Insurance Coverage Information'), Usage('R'), Position(310), Required(True)]
    
    mia: Annotated[L2320_MIA, Title('Medicare Inpatient Adjudication Information'), Usage('S'), Position(315), Required(True)]
    
    moa: Annotated[L2320_MOA, Title('Medicare Outpatient Adjudication Information'), Usage('S'), Position(320)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title('Other Subscriber Name'), Usage('R'), Position(325), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title('Other Payer Name'), Usage('R'), Position(325), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title('Other Payer Patient Information'), Usage('S'), Position(325), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(1)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title('Other Payer Attending Provider'), Usage('S'), Position(325), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title('Other Payer Operating Provider'), Usage('S'), Position(325), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]
    ItemL2330F: TypeAlias = Annotated[L2330F, Title('Other Payer Other Provider'), Usage('S'), Position(325), Required(True)]
    l2330f: Annotated[list[ItemL2330F], MinItems(1)]
    ItemL2330H: TypeAlias = Annotated[L2330H, Title('Other Payer Service Facility Provider'), Usage('S'), Position(325), Required(True)]
    l2330h: Annotated[list[ItemL2330H], MinItems(1)]


class L2400_LX(Segment):
    """Service Line Number"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]


class L2400_C003(Composite):
    """Service Line Procedure Code"""
    
    sv202_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['HC', 'IV', 'N4', 'ZZ'])]
    
    sv202_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv202_03: Annotated[D_1339, Title('HCPCS Modifier 1'), Usage('S'), Position(3)]
    
    sv202_04: Annotated[D_1339, Title('HCPCS Modifier 2'), Usage('S'), Position(4)]
    
    sv202_05: Annotated[D_1339, Title('HCPCS Modifier 3'), Usage('S'), Position(5)]
    
    sv202_06: Annotated[D_1339, Title('HCPCS Modifier 4'), Usage('S'), Position(6)]
    
    sv202_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2400_SV2(Segment):
    """Institutional Service Line"""
    _segment_name = 'SV2'
    
    sv201: Annotated[D_234, Title('Service Line Revenue Code'), Usage('R'), Position(1)]
    
    c003: Annotated[L2400_C003, Title('Service Line Procedure Code'), Usage('S'), Position(2), Required(True)]
    
    sv203: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(3)]
    
    sv204: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(4), Enumerated(*['DA', 'F2', 'UN'])]
    
    sv205: Annotated[D_380, Title('Service Unit Count'), Usage('R'), Position(5)]
    
    sv206: Annotated[D_1371, Title('Service Line Rate'), Usage('S'), Position(6)]
    
    sv207: Annotated[D_782, Title('Line Item Denied Charge or Non-Covered Charge Amount'), Usage('S'), Position(7)]
    
    sv208: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(8)]
    
    sv209: Annotated[D_1345, Title('Status Code'), Usage('N'), Position(9)]
    
    sv210: Annotated[D_1337, Title('Level of Care Code'), Usage('N'), Position(10)]


class L2400_C002(Composite):
    """Actions Indicated"""
    pass


class L2400_PWK(Segment):
    """Line Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['AS', 'B2', 'B3', 'B4', 'CT', 'DA', 'DG', 'DS', 'EB', 'MT', 'NN', 'OB', 'OZ', 'PN', 'PO', 'PZ', 'RB', 'RR', 'RT'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'AB', 'AD', 'AF', 'AG', 'BM', 'EL', 'EM', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2400_DTP(Segment):
    """Service Line Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Assessment Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['866'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Assessment Date'), Usage('R'), Position(3)]


class L2400_AMT(Segment):
    """Service Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['GT'])]
    
    amt02: Annotated[D_782, Title('Service Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Facility Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['N8'])]
    
    amt02: Annotated[D_782, Title('Facility Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_HCP(Segment):
    """Line Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repriced Organizational Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved Ambulatory Patient Group Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Ambulatory Patient Group Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Repriced Approved Revenue Code'), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product/ Service ID Qualifier'), Usage('S'), Position(9), Enumerated(*['HC'])]
    
    hcp10: Annotated[D_234, Title('Procedure Code'), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title('Repricing Approved Service Unit Count'), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Reject Reason Code'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2410_LIN(Segment):
    """Drug Identification"""
    _segment_name = 'LIN'
    
    lin01: Annotated[D_350, Title('Assigned Identification'), Usage('N'), Position(1)]
    
    lin02: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('R'), Position(2), Enumerated(*['N4'])]
    
    lin03: Annotated[D_234, Title('Product/Service ID'), Usage('R'), Position(3)]
    
    lin04: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(4), Enumerated(*['N4'])]
    
    lin05: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(5)]
    
    lin06: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(6), Enumerated(*['N4'])]
    
    lin07: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(7)]
    
    lin08: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(8), Enumerated(*['N4'])]
    
    lin09: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(9)]
    
    lin10: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(10), Enumerated(*['N4'])]
    
    lin11: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(11)]
    
    lin12: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(12), Enumerated(*['N4'])]
    
    lin13: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(13)]
    
    lin14: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(14), Enumerated(*['N4'])]
    
    lin15: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(15)]
    
    lin16: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(16), Enumerated(*['N4'])]
    
    lin17: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(17)]
    
    lin18: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(18), Enumerated(*['N4'])]
    
    lin19: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(19)]
    
    lin20: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(20), Enumerated(*['N4'])]
    
    lin21: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(21)]
    
    lin22: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(22), Enumerated(*['N4'])]
    
    lin23: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(23)]
    
    lin24: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(24), Enumerated(*['N4'])]
    
    lin25: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(25)]
    
    lin26: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(26), Enumerated(*['N4'])]
    
    lin27: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(27)]
    
    lin28: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(28), Enumerated(*['N4'])]
    
    lin29: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(29)]
    
    lin30: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(30), Enumerated(*['N4'])]
    
    lin31: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(31)]


class L2410_C001(Composite):
    """Composite Unit of Measure"""
    
    ctp05_01: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(1), Enumerated(*['F2', 'GR', 'ML', 'UN'])]
    
    ctp05_02: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(2)]
    
    ctp05_03: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(3)]
    
    ctp05_04: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(4)]
    
    ctp05_05: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(5)]
    
    ctp05_06: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(6)]
    
    ctp05_07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(7)]
    
    ctp05_08: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(8)]
    
    ctp05_09: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(9)]
    
    ctp05_10: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(10)]
    
    ctp05_11: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(11)]
    
    ctp05_12: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(12)]
    
    ctp05_13: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(13)]
    
    ctp05_14: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(14)]
    
    ctp05_15: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(15)]


class L2410_CTP(Segment):
    """Drug Pricing"""
    _segment_name = 'CTP'
    
    ctp01: Annotated[D_687, Title('Class of Trade Code'), Usage('N'), Position(1)]
    
    ctp02: Annotated[D_236, Title('Price Identifier Code'), Usage('N'), Position(2)]
    
    ctp03: Annotated[D_212, Title('Unit Price'), Usage('R'), Position(3)]
    
    ctp04: Annotated[D_380, Title('Quantity'), Usage('R'), Position(4)]
    
    c001: Annotated[L2410_C001, Title('Composite Unit of Measure'), Usage('R'), Position(5), Required(True)]
    
    ctp06: Annotated[D_648, Title('Price Multiplier Qualifier'), Usage('N'), Position(6)]
    
    ctp07: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(7)]
    
    ctp08: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]
    
    ctp09: Annotated[D_639, Title('Basis of Unit Price Code'), Usage('N'), Position(9)]
    
    ctp10: Annotated[D_499, Title('Condition Value'), Usage('N'), Position(10)]
    
    ctp11: Annotated[D_289, Title('Multiple Price Quantity'), Usage('N'), Position(11)]


class L2410(Loop):
    
    lin: Annotated[L2410_LIN, Title('Drug Identification'), Usage('S'), Position(494), Syntax(['P0405', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425', 'P2627', 'P2829', 'P3031']), Required(True)]
    
    ctp: Annotated[L2410_CTP, Title('Drug Pricing'), Usage('S'), Position(495), Syntax(['P0405', 'C0607', 'C0902', 'C1002', 'C1103']), Required(True)]


class L2420A_NM1(Segment):
    """Attending Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['71'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Attending Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Attending Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Attending Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Attending Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Attending Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420A_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420A_PRV(Segment):
    """Attending Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['AT'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420A_C040(Composite):
    """Reference Identifier"""
    pass


class L2420A_REF(Segment):
    """Attending Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Attending Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title('Attending Physician Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420A_PRV, Title('Attending Physician Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420A_REF, Title('Attending Physician Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2420B_NM1(Segment):
    """Operating Physician Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Operating Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Operating Physician First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Operating Physician Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Operating Physician Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Operating Physician Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420B_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420B_PRV(Segment):
    """Operating Physician Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OP'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420B_C040(Composite):
    """Reference Identifier"""
    pass


class L2420B_REF(Segment):
    """Operating Physician Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Operating Physician Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title('Operating Physician Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420B_PRV, Title('Operating Physician Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420B_REF, Title('Operating Physician Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2420C_NM1(Segment):
    """Other Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['73'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Physician Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Physician First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', '34', 'XX'])]
    
    nm109: Annotated[D_67, Title('Other Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2420C_C035(Composite):
    """Provider Specialty Information"""
    pass


class L2420C_PRV(Segment):
    """Other Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['OT', 'PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420C_C040(Composite):
    """Reference Identifier"""
    pass


class L2420C_REF(Segment):
    """Other Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', 'EI', 'G2', 'LU', 'N5', 'SY', 'X5'])]
    
    ref02: Annotated[D_127, Title('Other Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title('Other Provider Name'), Usage('R'), Position(500), Required(True)]
    
    prv: Annotated[L2420C_PRV, Title('Other Provider Specialty Information'), Usage('S'), Position(505), Required(True)]
    
    ref: Annotated[L2420C_REF, Title('Other Provider Secondary Identification'), Usage('S'), Position(525), Required(True)]


class L2430_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svd03_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['HC', 'IV', 'ZZ'])]
    
    svd03_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]


class L2430_SVD(Segment):
    """Service Line Adjudication Information"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title('Payer Identifier'), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title('Service Line Paid Amount'), Usage('R'), Position(2)]
    
    c003: Annotated[L2430_C003, Title('Composite Medical Procedure Identifier'), Usage('S'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title('Service Line Revenue Code'), Usage('R'), Position(4)]
    
    svd05: Annotated[D_380, Title('Adjustment Quantity'), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title('Bundled or Unbundled Line Number'), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """Service Line Adjustment"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title('Claim Adjustment Group Code'), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('R'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas03: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(5), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas06: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(8), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas09: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(11), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas12: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas15: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title('Adjustment Reason Code'), Usage('S'), Position(17), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'W1'])]
    
    cas18: Annotated[D_782, Title('Adjustment Amount'), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title('Adjustment Quantity'), Usage('S'), Position(19)]


class L2430_DTP(Segment):
    """Service Adjudication Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Service Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title('Service Line Adjudication Information'), Usage('R'), Position(540), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title('Service Line Adjustment'), Usage('S'), Position(545), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    
    dtp: Annotated[L2430_DTP, Title('Service Adjudication Date'), Usage('S'), Position(550), Required(True)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title('Service Line Number'), Usage('R'), Position(365), Required(True)]
    
    sv2: Annotated[L2400_SV2, Title('Institutional Service Line'), Usage('R'), Position(375), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2400_PWK, Title('Line Supplemental Information'), Usage('S'), Position(420), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(5)]
    
    dtp: Annotated[L2400_DTP, Title('Service Line Date'), Usage('S'), Position(455), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Assessment Date'), Usage('S'), Position(455), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Service Tax Amount'), Usage('S'), Position(475), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Facility Tax Amount'), Usage('S'), Position(475), Required(True)]
    
    hcp: Annotated[L2400_HCP, Title('Line Pricing/Repricing Information'), Usage('S'), Position(492), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2410: TypeAlias = Annotated[L2410, Title('Drug Identification'), Usage('S'), Position(494)]
    l2410: Annotated[list[ItemL2410], MinItems(25)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title('Attending Physician Name'), Usage('S'), Position(500), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title('Operating Physician Name'), Usage('S'), Position(500), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title('Other Provider Name'), Usage('S'), Position(500), Required(True)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title('Service Line Adjudication Information'), Usage('S'), Position(540), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(25)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title('Claim Information'), Usage('R'), Position(130), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Discharge Hour'), Usage('S'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Statement Dates'), Usage('R'), Position(135), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Admission Date/Hour'), Usage('S'), Position(135), Required(True)]
    
    cl1: Annotated[L2300_CL1, Title('Institutional Claim Code'), Usage('S'), Position(140)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title('Claim Supplemental Information'), Usage('S'), Position(155), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    cn1: Annotated[L2300_CN1, Title('Contract Information'), Usage('S'), Position(160), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Payer Estimated Amount Due'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Patient Estimated Amount Due'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Patient Paid Amount'), Usage('S'), Position(175), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Credit/Debit Card Maximum Amount'), Usage('S'), Position(175), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Adjusted Repriced Claim Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Repriced Claim Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Claim Identification Number For Clearinghouses and Other Transmission Intermediaries'), Usage('S'), Position(180), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Document Identification Code'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2300_REF, Title('Original Reference Number (ICN/DCN)'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Investigational Device Exemption Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Service Authorization Exception Code'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Peer Review Organization (PRO) Approval Number'), Usage('S'), Position(180), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Prior Authorization or Referral Number'), Usage('S'), Position(180), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2300_REF, Title('Medical Record Number'), Usage('S'), Position(180), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Demonstration Project Identifier'), Usage('S'), Position(180), Required(True)]
    ItemK3: TypeAlias = Annotated[L2300_K3, Title('File Information'), Usage('S'), Position(185), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    ItemNte: TypeAlias = Annotated[L2300_NTE, Title('Claim Note'), Usage('S'), Position(190), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(10)]
    
    nte: Annotated[L2300_NTE, Title('Billing Note'), Usage('S'), Position(190), Required(True)]
    
    cr6: Annotated[L2300_CR6, Title('Home Health Care Information'), Usage('S'), Position(216), Required(True)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Home Health Functional Limitations'), Usage('S'), Position(220), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Home Health Activities Permitted'), Usage('S'), Position(220), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Home Health Mental Status'), Usage('S'), Position(220), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(2)]
    
    hi: Annotated[L2300_HI, Title('Principal, Admitting, E-Code and Patient Reason for Visit Diagnosis Information'), Usage('S'), Position(231), Required(True)]
    
    hi: Annotated[L2300_HI, Title('Diagnosis Related Group (DRG) Information'), Usage('S'), Position(231), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Other Diagnosis Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hi: Annotated[L2300_HI, Title('Principal Procedure Information'), Usage('S'), Position(231), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Other Procedure Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Occurrence Span Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Occurrence Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Value Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Condition Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Treatment Code Information'), Usage('S'), Position(231), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemQty: TypeAlias = Annotated[L2300_QTY, Title('Claim Quantity'), Usage('S'), Position(240), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(4)]
    
    hcp: Annotated[L2300_HCP, Title('Claim Pricing/Repricing Information'), Usage('S'), Position(241), Required(True)]
    ItemL2305: TypeAlias = Annotated[L2305, Title('Home Health Care Plan Information'), Usage('S'), Position(242), Required(True)]
    l2305: Annotated[list[ItemL2305], MinItems(6)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title('Attending Physician Name'), Usage('S'), Position(250), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(1)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title('Operating Physician Name'), Usage('S'), Position(250), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title('Other Provider Name'), Usage('S'), Position(250), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310E: TypeAlias = Annotated[L2310E, Title('Service Facility Name'), Usage('S'), Position(250), Required(True)]
    l2310e: Annotated[list[ItemL2310E], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title('Other Subscriber Information'), Usage('S'), Position(290), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title('Service Line Number'), Usage('R'), Position(365), Required(True)]
    l2400: Annotated[list[ItemL2400], MinItems(999)]


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
    ItemL2010Bb: TypeAlias = Annotated[L2010BB, Title('Credit/Debit Card Account Holder Name'), Usage('S'), Position(15), Required(True)]
    l2010bb: Annotated[list[ItemL2010Bb], MinItems(1)]
    ItemL2010Bc: TypeAlias = Annotated[L2010BC, Title('Payer Name'), Usage('R'), Position(15), Required(True)]
    l2010bc: Annotated[list[ItemL2010Bc], MinItems(1)]
    ItemL2010Bd: TypeAlias = Annotated[L2010BD, Title('Responsible Party Name'), Usage('S'), Position(15), Required(True)]
    l2010bd: Annotated[list[ItemL2010Bd], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title('Claim Information'), Usage('S'), Position(130), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(100)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Patient Hierarchical Level'), Usage('S'), Position(160), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Billing/Pay-To Provider Hierarchical Level'), Usage('R'), Position(1), Required(True)]
    
    prv: Annotated[L2000A_PRV, Title('Billing/Pay-To Provider Specialty Information'), Usage('S'), Position(3), Required(True)]
    
    cur: Annotated[L2000A_CUR, Title('Foreign Currency Information'), Usage('S'), Position(10), Required(True)]
    ItemL2010Aa: TypeAlias = Annotated[L2010AA, Title('Billing Provider Name'), Usage('R'), Position(15), Required(True)]
    l2010aa: Annotated[list[ItemL2010Aa], MinItems(1)]
    ItemL2010Ab: TypeAlias = Annotated[L2010AB, Title('Pay-To Provider Name'), Usage('S'), Position(15), Required(True)]
    l2010ab: Annotated[list[ItemL2010Ab], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Subscriber Hierarchichal Level'), Usage('R'), Position(20), Required(True)]
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
    """HIPAA Health Care Claim: Institutional X096A1-837"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
