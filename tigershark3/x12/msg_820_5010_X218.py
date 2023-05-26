"""
820.5010.X218
Created 2023-05-19 10:17:35.943883
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
    """820 Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['820'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title('Implementation Convention Reference'), Usage('R'), Position(3), Enumerated(*['005010X218'])]


class HEADER_BPR(Segment):
    """Financial Information"""
    _segment_name = 'BPR'
    
    bpr01: Annotated[D_305, Title('Transaction Handling Code'), Usage('R'), Position(1), Enumerated(*['C', 'D', 'I', 'P', 'U', 'X'])]
    
    bpr02: Annotated[D_782, Title('Total Premium Payment Amount'), Usage('R'), Position(2)]
    
    bpr03: Annotated[D_478, Title('Credit or Debit Flag Code'), Usage('R'), Position(3), Enumerated(*['C'])]
    
    bpr04: Annotated[D_591, Title('Payment Method Code'), Usage('R'), Position(4), Enumerated(*['ACH', 'BOP', 'CHK', 'FWT', 'NON', 'SWT'])]
    
    bpr05: Annotated[D_812, Title('Payment Format Code'), Usage('S'), Position(5), Enumerated(*['CCP', 'CTX'])]
    
    bpr06: Annotated[D_506, Title('Depository Financial Institution (DFI) Identification Number Qualifier'), Usage('S'), Position(6), Enumerated(*['01', '02', '04'])]
    
    bpr07: Annotated[D_507, Title('Originating Depository Financial Institution (DFI) Identifier'), Usage('S'), Position(7)]
    
    bpr08: Annotated[D_569, Title('Account Number Qualifier'), Usage('S'), Position(8), Enumerated(*['ALC', 'DA'])]
    
    bpr09: Annotated[D_508, Title('Sender Bank Account Number'), Usage('S'), Position(9)]
    
    bpr10: Annotated[D_509, Title('Payer Identifier'), Usage('R'), Position(10)]
    
    bpr11: Annotated[D_510, Title('Originating Company Supplemental Code'), Usage('S'), Position(11)]
    
    bpr12: Annotated[D_506, Title('Depository Financial Institution (DFI) Identification Number Qualifier'), Usage('S'), Position(12), Enumerated(*['01', '02', '04'])]
    
    bpr13: Annotated[D_507, Title('Receiving Depository Financial Institution (DFI) Identifier'), Usage('S'), Position(13)]
    
    bpr14: Annotated[D_569, Title('Account Number Qualifier'), Usage('S'), Position(14), Enumerated(*['DA', 'SG'])]
    
    bpr15: Annotated[D_508, Title('Receiver Bank Account Number'), Usage('S'), Position(15)]
    
    bpr16: Annotated[D_373, Title('Check Issue or EFT Effective Date'), Usage('R'), Position(16)]
    
    bpr17: Annotated[D_1048, Title('Business Function Code'), Usage('N'), Position(17)]
    
    bpr18: Annotated[D_506, Title('(DFI) ID Number Qualifier'), Usage('N'), Position(18)]
    
    bpr19: Annotated[D_507, Title('(DFI) Identification Number'), Usage('N'), Position(19)]
    
    bpr20: Annotated[D_569, Title('Account Number Qualifier'), Usage('N'), Position(20)]
    
    bpr21: Annotated[D_508, Title('Account Number'), Usage('N'), Position(21)]


