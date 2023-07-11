"""
837Q3.I.5010.X223.A1.v2
Created 2023-05-19 10:17:36.340164
"""
from .base import *
from .common import *


class ST_LOOP_ST(Segment):
    """"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title(''), Usage('R'), Position(1), Enumerated(*['837'])]
    
    st02: Annotated[D_329, Title(''), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title(''), Usage('R'), Position(3), Enumerated(*['005010X223A2'])]


class HEADER_BHT(Segment):
    """"""
    _segment_name = 'BHT'
    
    bht01: Annotated[D_1005, Title(''), Usage('R'), Position(1), Enumerated(*['0019'])]
    
    bht02: Annotated[D_353, Title(''), Usage('R'), Position(2), Enumerated(*['00', '18'])]
    
    bht03: Annotated[D_127, Title(''), Usage('R'), Position(3)]
    
    bht04: Annotated[D_373, Title(''), Usage('R'), Position(4)]
    
    bht05: Annotated[D_337, Title(''), Usage('R'), Position(5)]
    
    bht06: Annotated[D_640, Title(''), Usage('R'), Position(6), Enumerated(*['31', 'CH', 'RP'])]


class L1000A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['41'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['46'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L1000A_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L1000A(Loop):
    
    nm1: Annotated[L1000A_NM1, Title(''), Usage('R'), Position(200), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000A_PER, Title(''), Usage('R'), Position(450), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]


class L1000B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['40'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['46'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L1000B(Loop):
    
    nm1: Annotated[L1000B_NM1, Title(''), Usage('R'), Position(200), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class HEADER(Loop):
    
    bht: Annotated[HEADER_BHT, Title(''), Usage('R'), Position(100), Required(True)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title(''), Usage('R'), Position(200), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title(''), Usage('R'), Position(500), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]


class L2000A_HL(Segment):
    """"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title(''), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title(''), Usage('N'), Position(2)]
    
    hl03: Annotated[D_735, Title(''), Usage('R'), Position(3), Enumerated(*['20'])]
    
    hl04: Annotated[D_736, Title(''), Usage('R'), Position(4), Enumerated(*['1'])]


class L2000A_PRV05(Composite):
    """"""
    pass


class L2000A_PRV(Segment):
    """"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    prv02: Annotated[D_128, Title(''), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title(''), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title(''), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title(''), Usage('N'), Position(6)]


class L2000A_CUR(Segment):
    """"""
    _segment_name = 'CUR'
    
    cur01: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['85'])]
    
    cur02: Annotated[D_100, Title(''), Usage('R'), Position(2), Enumerated(*currency)]
    
    cur03: Annotated[D_280, Title(''), Usage('N'), Position(3)]
    
    cur04: Annotated[D_98, Title(''), Usage('N'), Position(4)]
    
    cur05: Annotated[D_100, Title(''), Usage('N'), Position(5)]
    
    cur06: Annotated[D_669, Title(''), Usage('N'), Position(6)]
    
    cur07: Annotated[D_374, Title(''), Usage('N'), Position(7)]
    
    cur08: Annotated[D_373, Title(''), Usage('N'), Position(8)]
    
    cur09: Annotated[D_337, Title(''), Usage('N'), Position(9)]
    
    cur10: Annotated[D_374, Title(''), Usage('N'), Position(10)]
    
    cur11: Annotated[D_373, Title(''), Usage('N'), Position(11)]
    
    cur12: Annotated[D_337, Title(''), Usage('N'), Position(12)]
    
    cur13: Annotated[D_374, Title(''), Usage('N'), Position(13)]
    
    cur14: Annotated[D_373, Title(''), Usage('N'), Position(14)]
    
    cur15: Annotated[D_337, Title(''), Usage('N'), Position(15)]
    
    cur16: Annotated[D_374, Title(''), Usage('N'), Position(16)]
    
    cur17: Annotated[D_373, Title(''), Usage('N'), Position(17)]
    
    cur18: Annotated[D_337, Title(''), Usage('N'), Position(18)]
    
    cur19: Annotated[D_374, Title(''), Usage('N'), Position(19)]
    
    cur20: Annotated[D_373, Title(''), Usage('N'), Position(20)]
    
    cur21: Annotated[D_337, Title(''), Usage('N'), Position(21)]


class L2010AA_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['85'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2010AA_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2010AA_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2010AA_REF04(Composite):
    """"""
    pass


class L2010AA_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['EI'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010AA_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2010AA(Loop):
    
    nm1: Annotated[L2010AA_NM1, Title(''), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010AA_N3, Title(''), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010AA_N4, Title(''), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    ref: Annotated[L2010AA_REF, Title(''), Usage('R'), Position(350), Syntax(['R0203']), Required(True)]
    ItemPer: TypeAlias = Annotated[L2010AA_PER, Title(''), Usage('S'), Position(400), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]


class L2010AB_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['87'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
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


class L2010AB_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2010AB_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2010AB(Loop):
    
    nm1: Annotated[L2010AB_NM1, Title(''), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010AB_N3, Title(''), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010AB_N4, Title(''), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]


class L2010AC_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2010AC_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2010AC_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2010AC_REF04(Composite):
    """"""
    pass


class L2010AC_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010AC_REF04(Composite):
    """"""
    pass


class L2010AC_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['EI'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010AC(Loop):
    
    nm1: Annotated[L2010AC_NM1, Title(''), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010AC_N3, Title(''), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010AC_N4, Title(''), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    ref: Annotated[L2010AC_REF, Title(''), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2010AC_REF, Title(''), Usage('R'), Position(350), Syntax(['R0203']), Required(True)]


class L2000B_HL(Segment):
    """"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title(''), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title(''), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title(''), Usage('R'), Position(3), Enumerated(*['22'])]
    
    hl04: Annotated[D_736, Title(''), Usage('R'), Position(4), Enumerated(*['0', '1'])]


class L2000B_SBR(Segment):
    """"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title(''), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'P', 'S', 'T', 'U'])]
    
    sbr02: Annotated[D_1069, Title(''), Usage('S'), Position(2), Enumerated(*['18'])]
    
    sbr03: Annotated[D_127, Title(''), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title(''), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title(''), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title(''), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title(''), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title(''), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title(''), Usage('S'), Position(9), Enumerated(*['11', '12', '13', '14', '15', '16', '17', 'AM', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2010BA_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['II', 'MI'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2010BA_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2010BA_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2010BA_DMG05(Composite):
    """"""
    pass


class L2010BA_DMG(Segment):
    """"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title(''), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title(''), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title(''), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title(''), Usage('N'), Position(4)]
    
    dmg06: Annotated[D_1066, Title(''), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title(''), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title(''), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title(''), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title(''), Usage('N'), Position(10)]
    
    dmg11: Annotated[D_1271, Title(''), Usage('N'), Position(11)]


class L2010BA_REF04(Composite):
    """"""
    pass


