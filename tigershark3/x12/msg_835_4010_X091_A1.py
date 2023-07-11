"""
835.4010.X091.A1
Created 2023-05-19 10:17:35.992623
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
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['HP'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010X091A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['835'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class HEADER_BPR(Segment):
    """Financial Information"""
    _segment_name = 'BPR'
    
    bpr01: Annotated[D_305, Title('Transaction Handling Code'), Usage('R'), Position(1), Enumerated(*['C', 'D', 'H', 'I', 'P', 'U', 'X'])]
    
    bpr02: Annotated[D_782, Title('Total Actual Provider Payment Amount'), Usage('R'), Position(2)]
    
    bpr03: Annotated[D_478, Title('Credit or Debit Flag Code'), Usage('R'), Position(3), Enumerated(*['C', 'D'])]
    
    bpr04: Annotated[D_591, Title('Payment Method Code'), Usage('R'), Position(4), Enumerated(*['ACH', 'BOP', 'CHK', 'FWT', 'NON'])]
    
    bpr05: Annotated[D_812, Title('Payment Format Code'), Usage('S'), Position(5), Enumerated(*['CCP', 'CTX'])]
    
    bpr06: Annotated[D_506, Title('Depository Financial Institution (DFI) Identification Number Qualifier'), Usage('S'), Position(6), Enumerated(*['01', '04'])]
    
    bpr07: Annotated[D_507, Title('Sender DFI Identifier'), Usage('S'), Position(7)]
    
    bpr08: Annotated[D_569, Title('Account Number Qualifier'), Usage('S'), Position(8), Enumerated(*['DA'])]
    
    bpr09: Annotated[D_508, Title('Sender Bank Account Number'), Usage('S'), Position(9)]
    
    bpr10: Annotated[D_509, Title('Payer Identifier'), Usage('S'), Position(10)]
    
    bpr11: Annotated[D_510, Title('Originating Company Supplemental Code'), Usage('S'), Position(11)]
    
    bpr12: Annotated[D_506, Title('Depository Financial Institution (DFI) Identification Number Qualifier'), Usage('S'), Position(12), Enumerated(*['01', '04'])]
    
    bpr13: Annotated[D_507, Title('Receiver or Provider Bank ID Number'), Usage('S'), Position(13)]
    
    bpr14: Annotated[D_569, Title('Account Number Qualifier'), Usage('S'), Position(14), Enumerated(*['DA', 'SG'])]
    
    bpr15: Annotated[D_508, Title('Receiver or Provider Account Number'), Usage('S'), Position(15)]
    
    bpr16: Annotated[D_373, Title('Check Issue or EFT Effective Date'), Usage('R'), Position(16)]
    
    bpr17: Annotated[D_1048, Title('Business Function Code'), Usage('N'), Position(17)]
    
    bpr18: Annotated[D_506, Title('(DFI) ID Number Qualifier'), Usage('N'), Position(18)]
    
    bpr19: Annotated[D_507, Title('(DFI) Identification Number'), Usage('N'), Position(19)]
    
    bpr20: Annotated[D_569, Title('Account Number Qualifier'), Usage('N'), Position(20)]
    
    bpr21: Annotated[D_508, Title('Account Number'), Usage('N'), Position(21)]


class HEADER_TRN(Segment):
    """Reassociation Trace Number"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title('Trace Type Code'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title('Check or EFT Trace Number'), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title('Payer Identifier'), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title('Originating Company Supplemental Code'), Usage('S'), Position(4)]


class HEADER_CUR(Segment):
    """Foreign Currency Information"""
    _segment_name = 'CUR'
    
    cur01: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    cur02: Annotated[D_100, Title('Currency Code'), Usage('R'), Position(2)]
    
    cur03: Annotated[D_280, Title('Exchange Rate'), Usage('S'), Position(3)]
    
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


class HEADER_C040(Composite):
    """Reference Identifier"""
    pass


