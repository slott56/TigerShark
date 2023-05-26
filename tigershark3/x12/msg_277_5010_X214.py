"""
277.5010.X214
Created 2023-05-19 10:17:35.866604
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
    
    isa05: Annotated[I05, Title('Interchange Sender ID Qualifier'), Usage('R'), Position(5), Enumerated(*['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ'])]
    
    isa06: Annotated[I06, Title('Interchange Sender ID'), Usage('R'), Position(6)]
    
    isa07: Annotated[I05, Title('Interchange Receiver ID Qualifier'), Usage('R'), Position(7), Enumerated(*['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ'])]
    
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
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['HN'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Functional Group Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Functional Group Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['005010X214'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['277'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title('Version, Release, or Industry Identifier'), Usage('R'), Position(3), Enumerated(*['005010X214'])]


class HEADER_BHT(Segment):
    """Beginning of Hierarchical Transaction"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title('Hierarchical Structure Code'), Usage('R'), Position(1), Enumerated(*['0085'])]
    
    bht02: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(2), Enumerated(*['08'])]
    
    bht03: Annotated[D_127, Title('Originator Application Transaction Identifier'), Usage('R'), Position(3)]
    
    bht04: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title('Transaction Set Creation Time'), Usage('R'), Position(5)]
    
    bht06: Annotated[D_640, Title('Transaction Type Code'), Usage('R'), Position(6), Enumerated(*['TH'])]


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
    """Information Source Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR', 'AY'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Payer Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['46', 'FI', 'PI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Payer Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100A(Loop):
    
    nm1: Annotated[L2100A_NM1, Title('Information Source Name'), Usage('R'), Position(500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class L2200A_TRN(Segment):
    """Transmission Receipt Control Identifier"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Information Source Application Trace Identifier'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200A_DTP(Segment):
    """Information Source Receipt Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['050'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Information Source Receipt Date'), Usage('R'), Position(3)]


class L2200A_DTP(Segment):
    """Information Source Process Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['009'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Information Source Process Date'), Usage('R'), Position(3)]


class L2200A(Loop):
    
    trn: Annotated[L2200A_TRN, Title('Transmission Receipt Control Identifier'), Usage('R'), Position(900), Required(True)]
    
    dtp: Annotated[L2200A_DTP, Title('Information Source Receipt Date'), Usage('R'), Position(1200), Required(True)]
    
    dtp: Annotated[L2200A_DTP, Title('Information Source Process Date'), Usage('R'), Position(1200), Required(True)]


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
    
    nm103: Annotated[D_1035, Title('Information Receiver Last or Organization Name'), Usage('R'), Position(3)]
    
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
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['36', '40', '41', 'AY', 'PR'])]
    
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
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('R'), Position(3), Enumerated(*['U', 'WQ'])]
    
    stc04: Annotated[D_782, Title('Total Submitted Charges for Unit Work'), Usage('R'), Position(4)]
    
    stc05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check Number'), Usage('N'), Position(9)]
    
    stc10: Annotated[L2200B_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2200B_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2200B_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2200B_QTY(Segment):
    """Total Accepted Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['90'])]
    
    qty02: Annotated[D_380, Title('Total Accepted Quantity'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2200B_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2200B_QTY(Segment):
    """Total Rejected Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['AA'])]
    
    qty02: Annotated[D_380, Title('Total Rejected Quantity'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2200B_AMT(Segment):
    """Total Accepted Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['YU'])]
    
    amt02: Annotated[D_782, Title('Total Accepted Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2200B_AMT(Segment):
    """Total Rejected Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['YY'])]
    
    amt02: Annotated[D_782, Title('Total Rejected Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2200B(Loop):
    
    trn: Annotated[L2200B_TRN, Title('Information Receiver Trace Identifier'), Usage('R'), Position(900), Required(True)]
    ItemStc: TypeAlias = Annotated[L2200B_STC, Title('Information Receiver Status Information'), Usage('R'), Position(1000), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]
    
    qty: Annotated[L2200B_QTY, Title('Total Accepted Quantity'), Usage('S'), Position(1210), Syntax(['E0204', 'R0204']), Required(True)]
    
    qty: Annotated[L2200B_QTY, Title('Total Rejected Quantity'), Usage('S'), Position(1210), Syntax(['E0204', 'R0204']), Required(True)]
    
    amt: Annotated[L2200B_AMT, Title('Total Accepted Amount'), Usage('S'), Position(1220), Required(True)]
    
    amt: Annotated[L2200B_AMT, Title('Total Rejected Amount'), Usage('S'), Position(1220), Required(True)]


class L2000C_HL(Segment):
    """Billing Provider of Service Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['19'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('R'), Position(4), Enumerated(*['1'])]


class L2100C_NM1(Segment):
    """Billing Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['85'])]
    
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
    
    nm1: Annotated[L2100C_NM1, Title('Billing Provider Name'), Usage('R'), Position(500), Required(True)]


