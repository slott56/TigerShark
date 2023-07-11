"""
277.5010.X212
Created 2023-05-19 10:17:35.857645
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
    
    isa11: Annotated[I65, Title('Interchange Control Standards Identifier'), Usage('R'), Position(11)]
    
    isa12: Annotated[I11, Title('Interchange Control Version Number'), Usage('R'), Position(12), Enumerated(*['00501'])]
    
    isa13: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(13)]
    
    isa14: Annotated[I13, Title('Acknowledgment Requested'), Usage('R'), Position(14), Enumerated(*['0', '1'])]
    
    isa15: Annotated[I14, Title('Usage Indicator'), Usage('R'), Position(15), Enumerated(*['P', 'T'])]
    
    isa16: Annotated[I15, Title('Component Element Separator'), Usage('R'), Position(16)]


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    _segment_name = 'GS'
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['RA'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['005010X218'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['277'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title('Version, Release, or Industry Identifier'), Usage('R'), Position(3), Enumerated(*['005010X212'])]


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title('Hierarchical Structure Code'), Usage('R'), Position(1), Enumerated(*['0010'])]
    
    bht02: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(2), Enumerated(*['08'])]
    
    bht03: Annotated[D_127, Title('Originator Application Transaction Identifier'), Usage('R'), Position(3)]
    
    bht04: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title('Transaction Set Creation Time'), Usage('R'), Position(5)]
    
    bht06: Annotated[D_640, Title('Transaction Type Code'), Usage('R'), Position(6), Enumerated(*['DG'])]


class HEADER(Loop):
    
    bht: Annotated[HEADER_BHT, Title('Beginning of Hierarchical Transaction'), Usage('R'), Position(200), Required(True)]


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
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Payer Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100A_PER(Segment):
    """Payer Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Payer Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['ED', 'EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['ED', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100A(Loop):
    
    nm1: Annotated[L2100A_NM1, Title('Payer Name'), Usage('R'), Position(500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100A_PER, Title('Payer Contact Information'), Usage('S'), Position(800), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2000B_HL(Segment):
    """Information Receiver Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['21'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0', '1'])]


class L2100B_NM1(Segment):
    """Information Receiver Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['41'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Information Receiver Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Information Receiver First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Information Receiver Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Information Receiver Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Information Receiver Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['46'])]
    
    nm109: Annotated[D_67, Title('Information Receiver Identification Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100B(Loop):
    
    nm1: Annotated[L2100B_NM1, Title('Information Receiver Name'), Usage('R'), Position(500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class L2200B_TRN(Segment):
    """Information Receiver Trace Identifier"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['2'])]
    
    trn02: Annotated[D_127, Title('Claim Transaction Batch Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200B_STC01(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc01_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['41', 'AY', 'PR'])]
    
    stc01_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(4)]


class L2200B_STC10(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc10_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc10_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(4)]


class L2200B_STC11(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc11_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc11_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(4)]


class L2200B_STC(Segment):
    """Information Receiver Status Information"""
    _segment_name = 'STC'
    
    stc01: Annotated[L2200B_STC01, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('N'), Position(3)]
    
    stc04: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(4)]
    
    stc05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check Number'), Usage('N'), Position(9)]
    
    stc10: Annotated[L2200B_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2200B_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2200B(Loop):
    
    trn: Annotated[L2200B_TRN, Title('Information Receiver Trace Identifier'), Usage('R'), Position(900), Required(True)]
    ItemStc: TypeAlias = Annotated[L2200B_STC, Title('Information Receiver Status Information'), Usage('R'), Position(1000), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title('Information Receiver Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title('Information Receiver Name'), Usage('R'), Position(500), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2200B: TypeAlias = Annotated[L2200B, Title('Information Receiver Trace Identifier'), Usage('S'), Position(900), Required(True)]
    l2200b: Annotated[list[ItemL2200B], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Information Source Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100A: TypeAlias = Annotated[L2100A, Title('Payer Name'), Usage('R'), Position(500), Required(True)]
    l2100a: Annotated[list[ItemL2100A], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Information Receiver Level'), Usage('R'), Position(100), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class L2000C_HL(Segment):
    """Service Provider Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['19'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0', '1'])]


class L2100C_NM1(Segment):
    """Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['1P'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Provider Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['FI', 'SV', 'XX'])]
    
    nm109: Annotated[D_67, Title('Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100C(Loop):
    
    nm1: Annotated[L2100C_NM1, Title('Provider Name'), Usage('R'), Position(500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class L2200C_TRN(Segment):
    """Provider of Service Trace Identifier"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Provider of Service Information Trace Identifier'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200C_STC01(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc01_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['1P'])]
    
    stc01_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(4)]


class L2200C_STC10(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc10_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc10_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(4)]


class L2200C_STC11(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc11_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc11_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(4)]


class L2200C_STC(Segment):
    """Provider Status Information"""
    _segment_name = 'STC'
    
    stc01: Annotated[L2200C_STC01, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('N'), Position(3)]
    
    stc04: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(4)]
    
    stc05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check Number'), Usage('N'), Position(9)]
    
    stc10: Annotated[L2200C_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2200C_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2200C(Loop):
    
    trn: Annotated[L2200C_TRN, Title('Provider of Service Trace Identifier'), Usage('R'), Position(900), Required(True)]
    ItemStc: TypeAlias = Annotated[L2200C_STC, Title('Provider Status Information'), Usage('R'), Position(1000), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title('Service Provider Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100C: TypeAlias = Annotated[L2100C, Title('Provider Name'), Usage('R'), Position(500), Required(True)]
    l2100c: Annotated[list[ItemL2100C], MinItems(2)]
    ItemL2200C: TypeAlias = Annotated[L2200C, Title('Provider of Service Trace Identifier'), Usage('S'), Position(900), Required(True)]
    l2200c: Annotated[list[ItemL2200C], MinItems(1)]


class TABLE2AREA4(Loop):
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Service Provider Level'), Usage('S'), Position(100), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000D_HL(Segment):
    """Subscriber Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['22'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['0', '1'])]


class L2100D_NM1(Segment):
    """Subscriber Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Subscriber Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Subscriber First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Subscriber Middle Name or Initial'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Subscriber Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['24', 'II', 'MI'])]
    
    nm109: Annotated[D_67, Title('Subscriber Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100D(Loop):
    
    nm1: Annotated[L2100D_NM1, Title('Subscriber Name'), Usage('R'), Position(500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class L2200D_TRN(Segment):
    """Claim Status Tracking Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['2'])]
    
    trn02: Annotated[D_127, Title('Referenced Transaction Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200D_STC01(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc01_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ'])]
    
    stc01_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2200D_STC10(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc10_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc10_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2200D_STC11(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc11_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc11_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2200D_STC(Segment):
    """Claim Level Status Information"""
    _segment_name = 'STC'
    
    stc01: Annotated[L2200D_STC01, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('N'), Position(3)]
    
    stc04: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('S'), Position(4)]
    
    stc05: Annotated[D_782, Title('Claim Payment Amount'), Usage('S'), Position(5)]
    
    stc06: Annotated[D_373, Title('Adjudication Finalized Date'), Usage('S'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Remittance Date'), Usage('S'), Position(8)]
    
    stc09: Annotated[D_429, Title('Remittance Trace Number'), Usage('S'), Position(9)]
    
    stc10: Annotated[L2200D_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2200D_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2200D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Payer Claim Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1K'])]
    
    ref02: Annotated[D_127, Title('Payer Claim Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Institutional Bill Type Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BLT'])]
    
    ref02: Annotated[D_127, Title('Bill Type Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Patient Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EJ'])]
    
    ref02: Annotated[D_127, Title('Patient Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Pharmacy Prescription Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['XZ'])]
    
    ref02: Annotated[D_127, Title('Pharmacy Prescription Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Voucher Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['VV'])]
    
    ref02: Annotated[D_127, Title('Voucher Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Claim Identification Number For Clearinghouses and Other Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Clearinghouse Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_DTP(Segment):
    """Claim Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Claim Service Period'), Usage('R'), Position(3)]


class L2220D_SVC01(Composite):
    """Composite Medical Procedure Identifier"""
    
    svc01_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU', 'WK'])]
    
    svc01_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svc01_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svc01_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svc01_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svc01_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svc01_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    svc01_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2220D_SVC06(Composite):
    """Composite Medical Procedure Identifier"""
    pass


class L2220D_SVC(Segment):
    """Service Line Information"""
    _segment_name = 'SVC'
    
    svc01: Annotated[L2220D_SVC01, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    svc02: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    svc03: Annotated[D_782, Title('Line Item Payment Amount'), Usage('R'), Position(3)]
    
    svc04: Annotated[D_234, Title('Revenue Code'), Usage('S'), Position(4)]
    
    svc05: Annotated[D_380, Title('Quantity'), Usage('N'), Position(5)]
    
    svc07: Annotated[D_380, Title('Units of Service Count'), Usage('R'), Position(7)]


class L2220D_STC01(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc01_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ'])]
    
    stc01_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2220D_STC10(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc10_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc10_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2220D_STC11(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc11_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc11_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2220D_STC(Segment):
    """Service Line Status Information"""
    _segment_name = 'STC'
    
    stc01: Annotated[L2220D_STC01, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('N'), Position(3)]
    
    stc04: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(4)]
    
    stc05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check Number'), Usage('N'), Position(9)]
    
    stc10: Annotated[L2220D_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2220D_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2220D_REF04(Composite):
    """Reference Identifier"""
    pass


class L2220D_REF(Segment):
    """Service Line Item Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['FJ'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2220D_DTP(Segment):
    """Service Line Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Line Date'), Usage('R'), Position(3)]


class L2220D(Loop):
    
    svc: Annotated[L2220D_SVC, Title('Service Line Information'), Usage('R'), Position(1800), Required(True)]
    ItemStc: TypeAlias = Annotated[L2220D_STC, Title('Service Line Status Information'), Usage('R'), Position(1900), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]
    
    ref: Annotated[L2220D_REF, Title('Service Line Item Identification'), Usage('S'), Position(2000), Syntax(['R0203']), Required(True)]
    
    dtp: Annotated[L2220D_DTP, Title('Service Line Date'), Usage('R'), Position(2100), Required(True)]


class L2200D(Loop):
    
    trn: Annotated[L2200D_TRN, Title('Claim Status Tracking Number'), Usage('R'), Position(900), Required(True)]
    ItemStc: TypeAlias = Annotated[L2200D_STC, Title('Claim Level Status Information'), Usage('R'), Position(1000), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]
    
    ref: Annotated[L2200D_REF, Title('Payer Claim Control Number'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Institutional Bill Type Identification'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Patient Control Number'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Pharmacy Prescription Number'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Voucher Identifier'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Claim Identification Number For Clearinghouses and Other Transmission Intermediaries'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    dtp: Annotated[L2200D_DTP, Title('Claim Service Date'), Usage('S'), Position(1200), Required(True)]
    ItemL2220D: TypeAlias = Annotated[L2220D, Title('Service Line Information'), Usage('S'), Position(1800), Required(True)]
    l2220d: Annotated[list[ItemL2220D], MinItems(1)]


class L2000D(Loop):
    
    hl: Annotated[L2000D_HL, Title('Subscriber Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100D: TypeAlias = Annotated[L2100D, Title('Subscriber Name'), Usage('R'), Position(500), Required(True)]
    l2100d: Annotated[list[ItemL2100D], MinItems(1)]
    ItemL2200D: TypeAlias = Annotated[L2200D, Title('Claim Status Tracking Number'), Usage('S'), Position(900), Required(True)]
    l2200d: Annotated[list[ItemL2200D], MinItems(1)]


class TABLE2AREA5(Loop):
    ItemL2000D: TypeAlias = Annotated[L2000D, Title('Subscriber Level'), Usage('S'), Position(100), Required(True)]
    l2000d: Annotated[list[ItemL2000D], MinItems(1)]


class L2000E_HL(Segment):
    """Dependent Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['23'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('N'), Position(4)]


class L2100E_NM1(Segment):
    """Dependent Name"""
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


class L2100E(Loop):
    
    nm1: Annotated[L2100E_NM1, Title('Dependent Name'), Usage('R'), Position(500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class L2200E_TRN(Segment):
    """Claim Status Tracking Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['2'])]
    
    trn02: Annotated[D_127, Title('Referenced Transaction Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200E_STC01(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc01_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ'])]
    
    stc01_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2200E_STC10(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc10_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc10_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2200E_STC11(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc11_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc11_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2200E_STC(Segment):
    """Claim Level Status Information"""
    _segment_name = 'STC'
    
    stc01: Annotated[L2200E_STC01, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('N'), Position(3)]
    
    stc04: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('S'), Position(4)]
    
    stc05: Annotated[D_782, Title('Claim Payment Amount'), Usage('S'), Position(5)]
    
    stc06: Annotated[D_373, Title('Adjudication Finalized Date'), Usage('S'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Remittance Date'), Usage('S'), Position(8)]
    
    stc09: Annotated[D_429, Title('Remittance Trace Number'), Usage('S'), Position(9)]
    
    stc10: Annotated[L2200E_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2200E_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2200E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Payer Claim Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1K'])]
    
    ref02: Annotated[D_127, Title('Payer Claim Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Institutional Bill Type Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['BLT'])]
    
    ref02: Annotated[D_127, Title('Bill Type Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Patient Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EJ'])]
    
    ref02: Annotated[D_127, Title('Patient Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Pharmacy Prescription Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['XZ'])]
    
    ref02: Annotated[D_127, Title('Pharmacy Prescription Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Voucher Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['VV'])]
    
    ref02: Annotated[D_127, Title('Voucher Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2200E_REF(Segment):
    """Claim Identification Number For Clearinghouses and Other Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Clearinghouse Trace Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200E_DTP(Segment):
    """Claim Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Claim Service Period'), Usage('R'), Position(3)]


class L2220E_SVC01(Composite):
    """Composite Medical Procedure Identifier"""
    
    svc01_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU', 'WK'])]
    
    svc01_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svc01_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svc01_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svc01_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svc01_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svc01_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    svc01_08: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(8)]


class L2220E_SVC06(Composite):
    """Composite Medical Procedure Identifier"""
    pass


class L2220E_SVC(Segment):
    """Service Line Information"""
    _segment_name = 'SVC'
    
    svc01: Annotated[L2220E_SVC01, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    svc02: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    svc03: Annotated[D_782, Title('Line Item Payment Amount'), Usage('R'), Position(3)]
    
    svc04: Annotated[D_234, Title('Revenue Code'), Usage('S'), Position(4)]
    
    svc05: Annotated[D_380, Title('Quantity'), Usage('N'), Position(5)]
    
    svc07: Annotated[D_380, Title('Units of Service Count'), Usage('R'), Position(7)]


class L2220E_STC01(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc01_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['03', '13', '17', '1E', '1G', '1H', '1I', '1O', '1P', '1Q', '1R', '1S', '1T', '1U', '1V', '1W', '1X', '1Y', '1Z', '28', '2A', '2B', '2D', '2E', '2I', '2K', '2P', '2Q', '2S', '2Z', '30', '36', '3A', '3C', '3D', '3E', '3F', '3G', '3H', '3I', '3J', '3K', '3L', '3M', '3N', '3O', '3P', '3Q', '3R', '3S', '3T', '3U', '3V', '3W', '3X', '3Y', '3Z', '40', '43', '44', '4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I', '4J', '4L', '4M', '4N', '4O', '4P', '4Q', '4R', '4S', '4U', '4V', '4W', '4X', '4Y', '4Z', '5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I', '5J', '5K', '5L', '5M', '5N', '5O', '5P', '5Q', '5R', '5S', '5T', '5U', '5V', '5W', '5X', '5Y', '5Z', '61', '6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I', '6J', '6K', '6L', '6M', '6N', '6O', '6P', '6Q', '6R', '6S', '6U', '6V', '6W', '6X', '6Y', '71', '72', '73', '74', '77', '7C', '80', '82', '84', '85', '87', '95', 'CK', 'CZ', 'D2', 'DD', 'DJ', 'DK', 'DN', 'DO', 'DQ', 'E1', 'E2', 'E7', 'E9', 'FA', 'FD', 'FE', 'G0', 'G3', 'GB', 'GD', 'GI', 'GJ', 'GK', 'GM', 'GY', 'HF', 'HH', 'I3', 'IJ', 'IL', 'IN', 'LI', 'LR', 'MR', 'MSC', 'OB', 'OD', 'OX', 'P0', 'P2', 'P3', 'P4', 'P6', 'P7', 'PRP', 'PT', 'PV', 'PW', 'QA', 'QB', 'QC', 'QD', 'QE', 'QH', 'QK', 'QL', 'QN', 'QO', 'QS', 'QV', 'QY', 'RC', 'RW', 'S4', 'SEP', 'SJ', 'SU', 'T4', 'TL', 'TQ', 'TT', 'TTP', 'TU', 'UH', 'X3', 'X4', 'X5', 'ZZ'])]
    
    stc01_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2220E_STC10(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc10_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc10_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2220E_STC11(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc11_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3)]
    
    stc11_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(4), Enumerated(*['RX'])]


class L2220E_STC(Segment):
    """Service Line Status Information"""
    _segment_name = 'STC'
    
    stc01: Annotated[L2220E_STC01, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('N'), Position(3)]
    
    stc04: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(4)]
    
    stc05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check Number'), Usage('N'), Position(9)]
    
    stc10: Annotated[L2220E_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2220E_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2220E_REF04(Composite):
    """Reference Identifier"""
    pass


class L2220E_REF(Segment):
    """Service Line Item Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['FJ'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2220E_DTP(Segment):
    """Service Line Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Line Date'), Usage('R'), Position(3)]


class L2220E(Loop):
    
    svc: Annotated[L2220E_SVC, Title('Service Line Information'), Usage('R'), Position(1800), Required(True)]
    ItemStc: TypeAlias = Annotated[L2220E_STC, Title('Service Line Status Information'), Usage('R'), Position(1900), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]
    
    ref: Annotated[L2220E_REF, Title('Service Line Item Identification'), Usage('S'), Position(2000), Syntax(['R0203']), Required(True)]
    
    dtp: Annotated[L2220E_DTP, Title('Service Line Date'), Usage('R'), Position(2100), Required(True)]


class L2200E(Loop):
    
    trn: Annotated[L2200E_TRN, Title('Claim Status Tracking Number'), Usage('R'), Position(900), Required(True)]
    ItemStc: TypeAlias = Annotated[L2200E_STC, Title('Claim Level Status Information'), Usage('R'), Position(1000), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]
    
    ref: Annotated[L2200E_REF, Title('Payer Claim Control Number'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Institutional Bill Type Identification'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Patient Control Number'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Pharmacy Prescription Number'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Voucher Identifier'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2200E_REF, Title('Claim Identification Number For Clearinghouses and Other Transmission Intermediaries'), Usage('S'), Position(1100), Syntax(['R0203']), Required(True)]
    
    dtp: Annotated[L2200E_DTP, Title('Claim Service Date'), Usage('S'), Position(1200), Required(True)]
    ItemL2220E: TypeAlias = Annotated[L2220E, Title('Service Line Information'), Usage('S'), Position(1800), Required(True)]
    l2220e: Annotated[list[ItemL2220E], MinItems(1)]


class L2000E(Loop):
    
    hl: Annotated[L2000E_HL, Title('Dependent Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100E: TypeAlias = Annotated[L2100E, Title('Dependent Name'), Usage('R'), Position(500), Required(True)]
    l2100e: Annotated[list[ItemL2100E], MinItems(1)]
    ItemL2200E: TypeAlias = Annotated[L2200E, Title('Claim Status Tracking Number'), Usage('R'), Position(900), Required(True)]
    l2200e: Annotated[list[ItemL2200E], MinItems(1)]


class TABLE2AREA6(Loop):
    ItemL2000E: TypeAlias = Annotated[L2000E, Title('Dependent Level'), Usage('S'), Position(100), Required(True)]
    l2000e: Annotated[list[ItemL2000E], MinItems(1)]


class DETAIL(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title('Information Source Level'), Usage('R'), Position(100), Required(True)]
    l2000a: Annotated[list[ItemL2000A], MinItems(1)]
    ItemTable2Area4: TypeAlias = Annotated[TABLE2AREA4, Title('Table2 - Area4'), Usage('S'), Position(140)]
    table2area4: Annotated[list[ItemTable2Area4], MinItems(1)]
    ItemTable2Area5: TypeAlias = Annotated[TABLE2AREA5, Title('Table2 - Area5'), Usage('S'), Position(150)]
    table2area5: Annotated[list[ItemTable2Area5], MinItems(1)]
    ItemTable2Area6: TypeAlias = Annotated[TABLE2AREA6, Title('Table2 - Area6'), Usage('S'), Position(160)]
    table2area6: Annotated[list[ItemTable2Area6], MinItems(1)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(100), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Header'), Usage('R'), Position(110), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table2 - Detail'), Usage('R'), Position(120), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]


class FOOTER(Loop):
    pass


class TABLE2AREA3_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class TABLE2AREA3(Loop):
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Footer'), Usage('N'), Position(170)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[TABLE2AREA3_SE, Title('Transaction Set Trailer'), Usage('R'), Position(2700), Required(True)]


class GS_LOOP_GE(Segment):
    """Functional Group Trailer"""
    _segment_name = 'GE'
    
    ge01: Annotated[D_97, Title('Number of Transaction Sets Included'), Usage('R'), Position(1)]
    
    ge02: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(2)]


class GS_LOOP(Loop):
    
    gs: Annotated[GS_LOOP_GS, Title('Functional Group Header'), Usage('R'), Position(100), Required(True)]
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title('Transaction Set Header'), Usage('R'), Position(200), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
    
    table2area3: Annotated[TABLE2AREA3, Title('Table2 - Area3'), Usage('R'), Position(130), Required(True)]
    
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


class MSG277A1(Message):
    """HIPAA Health Care Information Status Notification 005010X212 277A1"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
