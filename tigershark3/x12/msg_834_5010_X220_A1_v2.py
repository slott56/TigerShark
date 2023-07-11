"""
834.5010.X220.A1.v2
Created 2023-05-19 10:17:35.966751
"""
from .base import *
from .common import *


class ST_LOOP_ST(Segment):
    """"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title(''), Usage('R'), Position(1), Enumerated(*['834'])]
    
    st02: Annotated[D_329, Title(''), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title(''), Usage('R'), Position(3), Enumerated(*['005010X220A1'])]


class HEADER_BGN(Segment):
    """"""
    _segment_name = 'BGN'
    
    bgn01: Annotated[D_353, Title(''), Usage('R'), Position(1), Enumerated(*['00', '15', '22'])]
    
    bgn02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    bgn03: Annotated[D_373, Title(''), Usage('R'), Position(3)]
    
    bgn04: Annotated[D_337, Title(''), Usage('R'), Position(4)]
    
    bgn05: Annotated[D_623, Title(''), Usage('S'), Position(5), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', 'AD', 'AS', 'AT', 'CD', 'CS', 'CT', 'ED', 'ES', 'ET', 'GM', 'HD', 'HS', 'HT', 'LT', 'MD', 'MS', 'MT', 'ND', 'NS', 'NT', 'PD', 'PS', 'PT', 'TD', 'TS', 'TT', 'UT'])]
    
    bgn06: Annotated[D_127, Title(''), Usage('S'), Position(6)]
    
    bgn07: Annotated[D_640, Title(''), Usage('N'), Position(7)]
    
    bgn08: Annotated[D_306, Title(''), Usage('R'), Position(8), Enumerated(*['2', '4', 'RX'])]
    
    bgn09: Annotated[D_786, Title(''), Usage('N'), Position(9)]


class HEADER_REF04(Composite):
    """"""
    pass


class HEADER_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['38'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class HEADER_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['007', '090', '091', '303', '382', '388'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class HEADER_QTY03(Composite):
    """"""
    pass


class HEADER_QTY(Segment):
    """"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title(''), Usage('R'), Position(1), Enumerated(*['DT', 'ET', 'TO'])]
    
    qty02: Annotated[D_380, Title(''), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title(''), Usage('N'), Position(4)]