class HEADER_TRN(Segment):
    """Reassociation Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1', '3'])]
    
    trn02: Annotated[D_127, Title('Check or EFT Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Originating Company Identifier'), Usage('S'), Position(3)]
    
    trn04: Annotated[D_127, Title('Originating Company Supplemental Code'), Usage('S'), Position(4)]


class HEADER_CUR(Segment):
    """Foreign Currency Information"""
    _segment_name = 'CUR'
    
    cur01: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['2B', 'PR'])]
    
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


class HEADER_REF04(Composite):
    """Reference Identifier"""
    pass


class HEADER_REF(Segment):
    """Premium Receivers Identification Key"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['14', '17', '18', '2F', '38', '72', 'LB'])]
    
    ref02: Annotated[D_127, Title('Premium Receiver Reference Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class HEADER_DTM(Segment):
    """Process Date"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['009'])]
    
    dtm02: Annotated[D_373, Title('Payer Process Date'), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]


class HEADER_DTM(Segment):
    """Delivery Date"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['035'])]
    
    dtm02: Annotated[D_373, Title('Premium Delivery Date'), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]


class HEADER_DTM(Segment):
    """Coverage Period"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['582'])]
    
    dtm02: Annotated[D_373, Title('Date'), Usage('N'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(5), Enumerated(*['RD8'])]
    
    dtm06: Annotated[D_1251, Title('Coverage Period'), Usage('R'), Position(6)]


class HEADER_DTM(Segment):
    """Creation Date"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['097'])]
    
    dtm02: Annotated[D_373, Title('Date'), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]


class L1000A_N1(Segment):
    """Premium Receiver's Name"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    n102: Annotated[D_93, Title("Premium Receiver's Last or Organization Name"), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(3), Enumerated(*['1', '9', 'EQ', 'FI', 'XV'])]
    
    n104: Annotated[D_67, Title("Premium Receiver's Identification Code"), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1000A_N2(Segment):
    """Premium Receiver Additional Name"""
    _segment_name = 'N2'
    
    n201: Annotated[D_93, Title("Premium Receiver's Additional Name"), Usage('R'), Position(1)]
    
    n202: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]


class L1000A_N3(Segment):
    """Premium Receiver's Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title("Premium Receiver's Address Line"), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title("Premium Receiver's Address Line"), Usage('S'), Position(2)]


class L1000A_N4(Segment):
    """Premium Receiver's City, State, and ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title("Premium Receiver's City Name"), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title("Premium Receiver's State Code"), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title("Premium Receiver's Postal Zone or Zip Code"), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L1000A_RDM04(Composite):
    """Reference Identifier"""
    pass


class L1000A_RDM05(Composite):
    """Reference Identifier"""
    pass


class L1000A_RDM(Segment):
    """Premium Receiver's Remittance Delivery Method"""
    _segment_name = 'RDM'
    
    rdm01: Annotated[D_756, Title('Remittance Delivery Method Code'), Usage('R'), Position(1), Enumerated(*['BM', 'EM', 'FT', 'FX', 'IA', 'OL'])]
    
    rdm02: Annotated[D_93, Title("Premium Receiver's Last or Organization Name"), Usage('S'), Position(2)]
    
    rdm03: Annotated[D_364, Title("Premium Receiver's Communication Number"), Usage('S'), Position(3)]


class L1000A(Loop):
    
    n1: Annotated[L1000A_N1, Title("Premium Receiver's Name"), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    
    n2: Annotated[L1000A_N2, Title('Premium Receiver Additional Name'), Usage('S'), Position(800), Required(True)]
    
    n3: Annotated[L1000A_N3, Title("Premium Receiver's Address"), Usage('S'), Position(900), Required(True)]
    
    n4: Annotated[L1000A_N4, Title("Premium Receiver's City, State, and ZIP Code"), Usage('S'), Position(1000), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    rdm: Annotated[L1000A_RDM, Title("Premium Receiver's Remittance Delivery Method"), Usage('S'), Position(1300), Required(True)]


class L1000B_N1(Segment):
    """Premium Payer's Name"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    n102: Annotated[D_93, Title('Premium Payer Name'), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(3), Enumerated(*['1', '24', '75', '9', 'EQ', 'FI', 'PI'])]
    
    n104: Annotated[D_67, Title('Premium Payer Identifier'), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1000B_N2(Segment):
    """Premium Payer Additional Name"""
    _segment_name = 'N2'
    
    n201: Annotated[D_93, Title('Premium Payer Additional Name'), Usage('R'), Position(1)]
    
    n202: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]


class L1000B_N3(Segment):
    """Premium Payer's Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Premium Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Premium Payer Address Line'), Usage('S'), Position(2)]


class L1000B_N4(Segment):
    """Premium Payer's City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Premium Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Premium Payer State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Premium Payer Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L1000B_PER(Segment):
    """Premium Payer's Administrative Contact"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Premium Payer Contact Name'), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L1000B(Loop):
    
    n1: Annotated[L1000B_N1, Title("Premium Payer's Name"), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    
    n2: Annotated[L1000B_N2, Title('Premium Payer Additional Name'), Usage('S'), Position(800), Required(True)]
    
    n3: Annotated[L1000B_N3, Title("Premium Payer's Address"), Usage('S'), Position(900), Required(True)]
    
    n4: Annotated[L1000B_N4, Title("Premium Payer's City, State, ZIP Code"), Usage('S'), Position(1000), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000B_PER, Title("Premium Payer's Administrative Contact"), Usage('S'), Position(1200), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MinItems(1)]


class L1000C_N1(Segment):
    """Intermediary Bank Information"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['04', '0B', '8W', 'AK', 'BE', 'BK', 'C1', 'C2', 'IAT', 'MJ', 'RB', 'Z6', 'ZB', 'ZL'])]
    
    n102: Annotated[D_93, Title('Intermediary Bank Name'), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(3), Enumerated(*['31', '57', '94', 'A3', 'A4', 'A6', 'CF', 'G', 'PA'])]
    
    n104: Annotated[D_67, Title('Intermediary Bank Identifier'), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1000C_N2(Segment):
    """Intermediary Bank Additional Name"""
    _segment_name = 'N2'
    
    n201: Annotated[D_93, Title('Intermediary Bank Additional Name'), Usage('R'), Position(1)]
    
    n202: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]


class L1000C_N3(Segment):
    """Intermediary Bank's Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Intermediary Bank Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Intermediary Bank Address Line'), Usage('S'), Position(2)]


