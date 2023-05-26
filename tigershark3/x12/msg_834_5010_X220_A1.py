"""
834.5010.X220.A1
Created 2023-05-19 10:17:35.979891
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
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['005010X220A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['834'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title('Implementation Convention Reference'), Usage('R'), Position(3), Enumerated(*['005010X220A1'])]


class HEADER_BGN(Segment):
    """Beginning Segment"""
    _segment_name = 'BGN'
    
    bgn01: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('R'), Position(1), Enumerated(*['00', '15', '22'])]
    
    bgn02: Annotated[D_127, Title('Transaction Set Reference Number'), Usage('R'), Position(2)]
    
    bgn03: Annotated[D_373, Title('Transaction Set Creation Date'), Usage('R'), Position(3)]
    
    bgn04: Annotated[D_337, Title('Transaction Set Creation Time'), Usage('R'), Position(4)]
    
    bgn05: Annotated[D_623, Title('Time Zone Code'), Usage('S'), Position(5), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', 'AD', 'AS', 'AT', 'CD', 'CS', 'CT', 'ED', 'ES', 'ET', 'GM', 'HD', 'HS', 'HT', 'LT', 'MD', 'MS', 'MT', 'ND', 'NS', 'NT', 'PD', 'PS', 'PT', 'TD', 'TS', 'TT', 'UT'])]
    
    bgn06: Annotated[D_127, Title('Original Transaction Set Reference Number'), Usage('S'), Position(6)]
    
    bgn07: Annotated[D_640, Title('Transaction Type Code'), Usage('N'), Position(7)]
    
    bgn08: Annotated[D_306, Title('Action Code'), Usage('R'), Position(8), Enumerated(*['2', '4', 'RX'])]
    
    bgn09: Annotated[D_786, Title('Security Level Code'), Usage('N'), Position(9)]


class HEADER_REF04(Composite):
    """Reference Identifier"""
    pass


class HEADER_REF(Segment):
    """Transaction Set Policy Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['38'])]
    
    ref02: Annotated[D_127, Title('Master Policy Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class HEADER_DTP(Segment):
    """File Effective Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['007', '090', '091', '303', '382', '388'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Date Time Period'), Usage('R'), Position(3)]


class HEADER_QTY03(Composite):
    """Composite Unit of Measure"""
    pass


class HEADER_QTY(Segment):
    """Transaction Set Control Totals"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['DT', 'ET', 'TO'])]
    
    qty02: Annotated[D_380, Title('Record Totals'), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title('Free-form Information'), Usage('N'), Position(4)]


class L1000A_N1(Segment):
    """Sponsor Name"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['P5'])]
    
    n102: Annotated[D_93, Title('Plan Sponsor Name'), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(3), Enumerated(*['24', '94', 'FI'])]
    
    n104: Annotated[D_67, Title('Sponsor Identifier'), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1000A(Loop):
    
    n1: Annotated[L1000A_N1, Title('Sponsor Name'), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]


class L1000B_N1(Segment):
    """Payer"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['IN'])]
    
    n102: Annotated[D_93, Title('Insurer Name'), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(3), Enumerated(*['94', 'FI', 'XV'])]
    
    n104: Annotated[D_67, Title('Insurer Identification Code'), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1000B(Loop):
    
    n1: Annotated[L1000B_N1, Title('Payer'), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]


class L1000C_N1(Segment):
    """TPA/Broker Name"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['BO', 'TV'])]
    
    n102: Annotated[D_93, Title('TPA or Broker Name'), Usage('R'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('R'), Position(3), Enumerated(*['94', 'FI', 'XV'])]
    
    n104: Annotated[D_67, Title('TPA or Broker Identification Code'), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1100C_ACT(Segment):
    """TPA/Broker Account Information"""
    _segment_name = 'ACT'
    
    act01: Annotated[D_508, Title('TPA or Broker Account Number'), Usage('R'), Position(1)]
    
    act02: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]
    
    act03: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(3)]
    
    act04: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(4)]
    
    act05: Annotated[D_569, Title('Account Number Qualifier'), Usage('N'), Position(5)]
    
    act06: Annotated[D_508, Title('TPA or Broker Account Number'), Usage('S'), Position(6)]
    
    act07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]
    
    act08: Annotated[D_107, Title('Payment Method Type Code'), Usage('N'), Position(8)]
    
    act09: Annotated[D_1216, Title('Benefit Status Code'), Usage('N'), Position(9)]


class L1100C(Loop):
    
    act: Annotated[L1100C_ACT, Title('TPA/Broker Account Information'), Usage('R'), Position(1200), Syntax(['P0304', 'C0506', 'C0705']), Required(True)]


class L1000C(Loop):
    
    n1: Annotated[L1000C_N1, Title('TPA/Broker Name'), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    ItemL1100C: TypeAlias = Annotated[L1100C, Title('TPA/Broker Account Information'), Usage('S'), Position(3600), Required(True)]
    l1100c: Annotated[list[ItemL1100C], MinItems(1)]


class HEADER(Loop):
    
    bgn: Annotated[HEADER_BGN, Title('Beginning Segment'), Usage('R'), Position(200), Syntax(['C0504']), Required(True)]
    
    ref: Annotated[HEADER_REF, Title('Transaction Set Policy Number'), Usage('S'), Position(300), Syntax(['R0203']), Required(True)]
    ItemDtp: TypeAlias = Annotated[HEADER_DTP, Title('File Effective Date'), Usage('S'), Position(400), Required(True)]
    dtp: Annotated[list[ItemDtp], MinItems(1)]
    ItemQty: TypeAlias = Annotated[HEADER_QTY, Title('Transaction Set Control Totals'), Usage('S'), Position(600), Syntax(['E0204', 'R0204']), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(3)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title('Sponsor Name'), Usage('R'), Position(700), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title('Payer'), Usage('R'), Position(1900), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]
    ItemL1000C: TypeAlias = Annotated[L1000C, Title('TPA/Broker Name'), Usage('S'), Position(3100), Required(True)]
    l1000c: Annotated[list[ItemL1000C], MinItems(2)]


class L2000_INS06(Composite):
    """Medicare Status Code"""
    
    ins06_01: Annotated[D_1218, Title('Medicare Plan Code'), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    ins06_02: Annotated[D_1701, Title('Medicare Eligibility Reason Code'), Usage('S'), Position(2), Enumerated(*['0', '1', '2'])]
    
    ins06_03: Annotated[D_1701, Title('Eligibility Reason Code'), Usage('N'), Position(3)]
    
    ins06_04: Annotated[D_1701, Title('Eligibility Reason Code'), Usage('N'), Position(4)]


class L2000_INS(Segment):
    """Member Level Detail"""
    _segment_name = 'INS'
    
    ins01: Annotated[D_1073, Title('Member Indicator'), Usage('R'), Position(1), Enumerated(*['N', 'Y'])]
    
    ins02: Annotated[D_1069, Title('Individual Relationship Code'), Usage('R'), Position(2), Enumerated(*['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26', '31', '38', '53', '60', 'D2', 'G8', 'G9'])]
    
    ins03: Annotated[D_875, Title('Maintenance Type Code'), Usage('R'), Position(3), Enumerated(*['001', '021', '024', '025', '030'])]
    
    ins04: Annotated[D_1203, Title('Maintenance Reason Code'), Usage('S'), Position(4), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '14', '15', '16', '17', '18', '20', '21', '22', '25', '26', '27', '28', '29', '31', '32', '33', '37', '38', '39', '40', '41', '43', '59', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AL', 'EC', 'XN', 'XT'])]
    
    ins05: Annotated[D_1216, Title('Benefit Status Code'), Usage('R'), Position(5), Enumerated(*['A', 'C', 'S', 'T'])]
    
    ins06: Annotated[L2000_INS06, Title('Medicare Status Code'), Usage('S'), Position(6), Required(True)]
    
    ins07: Annotated[D_1219, Title('Consolidated Omnibus Budget Reconciliation Act (COBRA) Qualifying Event Code'), Usage('S'), Position(7), Enumerated(*['1', '10', '2', '3', '4', '5', '6', '7', '8', '9', 'ZZ'])]
    
    ins08: Annotated[D_584, Title('Employment Status Code'), Usage('S'), Position(8), Enumerated(*['AC', 'AO', 'AU', 'FT', 'L1', 'PT', 'RT', 'TE'])]
    
    ins09: Annotated[D_1220, Title('Student Status Code'), Usage('S'), Position(9), Enumerated(*['F', 'N', 'P'])]
    
    ins10: Annotated[D_1073, Title('Handicap Indicator'), Usage('S'), Position(10), Enumerated(*['N', 'Y'])]
    
    ins11: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(11), Enumerated(*['D8'])]
    
    ins12: Annotated[D_1251, Title('Member Individual Death Date'), Usage('S'), Position(12)]
    
    ins13: Annotated[D_1165, Title('Confidentiality Code'), Usage('S'), Position(13), Enumerated(*['R', 'U'])]
    
    ins14: Annotated[D_19, Title('City Name'), Usage('N'), Position(14)]
    
    ins15: Annotated[D_156, Title('State or Province Code'), Usage('N'), Position(15)]
    
    ins16: Annotated[D_26, Title('Country Code'), Usage('N'), Position(16)]
    
    ins17: Annotated[D_1470, Title('Birth Sequence Number'), Usage('S'), Position(17)]


class L2000_REF04(Composite):
    """Reference Identifier"""
    pass


class L2000_REF(Segment):
    """Subscriber Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['0F'])]
    
    ref02: Annotated[D_127, Title('Subscriber Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2000_REF04(Composite):
    """Reference Identifier"""
    pass


class L2000_REF(Segment):
    """Member Policy Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['1L'])]
    
    ref02: Annotated[D_127, Title('Member Group or Policy Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2000_REF04(Composite):
    """Reference Identifier"""
    pass


class L2000_REF(Segment):
    """Member Supplemental Identifier"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['17', '23', '3H', '4A', '6O', 'ABB', 'D3', 'DX', 'F6', 'P5', 'Q4', 'QQ', 'ZZ'])]
    
    ref02: Annotated[D_127, Title('Member Supplemental Identifier'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2000_DTP(Segment):
    """Member Level Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['050', '286', '296', '297', '300', '301', '303', '336', '337', '338', '339', '340', '341', '350', '351', '356', '357', '383', '385', '386', '393', '394', '473', '474'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Status Information Effective Date'), Usage('R'), Position(3)]


class L2100A_NM1(Segment):
    """Member Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['74', 'IL'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Member Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Member First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Member Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Member Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Member Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Member Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100A_PER(Segment):
    """Member Communications Numbers"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IP'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100A_N3(Segment):
    """Member Residence Street Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Member Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Member Address Line'), Usage('S'), Position(2)]


class L2100A_N4(Segment):
    """Member City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Member City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Member State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Member Postal Zone or Zip Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('S'), Position(5), Enumerated(*['60', 'CY'])]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('S'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2100A_DMG05(Composite):
    """Composite Race or Ethnicity Information"""
    
    dmg05_01: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('S'), Position(1), Enumerated(*['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'N', 'O', 'P', 'Z'])]
    
    dmg05_02: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(2), Enumerated(*['RET'])]
    
    dmg05_03: Annotated[D_1271, Title('Race or Ethnicity Code'), Usage('S'), Position(3)]


class L2100A_DMG(Segment):
    """Member Demographics"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Member Birth Date'), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Gender Code'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('S'), Position(4), Enumerated(*['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X'])]
    ItemDmg05: TypeAlias = Annotated[L2100A_DMG05, Title('Composite Race or Ethnicity Information'), Usage('S'), Position(5)]
    dmg05: Annotated[list[ItemDmg05], MaxItems(10)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('S'), Position(6), Enumerated(*['1', '2', '3', '4', '5', '6', '7'])]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(10), Enumerated(*['REC'])]
    
    dmg11: Annotated[D_1271, Title('Race or Ethnicity Collection Code'), Usage('S'), Position(11)]


class L2100A_EC(Segment):
    """Employment Class"""
    _segment_name = 'EC'
    
    ec01: Annotated[D_1176, Title('Employment Class Code'), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23'])]
    
    ec02: Annotated[D_1176, Title('Employment Class Code'), Usage('S'), Position(2), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23'])]
    
    ec03: Annotated[D_1176, Title('Employment Class Code'), Usage('S'), Position(3), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23'])]
    
    ec04: Annotated[D_954, Title('Percentage as Decimal'), Usage('N'), Position(4)]
    
    ec05: Annotated[D_1201, Title('Information Status Code'), Usage('N'), Position(5)]
    
    ec06: Annotated[D_1149, Title('Occupation Code'), Usage('N'), Position(6)]


class L2100A_ICM(Segment):
    """Member Income"""
    _segment_name = 'ICM'
    
    icm01: Annotated[D_594, Title('Frequency Code'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '6', '7', '8', '9', 'B', 'C', 'H', 'Q', 'S', 'U'])]
    
    icm02: Annotated[D_782, Title('Wage Amount'), Usage('R'), Position(2)]
    
    icm03: Annotated[D_380, Title('Work Hours Count'), Usage('S'), Position(3)]
    
    icm04: Annotated[D_310, Title('Location Identification Code'), Usage('S'), Position(4)]
    
    icm05: Annotated[D_1214, Title('Salary Grade Code'), Usage('S'), Position(5)]
    
    icm06: Annotated[D_100, Title('Currency Code'), Usage('N'), Position(6)]


class L2100A_AMT(Segment):
    """Member Policy Amounts"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R'])]
    
    amt02: Annotated[D_782, Title('Contract Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2100A_HLH(Segment):
    """Member Health Information"""
    _segment_name = 'HLH'
    
    hlh01: Annotated[D_1212, Title('Health Related Code'), Usage('R'), Position(1), Enumerated(*['N', 'S', 'T', 'U', 'X'])]
    
    hlh02: Annotated[D_65, Title('Member Height'), Usage('S'), Position(2)]
    
    hlh03: Annotated[D_81, Title('Member Weight'), Usage('S'), Position(3)]
    
    hlh04: Annotated[D_81, Title('Weight'), Usage('N'), Position(4)]
    
    hlh05: Annotated[D_352, Title('Description'), Usage('N'), Position(5)]
    
    hlh06: Annotated[D_1213, Title('Current Health Condition Code'), Usage('N'), Position(6)]
    
    hlh07: Annotated[D_352, Title('Description'), Usage('N'), Position(7)]


class L2100A_LUI(Segment):
    """Member Language"""
    _segment_name = 'LUI'
    
    lui01: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(1), Enumerated(*['LD', 'LE'])]
    
    lui02: Annotated[D_67, Title('Language Code'), Usage('S'), Position(2)]
    
    lui03: Annotated[D_352, Title('Language Description'), Usage('S'), Position(3)]
    
    lui04: Annotated[D_1303, Title('Language Use Indicator'), Usage('S'), Position(4), Enumerated(*['5', '6', '7', '8'])]
    
    lui05: Annotated[D_1476, Title('Language Proficiency Indicator'), Usage('N'), Position(5)]


class L2100A(Loop):
    
    nm1: Annotated[L2100A_NM1, Title('Member Name'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100A_PER, Title('Member Communications Numbers'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100A_N3, Title('Member Residence Street Address'), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100A_N4, Title('Member City, State, ZIP Code'), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dmg: Annotated[L2100A_DMG, Title('Member Demographics'), Usage('S'), Position(800), Syntax(['P0102', 'P1011', 'C1105']), Required(True)]
    ItemEc: TypeAlias = Annotated[L2100A_EC, Title('Employment Class'), Usage('S'), Position(1000), Required(True)]
    ec: Annotated[list[ItemEc], MinItems(1)]
    
    icm: Annotated[L2100A_ICM, Title('Member Income'), Usage('S'), Position(1100), Required(True)]
    ItemAmt: TypeAlias = Annotated[L2100A_AMT, Title('Member Policy Amounts'), Usage('S'), Position(1200), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(7)]
    
    hlh: Annotated[L2100A_HLH, Title('Member Health Information'), Usage('S'), Position(1300), Required(True)]
    ItemLui: TypeAlias = Annotated[L2100A_LUI, Title('Member Language'), Usage('S'), Position(1500), Syntax(['P0102', 'L040203'])]
    lui: Annotated[list[ItemLui], MinItems(1)]


class L2100B_NM1(Segment):
    """Incorrect Member Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['70'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Prior Incorrect Member Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Prior Incorrect Member First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Prior Incorrect Member Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Prior Incorrect Member Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Prior Incorrect Member Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Prior Incorrect Insured Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100B_DMG05(Composite):
    """Composite Race or Ethnicity Information"""
    
    dmg05_01: Annotated[D_1109, Title('Race or Ethnicity Code'), Usage('S'), Position(1), Enumerated(*['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'N', 'O', 'P', 'Z'])]
    
    dmg05_02: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(2), Enumerated(*['RET'])]
    
    dmg05_03: Annotated[D_1271, Title('Race or Ethnicity Code'), Usage('S'), Position(3)]


class L2100B_DMG(Segment):
    """Incorrect Member Demographics"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('S'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title('Prior Incorrect Insured Birth Date'), Usage('S'), Position(2)]
    
    dmg03: Annotated[D_1068, Title('Prior Incorrect Insured Gender Code'), Usage('S'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title('Marital Status Code'), Usage('S'), Position(4), Enumerated(*['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X'])]
    ItemDmg05: TypeAlias = Annotated[L2100B_DMG05, Title('Composite Race or Ethnicity Information'), Usage('S'), Position(5)]
    dmg05: Annotated[list[ItemDmg05], MaxItems(10)]
    
    dmg06: Annotated[D_1066, Title('Citizenship Status Code'), Usage('S'), Position(6), Enumerated(*['1', '2', '3', '4', '5', '6', '7'])]
    
    dmg07: Annotated[D_26, Title('Country Code'), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title('Basis of Verification Code'), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title('Quantity'), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title('Code List Qualifier Code'), Usage('S'), Position(10), Enumerated(*['REC'])]
    
    dmg11: Annotated[D_1271, Title('Race or Ethnicity Collection Code'), Usage('S'), Position(11)]


class L2100B(Loop):
    
    nm1: Annotated[L2100B_NM1, Title('Incorrect Member Name'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    dmg: Annotated[L2100B_DMG, Title('Incorrect Member Demographics'), Usage('S'), Position(800), Syntax(['P0102', 'P1011', 'C1105'])]


class L2100C_NM1(Segment):
    """Member Mailing Address"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['31'])]
    
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


class L2100C_N3(Segment):
    """Member Mail Street Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Member Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Member Address Line'), Usage('S'), Position(2)]


class L2100C_N4(Segment):
    """Member Mail City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Member Mail City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Member Mail State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Member Mail Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2100C(Loop):
    
    nm1: Annotated[L2100C_NM1, Title('Member Mailing Address'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2100C_N3, Title('Member Mail Street Address'), Usage('R'), Position(500), Required(True)]
    
    n4: Annotated[L2100C_N4, Title('Member Mail City, State, ZIP Code'), Usage('R'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100D_NM1(Segment):
    """Member Employer"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['36'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Member Employer Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Member Employer First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Member Employer Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Member Employer Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Member Employer Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['24', '34'])]
    
    nm109: Annotated[D_67, Title('Member Employer Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100D_PER(Segment):
    """Member Employer Communications Numbers"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['EP'])]
    
    per02: Annotated[D_93, Title('Member Employer Communications Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100D_N3(Segment):
    """Member Employer Street Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Member Employer Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Member Employer Address Line'), Usage('S'), Position(2)]


class L2100D_N4(Segment):
    """Member Employer City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Member Employer City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Member Employer State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Member Employer Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2100D(Loop):
    
    nm1: Annotated[L2100D_NM1, Title('Member Employer'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100D_PER, Title('Member Employer Communications Numbers'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100D_N3, Title('Member Employer Street Address'), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100D_N4, Title('Member Employer City, State, ZIP Code'), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100E_NM1(Segment):
    """Member School"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['M8'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('School Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100E_PER(Segment):
    """Member School Commmunications Numbers"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['SK'])]
    
    per02: Annotated[D_93, Title('Member School Communications Contact Name'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100E_N3(Segment):
    """Member School Street Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('School Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('School Address Line'), Usage('S'), Position(2)]


class L2100E_N4(Segment):
    """Member School City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Member School City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Member School State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Member School Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2100E(Loop):
    
    nm1: Annotated[L2100E_NM1, Title('Member School'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100E_PER, Title('Member School Commmunications Numbers'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100E_N3, Title('Member School Street Address'), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100E_N4, Title('Member School City, State, ZIP Code'), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100F_NM1(Segment):
    """Custodial Parent"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['S3'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Custodial Parent Last Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Custodial Parent First Name'), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Custodial Parent Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Custodial Parent Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Custodial Parent Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Custodial Parent Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100F_PER(Segment):
    """Custodial Parent Communications Numbers"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['PQ'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100F_N3(Segment):
    """Custodial Parent Street Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Custodial Parent Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Custodial Parent Address Line'), Usage('S'), Position(2)]


class L2100F_N4(Segment):
    """Custodial Parent City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Custodial Parent City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Custodial Parent State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Custodial Parent Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2100F(Loop):
    
    nm1: Annotated[L2100F_NM1, Title('Custodial Parent'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100F_PER, Title('Custodial Parent Communications Numbers'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100F_N3, Title('Custodial Parent Street Address'), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100F_N4, Title('Custodial Parent City, State, ZIP Code'), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100G_NM1(Segment):
    """Responsible Person"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['6Y', '9K', 'E1', 'EI', 'EXS', 'GB', 'GD', 'J6', 'LR', 'QD', 'S1', 'TZ', 'X4'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Responsible Party Last or Organization Name'), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Responsible Party First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Responsible Party Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Responsible Party Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Responsible Party Suffix Name'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title('Responsible Party Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100G_PER(Segment):
    """Responsible Person Communications Numbers"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['RP'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2100G_N3(Segment):
    """Responsible Person Street Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Responsible Party Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Responsible Party Address Line'), Usage('S'), Position(2)]


class L2100G_N4(Segment):
    """Responsible Person City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Responsible Person City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Responsible Person State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Responsible Person Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2100G(Loop):
    
    nm1: Annotated[L2100G_NM1, Title('Responsible Person'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100G_PER, Title('Responsible Person Communications Numbers'), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100G_N3, Title('Responsible Person Street Address'), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100G_N4, Title('Responsible Person City, State, ZIP Code'), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100H_NM1(Segment):
    """Drop Off Location"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['45'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2100H_N3(Segment):
    """Drop Off Location Street Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Drop Off Location Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Drop Off Location Address Line'), Usage('S'), Position(2)]


class L2100H_N4(Segment):
    """Drop Off Location City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Drop Off Location City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Drop Off Location State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Drop Off Location Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2100H(Loop):
    
    nm1: Annotated[L2100H_NM1, Title('Drop Off Location'), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2100H_N3, Title('Drop Off Location Street Address'), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100H_N4, Title('Drop Off Location City, State, ZIP Code'), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2200_DSB(Segment):
    """Disability Information"""
    _segment_name = 'DSB'
    
    dsb01: Annotated[D_1146, Title('Disability Type Code'), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4'])]
    
    dsb02: Annotated[D_380, Title('Quantity'), Usage('N'), Position(2)]
    
    dsb03: Annotated[D_1149, Title('Occupation Code'), Usage('N'), Position(3)]
    
    dsb04: Annotated[D_1154, Title('Work Intensity Code'), Usage('N'), Position(4)]
    
    dsb05: Annotated[D_1161, Title('Product Option Code'), Usage('N'), Position(5)]
    
    dsb06: Annotated[D_782, Title('Monetary Amount'), Usage('N'), Position(6)]
    
    dsb07: Annotated[D_235, Title('Product or Service ID Qualifier'), Usage('S'), Position(7), Enumerated(*['DX', 'ZZ'])]
    
    dsb08: Annotated[D_1137, Title('Diagnosis Code'), Usage('S'), Position(8)]


class L2200_DTP(Segment):
    """Disability Eligibility Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['360', '361'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Disability Eligibility Date'), Usage('R'), Position(3)]


class L2200(Loop):
    
    dsb: Annotated[L2200_DSB, Title('Disability Information'), Usage('R'), Position(2000), Syntax(['P0708']), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2200_DTP, Title('Disability Eligibility Dates'), Usage('S'), Position(2100), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]


class L2300_HD(Segment):
    """Health Coverage"""
    _segment_name = 'HD'
    
    hd01: Annotated[D_875, Title('Maintenance Type Code'), Usage('R'), Position(1), Enumerated(*['001', '002', '021', '024', '025', '026', '030', '032'])]
    
    hd02: Annotated[D_1203, Title('Maintenance Reason Code'), Usage('N'), Position(2)]
    
    hd03: Annotated[D_1205, Title('Insurance Line Code'), Usage('R'), Position(3), Enumerated(*['AG', 'AH', 'AJ', 'AK', 'DCP', 'DEN', 'EPO', 'FAC', 'HE', 'HLT', 'HMO', 'LTC', 'LTD', 'MM', 'MOD', 'PDG', 'POS', 'PPO', 'PRA', 'STD', 'UR', 'VIS'])]
    
    hd04: Annotated[D_1204, Title('Plan Coverage Description'), Usage('S'), Position(4)]
    
    hd05: Annotated[D_1207, Title('Coverage Level Code'), Usage('S'), Position(5), Enumerated(*['CHD', 'DEP', 'E1D', 'E2D', 'E3D', 'E5D', 'E6D', 'E7D', 'E8D', 'E9D', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO', 'TWO'])]
    
    hd06: Annotated[D_609, Title('Count'), Usage('N'), Position(6)]
    
    hd07: Annotated[D_609, Title('Count'), Usage('N'), Position(7)]
    
    hd08: Annotated[D_1209, Title('Underwriting Decision Code'), Usage('N'), Position(8)]
    
    hd09: Annotated[D_1073, Title('Late Enrollment Indicator'), Usage('S'), Position(9), Enumerated(*['N', 'Y'])]
    
    hd10: Annotated[D_1211, Title('Drug House Code'), Usage('N'), Position(10)]
    
    hd11: Annotated[D_1073, Title('Yes/No Condition or Response Code'), Usage('N'), Position(11)]


class L2300_DTP(Segment):
    """Health Coverage Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['300', '303', '343', '348', '349', '543', '695'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Coverage Period'), Usage('R'), Position(3)]


class L2300_AMT(Segment):
    """Health Coverage Policy"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title('Amount Qualifier Code'), Usage('R'), Position(1), Enumerated(*['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R'])]
    
    amt02: Annotated[D_782, Title('Contract Amount'), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title('Credit/Debit Flag Code'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Health Coverage Policy Number"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['17', '1L', '9V', 'CE', 'E8', 'M7', 'PID', 'RB', 'X9', 'XM', 'XX1', 'XX2', 'ZX', 'ZZ'])]
    
    ref02: Annotated[D_127, Title('Member Group or Policy Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """Reference Identifier"""
    pass


class L2300_REF(Segment):
    """Prior Coverage Months"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['QQ'])]
    
    ref02: Annotated[D_127, Title('Prior Coverage Month Count'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2300_IDC(Segment):
    """Identification Card"""
    _segment_name = 'IDC'
    
    idc01: Annotated[D_1204, Title('Plan Coverage Description'), Usage('R'), Position(1)]
    
    idc02: Annotated[D_1215, Title('Identification Card Type Code'), Usage('R'), Position(2), Enumerated(*['D', 'H', 'P'])]
    
    idc03: Annotated[D_380, Title('Identification Card Count'), Usage('S'), Position(3)]
    
    idc04: Annotated[D_306, Title('Action Code'), Usage('S'), Position(4), Enumerated(*['1', '2', 'RX'])]


class L2310_LX(Segment):
    """Provider Information"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]


class L2310_NM1(Segment):
    """Provider Name"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['1X', '3D', '80', 'FA', 'OD', 'P3', 'QA', 'QN', 'Y2'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title('Provider Last or Organization Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Provider First Name'), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Provider Middle Name'), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Provider Name Prefix'), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Provider Name Suffix'), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['34', 'FI', 'SV', 'XX'])]
    
    nm109: Annotated[D_67, Title('Provider Identifier'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('R'), Position(10), Enumerated(*['25', '26', '72'])]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2310_N3(Segment):
    """Provider Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Provider Address Line'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Provider Address Line'), Usage('S'), Position(2)]


class L2310_N4(Segment):
    """Provider City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Provider City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Provider State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Provider Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2310_PER(Segment):
    """Provider Communications Numbers"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2310_PLA(Segment):
    """Provider Change Reason"""
    _segment_name = 'PLA'
    
    pla01: Annotated[D_306, Title('Action Code'), Usage('R'), Position(1), Enumerated(*['2'])]
    
    pla02: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(2), Enumerated(*['1P'])]
    
    pla03: Annotated[D_373, Title('Provider Effective Date'), Usage('R'), Position(3)]
    
    pla04: Annotated[D_337, Title('Time'), Usage('N'), Position(4)]
    
    pla05: Annotated[D_1203, Title('Maintenance Reason Code'), Usage('R'), Position(5), Enumerated(*['14', '22', '46', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ'])]


class L2310(Loop):
    
    lx: Annotated[L2310_LX, Title('Provider Information'), Usage('R'), Position(3100), Required(True)]
    
    nm1: Annotated[L2310_NM1, Title('Provider Name'), Usage('R'), Position(3200), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemN3: TypeAlias = Annotated[L2310_N3, Title('Provider Address'), Usage('S'), Position(3500), Required(True)]
    n3: Annotated[list[ItemN3], MaxItems(2)]
    
    n4: Annotated[L2310_N4, Title('Provider City, State, ZIP Code'), Usage('S'), Position(3600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemPer: TypeAlias = Annotated[L2310_PER, Title('Provider Communications Numbers'), Usage('S'), Position(3700), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]
    
    pla: Annotated[L2310_PLA, Title('Provider Change Reason'), Usage('S'), Position(3950), Required(True)]


class L2320_COB(Segment):
    """Coordination of Benefits"""
    _segment_name = 'COB'
    
    cob01: Annotated[D_1138, Title('Payer Responsibility Sequence Number Code'), Usage('R'), Position(1), Enumerated(*['P', 'S', 'T', 'U'])]
    
    cob02: Annotated[D_127, Title('Member Group or Policy Number'), Usage('S'), Position(2)]
    
    cob03: Annotated[D_1143, Title('Coordination of Benefits Code'), Usage('R'), Position(3), Enumerated(*['1', '5', '6'])]
    ItemCob04: TypeAlias = Annotated[D_1365, Title('Service Type Code'), Usage('S'), Position(4), Enumerated(*['1', '35', '48', '50', '54', '89', '90', 'A4', 'AG', 'AL', 'BB'])]
    cob04: Annotated[list[ItemCob04], MaxItems(9)]


class L2320_REF04(Composite):
    """Reference Identifier"""
    pass


class L2320_REF(Segment):
    """Additional Coordination of Benefits Identifiers"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['60', '6P', 'SY', 'ZZ'])]
    
    ref02: Annotated[D_127, Title('Member Group or Policy Number'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2320_DTP(Segment):
    """Coordination of Benefits Eligibility Dates"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['344', '345'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title('Coordination of Benefits Date'), Usage('R'), Position(3)]


class L2330_NM1(Segment):
    """Coordination of Benefits Related Entity"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['36', 'GW', 'IN'])]
    
    nm102: Annotated[D_1065, Title('Entity Type Qualifier'), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title('Coordination of Benefits Insurer Name'), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title('Name First'), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title('Name Middle'), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title('Name Prefix'), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title('Name Suffix'), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(8), Enumerated(*['FI', 'NI', 'XV'])]
    
    nm109: Annotated[D_67, Title('Coordination of Benefits Insurer Identification Code'), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title('Name Last or Organization Name'), Usage('N'), Position(12)]


class L2330_N3(Segment):
    """Coordination of Benefits Related Entity Address"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title('Address Information'), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title('Address Information'), Usage('S'), Position(2)]


class L2330_N4(Segment):
    """Coordination of Benefits Other Insurance Company City, State, ZIP Code"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title('Coordination of Benefits Other Insurance Company City Name'), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title('Coordination of Benefits Other Insurance Company State Code'), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title('Coordination of Benefits Other Insurance Company Postal Zone or ZIP Code'), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title('Country Code'), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title('Location Qualifier'), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title('Location Identifier'), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title('Country Subdivision Code'), Usage('S'), Position(7)]


class L2330_PER(Segment):
    """Administrative Communications Contact"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('Contact Function Code'), Usage('R'), Position(1), Enumerated(*['CN'])]
    
    per02: Annotated[D_93, Title('Name'), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title('Communication Number Qualifier'), Usage('R'), Position(3), Enumerated(*['TE'])]
    
    per04: Annotated[D_364, Title('Communication Number'), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title('Communication Number Qualifier'), Usage('N'), Position(5)]
    
    per06: Annotated[D_364, Title('Communication Number'), Usage('N'), Position(6)]
    
    per07: Annotated[D_365, Title('Communication Number Qualifier'), Usage('N'), Position(7)]
    
    per08: Annotated[D_364, Title('Communication Number'), Usage('N'), Position(8)]
    
    per09: Annotated[D_443, Title('Contact Inquiry Reference'), Usage('N'), Position(9)]


class L2330(Loop):
    
    nm1: Annotated[L2330_NM1, Title('Coordination of Benefits Related Entity'), Usage('R'), Position(4100), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330_N3, Title('Coordination of Benefits Related Entity Address'), Usage('S'), Position(4300), Required(True)]
    
    n4: Annotated[L2330_N4, Title('Coordination of Benefits Other Insurance Company City, State, ZIP Code'), Usage('S'), Position(4400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    per: Annotated[L2330_PER, Title('Administrative Communications Contact'), Usage('S'), Position(4500), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2320(Loop):
    
    cob: Annotated[L2320_COB, Title('Coordination of Benefits'), Usage('R'), Position(4000), Required(True)]
    ItemRef: TypeAlias = Annotated[L2320_REF, Title('Additional Coordination of Benefits Identifiers'), Usage('S'), Position(4050), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]
    ItemDtp: TypeAlias = Annotated[L2320_DTP, Title('Coordination of Benefits Eligibility Dates'), Usage('S'), Position(4070), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    ItemL2330: TypeAlias = Annotated[L2330, Title('Coordination of Benefits Related Entity'), Usage('S'), Position(4510), Required(True)]
    l2330: Annotated[list[ItemL2330], MinItems(3)]


class L2300(Loop):
    
    hd: Annotated[L2300_HD, Title('Health Coverage'), Usage('R'), Position(2600), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2300_DTP, Title('Health Coverage Dates'), Usage('R'), Position(2700), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(6)]
    ItemAmt: TypeAlias = Annotated[L2300_AMT, Title('Health Coverage Policy'), Usage('S'), Position(2800), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(9)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title('Health Coverage Policy Number'), Usage('S'), Position(2900), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(14)]
    
    ref: Annotated[L2300_REF, Title('Prior Coverage Months'), Usage('S'), Position(2900), Syntax(['R0203']), Required(True)]
    ItemIdc: TypeAlias = Annotated[L2300_IDC, Title('Identification Card'), Usage('S'), Position(3000), Required(True)]
    idc: Annotated[list[ItemIdc], MaxItems(3)]
    ItemL2310: TypeAlias = Annotated[L2310, Title('Provider Information'), Usage('S'), Position(3100), Required(True)]
    l2310: Annotated[list[ItemL2310], MinItems(30)]
    ItemL2320: TypeAlias = Annotated[L2320, Title('Coordination of Benefits'), Usage('S'), Position(4000), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(5)]


class L2700_LS_LS(Segment):
    """Additional Reporting Categories"""
    _segment_name = 'LS'
    
    ls01: Annotated[D_447, Title('Loop Identifier Code'), Usage('R'), Position(1), Enumerated(*['2700'])]


class L2700_LX(Segment):
    """Member Reporting Categories"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title('Assigned Number'), Usage('R'), Position(1)]


class L2750_N1(Segment):
    """Reporting Category"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['75'])]
    
    n102: Annotated[D_93, Title('Member Reporting Category Name'), Usage('R'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(3)]
    
    n104: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L2750_REF04(Composite):
    """Reference Identifier"""
    pass


class L2750_REF(Segment):
    """Reporting Category Reference"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['00', '17', '18', '19', '26', '3L', '6M', '9V', '9X', 'GE', 'LU', 'PID', 'XX1', 'XX2', 'YY', 'ZZ'])]
    
    ref02: Annotated[D_127, Title('Member Reporting Category Reference ID'), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title('Description'), Usage('N'), Position(3)]


class L2750_DTP(Segment):
    """Reporting Category Date"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title('Date Time Qualifier'), Usage('R'), Position(1), Enumerated(*['007'])]
    
    dtp02: Annotated[D_1250, Title('Date Time Period Format Qualifier'), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title('Member Reporting Category Effective Date(s)'), Usage('R'), Position(3)]


class L2750(Loop):
    
    n1: Annotated[L2750_N1, Title('Reporting Category'), Usage('R'), Position(6882), Syntax(['R0203', 'P0304']), Required(True)]
    
    ref: Annotated[L2750_REF, Title('Reporting Category Reference'), Usage('S'), Position(6883), Syntax(['R0203']), Required(True)]
    
    dtp: Annotated[L2750_DTP, Title('Reporting Category Date'), Usage('S'), Position(6884), Required(True)]


class L2700_LE(Segment):
    """Additional Reporting Categories Loop Termination"""
    _segment_name = 'LE'
    
    le01: Annotated[D_447, Title('Loop Identifier Code'), Usage('R'), Position(1), Enumerated(*['2700'])]


class L2700(Loop):
    
    lx: Annotated[L2700_LX, Title('Member Reporting Categories'), Usage('R'), Position(6881), Required(True)]
    ItemL2750: TypeAlias = Annotated[L2750, Title('Reporting Category'), Usage('S'), Position(6882), Required(True)]
    l2750: Annotated[list[ItemL2750], MinItems(1)]
    
    le: Annotated[L2700_LE, Title('Additional Reporting Categories Loop Termination'), Usage('S'), Position(6885), Required(True)]


class L2700_LS(Loop):
    
    ls: Annotated[L2700_LS_LS, Title('Additional Reporting Categories'), Usage('R'), Position(6880), Required(True)]
    ItemL2700: TypeAlias = Annotated[L2700, Title('Member Reporting Categories'), Usage('S'), Position(6881), Required(True)]
    l2700: Annotated[list[ItemL2700], MinItems(1)]


class L2000(Loop):
    
    ins: Annotated[L2000_INS, Title('Member Level Detail'), Usage('R'), Position(100), Syntax(['P1112']), Required(True)]
    
    ref: Annotated[L2000_REF, Title('Subscriber Identifier'), Usage('R'), Position(200), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2000_REF, Title('Member Policy Number'), Usage('S'), Position(200), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2000_REF, Title('Member Supplemental Identifier'), Usage('S'), Position(200), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(13)]
    ItemDtp: TypeAlias = Annotated[L2000_DTP, Title('Member Level Dates'), Usage('S'), Position(250), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(24)]
    ItemL2100A: TypeAlias = Annotated[L2100A, Title('Member Name'), Usage('R'), Position(300), Required(True)]
    l2100a: Annotated[list[ItemL2100A], MinItems(1)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title('Incorrect Member Name'), Usage('S'), Position(300), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2100C: TypeAlias = Annotated[L2100C, Title('Member Mailing Address'), Usage('S'), Position(300), Required(True)]
    l2100c: Annotated[list[ItemL2100C], MinItems(1)]
    ItemL2100D: TypeAlias = Annotated[L2100D, Title('Member Employer'), Usage('S'), Position(300), Required(True)]
    l2100d: Annotated[list[ItemL2100D], MinItems(3)]
    ItemL2100E: TypeAlias = Annotated[L2100E, Title('Member School'), Usage('S'), Position(300), Required(True)]
    l2100e: Annotated[list[ItemL2100E], MinItems(3)]
    ItemL2100F: TypeAlias = Annotated[L2100F, Title('Custodial Parent'), Usage('S'), Position(300), Required(True)]
    l2100f: Annotated[list[ItemL2100F], MinItems(1)]
    ItemL2100G: TypeAlias = Annotated[L2100G, Title('Responsible Person'), Usage('S'), Position(300), Required(True)]
    l2100g: Annotated[list[ItemL2100G], MinItems(13)]
    ItemL2100H: TypeAlias = Annotated[L2100H, Title('Drop Off Location'), Usage('S'), Position(700), Required(True)]
    l2100h: Annotated[list[ItemL2100H], MinItems(1)]
    ItemL2200: TypeAlias = Annotated[L2200, Title('Disability Information'), Usage('S'), Position(2000), Required(True)]
    l2200: Annotated[list[ItemL2200], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title('Health Coverage'), Usage('S'), Position(2600), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(99)]
    ItemL2700_Ls: TypeAlias = Annotated[L2700_LS, Title('Additional Reporting Categories'), Usage('S'), Position(6800), Required(True)]
    l2700_ls: Annotated[list[ItemL2700_Ls], MinItems(1)]


class DETAIL(Loop):
    ItemL2000: TypeAlias = Annotated[L2000, Title('Member Level Detail'), Usage('R'), Position(100), Required(True)]
    l2000: Annotated[list[ItemL2000], MinItems(1)]


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(100), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Header'), Usage('R'), Position(110), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table2 - Area2'), Usage('R'), Position(120), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(6900), Required(True)]


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


class MSG834A1(Message):
    """HIPAA Benefit Enrollment and Maintenance 005010X220A1 834A1"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