class HEADER_REF(Segment):
    """Receiver Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['EV'])]
    
    ref02: Annotated[D_127, Title('Receiver Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class HEADER_C040(Composite):
    """Reference Identifier"""
    pass


class HEADER_REF(Segment):
    """Version Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['F2'])]
    
    ref02: Annotated[D_127, Title('Version Identification Code'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class HEADER_DTM(Segment):
    """Production Date"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['405'])]
    
    dtm02: Annotated[D_373, Title('Production Date'), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]


class L1000A_N1(Segment):
    """Payer Identification"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    n102: Annotated[D_93, Title('Payer Name'), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(3), Enumerated(*['XV'])]
    
    n104: Annotated[D_67, Title('Payer Identifier'), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1000A_N3(Segment):
    """Payer Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Payer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Payer Address Line'), Usage('S'), Position(2)]


class L1000A_N4(Segment):
    """Payer City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Payer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Payer State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Payer Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('N'), Position(4)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L1000A_C040(Composite):
    """Reference Identifier"""
    pass


class L1000A_REF(Segment):
    """Additional Payer Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['2U', 'EO', 'HI', 'NF'])]
    
    ref02: Annotated[D_127, Title('Additional Payer Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L1000A_PER(Segment):
    """Payer Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['CX'])]
    
    per02: Annotated[D_93, Title('Payer Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EX'])]
    
    per08: Annotated[D_364, Title('Payer Contact Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L1000A(Loop):
    
    n1: Annotated[L1000A_N1, Title('Payer Identification'), Usage('R'), Position(80), Required(True)]
    
    n3: Annotated[L1000A_N3, Title('Payer Address'), Usage('R'), Position(100), Required(True)]
    
    n4: Annotated[L1000A_N4, Title('Payer City, State, ZIP Code'), Usage('R'), Position(110), Required(True)]
    ItemRef: TypeAlias = Annotated[L1000A_REF, Title('Additional Payer Identification'), Usage('S'), Position(120), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]
    
    per: Annotated[L1000A_PER, Title('Payer Contact Information'), Usage('S'), Position(130), Required(True)]


class L1000B_N1(Segment):
    """Payee Identification"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    n102: Annotated[D_93, Title('Payee Name'), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(3), Enumerated(*['FI', 'XX'])]
    
    n104: Annotated[D_67, Title('Payee Identification Code'), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1000B_N3(Segment):
    """Payee Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Payee Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Payee Address Line'), Usage('S'), Position(2)]


class L1000B_N4(Segment):
    """Payee City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Payee City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Payee State Code'), Usage('R'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Payee Postal Zone or ZIP Code'), Usage('R'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]


class L1000B_C040(Composite):
    """Reference Identifier"""
    pass


class L1000B_REF(Segment):
    """Payee Additional Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', 'D3', 'G2', 'N5', 'PQ', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Additional Payee Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L1000B(Loop):
    
    n1: Annotated[L1000B_N1, Title('Payee Identification'), Usage('R'), Position(80), Required(True)]
    
    n3: Annotated[L1000B_N3, Title('Payee Address'), Usage('S'), Position(100), Required(True)]
    
    n4: Annotated[L1000B_N4, Title('Payee City, State, ZIP Code'), Usage('S'), Position(110), Required(True)]
    ItemRef: TypeAlias = Annotated[L1000B_REF, Title('Payee Additional Identification'), Usage('S'), Position(120), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]


class HEADER(Loop):
    
    bpr: Annotated[HEADER_BPR, Title('Financial Information'), Usage('R'), Position(20), Required(True)]
    
    trn: Annotated[HEADER_TRN, Title('Reassociation Trace Number'), Usage('R'), Position(40), Required(True)]
    
    cur: Annotated[HEADER_CUR, Title('Foreign Currency Information'), Usage('S'), Position(50), Required(True)]
    
    ref: Annotated[HEADER_REF, Title('Receiver Identification'), Usage('S'), Position(60), Required(True)]
    
    ref: Annotated[HEADER_REF, Title('Version Identification'), Usage('S'), Position(60), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title('Production Date'), Usage('S'), Position(70), Required(True)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title('Payer Identification'), Usage('R'), Position(80), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title('Payee Identification'), Usage('R'), Position(80), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]


class L2000_LX(Segment):
    """Header Number"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]


class L2000_TS3(Segment):
    """Provider Summary Information"""
    _segment_name = 'TS3'
    
    ts301: Annotated[D_127, Title('Provider Identifier'), Usage('R'), Position(1)]
    
    ts302: Annotated[D_1331, Title('Facility Type Code'), Usage('R'), Position(2)]
    
    ts303: Annotated[D_373, Title('Fiscal Period Date'), Usage('R'), Position(3)]
    
    ts304: Annotated[D_380, Title('Total Claim Count'), Usage('R'), Position(4)]
    
    ts305: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(5)]
    
    ts306: Annotated[D_782, Title('Total Covered Charge Amount'), Usage('S'), Position(6)]
    
    ts307: Annotated[D_782, Title('Total Noncovered Charge Amount'), Usage('S'), Position(7)]
    
    ts308: Annotated[D_782, Title('Total Denied Charge Amount'), Usage('S'), Position(8)]
    
    ts309: Annotated[D_782, Title('Total Provider Payment Amount'), Usage('S'), Position(9)]
    
    ts310: Annotated[D_782, Title('Total Interest Amount'), Usage('S'), Position(10)]
    
    ts311: Annotated[D_782, Title('Total Contractual Adjustment Amount'), Usage('S'), Position(11)]
    
    ts312: Annotated[D_782, Title('Total Gramm-Rudman Reduction Amount'), Usage('S'), Position(12)]
    
    ts313: Annotated[D_782, Title('Total MSP Payer Amount'), Usage('S'), Position(13)]
    
    ts314: Annotated[D_782, Title('Total Blood Deductible Amount'), Usage('S'), Position(14)]
    
    ts315: Annotated[D_782, Title('Total Non-Lab Charge Amount'), Usage('S'), Position(15)]
    
    ts316: Annotated[D_782, Title('Total Coinsurance Amount'), Usage('S'), Position(16)]
    
    ts317: Annotated[D_782, Title('Total HCPCS Reported Charge Amount'), Usage('S'), Position(17)]
    
    ts318: Annotated[D_782, Title('Total HCPCS Payable Amount'), Usage('S'), Position(18)]
    
    ts319: Annotated[D_782, Title('Total Deductible Amount'), Usage('S'), Position(19)]
    
    ts320: Annotated[D_782, Title('Total Professional Component Amount'), Usage('S'), Position(20)]
    
    ts321: Annotated[D_782, Title('Total MSP Patient Liability Met Amount'), Usage('S'), Position(21)]
    
    ts322: Annotated[D_782, Title('Total Patient Reimbursement Amount'), Usage('S'), Position(22)]
    
    ts323: Annotated[D_380, Title('Total PIP Claim Count'), Usage('S'), Position(23)]
    
    ts324: Annotated[D_782, Title('Total PIP Adjustment Amount'), Usage('S'), Position(24)]


class L2000_TS2(Segment):
    """Provider Supplemental Summary Information"""
    _segment_name = 'TS2'
    
    ts201: Annotated[D_782, Title('Total DRG Amount'), Usage('S'), Position(1)]
    
    ts202: Annotated[D_782, Title('Total Federal Specific Amount'), Usage('S'), Position(2)]
    
    ts203: Annotated[D_782, Title('Total Hospital Specific Amount'), Usage('S'), Position(3)]
    
    ts204: Annotated[D_782, Title('Total Disproportionate Share Amount'), Usage('S'), Position(4)]
    
    ts205: Annotated[D_782, Title('Total Capital Amount'), Usage('S'), Position(5)]
    
    ts206: Annotated[D_782, Title('Total Indirect Medical Education Amount'), Usage('S'), Position(6)]
    
    ts207: Annotated[D_380, Title('Total Outlier Day Count'), Usage('S'), Position(7)]
    
    ts208: Annotated[D_782, Title('Total Day Outlier Amount'), Usage('S'), Position(8)]
    
    ts209: Annotated[D_782, Title('Total Cost Outlier Amount'), Usage('S'), Position(9)]
    
    ts210: Annotated[D_380, Title('Average DRG Length of Stay'), Usage('S'), Position(10)]
    
    ts211: Annotated[D_380, Title('Total Discharge Count'), Usage('S'), Position(11)]
    
    ts212: Annotated[D_380, Title('Total Cost Report Day Count'), Usage('S'), Position(12)]
    
    ts213: Annotated[D_380, Title('Total Covered Day Count'), Usage('S'), Position(13)]
    
    ts214: Annotated[D_380, Title('Total Noncovered Day Count'), Usage('S'), Position(14)]
    
    ts215: Annotated[D_782, Title('Total MSP Pass-Through Amount'), Usage('S'), Position(15)]
    
    ts216: Annotated[D_380, Title('Average DRG weight'), Usage('S'), Position(16)]
    
    ts217: Annotated[D_782, Title('Total PPS Capital FSP DRG Amount'), Usage('S'), Position(17)]
    
    ts218: Annotated[D_782, Title('Total PPS Capital HSP DRG Amount'), Usage('S'), Position(18)]
    
    ts219: Annotated[D_782, Title('Total PPS DSH DRG Amount'), Usage('S'), Position(19)]


class L2100_CLP(Segment):
    """Claim Payment Information"""
    _segment_name = 'CLP'
    
    clp01: Annotated[D_1028, Title('Patient Control Number'), Usage('R'), Position(1)]
    
    clp02: Annotated[D_1029, Title('Claim Status Code'), Usage('R'), Position(2), Enumerated(*claim_status)]
    
    clp03: Annotated[D_782, Title('Total Claim Charge Amount'), Usage('R'), Position(3)]
    
    clp04: Annotated[D_782, Title('Claim Payment Amount'), Usage('R'), Position(4)]
    
    clp05: Annotated[D_782, Title('Patient Responsibility Amount'), Usage('S'), Position(5)]
    
    clp06: Annotated[D_1032, Title('Claim Filing Indicator Code'), Usage('R'), Position(6), Enumerated(*['12', '13', '14', '15', '16', 'AM', 'CH', 'DS', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]
    
    clp07: Annotated[D_127, Title('Payer Claim Control Number'), Usage('S'), Position(7)]
    
    clp08: Annotated[D_1331, Title('Facility Type Code'), Usage('S'), Position(8)]
    
    clp09: Annotated[D_1325, Title('Claim Frequency Code'), Usage('S'), Position(9), Enumerated(*['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'X', 'Y', 'Z'])]
    
    clp10: Annotated[D_1352, Title('Patient Status Code'), Usage('N'), Position(10)]
    
    clp11: Annotated[D_1354, Title('Diagnosis Related Group (DRG) Code'), Usage('S'), Position(11)]
    
    clp12: Annotated[D_380, Title('Diagnosis Related Group (DRG) Weight'), Usage('S'), Position(12)]
    
    clp13: Annotated[D_954, Title('Discharge Fraction'), Usage('S'), Position(13)]


class L2100_CAS(Segment):
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


class L2100_NM1(Segment):
    """Patient Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Patient Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Patient First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Patient Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Patient Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['34', 'HN', 'II', 'MI', 'MR'])]
    
    nm109: Annotated[D_67, Title('Patient Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100_NM1(Segment):
    """Insured Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Subscriber Last Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Subscriber First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Subscriber Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Subscriber Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['34', 'HN', 'MI'])]
    
    nm109: Annotated[D_67, Title('Subscriber Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100_NM1(Segment):
    """Corrected Patient/Insured Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['74'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Corrected Patient or Insured Last Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Corrected Patient or Insured First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Corrected Patient or Insured Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Corrected Patient or Insured Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['C'])]
    
    nm109: Annotated[D_67, Title('Corrected Insured Identification Indicator'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100_NM1(Segment):
    """Service Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Rendering Provider Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Rendering Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Rendering Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Rendering Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['BD', 'BS', 'FI', 'MC', 'PC', 'SL', 'UP', 'XX'])]
    
    nm109: Annotated[D_67, Title('Rendering Provider Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100_NM1(Segment):
    """Crossover Carrier Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['TT'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Coordination of Benefits Carrier Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['AD', 'FI', 'NI', 'PI', 'PP', 'XV'])]
    
    nm109: Annotated[D_67, Title('Coordination of Benefits Carrier Identifier'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100_NM1(Segment):
    """Corrected Priority Payer Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Corrected Priority Payer Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(8), Enumerated(*['AD', 'FI', 'NI', 'PI', 'PP', 'XV'])]
    
    nm109: Annotated[D_67, Title('Corrected Priority Payer Identification Number'), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]


class L2100_MIA(Segment):
    """Inpatient Adjudication Information"""
    _segment_name = 'MIA'
    
    mia01: Annotated[D_380, Title('Covered Days or Visits Count'), Usage('R'), Position(1)]
    
    mia02: Annotated[D_380, Title('PPS Operating Outlier Amount'), Usage('S'), Position(2)]
    
    mia03: Annotated[D_380, Title('Lifetime Psychiatric Days Count'), Usage('S'), Position(3)]
    
    mia04: Annotated[D_782, Title('Claim DRG Amount'), Usage('S'), Position(4)]
    
    mia05: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(5), Enumerated(*remark_code)]
    
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
    
    mia20: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(20), Enumerated(*remark_code)]
    
    mia21: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(21), Enumerated(*remark_code)]
    
    mia22: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(22), Enumerated(*remark_code)]
    
    mia23: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(23), Enumerated(*remark_code)]
    
    mia24: Annotated[D_782, Title('PPS-Capital Exception Amount'), Usage('S'), Position(24)]


class L2100_MOA(Segment):
    """Outpatient Adjudication Information"""
    _segment_name = 'MOA'
    
    moa01: Annotated[D_954, Title('Reimbursement Rate'), Usage('S'), Position(1)]
    
    moa02: Annotated[D_782, Title('Claim HCPCS Payable Amount'), Usage('S'), Position(2)]
    
    moa03: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(3), Enumerated(*remark_code)]
    
    moa04: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(4), Enumerated(*remark_code)]
    
    moa05: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(5), Enumerated(*remark_code)]
    
    moa06: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(6), Enumerated(*remark_code)]
    
    moa07: Annotated[D_127, Title('Remark Code'), Usage('S'), Position(7), Enumerated(*remark_code)]
    
    moa08: Annotated[D_782, Title('Claim ESRD Payment Amount'), Usage('S'), Position(8)]
    
    moa09: Annotated[D_782, Title('Nonpayable Professional Component Amount'), Usage('S'), Position(9)]


class L2100_C040(Composite):
    """Reference Identifier"""
    pass


class L2100_REF(Segment):
    """Other Claim Related Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1L', '1W', '9A', '9C', 'A6', 'BB', 'CE', 'EA', 'F8', 'G1', 'G3', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title('Other Claim Related Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2100_C040(Composite):
    """Reference Identifier"""
    pass


class L2100_REF(Segment):
    """Rendering Provider Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', 'D3', 'G2'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Secondary Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2100_DTM(Segment):
    """Claim Date"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['036', '050', '232', '233'])]
    
    dtm02: Annotated[D_373, Title('Claim Date'), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]


class L2100_PER(Segment):
    """Claim Contact Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['CX'])]
    
    per02: Annotated[D_93, Title('Claim Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Claim Contact Communications Number'), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Claim Contact Communications Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EX'])]
    
    per08: Annotated[D_364, Title('Communication Number Extension'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100_AMT(Segment):
    """Claim Supplemental Information"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['I', 'T', 'AU', 'D8', 'DY', 'F5', 'NL', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO', 'ZZ'])]
    
    amt02: Annotated[D_782, Title('Claim Supplemental Information Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2100_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2100_QTY(Segment):
    """Claim Supplemental Information Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['CA', 'CD', 'LA', 'LE', 'NA', 'NE', 'NR', 'OU', 'PS', 'VS', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO'])]
    
    qty02: Annotated[D_380, Title('Claim Supplemental Information Quantity'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-Form Message'), Usage('N'), Position(4)]


class L2110_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svc01_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'ER', 'HC', 'ID', 'IV', 'N4', 'NU', 'RB', 'ZZ'])]
    
    svc01_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svc01_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svc01_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svc01_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svc01_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svc01_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]


class L2110_C003(Composite):
    """Composite Medical Procedure Identifier"""
    
    svc06_01: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('R'), Position(1), Enumerated(*['AD', 'ER', 'HC', 'ID', 'IV', 'N4', 'NU', 'RB', 'ZZ'])]
    
    svc06_02: Annotated[D_234, Title('Procedure Code'), Usage('R'), Position(2)]
    
    svc06_03: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(3)]
    
    svc06_04: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(4)]
    
    svc06_05: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(5)]
    
    svc06_06: Annotated[D_1339, Title('Procedure Modifier'), Usage('S'), Position(6)]
    
    svc06_07: Annotated[D_352, Title('Procedure Code Description'), Usage('S'), Position(7)]


class L2110_SVC(Segment):
    """Service Payment Information"""
    _segment_name = 'SVC'
    
    c003: Annotated[L2110_C003, Title('Composite Medical Procedure Identifier'), Usage('R'), Position(1), Required(True)]
    
    svc02: Annotated[D_782, Title('Line Item Charge Amount'), Usage('R'), Position(2)]
    
    svc03: Annotated[D_782, Title('Line Item Provider Payment Amount'), Usage('R'), Position(3)]
    
    svc04: Annotated[D_234, Title('National Uniform Billing Committee Revenue Code'), Usage('S'), Position(4)]
    
    svc05: Annotated[D_380, Title('Units of Service Paid Count'), Usage('S'), Position(5)]
    
    c003: Annotated[L2110_C003, Title('Composite Medical Procedure Identifier'), Usage('S'), Position(6), Required(True)]
    
    svc07: Annotated[D_380, Title('Original Units of Service Count'), Usage('S'), Position(7)]


class L2110_DTM(Segment):
    """Service Date"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['150', '151', '472'])]
    
    dtm02: Annotated[D_373, Title('Service Date'), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title('Time'), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title('Time Code'), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title('Date Time Period'), Usage('N'), Position(6)]


class L2110_CAS(Segment):
    """Service Adjustment"""
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


class L2110_C040(Composite):
    """Reference Identifier"""
    pass


class L2110_REF(Segment):
    """Service Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1S', '6R', 'BB', 'E9', 'G1', 'G3', 'LU', 'RB'])]
    
    ref02: Annotated[D_127, Title('Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2110_C040(Composite):
    """Reference Identifier"""
    pass


class L2110_REF(Segment):
    """Rendering Provider Information"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1A', '1B', '1C', '1D', '1G', '1H', '1J', 'HPI', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title('Rendering Provider Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2110_AMT(Segment):
    """Service Supplemental Amount"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B6', 'DY', 'KH', 'NE', 'T', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO'])]
    
    amt02: Annotated[D_782, Title('Service Supplemental Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2110_C001(Composite):
    """Composite Unit of Measure"""
    pass


class L2110_QTY(Segment):
    """Service Supplemental Quantity"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['NE', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO'])]
    
    qty02: Annotated[D_380, Title('Service Supplemental Quantity Count'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-Form Message'), Usage('N'), Position(4)]


class L2110_LQ(Segment):
    """Health Care Remark Codes"""
    _segment_name = 'LQ'
    
    lq01: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('R'), Position(1), Enumerated(*['HE', 'RX'])]
    
    lq02: Annotated[D_1271, Title('Remark Code'), Usage('R'), Position(2)]


class L2110(Loop):
    
    svc: Annotated[L2110_SVC, Title('Service Payment Information'), Usage('R'), Position(70), Required(True)]
    ItemDtm: TypeAlias = Annotated[L2110_DTM, Title('Service Date'), Usage('S'), Position(80), Required(True)]
    dtm: Annotated[list[ItemDtm], MaxItems(3)]
    ItemCas: TypeAlias = Annotated[L2110_CAS, Title('Service Adjustment'), Usage('S'), Position(90), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    ItemRef: TypeAlias = Annotated[L2110_REF, Title('Service Identification'), Usage('S'), Position(100), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(7)]
    ItemRef: TypeAlias = Annotated[L2110_REF, Title('Rendering Provider Information'), Usage('S'), Position(100), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(10)]
    ItemAmt: TypeAlias = Annotated[L2110_AMT, Title('Service Supplemental Amount'), Usage('S'), Position(110), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(12)]
    ItemQty: TypeAlias = Annotated[L2110_QTY, Title('Service Supplemental Quantity'), Usage('S'), Position(120), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(6)]
    ItemLq: TypeAlias = Annotated[L2110_LQ, Title('Health Care Remark Codes'), Usage('S'), Position(130), Required(True)]
    lq: Annotated[list[ItemLq], MaxItems(99)]


class L2100(Loop):
    
    clp: Annotated[L2100_CLP, Title('Claim Payment Information'), Usage('R'), Position(10), Required(True)]
    ItemCas: TypeAlias = Annotated[L2100_CAS, Title('Claim Adjustment'), Usage('S'), Position(20), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    
    nm1: Annotated[L2100_NM1, Title('Patient Name'), Usage('R'), Position(30), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title('Insured Name'), Usage('S'), Position(30), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title('Corrected Patient/Insured Name'), Usage('S'), Position(30), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title('Service Provider Name'), Usage('S'), Position(30), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title('Crossover Carrier Name'), Usage('S'), Position(30), Required(True)]
    ItemNm1: TypeAlias = Annotated[L2100_NM1, Title('Corrected Priority Payer Name'), Usage('S'), Position(30), Required(True)]
    nm1: Annotated[list[ItemNm1], MaxItems(2)]
    
    mia: Annotated[L2100_MIA, Title('Inpatient Adjudication Information'), Usage('S'), Position(33), Required(True)]
    
    moa: Annotated[L2100_MOA, Title('Outpatient Adjudication Information'), Usage('S'), Position(35)]
    ItemRef: TypeAlias = Annotated[L2100_REF, Title('Other Claim Related Identification'), Usage('S'), Position(40), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    ItemRef: TypeAlias = Annotated[L2100_REF, Title('Rendering Provider Identification'), Usage('S'), Position(40), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(10)]
    ItemDtm: TypeAlias = Annotated[L2100_DTM, Title('Claim Date'), Usage('S'), Position(50), Required(True)]
    dtm: Annotated[list[ItemDtm], MaxItems(4)]
    ItemPer: TypeAlias = Annotated[L2100_PER, Title('Claim Contact Information'), Usage('S'), Position(60), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(3)]
    ItemAmt: TypeAlias = Annotated[L2100_AMT, Title('Claim Supplemental Information'), Usage('S'), Position(62), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(14)]
    ItemQty: TypeAlias = Annotated[L2100_QTY, Title('Claim Supplemental Information Quantity'), Usage('S'), Position(64), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(15)]
    ItemL2110: TypeAlias = Annotated[L2110, Title('Service Payment Information'), Usage('S'), Position(70), Required(True)]
    l2110: Annotated[list[ItemL2110], MinItems(999)]


class L2000(Loop):
    
    lx: Annotated[L2000_LX, Title('Header Number'), Usage('R'), Position(3), Required(True)]
    
    ts3: Annotated[L2000_TS3, Title('Provider Summary Information'), Usage('S'), Position(5), Required(True)]
    
    ts2: Annotated[L2000_TS2, Title('Provider Supplemental Summary Information'), Usage('S'), Position(7)]
    ItemL2100: TypeAlias = Annotated[L2100, Title('Claim Payment Information'), Usage('R'), Position(10), Required(True)]
    l2100: Annotated[list[ItemL2100], MinItems(1)]


class DETAIL(Loop):
    ItemL2000: TypeAlias = Annotated[L2000, Title('Header Number'), Usage('S'), Position(3), Required(True)]
    l2000: Annotated[list[ItemL2000], MinItems(1)]


class FOOTER_C042(Composite):
    """Adjustment Identifier"""
    
    plb03_01: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(1)]
    
    plb03_02: Annotated[D_127, Title('Provider Adjustment Identifier'), Usage('S'), Position(2)]


class FOOTER_C042(Composite):
    """Adjustment Identifier"""
    
    plb05_01: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(1)]
    
    plb05_02: Annotated[D_127, Title('Provider Adjustment Identifier'), Usage('S'), Position(2)]


class FOOTER_C042(Composite):
    """Adjustment Identifier"""
    
    plb07_01: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(1)]
    
    plb07_02: Annotated[D_127, Title('Provider Adjustment Identifier'), Usage('S'), Position(2)]


class FOOTER_C042(Composite):
    """Adjustment Identifier"""
    
    plb09_01: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(1)]
    
    plb09_02: Annotated[D_127, Title('Provider Adjustment Identifier'), Usage('S'), Position(2)]


class FOOTER_C042(Composite):
    """Adjustment Identifier"""
    
    plb11_01: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(1)]
    
    plb11_02: Annotated[D_127, Title('Provider Adjustment Identifier'), Usage('S'), Position(2)]


class FOOTER_C042(Composite):
    """Adjustment Identifier"""
    
    plb13_01: Annotated[D_426, Title('Adjustment Reason Code'), Usage('R'), Position(1)]
    
    plb13_02: Annotated[D_127, Title('Provider Adjustment Identifier'), Usage('S'), Position(2)]


class FOOTER_PLB(Segment):
    """Provider Adjustment"""
    _segment_name = 'PLB'
    
    plb01: Annotated[D_127, Title('Provider Identifier'), Usage('R'), Position(1)]
    
    plb02: Annotated[D_373, Title('Fiscal Period Date'), Usage('R'), Position(2)]
    
    c042: Annotated[FOOTER_C042, Title('Adjustment Identifier'), Usage('R'), Position(3), Required(True)]
    
    plb04: Annotated[D_782, Title('Provider Adjustment Amount'), Usage('R'), Position(4)]
    
    c042: Annotated[FOOTER_C042, Title('Adjustment Identifier'), Usage('S'), Position(5), Required(True)]
    
    plb06: Annotated[D_782, Title('Provider Adjustment Amount'), Usage('S'), Position(6)]
    
    c042: Annotated[FOOTER_C042, Title('Adjustment Identifier'), Usage('S'), Position(7), Required(True)]
    
    plb08: Annotated[D_782, Title('Provider Adjustment Amount'), Usage('S'), Position(8)]
    
    c042: Annotated[FOOTER_C042, Title('Adjustment Identifier'), Usage('S'), Position(9), Required(True)]
    
    plb10: Annotated[D_782, Title('Provider Adjustment Amount'), Usage('S'), Position(10)]
    
    c042: Annotated[FOOTER_C042, Title('Adjustment Identifier'), Usage('S'), Position(11), Required(True)]
    
    plb12: Annotated[D_782, Title('Provider Adjustment Amount'), Usage('S'), Position(12)]
    
    c042: Annotated[FOOTER_C042, Title('Adjustment Identifier'), Usage('S'), Position(13), Required(True)]
    
    plb14: Annotated[D_782, Title('Provider Adjustment Amount'), Usage('S'), Position(14)]


class FOOTER(Loop):
    ItemPlb: TypeAlias = Annotated[FOOTER_PLB, Title('Provider Adjustment'), Usage('S'), Position(10), Required(True)]
    plb: Annotated[list[ItemPlb], MinItems(1)]


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(10), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Table 1 - Header'), Usage('R'), Position(15), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('S'), Position(20)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('S'), Position(30)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(50), Required(True)]


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


class MSG835(Message):
    """HIPAA Health Care Claim Payment/Advice X091-835"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