class L1000C_N4(Segment):
    """Intermediary Bank's City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Intermediary Bank City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Intermediary Bank State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Intermediary Bank Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L1000C_PER(Segment):
    """Intermediary Bank's Administrative Contact"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Intermediary Bank Contact Name'), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L1000C(Loop):
    
    n1: Annotated[L1000C_N1, Title('Intermediary Bank Information'), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    
    n2: Annotated[L1000C_N2, Title('Intermediary Bank Additional Name'), Usage('S'), Position(800), Required(True)]
    
    n3: Annotated[L1000C_N3, Title("Intermediary Bank's Address"), Usage('S'), Position(900), Required(True)]
    
    n4: Annotated[L1000C_N4, Title("Intermediary Bank's City, State, ZIP Code"), Usage('S'), Position(1000), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000C_PER, Title("Intermediary Bank's Administrative Contact"), Usage('S'), Position(1200), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MinItems(1)]


class HEADER(Loop):
    
    bpr: Annotated[HEADER_BPR, Title('Financial Information'), Usage('R'), Position(200), Syntax(['P0607', 'C0809', 'P1213', 'C1415', 'P1819', 'C2021']), Required(True)]
    
    trn: Annotated[HEADER_TRN, Title('Reassociation Trace Number'), Usage('R'), Position(350), Required(True)]
    
    cur: Annotated[HEADER_CUR, Title('Foreign Currency Information'), Usage('S'), Position(400), Syntax(['C0807', 'C0907', 'L101112', 'C1110', 'C1210', 'L131415', 'C1413', 'C1513', 'L161718', 'C1716', 'C1816', 'L192021', 'C2019', 'C2119']), Required(True)]
    ItemRef: TypeAlias = Annotated[HEADER_REF, Title('Premium Receivers Identification Key'), Usage('S'), Position(500), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]
    
    dtm: Annotated[HEADER_DTM, Title('Process Date'), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title('Delivery Date'), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title('Coverage Period'), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title('Creation Date'), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title("Premium Receiver's Name"), Usage('R'), Position(700), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title("Premium Payer's Name"), Usage('R'), Position(1500), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]
    ItemL1000C: TypeAlias = Annotated[L1000C, Title('Intermediary Bank Information'), Usage('S'), Position(2300), Required(True)]
    l1000c: Annotated[list[ItemL1000C], MinItems(14)]


class L2000A_ENT(Segment):
    """Organization Summary Remittance"""
    _segment_name = 'ENT'
    
    ent01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]
    
    ent02: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(2), Enumerated(*['2L', 'AG', 'NH', 'RGA', 'UN'])]
    
    ent03: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(3), Enumerated(*['1', '24', '9', 'FI'])]
    
    ent04: Annotated[D_67, Title('Organization Identification Code'), Usage('R'), Position(4)]
    
    ent05: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(5)]
    
    ent06: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(6)]
    
    ent07: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(7)]
    
    ent08: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(8)]
    
    ent09: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(9)]