class L2010BA_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['SY'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010BA_REF04(Composite):
    """"""
    pass


class L2010BA_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['Y4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010BA(Loop):
    
    nm1: Annotated[L2010BA_NM1, Title(''), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010BA_N3, Title(''), Usage('S'), Position(250), Required(True)]
    
    n4: Annotated[L2010BA_N4, Title(''), Usage('S'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dmg: Annotated[L2010BA_DMG, Title(''), Usage('S'), Position(320), Syntax(['P0102', 'P1011', 'C1105']), Required(True)]
    
    ref: Annotated[L2010BA_REF, Title(''), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2010BA_REF, Title(''), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]


class L2010BB_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2010BB_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2010BB_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2010BB_REF04(Composite):
    """"""
    pass


class L2010BB_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U', 'EI', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010BB_REF04(Composite):
    """"""
    pass


class L2010BB_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010BB(Loop):
    
    nm1: Annotated[L2010BB_NM1, Title(''), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010BB_N3, Title(''), Usage('S'), Position(250), Required(True)]
    
    n4: Annotated[L2010BB_N4, Title(''), Usage('S'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2010BB_REF, Title(''), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]
    
    ref: Annotated[L2010BB_REF, Title(''), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]


class L2300_CLM05(Composite):
    """"""
    
    clm05_01: Annotated[D_1331, Title(''), Usage('R'), Position(1)]
    
    clm05_02: Annotated[D_1332, Title(''), Usage('R'), Position(2), Enumerated(*['A'])]
    
    clm05_03: Annotated[D_1325, Title(''), Usage('R'), Position(3)]


class L2300_CLM11(Composite):
    """"""
    pass


class L2300_CLM(Segment):
    """"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title(''), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title(''), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title(''), Usage('N'), Position(4)]
    
    clm05: Annotated[L2300_CLM05, Title(''), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title(''), Usage('N'), Position(6)]
    
    clm07: Annotated[D_1359, Title(''), Usage('R'), Position(7), Enumerated(*['A', 'B', 'C'])]
    
    clm08: Annotated[D_1073, Title(''), Usage('R'), Position(8), Enumerated(*['N', 'W', 'Y'])]
    
    clm09: Annotated[D_1363, Title(''), Usage('R'), Position(9), Enumerated(*['I', 'Y'])]
    
    clm10: Annotated[D_1351, Title(''), Usage('N'), Position(10)]
    
    clm12: Annotated[D_1366, Title(''), Usage('N'), Position(12)]
    
    clm13: Annotated[D_1073, Title(''), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title(''), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title(''), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title(''), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title(''), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title(''), Usage('N'), Position(18)]
    
    clm19: Annotated[D_1383, Title(''), Usage('N'), Position(19)]
    
    clm20: Annotated[D_1514, Title(''), Usage('S'), Position(20), Enumerated(*['1', '10', '11', '15', '2', '3', '4', '5', '6', '7', '8', '9'])]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['TM'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['434'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['RD8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8', 'DT'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['050'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_CL1(Segment):
    """"""
    _segment_name = 'CL1'
    
    cl101: Annotated[D_1315, Title(''), Usage('R'), Position(1)]
    
    cl102: Annotated[D_1314, Title(''), Usage('S'), Position(2)]
    
    cl103: Annotated[D_1352, Title(''), Usage('R'), Position(3)]
    
    cl104: Annotated[D_1345, Title(''), Usage('N'), Position(4)]


class L2300_PWK08(Composite):
    """"""
    pass


class L2300_PWK(Segment):
    """"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title(''), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title(''), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title(''), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title(''), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title(''), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title(''), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title(''), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title(''), Usage('N'), Position(9)]


class L2300_CN1(Segment):
    """"""
    _segment_name = 'CN1'
    
    cn101: Annotated[D_1166, Title(''), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '09'])]
    
    cn102: Annotated[D_782, Title(''), Usage('S'), Position(2)]
    
    cn103: Annotated[D_332, Title(''), Usage('S'), Position(3)]
    
    cn104: Annotated[D_127, Title(''), Usage('S'), Position(4)]
    
    cn105: Annotated[D_338, Title(''), Usage('S'), Position(5)]
    
    cn106: Annotated[D_799, Title(''), Usage('S'), Position(6)]


class L2300_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['F3'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['4N'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9A'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9C'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['LX'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['P4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_K303(Composite):
    """"""
    pass


class L2300_K3(Segment):
    """"""
    _segment_name = 'K3'
    
    k301: Annotated[D_449, Title(''), Usage('R'), Position(1)]
    
    k302: Annotated[D_1333, Title(''), Usage('N'), Position(2)]


class L2300_NTE(Segment):
    """"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title(''), Usage('R'), Position(1), Enumerated(*['ALG', 'DCP', 'DGN', 'DME', 'MED', 'NTR', 'ODT', 'RHB', 'RLH', 'RNH', 'SET', 'SFM', 'SPT', 'UPI'])]
    
    nte02: Annotated[D_352, Title(''), Usage('R'), Position(2)]


class L2300_NTE(Segment):
    """"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title(''), Usage('R'), Position(1), Enumerated(*['ADD'])]
    
    nte02: Annotated[D_352, Title(''), Usage('R'), Position(2)]


class L2300_CRC(Segment):
    """"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    crc02: Annotated[D_1073, Title(''), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title(''), Usage('R'), Position(3), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc04: Annotated[D_1321, Title(''), Usage('S'), Position(4)]
    
    crc05: Annotated[D_1321, Title(''), Usage('S'), Position(5)]
    
    crc06: Annotated[D_1321, Title(''), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title(''), Usage('N'), Position(7)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABK', 'BK'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABJ', 'BJ'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['APR', 'PR'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['APR', 'PR'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['APR', 'PR'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['DR'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBR', 'BR', 'CAH'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HCP(Segment):
    """"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title(''), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title(''), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title(''), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title(''), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title(''), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title(''), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title(''), Usage('N'), Position(9)]
    
    hcp10: Annotated[D_234, Title(''), Usage('N'), Position(10)]
    
    hcp11: Annotated[D_355, Title(''), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title(''), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title(''), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title(''), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title(''), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2310A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['71'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310A_PRV05(Composite):
    """"""
    pass


class L2310A_PRV(Segment):
    """"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title(''), Usage('R'), Position(1), Enumerated(*['AT'])]
    
    prv02: Annotated[D_128, Title(''), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title(''), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title(''), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title(''), Usage('N'), Position(6)]


class L2310A_REF04(Composite):
    """"""
    pass


class L2310A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    prv: Annotated[L2310A_PRV, Title(''), Usage('S'), Position(2550), Syntax(['P0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310B_REF04(Composite):
    """"""
    pass


class L2310B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310C_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310C_REF04(Composite):
    """"""
    pass


class L2310C_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310D_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310D_REF04(Composite):
    """"""
    pass


class L2310D_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310D(Loop):
    
    nm1: Annotated[L2310D_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310D_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310E_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310E_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2310E_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2310E_REF04(Composite):
    """"""
    pass


class L2310E_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310E(Loop):
    
    nm1: Annotated[L2310E_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310E_N3, Title(''), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310E_N4, Title(''), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310E_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2310F_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['DN'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310F_REF04(Composite):
    """"""
    pass


class L2310F_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310F(Loop):
    
    nm1: Annotated[L2310F_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310F_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2320_SBR(Segment):
    """"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title(''), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'P', 'S', 'T', 'U'])]
    
    sbr02: Annotated[D_1069, Title(''), Usage('R'), Position(2), Enumerated(*['01', '18', '19', '20', '21', '39', '40', '53', 'G8'])]
    
    sbr03: Annotated[D_127, Title(''), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title(''), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title(''), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title(''), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title(''), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title(''), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title(''), Usage('S'), Position(9), Enumerated(*['11', '12', '13', '14', '15', '16', '17', 'AM', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title(''), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title(''), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title(''), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title(''), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title(''), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title(''), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title(''), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title(''), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title(''), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title(''), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title(''), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title(''), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title(''), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title(''), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title(''), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title(''), Usage('S'), Position(19)]


class L2320_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['D'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['A8'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2320_OI(Segment):
    """"""
    _segment_name = 'OI'
    
    oi01: Annotated[D_1032, Title(''), Usage('N'), Position(1)]
    
    oi02: Annotated[D_1383, Title(''), Usage('N'), Position(2)]
    
    oi03: Annotated[D_1073, Title(''), Usage('R'), Position(3), Enumerated(*['N', 'W', 'Y'])]
    
    oi04: Annotated[D_1351, Title(''), Usage('N'), Position(4)]
    
    oi05: Annotated[D_1360, Title(''), Usage('N'), Position(5)]
    
    oi06: Annotated[D_1363, Title(''), Usage('R'), Position(6), Enumerated(*['I', 'Y'])]


class L2320_MIA(Segment):
    """"""
    _segment_name = 'MIA'
    
    mia01: Annotated[D_380, Title(''), Usage('R'), Position(1)]
    
    mia02: Annotated[D_782, Title(''), Usage('N'), Position(2)]
    
    mia03: Annotated[D_380, Title(''), Usage('S'), Position(3)]
    
    mia04: Annotated[D_782, Title(''), Usage('S'), Position(4)]
    
    mia05: Annotated[D_127, Title(''), Usage('S'), Position(5), Enumerated(*remark_code)]
    
    mia06: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    mia07: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    mia08: Annotated[D_782, Title(''), Usage('S'), Position(8)]
    
    mia09: Annotated[D_782, Title(''), Usage('S'), Position(9)]
    
    mia10: Annotated[D_782, Title(''), Usage('S'), Position(10)]
    
    mia11: Annotated[D_782, Title(''), Usage('S'), Position(11)]
    
    mia12: Annotated[D_782, Title(''), Usage('S'), Position(12)]
    
    mia13: Annotated[D_782, Title(''), Usage('S'), Position(13)]
    
    mia14: Annotated[D_782, Title(''), Usage('S'), Position(14)]
    
    mia15: Annotated[D_380, Title(''), Usage('S'), Position(15)]
    
    mia16: Annotated[D_782, Title(''), Usage('S'), Position(16)]
    
    mia17: Annotated[D_782, Title(''), Usage('S'), Position(17)]
    
    mia18: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    mia19: Annotated[D_782, Title(''), Usage('S'), Position(19)]
    
    mia20: Annotated[D_127, Title(''), Usage('S'), Position(20), Enumerated(*remark_code)]
    
    mia21: Annotated[D_127, Title(''), Usage('S'), Position(21), Enumerated(*remark_code)]
    
    mia22: Annotated[D_127, Title(''), Usage('S'), Position(22), Enumerated(*remark_code)]
    
    mia23: Annotated[D_127, Title(''), Usage('S'), Position(23), Enumerated(*remark_code)]
    
    mia24: Annotated[D_782, Title(''), Usage('S'), Position(24)]


class L2320_MOA(Segment):
    """"""
    _segment_name = 'MOA'
    
    moa01: Annotated[D_954, Title(''), Usage('S'), Position(1)]
    
    moa02: Annotated[D_782, Title(''), Usage('S'), Position(2)]
    
    moa03: Annotated[D_127, Title(''), Usage('S'), Position(3), Enumerated(*remark_code)]
    
    moa04: Annotated[D_127, Title(''), Usage('S'), Position(4), Enumerated(*remark_code)]
    
    moa05: Annotated[D_127, Title(''), Usage('S'), Position(5), Enumerated(*remark_code)]
    
    moa06: Annotated[D_127, Title(''), Usage('S'), Position(6), Enumerated(*remark_code)]
    
    moa07: Annotated[D_127, Title(''), Usage('S'), Position(7), Enumerated(*remark_code)]
    
    moa08: Annotated[D_782, Title(''), Usage('S'), Position(8)]
    
    moa09: Annotated[D_782, Title(''), Usage('S'), Position(9)]


class L2330A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['II', 'MI'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2330A_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2330A_REF04(Composite):
    """"""
    pass


class L2330A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['SY'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330A_N3, Title(''), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330A_N4, Title(''), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330A_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2330B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2330B_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2330B_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2330B_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U', 'EI', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['T4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330B_N3, Title(''), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330B_N4, Title(''), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dtp: Annotated[L2330B_DTP, Title(''), Usage('S'), Position(3500), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]


class L2330C_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['71'])]
    
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


class L2330C_REF04(Composite):
    """"""
    pass


class L2330C_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330D_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['72'])]
    
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


class L2330D_REF04(Composite):
    """"""
    pass


class L2330D_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330E_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
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


class L2330E_REF04(Composite):
    """"""
    pass


class L2330E_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330F_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
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


class L2330F_REF04(Composite):
    """"""
    pass


class L2330F_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330F(Loop):
    
    nm1: Annotated[L2330F_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330F_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330G_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['82'])]
    
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


class L2330G_REF04(Composite):
    """"""
    pass


class L2330G_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330G(Loop):
    
    nm1: Annotated[L2330G_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330G_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330H_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['DN'])]
    
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


class L2330H_REF04(Composite):
    """"""
    pass


class L2330H_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330H(Loop):
    
    nm1: Annotated[L2330H_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330H_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330I_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['85'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
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


class L2330I_REF04(Composite):
    """"""
    pass


class L2330I_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330I(Loop):
    
    nm1: Annotated[L2330I_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330I_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title(''), Usage('R'), Position(2900), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title(''), Usage('S'), Position(2950), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title(''), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title(''), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title(''), Usage('S'), Position(3000), Required(True)]
    
    oi: Annotated[L2320_OI, Title(''), Usage('R'), Position(3100), Required(True)]
    
    mia: Annotated[L2320_MIA, Title(''), Usage('S'), Position(3150), Required(True)]
    
    moa: Annotated[L2320_MOA, Title(''), Usage('S'), Position(3200)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title(''), Usage('R'), Position(3250), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title(''), Usage('R'), Position(3250), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title(''), Usage('S'), Position(3250), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(1)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title(''), Usage('S'), Position(3600), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title(''), Usage('S'), Position(3700), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]
    ItemL2330F: TypeAlias = Annotated[L2330F, Title(''), Usage('S'), Position(3900), Required(True)]
    l2330f: Annotated[list[ItemL2330F], MinItems(1)]
    ItemL2330G: TypeAlias = Annotated[L2330G, Title(''), Usage('S'), Position(4000), Required(True)]
    l2330g: Annotated[list[ItemL2330G], MinItems(1)]
    ItemL2330H: TypeAlias = Annotated[L2330H, Title(''), Usage('S'), Position(5000), Required(True)]
    l2330h: Annotated[list[ItemL2330H], MinItems(1)]
    ItemL2330I: TypeAlias = Annotated[L2330I, Title(''), Usage('S'), Position(6000), Required(True)]
    l2330i: Annotated[list[ItemL2330I], MinItems(1)]


class L2400_LX(Segment):
    """"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title(''), Usage('R'), Position(1)]


class L2400_SV202(Composite):
    """"""
    
    sv202_01: Annotated[D_235, Title(''), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'HP', 'IV', 'WK'])]
    
    sv202_02: Annotated[D_234, Title(''), Usage('R'), Position(2)]
    
    sv202_03: Annotated[D_1339, Title(''), Usage('S'), Position(3)]
    
    sv202_04: Annotated[D_1339, Title(''), Usage('S'), Position(4)]
    
    sv202_05: Annotated[D_1339, Title(''), Usage('S'), Position(5)]
    
    sv202_06: Annotated[D_1339, Title(''), Usage('S'), Position(6)]
    
    sv202_07: Annotated[D_352, Title(''), Usage('S'), Position(7)]
    
    sv202_08: Annotated[D_234, Title(''), Usage('N'), Position(8)]


class L2400_SV2(Segment):
    """"""
    _segment_name = 'SV2'
    
    sv201: Annotated[D_234, Title(''), Usage('R'), Position(1)]
    
    sv202: Annotated[L2400_SV202, Title(''), Usage('S'), Position(2), Required(True)]
    
    sv203: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    sv204: Annotated[D_355, Title(''), Usage('R'), Position(4), Enumerated(*['DA', 'UN'])]
    
    sv205: Annotated[D_380, Title(''), Usage('R'), Position(5)]
    
    sv206: Annotated[D_1371, Title(''), Usage('N'), Position(6)]
    
    sv207: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    sv208: Annotated[D_1073, Title(''), Usage('N'), Position(8)]
    
    sv209: Annotated[D_1345, Title(''), Usage('N'), Position(9)]
    
    sv210: Annotated[D_1337, Title(''), Usage('N'), Position(10)]


class L2400_PWK08(Composite):
    """"""
    pass


class L2400_PWK(Segment):
    """"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title(''), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title(''), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title(''), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title(''), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title(''), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title(''), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title(''), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title(''), Usage('N'), Position(9)]


class L2400_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2400_REF04(Composite):
    """"""
    pass


class L2400_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['6R'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """"""
    pass


class L2400_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9B'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """"""
    pass


class L2400_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9D'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['GT'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['N8'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2400_NTE(Segment):
    """"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title(''), Usage('R'), Position(1), Enumerated(*['TPO'])]
    
    nte02: Annotated[D_352, Title(''), Usage('R'), Position(2)]


class L2400_HCP(Segment):
    """"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title(''), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title(''), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title(''), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title(''), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title(''), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title(''), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title(''), Usage('S'), Position(9), Enumerated(*['ER', 'HC', 'HP', 'IV', 'WK'])]
    
    hcp10: Annotated[D_234, Title(''), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title(''), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title(''), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title(''), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title(''), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title(''), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2410_LIN(Segment):
    """"""
    _segment_name = 'LIN'
    
    lin01: Annotated[D_350, Title(''), Usage('N'), Position(1)]
    
    lin02: Annotated[D_235, Title(''), Usage('R'), Position(2), Enumerated(*['N4'])]
    
    lin03: Annotated[D_234, Title(''), Usage('R'), Position(3)]
    
    lin04: Annotated[D_235, Title(''), Usage('N'), Position(4)]
    
    lin05: Annotated[D_234, Title(''), Usage('N'), Position(5)]
    
    lin06: Annotated[D_235, Title(''), Usage('N'), Position(6)]
    
    lin07: Annotated[D_234, Title(''), Usage('N'), Position(7)]
    
    lin08: Annotated[D_235, Title(''), Usage('N'), Position(8)]
    
    lin09: Annotated[D_234, Title(''), Usage('N'), Position(9)]
    
    lin10: Annotated[D_235, Title(''), Usage('N'), Position(10)]
    
    lin11: Annotated[D_234, Title(''), Usage('N'), Position(11)]
    
    lin12: Annotated[D_235, Title(''), Usage('N'), Position(12)]
    
    lin13: Annotated[D_234, Title(''), Usage('N'), Position(13)]
    
    lin14: Annotated[D_235, Title(''), Usage('N'), Position(14)]
    
    lin15: Annotated[D_234, Title(''), Usage('N'), Position(15)]
    
    lin16: Annotated[D_235, Title(''), Usage('N'), Position(16)]
    
    lin17: Annotated[D_234, Title(''), Usage('N'), Position(17)]
    
    lin18: Annotated[D_235, Title(''), Usage('N'), Position(18)]
    
    lin19: Annotated[D_234, Title(''), Usage('N'), Position(19)]
    
    lin20: Annotated[D_235, Title(''), Usage('N'), Position(20)]
    
    lin21: Annotated[D_234, Title(''), Usage('N'), Position(21)]
    
    lin22: Annotated[D_235, Title(''), Usage('N'), Position(22)]
    
    lin23: Annotated[D_234, Title(''), Usage('N'), Position(23)]
    
    lin24: Annotated[D_235, Title(''), Usage('N'), Position(24)]
    
    lin25: Annotated[D_234, Title(''), Usage('N'), Position(25)]
    
    lin26: Annotated[D_235, Title(''), Usage('N'), Position(26)]
    
    lin27: Annotated[D_234, Title(''), Usage('N'), Position(27)]
    
    lin28: Annotated[D_235, Title(''), Usage('N'), Position(28)]
    
    lin29: Annotated[D_234, Title(''), Usage('N'), Position(29)]
    
    lin30: Annotated[D_235, Title(''), Usage('N'), Position(30)]
    
    lin31: Annotated[D_234, Title(''), Usage('N'), Position(31)]


class L2410_CTP05(Composite):
    """"""
    
    ctp05_01: Annotated[D_355, Title(''), Usage('R'), Position(1), Enumerated(*['F2', 'GR', 'ME', 'ML', 'UN'])]
    
    ctp05_02: Annotated[D_1018, Title(''), Usage('N'), Position(2)]
    
    ctp05_03: Annotated[D_649, Title(''), Usage('N'), Position(3)]
    
    ctp05_04: Annotated[D_355, Title(''), Usage('N'), Position(4)]
    
    ctp05_05: Annotated[D_1018, Title(''), Usage('N'), Position(5)]
    
    ctp05_06: Annotated[D_649, Title(''), Usage('N'), Position(6)]
    
    ctp05_07: Annotated[D_355, Title(''), Usage('N'), Position(7)]
    
    ctp05_08: Annotated[D_1018, Title(''), Usage('N'), Position(8)]
    
    ctp05_09: Annotated[D_649, Title(''), Usage('N'), Position(9)]
    
    ctp05_10: Annotated[D_355, Title(''), Usage('N'), Position(10)]
    
    ctp05_11: Annotated[D_1018, Title(''), Usage('N'), Position(11)]
    
    ctp05_12: Annotated[D_649, Title(''), Usage('N'), Position(12)]
    
    ctp05_13: Annotated[D_355, Title(''), Usage('N'), Position(13)]
    
    ctp05_14: Annotated[D_1018, Title(''), Usage('N'), Position(14)]
    
    ctp05_15: Annotated[D_649, Title(''), Usage('N'), Position(15)]


class L2410_CTP(Segment):
    """"""
    _segment_name = 'CTP'
    
    ctp01: Annotated[D_687, Title(''), Usage('N'), Position(1)]
    
    ctp02: Annotated[D_236, Title(''), Usage('N'), Position(2)]
    
    ctp03: Annotated[D_212, Title(''), Usage('N'), Position(3)]
    
    ctp04: Annotated[D_380, Title(''), Usage('R'), Position(4)]
    
    ctp05: Annotated[L2410_CTP05, Title(''), Usage('R'), Position(5), Required(True)]
    
    ctp06: Annotated[D_648, Title(''), Usage('N'), Position(6)]
    
    ctp07: Annotated[D_649, Title(''), Usage('N'), Position(7)]
    
    ctp08: Annotated[D_782, Title(''), Usage('N'), Position(8)]
    
    ctp09: Annotated[D_639, Title(''), Usage('N'), Position(9)]
    
    ctp10: Annotated[D_499, Title(''), Usage('N'), Position(10)]
    
    ctp11: Annotated[D_289, Title(''), Usage('N'), Position(11)]


class L2410_REF04(Composite):
    """"""
    pass


class L2410_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['VY', 'XZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2410(Loop):
    
    lin: Annotated[L2410_LIN, Title(''), Usage('R'), Position(4930), Syntax(['P0405', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425', 'P2627', 'P2829', 'P3031']), Required(True)]
    
    ctp: Annotated[L2410_CTP, Title(''), Usage('R'), Position(4940), Syntax(['P0405', 'C0607', 'C0902', 'C1002', 'C1103']), Required(True)]
    
    ref: Annotated[L2410_REF, Title(''), Usage('S'), Position(4950), Syntax(['R0203']), Required(True)]


class L2420A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420A_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420A_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420A_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420B_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420B_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420B_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420C_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420C_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420C_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420C_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420C_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420D_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['DN'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420D_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420D_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420D_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420D(Loop):
    
    nm1: Annotated[L2420D_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420D_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2430_SVD03(Composite):
    """"""
    
    svd03_01: Annotated[D_235, Title(''), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'HP', 'IV', 'WK'])]
    
    svd03_02: Annotated[D_234, Title(''), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title(''), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title(''), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title(''), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title(''), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title(''), Usage('S'), Position(7)]
    
    svd03_08: Annotated[D_234, Title(''), Usage('N'), Position(8)]


class L2430_SVD(Segment):
    """"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title(''), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    svd03: Annotated[L2430_SVD03, Title(''), Usage('S'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title(''), Usage('R'), Position(4)]
    
    svd05: Annotated[D_380, Title(''), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title(''), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title(''), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title(''), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title(''), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title(''), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title(''), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title(''), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title(''), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title(''), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title(''), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title(''), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title(''), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title(''), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title(''), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title(''), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title(''), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title(''), Usage('S'), Position(19)]


class L2430_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2430_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title(''), Usage('R'), Position(5400), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title(''), Usage('S'), Position(5450), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    dtp: Annotated[L2430_DTP, Title(''), Usage('R'), Position(5500), Required(True)]
    
    amt: Annotated[L2430_AMT, Title(''), Usage('S'), Position(5505), Required(True)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title(''), Usage('R'), Position(3650), Required(True)]
    
    sv2: Annotated[L2400_SV2, Title(''), Usage('R'), Position(3750), Syntax(['R0102', 'P0405']), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2400_PWK, Title(''), Usage('S'), Position(4200), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    dtp: Annotated[L2400_DTP, Title(''), Usage('S'), Position(4550), Required(True)]
    
    ref: Annotated[L2400_REF, Title(''), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title(''), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title(''), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    amt: Annotated[L2400_AMT, Title(''), Usage('S'), Position(4750), Required(True)]
    
    amt: Annotated[L2400_AMT, Title(''), Usage('S'), Position(4750), Required(True)]
    
    nte: Annotated[L2400_NTE, Title(''), Usage('S'), Position(4850), Required(True)]
    
    hcp: Annotated[L2400_HCP, Title(''), Usage('S'), Position(4920), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2410: TypeAlias = Annotated[L2410, Title(''), Usage('S'), Position(4940), Required(True)]
    l2410: Annotated[list[ItemL2410], MinItems(1)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title(''), Usage('S'), Position(5000), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title(''), Usage('S'), Position(5000), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title(''), Usage('S'), Position(5000), Required(True)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2420D: TypeAlias = Annotated[L2420D, Title(''), Usage('S'), Position(5300), Required(True)]
    l2420d: Annotated[list[ItemL2420D], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title(''), Usage('S'), Position(5400), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(15)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title(''), Usage('R'), Position(1300), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('R'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('S'), Position(1350), Required(True)]
    
    cl1: Annotated[L2300_CL1, Title(''), Usage('R'), Position(1400), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title(''), Usage('S'), Position(1550), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    cn1: Annotated[L2300_CN1, Title(''), Usage('S'), Position(1600), Required(True)]
    
    amt: Annotated[L2300_AMT, Title(''), Usage('S'), Position(1750), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ItemK3: TypeAlias = Annotated[L2300_K3, Title(''), Usage('S'), Position(1850), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    ItemNte: TypeAlias = Annotated[L2300_NTE, Title(''), Usage('S'), Position(1900), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(10)]
    
    nte: Annotated[L2300_NTE, Title(''), Usage('S'), Position(1900), Required(True)]
    
    crc: Annotated[L2300_CRC, Title(''), Usage('S'), Position(2200), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('R'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hcp: Annotated[L2300_HCP, Title(''), Usage('S'), Position(2410), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(1)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310D: TypeAlias = Annotated[L2310D, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310d: Annotated[list[ItemL2310D], MinItems(1)]
    ItemL2310E: TypeAlias = Annotated[L2310E, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310e: Annotated[list[ItemL2310E], MinItems(1)]
    ItemL2310F: TypeAlias = Annotated[L2310F, Title(''), Usage('S'), Position(2800), Required(True)]
    l2310f: Annotated[list[ItemL2310F], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title(''), Usage('S'), Position(2900), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title(''), Usage('R'), Position(3650), Required(True)]
    l2400: Annotated[list[ItemL2400], MinItems(999)]


class L2000C_HL(Segment):
    """"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title(''), Usage('R'), Position(1)]
    
    hl02: Annotated[D_734, Title(''), Usage('R'), Position(2)]
    
    hl03: Annotated[D_735, Title(''), Usage('R'), Position(3), Enumerated(*['23'])]
    
    hl04: Annotated[D_736, Title(''), Usage('R'), Position(4), Enumerated(*['0'])]


class L2000C_PAT(Segment):
    """"""
    _segment_name = 'PAT'
    
    pat01: Annotated[D_1069, Title(''), Usage('R'), Position(1), Enumerated(*['01', '19', '20', '21', '39', '40', '53', 'G8'])]
    
    pat02: Annotated[D_1384, Title(''), Usage('N'), Position(2)]
    
    pat03: Annotated[D_584, Title(''), Usage('N'), Position(3)]
    
    pat04: Annotated[D_1220, Title(''), Usage('N'), Position(4)]
    
    pat05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    pat06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]
    
    pat07: Annotated[D_355, Title(''), Usage('N'), Position(7)]
    
    pat08: Annotated[D_81, Title(''), Usage('N'), Position(8)]
    
    pat09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2010CA_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('N'), Position(8)]
    
    nm109: Annotated[D_67, Title(''), Usage('N'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2010CA_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2010CA_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2010CA_DMG05(Composite):
    """"""
    pass


class L2010CA_DMG(Segment):
    """"""
    _segment_name = 'DMG'
    
    dmg01: Annotated[D_1250, Title(''), Usage('R'), Position(1), Enumerated(*['D8'])]
    
    dmg02: Annotated[D_1251, Title(''), Usage('R'), Position(2)]
    
    dmg03: Annotated[D_1068, Title(''), Usage('R'), Position(3), Enumerated(*['F', 'M', 'U'])]
    
    dmg04: Annotated[D_1067, Title(''), Usage('N'), Position(4)]
    
    dmg06: Annotated[D_1066, Title(''), Usage('N'), Position(6)]
    
    dmg07: Annotated[D_26, Title(''), Usage('N'), Position(7)]
    
    dmg08: Annotated[D_659, Title(''), Usage('N'), Position(8)]
    
    dmg09: Annotated[D_380, Title(''), Usage('N'), Position(9)]
    
    dmg10: Annotated[D_1270, Title(''), Usage('N'), Position(10)]
    
    dmg11: Annotated[D_1271, Title(''), Usage('N'), Position(11)]


class L2010CA_REF04(Composite):
    """"""
    pass


class L2010CA_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['Y4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010CA_REF04(Composite):
    """"""
    pass


class L2010CA_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['1W', 'SY'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2010CA(Loop):
    
    nm1: Annotated[L2010CA_NM1, Title(''), Usage('R'), Position(150), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2010CA_N3, Title(''), Usage('R'), Position(250), Required(True)]
    
    n4: Annotated[L2010CA_N4, Title(''), Usage('R'), Position(300), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dmg: Annotated[L2010CA_DMG, Title(''), Usage('R'), Position(320), Syntax(['P0102', 'P1011', 'C1105']), Required(True)]
    
    ref: Annotated[L2010CA_REF, Title(''), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2010CA_REF, Title(''), Usage('S'), Position(350), Syntax(['R0203']), Required(True)]


class L2300_CLM05(Composite):
    """"""
    
    clm05_01: Annotated[D_1331, Title(''), Usage('R'), Position(1)]
    
    clm05_02: Annotated[D_1332, Title(''), Usage('R'), Position(2), Enumerated(*['A'])]
    
    clm05_03: Annotated[D_1325, Title(''), Usage('R'), Position(3)]


class L2300_CLM11(Composite):
    """"""
    pass


class L2300_CLM(Segment):
    """"""
    _segment_name = 'CLM'
    
    clm01: Annotated[D_1028, Title(''), Usage('R'), Position(1)]
    
    clm02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    clm03: Annotated[D_1032, Title(''), Usage('N'), Position(3)]
    
    clm04: Annotated[D_1343, Title(''), Usage('N'), Position(4)]
    
    clm05: Annotated[L2300_CLM05, Title(''), Usage('R'), Position(5), Required(True)]
    
    clm06: Annotated[D_1073, Title(''), Usage('N'), Position(6)]
    
    clm07: Annotated[D_1359, Title(''), Usage('R'), Position(7), Enumerated(*['A', 'B', 'C'])]
    
    clm08: Annotated[D_1073, Title(''), Usage('R'), Position(8), Enumerated(*['N', 'W', 'Y'])]
    
    clm09: Annotated[D_1363, Title(''), Usage('R'), Position(9), Enumerated(*['I', 'Y'])]
    
    clm10: Annotated[D_1351, Title(''), Usage('N'), Position(10)]
    
    clm12: Annotated[D_1366, Title(''), Usage('N'), Position(12)]
    
    clm13: Annotated[D_1073, Title(''), Usage('N'), Position(13)]
    
    clm14: Annotated[D_1338, Title(''), Usage('N'), Position(14)]
    
    clm15: Annotated[D_1073, Title(''), Usage('N'), Position(15)]
    
    clm16: Annotated[D_1360, Title(''), Usage('N'), Position(16)]
    
    clm17: Annotated[D_1029, Title(''), Usage('N'), Position(17)]
    
    clm18: Annotated[D_1073, Title(''), Usage('N'), Position(18)]
    
    clm19: Annotated[D_1383, Title(''), Usage('N'), Position(19)]
    
    clm20: Annotated[D_1514, Title(''), Usage('S'), Position(20), Enumerated(*['1', '10', '11', '15', '2', '3', '4', '5', '6', '7', '8', '9'])]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['096'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['TM'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['434'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['RD8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['435'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8', 'DT'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['050'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2300_CL1(Segment):
    """"""
    _segment_name = 'CL1'
    
    cl101: Annotated[D_1315, Title(''), Usage('R'), Position(1)]
    
    cl102: Annotated[D_1314, Title(''), Usage('S'), Position(2)]
    
    cl103: Annotated[D_1352, Title(''), Usage('R'), Position(3)]
    
    cl104: Annotated[D_1345, Title(''), Usage('N'), Position(4)]


class L2300_PWK08(Composite):
    """"""
    pass


class L2300_PWK(Segment):
    """"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title(''), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title(''), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title(''), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title(''), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title(''), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title(''), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title(''), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title(''), Usage('N'), Position(9)]


class L2300_CN1(Segment):
    """"""
    _segment_name = 'CN1'
    
    cn101: Annotated[D_1166, Title(''), Usage('R'), Position(1), Enumerated(*['01', '02', '03', '04', '05', '06', '09'])]
    
    cn102: Annotated[D_782, Title(''), Usage('S'), Position(2)]
    
    cn103: Annotated[D_332, Title(''), Usage('S'), Position(3)]
    
    cn104: Annotated[D_127, Title(''), Usage('S'), Position(4)]
    
    cn105: Annotated[D_338, Title(''), Usage('S'), Position(5)]
    
    cn106: Annotated[D_799, Title(''), Usage('S'), Position(6)]


class L2300_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['F3'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['4N'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9A'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9C'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['LX'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['D9'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['EA'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['P4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_REF04(Composite):
    """"""
    pass


class L2300_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300_K303(Composite):
    """"""
    pass


class L2300_K3(Segment):
    """"""
    _segment_name = 'K3'
    
    k301: Annotated[D_449, Title(''), Usage('R'), Position(1)]
    
    k302: Annotated[D_1333, Title(''), Usage('N'), Position(2)]


class L2300_NTE(Segment):
    """"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title(''), Usage('R'), Position(1), Enumerated(*['ALG', 'DCP', 'DGN', 'DME', 'MED', 'NTR', 'ODT', 'RHB', 'RLH', 'RNH', 'SET', 'SFM', 'SPT', 'UPI'])]
    
    nte02: Annotated[D_352, Title(''), Usage('R'), Position(2)]


class L2300_NTE(Segment):
    """"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title(''), Usage('R'), Position(1), Enumerated(*['ADD'])]
    
    nte02: Annotated[D_352, Title(''), Usage('R'), Position(2)]


class L2300_CRC(Segment):
    """"""
    _segment_name = 'CRC'
    
    crc01: Annotated[D_1136, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    crc02: Annotated[D_1073, Title(''), Usage('R'), Position(2), Enumerated(*['N', 'Y'])]
    
    crc03: Annotated[D_1321, Title(''), Usage('R'), Position(3), Enumerated(*['AV', 'NU', 'S2', 'ST'])]
    
    crc04: Annotated[D_1321, Title(''), Usage('S'), Position(4)]
    
    crc05: Annotated[D_1321, Title(''), Usage('S'), Position(5)]
    
    crc06: Annotated[D_1321, Title(''), Usage('N'), Position(6)]
    
    crc07: Annotated[D_1321, Title(''), Usage('N'), Position(7)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABK', 'BK'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABJ', 'BJ'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['APR', 'PR'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['APR', 'PR'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['APR', 'PR'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABN', 'BN'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['DR'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['ABF', 'BF'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('S'), Position(9), Enumerated(*['N', 'U', 'W', 'Y'])]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBR', 'BR', 'CAH'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    pass


class L2300_HI03(Composite):
    """"""
    pass


class L2300_HI04(Composite):
    """"""
    pass


class L2300_HI05(Composite):
    """"""
    pass


class L2300_HI06(Composite):
    """"""
    pass


class L2300_HI07(Composite):
    """"""
    pass


class L2300_HI08(Composite):
    """"""
    pass


class L2300_HI09(Composite):
    """"""
    pass


class L2300_HI10(Composite):
    """"""
    pass


class L2300_HI11(Composite):
    """"""
    pass


class L2300_HI12(Composite):
    """"""
    pass


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BBQ', 'BQ'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BI'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['RD8'])]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BH'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('R'), Position(3), Enumerated(*['D8'])]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('R'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BE'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['BG'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HI01(Composite):
    """"""
    
    hi01_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi01_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi01_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi01_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi01_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi01_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi01_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi01_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi01_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI02(Composite):
    """"""
    
    hi02_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi02_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi02_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi02_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi02_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi02_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi02_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi02_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi02_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI03(Composite):
    """"""
    
    hi03_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi03_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi03_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi03_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi03_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi03_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi03_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi03_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi03_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI04(Composite):
    """"""
    
    hi04_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi04_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi04_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi04_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi04_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi04_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi04_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi04_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi04_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI05(Composite):
    """"""
    
    hi05_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi05_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi05_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi05_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi05_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi05_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi05_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi05_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi05_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI06(Composite):
    """"""
    
    hi06_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi06_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi06_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi06_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi06_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi06_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi06_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi06_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi06_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI07(Composite):
    """"""
    
    hi07_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi07_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi07_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi07_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi07_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi07_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi07_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi07_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi07_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI08(Composite):
    """"""
    
    hi08_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi08_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi08_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi08_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi08_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi08_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi08_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi08_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi08_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI09(Composite):
    """"""
    
    hi09_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi09_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi09_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi09_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi09_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi09_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi09_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi09_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi09_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI10(Composite):
    """"""
    
    hi10_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi10_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi10_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi10_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi10_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi10_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi10_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi10_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi10_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI11(Composite):
    """"""
    
    hi11_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi11_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi11_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi11_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi11_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi11_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi11_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi11_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi11_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI12(Composite):
    """"""
    
    hi12_01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['TC'])]
    
    hi12_02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]
    
    hi12_03: Annotated[D_1250, Title(''), Usage('N'), Position(3)]
    
    hi12_04: Annotated[D_1251, Title(''), Usage('N'), Position(4)]
    
    hi12_05: Annotated[D_782, Title(''), Usage('N'), Position(5)]
    
    hi12_06: Annotated[D_380, Title(''), Usage('N'), Position(6)]
    
    hi12_07: Annotated[D_799, Title(''), Usage('N'), Position(7)]
    
    hi12_08: Annotated[D_1271, Title(''), Usage('N'), Position(8)]
    
    hi12_09: Annotated[D_1073, Title(''), Usage('N'), Position(9)]


class L2300_HI(Segment):
    """"""
    _segment_name = 'HI'
    
    hi01: Annotated[L2300_HI01, Title(''), Usage('R'), Position(1), Required(True)]
    
    hi02: Annotated[L2300_HI02, Title(''), Usage('S'), Position(2), Required(True)]
    
    hi03: Annotated[L2300_HI03, Title(''), Usage('S'), Position(3), Required(True)]
    
    hi04: Annotated[L2300_HI04, Title(''), Usage('S'), Position(4), Required(True)]
    
    hi05: Annotated[L2300_HI05, Title(''), Usage('S'), Position(5), Required(True)]
    
    hi06: Annotated[L2300_HI06, Title(''), Usage('S'), Position(6), Required(True)]
    
    hi07: Annotated[L2300_HI07, Title(''), Usage('S'), Position(7), Required(True)]
    
    hi08: Annotated[L2300_HI08, Title(''), Usage('S'), Position(8), Required(True)]
    
    hi09: Annotated[L2300_HI09, Title(''), Usage('S'), Position(9), Required(True)]
    
    hi10: Annotated[L2300_HI10, Title(''), Usage('S'), Position(10), Required(True)]
    
    hi11: Annotated[L2300_HI11, Title(''), Usage('S'), Position(11), Required(True)]
    
    hi12: Annotated[L2300_HI12, Title(''), Usage('S'), Position(12), Required(True)]


class L2300_HCP(Segment):
    """"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title(''), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title(''), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title(''), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title(''), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title(''), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title(''), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title(''), Usage('N'), Position(9)]
    
    hcp10: Annotated[D_234, Title(''), Usage('N'), Position(10)]
    
    hcp11: Annotated[D_355, Title(''), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title(''), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title(''), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title(''), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title(''), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2310A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['71'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310A_PRV05(Composite):
    """"""
    pass


class L2310A_PRV(Segment):
    """"""
    _segment_name = 'PRV'
    
    prv01: Annotated[D_1221, Title(''), Usage('R'), Position(1), Enumerated(*['AT'])]
    
    prv02: Annotated[D_128, Title(''), Usage('R'), Position(2), Enumerated(*['PXC'])]
    
    prv03: Annotated[D_127, Title(''), Usage('R'), Position(3)]
    
    prv04: Annotated[D_156, Title(''), Usage('N'), Position(4)]
    
    prv06: Annotated[D_1223, Title(''), Usage('N'), Position(6)]


class L2310A_REF04(Composite):
    """"""
    pass


class L2310A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310A(Loop):
    
    nm1: Annotated[L2310A_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    prv: Annotated[L2310A_PRV, Title(''), Usage('S'), Position(2550), Syntax(['P0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310A_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310B_REF04(Composite):
    """"""
    pass


class L2310B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310B(Loop):
    
    nm1: Annotated[L2310B_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310B_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310C_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310C_REF04(Composite):
    """"""
    pass


class L2310C_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310C(Loop):
    
    nm1: Annotated[L2310C_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310C_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310D_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310D_REF04(Composite):
    """"""
    pass


class L2310D_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310D(Loop):
    
    nm1: Annotated[L2310D_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310D_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2310E_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310E_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2310E_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2310E_REF04(Composite):
    """"""
    pass


class L2310E_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310E(Loop):
    
    nm1: Annotated[L2310E_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2310E_N3, Title(''), Usage('R'), Position(2650), Required(True)]
    
    n4: Annotated[L2310E_N4, Title(''), Usage('R'), Position(2700), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310E_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2310F_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['DN'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2310F_REF04(Composite):
    """"""
    pass


class L2310F_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2310F(Loop):
    
    nm1: Annotated[L2310F_NM1, Title(''), Usage('R'), Position(2500), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2310F_REF, Title(''), Usage('S'), Position(2710), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2320_SBR(Segment):
    """"""
    _segment_name = 'SBR'
    
    sbr01: Annotated[D_1138, Title(''), Usage('R'), Position(1), Enumerated(*['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'P', 'S', 'T', 'U'])]
    
    sbr02: Annotated[D_1069, Title(''), Usage('R'), Position(2), Enumerated(*['01', '18', '19', '20', '21', '39', '40', '53', 'G8'])]
    
    sbr03: Annotated[D_127, Title(''), Usage('S'), Position(3)]
    
    sbr04: Annotated[D_93, Title(''), Usage('S'), Position(4)]
    
    sbr05: Annotated[D_1336, Title(''), Usage('N'), Position(5)]
    
    sbr06: Annotated[D_1143, Title(''), Usage('N'), Position(6)]
    
    sbr07: Annotated[D_1073, Title(''), Usage('N'), Position(7)]
    
    sbr08: Annotated[D_584, Title(''), Usage('N'), Position(8)]
    
    sbr09: Annotated[D_1032, Title(''), Usage('S'), Position(9), Enumerated(*['11', '12', '13', '14', '15', '16', '17', 'AM', 'BL', 'CH', 'CI', 'DS', 'FI', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]


class L2320_CAS(Segment):
    """"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title(''), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title(''), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title(''), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title(''), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title(''), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title(''), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title(''), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title(''), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title(''), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title(''), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title(''), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title(''), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title(''), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title(''), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title(''), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title(''), Usage('S'), Position(19)]


class L2320_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['D'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2320_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['A8'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2320_OI(Segment):
    """"""
    _segment_name = 'OI'
    
    oi01: Annotated[D_1032, Title(''), Usage('N'), Position(1)]
    
    oi02: Annotated[D_1383, Title(''), Usage('N'), Position(2)]
    
    oi03: Annotated[D_1073, Title(''), Usage('R'), Position(3), Enumerated(*['N', 'W', 'Y'])]
    
    oi04: Annotated[D_1351, Title(''), Usage('N'), Position(4)]
    
    oi05: Annotated[D_1360, Title(''), Usage('N'), Position(5)]
    
    oi06: Annotated[D_1363, Title(''), Usage('R'), Position(6), Enumerated(*['I', 'Y'])]


class L2320_MIA(Segment):
    """"""
    _segment_name = 'MIA'
    
    mia01: Annotated[D_380, Title(''), Usage('R'), Position(1)]
    
    mia02: Annotated[D_782, Title(''), Usage('N'), Position(2)]
    
    mia03: Annotated[D_380, Title(''), Usage('S'), Position(3)]
    
    mia04: Annotated[D_782, Title(''), Usage('S'), Position(4)]
    
    mia05: Annotated[D_127, Title(''), Usage('S'), Position(5), Enumerated(*remark_code)]
    
    mia06: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    mia07: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    mia08: Annotated[D_782, Title(''), Usage('S'), Position(8)]
    
    mia09: Annotated[D_782, Title(''), Usage('S'), Position(9)]
    
    mia10: Annotated[D_782, Title(''), Usage('S'), Position(10)]
    
    mia11: Annotated[D_782, Title(''), Usage('S'), Position(11)]
    
    mia12: Annotated[D_782, Title(''), Usage('S'), Position(12)]
    
    mia13: Annotated[D_782, Title(''), Usage('S'), Position(13)]
    
    mia14: Annotated[D_782, Title(''), Usage('S'), Position(14)]
    
    mia15: Annotated[D_380, Title(''), Usage('S'), Position(15)]
    
    mia16: Annotated[D_782, Title(''), Usage('S'), Position(16)]
    
    mia17: Annotated[D_782, Title(''), Usage('S'), Position(17)]
    
    mia18: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    mia19: Annotated[D_782, Title(''), Usage('S'), Position(19)]
    
    mia20: Annotated[D_127, Title(''), Usage('S'), Position(20), Enumerated(*remark_code)]
    
    mia21: Annotated[D_127, Title(''), Usage('S'), Position(21), Enumerated(*remark_code)]
    
    mia22: Annotated[D_127, Title(''), Usage('S'), Position(22), Enumerated(*remark_code)]
    
    mia23: Annotated[D_127, Title(''), Usage('S'), Position(23), Enumerated(*remark_code)]
    
    mia24: Annotated[D_782, Title(''), Usage('S'), Position(24)]


class L2320_MOA(Segment):
    """"""
    _segment_name = 'MOA'
    
    moa01: Annotated[D_954, Title(''), Usage('S'), Position(1)]
    
    moa02: Annotated[D_782, Title(''), Usage('S'), Position(2)]
    
    moa03: Annotated[D_127, Title(''), Usage('S'), Position(3), Enumerated(*remark_code)]
    
    moa04: Annotated[D_127, Title(''), Usage('S'), Position(4), Enumerated(*remark_code)]
    
    moa05: Annotated[D_127, Title(''), Usage('S'), Position(5), Enumerated(*remark_code)]
    
    moa06: Annotated[D_127, Title(''), Usage('S'), Position(6), Enumerated(*remark_code)]
    
    moa07: Annotated[D_127, Title(''), Usage('S'), Position(7), Enumerated(*remark_code)]
    
    moa08: Annotated[D_782, Title(''), Usage('S'), Position(8)]
    
    moa09: Annotated[D_782, Title(''), Usage('S'), Position(9)]


class L2330A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['II', 'MI'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2330A_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2330A_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2330A_REF04(Composite):
    """"""
    pass


class L2330A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['SY'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330A(Loop):
    
    nm1: Annotated[L2330A_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330A_N3, Title(''), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330A_N4, Title(''), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330A_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2330B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['PI', 'XV'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2330B_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L2330B_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L2330B_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U', 'EI', 'FY', 'NF'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G1'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9F'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['T4'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B_REF04(Composite):
    """"""
    pass


class L2330B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['F8'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330B(Loop):
    
    nm1: Annotated[L2330B_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    n3: Annotated[L2330B_N3, Title(''), Usage('S'), Position(3320), Required(True)]
    
    n4: Annotated[L2330B_N4, Title(''), Usage('S'), Position(3400), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    dtp: Annotated[L2330B_DTP, Title(''), Usage('S'), Position(3500), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2330B_REF, Title(''), Usage('S'), Position(3550), Syntax(['R0203']), Required(True)]


class L2330C_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['71'])]
    
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


class L2330C_REF04(Composite):
    """"""
    pass


class L2330C_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330C(Loop):
    
    nm1: Annotated[L2330C_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330C_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330D_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['72'])]
    
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


class L2330D_REF04(Composite):
    """"""
    pass


class L2330D_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330D(Loop):
    
    nm1: Annotated[L2330D_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330D_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330E_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
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


class L2330E_REF04(Composite):
    """"""
    pass


class L2330E_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330E(Loop):
    
    nm1: Annotated[L2330E_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330E_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330F_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['77'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
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


class L2330F_REF04(Composite):
    """"""
    pass


class L2330F_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330F(Loop):
    
    nm1: Annotated[L2330F_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330F_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330G_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['82'])]
    
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


class L2330G_REF04(Composite):
    """"""
    pass


class L2330G_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330G(Loop):
    
    nm1: Annotated[L2330G_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330G_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]


class L2330H_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['DN'])]
    
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


class L2330H_REF04(Composite):
    """"""
    pass


class L2330H_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330H(Loop):
    
    nm1: Annotated[L2330H_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330H_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(3)]


class L2330I_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['85'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
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


class L2330I_REF04(Composite):
    """"""
    pass


class L2330I_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2330I(Loop):
    
    nm1: Annotated[L2330I_NM1, Title(''), Usage('R'), Position(3250), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2330I_REF, Title(''), Usage('R'), Position(3550), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(2)]


class L2320(Loop):
    
    sbr: Annotated[L2320_SBR, Title(''), Usage('R'), Position(2900), Required(True)]
    ItemCas: TypeAlias = Annotated[L2320_CAS, Title(''), Usage('S'), Position(2950), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    amt: Annotated[L2320_AMT, Title(''), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title(''), Usage('S'), Position(3000), Required(True)]
    
    amt: Annotated[L2320_AMT, Title(''), Usage('S'), Position(3000), Required(True)]
    
    oi: Annotated[L2320_OI, Title(''), Usage('R'), Position(3100), Required(True)]
    
    mia: Annotated[L2320_MIA, Title(''), Usage('S'), Position(3150), Required(True)]
    
    moa: Annotated[L2320_MOA, Title(''), Usage('S'), Position(3200)]
    ItemL2330A: TypeAlias = Annotated[L2330A, Title(''), Usage('R'), Position(3250), Required(True)]
    l2330a: Annotated[list[ItemL2330A], MinItems(1)]
    ItemL2330B: TypeAlias = Annotated[L2330B, Title(''), Usage('R'), Position(3250), Required(True)]
    l2330b: Annotated[list[ItemL2330B], MinItems(1)]
    ItemL2330C: TypeAlias = Annotated[L2330C, Title(''), Usage('S'), Position(3250), Required(True)]
    l2330c: Annotated[list[ItemL2330C], MinItems(1)]
    ItemL2330D: TypeAlias = Annotated[L2330D, Title(''), Usage('S'), Position(3600), Required(True)]
    l2330d: Annotated[list[ItemL2330D], MinItems(1)]
    ItemL2330E: TypeAlias = Annotated[L2330E, Title(''), Usage('S'), Position(3700), Required(True)]
    l2330e: Annotated[list[ItemL2330E], MinItems(1)]
    ItemL2330F: TypeAlias = Annotated[L2330F, Title(''), Usage('S'), Position(3900), Required(True)]
    l2330f: Annotated[list[ItemL2330F], MinItems(1)]
    ItemL2330G: TypeAlias = Annotated[L2330G, Title(''), Usage('S'), Position(4000), Required(True)]
    l2330g: Annotated[list[ItemL2330G], MinItems(1)]
    ItemL2330H: TypeAlias = Annotated[L2330H, Title(''), Usage('S'), Position(5000), Required(True)]
    l2330h: Annotated[list[ItemL2330H], MinItems(1)]
    ItemL2330I: TypeAlias = Annotated[L2330I, Title(''), Usage('S'), Position(6000), Required(True)]
    l2330i: Annotated[list[ItemL2330I], MinItems(1)]


class L2400_LX(Segment):
    """"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title(''), Usage('R'), Position(1)]


class L2400_SV202(Composite):
    """"""
    
    sv202_01: Annotated[D_235, Title(''), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'HP', 'IV', 'WK'])]
    
    sv202_02: Annotated[D_234, Title(''), Usage('R'), Position(2)]
    
    sv202_03: Annotated[D_1339, Title(''), Usage('S'), Position(3)]
    
    sv202_04: Annotated[D_1339, Title(''), Usage('S'), Position(4)]
    
    sv202_05: Annotated[D_1339, Title(''), Usage('S'), Position(5)]
    
    sv202_06: Annotated[D_1339, Title(''), Usage('S'), Position(6)]
    
    sv202_07: Annotated[D_352, Title(''), Usage('S'), Position(7)]
    
    sv202_08: Annotated[D_234, Title(''), Usage('N'), Position(8)]


class L2400_SV2(Segment):
    """"""
    _segment_name = 'SV2'
    
    sv201: Annotated[D_234, Title(''), Usage('R'), Position(1)]
    
    sv202: Annotated[L2400_SV202, Title(''), Usage('S'), Position(2), Required(True)]
    
    sv203: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    sv204: Annotated[D_355, Title(''), Usage('R'), Position(4), Enumerated(*['DA', 'UN'])]
    
    sv205: Annotated[D_380, Title(''), Usage('R'), Position(5)]
    
    sv206: Annotated[D_1371, Title(''), Usage('N'), Position(6)]
    
    sv207: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    sv208: Annotated[D_1073, Title(''), Usage('N'), Position(8)]
    
    sv209: Annotated[D_1345, Title(''), Usage('N'), Position(9)]
    
    sv210: Annotated[D_1337, Title(''), Usage('N'), Position(10)]


class L2400_PWK08(Composite):
    """"""
    pass


class L2400_PWK(Segment):
    """"""
    _segment_name = 'PWK'
    
    pwk01: Annotated[D_755, Title(''), Usage('R'), Position(1), Enumerated(*['03', '04', '05', '06', '07', '08', '09', '10', '11', '13', '15', '21', 'A3', 'A4', 'AM', 'AS', 'B2', 'B3', 'B4', 'BR', 'BS', 'BT', 'CB', 'CK', 'CT', 'D2', 'DA', 'DB', 'DG', 'DJ', 'DS', 'EB', 'HC', 'HR', 'I5', 'IR', 'LA', 'M1', 'MT', 'NN', 'OB', 'OC', 'OD', 'OE', 'OX', 'OZ', 'P4', 'P5', 'PE', 'PN', 'PO', 'PQ', 'PY', 'PZ', 'RB', 'RR', 'RT', 'RX', 'SG', 'V5', 'XP'])]
    
    pwk02: Annotated[D_756, Title(''), Usage('R'), Position(2), Enumerated(*['AA', 'BM', 'EL', 'EM', 'FT', 'FX'])]
    
    pwk03: Annotated[D_757, Title(''), Usage('N'), Position(3)]
    
    pwk04: Annotated[D_98, Title(''), Usage('N'), Position(4)]
    
    pwk05: Annotated[D_66, Title(''), Usage('S'), Position(5), Enumerated(*['AC'])]
    
    pwk06: Annotated[D_67, Title(''), Usage('S'), Position(6)]
    
    pwk07: Annotated[D_352, Title(''), Usage('N'), Position(7)]
    
    pwk09: Annotated[D_1525, Title(''), Usage('N'), Position(9)]


class L2400_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['472'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8', 'RD8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2400_REF04(Composite):
    """"""
    pass


class L2400_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['6R'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """"""
    pass


class L2400_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9B'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2400_REF04(Composite):
    """"""
    pass


class L2400_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['9D'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['GT'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2400_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['N8'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2400_NTE(Segment):
    """"""
    _segment_name = 'NTE'
    
    nte01: Annotated[D_363, Title(''), Usage('R'), Position(1), Enumerated(*['TPO'])]
    
    nte02: Annotated[D_352, Title(''), Usage('R'), Position(2)]


class L2400_HCP(Segment):
    """"""
    _segment_name = 'HCP'
    
    hcp01: Annotated[D_1473, Title(''), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'])]
    
    hcp02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    hcp03: Annotated[D_782, Title(''), Usage('S'), Position(3)]
    
    hcp04: Annotated[D_127, Title(''), Usage('S'), Position(4)]
    
    hcp05: Annotated[D_118, Title(''), Usage('S'), Position(5)]
    
    hcp06: Annotated[D_127, Title(''), Usage('S'), Position(6)]
    
    hcp07: Annotated[D_782, Title(''), Usage('S'), Position(7)]
    
    hcp08: Annotated[D_234, Title(''), Usage('S'), Position(8)]
    
    hcp09: Annotated[D_235, Title(''), Usage('S'), Position(9), Enumerated(*['ER', 'HC', 'HP', 'IV', 'WK'])]
    
    hcp10: Annotated[D_234, Title(''), Usage('S'), Position(10)]
    
    hcp11: Annotated[D_355, Title(''), Usage('S'), Position(11), Enumerated(*['DA', 'UN'])]
    
    hcp12: Annotated[D_380, Title(''), Usage('S'), Position(12)]
    
    hcp13: Annotated[D_901, Title(''), Usage('S'), Position(13), Enumerated(*['T1', 'T2', 'T3', 'T4', 'T5', 'T6'])]
    
    hcp14: Annotated[D_1526, Title(''), Usage('S'), Position(14), Enumerated(*['1', '2', '3', '4', '5'])]
    
    hcp15: Annotated[D_1527, Title(''), Usage('S'), Position(15), Enumerated(*['1', '2', '3', '4', '5', '6'])]


class L2410_LIN(Segment):
    """"""
    _segment_name = 'LIN'
    
    lin01: Annotated[D_350, Title(''), Usage('N'), Position(1)]
    
    lin02: Annotated[D_235, Title(''), Usage('R'), Position(2), Enumerated(*['N4'])]
    
    lin03: Annotated[D_234, Title(''), Usage('R'), Position(3)]
    
    lin04: Annotated[D_235, Title(''), Usage('N'), Position(4)]
    
    lin05: Annotated[D_234, Title(''), Usage('N'), Position(5)]
    
    lin06: Annotated[D_235, Title(''), Usage('N'), Position(6)]
    
    lin07: Annotated[D_234, Title(''), Usage('N'), Position(7)]
    
    lin08: Annotated[D_235, Title(''), Usage('N'), Position(8)]
    
    lin09: Annotated[D_234, Title(''), Usage('N'), Position(9)]
    
    lin10: Annotated[D_235, Title(''), Usage('N'), Position(10)]
    
    lin11: Annotated[D_234, Title(''), Usage('N'), Position(11)]
    
    lin12: Annotated[D_235, Title(''), Usage('N'), Position(12)]
    
    lin13: Annotated[D_234, Title(''), Usage('N'), Position(13)]
    
    lin14: Annotated[D_235, Title(''), Usage('N'), Position(14)]
    
    lin15: Annotated[D_234, Title(''), Usage('N'), Position(15)]
    
    lin16: Annotated[D_235, Title(''), Usage('N'), Position(16)]
    
    lin17: Annotated[D_234, Title(''), Usage('N'), Position(17)]
    
    lin18: Annotated[D_235, Title(''), Usage('N'), Position(18)]
    
    lin19: Annotated[D_234, Title(''), Usage('N'), Position(19)]
    
    lin20: Annotated[D_235, Title(''), Usage('N'), Position(20)]
    
    lin21: Annotated[D_234, Title(''), Usage('N'), Position(21)]
    
    lin22: Annotated[D_235, Title(''), Usage('N'), Position(22)]
    
    lin23: Annotated[D_234, Title(''), Usage('N'), Position(23)]
    
    lin24: Annotated[D_235, Title(''), Usage('N'), Position(24)]
    
    lin25: Annotated[D_234, Title(''), Usage('N'), Position(25)]
    
    lin26: Annotated[D_235, Title(''), Usage('N'), Position(26)]
    
    lin27: Annotated[D_234, Title(''), Usage('N'), Position(27)]
    
    lin28: Annotated[D_235, Title(''), Usage('N'), Position(28)]
    
    lin29: Annotated[D_234, Title(''), Usage('N'), Position(29)]
    
    lin30: Annotated[D_235, Title(''), Usage('N'), Position(30)]
    
    lin31: Annotated[D_234, Title(''), Usage('N'), Position(31)]


class L2410_CTP05(Composite):
    """"""
    
    ctp05_01: Annotated[D_355, Title(''), Usage('R'), Position(1), Enumerated(*['F2', 'GR', 'ME', 'ML', 'UN'])]
    
    ctp05_02: Annotated[D_1018, Title(''), Usage('N'), Position(2)]
    
    ctp05_03: Annotated[D_649, Title(''), Usage('N'), Position(3)]
    
    ctp05_04: Annotated[D_355, Title(''), Usage('N'), Position(4)]
    
    ctp05_05: Annotated[D_1018, Title(''), Usage('N'), Position(5)]
    
    ctp05_06: Annotated[D_649, Title(''), Usage('N'), Position(6)]
    
    ctp05_07: Annotated[D_355, Title(''), Usage('N'), Position(7)]
    
    ctp05_08: Annotated[D_1018, Title(''), Usage('N'), Position(8)]
    
    ctp05_09: Annotated[D_649, Title(''), Usage('N'), Position(9)]
    
    ctp05_10: Annotated[D_355, Title(''), Usage('N'), Position(10)]
    
    ctp05_11: Annotated[D_1018, Title(''), Usage('N'), Position(11)]
    
    ctp05_12: Annotated[D_649, Title(''), Usage('N'), Position(12)]
    
    ctp05_13: Annotated[D_355, Title(''), Usage('N'), Position(13)]
    
    ctp05_14: Annotated[D_1018, Title(''), Usage('N'), Position(14)]
    
    ctp05_15: Annotated[D_649, Title(''), Usage('N'), Position(15)]


class L2410_CTP(Segment):
    """"""
    _segment_name = 'CTP'
    
    ctp01: Annotated[D_687, Title(''), Usage('N'), Position(1)]
    
    ctp02: Annotated[D_236, Title(''), Usage('N'), Position(2)]
    
    ctp03: Annotated[D_212, Title(''), Usage('N'), Position(3)]
    
    ctp04: Annotated[D_380, Title(''), Usage('R'), Position(4)]
    
    ctp05: Annotated[L2410_CTP05, Title(''), Usage('R'), Position(5), Required(True)]
    
    ctp06: Annotated[D_648, Title(''), Usage('N'), Position(6)]
    
    ctp07: Annotated[D_649, Title(''), Usage('N'), Position(7)]
    
    ctp08: Annotated[D_782, Title(''), Usage('N'), Position(8)]
    
    ctp09: Annotated[D_639, Title(''), Usage('N'), Position(9)]
    
    ctp10: Annotated[D_499, Title(''), Usage('N'), Position(10)]
    
    ctp11: Annotated[D_289, Title(''), Usage('N'), Position(11)]


class L2410_REF04(Composite):
    """"""
    pass


class L2410_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['VY', 'XZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2410(Loop):
    
    lin: Annotated[L2410_LIN, Title(''), Usage('R'), Position(4930), Syntax(['P0405', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425', 'P2627', 'P2829', 'P3031']), Required(True)]
    
    ctp: Annotated[L2410_CTP, Title(''), Usage('R'), Position(4940), Syntax(['P0405', 'C0607', 'C0902', 'C1002', 'C1103']), Required(True)]
    
    ref: Annotated[L2410_REF, Title(''), Usage('S'), Position(4950), Syntax(['R0203']), Required(True)]


class L2420A_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['72'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420A_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420A_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420A(Loop):
    
    nm1: Annotated[L2420A_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420A_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['ZZ'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420B_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420B_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420B(Loop):
    
    nm1: Annotated[L2420B_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420B_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420C_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420C_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420C_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420C_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420C(Loop):
    
    nm1: Annotated[L2420C_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420C_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2420D_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['DN'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2420D_REF04(Composite):
    """"""
    
    ref04_01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U'])]
    
    ref04_02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref04_03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    ref04_04: Annotated[D_127, Title(''), Usage('N'), Position(4)]
    
    ref04_05: Annotated[D_128, Title(''), Usage('N'), Position(5)]
    
    ref04_06: Annotated[D_127, Title(''), Usage('N'), Position(6)]


class L2420D_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1G', 'G2'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]
    
    ref04: Annotated[L2420D_REF04, Title(''), Usage('S'), Position(4), Required(True)]


class L2420D(Loop):
    
    nm1: Annotated[L2420D_NM1, Title(''), Usage('R'), Position(5000), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2420D_REF, Title(''), Usage('S'), Position(5250), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(20)]


class L2430_SVD03(Composite):
    """"""
    
    svd03_01: Annotated[D_235, Title(''), Usage('R'), Position(1), Enumerated(*['ER', 'HC', 'HP', 'IV', 'WK'])]
    
    svd03_02: Annotated[D_234, Title(''), Usage('R'), Position(2)]
    
    svd03_03: Annotated[D_1339, Title(''), Usage('S'), Position(3)]
    
    svd03_04: Annotated[D_1339, Title(''), Usage('S'), Position(4)]
    
    svd03_05: Annotated[D_1339, Title(''), Usage('S'), Position(5)]
    
    svd03_06: Annotated[D_1339, Title(''), Usage('S'), Position(6)]
    
    svd03_07: Annotated[D_352, Title(''), Usage('S'), Position(7)]
    
    svd03_08: Annotated[D_234, Title(''), Usage('N'), Position(8)]


class L2430_SVD(Segment):
    """"""
    _segment_name = 'SVD'
    
    svd01: Annotated[D_67, Title(''), Usage('R'), Position(1)]
    
    svd02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    svd03: Annotated[L2430_SVD03, Title(''), Usage('S'), Position(3), Required(True)]
    
    svd04: Annotated[D_234, Title(''), Usage('R'), Position(4)]
    
    svd05: Annotated[D_380, Title(''), Usage('R'), Position(5)]
    
    svd06: Annotated[D_554, Title(''), Usage('S'), Position(6)]


class L2430_CAS(Segment):
    """"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title(''), Usage('R'), Position(1), Enumerated(*['CO', 'CR', 'OA', 'PI', 'PR'])]
    
    cas02: Annotated[D_1034, Title(''), Usage('R'), Position(2)]
    
    cas03: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    cas04: Annotated[D_380, Title(''), Usage('S'), Position(4)]
    
    cas05: Annotated[D_1034, Title(''), Usage('S'), Position(5)]
    
    cas06: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    cas07: Annotated[D_380, Title(''), Usage('S'), Position(7)]
    
    cas08: Annotated[D_1034, Title(''), Usage('S'), Position(8)]
    
    cas09: Annotated[D_782, Title(''), Usage('S'), Position(9)]
    
    cas10: Annotated[D_380, Title(''), Usage('S'), Position(10)]
    
    cas11: Annotated[D_1034, Title(''), Usage('S'), Position(11)]
    
    cas12: Annotated[D_782, Title(''), Usage('S'), Position(12)]
    
    cas13: Annotated[D_380, Title(''), Usage('S'), Position(13)]
    
    cas14: Annotated[D_1034, Title(''), Usage('S'), Position(14)]
    
    cas15: Annotated[D_782, Title(''), Usage('S'), Position(15)]
    
    cas16: Annotated[D_380, Title(''), Usage('S'), Position(16)]
    
    cas17: Annotated[D_1034, Title(''), Usage('S'), Position(17)]
    
    cas18: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    cas19: Annotated[D_380, Title(''), Usage('S'), Position(19)]


class L2430_DTP(Segment):
    """"""
    _segment_name = 'DTP'
    
    dtp01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['573'])]
    
    dtp02: Annotated[D_1250, Title(''), Usage('R'), Position(2), Enumerated(*['D8'])]
    
    dtp03: Annotated[D_1251, Title(''), Usage('R'), Position(3)]


class L2430_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['EAF'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2430(Loop):
    
    svd: Annotated[L2430_SVD, Title(''), Usage('R'), Position(5400), Required(True)]
    ItemCas: TypeAlias = Annotated[L2430_CAS, Title(''), Usage('S'), Position(5450), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(5)]
    
    dtp: Annotated[L2430_DTP, Title(''), Usage('R'), Position(5500), Required(True)]
    
    amt: Annotated[L2430_AMT, Title(''), Usage('S'), Position(5505), Required(True)]


class L2400(Loop):
    
    lx: Annotated[L2400_LX, Title(''), Usage('R'), Position(3650), Required(True)]
    
    sv2: Annotated[L2400_SV2, Title(''), Usage('R'), Position(3750), Syntax(['R0102', 'P0405']), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2400_PWK, Title(''), Usage('S'), Position(4200), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    dtp: Annotated[L2400_DTP, Title(''), Usage('S'), Position(4550), Required(True)]
    
    ref: Annotated[L2400_REF, Title(''), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title(''), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2400_REF, Title(''), Usage('S'), Position(4700), Syntax(['R0203']), Required(True)]
    
    amt: Annotated[L2400_AMT, Title(''), Usage('S'), Position(4750), Required(True)]
    
    amt: Annotated[L2400_AMT, Title(''), Usage('S'), Position(4750), Required(True)]
    
    nte: Annotated[L2400_NTE, Title(''), Usage('S'), Position(4850), Required(True)]
    
    hcp: Annotated[L2400_HCP, Title(''), Usage('S'), Position(4920), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2410: TypeAlias = Annotated[L2410, Title(''), Usage('S'), Position(4940), Required(True)]
    l2410: Annotated[list[ItemL2410], MinItems(1)]
    ItemL2420A: TypeAlias = Annotated[L2420A, Title(''), Usage('S'), Position(5000), Required(True)]
    l2420a: Annotated[list[ItemL2420A], MinItems(1)]
    ItemL2420B: TypeAlias = Annotated[L2420B, Title(''), Usage('S'), Position(5000), Required(True)]
    l2420b: Annotated[list[ItemL2420B], MinItems(1)]
    ItemL2420C: TypeAlias = Annotated[L2420C, Title(''), Usage('S'), Position(5000), Required(True)]
    l2420c: Annotated[list[ItemL2420C], MinItems(1)]
    ItemL2420D: TypeAlias = Annotated[L2420D, Title(''), Usage('S'), Position(5300), Required(True)]
    l2420d: Annotated[list[ItemL2420D], MinItems(1)]
    ItemL2430: TypeAlias = Annotated[L2430, Title(''), Usage('S'), Position(5400), Required(True)]
    l2430: Annotated[list[ItemL2430], MinItems(15)]


class L2300(Loop):
    
    clm: Annotated[L2300_CLM, Title(''), Usage('R'), Position(1300), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('R'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('S'), Position(1350), Required(True)]
    
    dtp: Annotated[L2300_DTP, Title(''), Usage('S'), Position(1350), Required(True)]
    
    cl1: Annotated[L2300_CL1, Title(''), Usage('R'), Position(1400), Required(True)]
    ItemPwk: TypeAlias = Annotated[L2300_PWK, Title(''), Usage('S'), Position(1550), Syntax(['P0506']), Required(True)]
    pwk: Annotated[list[ItemPwk], MaxItems(10)]
    
    cn1: Annotated[L2300_CN1, Title(''), Usage('S'), Position(1600), Required(True)]
    
    amt: Annotated[L2300_AMT, Title(''), Usage('S'), Position(1750), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[L2300_REF, Title(''), Usage('S'), Position(1800), Syntax(['R0203']), Required(True)]
    ItemK3: TypeAlias = Annotated[L2300_K3, Title(''), Usage('S'), Position(1850), Required(True)]
    k3: Annotated[list[ItemK3], MaxItems(10)]
    ItemNte: TypeAlias = Annotated[L2300_NTE, Title(''), Usage('S'), Position(1900), Required(True)]
    nte: Annotated[list[ItemNte], MaxItems(10)]
    
    nte: Annotated[L2300_NTE, Title(''), Usage('S'), Position(1900), Required(True)]
    
    crc: Annotated[L2300_CRC, Title(''), Usage('S'), Position(2200), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('R'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hi: Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    ItemHi: TypeAlias = Annotated[L2300_HI, Title(''), Usage('S'), Position(2310), Required(True)]
    hi: Annotated[list[ItemHi], MaxItems(2)]
    
    hcp: Annotated[L2300_HCP, Title(''), Usage('S'), Position(2410), Syntax(['R0113', 'P0910', 'P1112']), Required(True)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(1)]
    ItemL2310B: TypeAlias = Annotated[L2310B, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310b: Annotated[list[ItemL2310B], MinItems(1)]
    ItemL2310C: TypeAlias = Annotated[L2310C, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310c: Annotated[list[ItemL2310C], MinItems(1)]
    ItemL2310D: TypeAlias = Annotated[L2310D, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310d: Annotated[list[ItemL2310D], MinItems(1)]
    ItemL2310E: TypeAlias = Annotated[L2310E, Title(''), Usage('S'), Position(2500), Required(True)]
    l2310e: Annotated[list[ItemL2310E], MinItems(1)]
    ItemL2310F: TypeAlias = Annotated[L2310F, Title(''), Usage('S'), Position(2800), Required(True)]
    l2310f: Annotated[list[ItemL2310F], MinItems(1)]
    ItemL2320: TypeAlias = Annotated[L2320, Title(''), Usage('S'), Position(2900), Required(True)]
    l2320: Annotated[list[ItemL2320], MinItems(10)]
    ItemL2400: TypeAlias = Annotated[L2400, Title(''), Usage('R'), Position(3650), Required(True)]
    l2400: Annotated[list[ItemL2400], MinItems(999)]


class L2000C(Loop):
    
    hl: Annotated[L2000C_HL, Title(''), Usage('R'), Position(10), Required(True)]
    
    pat: Annotated[L2000C_PAT, Title(''), Usage('R'), Position(70), Syntax(['P0506', 'P0708']), Required(True)]
    ItemL2010Ca: TypeAlias = Annotated[L2010CA, Title(''), Usage('R'), Position(150), Required(True)]
    l2010ca: Annotated[list[ItemL2010Ca], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title(''), Usage('R'), Position(1300), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(100)]


class L2000B(Loop):
    
    hl: Annotated[L2000B_HL, Title(''), Usage('R'), Position(10), Required(True)]
    
    sbr: Annotated[L2000B_SBR, Title(''), Usage('R'), Position(50), Required(True)]
    ItemL2010Ba: TypeAlias = Annotated[L2010BA, Title(''), Usage('R'), Position(150), Required(True)]
    l2010ba: Annotated[list[ItemL2010Ba], MinItems(1)]
    ItemL2010Bb: TypeAlias = Annotated[L2010BB, Title(''), Usage('R'), Position(150), Required(True)]
    l2010bb: Annotated[list[ItemL2010Bb], MinItems(1)]
    ItemL2300: TypeAlias = Annotated[L2300, Title(''), Usage('R'), Position(1300), Required(True)]
    l2300: Annotated[list[ItemL2300], MinItems(100)]
    ItemL2000C: TypeAlias = Annotated[L2000C, Title(''), Usage('S'), Position(200), Required(True)]
    l2000c: Annotated[list[ItemL2000C], MinItems(1)]


class L2000A(Loop):
    
    hl: Annotated[L2000A_HL, Title(''), Usage('R'), Position(10), Required(True)]
    
    prv: Annotated[L2000A_PRV, Title(''), Usage('S'), Position(30), Syntax(['P0203']), Required(True)]
    
    cur: Annotated[L2000A_CUR, Title(''), Usage('S'), Position(100), Syntax(['C0807', 'C0907', 'L101112', 'C1110', 'C1210', 'L131415', 'C1413', 'C1513', 'L161718', 'C1716', 'C1816', 'L192021', 'C2019', 'C2119']), Required(True)]
    ItemL2010Aa: TypeAlias = Annotated[L2010AA, Title(''), Usage('R'), Position(150), Required(True)]
    l2010aa: Annotated[list[ItemL2010Aa], MinItems(1)]
    ItemL2010Ab: TypeAlias = Annotated[L2010AB, Title(''), Usage('S'), Position(150), Required(True)]
    l2010ab: Annotated[list[ItemL2010Ab], MinItems(1)]
    ItemL2010Ac: TypeAlias = Annotated[L2010AC, Title(''), Usage('S'), Position(500), Required(True)]
    l2010ac: Annotated[list[ItemL2010Ac], MinItems(1)]
    ItemL2000B: TypeAlias = Annotated[L2000B, Title(''), Usage('R'), Position(700), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class DETAIL(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title(''), Usage('R'), Position(10), Required(True)]
    l2000a: Annotated[list[ItemL2000A], MinItems(1)]


class ST_LOOP_SE(Segment):
    """"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title(''), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title(''), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title(''), Usage('R'), Position(50), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title(''), Usage('R'), Position(110), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title(''), Usage('R'), Position(120), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title(''), Usage('R'), Position(5550), Required(True)]


class MSG837Q3(Message):
    """HIPAA Health Care Claim - Institutional 005010X223A2 837Q3"""
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title(''), Usage('R'), Position(200), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