class L1000A_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['P5'])]
    
    n102: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('R'), Position(3), Enumerated(*['24', '94', 'FI'])]
    
    n104: Annotated[D_67, Title(''), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


class L1000A(Loop):
    
    n1: Annotated[L1000A_N1, Title(''), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]


class L1000B_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['IN'])]
    
    n102: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('R'), Position(3), Enumerated(*['94', 'FI', 'XV'])]
    
    n104: Annotated[D_67, Title(''), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


class L1000B(Loop):
    
    n1: Annotated[L1000B_N1, Title(''), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]


class L1000C_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['BO', 'TV'])]
    
    n102: Annotated[D_93, Title(''), Usage('R'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('R'), Position(3), Enumerated(*['94', 'FI', 'XV'])]
    
    n104: Annotated[D_67, Title(''), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


class L1100C_ACT(Segment):
    """"""
    _segment_name = 'ACT'
    
    act01: Annotated[D_508, Title(''), Usage('R'), Position(1)]
    
    act02: Annotated[D_93, Title(''), Usage('N'), Position(2)]
    
    act03: Annotated[D_66, Title(''), Usage('N'), Position(3)]
    
    act04: Annotated[D_67, Title(''), Usage('N'), Position(4)]
    
    act05: Annotated[D_569, Title(''), Usage('N'), Position(5)]
    
    act06: Annotated[D_508, Title(''), Usage('S'), Position(6)]
    
    act07: Annotated[D_352, Title(''), Usage('N'), Position(7)]
    
    act08: Annotated[D_107, Title(''), Usage('N'), Position(8)]
    
    act09: Annotated[D_1216, Title(''), Usage('N'), Position(9)]


class L1100C(Loop):
    
    act: Annotated[L1100C_ACT, Title(''), Usage('R'), Position(1200), Syntax(['P0304', 'C0506', 'C0705']), Required(True)]


class L1000C(Loop):
    
    n1: Annotated[L1000C_N1, Title(''), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    ItemL1100C: TypeAlias = Annotated[L1100C, Title(''), Usage('R'), Position(3600), Required(True)]
    l1100c: Annotated[list[ItemL1100C], MinItems(1)]


class HEADER(Loop):
    
    bgn: Annotated[HEADER_BGN, Title(''), Usage('R'), Position(200), Syntax(['C0504']), Required(True)]
    
    ref: Annotated[HEADER_REF, Title(''), Usage('S'), Position(300), Syntax(['R0203']), Required(True)]
    ItemDtp: TypeAlias = Annotated[HEADER_DTP, Title(''), Usage('S'), Position(400), Required(True)]
    dtp: Annotated[list[ItemDtp], MinItems(1)]
    ItemQty: TypeAlias = Annotated[HEADER_QTY, Title(''), Usage('S'), Position(600), Syntax(['E0204', 'R0204']), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(3)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title(''), Usage('R'), Position(700), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title(''), Usage('R'), Position(1900), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]
    ItemL1000C: TypeAlias = Annotated[L1000C, Title(''), Usage('R'), Position(3100), Required(True)]
    l1000c: Annotated[list[ItemL1000C], MinItems(2)]


class L2000_INS06(Composite):
    """"""
    
    ins06_01: Annotated[D_1218, Title(''), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E'])]
    
    ins06_02: Annotated[D_1701, Title(''), Usage('S'), Position(2), Enumerated(*['0', '1', '2'])]
    
    ins06_03: Annotated[D_1701, Title(''), Usage('N'), Position(3)]
    
    ins06_04: Annotated[D_1701, Title(''), Usage('N'), Position(4)]


class L2000_INS(Segment):
    """"""
    _segment_name = 'INS'
    
    ins01: Annotated[D_1073, Title(''), Usage('R'), Position(1), Enumerated(*['N', 'Y'])]
    
    ins02: Annotated[D_1069, Title(''), Usage('R'), Position(2), Enumerated(*['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26', '31', '38', '53', '60', 'D2', 'G8', 'G9'])]
    
    ins03: Annotated[D_875, Title(''), Usage('R'), Position(3), Enumerated(*['001', '021', '024', '025', '030'])]
    
    ins04: Annotated[D_1203, Title(''), Usage('S'), Position(4), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '14', '15', '16', '17', '18', '20', '21', '22', '25', '26', '27', '28', '29', '31', '32', '33', '37', '38', '39', '40', '41', '43', '59', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AL', 'EC', 'XN', 'XT'])]
    
    ins05: Annotated[D_1216, Title(''), Usage('R'), Position(5), Enumerated(*['A', 'C', 'S', 'T'])]
    
    ins06: Annotated[L2000_INS06, Title(''), Usage('S'), Position(6), Required(True)]
    
    ins07: Annotated[D_1219, Title(''), Usage('S'), Position(7), Enumerated(*['1', '10', '2', '3', '4', '5', '6', '7', '8', '9', 'ZZ'])]
    
    ins08: Annotated[D_584, Title(''), Usage('S'), Position(8), Enumerated(*['AC', 'AO', 'AU', 'FT', 'L1', 'PT', 'RT', 'TE'])]
    
    ins09: Annotated[D_1220, Title(''), Usage('S'), Position(9), Enumerated(*['F', 'N', 'P'])]
    
    ins10: Annotated[D_1073, Title(''), Usage('S'), Position(10), Enumerated(*['N', 'Y'])]
    
    ins11: Annotated[D_1250, Title(''), Usage('S'), Position(11), Enumerated(*['D8'])]
    
    ins12: Annotated[D_1251, Title(''), Usage('S'), Position(12)]
    
    ins13: Annotated[D_1165, Title(''), Usage('S'), Position(13), Enumerated(*['R', 'U'])]
    
    ins14: Annotated[D_19, Title(''), Usage('N'), Position(14)]
    
    ins15: Annotated[D_156, Title(''), Usage('N'), Position(15)]
    
    ins16: Annotated[D_26, Title(''), Usage('N'), Position(16)]
    
    ins17: Annotated[D_1470, Title(''), Usage('S'), Position(17)]


class L2000_REF04(Composite):
    """"""
    pass


class L2000_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0F'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2000_REF04(Composite):
    """"""
    pass


class L2000_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['1L'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2000_REF04(Composite):
    """"""
    pass


class L2000_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['17', '23', '3H', '4A', '6O', 'ABB', 'D3', 'DX', 'F6', 'P5', 'Q4', 'QQ', 'ZZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2000_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['050', '286', '296', '297', '300', '301', '303', '336', '337', '338', '339', '340', '341', '350', '351', '356', '357', '383', '385', '386', '393', '394', '473', '474'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2100A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['74', 'IL'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100A_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['IP'])]
    
    per02: Annotated[D_93, Title(''), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2100A_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2100A_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('S'), Position(5), Enumerated(*['60', 'CY'])]
    
    n406: Annotated[D_310, Title(''), Usage('S'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2100A_DMG05(Composite):
    """"""
    
    dmg05_01: Annotated[D_1109, Title(''), Usage('S'), Position(1), Enumerated(*['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'N', 'O', 'P', 'Z'])]
    
    dmg05_02: Annotated[D_1270, Title(''), Usage('S'), Position(2), Enumerated(*['RET'])]
    
    dmg05_03: Annotated[D_1271, Title(''), Usage('S'), Position(3)]


class L2100A_DMG(Segment):
    """"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title(''), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title(''), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title(''), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title(''), Usage('S'), Position(4), Enumerated(*['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X'])]
    
    dmg05: Annotated[L2100A_DMG05, Title(''), Usage('S'), Position(5)]
    
    dmg06: Annotated[D_1066, Title(''), Usage('S'), Position(6), Enumerated(*['1', '2', '3', '4', '5', '6', '7'])]
    
    dmg07: Annotated[D_26, Title(''), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title(''), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title(''), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title(''), Usage('S'), Position(10), Enumerated(*['REC'])]
    
    dmg11: Annotated[D_1271, Title(''), Usage('S'), Position(11)]


class L2100A_EC(Segment):
    """"""
    _segment_name = 'EC'
    
    ec01: Annotated[D_1176, Title(''), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23'])]
    
    ec02: Annotated[D_1176, Title(''), Usage('S'), Position(2), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23'])]
    
    ec03: Annotated[D_1176, Title(''), Usage('S'), Position(3), Enumerated(*['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '17', '18', '19', '20', '21', '22', '23'])]
    
    ec04: Annotated[D_954, Title(''), Usage('N'), Position(4)]
    
    ec05: Annotated[D_1201, Title(''), Usage('N'), Position(5)]
    
    ec06: Annotated[D_1149, Title(''), Usage('N'), Position(6)]


class L2100A_ICM(Segment):
    """"""
    _segment_name = 'ICM'
    
    icm01: Annotated[D_594, Title(''), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4', '6', '7', '8', '9', 'B', 'C', 'H', 'Q', 'S', 'U'])]
    
    icm02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    icm03: Annotated[D_380, Title(''), Usage('S'), Position(3)]
    
    icm04: Annotated[D_310, Title(''), Usage('S'), Position(4)]
    
    icm05: Annotated[D_1214, Title(''), Usage('S'), Position(5)]
    
    icm06: Annotated[D_100, Title(''), Usage('N'), Position(6)]


class L2100A_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2100A_HLH(Segment):
    """"""
    _segment_name = 'HLH'
    
    hlh01: Annotated[D_1212, Title(''), Usage('R'), Position(1), Enumerated(*['N', 'S', 'T', 'U', 'X'])]
    
    hlh02: Annotated[D_65, Title(''), Usage('S'), Position(2)]
    
    hlh03: Annotated[D_81, Title(''), Usage('S'), Position(3)]
    
    hlh04: Annotated[D_81, Title(''), Usage('N'), Position(4)]
    
    hlh05: Annotated[D_352, Title(''), Usage('N'), Position(5)]
    
    hlh06: Annotated[D_1213, Title(''), Usage('N'), Position(6)]
    
    hlh07: Annotated[D_352, Title(''), Usage('N'), Position(7)]


class L2100A_LUI(Segment):
    """"""
    _segment_name = 'LUI'
    
    lui01: Annotated[D_66, Title(''), Usage('S'), Position(1), Enumerated(*['LD', 'LE'])]
    
    lui02: Annotated[D_67, Title(''), Usage('S'), Position(2)]
    
    lui03: Annotated[D_352, Title(''), Usage('S'), Position(3)]
    
    lui04: Annotated[D_1303, Title(''), Usage('S'), Position(4), Enumerated(*['5', '6', '7', '8'])]
    
    lui05: Annotated[D_1476, Title(''), Usage('N'), Position(5)]


class L2100A(Loop):
    
    nm1: Annotated[L2100A_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100A_PER, Title(''), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100A_N3, Title(''), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100A_N4, Title(''), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dmg: Annotated[L2100A_DMG, Title(''), Usage('S'), Position(800), Syntax(['P0102', 'P1011', 'C1105']), Required(True)]
    ItemEc: TypeAlias = Annotated[L2100A_EC, Title(''), Usage('S'), Position(1000), Required(True)]
    ec: Annotated[list[ItemEc], MinItems(1)]
    
    icm: Annotated[L2100A_ICM, Title(''), Usage('S'), Position(1100), Required(True)]
    ItemAmt: TypeAlias = Annotated[L2100A_AMT, Title(''), Usage('S'), Position(1200), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(7)]
    
    hlh: Annotated[L2100A_HLH, Title(''), Usage('S'), Position(1300), Required(True)]
    ItemLui: TypeAlias = Annotated[L2100A_LUI, Title(''), Usage('S'), Position(1500), Syntax(['P0102', 'L040203'])]
    lui: Annotated[list[ItemLui], MinItems(1)]


class L2100B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['70'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100B_DMG05(Composite):
    """"""
    
    dmg05_01: Annotated[D_1109, Title(''), Usage('S'), Position(1), Enumerated(*['7', '8', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'N', 'O', 'P', 'Z'])]
    
    dmg05_02: Annotated[D_1270, Title(''), Usage('S'), Position(2), Enumerated(*['RET'])]
    
    dmg05_03: Annotated[D_1271, Title(''), Usage('S'), Position(3)]


class L2100B_DMG(Segment):
    """"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title(''), Usage('S'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title(''), Usage('S'), Position(2)]
    
    dmg03: Annotated[D_1068, Title(''), Usage('S'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title(''), Usage('S'), Position(4), Enumerated(*['B', 'D', 'I', 'M', 'R', 'S', 'U', 'W', 'X'])]
    
    dmg05: Annotated[L2100B_DMG05, Title(''), Usage('S'), Position(5)]
    
    dmg06: Annotated[D_1066, Title(''), Usage('S'), Position(6), Enumerated(*['1', '2', '3', '4', '5', '6', '7'])]
    
    dmg07: Annotated[D_26, Title(''), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title(''), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title(''), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title(''), Usage('S'), Position(10), Enumerated(*['REC'])]
    
    dmg11: Annotated[D_1271, Title(''), Usage('S'), Position(11)]


class L2100B(Loop):
    
    nm1: Annotated[L2100B_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    dmg: Annotated[L2100B_DMG, Title(''), Usage('S'), Position(800), Syntax(['P0102', 'P1011', 'C1105'])]


class L2100C_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['31'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('N'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title(''), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100C_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2100C_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2100C(Loop):
    
    nm1: Annotated[L2100C_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2100C_N3, Title(''), Usage('R'), Position(500), Required(True)]
    
    n4: Annotated[L2100C_N4, Title(''), Usage('R'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100D_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['36'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['24', '34'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100D_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['EP'])]
    
    per02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2100D_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2100D_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2100D(Loop):
    
    nm1: Annotated[L2100D_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100D_PER, Title(''), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100D_N3, Title(''), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100D_N4, Title(''), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100E_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['M8'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title(''), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100E_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['SK'])]
    
    per02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2100E_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2100E_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2100E(Loop):
    
    nm1: Annotated[L2100E_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100E_PER, Title(''), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100E_N3, Title(''), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100E_N4, Title(''), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100F_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['S3'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('R'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100F_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['PQ'])]
    
    per02: Annotated[D_93, Title(''), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2100F_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2100F_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2100F(Loop):
    
    nm1: Annotated[L2100F_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100F_PER, Title(''), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100F_N3, Title(''), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100F_N4, Title(''), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100G_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['6Y', '9K', 'E1', 'EI', 'EXS', 'GB', 'GD', 'J6', 'LR', 'QD', 'S1', 'TZ', 'X4'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['34', 'ZZ'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100G_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['RP'])]
    
    per02: Annotated[D_93, Title(''), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2100G_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2100G_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2100G(Loop):
    
    nm1: Annotated[L2100G_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    per: Annotated[L2100G_PER, Title(''), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    
    n3: Annotated[L2100G_N3, Title(''), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100G_N4, Title(''), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2100H_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['45'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title(''), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100H_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2100H_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2100H(Loop):
    
    nm1: Annotated[L2100H_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2100H_N3, Title(''), Usage('S'), Position(500), Required(True)]
    
    n4: Annotated[L2100H_N4, Title(''), Usage('S'), Position(600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2200_DSB(Segment):
    """"""
    _segment_name = 'DSB'
    
    dsb01: Annotated[D_1146, Title(''), Usage('R'), Position(1), Enumerated(*['1', '2', '3', '4'])]
    
    dsb02: Annotated[D_380, Title(''), Usage('N'), Position(2)]
    
    dsb03: Annotated[D_1149, Title(''), Usage('N'), Position(3)]
    
    dsb04: Annotated[D_1154, Title(''), Usage('N'), Position(4)]
    
    dsb05: Annotated[D_1161, Title(''), Usage('N'), Position(5)]
    
    dsb06: Annotated[D_782, Title(''), Usage('N'), Position(6)]
    
    dsb07: Annotated[D_235, Title(''), Usage('S'), Position(7), Enumerated(*['DX', 'ZZ'])]
    
    dsb08: Annotated[D_1137, Title(''), Usage('S'), Position(8)]


class L2200_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['360', '361'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2200(Loop):
    
    dsb: Annotated[L2200_DSB, Title(''), Usage('R'), Position(2000), Syntax(['P0708']), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2200_DTP, Title(''), Usage('S'), Position(2100), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]


class L2300_HD(Segment):
    """"""
    _segment_name = 'HD'
    
    hd01: Annotated[D_875, Title(''), Usage('R'), Position(1), Enumerated(*['001', '002', '021', '024', '025', '026', '030', '032'])]
    
    hd02: Annotated[D_1203, Title(''), Usage('N'), Position(2)]
    
    hd03: Annotated[D_1205, Title(''), Usage('R'), Position(3), Enumerated(*['AG', 'AH', 'AJ', 'AK', 'DCP', 'DEN', 'EPO', 'FAC', 'HE', 'HLT', 'HMO', 'LTC', 'LTD', 'MM', 'MOD', 'PDG', 'POS', 'PPO', 'PRA', 'STD', 'UR', 'VIS'])]
    
    hd04: Annotated[D_1204, Title(''), Usage('S'), Position(4)]
    
    hd05: Annotated[D_1207, Title(''), Usage('S'), Position(5), Enumerated(*['CHD', 'DEP', 'E1D', 'E2D', 'E3D', 'E5D', 'E6D', 'E7D', 'E8D', 'E9D', 'ECH', 'EMP', 'ESP', 'FAM', 'IND', 'SPC', 'SPO', 'TWO'])]
    
    hd06: Annotated[D_609, Title(''), Usage('N'), Position(6)]
    
    hd07: Annotated[D_609, Title(''), Usage('N'), Position(7)]
    
    hd08: Annotated[D_1209, Title(''), Usage('N'), Position(8)]
    
    hd09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'Y'])]
    
    hd10: Annotated[D_1211, Title(''), Usage('N'), Position(10)]
    
    hd11: Annotated[D_1073, Title(''), Usage('N'), Position(11)]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['300', '303', '343', '348', '349', '543', '695'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['B9', 'C1', 'D2', 'EBA', 'FK', 'P3', 'R'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['17', '1L', '9V', 'CE', 'E8', 'M7', 'PID', 'RB', 'X9', 'XM', 'XX1', 'XX2', 'ZX', 'ZZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['QQ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_IDC(Segment):
    """"""
    _segment_name = 'IDC'
    
    idc01: Annotated[D_1204, Title(''), Usage('R'), Position(1)]
    
    idc02: Annotated[D_1215, Title(''), Usage('R'), Position(2), Enumerated(*['D', 'H', 'P'])]
    
    idc03: Annotated[D_380, Title(''), Usage('S'), Position(3)]
    
    idc04: Annotated[D_306, Title(''), Usage('S'), Position(4), Enumerated(*['1', '2', 'RX'])]


class L2310_LX(Segment):
    """"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title(''), Usage('R'), Position(1)]


class L2310_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['1X', '3D', '80', 'FA', 'OD', 'P3', 'QA', 'QN', 'Y2'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['34', 'FI', 'SV', 'XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('R'), Position(10), Enumerated(*['25', '26', '72'])]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2310_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2310_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title(''), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['AP', 'BN', 'CP', 'EM', 'EX', 'FX', 'HP', 'TE', 'WP'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2310_PLA(Segment):
    """"""
    _segment_name = 'PLA'
    
    pla01: Annotated[D_306, Title(''), Usage('R'), Position(1), Enumerated(*['2'])]
    
    pla02: Annotated[D_98, Title(''), Usage('R'), Position(2), Enumerated(*['1P'])]
    
    pla03: Annotated[D_373, Title(''), Usage('R'), Position(3)]
    
    pla04: Annotated[D_337, Title(''), Usage('N'), Position(4)]
    
    pla05: Annotated[D_1203, Title(''), Usage('R'), Position(5), Enumerated(*['14', '22', '46', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ'])]


class L2310(Loop):
    
    lx: Annotated[L2310_LX, Title(''), Usage('R'), Position(3100), Required(True)]
    
    nm1: Annotated[L2310_NM1, Title(''), Usage('R'), Position(3200), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemN3: TypeAlias = Annotated[L2310_N3, Title(''), Usage('S'), Position(3500), Required(True)]
    n3: Annotated[list[ItemN3], MaxItems(2)]
    
    n4: Annotated[L2310_N4, Title(''), Usage('S'), Position(3600), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemPer: TypeAlias = Annotated[L2310_PER, Title(''), Usage('S'), Position(3700), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]
    
    pla: Annotated[L2310_PLA, Title(''), Usage('S'), Position(3950), Required(True)]


class L2320_COB(Segment):
    """"""
    _segment_name = 'COB'
    
    cob01: Annotated[D_1138, Title(''), Usage('R'), Position(1), Enumerated(*['P', 'S', 'T', 'U'])]
    
    cob02: Annotated[D_127, Title(''), Usage('S'), Position(2)]
    
    cob03: Annotated[D_1143, Title(''), Usage('R'), Position(3), Enumerated(*['1', '5', '6'])]
    
    cob04: Annotated[D_1365, Title(''), Usage('S'), Position(4), Enumerated(*['1', '35', '48', '50', '54', '89', '90', 'A4', 'AG', 'AL', 'BB'])]


class L2320_REF04(Composite):
    """"""
    pass


class L2320_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['60', '6P', 'SY', 'ZZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2320_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['344', '345'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2330_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['36', 'GW', 'IN'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['FI', 'NI', 'XV'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2330_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2330_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2330_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['CN'])]
    
    per02: Annotated[D_93, Title(''), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('N'), Position(5)]
    
    per06: Annotated[D_364, Title(''), Usage('N'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('N'), Position(7)]
    
    per08: Annotated[D_364, Title(''), Usage('N'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2330(Loop):
    
    nm1: Annotated[L2330_NM1, Title(''), Usage('R'), Position(4100), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330_N3, Title(''), Usage('S'), Position(4300), Required(True)]
    
    n4: Annotated[L2330_N4, Title(''), Usage('S'), Position(4400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    per: Annotated[L2330_PER, Title(''), Usage('S'), Position(4500), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L2320(Loop):
    
    cob: Annotated[L2320_COB, Title(''), Usage('R'), Position(4000), Required(True)]
    ItemRef: TypeAlias = Annotated[L2320_REF, Title(''), Usage('S'), Position(4050), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]
    ItemDtp: TypeAlias = Annotated[L2320_DTP, Title(''), Usage('S'), Position(4070), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(2)]
    ItemL2330: TypeAlias = Annotated[L2330, Title(''), Usage('R'), Position(4510), Required(True)]
    l2330: Annotated[list[ItemL2330], MinItems(3)]


class L2300(Loop):
    
    hd: Annotated[L2300_HD, Title(''), Usage('R'), Position(2600), Required(True)]
    ItemDtp: TypeAlias = Annotated[L2300_DTP, Title(''), Usage('R'), Position(2700), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(6)]
    ItemAmt: TypeAlias = Annotated[L2300_AMT, Title(''), Usage('S'), Position(2800), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(9)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title(''), Usage('S'), Position(2900), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(14)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(2900), Syntax(['R0203']), Required(True)]
    ItemIdc: TypeAlias = Annotated[L2300_IDC, Title(''), Usage('S'), Position(3000), Required(True)]
    idc: Annotated[list[ItemIdc], MaxItems(3)]
    ItemL2310: TypeAlias = Annotated[L2310, Title(''), Usage('R'), Position(3100), Required(True)]
    l2310: Annotated[list[ItemL2310], MinItems(30)]
    ItemL2320: TypeAlias = Annotated[L2320, Title(''), Usage('R'), Position(4000), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(5)]


class L2700_LS_LS(Segment):
    """"""
    _segment_name = 'LS'
    
    ls01: Annotated[D_447, Title(''), Usage('R'), Position(1), Enumerated(*['2700'])]


class L2700_LX(Segment):
    """"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title(''), Usage('R'), Position(1)]


class L2750_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['75'])]
    
    n102: Annotated[D_93, Title(''), Usage('R'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('N'), Position(3)]
    
    n104: Annotated[D_67, Title(''), Usage('N'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


class L2750_REF04(Composite):
    """"""
    pass


class L2750_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['00', '17', '18', '19', '26', '3L', '6M', '9V', '9X', 'GE', 'LU', 'PID', 'XX1', 'XX2', 'YY', 'ZZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2750_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['007'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2750(Loop):
    
    n1: Annotated[L2750_N1, Title(''), Usage('R'), Position(6882), Syntax(['R0203', 'P0304']), Required(True)]
    
    ref: Annotated[L2750_REF, Title(''), Usage('S'), Position(6883), Syntax(['R0203']), Required(True)]
    
    dtp: Annotated[L2750_DTP, Title(''), Usage('S'), Position(6884), Required(True)]


class L2700_LE(Segment):
    """"""
    _segment_name = 'LE'
    
    le01: Annotated[D_447, Title(''), Usage('R'), Position(1)]


class L2700(Loop):
    
    lx: Annotated[L2700_LX, Title(''), Usage('R'), Position(6881), Required(True)]
    ItemL2750: TypeAlias = Annotated[L2750, Title(''), Usage('R'), Position(6882), Required(True)]
    l2750: Annotated[list[ItemL2750], MinItems(1)]
    
    le: Annotated[L2700_LE, Title(''), Usage('S'), Position(6885), Required(True)]


class L2700_LS(Loop):
    
    ls: Annotated[L2700_LS_LS, Title(''), Usage('R'), Position(6880), Required(True)]
    ItemL2700: TypeAlias = Annotated[L2700, Title(''), Usage('R'), Position(6881), Required(True)]
    l2700: Annotated[list[ItemL2700], MinItems(1)]


class L2000(Loop):
    
    ins: Annotated[L2000_INS, Title(''), Usage('R'), Position(100), Syntax(['P1112']), Required(True)]
    
    ref: Annotated[L2000_REF, Title(''), Usage('R'), Position(200), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2000_REF, Title(''), Usage('S'), Position(200), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2000_REF, Title(''), Usage('S'), Position(200), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(13)]
    ItemDtp: TypeAlias = Annotated[L2000_DTP, Title(''), Usage('S'), Position(250), Required(True)]
    dtp: Annotated[list[ItemDtp], MaxItems(24)]
    ItemL2100A: TypeAlias = Annotated[L2100A, Title(''), Usage('R'), Position(300), Required(True)]
    l2100a: Annotated[list[ItemL2100A], MinItems(1)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title(''), Usage('R'), Position(300), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2100C: TypeAlias = Annotated[L2100C, Title(''), Usage('R'), Position(300), Required(True)]
    l2100c: Annotated[list[ItemL2100C], MinItems(1)]
    ItemL2100D: TypeAlias = Annotated[L2100D, Title(''), Usage('R'), Position(300), Required(True)]
    l2100d: Annotated[list[ItemL2100D], MinItems(3)]
    ItemL2100E: TypeAlias = Annotated[L2100E, Title(''), Usage('R'), Position(300), Required(True)]
    l2100e: Annotated[list[ItemL2100E], MinItems(3)]
    ItemL2100F: TypeAlias = Annotated[L2100F, Title(''), Usage('R'), Position(300), Required(True)]
    l2100f: Annotated[list[ItemL2100F], MinItems(1)]
    ItemL2100G: TypeAlias = Annotated[L2100G, Title(''), Usage('R'), Position(300), Required(True)]
    l2100g: Annotated[list[ItemL2100G], MinItems(13)]
    ItemL2100H: TypeAlias = Annotated[L2100H, Title(''), Usage('R'), Position(700), Required(True)]
    l2100h: Annotated[list[ItemL2100H], MinItems(1)]
    ItemL2200: TypeAlias = Annotated[L2200, Title(''), Usage('R'), Position(2000), Required(True)]
    l2200: Annotated[list[ItemL2200], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title(''), Usage('R'), Position(2600), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(99)]
    ItemL2700_Ls: TypeAlias = Annotated[L2700_LS, Title(''), Usage('S'), Position(6800), Required(True)]
    l2700_ls: Annotated[list[ItemL2700_Ls], MinItems(1)]


class TABLE2AREA2(Loop):
    ItemL2000: TypeAlias = Annotated[L2000, Title(''), Usage('R'), Position(100), Required(True)]
    l2000: Annotated[list[ItemL2000], MinItems(1)]


class ST_LOOP_SE(Segment):
    """"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title(''), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title(''), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title(''), Usage('R'), Position(100), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title(''), Usage('R'), Position(110), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemTable2Area2: TypeAlias = Annotated[TABLE2AREA2, Title(''), Usage('R'), Position(120), Required(True)]
    table2area2: Annotated[list[ItemTable2Area2], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title(''), Usage('R'), Position(6900), Required(True)]


class MSG834A1(Message):
    """HIPAA Benefit Enrollment and Maintenance 005010X220A1 834A1"""
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title(''), Usage('R'), Position(200), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