class L2200C_TRN(Segment):
    """Provider of Service Information Trace Identifier"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Provider of Service Information Trace Identifier'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200C_STC01(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1)]
    
    stc01_02: Annotated[D_1271, Title('Status Code'), Usage('R'), Position(2)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['36', '40', '41', '77', '82', '85', '87', 'AY', 'PR'])]
    
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
    """Billing Provider Status Information"""
    _segment_name = 'STC'
    
    stc01: Annotated[L2200C_STC01, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('N'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('R'), Position(3), Enumerated(*['U', 'WQ'])]
    
    stc04: Annotated[D_782, Title('Total Submitted Charges for Unit Work'), Usage('R'), Position(4)]
    
    stc05: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check Number'), Usage('N'), Position(9)]
    
    stc10: Annotated[L2200C_STC10, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    stc11: Annotated[L2200C_STC11, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-form Message Text'), Usage('N'), Position(12)]


class L2200C_C040(Composite):
    """Reference Identifier"""
    pass


class L2200C_REF(Segment):
    """Provider Secondary Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200C_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2200C_QTY(Segment):
    """Total Accepted Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['QA'])]
    
    qty02: Annotated[D_380, Title('Total Accepted Quantity'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2200C_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class L2200C_QTY(Segment):
    """Total Rejected Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    qty02: Annotated[D_380, Title('Total Rejected Quantity'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L2200C_AMT(Segment):
    """Total Accepted Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['YU'])]
    
    amt02: Annotated[D_782, Title('Total Accepted Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2200C_AMT(Segment):
    """Total Rejected Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['YY'])]
    
    amt02: Annotated[D_782, Title('Total Rejected Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2200C(Loop):
    
    trn: Annotated[L2200C_TRN, Title('Provider of Service Information Trace Identifier'), Usage('R'), Position(900), Required(True)]
    ItemStc: TypeAlias = Annotated[L2200C_STC, Title('Billing Provider Status Information'), Usage('R'), Position(1000), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]
    
    ref: Annotated[L2200C_REF, Title('Provider Secondary Identifier'), Usage('S'), Position(1100), Required(True)]
    
    qty: Annotated[L2200C_QTY, Title('Total Accepted Quantity'), Usage('S'), Position(1210), Syntax(['E0204', 'R0204']), Required(True)]
    
    qty: Annotated[L2200C_QTY, Title('Total Rejected Quantity'), Usage('S'), Position(1210), Syntax(['E0204', 'R0204']), Required(True)]
    
    amt: Annotated[L2200C_AMT, Title('Total Accepted Amount'), Usage('S'), Position(1220), Required(True)]
    
    amt: Annotated[L2200C_AMT, Title('Total Rejected Amount'), Usage('S'), Position(1220), Required(True)]


class L2000D_HL(Segment):
    """Patient Level"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['PT'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('N'), Position(4), Enumerated(*['0', '1'])]


class L2100D_NM1(Segment):
    """Patient Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Patient Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Patient First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Patient Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Patient Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Patient Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['II', 'MI'])]
    
    nm109: Annotated[D_67, Title('Patient Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100D(Loop):
    
    nm1: Annotated[L2100D_NM1, Title('Patient Name'), Usage('R'), Position(500), Required(True)]


class L2200D_TRN(Segment):
    """Claim Status Tracking Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['2'])]
    
    trn02: Annotated[D_127, Title('Patient Control Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('N'), Position(3)]
    
    trn04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200D_C043(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1), Enumerated(*claim_status_cat)]
    
    stc01_02: Annotated[D_1271, Title('Health Care Claim Status Code'), Usage('R'), Position(2), Enumerated(*claim_status)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['03', '1P', '1Z', '40', '41', '71', '72', '73', '77', '82', '85', '87', 'DK', 'DN', 'DQ', 'FA', 'GB', 'HK', 'IL', 'LI', 'MSC', 'PR', 'PRP', 'QB', 'QC', 'QD', 'SEP', 'TL', 'TTP', 'TU'])]
    
    stc01_04: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('N'), Position(4)]


class L2200D_C043(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1), Enumerated(*claim_status_cat)]
    
    stc10_02: Annotated[D_1271, Title('Health Care Claim Status Code'), Usage('R'), Position(2), Enumerated(*claim_status)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*entity_id)]


class L2200D_C043(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1), Enumerated(*claim_status_cat)]
    
    stc11_02: Annotated[D_1271, Title('Health Care Claim Status Code'), Usage('R'), Position(2), Enumerated(*claim_status)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*entity_id)]


class L2200D_STC(Segment):
    """Claim Level Status Information"""
    _segment_name = 'STC'
    
    c043: Annotated[L2200D_C043, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('R'), Position(3), Enumerated(*['U', 'WQ'])]
    
    stc04: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(4)]
    
    stc05: Annotated[D_782, Title('Claim Payment Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Adjudication or Payment Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7), Enumerated(*['ACH', 'BOP', 'CHK', 'FWT', 'NON'])]
    
    stc08: Annotated[D_373, Title('Check Issue or EFT Effective Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check or EFT Trace Number'), Usage('N'), Position(9)]
    
    c043: Annotated[L2200D_C043, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    c043: Annotated[L2200D_C043, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-Form Message Text'), Usage('S'), Position(12)]


class L2200D_C040(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Payer Claim Control Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1K'])]
    
    ref02: Annotated[D_127, Title('Payer Claim Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2200D_C040(Composite):
    """Reference Identifier"""
    pass


class L2200D_REF(Segment):
    """Claim Indentifier Number For Clearinghouses and Other Transmission Intermediaries"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title('Claim Indentifier Number For Clearinghouses and Other Transmission Intermediaries'), Usage('R'), Position(2)]
    
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


class L2200D_DTP(Segment):
    """Claim Level Service Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['RD8', 'D8'])]
    
    dtp03: Annotated[D_1251, Title('Claim Service Period'), Usage('R'), Position(3)]


class L2220D_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svc01_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'ER', 'HC', 'HP', 'IV', 'NU', 'NU', 'WK'])]
    
    svc01_02: Annotated[D_234, Title('Service Identification Code'), Usage('R'), Position(2)]
    
    svc01_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svc01_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svc01_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svc01_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svc01_07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2220D_C003(Composite):
    """Composite Medical Procedure Identifier"""
    pass


class L2220D_SVC(Segment):
    """Service Line Information"""
    _segment_name = 'SVC'
    
    c003: Annotated[L2220D_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    svc02: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    svc03: Annotated[D_782, Title('Line Item Provider Payment Amount'), Usage('N'), Position(3)]
    
    svc04: Annotated[D_234, Title('Revenue Code'), Usage('S'), Position(4)]
    
    svc05: Annotated[D_380, Title('Quantity'), Usage('N'), Position(5)]
    
    svc07: Annotated[D_380, Title('Original Units of Service Count'), Usage('S'), Position(7)]


class L2220D_C043(Composite):
    """Health Care Claim Status"""
    
    stc01_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1), Enumerated(*claim_status_cat)]
    
    stc01_02: Annotated[D_1271, Title('Health Care Claim Status Code'), Usage('R'), Position(2), Enumerated(*claim_status)]
    
    stc01_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*['03', '1P', '1Z', '40', '41', '71', '72', '73', '77', '82', '85', '87', 'DK', 'DN', 'DQ', 'FA', 'GB', 'HK', 'IL', 'LI', 'MSC', 'PR', 'PRP', 'QB', 'QC', 'QD', 'SEP', 'TL', 'TTP', 'TU'])]


class L2220D_C043(Composite):
    """Health Care Claim Status"""
    
    stc10_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1), Enumerated(*claim_status_cat)]
    
    stc10_02: Annotated[D_1271, Title('Health Care Claim Status Code'), Usage('R'), Position(2), Enumerated(*claim_status)]
    
    stc10_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*entity_id)]


class L2220D_C043(Composite):
    """Health Care Claim Status"""
    
    stc11_01: Annotated[D_1271, Title('Health Care Claim Status Category Code'), Usage('R'), Position(1), Enumerated(*claim_status_cat)]
    
    stc11_02: Annotated[D_1271, Title('Health Care Claim Status Code'), Usage('R'), Position(2), Enumerated(*claim_status)]
    
    stc11_03: Annotated[D_98, Title('Entity Identifier Code'), Usage('S'), Position(3), Enumerated(*entity_id)]


class L2220D_STC(Segment):
    """Service Line Level Status Information"""
    _segment_name = 'STC'
    
    c043: Annotated[L2220D_C043, Title('Health Care Claim Status'), Usage('R'), Position(1), Required(True)]
    
    stc02: Annotated[D_373, Title('Status Information Effective Date'), Usage('R'), Position(2)]
    
    stc03: Annotated[D_306, Title('Action Code'), Usage('R'), Position(3), Enumerated(*['U'])]
    
    stc04: Annotated[D_782, Title('Line Item Charge Amount'), Usage('N'), Position(4)]
    
    stc05: Annotated[D_782, Title('Line Item Provider Payment Amount'), Usage('N'), Position(5)]
    
    stc06: Annotated[D_373, Title('Date'), Usage('N'), Position(6)]
    
    stc07: Annotated[D_591, Title('Payment Method Code'), Usage('N'), Position(7)]
    
    stc08: Annotated[D_373, Title('Date'), Usage('N'), Position(8)]
    
    stc09: Annotated[D_429, Title('Check Number'), Usage('N'), Position(9)]
    
    c043: Annotated[L2220D_C043, Title('Health Care Claim Status'), Usage('S'), Position(10), Required(True)]
    
    c043: Annotated[L2220D_C043, Title('Health Care Claim Status'), Usage('S'), Position(11), Required(True)]
    
    stc12: Annotated[D_933, Title('Free-Form Message Text'), Usage('N'), Position(12)]


class L2220D_C040(Composite):
    """Reference Identifier"""
    pass


class L2220D_REF(Segment):
    """Service Line Item Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['FJ'])]
    
    ref02: Annotated[D_127, Title('Line Item Control Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2220D_C040(Composite):
    """Reference Identifier"""
    pass


class L2220D_REF(Segment):
    """Pharmacy Prescription Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['XZ'])]
    
    ref02: Annotated[D_127, Title('Pharmacy Prescription Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2220D_DTP(Segment):
    """Service Line Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Service Line Date'), Usage('R'), Position(3)]


class L2220D(Loop):
    
    svc: Annotated[L2220D_SVC, Title('Service Line Information'), Usage('R'), Position(1800), Required(True)]
    
    stc: Annotated[L2220D_STC, Title('Service Line Level Status Information'), Usage('R'), Position(1900), Required(True)]
    
    ref: Annotated[L2220D_REF, Title('Service Line Item Identification'), Usage('S'), Position(2000), Required(True)]
    
    ref: Annotated[L2220D_REF, Title('Pharmacy Prescription Number'), Usage('S'), Position(2000), Required(True)]
    
    dtp: Annotated[L2220D_DTP, Title('Service Line Date'), Usage('S'), Position(2100), Required(True)]


class L2200D(Loop):
    
    trn: Annotated[L2200D_TRN, Title('Claim Status Tracking Number'), Usage('R'), Position(900), Required(True)]
    ItemStc: TypeAlias = Annotated[L2200D_STC, Title('Claim Level Status Information'), Usage('R'), Position(1000), Required(True)]
    stc: Annotated[list[ItemStc], MinItems(1)]
    
    ref: Annotated[L2200D_REF, Title('Payer Claim Control Number'), Usage('S'), Position(1100), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Claim Indentifier Number For Clearinghouses and Other Transmission Intermediaries'), Usage('S'), Position(1100), Required(True)]
    
    ref: Annotated[L2200D_REF, Title('Institutional Bill Type Identification'), Usage('S'), Position(1100), Required(True)]
    
    dtp: Annotated[L2200D_DTP, Title('Claim Level Service Date'), Usage('R'), Position(1200), Required(True)]
    ItemL2220D: TypeAlias = Annotated[L2220D, Title('Service Line Information'), Usage('S'), Position(1800), Required(True)]
    l2220d: Annotated[list[ItemL2220D], MinItems(1)]


class L2000D(Loop):
    
    hl: Annotated[L2000D_HL, Title('Patient Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100D: TypeAlias = Annotated[L2100D, Title('Patient Name'), Usage('R'), Position(500), Required(True)]
    l2100d: Annotated[list[ItemL2100D], MinItems(1)]
    ItemL2200D: TypeAlias = Annotated[L2200D, Title('Claim Status Tracking Number'), Usage('S'), Position(900), Required(True)]
    l2200d: Annotated[list[ItemL2200D], MinItems(1)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title('Billing Provider of Service Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100C: TypeAlias = Annotated[L2100C, Title('Billing Provider Name'), Usage('R'), Position(500), Required(True)]
    l2100c: Annotated[list[ItemL2100C], MinItems(1)]
    ItemL2200C: TypeAlias = Annotated[L2200C, Title('Provider of Service Information Trace Identifier'), Usage('R'), Position(900), Required(True)]
    l2200c: Annotated[list[ItemL2200C], MinItems(1)]
    ItemL2000D: TypeAlias = Annotated[L2000D, Title('Patient Level'), Usage('R'), Position(2000), Required(True)]
    l2000d: Annotated[list[ItemL2000D], MinItems(1)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title('Information Receiver Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title('Information Receiver Name'), Usage('R'), Position(500), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2200B: TypeAlias = Annotated[L2200B, Title('Information Receiver Trace Identifier'), Usage('R'), Position(900), Required(True)]
    l2200b: Annotated[list[ItemL2200B], MinItems(1)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title('Billing Provider of Service Level'), Usage('R'), Position(2000), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title('Information Source Level'), Usage('R'), Position(100), Required(True)]
    ItemL2100A: TypeAlias = Annotated[L2100A, Title('Information Source Name'), Usage('R'), Position(500), Required(True)]
    l2100a: Annotated[list[ItemL2100A], MinItems(1)]
    ItemL2200A: TypeAlias = Annotated[L2200A, Title('Transmission Receipt Control Identifier'), Usage('R'), Position(900), Required(True)]
    l2200a: Annotated[list[ItemL2200A], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Information Receiver Level'), Usage('R'), Position(2000), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class DETAIL(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title('Information Source Level'), Usage('R'), Position(100), Required(True)]
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
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Header'), Usage('R'), Position(100), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('R'), Position(200), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('N'), Position(3000)]
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


class MSG277(Message):
    """HIPAA Health Care Claim Acknowledgement X214-277"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