class L2200A_ADX(Segment):
    """Organization Summary Remittance Level Adjustment for Previous Payment"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title('Premium Payment Adjustment Amount'), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title('Premium Payment Adjustment Reason'), Usage('R'), Position(2), Enumerated(*['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6', 'RU', 'WO', 'WW'])]
    
    adx03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200A(Loop):
    
    adx: Annotated[L2200A_ADX, Title('Organization Summary Remittance Level Adjustment for Previous Payment'), Usage('R'), Position(800), Syntax(['P0304']), Required(True)]


class L2300A_RMR(Segment):
    """Organization Summary Remittance Detail"""
    _segment_name = 'RMR'
    
    rmr01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['11', '1L', 'CT', 'IK'])]
    
    rmr02: Annotated[D_127, Title('Contract, Invoice, Account, Group, or Policy Number'), Usage('R'), Position(2)]
    
    rmr03: Annotated[D_482, Title('Payment Action Code'), Usage('S'), Position(3), Enumerated(*['PA', 'PI', 'PO', 'PP'])]
    
    rmr04: Annotated[D_782, Title('Detail Premium Payment Amount'), Usage('R'), Position(4)]
    
    rmr05: Annotated[D_782, Title('Billed Premium Amount'), Usage('S'), Position(5)]
    
    rmr06: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(6)]
    
    rmr07: Annotated[D_426, Title('Adjustment Reason Code'), Usage('N'), Position(7)]
    
    rmr08: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]


class L2300A_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300A_REF(Segment):
    """Reference Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Organizational Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['14', '17', '18', '2F', '38', 'E9', 'LB', 'LU', 'ZZ'])]
    
    ref02: Annotated[D_127, Title('Organizational Reference Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300A_DTM(Segment):
    """Organizational Coverage Period"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['582', 'AAG'])]
    
    dtm02: Annotated[D_373, Title('Date'), Usage('S'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(5), Enumerated(*['RD8'])]
    
    dtm06: Annotated[D_1251, Title('Coverage Period'), Usage('S'), Position(6)]


class L2310A_IT1(Segment):
    """Summary Line Item"""
    _segment_name = 'IT1'
    
    it101: Annotated[D_350, Title('Line Item Control Number'), Usage('R'), Position(1)]
    
    it102: Annotated[D_358, Title('Quantity Invoiced'), Usage('N'), Position(2)]
    
    it103: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(3)]
    
    it104: Annotated[D_212, Title('Unit Price'), Usage('N'), Position(4)]
    
    it105: Annotated[D_639, Title('Basis of Unit Price Code'), Usage('N'), Position(5)]
    
    it106: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(6)]
    
    it107: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(7)]
    
    it108: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(8)]
    
    it109: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(9)]
    
    it110: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(10)]
    
    it111: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(11)]
    
    it112: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(12)]
    
    it113: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(13)]
    
    it114: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(14)]
    
    it115: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(15)]
    
    it116: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(16)]
    
    it117: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(17)]
    
    it118: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(18)]
    
    it119: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(19)]
    
    it120: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(20)]
    
    it121: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(21)]
    
    it122: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(22)]
    
    it123: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(23)]
    
    it124: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(24)]
    
    it125: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(25)]


class L2312A_SAC(Segment):
    """Service, Promotion, Allowance, or Charge Information"""
    _segment_name = 'SAC'
    
    sac01: Annotated[D_248, Title('Allowance or Charge Indicator'), Usage('R'), Position(1), Enumerated(*['C'])]
    
    sac02: Annotated[D_1300, Title('Service, Promotion, Allowance, or Charge Code'), Usage('R'), Position(2), Enumerated(*['A172', 'B680', 'D940', 'G740'])]
    
    sac03: Annotated[D_559, Title('Agency Qualifier Code'), Usage('N'), Position(3)]
    
    sac04: Annotated[D_1301, Title('Agency Service, Promotion, Allowance, or Charge Code'), Usage('N'), Position(4)]
    
    sac05: Annotated[D_610, Title('Amount'), Usage('R'), Position(5)]
    
    sac06: Annotated[D_378, Title('Allowance/Charge Percent Qualifier'), Usage('N'), Position(6)]
    
    sac07: Annotated[D_332, Title('Percent, Decimal Format'), Usage('N'), Position(7)]
    
    sac08: Annotated[D_118, Title('Rate'), Usage('N'), Position(8)]
    
    sac09: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(9)]
    
    sac10: Annotated[D_380, Title('Quantity'), Usage('N'), Position(10)]
    
    sac11: Annotated[D_380, Title('Quantity'), Usage('N'), Position(11)]
    
    sac12: Annotated[D_331, Title('Allowance or Charge Method of Handling Code'), Usage('N'), Position(12)]
    
    sac13: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(13)]
    
    sac14: Annotated[D_770, Title('Option Number'), Usage('N'), Position(14)]
    
    sac15: Annotated[D_352, Title('Description'), Usage('N'), Position(15)]
    
    sac16: Annotated[D_819, Title('Language Code'), Usage('N'), Position(16)]


class L2312A(Loop):
    
    sac: Annotated[L2312A_SAC, Title('Service, Promotion, Allowance, or Charge Information'), Usage('R'), Position(2020), Syntax(['R0203', 'P0304', 'P0607', 'P0910', 'C1110', 'C1413', 'C1615']), Required(True)]


class L2315A_SLN05(Composite):
    """Composite Unit of Measure"""
    
    sln05_01: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('R'), Position(1), Enumerated(*['10', 'IE', 'PR'])]
    
    sln05_02: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(2)]
    
    sln05_03: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(3)]
    
    sln05_04: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(4)]
    
    sln05_05: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(5)]
    
    sln05_06: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(6)]
    
    sln05_07: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(7)]
    
    sln05_08: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(8)]
    
    sln05_09: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(9)]
    
    sln05_10: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(10)]
    
    sln05_11: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(11)]
    
    sln05_12: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(12)]
    
    sln05_13: Annotated[D_355, Title('Unit or Basis for Measurement Code'), Usage('N'), Position(13)]
    
    sln05_14: Annotated[D_1018, Title('Exponent'), Usage('N'), Position(14)]
    
    sln05_15: Annotated[D_649, Title('Multiplier'), Usage('N'), Position(15)]


class L2315A_SLN(Segment):
    """Member Count"""
    _segment_name = 'SLN'
    
    sln01: Annotated[D_350, Title('Line Item Control Number'), Usage('R'), Position(1)]
    
    sln02: Annotated[D_350, Title('Assigned Identification'), Usage('N'), Position(2)]
    
    sln03: Annotated[D_662, Title('Information Only Indicator'), Usage('R'), Position(3), Enumerated(*['O'])]
    
    sln04: Annotated[D_380, Title('Head Count'), Usage('R'), Position(4)]
    
    sln05: Annotated[L2315A_SLN05, Title('Composite Unit of Measure'), Usage('R'), Position(5), Required(True)]
    
    sln06: Annotated[D_212, Title('Unit Price'), Usage('N'), Position(6)]
    
    sln07: Annotated[D_639, Title('Basis of Unit Price Code'), Usage('N'), Position(7)]
    
    sln08: Annotated[D_662, Title('Relationship Code'), Usage('N'), Position(8)]
    
    sln09: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(9)]
    
    sln10: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(10)]
    
    sln11: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(11)]
    
    sln12: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(12)]
    
    sln13: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(13)]
    
    sln14: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(14)]
    
    sln15: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(15)]
    
    sln16: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(16)]
    
    sln17: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(17)]
    
    sln18: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(18)]
    
    sln19: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(19)]
    
    sln20: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(20)]
    
    sln21: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(21)]
    
    sln22: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(22)]
    
    sln23: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(23)]
    
    sln24: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(24)]
    
    sln25: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(25)]
    
    sln26: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(26)]
    
    sln27: Annotated[D_235, Title('Product/Service ID Qualifier'), Usage('N'), Position(27)]
    
    sln28: Annotated[D_234, Title('Product/Service ID'), Usage('N'), Position(28)]


class L2315A(Loop):
    
    sln: Annotated[L2315A_SLN, Title('Member Count'), Usage('R'), Position(2040), Syntax(['P0405', 'C0706', 'C0806', 'P0910', 'P1112', 'P1314', 'P1516', 'P1718', 'P1920', 'P2122', 'P2324', 'P2526', 'P2728']), Required(True)]


class L2310A(Loop):
    
    it1: Annotated[L2310A_IT1, Title('Summary Line Item'), Usage('R'), Position(1900), Syntax(['P020304', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425']), Required(True)]
    ItemL2312A: TypeAlias = Annotated[L2312A, Title('Service, Promotion, Allowance, or Charge Information'), Usage('S'), Position(2020), Required(True)]
    l2312a: Annotated[list[ItemL2312A], MinItems(4)]
    ItemL2315A: TypeAlias = Annotated[L2315A, Title('Member Count'), Usage('S'), Position(2040), Required(True)]
    l2315a: Annotated[list[ItemL2315A], MinItems(3)]


class L2320A_ADX(Segment):
    """Organization Summary Remittance Level Adjustment for Current Payment"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(2), Enumerated(*['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA', 'J3'])]
    
    adx03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2320A(Loop):
    
    adx: Annotated[L2320A_ADX, Title('Organization Summary Remittance Level Adjustment for Current Payment'), Usage('R'), Position(2100), Syntax(['P0304']), Required(True)]


class L2300A(Loop):
    
    rmr: Annotated[L2300A_RMR, Title('Organization Summary Remittance Detail'), Usage('R'), Position(1500), Syntax(['P0102', 'P0708']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300A_REF, Title('Reference Information'), Usage('S'), Position(1700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]
    
    dtm: Annotated[L2300A_DTM, Title('Organizational Coverage Period'), Usage('S'), Position(1800), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title('Summary Line Item'), Usage('S'), Position(1900), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(1)]
    ItemL2320A: TypeAlias = Annotated[L2320A, Title('Organization Summary Remittance Level Adjustment for Current Payment'), Usage('S'), Position(2100), Required(True)]
    l2320a: Annotated[list[ItemL2320A], MinItems(1)]


class L2000A(Loop):
    
    ent: Annotated[L2000A_ENT, Title('Organization Summary Remittance'), Usage('R'), Position(100), Syntax(['P020304', 'P050607', 'P0809']), Required(True)]
    ItemL2200A: TypeAlias = Annotated[L2200A, Title('Organization Summary Remittance Level Adjustment for Previous Payment'), Usage('S'), Position(800), Required(True)]
    l2200a: Annotated[list[ItemL2200A], MinItems(1)]
    ItemL2300A: TypeAlias = Annotated[L2300A, Title('Organization Summary Remittance Detail'), Usage('R'), Position(1500), Required(True)]
    l2300a: Annotated[list[ItemL2300A], MinItems(1)]


class TABLE2AREA2(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title('Organization Summary Remittance'), Usage('S'), Position(100), Required(True)]
    l2000a: Annotated[list[ItemL2000A], MinItems(1)]


class L2000B_ENT(Segment):
    """Individual Remittance"""
    _segment_name = 'ENT'
    
    ent01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]
    
    ent02: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(2), Enumerated(*['2J'])]
    
    ent03: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(3), Enumerated(*['34', 'EI', 'II'])]
    
    ent04: Annotated[D_67, Title("Receiver's Individual Identifier"), Usage('R'), Position(4)]
    
    ent05: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(5)]
    
    ent06: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(6)]
    
    ent07: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(7)]
    
    ent08: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(8)]
    
    ent09: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(9)]


