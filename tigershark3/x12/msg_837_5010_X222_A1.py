"""
837.5010.X222.A1
Created 2023-05-19 10:17:36.277699
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
    
    isa12: Annotated[I11, Title('Interchange Control Version Number'), Usage('R'), Position(12), Enumerated(*['00501'])]
    
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
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['005010X222A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['837'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title('Implementation Convention Reference'), Usage('S'), Position(3)]


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title('Hierarchical Structure Code'), Usage('R'), Position(1), Enumerated(*['0019'])]
    
    bht02: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(2), Enumerated(*['00', '18'])]
    
    bht03: Annotated[D_127, Title('Originator Application Transaction Identifier'), Usage('R'), Position(3)]
    
    bht04: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title('Transaction Set Creation Time'), Usage('R'), Position(5)]
    
    bht06: Annotated[D_640, Title('Claim or Encounter Identifier'), Usage('R'), Position(6), Enumerated(*['CH', 'RP'])]


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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L1000A_PER(Segment):
    """Submitter EDI Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Submitter Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['ED', 'EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L1000A(Loop):
    
    nm1: Annotated[L1000A_NM1, Title('Submitter Name'), Usage('R'), Position(200), Syntax(['P0809', 'C1110']), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000A_PER, Title('Submitter EDI Contact Information'), Usage('R'), Position(450), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L1000B(Loop):
    
    nm1: Annotated[L1000B_NM1, Title('Receiver Name'), Usage('R'), Position(200), Syntax(['P0809', 'C1110']), Required(True)]


class HEADER(Loop):
    
    bht: Annotated[HEADER_BHT, Title('Beginning of Hierarchical Transaction'), Usage('R'), Position(100), Required(True)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title('Submitter Name'), Usage('R'), Position(200), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title('Receiver Name'), Usage('R'), Position(200), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]


class L2000A_HL(Segment):
    """Billing Provider Hierarchical Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('N'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['20'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2000A_PRV05(Composite):
    """Provider Specialty Information"""
    pass


class L2000A_PRV(Segment):
    """Billing Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4)]
    
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
    
    nm105: Annotated[D_1037, Title('Billing Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Billing Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Billing Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2010AA_N3(Segment):
    """Billing Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Billing Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Billing Provider Address Line'), Usage('S'), Position(2)]


class L2010AA_N4(Segment):
    """Billing Provider City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Billing Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Billing Provider State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Billing Provider Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2010AA_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010AA_REF(Segment):
    """Billing Provider Tax Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EI', 'SY'])]
    
    ref02: Annotated[D_127, Title('Billing Provider Tax Identification Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AA_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010AA_REF(Segment):
    """Billing Provider UPIN/License Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G'])]
    
    ref02: Annotated[D_127, Title('Billing Provider License and/or UPIN Information'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AA_PER(Segment):
    """Billing Provider Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Billing Provider Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2010AA(Loop):
    
    nm1: Annotated[L2010AA_NM1, Title('Billing Provider Name'), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010AA_N3, Title('Billing Provider Address'), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010AA_N4, Title('Billing Provider City, State, ZIP Code'), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    ref: Annotated[L2010AA_REF, Title('Billing Provider Tax Identification'), Usage('R'), Position(350), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010AA_REF, Title('Billing Provider UPIN/License Information'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    ItemPer: TypeAlias = Annotated[L2010AA_PER, Title('Billing Provider Contact Information'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]


class L2010AB_NM1(Segment):
    """Pay-to Address Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['87'])]
    
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2010AB_N3(Segment):
    """Pay-to Address - ADDRESS"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Pay-To Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Pay-To Address Line'), Usage('S'), Position(2)]


class L2010AB_N4(Segment):
    """Pay-To Address City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Pay-to Address City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Pay-to Address State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Pay-to Address Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2010AB(Loop):
    
    nm1: Annotated[L2010AB_NM1, Title('Pay-to Address Name'), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010AB_N3, Title('Pay-to Address - ADDRESS'), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010AB_N4, Title('Pay-To Address City, State, ZIP Code'), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2010AC_NM1(Segment):
    """Pay-To Plan Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Pay-To Plan Organizational Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Pay-To Plan First Name'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Pay-To Plan Middle Name'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Pay-To Plan Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Pay-To Plan Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2010AC_N3(Segment):
    """Pay-to Plan Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Pay-To Plan Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Pay-To Plan Address Line'), Usage('S'), Position(2)]


class L2010AC_N4(Segment):
    """Pay-To Plan City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Pay-To Plan City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Pay-To Plan State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Pay-To Plan Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2010AC_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010AC_REF(Segment):
    """Pay-to Plan Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title('Pay-to Plan Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AC_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010AC_REF(Segment):
    """Pay-To Plan Tax Identification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EI'])]
    
    ref02: Annotated[D_127, Title('Pay-To Plan Tax Identification Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010AC(Loop):
    
    nm1: Annotated[L2010AC_NM1, Title('Pay-To Plan Name'), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010AC_N3, Title('Pay-to Plan Address'), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010AC_N4, Title('Pay-To Plan City, State, ZIP Code'), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    ref: Annotated[L2010AC_REF, Title('Pay-to Plan Secondary Identification'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2010AC_REF, Title('Pay-To Plan Tax Identification Number'), Usage('R'), Position(350), Syntax(['R0203']), Required(True)]


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
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'P', 'S', 'T', 'U'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('S'), Position(2), Enumerated(*['18'])]
    
    sbr03: Annotated[D_127, Title('Subscriber Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Subscriber Group Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('S'), Position(5), Enumerated(*['12', '13', '14', '15', '16', '41', '42', '43', '47'])]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['11', '12', '13', '14', '15', '16', '17', 'AM', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2000B_PAT(Segment):
    """Patient Information"""
    _segment_name = 'PAT'
    
    pat01: Annotated[D_1069, Title('Individual Relationship Code'), Usage('N'), Position(1)]
    
    pat02: Annotated[D_1384, Title('Patient Location Code'), Usage('N'), Position(2)]
    
    pat03: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(3)]
    
    pat04: Annotated[D_1220, Title('Student Status Code'), Usage('N'), Position(4)]
    
    pat05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(5), Enumerated(*['D8'])]
    
    pat06: Annotated[D_1251, Title('Patient Death Date'), Usage('S'), Position(6)]
    
    pat07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(7), Enumerated(*['01'])]
    
    pat08: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(8)]
    
    pat09: Annotated[D_1073, Title('Pregnancy Indicator'), Usage('S'), Position(9), Enumerated(*['Y'])]


class L2010BA_NM1(Segment):
    """Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Subscriber Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Subscriber First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Subscriber Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Subscriber Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['II', 'MI'])]
    
    nm109: Annotated[D_67, Title('Subscriber Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2010BA_N3(Segment):
    """Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Subscriber Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Subscriber Address Line'), Usage('S'), Position(2)]


class L2010BA_N4(Segment):
    """Subscriber City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Subscriber City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Subscriber State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Subscriber Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2010BA_DMG05(Composite):
    """Composite Race or Ethnicity Information"""
    pass


class L2010BA_DMG(Segment):
    """Subscriber Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Subscriber Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Subscriber Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(10)]
    
    dmg11: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(11)]


class L2010BA_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010BA_REF(Segment):
    """Subscriber Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['SY'])]
    
    ref02: Annotated[D_127, Title('Subscriber Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BA_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010BA_REF(Segment):
    """Property and Casualty Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['Y4'])]
    
    ref02: Annotated[D_127, Title('Property Casualty Claim Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BA_PER(Segment):
    """Property and Casualty Subscriber Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EX'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('N'), Position(7)]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('N'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2010BA(Loop):
    
    nm1: Annotated[L2010BA_NM1, Title('Subscriber Name'), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010BA_N3, Title('Subscriber Address'), Usage('S'), Position(250), Required(True)]
    
    n4: Annotated[L2010BA_N4, Title('Subscriber City, State, ZIP Code'), Usage('S'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dmg: Annotated[L2010BA_DMG, Title('Subscriber Demographic Information'), Usage('S'), Position(320), Syntax(['P0102', 'P1011', 'C1105']), Required(True)]
    
    ref: Annotated[L2010BA_REF, Title('Subscriber Secondary Identification'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2010BA_REF, Title('Property and Casualty Claim Number'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    per: Annotated[L2010BA_PER, Title('Property and Casualty Subscriber Contact Information'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2010BB_N3(Segment):
    """Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Payer Address Line'), Usage('S'), Position(2)]


class L2010BB_N4(Segment):
    """Payer City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Payer State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Payer Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2010BB_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010BB_REF(Segment):
    """Payer Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'EI', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title('Payer Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BB_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010BB_REF(Segment):
    """Billing Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Billing Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010BB(Loop):
    
    nm1: Annotated[L2010BB_NM1, Title('Payer Name'), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010BB_N3, Title('Payer Address'), Usage('S'), Position(250), Required(True)]
    
    n4: Annotated[L2010BB_N4, Title('Payer City, State, ZIP Code'), Usage('S'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010BB_REF, Title('Payer Secondary Identification'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]
    ItemRef: TypeAlias = Annotated[L2010BB_REF, Title('Billing Provider Secondary Identification'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2300_CLM05(Composite):
    """Health Care Service Location Information"""
    
    clm05_01: Annotated[D_1331, Title('Place of Service Code'), Usage('R'), Position(1), Enumerated(*pos)]
    
    clm05_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('R'), Position(2), Enumerated(*['B'])]
    
    clm05_03: Annotated[D_1325, Title('Claim Frequency Code'), Usage('R'), Position(3)]


class L2300_CLM11(Composite):
    """Related Causes Information"""
    
    clm11_01: Annotated[D_1362, Title('Related Causes Code'), Usage('R'), Position(1), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_02: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(2), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_03: Annotated[D_1362, Title('Related-Causes Code'), Usage('N'), Position(3)]
    
    clm11_04: Annotated[D_156, Title('Auto Accident State or Province Code'), Usage('S'), Position(4), Enumerated(*states)]
    
    clm11_05: Annotated[D_26, Title('Country Code'), Usage('S'), Position(5), Enumerated(*country)]


class L2300_CLM(Segment):
    """Claim Information"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title('Patient Control Number'), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title('Non-Institutional Claim Type Code'), Usage('N'), Position(4)]
    
    clm05: Annotated[L2300_CLM05, Title('Health Care Service Location Information'), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title('Provider or Supplier Signature Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]
    
    clm07: Annotated[D_1359, Title('Assignment or Plan Participation Code'), Usage('R'), Position(7), Enumerated(*['A', 'B', 'C'])]
    
    clm08: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(8), Enumerated(*['N', 'W', 'Y'])]
    
    clm09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['I', 'Y'])]
    
    clm10: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('S'), Position(10), Enumerated(*['P'])]
    
    clm11: Annotated[L2300_CLM11, Title('Related Causes Information'), Usage('S'), Position(11), Required(True)]
    
    clm12: Annotated[D_1366, Title('Special Program Indicator'), Usage('S'), Position(12), Enumerated(*['02', '03', '05', '09'])]
    
    clm13: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title('Level of Service Code'), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title('Claim Status Code'), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(18)]
    
    clm19: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(19)]
    
    clm20: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(20), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '15'])]


class L2300_DTP(Segment):
    """Date - Onset of Current Illness or Symptom"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['431'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Onset of Current Illness or Injury Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Initial Treatment Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['454'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Initial Treatment Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last Seen Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['304'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Seen Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Acute Manifestation"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['453'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Acute Manifestation Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Accident"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['439'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Accident Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last Menstrual Period"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['484'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Menstrual Period Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last X-ray Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['455'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last X-Ray Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Hearing and Vision Prescription Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['471'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Prescription Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Disability Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['314', '360', '361'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Disability From Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last Worked"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['297'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Worked Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Authorized Return to Work"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['296'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Work Return Date'), Usage('R'), Position(3)]


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
    
    dtp03: Annotated[D_1251, Title('Related Hospitalization Discharge Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Assumed and Relinquished Care Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['090', '091'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Assumed or Relinquished Care Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Property and Casualty Date of First Contact"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['444'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Date Time Period'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Repricer Received Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['050'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Repricer Received Date'), Usage('R'), Position(3)]


class L2300_PWK08(Composite):
    """Actions Indicated"""
    pass


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
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
    """Patient Amount Paid"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Patient Amount Paid'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Service Authorization Exception Code"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['4N'])]
    
    ref02: Annotated[D_127, Title('Service Authorization Exception Code'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Mandatory Medicare (Section 4081) Crossover Indicator"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    ref02: Annotated[D_127, Title('Medicare Section 4081 Indicator'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Mammography Certification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EW'])]
    
    ref02: Annotated[D_127, Title('Mammography Certification Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Prior Authorization"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Payer Claim Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title('Payer Claim Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Clinical Laboratory Improvement Amendment (CLIA) Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['X4'])]
    
    ref02: Annotated[D_127, Title('Clinical Laboratory Improvement Amendment Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9A'])]
    
    ref02: Annotated[D_127, Title('Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Adjusted Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9C'])]
    
    ref02: Annotated[D_127, Title('Adjusted Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Investigational Device Exemption Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['LX'])]
    
    ref02: Annotated[D_127, Title('Investigational Device Exemption Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Claim Identifier For Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Value Added Network Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Medical Record Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title('Medical Record Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Demonstration Project Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['P4'])]
    
    ref02: Annotated[D_127, Title('Demonstration Project Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Care Plan Oversight"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1J'])]
    
    ref02: Annotated[D_127, Title('Care Plan Oversight Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_K303(Composite):
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
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD', 'CER', 'DCP', 'DGN', 'TPO'])]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2300_CR1(Segment):
    """Ambulance Transport Information"""
    _segment_name = 'CR1'
    
    cr101: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(1), Enumerated(*['LB'])]
    
    cr102: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(2)]
    
    cr103: Annotated[D_1316, Title('Ambulance Transport Code'), Usage('N'), Position(3)]
    
    cr104: Annotated[D_1317, Title('Ambulance Transport Reason Code'), Usage('R'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr105: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(5), Enumerated(*['DH'])]
    
    cr106: Annotated[D_380, Title('Transport Distance'), Usage('R'), Position(6)]
    
    cr107: Annotated[D_166, Title('Address Information'), Usage('N'), Position(7)]
    
    cr108: Annotated[D_166, Title('Address Information'), Usage('N'), Position(8)]
    
    cr109: Annotated[D_352, Title('Round Trip Purpose Description'), Usage('S'), Position(9)]
    
    cr110: Annotated[D_352, Title('Stretcher Purpose Description'), Usage('S'), Position(10)]


class L2300_CR2(Segment):
    """Spinal Manipulation Service Information"""
    _segment_name = 'CR2'
    
    cr201: Annotated[D_609, Title('Count'), Usage('N'), Position(1)]
    
    cr202: Annotated[D_380, Title('Quantity'), Usage('N'), Position(2)]
    
    cr203: Annotated[D_1367, Title('Subluxation Level Code'), Usage('N'), Position(3)]
    
    cr204: Annotated[D_1367, Title('Subluxation Level Code'), Usage('N'), Position(4)]
    
    cr205: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(5)]
    
    cr206: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    cr207: Annotated[D_380, Title('Quantity'), Usage('N'), Position(7)]
    
    cr208: Annotated[D_1342, Title('Patient Condition Code'), Usage('R'), Position(8), Enumerated(*['A', 'C', 'D', 'E', 'F', 'G', 'M'])]
    
    cr209: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]
    
    cr210: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(10)]
    
    cr211: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(11)]
    
    cr212: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(12)]


class L2300_CRC(Segment):
    """Ambulance Certification"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['07'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]


class L2300_CRC(Segment):
    """Patient Condition Information: Vision"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['E1', 'E2', 'E3'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]


class L2300_CRC(Segment):
    """Homebound Indicator"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['75'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['Y'])]
    
    crc03: Annotated[D_1321, Title('Homebound Indicator'), Usage('R'), Position(3), Enumerated(*['IH'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(4)]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(5)]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7)]


class L2300_CRC(Segment):
    """EPSDT Referral"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Qualifier'), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Code Applies Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Indicator'), Usage('R'), Position(3), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('S'), Position(4), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('S'), Position(5), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7)]


class L2300_HI01(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABK', 'BK'])]
    
    hi01_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi02_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi03_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi04_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi05_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi06_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi07_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi08_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi09_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi10_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi11_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi12_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """Health Care Diagnosis Code"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BP'])]
    
    hi01_02: Annotated[D_1271, Title('Anesthesia Related Surgical Procedure'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO'])]
    
    hi02_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI04(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI05(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI06(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI07(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI08(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI09(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI10(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI11(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI12(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Anesthesia Related Procedure"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]


class L2300_HI01(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi01_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi02_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi03_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi04_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi05_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi06_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi07_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi08_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi09_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi10_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi11_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi12_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """Condition Information"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_HCP(Segment):
    """Claim Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repricing Organization Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved Ambulatory Patient Group Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Ambulatory Patient Group Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(9)]
    
    hcp10: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(11)]
    
    hcp12: Annotated[D_380, Title('Quantity'), Usage('N'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Reject Reason Code'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2310A_NM1(Segment):
    """Referring Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Referring Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Referring Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Referring Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Referring Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Referring Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310A_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310A_REF(Segment):
    """Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Referring Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title('Referring Provider Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title('Referring Provider Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2310B_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310B_PRV05(Composite):
    """Provider Specialty Information"""
    pass


class L2310B_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4), Enumerated(*states)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310B_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title('Rendering Provider Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    prv: Annotated[L2310B_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(2550), Syntax(['P0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310C_NM1(Segment):
    """Service Facility Location Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310C_N3(Segment):
    """Service Facility Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('S'), Position(2)]


class L2310C_N4(Segment):
    """Service Facility Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Laboratory or Facility City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Laboratory or Facility State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Laboratory or Facility Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2310C_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Laboratory or Facility Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310C_PER(Segment):
    """Service Facility Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EX'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('N'), Position(7)]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('N'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title('Service Facility Location Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310C_N3, Title('Service Facility Location Address'), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310C_N4, Title('Service Facility Location City, State, ZIP Code'), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title('Service Facility Location Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]
    
    per: Annotated[L2310C_PER, Title('Service Facility Contact Information'), Usage('S'), Position(2750), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2310D_NM1(Segment):
    """Supervising Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DQ'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Supervising Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Supervising Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Supervising Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Supervising Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Supervising Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310D_REF(Segment):
    """Supervising Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Supervising Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310D(Loop):
    
    nm1: Annotated[L2310D_NM1, Title('Supervising Provider Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310D_REF, Title('Supervising Provider Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310E_NM1(Segment):
    """Ambulance Pick-up Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PW'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310E_N3(Segment):
    """Ambulance Pick-up Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('S'), Position(2)]


class L2310E_N4(Segment):
    """Ambulance Pick-up Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Pick-up City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Pick-up State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Pick-up Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2310E(Loop):
    
    nm1: Annotated[L2310E_NM1, Title('Ambulance Pick-up Location'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310E_N3, Title('Ambulance Pick-up Location Address'), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310E_N4, Title('Ambulance Pick-up Location City, State, ZIP Code'), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2310F_NM1(Segment):
    """Ambulance Drop-off Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['45'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Ambulance Drop-off Location'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310F_N3(Segment):
    """Ambulance Drop-off Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('S'), Position(2)]


class L2310F_N4(Segment):
    """Ambulance Drop-off Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Drop-off City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Drop-off State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Drop-off Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2310F(Loop):
    
    nm1: Annotated[L2310F_NM1, Title('Ambulance Drop-off Location'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310F_N3, Title('Ambulance Drop-off Location Address'), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310F_N4, Title('Ambulance Drop-off Location City, State, ZIP Code'), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'P', 'S', 'T', 'U'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '18', '19', '20', '21', '39', '40', '53', 'G8'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Other Insured Group Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('S'), Position(5), Enumerated(*['12', '13', '14', '15', '16', '41', '42', '43', '47'])]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['11', '12', '13', '14', '15', '16', '17', 'AM', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """Claim Level Adjustments"""
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
    """Coordination of Benefits (COB) Total Non-Covered Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['A8'])]
    
    amt02: Annotated[D_782, Title('Non-Covered Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Remaining Patient Liability"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title('Remaining Patient Liability'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_OI(Segment):
    """Other Insurance Coverage Information"""
    _segment_name = 'OI'
    
    oi01: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(1)]
    
    oi02: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(2)]
    
    oi03: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(3), Enumerated(*['N', 'W', 'Y'])]
    
    oi04: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('S'), Position(4), Enumerated(*['P'])]
    
    oi05: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(5)]
    
    oi06: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(6), Enumerated(*['I', 'Y'])]


class L2320_MOA(Segment):
    """Outpatient Adjudication Information"""
    _segment_name = 'MOA'
    
    moa01: Annotated[D_954, Title('Reimbursement Rate'), Usage('S'), Position(1)]
    
    moa02: Annotated[D_782, Title('HCPCS Payable Amount'), Usage('S'), Position(2)]
    
    moa03: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(3), Enumerated(*remark_code)]
    
    moa04: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(4), Enumerated(*remark_code)]
    
    moa05: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(5), Enumerated(*remark_code)]
    
    moa06: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(6), Enumerated(*remark_code)]
    
    moa07: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(7), Enumerated(*remark_code)]
    
    moa08: Annotated[D_782, Title('End Stage Renal Disease Payment Amount'), Usage('S'), Position(8)]
    
    moa09: Annotated[D_782, Title('Non-Payable Professional Component Billed Amount'), Usage('S'), Position(9)]


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Insured Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Insured First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Insured Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Insured Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['II', 'MI'])]
    
    nm109: Annotated[D_67, Title('Other Insured Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Subscriber Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Insured Address Line'), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """Other Subscriber City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Subscriber City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Subscriber State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Subscriber Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2330A_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330A_REF(Segment):
    """Other Subscriber Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['SY'])]
    
    ref02: Annotated[D_127, Title('Other Insured Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title('Other Subscriber Name'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330A_N3, Title('Other Subscriber Address'), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330A_N4, Title('Other Subscriber City, State, ZIP Code'), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    ref: Annotated[L2330A_REF, Title('Other Subscriber Secondary Identification'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]


class L2330B_NM1(Segment):
    """Other Payer Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330B_N3(Segment):
    """Other Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Payer Address Line'), Usage('S'), Position(2)]


class L2330B_N4(Segment):
    """Other Payer City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Payer State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Payer Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2330B_DTP(Segment):
    """Claim Check or Remittance Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Secondary Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'EI', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title('Other Payer Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Prior Authorization Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Claim Adjustment Indicator"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['T4'])]
    
    ref02: Annotated[D_127, Title('Other Payer Claim Adjustment Indicator'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Claim Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title("Other Payer's Claim Control Number"), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title('Other Payer Name'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330B_N3, Title('Other Payer Address'), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330B_N4, Title('Other Payer City, State, ZIP Code'), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dtp: Annotated[L2330B_DTP, Title('Claim Check or Remittance Date'), Usage('S'), Position(3450), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Secondary Identifier'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Prior Authorization Number'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Referral Number'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Claim Adjustment Indicator'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Claim Control Number'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]


class L2330C_NM1(Segment):
    """Other Payer Referring Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330C_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330C_REF(Segment):
    """Other Payer Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Other Payer Referring Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title('Other Payer Referring Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title('Other Payer Referring Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330D_NM1(Segment):
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330D_REF(Segment):
    """Other Payer Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title('Other Payer Rendering Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title('Other Payer Rendering Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330E_NM1(Segment):
    """Other Payer Service Facility Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330E_REF(Segment):
    """Other Payer Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Service Facility Location Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title('Other Payer Service Facility Location'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title('Other Payer Service Facility Location Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330F_NM1(Segment):
    """Other Payer Supervising Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DQ'])]
    
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330F_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330F_REF(Segment):
    """Other Payer Supervising Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Supervising Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330F(Loop):
    
    nm1: Annotated[L2330F_NM1, Title('Other Payer Supervising Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330F_REF, Title('Other Payer Supervising Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330G_NM1(Segment):
    """Other Payer Billing Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['85'])]
    
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330G_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330G_REF(Segment):
    """Other Payer Billing Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Billing Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330G(Loop):
    
    nm1: Annotated[L2330G_NM1, Title('Other Payer Billing Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330G_REF, Title('Other Payer Billing Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title('Other Subscriber Information'), Usage('R'), Position(2900), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title('Claim Level Adjustments'), Usage('S'), Position(2950), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Payer Paid Amount'), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Non-Covered Amount'), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Remaining Patient Liability'), Usage('S'), Position(3000), Required(True)]
    
    oi: Annotated[L2320_OI, Title('Other Insurance Coverage Information'), Usage('R'), Position(3100), Required(True)]
    
    moa: Annotated[L2320_MOA, Title('Outpatient Adjudication Information'), Usage('S'), Position(3200)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title('Other Subscriber Name'), Usage('R'), Position(3250), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title('Other Payer Name'), Usage('R'), Position(3250), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title('Other Payer Referring Provider'), Usage('S'), Position(3250), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(2)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title('Other Payer Rendering Provider'), Usage('S'), Position(3650), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title('Other Payer Service Facility Location'), Usage('S'), Position(4650), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]
    ItemL2330F: TypeAlias = Annotated[L2330F, Title('Other Payer Supervising Provider'), Usage('S'), Position(5650), Required(True)]
    l2330f: Annotated[list[ItemL2330F], MinItems(1)]
    ItemL2330G: TypeAlias = Annotated[L2330G, Title('Other Payer Billing Provider'), Usage('S'), Position(6350), Required(True)]
    l2330g: Annotated[list[ItemL2330G], MinItems(1)]


class L2400_LX(Segment):
    """Service Line Number"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]


class L2400_SV101(Composite):
    """Composite Medical Procedure Identifier"""
    
    sv101_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'IV', 'WK'])]
    
    sv101_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv101_03: Annotated[D_1339, Title('Procedure Modifier 1'), Usage('S'), Position(3)]
    
    sv101_04: Annotated[D_1339, Title('Procedure Modifier 2'), Usage('S'), Position(4)]
    
    sv101_05: Annotated[D_1339, Title('Procedure Modifier 3'), Usage('S'), Position(5)]
    
    sv101_06: Annotated[D_1339, Title('Procedure Modifier 4'), Usage('S'), Position(6)]
    
    sv101_07: Annotated[D_352, Title('Description'), Usage('S'), Position(7)]
    
    sv101_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2400_SV107(Composite):
    """Composite Diagnosis Code Pointer"""
    
    sv107_01: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]
    
    sv107_02: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('S'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]
    
    sv107_03: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('S'), Position(3), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]
    
    sv107_04: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('S'), Position(4), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]


class L2400_SV1(Segment):
    """Professional Service"""
    _segment_name = 'SV1'
    
    sv101: Annotated[L2400_SV101, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    sv102: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    sv103: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(3), Enumerated(*['MJ', 'UN'])]
    
    sv104: Annotated[D_380, Title('Service Unit Count'), Usage('R'), Position(4)]
    
    sv105: Annotated[D_1331, Title('Place of Service Code'), Usage('S'), Position(5), Enumerated(*pos)]
    
    sv106: Annotated[D_1365, Title('Service Type Code'), Usage('N'), Position(6)]
    
    sv107: Annotated[L2400_SV107, Title('Composite Diagnosis Code Pointer'), Usage('R'), Position(7), Required(True)]
    
    sv108: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]
    
    sv109: Annotated[D_1073, Title('Emergency Indicator'), Usage('S'), Position(9), Enumerated(*['Y'])]
    
    sv110: Annotated[D_1340, Title('Multiple Procedure Code'), Usage('N'), Position(10)]
    
    sv111: Annotated[D_1073, Title('EPSDT Indicator'), Usage('S'), Position(11), Enumerated(*['Y'])]
    
    sv112: Annotated[D_1073, Title('Family Planning Indicator'), Usage('S'), Position(12), Enumerated(*['Y'])]
    
    sv113: Annotated[D_1364, Title('Review Code'), Usage('N'), Position(13)]
    
    sv114: Annotated[D_1341, Title('National or Local Assigned Review Value'), Usage('N'), Position(14)]
    
    sv115: Annotated[D_1327, Title('Co-Pay Status Code'), Usage('S'), Position(15), Enumerated(*['0'])]
    
    sv116: Annotated[D_1334, Title('Health Care Professional Shortage Area Code'), Usage('N'), Position(16)]
    
    sv117: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(17)]
    
    sv118: Annotated[D_116, Title('Postal Code'), Usage('N'), Position(18)]
    
    sv119: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(19)]
    
    sv120: Annotated[D_1337, Title('Level of Care Code'), Usage('N'), Position(20)]
    
    sv121: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(21)]


class L2400_SV501(Composite):
    """Composite Medical Procedure Identifier"""
    
    sv501_01: Annotated[D_235, Title('Procedure Identifier'), Usage('R'), Position(1), Enumerated(*['HC'])]
    
    sv501_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv501_03: Annotated[D_1339, Title('Procedure Modifier 1'), Usage('N'), Position(3)]
    
    sv501_04: Annotated[D_1339, Title('Procedure Modifier 2'), Usage('N'), Position(4)]
    
    sv501_05: Annotated[D_1339, Title('Procedure Modifier 3'), Usage('N'), Position(5)]
    
    sv501_06: Annotated[D_1339, Title('Procedure Modifier 4'), Usage('N'), Position(6)]
    
    sv501_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    sv501_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2400_SV5(Segment):
    """Durable Medical Equipment Service"""
    _segment_name = 'SV5'
    
    sv501: Annotated[L2400_SV501, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    sv502: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(2), Enumerated(*['DA'])]
    
    sv503: Annotated[D_380, Title('Length of Medical Necessity'), Usage('R'), Position(3)]
    
    sv504: Annotated[D_782, Title('DME Rental Price'), Usage('R'), Position(4)]
    
    sv505: Annotated[D_782, Title('DME Purchase Price'), Usage('R'), Position(5)]
    
    sv506: Annotated[D_594, Title('Rental Unit Price Indicator'), Usage('R'), Position(6), Enumerated(*['1', '4', '6'])]
    
    sv507: Annotated[D_923, Title('Prognosis Code'), Usage('N'), Position(7)]


class L2400_PWK08(Composite):
    """Actions Indicated"""
    pass


class L2400_PWK(Segment):
    """Line Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2400_PWK08(Composite):
    """Actions Indicated"""
    pass


class L2400_PWK(Segment):
    """Durable Medical Equipment Certificate of Medical Necessity Indicator"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['CT'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AB', 'AD', 'AF', 'AG', 'NS'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(5)]
    
    pwk06: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2400_CR1(Segment):
    """Ambulance Transport Information"""
    _segment_name = 'CR1'
    
    cr101: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(1), Enumerated(*['LB'])]
    
    cr102: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(2)]
    
    cr103: Annotated[D_1316, Title('Ambulance Transport Code'), Usage('N'), Position(3)]
    
    cr104: Annotated[D_1317, Title('Ambulance Transport Reason Code'), Usage('R'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr105: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(5), Enumerated(*['DH'])]
    
    cr106: Annotated[D_380, Title('Transport Distance'), Usage('R'), Position(6)]
    
    cr107: Annotated[D_166, Title('Address Information'), Usage('N'), Position(7)]
    
    cr108: Annotated[D_166, Title('Address Information'), Usage('N'), Position(8)]
    
    cr109: Annotated[D_352, Title('Round Trip Purpose Description'), Usage('S'), Position(9)]
    
    cr110: Annotated[D_352, Title('Stretcher Purpose Description'), Usage('S'), Position(10)]


class L2400_CR3(Segment):
    """Durable Medical Equipment Certification"""
    _segment_name = 'CR3'
    
    cr301: Annotated[D_1322, Title('Certification Type Code'), Usage('R'), Position(1), Enumerated(*['I', 'R', 'S'])]
    
    cr302: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(2), Enumerated(*['MO'])]
    
    cr303: Annotated[D_380, Title('Durable Medical Equipment Duration'), Usage('R'), Position(3)]
    
    cr304: Annotated[D_1335, Title('Insulin Dependent Code'), Usage('N'), Position(4)]
    
    cr305: Annotated[D_352, Title('Description'), Usage('N'), Position(5)]


class L2400_CRC(Segment):
    """Ambulance Certification"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['07'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]


class L2400_CRC(Segment):
    """Hospice Employee Indicator"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['70'])]
    
    crc02: Annotated[D_1073, Title('Hospice Employed Provider Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Indicator'), Usage('R'), Position(3), Enumerated(*['65'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(4)]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(5)]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7)]


class L2400_CRC(Segment):
    """Condition Indicator/Durable Medical Equipment"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['09'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Indicator'), Usage('R'), Position(3), Enumerated(*['38', 'ZV'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('S'), Position(4), Enumerated(*['38', 'ZV'])]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(5), Enumerated(*['38', 'ZV'])]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6), Enumerated(*['38', 'ZV'])]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7), Enumerated(*['38', 'ZV'])]


class L2400_DTP(Segment):
    """Date - Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Prescription Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['471'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Prescription Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """DATE - Certification Revision/Recertification Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['607'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Certification Revision or Recertification Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Begin Therapy Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['463'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Begin Therapy Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Last Certification Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['461'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Certification Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Last Seen Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['304'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Treatment or Therapy Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Test Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['738', '739'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Test Performed Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Shipped Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['011'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Shipped Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Last X-ray Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['455'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last X-Ray Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Initial Treatment Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['454'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Initial Treatment Date'), Usage('R'), Position(3)]


class L2400_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_QTY(Segment):
    """Ambulance Patient Count"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['PT'])]
    
    qty02: Annotated[D_380, Title('Ambulance Patient Count'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2400_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_QTY(Segment):
    """Obstetric Anesthesia Additional Units"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['FL'])]
    
    qty02: Annotated[D_380, Title('Obstetric Additional Units'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2400_MEA04(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_MEA(Segment):
    """Test Result"""
    _segment_name = 'MEA'
    
    mea01: Annotated[D_737, Title('Measurement Reference Identification Code'), Usage('R'), Position(1), Enumerated(*['OG', 'TR'])]
    
    mea02: Annotated[D_738, Title('Measurement Qualifier'), Usage('R'), Position(2), Enumerated(*['HT', 'R1', 'R2', 'R3', 'R4'])]
    
    mea03: Annotated[D_739, Title('Test Results'), Usage('R'), Position(3)]
    
    mea05: Annotated[D_740, Title('Range Minimum'), Usage('N'), Position(5)]
    
    mea06: Annotated[D_741, Title('Range Maximum'), Usage('N'), Position(6)]
    
    mea07: Annotated[D_935, Title('Measurement Significance Code'), Usage('N'), Position(7)]
    
    mea08: Annotated[D_936, Title('Measurement Attribute Code'), Usage('N'), Position(8)]
    
    mea09: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(9)]
    
    mea10: Annotated[D_1373, Title('Measurement Method or Device'), Usage('N'), Position(10)]
    
    mea11: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(11)]
    
    mea12: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(12)]


class L2400_CN1(Segment):
    """Contract Information"""
    _segment_name = 'CN1'
    
    cn101: Annotated[D_1166, Title('Contract Type Code'), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '09'])]
    
    cn102: Annotated[D_782, Title('Contract Amount'), Usage('S'), Position(2)]
    
    cn103: Annotated[D_332, Title('Contract Percentage'), Usage('S'), Position(3)]
    
    cn104: Annotated[D_127, Title('Contract Code'), Usage('S'), Position(4)]
    
    cn105: Annotated[D_338, Title('Terms Discount Percentage'), Usage('S'), Position(5)]
    
    cn106: Annotated[D_799, Title('Contract Version Identifier'), Usage('S'), Position(6)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Repriced Line Item Reference Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9B'])]
    
    ref02: Annotated[D_127, Title('Repriced Line Item Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Adjusted Repriced Line Item Reference Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9D'])]
    
    ref02: Annotated[D_127, Title('Adjusted Repriced Line Item Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2400_REF(Segment):
    """Prior Authorization"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2400_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Line Item Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['6R'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Mammography Certification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EW'])]
    
    ref02: Annotated[D_127, Title('Mammography Certification Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Clinical Laboratory Improvement Amendment (CLIA) Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['X4'])]
    
    ref02: Annotated[D_127, Title('Clinical Laboratory Improvement Amendment Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Referring Clinical Laboratory Improvement Amendment (CLIA) Facility Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F4'])]
    
    ref02: Annotated[D_127, Title('Referring CLIA Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Immunization Batch Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BT'])]
    
    ref02: Annotated[D_127, Title('Immunization Batch Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2400_REF(Segment):
    """Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2400_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2400_AMT(Segment):
    """Sales Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T'])]
    
    amt02: Annotated[D_782, Title('Sales Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Postage Claimed Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F4'])]
    
    amt02: Annotated[D_782, Title('Postage Claimed Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_K303(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_K3(Segment):
    """File Information"""
    _segment_name = 'K3'
    
    k301: Annotated[D_449, Title('Fixed Format Information'), Usage('R'), Position(1)]
    
    k302: Annotated[D_1333, Title('Record Format Code'), Usage('N'), Position(2)]


class L2400_NTE(Segment):
    """Line Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD', 'DCP'])]
    
    nte02: Annotated[D_352, Title('Line Note Text'), Usage('R'), Position(2)]


class L2400_NTE(Segment):
    """Third Party Organization Notes"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['TPO'])]
    
    nte02: Annotated[D_352, Title('Line Note Text'), Usage('R'), Position(2)]


class L2400_PS1(Segment):
    """Purchased Service Information"""
    _segment_name = 'PS1'
    
    ps101: Annotated[D_127, Title('Purchased Service Provider Identifier'), Usage('R'), Position(1)]
    
    ps102: Annotated[D_782, Title('Purchased Service Charge Amount'), Usage('R'), Position(2)]
    
    ps103: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(3), Enumerated(*states)]


class L2400_HCP(Segment):
    """Line Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repricing Organization Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved Ambulatory Patient Group Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Ambulatory Patient Group Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(9), Enumerated(*['ER', 'HC', 'IV', 'WK'])]
    
    hcp10: Annotated[D_234, Title('Repriced Approved HCPCS Code'), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(11), Enumerated(*['MJ', 'UN'])]
    
    hcp12: Annotated[D_380, Title('Repriced Approved Service Unit Count'), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Reject Reason Code'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2410_LIN(Segment):
    """Drug Identification"""
    _segment_name = 'LIN'
    
    lin01: Annotated[D_350, Title('Assigned Identification'), Usage('N'), Position(1)]
    
    lin02: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(2), Enumerated(*['EN', 'EO', 'HI', 'N4', 'ON', 'UK', 'UP'])]
    
    lin03: Annotated[D_234, Title('National Drug Code or Universal Product Number'), Usage('R'), Position(3)]
    
    lin04: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(4)]
    
    lin05: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(5)]
    
    lin06: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(6)]
    
    lin07: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(7)]
    
    lin08: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(8)]
    
    lin09: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(9)]
    
    lin10: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(10)]
    
    lin11: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(11)]
    
    lin12: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(12)]
    
    lin13: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(13)]
    
    lin14: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(14)]
    
    lin15: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(15)]
    
    lin16: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(16)]
    
    lin17: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(17)]
    
    lin18: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(18)]
    
    lin19: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(19)]
    
    lin20: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(20)]
    
    lin21: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(21)]
    
    lin22: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(22)]
    
    lin23: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(23)]
    
    lin24: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(24)]
    
    lin25: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(25)]
    
    lin26: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(26)]
    
    lin27: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(27)]
    
    lin28: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(28)]
    
    lin29: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(29)]
    
    lin30: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(30)]
    
    lin31: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(31)]


class L2410_CTP05(Composite):
    """Composite Unit of Measure"""
    
    ctp05_01: Annotated[D_355, Title('Code Qualifier'), Usage('R'), Position(1), Enumerated(*['F2', 'GR', 'ME', 'ML', 'UN'])]
    
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
    """Drug Quantity"""
    _segment_name = 'CTP'
    
    ctp01: Annotated[D_687, Title('Class of Trade Code'), Usage('N'), Position(1)]
    
    ctp02: Annotated[D_236, Title('Price Identifier Code'), Usage('N'), Position(2)]
    
    ctp03: Annotated[D_212, Title('Unit Price'), Usage('N'), Position(3)]
    
    ctp04: Annotated[D_380, Title('National Drug Unit Count'), Usage('R'), Position(4)]
    
    ctp05: Annotated[L2410_CTP05, Title('Composite Unit of Measure'), Usage('R'), Position(5), Required(True)]
    
    ctp06: Annotated[D_648, Title('Price Multiplier Qualifier'), Usage('N'), Position(6)]
    
    ctp07: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(7)]
    
    ctp08: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]
    
    ctp09: Annotated[D_639, Title('Basis of Unit Price Code'), Usage('N'), Position(9)]
    
    ctp10: Annotated[D_499, Title('Condition Value'), Usage('N'), Position(10)]
    
    ctp11: Annotated[D_289, Title('Multiple Price Quantity'), Usage('N'), Position(11)]


class L2410_REF04(Composite):
    """Reference Identifier"""
    pass


class L2410_REF(Segment):
    """Prescription or Compound Drug Association Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['VY', 'XZ'])]
    
    ref02: Annotated[D_127, Title('Prescription Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2410(Loop):
    
    lin: Annotated[L2410_LIN, Title('Drug Identification'), Usage('R'), Position(4930), Syntax(['P0405', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425', 'P2627', 'P2829', 'P3031']), Required(True)]
    
    ctp: Annotated[L2410_CTP, Title('Drug Quantity'), Usage('R'), Position(4940), Syntax(['P0405', 'C0607', 'C0902', 'C1002', 'C1103']), Required(True)]
    
    ref: Annotated[L2410_REF, Title('Prescription or Compound Drug Association Number'), Usage('S'), Position(4950), Syntax(['R0203']), Required(True)]


class L2420A_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420A_PRV05(Composite):
    """Provider Specialty Information"""
    pass


class L2420A_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4), Enumerated(*states)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420A_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420A_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420A_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title('Rendering Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    prv: Annotated[L2420A_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(5050), Syntax(['P0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420A_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420B_NM1(Segment):
    """Purchased Service Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QB'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Purchased Service Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420B_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420B_REF(Segment):
    """Purchased Service Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Purchased Service Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420B_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title('Purchased Service Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420B_REF, Title('Purchased Service Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420C_NM1(Segment):
    """Service Facility Location Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420C_N3(Segment):
    """Service Facility Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('S'), Position(2)]


class L2420C_N4(Segment):
    """Service Facility Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Laboratory or Facility City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Laboratory or Facility State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Laboratory or Facility Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420C_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Service Facility Location Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420C_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title('Service Facility Location Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420C_N3, Title('Service Facility Location Address'), Usage('R'), Position(5140), Required(True)]
    
    n4: Annotated[L2420C_N4, Title('Service Facility Location City, State, ZIP Code'), Usage('R'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420C_REF, Title('Service Facility Location Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2420D_NM1(Segment):
    """Supervising Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DQ'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Supervising Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Supervising Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Supervising Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Supervising Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Supervising Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420D_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420D_REF(Segment):
    """Supervising Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Supervising Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420D_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420D(Loop):
    
    nm1: Annotated[L2420D_NM1, Title('Supervising Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420D_REF, Title('Supervising Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420E_NM1(Segment):
    """Ordering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DK'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Ordering Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Ordering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Ordering Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Ordering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Ordering Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420E_N3(Segment):
    """Ordering Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ordering Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ordering Provider Address Line'), Usage('S'), Position(2)]


class L2420E_N4(Segment):
    """Ordering Provider City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ordering Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ordering Provider State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Ordering Provider Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420E_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420E_REF(Segment):
    """Ordering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Ordering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420E_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420E_PER(Segment):
    """Ordering Provider Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Ordering Provider Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2420E(Loop):
    
    nm1: Annotated[L2420E_NM1, Title('Ordering Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420E_N3, Title('Ordering Provider Address'), Usage('S'), Position(5140), Required(True)]
    
    n4: Annotated[L2420E_N4, Title('Ordering Provider City, State, ZIP Code'), Usage('S'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420E_REF, Title('Ordering Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]
    
    per: Annotated[L2420E_PER, Title('Ordering Provider Contact Information'), Usage('S'), Position(5300), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2420F_NM1(Segment):
    """Referring Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Referring Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Referring Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Referring Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Referring Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Referring Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420F_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420F_REF(Segment):
    """Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Referring Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420F_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420F(Loop):
    
    nm1: Annotated[L2420F_NM1, Title('Referring Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420F_REF, Title('Referring Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420G_NM1(Segment):
    """Ambulance Pick-up Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PW'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420G_N3(Segment):
    """Ambulance Pick-up Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('S'), Position(2)]


class L2420G_N4(Segment):
    """Ambulance Pick-up Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Pick-up City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Pick-up State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Pick-up Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420G(Loop):
    
    nm1: Annotated[L2420G_NM1, Title('Ambulance Pick-up Location'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420G_N3, Title('Ambulance Pick-up Location Address'), Usage('R'), Position(5140), Required(True)]
    
    n4: Annotated[L2420G_N4, Title('Ambulance Pick-up Location City, State, ZIP Code'), Usage('R'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2420H_NM1(Segment):
    """Ambulance Drop-off Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['45'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Ambulance Drop-off Location'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420H_N3(Segment):
    """Ambulance Drop-off Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('S'), Position(2)]


class L2420H_N4(Segment):
    """Ambulance Drop-off Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Drop-off City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Drop-off State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Drop-off Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420H(Loop):
    
    nm1: Annotated[L2420H_NM1, Title('Ambulance Drop-off Location'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420H_N3, Title('Ambulance Drop-off Location Address'), Usage('R'), Position(5140), Required(True)]
    
    n4: Annotated[L2420H_N4, Title('Ambulance Drop-off Location City, State, ZIP Code'), Usage('R'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2430_SVD03(Composite):
    """Composite Medical Procedure Identifier"""
    
    svd03_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'IV', 'WK'])]
    
    svd03_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]
    
    svd03_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2430_SVD(Segment):
    """Line Adjudication Information"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title('Service Line Paid Amount'), Usage('R'), Position(2)]
    
    svd03: Annotated[L2430_SVD03, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(4)]
    
    svd05: Annotated[D_380, Title('Paid Service Unit Count'), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title('Bundled or Unbundled Line Number'), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """Line Adjustment"""
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


class L2430_DTP(Segment):
    """Line Check or Remittance Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2430_AMT(Segment):
    """Remaining Patient Liability"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title('Remaining Patient Liability'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title('Line Adjudication Information'), Usage('R'), Position(5400), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title('Line Adjustment'), Usage('S'), Position(5450), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    dtp: Annotated[L2430_DTP, Title('Line Check or Remittance Date'), Usage('R'), Position(5500), Required(True)]
    
    amt: Annotated[L2430_AMT, Title('Remaining Patient Liability'), Usage('S'), Position(5505), Required(True)]


class L2440_LQ(Segment):
    """Form Identification Code"""
    _segment_name = 'LQ'
    
    lq01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AS', 'UT'])]
    
    lq02: Annotated[D_1271, Title('Form Identifier'), Usage('R'), Position(2)]


class L2440_FRM(Segment):
    """Supporting Documentation"""
    _segment_name = 'FRM'
    
    frm01: Annotated[D_350, Title('Question Number/Letter'), Usage('R'), Position(1)]
    
    frm02: Annotated[D_1073, Title('Question Response'), Usage('S'), Position(2), Enumerated(*['N', 'W', 'Y'])]
    
    frm03: Annotated[D_127, Title('Question Response'), Usage('S'), Position(3)]
    
    frm04: Annotated[D_373, Title('Question Response'), Usage('S'), Position(4)]
    
    frm05: Annotated[D_332, Title('Question Response'), Usage('S'), Position(5)]


class L2440(Loop):
    
    lq: Annotated[L2440_LQ, Title('Form Identification Code'), Usage('R'), Position(5510), Syntax(['C0102']), Required(True)]
    ItemFrm: TypeAlias = Annotated[L2440_FRM, Title('Supporting Documentation'), Usage('R'), Position(5520), Syntax(['R02030405']), Required(True)]
    frm: Annotated[list[ItemFrm], MaxItems(99)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title('Service Line Number'), Usage('R'), Position(3650), Required(True)]
    
    sv1: Annotated[L2400_SV1, Title('Professional Service'), Usage('R'), Position(3700), Syntax(['P0304']), Required(True)]
    
    sv5: Annotated[L2400_SV5, Title('Durable Medical Equipment Service'), Usage('S'), Position(4000), Syntax(['R0405', 'C0604']), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2400_PWK, Title('Line Supplemental Information'), Usage('S'), Position(4200), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    pwk: Annotated[L2400_PWK, Title('Durable Medical Equipment Certificate of Medical Necessity Indicator'), Usage('S'), Position(4200), Syntax(['P0506']), Required(True)]
    
    cr1: Annotated[L2400_CR1, Title('Ambulance Transport Information'), Usage('S'), Position(4250), Syntax(['P0102', 'P0506']), Required(True)]
    
    cr3: Annotated[L2400_CR3, Title('Durable Medical Equipment Certification'), Usage('S'), Position(4350), Syntax(['P0203']), Required(True)]
    ItemCrc: TypeAlias = Annotated[L2400_CRC, Title('Ambulance Certification'), Usage('S'), Position(4500), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    
    crc: Annotated[L2400_CRC, Title('Hospice Employee Indicator'), Usage('S'), Position(4500), Required(True)]
    
    crc: Annotated[L2400_CRC, Title('Condition Indicator/Durable Medical Equipment'), Usage('S'), Position(4500), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Service Date'), Usage('R'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Prescription Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('DATE - Certification Revision/Recertification Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Begin Therapy Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Last Certification Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Last Seen Date'), Usage('S'), Position(4550), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2400_DTP, Title('Date - Test Date'), Usage('S'), Position(4550), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Shipped Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Last X-ray Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Initial Treatment Date'), Usage('S'), Position(4550), Required(True)]
    
    qty: Annotated[L2400_QTY, Title('Ambulance Patient Count'), Usage('S'), Position(4600), Syntax(['E0204', 'R0204']), Required(True)]
    
    qty: Annotated[L2400_QTY, Title('Obstetric Anesthesia Additional Units'), Usage('S'), Position(4600), Syntax(['E0204', 'R0204']), Required(True)]
    ItemMea: TypeAlias = Annotated[L2400_MEA, Title('Test Result'), Usage('S'), Position(4620), Syntax(['R03050608', 'L050412', 'L060412', 'L07030506', 'E0803', 'P1112']), Required(True)]
    mea: Annotated[list[ItemMea], MaxItems(5)]
    
    cn1: Annotated[L2400_CN1, Title('Contract Information'), Usage('S'), Position(4650), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Repriced Line Item Reference Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Adjusted Repriced Line Item Reference Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2400_REF, Title('Prior Authorization'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2400_REF, Title('Line Item Control Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Mammography Certification Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Clinical Laboratory Improvement Amendment (CLIA) Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Referring Clinical Laboratory Improvement Amendment (CLIA) Facility Identification'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Immunization Batch Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2400_REF, Title('Referral Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    amt: Annotated[L2400_AMT, Title('Sales Tax Amount'), Usage('S'), Position(4750), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Postage Claimed Amount'), Usage('S'), Position(4750), Required(True)]
    ItemK3: TypeAlias = Annotated[L2400_K3, Title('File Information'), Usage('S'), Position(4800), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    
    nte: Annotated[L2400_NTE, Title('Line Note'), Usage('S'), Position(4850), Required(True)]
    
    nte: Annotated[L2400_NTE, Title('Third Party Organization Notes'), Usage('S'), Position(4850), Required(True)]
    
    ps1: Annotated[L2400_PS1, Title('Purchased Service Information'), Usage('S'), Position(4880), Required(True)]
    
    hcp: Annotated[L2400_HCP, Title('Line Pricing/Repricing Information'), Usage('S'), Position(4920), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2410: TypeAlias = Annotated[L2410, Title('Drug Identification'), Usage('S'), Position(4940), Required(True)]
    l2410: Annotated[list[ItemL2410], MinItems(1)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title('Rendering Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title('Purchased Service Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title('Service Facility Location Name'), Usage('S'), Position(5000), Required(True)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2420D: TypeAlias = Annotated[L2420D, Title('Supervising Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420d: Annotated[list[ItemL2420D], MinItems(1)]
    ItemL2420E: TypeAlias = Annotated[L2420E, Title('Ordering Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420e: Annotated[list[ItemL2420E], MinItems(1)]
    ItemL2420F: TypeAlias = Annotated[L2420F, Title('Referring Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420f: Annotated[list[ItemL2420F], MinItems(2)]
    ItemL2420G: TypeAlias = Annotated[L2420G, Title('Ambulance Pick-up Location'), Usage('S'), Position(5310), Required(True)]
    l2420g: Annotated[list[ItemL2420G], MinItems(1)]
    ItemL2420H: TypeAlias = Annotated[L2420H, Title('Ambulance Drop-off Location'), Usage('S'), Position(5380), Required(True)]
    l2420h: Annotated[list[ItemL2420H], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title('Line Adjudication Information'), Usage('S'), Position(5400), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(15)]
    ItemL2440: TypeAlias = Annotated[L2440, Title('Form Identification Code'), Usage('S'), Position(5510), Required(True)]
    l2440: Annotated[list[ItemL2440], MinItems(1)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title('Claim Information'), Usage('R'), Position(1300), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Onset of Current Illness or Symptom'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Initial Treatment Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last Seen Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Acute Manifestation'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Accident'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last Menstrual Period'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last X-ray Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Hearing and Vision Prescription Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Disability Dates'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last Worked'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Authorized Return to Work'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Admission'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Discharge'), Usage('S'), Position(1350), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2300_DTP, Title('Date - Assumed and Relinquished Care Dates'), Usage('S'), Position(1350), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Property and Casualty Date of First Contact'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Repricer Received Date'), Usage('S'), Position(1350), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title('Claim Supplemental Information'), Usage('S'), Position(1550), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    cn1: Annotated[L2300_CN1, Title('Contract Information'), Usage('S'), Position(1600), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Patient Amount Paid'), Usage('S'), Position(1750), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Service Authorization Exception Code'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Mandatory Medicare (Section 4081) Crossover Indicator'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Mammography Certification Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Referral Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Prior Authorization'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Payer Claim Control Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Clinical Laboratory Improvement Amendment (CLIA) Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Repriced Claim Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Adjusted Repriced Claim Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Investigational Device Exemption Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Claim Identifier For Transmission Intermediaries'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Medical Record Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Demonstration Project Identifier'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Care Plan Oversight'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ItemK3: TypeAlias = Annotated[L2300_K3, Title('File Information'), Usage('S'), Position(1850), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    
    nte: Annotated[L2300_NTE, Title('Claim Note'), Usage('S'), Position(1900), Required(True)]
    
    cr1: Annotated[L2300_CR1, Title('Ambulance Transport Information'), Usage('S'), Position(1950), Syntax(['P0102', 'P0506']), Required(True)]
    
    cr2: Annotated[L2300_CR2, Title('Spinal Manipulation Service Information'), Usage('S'), Position(2000), Syntax(['P0102', 'C0403', 'P0506']), Required(True)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Ambulance Certification'), Usage('S'), Position(2200), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Patient Condition Information: Vision'), Usage('S'), Position(2200), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    
    crc: Annotated[L2300_CRC, Title('Homebound Indicator'), Usage('S'), Position(2200), Required(True)]
    
    crc: Annotated[L2300_CRC, Title('EPSDT Referral'), Usage('S'), Position(2200), Required(True)]
    
    hi: Annotated[L2300_HI, Title('Health Care Diagnosis Code'), Usage('R'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title('Anesthesia Related Procedure'), Usage('S'), Position(2310), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Condition Information'), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hcp: Annotated[L2300_HCP, Title('Claim Pricing/Repricing Information'), Usage('S'), Position(2410), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title('Referring Provider Name'), Usage('S'), Position(2500), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(2)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title('Rendering Provider Name'), Usage('S'), Position(2500), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title('Service Facility Location Name'), Usage('S'), Position(2500), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310D: TypeAlias = Annotated[L2310D, Title('Supervising Provider Name'), Usage('S'), Position(2500), Required(True)]
    l2310d: Annotated[list[ItemL2310D], MinItems(1)]
    ItemL2310E: TypeAlias = Annotated[L2310E, Title('Ambulance Pick-up Location'), Usage('S'), Position(2500), Required(True)]
    l2310e: Annotated[list[ItemL2310E], MinItems(1)]
    ItemL2310F: TypeAlias = Annotated[L2310F, Title('Ambulance Drop-off Location'), Usage('S'), Position(2500), Required(True)]
    l2310f: Annotated[list[ItemL2310F], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title('Other Subscriber Information'), Usage('S'), Position(2900), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title('Service Line Number'), Usage('R'), Position(3650), Required(True)]
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
    
    pat01: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(1), Enumerated(*['01', '19', '20', '21', '39', '40', '53', 'G8'])]
    
    pat02: Annotated[D_1384, Title('Patient Location Code'), Usage('N'), Position(2)]
    
    pat03: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(3)]
    
    pat04: Annotated[D_1220, Title('Student Status Code'), Usage('N'), Position(4)]
    
    pat05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(5), Enumerated(*['D8'])]
    
    pat06: Annotated[D_1251, Title('Patient Death Date'), Usage('S'), Position(6)]
    
    pat07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(7), Enumerated(*['01'])]
    
    pat08: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(8)]
    
    pat09: Annotated[D_1073, Title('Pregnancy Indicator'), Usage('S'), Position(9), Enumerated(*['Y'])]


class L2010CA_NM1(Segment):
    """Patient Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Patient Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Patient First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Patient Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Patient Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2010CA_N3(Segment):
    """Patient Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Patient Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Patient Address Line'), Usage('S'), Position(2)]


class L2010CA_N4(Segment):
    """Patient City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Patient City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Patient State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Patient Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2010CA_DMG05(Composite):
    """Composite Race or Ethnicity Information"""
    pass


class L2010CA_DMG(Segment):
    """Patient Demographic Information"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Patient Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Patient Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('N'), Position(4)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(10)]
    
    dmg11: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(11)]


class L2010CA_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010CA_REF(Segment):
    """Property and Casualty Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['Y4'])]
    
    ref02: Annotated[D_127, Title('Property Casualty Claim Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010CA_REF04(Composite):
    """Reference Identifier"""
    pass


class L2010CA_REF(Segment):
    """Property and Casualty Patient Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1W', 'SY'])]
    
    ref02: Annotated[D_127, Title('Property and Casualty Patient Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2010CA_PER(Segment):
    """Property and Casualty Patient Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EX'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('N'), Position(7)]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('N'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2010CA(Loop):
    
    nm1: Annotated[L2010CA_NM1, Title('Patient Name'), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010CA_N3, Title('Patient Address'), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010CA_N4, Title('Patient City, State, ZIP Code'), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dmg: Annotated[L2010CA_DMG, Title('Patient Demographic Information'), Usage('R'), Position(320), Syntax(['P0102', 'P1011', 'C1105']), Required(True)]
    
    ref: Annotated[L2010CA_REF, Title('Property and Casualty Claim Number'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2010CA_REF, Title('Property and Casualty Patient Identifier'), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    per: Annotated[L2010CA_PER, Title('Property and Casualty Patient Contact Information'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2300_CLM05(Composite):
    """Health Care Service Location Information"""
    
    clm05_01: Annotated[D_1331, Title('Place of Service Code'), Usage('R'), Position(1), Enumerated(*pos)]
    
    clm05_02: Annotated[D_1332, Title('Facility Code Qualifier'), Usage('R'), Position(2), Enumerated(*['B'])]
    
    clm05_03: Annotated[D_1325, Title('Claim Frequency Code'), Usage('R'), Position(3)]


class L2300_CLM11(Composite):
    """Related Causes Information"""
    
    clm11_01: Annotated[D_1362, Title('Related Causes Code'), Usage('R'), Position(1), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_02: Annotated[D_1362, Title('Related Causes Code'), Usage('S'), Position(2), Enumerated(*['AA', 'EM', 'OA'])]
    
    clm11_03: Annotated[D_1362, Title('Related-Causes Code'), Usage('N'), Position(3)]
    
    clm11_04: Annotated[D_156, Title('Auto Accident State or Province Code'), Usage('S'), Position(4), Enumerated(*states)]
    
    clm11_05: Annotated[D_26, Title('Country Code'), Usage('S'), Position(5), Enumerated(*country)]


class L2300_CLM(Segment):
    """Claim Information"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title('Patient Control Number'), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title('Non-Institutional Claim Type Code'), Usage('N'), Position(4)]
    
    clm05: Annotated[L2300_CLM05, Title('Health Care Service Location Information'), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title('Provider or Supplier Signature Indicator'), Usage('R'), Position(6), Enumerated(*['N', 'Y'])]
    
    clm07: Annotated[D_1359, Title('Assignment or Plan Participation Code'), Usage('R'), Position(7), Enumerated(*['A', 'B', 'C'])]
    
    clm08: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(8), Enumerated(*['N', 'W', 'Y'])]
    
    clm09: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(9), Enumerated(*['I', 'Y'])]
    
    clm10: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('S'), Position(10), Enumerated(*['P'])]
    
    clm11: Annotated[L2300_CLM11, Title('Related Causes Information'), Usage('S'), Position(11), Required(True)]
    
    clm12: Annotated[D_1366, Title('Special Program Indicator'), Usage('S'), Position(12), Enumerated(*['02', '03', '05', '09'])]
    
    clm13: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title('Level of Service Code'), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title('Claim Status Code'), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(18)]
    
    clm19: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(19)]
    
    clm20: Annotated[D_1514, Title('Delay Reason Code'), Usage('S'), Position(20), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '15'])]


class L2300_DTP(Segment):
    """Date - Onset of Current Illness or Symptom"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['431'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Onset of Current Illness or Injury Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Initial Treatment Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['454'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Initial Treatment Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last Seen Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['304'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Seen Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Acute Manifestation"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['453'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Acute Manifestation Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Accident"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['439'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Accident Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last Menstrual Period"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['484'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Menstrual Period Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last X-ray Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['455'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last X-Ray Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Hearing and Vision Prescription Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['471'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Prescription Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Disability Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['314', '360', '361'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Disability From Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Last Worked"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['297'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Worked Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Authorized Return to Work"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['296'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Work Return Date'), Usage('R'), Position(3)]


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
    
    dtp03: Annotated[D_1251, Title('Related Hospitalization Discharge Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Assumed and Relinquished Care Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['090', '091'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Assumed or Relinquished Care Date'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Property and Casualty Date of First Contact"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['444'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Date Time Period'), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """Date - Repricer Received Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['050'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Repricer Received Date'), Usage('R'), Position(3)]


class L2300_PWK08(Composite):
    """Actions Indicated"""
    pass


class L2300_PWK(Segment):
    """Claim Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
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
    """Patient Amount Paid"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    amt02: Annotated[D_782, Title('Patient Amount Paid'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Service Authorization Exception Code"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['4N'])]
    
    ref02: Annotated[D_127, Title('Service Authorization Exception Code'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Mandatory Medicare (Section 4081) Crossover Indicator"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F5'])]
    
    ref02: Annotated[D_127, Title('Medicare Section 4081 Indicator'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Mammography Certification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EW'])]
    
    ref02: Annotated[D_127, Title('Mammography Certification Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Prior Authorization"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Payer Claim Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title('Payer Claim Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Clinical Laboratory Improvement Amendment (CLIA) Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['X4'])]
    
    ref02: Annotated[D_127, Title('Clinical Laboratory Improvement Amendment Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9A'])]
    
    ref02: Annotated[D_127, Title('Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Adjusted Repriced Claim Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9C'])]
    
    ref02: Annotated[D_127, Title('Adjusted Repriced Claim Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Investigational Device Exemption Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['LX'])]
    
    ref02: Annotated[D_127, Title('Investigational Device Exemption Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Claim Identifier For Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Value Added Network Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Medical Record Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title('Medical Record Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Demonstration Project Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['P4'])]
    
    ref02: Annotated[D_127, Title('Demonstration Project Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Care Plan Oversight"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1J'])]
    
    ref02: Annotated[D_127, Title('Care Plan Oversight Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_K303(Composite):
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
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD', 'CER', 'DCP', 'DGN', 'TPO'])]
    
    nte02: Annotated[D_352, Title('Claim Note Text'), Usage('R'), Position(2)]


class L2300_CR1(Segment):
    """Ambulance Transport Information"""
    _segment_name = 'CR1'
    
    cr101: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(1), Enumerated(*['LB'])]
    
    cr102: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(2)]
    
    cr103: Annotated[D_1316, Title('Ambulance Transport Code'), Usage('N'), Position(3)]
    
    cr104: Annotated[D_1317, Title('Ambulance Transport Reason Code'), Usage('R'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr105: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(5), Enumerated(*['DH'])]
    
    cr106: Annotated[D_380, Title('Transport Distance'), Usage('R'), Position(6)]
    
    cr107: Annotated[D_166, Title('Address Information'), Usage('N'), Position(7)]
    
    cr108: Annotated[D_166, Title('Address Information'), Usage('N'), Position(8)]
    
    cr109: Annotated[D_352, Title('Round Trip Purpose Description'), Usage('S'), Position(9)]
    
    cr110: Annotated[D_352, Title('Stretcher Purpose Description'), Usage('S'), Position(10)]


class L2300_CR2(Segment):
    """Spinal Manipulation Service Information"""
    _segment_name = 'CR2'
    
    cr201: Annotated[D_609, Title('Count'), Usage('N'), Position(1)]
    
    cr202: Annotated[D_380, Title('Quantity'), Usage('N'), Position(2)]
    
    cr203: Annotated[D_1367, Title('Subluxation Level Code'), Usage('N'), Position(3)]
    
    cr204: Annotated[D_1367, Title('Subluxation Level Code'), Usage('N'), Position(4)]
    
    cr205: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(5)]
    
    cr206: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    cr207: Annotated[D_380, Title('Quantity'), Usage('N'), Position(7)]
    
    cr208: Annotated[D_1342, Title('Patient Condition Code'), Usage('R'), Position(8), Enumerated(*['A', 'C', 'D', 'E', 'F', 'G', 'M'])]
    
    cr209: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]
    
    cr210: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(10)]
    
    cr211: Annotated[D_352, Title('Patient Condition Description'), Usage('S'), Position(11)]
    
    cr212: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(12)]


class L2300_CRC(Segment):
    """Ambulance Certification"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['07'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]


class L2300_CRC(Segment):
    """Patient Condition Information: Vision"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['E1', 'E2', 'E3'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['L1', 'L2', 'L3', 'L4', 'L5'])]


class L2300_CRC(Segment):
    """Homebound Indicator"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['75'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['Y'])]
    
    crc03: Annotated[D_1321, Title('Homebound Indicator'), Usage('R'), Position(3), Enumerated(*['IH'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(4)]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(5)]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7)]


class L2300_CRC(Segment):
    """EPSDT Referral"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Qualifier'), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Code Applies Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Indicator'), Usage('R'), Position(3), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('S'), Position(4), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('S'), Position(5), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7)]


class L2300_HI01(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABK', 'BK'])]
    
    hi01_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi02_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi03_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi04_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi05_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi06_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi07_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi08_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi09_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi10_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi11_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Diagnosis Type Code'), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi12_02: Annotated[D_1271, Title('Diagnosis Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """Health Care Diagnosis Code"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BP'])]
    
    hi01_02: Annotated[D_1271, Title('Anesthesia Related Surgical Procedure'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BO'])]
    
    hi02_02: Annotated[D_1271, Title('Industry Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI04(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI05(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI06(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI07(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI08(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI09(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI10(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI11(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI12(Composite):
    """Health Care Code Information"""
    pass


class L2300_HI(Segment):
    """Anesthesia Related Procedure"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]


class L2300_HI01(Composite):
    """Health Care Code Information"""
    
    hi01_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi01_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """Health Care Code Information"""
    
    hi02_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi02_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """Health Care Code Information"""
    
    hi03_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi03_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """Health Care Code Information"""
    
    hi04_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi04_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """Health Care Code Information"""
    
    hi05_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi05_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """Health Care Code Information"""
    
    hi06_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi06_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """Health Care Code Information"""
    
    hi07_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi07_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """Health Care Code Information"""
    
    hi08_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi08_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """Health Care Code Information"""
    
    hi09_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi09_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """Health Care Code Information"""
    
    hi10_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi10_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """Health Care Code Information"""
    
    hi11_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi11_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """Health Care Code Information"""
    
    hi12_01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi12_02: Annotated[D_1271, Title('Condition Code'), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title('Quantity'), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title('Version Identifier'), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """Condition Information"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title('Health Care Code Information'), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title('Health Care Code Information'), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title('Health Care Code Information'), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title('Health Care Code Information'), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title('Health Care Code Information'), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title('Health Care Code Information'), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title('Health Care Code Information'), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title('Health Care Code Information'), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title('Health Care Code Information'), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title('Health Care Code Information'), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title('Health Care Code Information'), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title('Health Care Code Information'), Usage('S'), Position(12), Required(True)]


class L2300_HCP(Segment):
    """Claim Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repricing Organization Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved Ambulatory Patient Group Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Ambulatory Patient Group Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(9)]
    
    hcp10: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(11)]
    
    hcp12: Annotated[D_380, Title('Quantity'), Usage('N'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Reject Reason Code'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2310A_NM1(Segment):
    """Referring Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Referring Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Referring Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Referring Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Referring Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Referring Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310A_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310A_REF(Segment):
    """Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Referring Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title('Referring Provider Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title('Referring Provider Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2310B_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310B_PRV05(Composite):
    """Provider Specialty Information"""
    pass


class L2310B_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4), Enumerated(*states)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2310B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310B_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title('Rendering Provider Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    prv: Annotated[L2310B_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(2550), Syntax(['P0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310C_NM1(Segment):
    """Service Facility Location Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310C_N3(Segment):
    """Service Facility Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('S'), Position(2)]


class L2310C_N4(Segment):
    """Service Facility Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Laboratory or Facility City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Laboratory or Facility State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Laboratory or Facility Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2310C_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Laboratory or Facility Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310C_PER(Segment):
    """Service Facility Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EX'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('N'), Position(7)]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('N'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title('Service Facility Location Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310C_N3, Title('Service Facility Location Address'), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310C_N4, Title('Service Facility Location City, State, ZIP Code'), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title('Service Facility Location Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]
    
    per: Annotated[L2310C_PER, Title('Service Facility Contact Information'), Usage('S'), Position(2750), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2310D_NM1(Segment):
    """Supervising Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DQ'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Supervising Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Supervising Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Supervising Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Supervising Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Supervising Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2310D_REF(Segment):
    """Supervising Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Supervising Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2310D(Loop):
    
    nm1: Annotated[L2310D_NM1, Title('Supervising Provider Name'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310D_REF, Title('Supervising Provider Secondary Identification'), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310E_NM1(Segment):
    """Ambulance Pick-up Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PW'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310E_N3(Segment):
    """Ambulance Pick-up Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('S'), Position(2)]


class L2310E_N4(Segment):
    """Ambulance Pick-up Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Pick-up City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Pick-up State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Pick-up Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2310E(Loop):
    
    nm1: Annotated[L2310E_NM1, Title('Ambulance Pick-up Location'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310E_N3, Title('Ambulance Pick-up Location Address'), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310E_N4, Title('Ambulance Pick-up Location City, State, ZIP Code'), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2310F_NM1(Segment):
    """Ambulance Drop-off Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['45'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Ambulance Drop-off Location'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310F_N3(Segment):
    """Ambulance Drop-off Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('S'), Position(2)]


class L2310F_N4(Segment):
    """Ambulance Drop-off Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Drop-off City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Drop-off State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Drop-off Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2310F(Loop):
    
    nm1: Annotated[L2310F_NM1, Title('Ambulance Drop-off Location'), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310F_N3, Title('Ambulance Drop-off Location Address'), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310F_N4, Title('Ambulance Drop-off Location City, State, ZIP Code'), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2320_SBR(Segment):
    """Other Subscriber Information"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'P', 'S', 'T', 'U'])]
    
    sbr02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '18', '19', '20', '21', '39', '40', '53', 'G8'])]
    
    sbr03: Annotated[D_127, Title('Insured Group or Policy Number'), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title('Other Insured Group Name'), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title('Insurance Type Code'), Usage('S'), Position(5), Enumerated(*['12', '13', '14', '15', '16', '41', '42', '43', '47'])]
    
    sbr06: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title('Employment Status Code'), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('S'), Position(9), Enumerated(*['11', '12', '13', '14', '15', '16', '17', 'AM', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """Claim Level Adjustments"""
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
    """Coordination of Benefits (COB) Total Non-Covered Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['A8'])]
    
    amt02: Annotated[D_782, Title('Non-Covered Charge Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """Remaining Patient Liability"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title('Remaining Patient Liability'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2320_OI(Segment):
    """Other Insurance Coverage Information"""
    _segment_name = 'OI'
    
    oi01: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('N'), Position(1)]
    
    oi02: Annotated[D_1383, Title('Claim Submission Reason Code'), Usage('N'), Position(2)]
    
    oi03: Annotated[D_1073, Title('Benefits Assignment Certification Indicator'), Usage('R'), Position(3), Enumerated(*['N', 'W', 'Y'])]
    
    oi04: Annotated[D_1351, Title('Patient Signature Source Code'), Usage('S'), Position(4), Enumerated(*['P'])]
    
    oi05: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(5)]
    
    oi06: Annotated[D_1363, Title('Release of Information Code'), Usage('R'), Position(6), Enumerated(*['I', 'Y'])]


class L2320_MOA(Segment):
    """Outpatient Adjudication Information"""
    _segment_name = 'MOA'
    
    moa01: Annotated[D_954, Title('Reimbursement Rate'), Usage('S'), Position(1)]
    
    moa02: Annotated[D_782, Title('HCPCS Payable Amount'), Usage('S'), Position(2)]
    
    moa03: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(3), Enumerated(*remark_code)]
    
    moa04: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(4), Enumerated(*remark_code)]
    
    moa05: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(5), Enumerated(*remark_code)]
    
    moa06: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(6), Enumerated(*remark_code)]
    
    moa07: Annotated[D_127, Title('Claim Payment Remark Code'), Usage('S'), Position(7), Enumerated(*remark_code)]
    
    moa08: Annotated[D_782, Title('End Stage Renal Disease Payment Amount'), Usage('S'), Position(8)]
    
    moa09: Annotated[D_782, Title('Non-Payable Professional Component Billed Amount'), Usage('S'), Position(9)]


class L2330A_NM1(Segment):
    """Other Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Other Insured Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Other Insured First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Other Insured Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Other Insured Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['II', 'MI'])]
    
    nm109: Annotated[D_67, Title('Other Insured Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330A_N3(Segment):
    """Other Subscriber Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Subscriber Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Insured Address Line'), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """Other Subscriber City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Subscriber City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Subscriber State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Subscriber Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2330A_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330A_REF(Segment):
    """Other Subscriber Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['SY'])]
    
    ref02: Annotated[D_127, Title('Other Insured Additional Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title('Other Subscriber Name'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330A_N3, Title('Other Subscriber Address'), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330A_N4, Title('Other Subscriber City, State, ZIP Code'), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    ref: Annotated[L2330A_REF, Title('Other Subscriber Secondary Identification'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]


class L2330B_NM1(Segment):
    """Other Payer Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Other Payer Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330B_N3(Segment):
    """Other Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Other Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Other Payer Address Line'), Usage('S'), Position(2)]


class L2330B_N4(Segment):
    """Other Payer City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Other Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Other Payer State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Other Payer Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2330B_DTP(Segment):
    """Claim Check or Remittance Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Secondary Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'EI', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title('Other Payer Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Prior Authorization Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title('Other Payer Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Claim Adjustment Indicator"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['T4'])]
    
    ref02: Annotated[D_127, Title('Other Payer Claim Adjustment Indicator'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330B_REF(Segment):
    """Other Payer Claim Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title("Other Payer's Claim Control Number"), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title('Other Payer Name'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330B_N3, Title('Other Payer Address'), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330B_N4, Title('Other Payer City, State, ZIP Code'), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dtp: Annotated[L2330B_DTP, Title('Claim Check or Remittance Date'), Usage('S'), Position(3450), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title('Other Payer Secondary Identifier'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Prior Authorization Number'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Referral Number'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Claim Adjustment Indicator'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title('Other Payer Claim Control Number'), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]


class L2330C_NM1(Segment):
    """Other Payer Referring Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330C_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330C_REF(Segment):
    """Other Payer Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Other Payer Referring Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title('Other Payer Referring Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title('Other Payer Referring Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330D_NM1(Segment):
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330D_REF(Segment):
    """Other Payer Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title('Other Payer Rendering Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title('Other Payer Rendering Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330E_NM1(Segment):
    """Other Payer Service Facility Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330E_REF(Segment):
    """Other Payer Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Service Facility Location Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title('Other Payer Service Facility Location'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title('Other Payer Service Facility Location Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330F_NM1(Segment):
    """Other Payer Supervising Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DQ'])]
    
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330F_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330F_REF(Segment):
    """Other Payer Supervising Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Supervising Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330F(Loop):
    
    nm1: Annotated[L2330F_NM1, Title('Other Payer Supervising Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330F_REF, Title('Other Payer Supervising Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330G_NM1(Segment):
    """Other Payer Billing Provider"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['85'])]
    
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
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330G_REF04(Composite):
    """Reference Identifier"""
    pass


class L2330G_REF(Segment):
    """Other Payer Billing Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Other Payer Billing Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2330G(Loop):
    
    nm1: Annotated[L2330G_NM1, Title('Other Payer Billing Provider'), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330G_REF, Title('Other Payer Billing Provider Secondary Identification'), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title('Other Subscriber Information'), Usage('R'), Position(2900), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title('Claim Level Adjustments'), Usage('S'), Position(2950), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Payer Paid Amount'), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Coordination of Benefits (COB) Total Non-Covered Amount'), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title('Remaining Patient Liability'), Usage('S'), Position(3000), Required(True)]
    
    oi: Annotated[L2320_OI, Title('Other Insurance Coverage Information'), Usage('R'), Position(3100), Required(True)]
    
    moa: Annotated[L2320_MOA, Title('Outpatient Adjudication Information'), Usage('S'), Position(3200)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title('Other Subscriber Name'), Usage('R'), Position(3250), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title('Other Payer Name'), Usage('R'), Position(3250), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title('Other Payer Referring Provider'), Usage('S'), Position(3250), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(2)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title('Other Payer Rendering Provider'), Usage('S'), Position(3650), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title('Other Payer Service Facility Location'), Usage('S'), Position(4650), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]
    ItemL2330F: TypeAlias = Annotated[L2330F, Title('Other Payer Supervising Provider'), Usage('S'), Position(5650), Required(True)]
    l2330f: Annotated[list[ItemL2330F], MinItems(1)]
    ItemL2330G: TypeAlias = Annotated[L2330G, Title('Other Payer Billing Provider'), Usage('S'), Position(6350), Required(True)]
    l2330g: Annotated[list[ItemL2330G], MinItems(1)]


class L2400_LX(Segment):
    """Service Line Number"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]


class L2400_SV101(Composite):
    """Composite Medical Procedure Identifier"""
    
    sv101_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'IV', 'WK'])]
    
    sv101_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv101_03: Annotated[D_1339, Title('Procedure Modifier 1'), Usage('S'), Position(3)]
    
    sv101_04: Annotated[D_1339, Title('Procedure Modifier 2'), Usage('S'), Position(4)]
    
    sv101_05: Annotated[D_1339, Title('Procedure Modifier 3'), Usage('S'), Position(5)]
    
    sv101_06: Annotated[D_1339, Title('Procedure Modifier 4'), Usage('S'), Position(6)]
    
    sv101_07: Annotated[D_352, Title('Description'), Usage('S'), Position(7)]
    
    sv101_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2400_SV107(Composite):
    """Composite Diagnosis Code Pointer"""
    
    sv107_01: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]
    
    sv107_02: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('S'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]
    
    sv107_03: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('S'), Position(3), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]
    
    sv107_04: Annotated[D_1328, Title('Diagnosis Code Pointer'), Usage('S'), Position(4), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])]


class L2400_SV1(Segment):
    """Professional Service"""
    _segment_name = 'SV1'
    
    sv101: Annotated[L2400_SV101, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    sv102: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    sv103: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(3), Enumerated(*['MJ', 'UN'])]
    
    sv104: Annotated[D_380, Title('Service Unit Count'), Usage('R'), Position(4)]
    
    sv105: Annotated[D_1331, Title('Place of Service Code'), Usage('S'), Position(5), Enumerated(*pos)]
    
    sv106: Annotated[D_1365, Title('Service Type Code'), Usage('N'), Position(6)]
    
    sv107: Annotated[L2400_SV107, Title('Composite Diagnosis Code Pointer'), Usage('R'), Position(7), Required(True)]
    
    sv108: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]
    
    sv109: Annotated[D_1073, Title('Emergency Indicator'), Usage('S'), Position(9), Enumerated(*['Y'])]
    
    sv110: Annotated[D_1340, Title('Multiple Procedure Code'), Usage('N'), Position(10)]
    
    sv111: Annotated[D_1073, Title('EPSDT Indicator'), Usage('S'), Position(11), Enumerated(*['Y'])]
    
    sv112: Annotated[D_1073, Title('Family Planning Indicator'), Usage('S'), Position(12), Enumerated(*['Y'])]
    
    sv113: Annotated[D_1364, Title('Review Code'), Usage('N'), Position(13)]
    
    sv114: Annotated[D_1341, Title('National or Local Assigned Review Value'), Usage('N'), Position(14)]
    
    sv115: Annotated[D_1327, Title('Co-Pay Status Code'), Usage('S'), Position(15), Enumerated(*['0'])]
    
    sv116: Annotated[D_1334, Title('Health Care Professional Shortage Area Code'), Usage('N'), Position(16)]
    
    sv117: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(17)]
    
    sv118: Annotated[D_116, Title('Postal Code'), Usage('N'), Position(18)]
    
    sv119: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(19)]
    
    sv120: Annotated[D_1337, Title('Level of Care Code'), Usage('N'), Position(20)]
    
    sv121: Annotated[D_1360, Title('Provider Agreement Code'), Usage('N'), Position(21)]


class L2400_SV501(Composite):
    """Composite Medical Procedure Identifier"""
    
    sv501_01: Annotated[D_235, Title('Procedure Identifier'), Usage('R'), Position(1), Enumerated(*['HC'])]
    
    sv501_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    sv501_03: Annotated[D_1339, Title('Procedure Modifier 1'), Usage('N'), Position(3)]
    
    sv501_04: Annotated[D_1339, Title('Procedure Modifier 2'), Usage('N'), Position(4)]
    
    sv501_05: Annotated[D_1339, Title('Procedure Modifier 3'), Usage('N'), Position(5)]
    
    sv501_06: Annotated[D_1339, Title('Procedure Modifier 4'), Usage('N'), Position(6)]
    
    sv501_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    sv501_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2400_SV5(Segment):
    """Durable Medical Equipment Service"""
    _segment_name = 'SV5'
    
    sv501: Annotated[L2400_SV501, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    sv502: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(2), Enumerated(*['DA'])]
    
    sv503: Annotated[D_380, Title('Length of Medical Necessity'), Usage('R'), Position(3)]
    
    sv504: Annotated[D_782, Title('DME Rental Price'), Usage('R'), Position(4)]
    
    sv505: Annotated[D_782, Title('DME Purchase Price'), Usage('R'), Position(5)]
    
    sv506: Annotated[D_594, Title('Rental Unit Price Indicator'), Usage('R'), Position(6), Enumerated(*['1', '4', '6'])]
    
    sv507: Annotated[D_923, Title('Prognosis Code'), Usage('N'), Position(7)]


class L2400_PWK08(Composite):
    """Actions Indicated"""
    pass


class L2400_PWK(Segment):
    """Line Supplemental Information"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title('Attachment Control Number'), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2400_PWK08(Composite):
    """Actions Indicated"""
    pass


class L2400_PWK(Segment):
    """Durable Medical Equipment Certificate of Medical Necessity Indicator"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title('Attachment Report Type Code'), Usage('R'), Position(1), Enumerated(*['CT'])]
    
    pwk02: Annotated[D_756, Title('Attachment Transmission Code'), Usage('R'), Position(2), Enumerated(*['AB', 'AD', 'AF', 'AG', 'NS'])]
    
    pwk03: Annotated[D_757, Title('Report Copies Needed'), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(5)]
    
    pwk06: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(6)]
    
    pwk07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title('Request Category Code'), Usage('N'), Position(9)]


class L2400_CR1(Segment):
    """Ambulance Transport Information"""
    _segment_name = 'CR1'
    
    cr101: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(1), Enumerated(*['LB'])]
    
    cr102: Annotated[D_81, Title('Patient Weight'), Usage('S'), Position(2)]
    
    cr103: Annotated[D_1316, Title('Ambulance Transport Code'), Usage('N'), Position(3)]
    
    cr104: Annotated[D_1317, Title('Ambulance Transport Reason Code'), Usage('R'), Position(4), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    cr105: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(5), Enumerated(*['DH'])]
    
    cr106: Annotated[D_380, Title('Transport Distance'), Usage('R'), Position(6)]
    
    cr107: Annotated[D_166, Title('Address Information'), Usage('N'), Position(7)]
    
    cr108: Annotated[D_166, Title('Address Information'), Usage('N'), Position(8)]
    
    cr109: Annotated[D_352, Title('Round Trip Purpose Description'), Usage('S'), Position(9)]
    
    cr110: Annotated[D_352, Title('Stretcher Purpose Description'), Usage('S'), Position(10)]


class L2400_CR3(Segment):
    """Durable Medical Equipment Certification"""
    _segment_name = 'CR3'
    
    cr301: Annotated[D_1322, Title('Certification Type Code'), Usage('R'), Position(1), Enumerated(*['I', 'R', 'S'])]
    
    cr302: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(2), Enumerated(*['MO'])]
    
    cr303: Annotated[D_380, Title('Durable Medical Equipment Duration'), Usage('R'), Position(3)]
    
    cr304: Annotated[D_1335, Title('Insulin Dependent Code'), Usage('N'), Position(4)]
    
    cr305: Annotated[D_352, Title('Description'), Usage('N'), Position(5)]


class L2400_CRC(Segment):
    """Ambulance Certification"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['07'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Code'), Usage('R'), Position(3), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc04: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(4), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc05: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(5), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc06: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(6), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]
    
    crc07: Annotated[D_1321, Title('Condition Code'), Usage('S'), Position(7), Enumerated(*['01', '04', '05', '06', '07', '08', '09', '12'])]


class L2400_CRC(Segment):
    """Hospice Employee Indicator"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['70'])]
    
    crc02: Annotated[D_1073, Title('Hospice Employed Provider Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Indicator'), Usage('R'), Position(3), Enumerated(*['65'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(4)]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(5)]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7)]


class L2400_CRC(Segment):
    """Condition Indicator/Durable Medical Equipment"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title('Code Category'), Usage('R'), Position(1), Enumerated(*['09'])]
    
    crc02: Annotated[D_1073, Title('Certification Condition Indicator'), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title('Condition Indicator'), Usage('R'), Position(3), Enumerated(*['38', 'ZV'])]
    
    crc04: Annotated[D_1321, Title('Condition Indicator'), Usage('S'), Position(4), Enumerated(*['38', 'ZV'])]
    
    crc05: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(5), Enumerated(*['38', 'ZV'])]
    
    crc06: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(6), Enumerated(*['38', 'ZV'])]
    
    crc07: Annotated[D_1321, Title('Condition Indicator'), Usage('N'), Position(7), Enumerated(*['38', 'ZV'])]


class L2400_DTP(Segment):
    """Date - Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Prescription Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['471'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Prescription Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """DATE - Certification Revision/Recertification Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['607'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Certification Revision or Recertification Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Begin Therapy Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['463'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Begin Therapy Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Last Certification Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['461'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last Certification Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Last Seen Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['304'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Treatment or Therapy Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Test Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['738', '739'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Test Performed Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Shipped Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['011'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Shipped Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Last X-ray Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['455'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Last X-Ray Date'), Usage('R'), Position(3)]


class L2400_DTP(Segment):
    """Date - Initial Treatment Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['454'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Initial Treatment Date'), Usage('R'), Position(3)]


class L2400_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_QTY(Segment):
    """Ambulance Patient Count"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['PT'])]
    
    qty02: Annotated[D_380, Title('Ambulance Patient Count'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2400_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_QTY(Segment):
    """Obstetric Anesthesia Additional Units"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['FL'])]
    
    qty02: Annotated[D_380, Title('Obstetric Additional Units'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2400_MEA04(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_MEA(Segment):
    """Test Result"""
    _segment_name = 'MEA'
    
    mea01: Annotated[D_737, Title('Measurement Reference Identification Code'), Usage('R'), Position(1), Enumerated(*['OG', 'TR'])]
    
    mea02: Annotated[D_738, Title('Measurement Qualifier'), Usage('R'), Position(2), Enumerated(*['HT', 'R1', 'R2', 'R3', 'R4'])]
    
    mea03: Annotated[D_739, Title('Test Results'), Usage('R'), Position(3)]
    
    mea05: Annotated[D_740, Title('Range Minimum'), Usage('N'), Position(5)]
    
    mea06: Annotated[D_741, Title('Range Maximum'), Usage('N'), Position(6)]
    
    mea07: Annotated[D_935, Title('Measurement Significance Code'), Usage('N'), Position(7)]
    
    mea08: Annotated[D_936, Title('Measurement Attribute Code'), Usage('N'), Position(8)]
    
    mea09: Annotated[D_752, Title('Surface/Layer/Position Code'), Usage('N'), Position(9)]
    
    mea10: Annotated[D_1373, Title('Measurement Method or Device'), Usage('N'), Position(10)]
    
    mea11: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(11)]
    
    mea12: Annotated[D_1271, Title('Industry Code'), Usage('N'), Position(12)]


class L2400_CN1(Segment):
    """Contract Information"""
    _segment_name = 'CN1'
    
    cn101: Annotated[D_1166, Title('Contract Type Code'), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '09'])]
    
    cn102: Annotated[D_782, Title('Contract Amount'), Usage('S'), Position(2)]
    
    cn103: Annotated[D_332, Title('Contract Percentage'), Usage('S'), Position(3)]
    
    cn104: Annotated[D_127, Title('Contract Code'), Usage('S'), Position(4)]
    
    cn105: Annotated[D_338, Title('Terms Discount Percentage'), Usage('S'), Position(5)]
    
    cn106: Annotated[D_799, Title('Contract Version Identifier'), Usage('S'), Position(6)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Repriced Line Item Reference Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9B'])]
    
    ref02: Annotated[D_127, Title('Repriced Line Item Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Adjusted Repriced Line Item Reference Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9D'])]
    
    ref02: Annotated[D_127, Title('Adjusted Repriced Line Item Reference Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2400_REF(Segment):
    """Prior Authorization"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title('Prior Authorization or Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2400_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Line Item Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['6R'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Mammography Certification Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EW'])]
    
    ref02: Annotated[D_127, Title('Mammography Certification Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Clinical Laboratory Improvement Amendment (CLIA) Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['X4'])]
    
    ref02: Annotated[D_127, Title('Clinical Laboratory Improvement Amendment Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Referring Clinical Laboratory Improvement Amendment (CLIA) Facility Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F4'])]
    
    ref02: Annotated[D_127, Title('Referring CLIA Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    pass


class L2400_REF(Segment):
    """Immunization Batch Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BT'])]
    
    ref02: Annotated[D_127, Title('Immunization Batch Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2400_REF(Segment):
    """Referral Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title('Referral Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2400_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2400_AMT(Segment):
    """Sales Tax Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['T'])]
    
    amt02: Annotated[D_782, Title('Sales Tax Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """Postage Claimed Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['F4'])]
    
    amt02: Annotated[D_782, Title('Postage Claimed Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2400_K303(Composite):
    """Composite Unit of Measure"""
    pass


class L2400_K3(Segment):
    """File Information"""
    _segment_name = 'K3'
    
    k301: Annotated[D_449, Title('Fixed Format Information'), Usage('R'), Position(1)]
    
    k302: Annotated[D_1333, Title('Record Format Code'), Usage('N'), Position(2)]


class L2400_NTE(Segment):
    """Line Note"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['ADD', 'DCP'])]
    
    nte02: Annotated[D_352, Title('Line Note Text'), Usage('R'), Position(2)]


class L2400_NTE(Segment):
    """Third Party Organization Notes"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title('Note Reference Code'), Usage('R'), Position(1), Enumerated(*['TPO'])]
    
    nte02: Annotated[D_352, Title('Line Note Text'), Usage('R'), Position(2)]


class L2400_PS1(Segment):
    """Purchased Service Information"""
    _segment_name = 'PS1'
    
    ps101: Annotated[D_127, Title('Purchased Service Provider Identifier'), Usage('R'), Position(1)]
    
    ps102: Annotated[D_782, Title('Purchased Service Charge Amount'), Usage('R'), Position(2)]
    
    ps103: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(3), Enumerated(*states)]


class L2400_HCP(Segment):
    """Line Pricing/Repricing Information"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title('Pricing Methodology'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title('Repriced Allowed Amount'), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title('Repriced Saving Amount'), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title('Repricing Organization Identifier'), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title('Repricing Per Diem or Flat Rate Amount'), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title('Repriced Approved Ambulatory Patient Group Code'), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title('Repriced Approved Ambulatory Patient Group Amount'), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]
    
    hcp09: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(9), Enumerated(*['ER', 'HC', 'IV', 'WK'])]
    
    hcp10: Annotated[D_234, Title('Repriced Approved HCPCS Code'), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('S'), Position(11), Enumerated(*['MJ', 'UN'])]
    
    hcp12: Annotated[D_380, Title('Repriced Approved Service Unit Count'), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title('Reject Reason Code'), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title('Policy Compliance Code'), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title('Exception Code'), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2410_LIN(Segment):
    """Drug Identification"""
    _segment_name = 'LIN'
    
    lin01: Annotated[D_350, Title('Assigned Identification'), Usage('N'), Position(1)]
    
    lin02: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(2), Enumerated(*['EN', 'EO', 'HI', 'N4', 'ON', 'UK', 'UP'])]
    
    lin03: Annotated[D_234, Title('National Drug Code or Universal Product Number'), Usage('R'), Position(3)]
    
    lin04: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(4)]
    
    lin05: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(5)]
    
    lin06: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(6)]
    
    lin07: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(7)]
    
    lin08: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(8)]
    
    lin09: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(9)]
    
    lin10: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(10)]
    
    lin11: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(11)]
    
    lin12: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(12)]
    
    lin13: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(13)]
    
    lin14: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(14)]
    
    lin15: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(15)]
    
    lin16: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(16)]
    
    lin17: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(17)]
    
    lin18: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(18)]
    
    lin19: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(19)]
    
    lin20: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(20)]
    
    lin21: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(21)]
    
    lin22: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(22)]
    
    lin23: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(23)]
    
    lin24: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(24)]
    
    lin25: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(25)]
    
    lin26: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(26)]
    
    lin27: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(27)]
    
    lin28: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(28)]
    
    lin29: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(29)]
    
    lin30: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(30)]
    
    lin31: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(31)]


class L2410_CTP05(Composite):
    """Composite Unit of Measure"""
    
    ctp05_01: Annotated[D_355, Title('Code Qualifier'), Usage('R'), Position(1), Enumerated(*['F2', 'GR', 'ME', 'ML', 'UN'])]
    
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
    """Drug Quantity"""
    _segment_name = 'CTP'
    
    ctp01: Annotated[D_687, Title('Class of Trade Code'), Usage('N'), Position(1)]
    
    ctp02: Annotated[D_236, Title('Price Identifier Code'), Usage('N'), Position(2)]
    
    ctp03: Annotated[D_212, Title('Unit Price'), Usage('N'), Position(3)]
    
    ctp04: Annotated[D_380, Title('National Drug Unit Count'), Usage('R'), Position(4)]
    
    ctp05: Annotated[L2410_CTP05, Title('Composite Unit of Measure'), Usage('R'), Position(5), Required(True)]
    
    ctp06: Annotated[D_648, Title('Price Multiplier Qualifier'), Usage('N'), Position(6)]
    
    ctp07: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(7)]
    
    ctp08: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]
    
    ctp09: Annotated[D_639, Title('Basis of Unit Price Code'), Usage('N'), Position(9)]
    
    ctp10: Annotated[D_499, Title('Condition Value'), Usage('N'), Position(10)]
    
    ctp11: Annotated[D_289, Title('Multiple Price Quantity'), Usage('N'), Position(11)]


class L2410_REF04(Composite):
    """Reference Identifier"""
    pass


class L2410_REF(Segment):
    """Prescription or Compound Drug Association Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['VY', 'XZ'])]
    
    ref02: Annotated[D_127, Title('Prescription Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2410(Loop):
    
    lin: Annotated[L2410_LIN, Title('Drug Identification'), Usage('R'), Position(4930), Syntax(['P0405', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425', 'P2627', 'P2829', 'P3031']), Required(True)]
    
    ctp: Annotated[L2410_CTP, Title('Drug Quantity'), Usage('R'), Position(4940), Syntax(['P0405', 'C0607', 'C0902', 'C1002', 'C1103']), Required(True)]
    
    ref: Annotated[L2410_REF, Title('Prescription or Compound Drug Association Number'), Usage('S'), Position(4950), Syntax(['R0203']), Required(True)]


class L2420A_NM1(Segment):
    """Rendering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420A_PRV05(Composite):
    """Provider Specialty Information"""
    pass


class L2420A_PRV(Segment):
    """Rendering Provider Specialty Information"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title('Provider Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    prv02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title('Provider Taxonomy Code'), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(4), Enumerated(*states)]
    
    prv06: Annotated[D_1223, Title('Provider Organization Code'), Usage('N'), Position(6)]


class L2420A_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420A_REF(Segment):
    """Rendering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420A_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title('Rendering Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    prv: Annotated[L2420A_PRV, Title('Rendering Provider Specialty Information'), Usage('S'), Position(5050), Syntax(['P0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420A_REF, Title('Rendering Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420B_NM1(Segment):
    """Purchased Service Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QB'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Purchased Service Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420B_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420B_REF(Segment):
    """Purchased Service Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Purchased Service Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420B_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title('Purchased Service Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420B_REF, Title('Purchased Service Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420C_NM1(Segment):
    """Service Facility Location Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Laboratory or Facility Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Laboratory or Facility Primary Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420C_N3(Segment):
    """Service Facility Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Laboratory or Facility Address Line'), Usage('S'), Position(2)]


class L2420C_N4(Segment):
    """Service Facility Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Laboratory or Facility City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Laboratory or Facility State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Laboratory or Facility Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420C_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420C_REF(Segment):
    """Service Facility Location Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Service Facility Location Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420C_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title('Service Facility Location Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420C_N3, Title('Service Facility Location Address'), Usage('R'), Position(5140), Required(True)]
    
    n4: Annotated[L2420C_N4, Title('Service Facility Location City, State, ZIP Code'), Usage('R'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420C_REF, Title('Service Facility Location Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2420D_NM1(Segment):
    """Supervising Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DQ'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Supervising Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Supervising Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Supervising Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Supervising Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Supervising Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420D_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420D_REF(Segment):
    """Supervising Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title('Supervising Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420D_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420D(Loop):
    
    nm1: Annotated[L2420D_NM1, Title('Supervising Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420D_REF, Title('Supervising Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420E_NM1(Segment):
    """Ordering Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DK'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Ordering Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Ordering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Ordering Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Ordering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Ordering Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420E_N3(Segment):
    """Ordering Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ordering Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ordering Provider Address Line'), Usage('S'), Position(2)]


class L2420E_N4(Segment):
    """Ordering Provider City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ordering Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ordering Provider State or Province Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Ordering Provider Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420E_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420E_REF(Segment):
    """Ordering Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Ordering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420E_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420E_PER(Segment):
    """Ordering Provider Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Ordering Provider Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2420E(Loop):
    
    nm1: Annotated[L2420E_NM1, Title('Ordering Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420E_N3, Title('Ordering Provider Address'), Usage('S'), Position(5140), Required(True)]
    
    n4: Annotated[L2420E_N4, Title('Ordering Provider City, State, ZIP Code'), Usage('S'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420E_REF, Title('Ordering Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]
    
    per: Annotated[L2420E_PER, Title('Ordering Provider Contact Information'), Usage('S'), Position(5300), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2420F_NM1(Segment):
    """Referring Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DN', 'P3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Referring Provider Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Referring Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Referring Provider Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Referring Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title('Referring Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420F_REF04(Composite):
    """Reference Identifier"""
    
    ref04_01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title('Other Payer Primary Identifier'), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(6)]


class L2420F_REF(Segment):
    """Referring Provider Secondary Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title('Referring Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420F_REF04, Title('Reference Identifier'), Usage('S'), Position(4), Required(True)]


class L2420F(Loop):
    
    nm1: Annotated[L2420F_NM1, Title('Referring Provider Name'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420F_REF, Title('Referring Provider Secondary Identification'), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420G_NM1(Segment):
    """Ambulance Pick-up Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PW'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420G_N3(Segment):
    """Ambulance Pick-up Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Pick-up Address Line'), Usage('S'), Position(2)]


class L2420G_N4(Segment):
    """Ambulance Pick-up Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Pick-up City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Pick-up State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Pick-up Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420G(Loop):
    
    nm1: Annotated[L2420G_NM1, Title('Ambulance Pick-up Location'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420G_N3, Title('Ambulance Pick-up Location Address'), Usage('R'), Position(5140), Required(True)]
    
    n4: Annotated[L2420G_N4, Title('Ambulance Pick-up Location City, State, ZIP Code'), Usage('R'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2420H_NM1(Segment):
    """Ambulance Drop-off Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['45'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Ambulance Drop-off Location'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2420H_N3(Segment):
    """Ambulance Drop-off Location Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Ambulance Drop-off Address Line'), Usage('S'), Position(2)]


class L2420H_N4(Segment):
    """Ambulance Drop-off Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Ambulance Drop-off City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Ambulance Drop-off State or Province Code'), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title('Ambulance Drop-off Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2420H(Loop):
    
    nm1: Annotated[L2420H_NM1, Title('Ambulance Drop-off Location'), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2420H_N3, Title('Ambulance Drop-off Location Address'), Usage('R'), Position(5140), Required(True)]
    
    n4: Annotated[L2420H_N4, Title('Ambulance Drop-off Location City, State, ZIP Code'), Usage('R'), Position(5200), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2430_SVD03(Composite):
    """Composite Medical Procedure Identifier"""
    
    svd03_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'IV', 'WK'])]
    
    svd03_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]
    
    svd03_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2430_SVD(Segment):
    """Line Adjudication Information"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title('Other Payer Primary Identifier'), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title('Service Line Paid Amount'), Usage('R'), Position(2)]
    
    svd03: Annotated[L2430_SVD03, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(4)]
    
    svd05: Annotated[D_380, Title('Paid Service Unit Count'), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title('Bundled or Unbundled Line Number'), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """Line Adjustment"""
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


class L2430_DTP(Segment):
    """Line Check or Remittance Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Adjudication or Payment Date'), Usage('R'), Position(3)]


class L2430_AMT(Segment):
    """Remaining Patient Liability"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title('Remaining Patient Liability'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title('Line Adjudication Information'), Usage('R'), Position(5400), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title('Line Adjustment'), Usage('S'), Position(5450), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    dtp: Annotated[L2430_DTP, Title('Line Check or Remittance Date'), Usage('R'), Position(5500), Required(True)]
    
    amt: Annotated[L2430_AMT, Title('Remaining Patient Liability'), Usage('S'), Position(5505), Required(True)]


class L2440_LQ(Segment):
    """Form Identification Code"""
    _segment_name = 'LQ'
    
    lq01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['AS', 'UT'])]
    
    lq02: Annotated[D_1271, Title('Form Identifier'), Usage('R'), Position(2)]


class L2440_FRM(Segment):
    """Supporting Documentation"""
    _segment_name = 'FRM'
    
    frm01: Annotated[D_350, Title('Question Number/Letter'), Usage('R'), Position(1)]
    
    frm02: Annotated[D_1073, Title('Question Response'), Usage('S'), Position(2), Enumerated(*['N', 'W', 'Y'])]
    
    frm03: Annotated[D_127, Title('Question Response'), Usage('S'), Position(3)]
    
    frm04: Annotated[D_373, Title('Question Response'), Usage('S'), Position(4)]
    
    frm05: Annotated[D_332, Title('Question Response'), Usage('S'), Position(5)]


class L2440(Loop):
    
    lq: Annotated[L2440_LQ, Title('Form Identification Code'), Usage('R'), Position(5510), Syntax(['C0102']), Required(True)]
    ItemFrm: TypeAlias = Annotated[L2440_FRM, Title('Supporting Documentation'), Usage('R'), Position(5520), Syntax(['R02030405']), Required(True)]
    frm: Annotated[list[ItemFrm], MaxItems(99)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title('Service Line Number'), Usage('R'), Position(3650), Required(True)]
    
    sv1: Annotated[L2400_SV1, Title('Professional Service'), Usage('R'), Position(3700), Syntax(['P0304']), Required(True)]
    
    sv5: Annotated[L2400_SV5, Title('Durable Medical Equipment Service'), Usage('S'), Position(4000), Syntax(['R0405', 'C0604']), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2400_PWK, Title('Line Supplemental Information'), Usage('S'), Position(4200), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    pwk: Annotated[L2400_PWK, Title('Durable Medical Equipment Certificate of Medical Necessity Indicator'), Usage('S'), Position(4200), Syntax(['P0506']), Required(True)]
    
    cr1: Annotated[L2400_CR1, Title('Ambulance Transport Information'), Usage('S'), Position(4250), Syntax(['P0102', 'P0506']), Required(True)]
    
    cr3: Annotated[L2400_CR3, Title('Durable Medical Equipment Certification'), Usage('S'), Position(4350), Syntax(['P0203']), Required(True)]
    ItemCrc: TypeAlias = Annotated[L2400_CRC, Title('Ambulance Certification'), Usage('S'), Position(4500), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    
    crc: Annotated[L2400_CRC, Title('Hospice Employee Indicator'), Usage('S'), Position(4500), Required(True)]
    
    crc: Annotated[L2400_CRC, Title('Condition Indicator/Durable Medical Equipment'), Usage('S'), Position(4500), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Service Date'), Usage('R'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Prescription Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('DATE - Certification Revision/Recertification Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Begin Therapy Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Last Certification Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Last Seen Date'), Usage('S'), Position(4550), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2400_DTP, Title('Date - Test Date'), Usage('S'), Position(4550), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Shipped Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Last X-ray Date'), Usage('S'), Position(4550), Required(True)]
    
    dtp: Annotated[L2400_DTP, Title('Date - Initial Treatment Date'), Usage('S'), Position(4550), Required(True)]
    
    qty: Annotated[L2400_QTY, Title('Ambulance Patient Count'), Usage('S'), Position(4600), Syntax(['E0204', 'R0204']), Required(True)]
    
    qty: Annotated[L2400_QTY, Title('Obstetric Anesthesia Additional Units'), Usage('S'), Position(4600), Syntax(['E0204', 'R0204']), Required(True)]
    ItemMea: TypeAlias = Annotated[L2400_MEA, Title('Test Result'), Usage('S'), Position(4620), Syntax(['R03050608', 'L050412', 'L060412', 'L07030506', 'E0803', 'P1112']), Required(True)]
    mea: Annotated[list[ItemMea], MaxItems(5)]
    
    cn1: Annotated[L2400_CN1, Title('Contract Information'), Usage('S'), Position(4650), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Repriced Line Item Reference Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Adjusted Repriced Line Item Reference Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2400_REF, Title('Prior Authorization'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2400_REF, Title('Line Item Control Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Mammography Certification Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Clinical Laboratory Improvement Amendment (CLIA) Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Referring Clinical Laboratory Improvement Amendment (CLIA) Facility Identification'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title('Immunization Batch Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2400_REF, Title('Referral Number'), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    amt: Annotated[L2400_AMT, Title('Sales Tax Amount'), Usage('S'), Position(4750), Required(True)]
    
    amt: Annotated[L2400_AMT, Title('Postage Claimed Amount'), Usage('S'), Position(4750), Required(True)]
    ItemK3: TypeAlias = Annotated[L2400_K3, Title('File Information'), Usage('S'), Position(4800), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    
    nte: Annotated[L2400_NTE, Title('Line Note'), Usage('S'), Position(4850), Required(True)]
    
    nte: Annotated[L2400_NTE, Title('Third Party Organization Notes'), Usage('S'), Position(4850), Required(True)]
    
    ps1: Annotated[L2400_PS1, Title('Purchased Service Information'), Usage('S'), Position(4880), Required(True)]
    
    hcp: Annotated[L2400_HCP, Title('Line Pricing/Repricing Information'), Usage('S'), Position(4920), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2410: TypeAlias = Annotated[L2410, Title('Drug Identification'), Usage('S'), Position(4940), Required(True)]
    l2410: Annotated[list[ItemL2410], MinItems(1)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title('Rendering Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title('Purchased Service Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title('Service Facility Location Name'), Usage('S'), Position(5000), Required(True)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2420D: TypeAlias = Annotated[L2420D, Title('Supervising Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420d: Annotated[list[ItemL2420D], MinItems(1)]
    ItemL2420E: TypeAlias = Annotated[L2420E, Title('Ordering Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420e: Annotated[list[ItemL2420E], MinItems(1)]
    ItemL2420F: TypeAlias = Annotated[L2420F, Title('Referring Provider Name'), Usage('S'), Position(5000), Required(True)]
    l2420f: Annotated[list[ItemL2420F], MinItems(2)]
    ItemL2420G: TypeAlias = Annotated[L2420G, Title('Ambulance Pick-up Location'), Usage('S'), Position(5310), Required(True)]
    l2420g: Annotated[list[ItemL2420G], MinItems(1)]
    ItemL2420H: TypeAlias = Annotated[L2420H, Title('Ambulance Drop-off Location'), Usage('S'), Position(5380), Required(True)]
    l2420h: Annotated[list[ItemL2420H], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title('Line Adjudication Information'), Usage('S'), Position(5400), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(15)]
    ItemL2440: TypeAlias = Annotated[L2440, Title('Form Identification Code'), Usage('S'), Position(5510), Required(True)]
    l2440: Annotated[list[ItemL2440], MinItems(1)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title('Claim Information'), Usage('R'), Position(1300), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Onset of Current Illness or Symptom'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Initial Treatment Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last Seen Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Acute Manifestation'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Accident'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last Menstrual Period'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last X-ray Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Hearing and Vision Prescription Date'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Disability Dates'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Last Worked'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Authorized Return to Work'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Admission'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Discharge'), Usage('S'), Position(1350), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2300_DTP, Title('Date - Assumed and Relinquished Care Dates'), Usage('S'), Position(1350), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Property and Casualty Date of First Contact'), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title('Date - Repricer Received Date'), Usage('S'), Position(1350), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title('Claim Supplemental Information'), Usage('S'), Position(1550), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    cn1: Annotated[L2300_CN1, Title('Contract Information'), Usage('S'), Position(1600), Required(True)]
    
    amt: Annotated[L2300_AMT, Title('Patient Amount Paid'), Usage('S'), Position(1750), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Service Authorization Exception Code'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Mandatory Medicare (Section 4081) Crossover Indicator'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Mammography Certification Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Referral Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Prior Authorization'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Payer Claim Control Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Clinical Laboratory Improvement Amendment (CLIA) Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Repriced Claim Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Adjusted Repriced Claim Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Investigational Device Exemption Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Claim Identifier For Transmission Intermediaries'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Medical Record Number'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Demonstration Project Identifier'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title('Care Plan Oversight'), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ItemK3: TypeAlias = Annotated[L2300_K3, Title('File Information'), Usage('S'), Position(1850), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    
    nte: Annotated[L2300_NTE, Title('Claim Note'), Usage('S'), Position(1900), Required(True)]
    
    cr1: Annotated[L2300_CR1, Title('Ambulance Transport Information'), Usage('S'), Position(1950), Syntax(['P0102', 'P0506']), Required(True)]
    
    cr2: Annotated[L2300_CR2, Title('Spinal Manipulation Service Information'), Usage('S'), Position(2000), Syntax(['P0102', 'C0403', 'P0506']), Required(True)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Ambulance Certification'), Usage('S'), Position(2200), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    ItemCrc: TypeAlias = Annotated[L2300_CRC, Title('Patient Condition Information: Vision'), Usage('S'), Position(2200), Required(True)]
    crc: Annotated[list[ItemCrc], MaxItems(3)]
    
    crc: Annotated[L2300_CRC, Title('Homebound Indicator'), Usage('S'), Position(2200), Required(True)]
    
    crc: Annotated[L2300_CRC, Title('EPSDT Referral'), Usage('S'), Position(2200), Required(True)]
    
    hi: Annotated[L2300_HI, Title('Health Care Diagnosis Code'), Usage('R'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title('Anesthesia Related Procedure'), Usage('S'), Position(2310), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title('Condition Information'), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hcp: Annotated[L2300_HCP, Title('Claim Pricing/Repricing Information'), Usage('S'), Position(2410), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title('Referring Provider Name'), Usage('S'), Position(2500), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(2)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title('Rendering Provider Name'), Usage('S'), Position(2500), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title('Service Facility Location Name'), Usage('S'), Position(2500), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310D: TypeAlias = Annotated[L2310D, Title('Supervising Provider Name'), Usage('S'), Position(2500), Required(True)]
    l2310d: Annotated[list[ItemL2310D], MinItems(1)]
    ItemL2310E: TypeAlias = Annotated[L2310E, Title('Ambulance Pick-up Location'), Usage('S'), Position(2500), Required(True)]
    l2310e: Annotated[list[ItemL2310E], MinItems(1)]
    ItemL2310F: TypeAlias = Annotated[L2310F, Title('Ambulance Drop-off Location'), Usage('S'), Position(2500), Required(True)]
    l2310f: Annotated[list[ItemL2310F], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title('Other Subscriber Information'), Usage('S'), Position(2900), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title('Service Line Number'), Usage('R'), Position(3650), Required(True)]
    l2400: Annotated[list[ItemL2400], MinItems(50)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title('Patient Hierarchical Level'), Usage('R'), Position(10), Required(True)]
    
    pat: Annotated[L2000C_PAT, Title('Patient Information'), Usage('R'), Position(70), Syntax(['P0506', 'P0708']), Required(True)]
    ItemL2010Ca: TypeAlias = Annotated[L2010CA, Title('Patient Name'), Usage('R'), Position(150), Required(True)]
    l2010ca: Annotated[list[ItemL2010Ca], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title('Claim Information'), Usage('R'), Position(1300), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(100)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title('Subscriber Hierarchical Level'), Usage('R'), Position(10), Required(True)]
    
    sbr: Annotated[L2000B_SBR, Title('Subscriber Information'), Usage('R'), Position(50), Required(True)]
    
    pat: Annotated[L2000B_PAT, Title('Patient Information'), Usage('S'), Position(70), Syntax(['P0506', 'P0708'])]
    ItemL2010Ba: TypeAlias = Annotated[L2010BA, Title('Subscriber Name'), Usage('R'), Position(150), Required(True)]
    l2010ba: Annotated[list[ItemL2010Ba], MinItems(1)]
    ItemL2010Bb: TypeAlias = Annotated[L2010BB, Title('Payer Name'), Usage('R'), Position(150), Required(True)]
    l2010bb: Annotated[list[ItemL2010Bb], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title('Claim Information'), Usage('S'), Position(1300), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(100)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Patient Hierarchical Level'), Usage('S'), Position(1400), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Billing Provider Hierarchical Level'), Usage('R'), Position(10), Required(True)]
    
    prv: Annotated[L2000A_PRV, Title('Billing Provider Specialty Information'), Usage('S'), Position(30), Syntax(['P0203']), Required(True)]
    
    cur: Annotated[L2000A_CUR, Title('Foreign Currency Information'), Usage('S'), Position(100), Syntax(['C0807', 'C0907', 'L101112', 'C1110', 'C1210', 'L131415', 'C1413', 'C1513', 'L161718', 'C1716', 'C1816', 'L192021', 'C2019', 'C2119']), Required(True)]
    ItemL2010Aa: TypeAlias = Annotated[L2010AA, Title('Billing Provider Name'), Usage('R'), Position(150), Required(True)]
    l2010aa: Annotated[list[ItemL2010Aa], MinItems(1)]
    ItemL2010Ab: TypeAlias = Annotated[L2010AB, Title('Pay-to Address Name'), Usage('S'), Position(150), Required(True)]
    l2010ab: Annotated[list[ItemL2010Ab], MinItems(1)]
    ItemL2010Ac: TypeAlias = Annotated[L2010AC, Title('Pay-To Plan Name'), Usage('S'), Position(150), Required(True)]
    l2010ac: Annotated[list[ItemL2010Ac], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Subscriber Hierarchical Level'), Usage('R'), Position(200), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class DETAIL(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title('Billing Provider Hierarchical Level'), Usage('R'), Position(10), Required(True)]
    l2000a: Annotated[list[ItemL2000A], MinItems(1)]


class FOOTER(Loop):
    pass


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(50), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Table 1 - Header'), Usage('R'), Position(100), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('S'), Position(200), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('N'), Position(300)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(5550), Required(True)]


class GS_LOOP_GE(Segment):
    """Functional Group Trailer"""
    _segment_name = 'GE'
    
    ge01: Annotated[D_97, Title('Number of Transaction Sets Included'), Usage('R'), Position(1)]
    
    ge02: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(2)]


class GS_LOOP(Loop):
    
    gs: Annotated[GS_LOOP_GS, Title('Functional Group Header'), Usage('R'), Position(100), Required(True)]
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title('Transaction Set Header'), Usage('R'), Position(200), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
    
    ge: Annotated[GS_LOOP_GE, Title('Functional Group Trailer'), Usage('R'), Position(300), Required(True)]


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
    
    isa: Annotated[ISA_LOOP_ISA, Title('Interchange Control Header'), Usage('R'), Position(100), Required(True)]
    ItemGs_Loop: TypeAlias = Annotated[GS_LOOP, Title('Functional Group Header'), Usage('R'), Position(200), Required(True)]
    gs_loop: Annotated[list[ItemGs_Loop], MinItems(1)]
    
    ta1: Annotated[ISA_LOOP_TA1, Title('Interchange Acknowledgement'), Usage('S'), Position(200), Required(True)]
    
    iea: Annotated[ISA_LOOP_IEA, Title('Interchange Control Trailer'), Usage('R'), Position(300), Required(True)]


class MSG837(Message):
    """HIPAA Health Care Claim: Professional X222A1-837"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