class L2100B_NM1(Segment):
    """Individual Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['DO', 'EY', 'IL', 'QE'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Individual Last Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Individual First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Individual Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Individual Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Individual Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['34', 'EI', 'N'])]
    
    nm109: Annotated[D_67, Title('Individual Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100B(Loop):
    
    nm1: Annotated[L2100B_NM1, Title('Individual Name'), Usage('R'), Position(200), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class L2200B_ADX(Segment):
    """Individual Premium Adjustment for Previous Payment"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title('Premium Payment Adjustment Amount'), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title('Premium Payment Adjustment Reason'), Usage('R'), Position(2), Enumerated(*['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6', 'RU', 'WO'])]
    
    adx03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2200B(Loop):
    
    adx: Annotated[L2200B_ADX, Title('Individual Premium Adjustment for Previous Payment'), Usage('R'), Position(800), Syntax(['P0304']), Required(True)]


class L2300B_RMR(Segment):
    """Individual Premium Remittance Detail"""
    _segment_name = 'RMR'
    
    rmr01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['11', '9J', 'AZ', 'B7', 'CT', 'ID', 'IG', 'IK', 'KW'])]
    
    rmr02: Annotated[D_127, Title('Insurance Remittance Reference Number'), Usage('R'), Position(2)]
    
    rmr03: Annotated[D_482, Title('Payment Action Code'), Usage('N'), Position(3)]
    
    rmr04: Annotated[D_782, Title('Detail Premium Payment Amount'), Usage('R'), Position(4)]
    
    rmr05: Annotated[D_782, Title('Billed Premium Amount'), Usage('S'), Position(5)]
    
    rmr06: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(6)]
    
    rmr07: Annotated[D_426, Title('Adjustment Reason Code'), Usage('N'), Position(7)]
    
    rmr08: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(8)]


class L2300B_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300B_REF(Segment):
    """Reference Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Organizational Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['14', '18', '2F', '38', 'E9', 'LU', 'ZZ'])]
    
    ref02: Annotated[D_127, Title('Organizational Reference Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300B_DTM(Segment):
    """Individual Coverage Period"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['582', 'AAG'])]
    
    dtm02: Annotated[D_373, Title('Date'), Usage('S'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(5), Enumerated(*['RD8'])]
    
    dtm06: Annotated[D_1251, Title('Coverage Period'), Usage('S'), Position(6)]


class L2320B_ADX(Segment):
    """Individual Premium Adjustment for Current Payment"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title('Adjustment Amount'), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(2), Enumerated(*['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA', 'J3'])]
    
    adx03: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(4)]


class L2320B(Loop):
    
    adx: Annotated[L2320B_ADX, Title('Individual Premium Adjustment for Current Payment'), Usage('R'), Position(2100), Syntax(['P0304']), Required(True)]


class L2300B(Loop):
    
    rmr: Annotated[L2300B_RMR, Title('Individual Premium Remittance Detail'), Usage('R'), Position(1500), Syntax(['P0102', 'P0708']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300B_REF, Title('Reference Information'), Usage('S'), Position(1700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]
    
    dtm: Annotated[L2300B_DTM, Title('Individual Coverage Period'), Usage('S'), Position(1800), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemL2320B: TypeAlias = Annotated[L2320B, Title('Individual Premium Adjustment for Current Payment'), Usage('S'), Position(2100), Required(True)]
    l2320b: Annotated[list[ItemL2320B], MinItems(1)]


class L2000B(Loop):
    
    ent: Annotated[L2000B_ENT, Title('Individual Remittance'), Usage('R'), Position(100), Syntax(['P020304', 'P050607', 'P0809']), Required(True)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title('Individual Name'), Usage('S'), Position(200), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2200B: TypeAlias = Annotated[L2200B, Title('Individual Premium Adjustment for Previous Payment'), Usage('S'), Position(800), Required(True)]
    l2200b: Annotated[list[ItemL2200B], MinItems(1)]
    ItemL2300B: TypeAlias = Annotated[L2300B, Title('Individual Premium Remittance Detail'), Usage('R'), Position(1500), Required(True)]
    l2300b: Annotated[list[ItemL2300B], MinItems(1)]


class TABLE2AREA3(Loop):
    ItemL2000B: TypeAlias = Annotated[L2000B, Title('Individual Remittance'), Usage('S'), Position(100), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class FOOTER(Loop):
    pass


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('820 Header'), Usage('R'), Position(100), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Header'), Usage('R'), Position(110), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemTable2Area2: TypeAlias = Annotated[TABLE2AREA2, Title('Table2 - Area2'), Usage('S'), Position(120)]
    table2area2: Annotated[list[ItemTable2Area2], MinItems(1)]
    ItemTable2Area3: TypeAlias = Annotated[TABLE2AREA3, Title('Table2 - Area3'), Usage('S'), Position(130)]
    table2area3: Annotated[list[ItemTable2Area3], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Footer'), Usage('N'), Position(140)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(500), Required(True)]


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


class MSG820A1(Message):
    """HIPAA Payment Order/Remittance Advice 005010X218 820A1"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
