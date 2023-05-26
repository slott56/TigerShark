"""
820.5010.X218.v2
Created 2023-05-19 10:17:35.935546
"""
from .base import *
from .common import *


class ST_LOOP_ST(Segment):
    """"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title(''), Usage('R'), Position(1), Enumerated(*['820'])]
    
    st02: Annotated[D_329, Title(''), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title(''), Usage('R'), Position(3), Enumerated(*['005010X218'])]


class HEADER_BPR(Segment):
    """"""
    _segment_name = 'BPR'
    
    bpr01: Annotated[D_305, Title(''), Usage('R'), Position(1), Enumerated(*['C', 'D', 'I', 'P', 'U', 'X'])]
    
    bpr02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    bpr03: Annotated[D_478, Title(''), Usage('R'), Position(3), Enumerated(*['C'])]
    
    bpr04: Annotated[D_591, Title(''), Usage('R'), Position(4), Enumerated(*['ACH', 'BOP', 'CHK', 'FWT', 'NON', 'SWT'])]
    
    bpr05: Annotated[D_812, Title(''), Usage('S'), Position(5), Enumerated(*['CCP', 'CTX'])]
    
    bpr06: Annotated[D_506, Title(''), Usage('S'), Position(6), Enumerated(*['01', '02', '04'])]
    
    bpr07: Annotated[D_507, Title(''), Usage('S'), Position(7)]
    
    bpr08: Annotated[D_569, Title(''), Usage('S'), Position(8), Enumerated(*['ALC', 'DA'])]
    
    bpr09: Annotated[D_508, Title(''), Usage('S'), Position(9)]
    
    bpr10: Annotated[D_509, Title(''), Usage('R'), Position(10)]
    
    bpr11: Annotated[D_510, Title(''), Usage('S'), Position(11)]
    
    bpr12: Annotated[D_506, Title(''), Usage('S'), Position(12), Enumerated(*['01', '02', '04'])]
    
    bpr13: Annotated[D_507, Title(''), Usage('S'), Position(13)]
    
    bpr14: Annotated[D_569, Title(''), Usage('S'), Position(14), Enumerated(*['DA', 'SG'])]
    
    bpr15: Annotated[D_508, Title(''), Usage('S'), Position(15)]
    
    bpr16: Annotated[D_373, Title(''), Usage('R'), Position(16)]
    
    bpr17: Annotated[D_1048, Title(''), Usage('N'), Position(17)]
    
    bpr18: Annotated[D_506, Title(''), Usage('N'), Position(18)]
    
    bpr19: Annotated[D_507, Title(''), Usage('N'), Position(19)]
    
    bpr20: Annotated[D_569, Title(''), Usage('N'), Position(20)]
    
    bpr21: Annotated[D_508, Title(''), Usage('N'), Position(21)]


class HEADER_TRN(Segment):
    """"""
    _segment_name = 'TRN'
    
    trn01: Annotated[D_481, Title(''), Usage('R'), Position(1), Enumerated(*['1', '3'])]
    
    trn02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title(''), Usage('S'), Position(3)]
    
    trn04: Annotated[D_127, Title(''), Usage('S'), Position(4)]


class HEADER_CUR(Segment):
    """"""
    _segment_name = 'CUR'
    
    cur01: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['2B', 'PR'])]
    
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


class HEADER_REF04(Composite):
    """"""
    pass


class HEADER_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['14', '17', '18', '2F', '38', '72', 'LB'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class HEADER_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['009'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class HEADER_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['035'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class HEADER_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['582'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('N'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('R'), Position(5), Enumerated(*['RD8'])]
    
    dtm06: Annotated[D_1251, Title(''), Usage('R'), Position(6)]


class HEADER_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['097'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class L1000A_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    n102: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('S'), Position(3), Enumerated(*['1', '9', 'EQ', 'FI', 'XV'])]
    
    n104: Annotated[D_67, Title(''), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


class L1000A_N2(Segment):
    """"""
    _segment_name = 'N2'
    
    n201: Annotated[D_93, Title(''), Usage('R'), Position(1)]
    
    n202: Annotated[D_93, Title(''), Usage('N'), Position(2)]


class L1000A_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L1000A_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L1000A_RDM04(Composite):
    """"""
    pass


class L1000A_RDM05(Composite):
    """"""
    pass


class L1000A_RDM(Segment):
    """"""
    _segment_name = 'RDM'
    
    rdm01: Annotated[D_756, Title(''), Usage('R'), Position(1), Enumerated(*['BM', 'EM', 'FT', 'FX', 'IA', 'OL'])]
    
    rdm02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    rdm03: Annotated[D_364, Title(''), Usage('S'), Position(3)]


class L1000A(Loop):
    
    n1: Annotated[L1000A_N1, Title(''), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    
    n2: Annotated[L1000A_N2, Title(''), Usage('S'), Position(800), Required(True)]
    
    n3: Annotated[L1000A_N3, Title(''), Usage('S'), Position(900), Required(True)]
    
    n4: Annotated[L1000A_N4, Title(''), Usage('S'), Position(1000), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    
    rdm: Annotated[L1000A_RDM, Title(''), Usage('S'), Position(1300), Required(True)]


class L1000B_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    n102: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('S'), Position(3), Enumerated(*['1', '24', '75', '9', 'EQ', 'FI', 'PI'])]
    
    n104: Annotated[D_67, Title(''), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


class L1000B_N2(Segment):
    """"""
    _segment_name = 'N2'
    
    n201: Annotated[D_93, Title(''), Usage('R'), Position(1)]
    
    n202: Annotated[D_93, Title(''), Usage('N'), Position(2)]


class L1000B_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L1000B_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L1000B_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title(''), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L1000B(Loop):
    
    n1: Annotated[L1000B_N1, Title(''), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    
    n2: Annotated[L1000B_N2, Title(''), Usage('S'), Position(800), Required(True)]
    
    n3: Annotated[L1000B_N3, Title(''), Usage('S'), Position(900), Required(True)]
    
    n4: Annotated[L1000B_N4, Title(''), Usage('S'), Position(1000), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000B_PER, Title(''), Usage('S'), Position(1200), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MinItems(1)]


class L1000C_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['04', '0B', '8W', 'AK', 'BE', 'BK', 'C1', 'C2', 'IAT', 'MJ', 'RB', 'Z6', 'ZB', 'ZL'])]
    
    n102: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('S'), Position(3), Enumerated(*['31', '57', '94', 'A3', 'A4', 'A6', 'CF', 'G', 'PA'])]
    
    n104: Annotated[D_67, Title(''), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


class L1000C_N2(Segment):
    """"""
    _segment_name = 'N2'
    
    n201: Annotated[D_93, Title(''), Usage('R'), Position(1)]
    
    n202: Annotated[D_93, Title(''), Usage('N'), Position(2)]


class L1000C_N3(Segment):
    """"""
    _segment_name = 'N3'
    
    n301: Annotated[D_166, Title(''), Usage('R'), Position(1)]
    
    n302: Annotated[D_166, Title(''), Usage('S'), Position(2)]


class L1000C_N4(Segment):
    """"""
    _segment_name = 'N4'
    
    n401: Annotated[D_19, Title(''), Usage('R'), Position(1)]
    
    n402: Annotated[D_156, Title(''), Usage('S'), Position(2), Enumerated(*states)]
    
    n403: Annotated[D_116, Title(''), Usage('S'), Position(3)]
    
    n404: Annotated[D_26, Title(''), Usage('S'), Position(4), Enumerated(*country)]
    
    n405: Annotated[D_309, Title(''), Usage('N'), Position(5)]
    
    n406: Annotated[D_310, Title(''), Usage('N'), Position(6)]
    
    n407: Annotated[D_1715, Title(''), Usage('S'), Position(7)]


class L1000C_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title(''), Usage('R'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L1000C(Loop):
    
    n1: Annotated[L1000C_N1, Title(''), Usage('R'), Position(700), Syntax(['R0203', 'P0304']), Required(True)]
    
    n2: Annotated[L1000C_N2, Title(''), Usage('S'), Position(800), Required(True)]
    
    n3: Annotated[L1000C_N3, Title(''), Usage('S'), Position(900), Required(True)]
    
    n4: Annotated[L1000C_N4, Title(''), Usage('S'), Position(1000), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000C_PER, Title(''), Usage('S'), Position(1200), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MinItems(1)]


class HEADER(Loop):
    
    bpr: Annotated[HEADER_BPR, Title(''), Usage('R'), Position(200), Syntax(['P0607', 'C0809', 'P1213', 'C1415', 'P1819', 'C2021']), Required(True)]
    
    trn: Annotated[HEADER_TRN, Title(''), Usage('R'), Position(350), Required(True)]
    
    cur: Annotated[HEADER_CUR, Title(''), Usage('S'), Position(400), Syntax(['C0807', 'C0907', 'L101112', 'C1110', 'C1210', 'L131415', 'C1413', 'C1513', 'L161718', 'C1716', 'C1816', 'L192021', 'C2019', 'C2119']), Required(True)]
    ItemRef: TypeAlias = Annotated[HEADER_REF, Title(''), Usage('S'), Position(500), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]
    
    dtm: Annotated[HEADER_DTM, Title(''), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title(''), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title(''), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title(''), Usage('S'), Position(600), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title(''), Usage('R'), Position(700), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title(''), Usage('R'), Position(1500), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]
    ItemL1000C: TypeAlias = Annotated[L1000C, Title(''), Usage('S'), Position(2300), Required(True)]
    l1000c: Annotated[list[ItemL1000C], MinItems(14)]


class L2000A_ENT(Segment):
    """"""
    _segment_name = 'ENT'
    
    ent01: Annotated[D_554, Title(''), Usage('R'), Position(1)]
    
    ent02: Annotated[D_98, Title(''), Usage('R'), Position(2), Enumerated(*['2L', 'AG', 'NH', 'RGA', 'UN'])]
    
    ent03: Annotated[D_66, Title(''), Usage('R'), Position(3), Enumerated(*['1', '24', '9', 'FI'])]
    
    ent04: Annotated[D_67, Title(''), Usage('R'), Position(4)]
    
    ent05: Annotated[D_98, Title(''), Usage('N'), Position(5)]
    
    ent06: Annotated[D_66, Title(''), Usage('N'), Position(6)]
    
    ent07: Annotated[D_67, Title(''), Usage('N'), Position(7)]
    
    ent08: Annotated[D_128, Title(''), Usage('N'), Position(8)]
    
    ent09: Annotated[D_127, Title(''), Usage('N'), Position(9)]


class L2200A_ADX(Segment):
    """"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title(''), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title(''), Usage('R'), Position(2), Enumerated(*['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6', 'RU', 'WO', 'WW'])]
    
    adx03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title(''), Usage('N'), Position(4)]


class L2200A(Loop):
    
    adx: Annotated[L2200A_ADX, Title(''), Usage('R'), Position(800), Syntax(['P0304']), Required(True)]


class L2300A_RMR(Segment):
    """"""
    _segment_name = 'RMR'
    
    rmr01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['11', '1L', 'CT', 'IK'])]
    
    rmr02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    rmr03: Annotated[D_482, Title(''), Usage('S'), Position(3), Enumerated(*['PA', 'PI', 'PO', 'PP'])]
    
    rmr04: Annotated[D_782, Title(''), Usage('R'), Position(4)]
    
    rmr05: Annotated[D_782, Title(''), Usage('S'), Position(5)]
    
    rmr06: Annotated[D_782, Title(''), Usage('N'), Position(6)]
    
    rmr07: Annotated[D_426, Title(''), Usage('N'), Position(7)]
    
    rmr08: Annotated[D_782, Title(''), Usage('N'), Position(8)]


class L2300A_REF04(Composite):
    """"""
    pass


class L2300A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['14', '17', '18', '2F', '38', 'E9', 'LB', 'LU', 'ZZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300A_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['582', 'AAG'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('S'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('S'), Position(5), Enumerated(*['RD8'])]
    
    dtm06: Annotated[D_1251, Title(''), Usage('S'), Position(6)]


class L2310A_IT1(Segment):
    """"""
    _segment_name = 'IT1'
    
    it101: Annotated[D_350, Title(''), Usage('R'), Position(1)]
    
    it102: Annotated[D_358, Title(''), Usage('N'), Position(2)]
    
    it103: Annotated[D_355, Title(''), Usage('N'), Position(3)]
    
    it104: Annotated[D_212, Title(''), Usage('N'), Position(4)]
    
    it105: Annotated[D_639, Title(''), Usage('N'), Position(5)]
    
    it106: Annotated[D_235, Title(''), Usage('N'), Position(6)]
    
    it107: Annotated[D_234, Title(''), Usage('N'), Position(7)]
    
    it108: Annotated[D_235, Title(''), Usage('N'), Position(8)]
    
    it109: Annotated[D_234, Title(''), Usage('N'), Position(9)]
    
    it110: Annotated[D_235, Title(''), Usage('N'), Position(10)]
    
    it111: Annotated[D_234, Title(''), Usage('N'), Position(11)]
    
    it112: Annotated[D_235, Title(''), Usage('N'), Position(12)]
    
    it113: Annotated[D_234, Title(''), Usage('N'), Position(13)]
    
    it114: Annotated[D_235, Title(''), Usage('N'), Position(14)]
    
    it115: Annotated[D_234, Title(''), Usage('N'), Position(15)]
    
    it116: Annotated[D_235, Title(''), Usage('N'), Position(16)]
    
    it117: Annotated[D_234, Title(''), Usage('N'), Position(17)]
    
    it118: Annotated[D_235, Title(''), Usage('N'), Position(18)]
    
    it119: Annotated[D_234, Title(''), Usage('N'), Position(19)]
    
    it120: Annotated[D_235, Title(''), Usage('N'), Position(20)]
    
    it121: Annotated[D_234, Title(''), Usage('N'), Position(21)]
    
    it122: Annotated[D_235, Title(''), Usage('N'), Position(22)]
    
    it123: Annotated[D_234, Title(''), Usage('N'), Position(23)]
    
    it124: Annotated[D_235, Title(''), Usage('N'), Position(24)]
    
    it125: Annotated[D_234, Title(''), Usage('N'), Position(25)]


class L2312A_SAC(Segment):
    """"""
    _segment_name = 'SAC'
    
    sac01: Annotated[D_248, Title(''), Usage('R'), Position(1), Enumerated(*['C'])]
    
    sac02: Annotated[D_1300, Title(''), Usage('R'), Position(2), Enumerated(*['A172', 'B680', 'D940', 'G740'])]
    
    sac03: Annotated[D_559, Title(''), Usage('N'), Position(3)]
    
    sac04: Annotated[D_1301, Title(''), Usage('N'), Position(4)]
    
    sac05: Annotated[D_610, Title(''), Usage('R'), Position(5)]
    
    sac06: Annotated[D_378, Title(''), Usage('N'), Position(6)]
    
    sac07: Annotated[D_332, Title(''), Usage('N'), Position(7)]
    
    sac08: Annotated[D_118, Title(''), Usage('N'), Position(8)]
    
    sac09: Annotated[D_355, Title(''), Usage('N'), Position(9)]
    
    sac10: Annotated[D_380, Title(''), Usage('N'), Position(10)]
    
    sac11: Annotated[D_380, Title(''), Usage('N'), Position(11)]
    
    sac12: Annotated[D_331, Title(''), Usage('N'), Position(12)]
    
    sac13: Annotated[D_127, Title(''), Usage('N'), Position(13)]
    
    sac14: Annotated[D_770, Title(''), Usage('N'), Position(14)]
    
    sac15: Annotated[D_352, Title(''), Usage('N'), Position(15)]
    
    sac16: Annotated[D_819, Title(''), Usage('N'), Position(16)]


class L2312A(Loop):
    
    sac: Annotated[L2312A_SAC, Title(''), Usage('R'), Position(2020), Syntax(['R0203', 'P0304', 'P0607', 'P0910', 'C1110', 'C1413', 'C1615']), Required(True)]


class L2315A_SLN05(Composite):
    """"""
    
    sln05_01: Annotated[D_355, Title(''), Usage('R'), Position(1), Enumerated(*['10', 'IE', 'PR'])]
    
    sln05_02: Annotated[D_1018, Title(''), Usage('N'), Position(2)]
    
    sln05_03: Annotated[D_649, Title(''), Usage('N'), Position(3)]
    
    sln05_04: Annotated[D_355, Title(''), Usage('N'), Position(4)]
    
    sln05_05: Annotated[D_1018, Title(''), Usage('N'), Position(5)]
    
    sln05_06: Annotated[D_649, Title(''), Usage('N'), Position(6)]
    
    sln05_07: Annotated[D_355, Title(''), Usage('N'), Position(7)]
    
    sln05_08: Annotated[D_1018, Title(''), Usage('N'), Position(8)]
    
    sln05_09: Annotated[D_649, Title(''), Usage('N'), Position(9)]
    
    sln05_10: Annotated[D_355, Title(''), Usage('N'), Position(10)]
    
    sln05_11: Annotated[D_1018, Title(''), Usage('N'), Position(11)]
    
    sln05_12: Annotated[D_649, Title(''), Usage('N'), Position(12)]
    
    sln05_13: Annotated[D_355, Title(''), Usage('N'), Position(13)]
    
    sln05_14: Annotated[D_1018, Title(''), Usage('N'), Position(14)]
    
    sln05_15: Annotated[D_649, Title(''), Usage('N'), Position(15)]


class L2315A_SLN(Segment):
    """"""
    _segment_name = 'SLN'
    
    sln01: Annotated[D_350, Title(''), Usage('R'), Position(1)]
    
    sln02: Annotated[D_350, Title(''), Usage('N'), Position(2)]
    
    sln03: Annotated[D_662, Title(''), Usage('R'), Position(3), Enumerated(*['O'])]
    
    sln04: Annotated[D_380, Title(''), Usage('R'), Position(4)]
    
    sln05: Annotated[L2315A_SLN05, Title(''), Usage('R'), Position(5), Required(True)]
    
    sln06: Annotated[D_212, Title(''), Usage('N'), Position(6)]
    
    sln07: Annotated[D_639, Title(''), Usage('N'), Position(7)]
    
    sln08: Annotated[D_662, Title(''), Usage('N'), Position(8)]
    
    sln09: Annotated[D_235, Title(''), Usage('N'), Position(9)]
    
    sln10: Annotated[D_234, Title(''), Usage('N'), Position(10)]
    
    sln11: Annotated[D_235, Title(''), Usage('N'), Position(11)]
    
    sln12: Annotated[D_234, Title(''), Usage('N'), Position(12)]
    
    sln13: Annotated[D_235, Title(''), Usage('N'), Position(13)]
    
    sln14: Annotated[D_234, Title(''), Usage('N'), Position(14)]
    
    sln15: Annotated[D_235, Title(''), Usage('N'), Position(15)]
    
    sln16: Annotated[D_234, Title(''), Usage('N'), Position(16)]
    
    sln17: Annotated[D_235, Title(''), Usage('N'), Position(17)]
    
    sln18: Annotated[D_234, Title(''), Usage('N'), Position(18)]
    
    sln19: Annotated[D_235, Title(''), Usage('N'), Position(19)]
    
    sln20: Annotated[D_234, Title(''), Usage('N'), Position(20)]
    
    sln21: Annotated[D_235, Title(''), Usage('N'), Position(21)]
    
    sln22: Annotated[D_234, Title(''), Usage('N'), Position(22)]
    
    sln23: Annotated[D_235, Title(''), Usage('N'), Position(23)]
    
    sln24: Annotated[D_234, Title(''), Usage('N'), Position(24)]
    
    sln25: Annotated[D_235, Title(''), Usage('N'), Position(25)]
    
    sln26: Annotated[D_234, Title(''), Usage('N'), Position(26)]
    
    sln27: Annotated[D_235, Title(''), Usage('N'), Position(27)]
    
    sln28: Annotated[D_234, Title(''), Usage('N'), Position(28)]


class L2315A(Loop):
    
    sln: Annotated[L2315A_SLN, Title(''), Usage('R'), Position(2040), Syntax(['P0405', 'C0706', 'C0806', 'P0910', 'P1112', 'P1314', 'P1516', 'P1718', 'P1920', 'P2122', 'P2324', 'P2526', 'P2728']), Required(True)]


class L2310A(Loop):
    
    it1: Annotated[L2310A_IT1, Title(''), Usage('R'), Position(1900), Syntax(['P020304', 'P0607', 'P0809', 'P1011', 'P1213', 'P1415', 'P1617', 'P1819', 'P2021', 'P2223', 'P2425']), Required(True)]
    ItemL2312A: TypeAlias = Annotated[L2312A, Title(''), Usage('S'), Position(2020), Required(True)]
    l2312a: Annotated[list[ItemL2312A], MinItems(4)]
    ItemL2315A: TypeAlias = Annotated[L2315A, Title(''), Usage('S'), Position(2040), Required(True)]
    l2315a: Annotated[list[ItemL2315A], MinItems(3)]


class L2320A_ADX(Segment):
    """"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title(''), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title(''), Usage('R'), Position(2), Enumerated(*['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA', 'J3'])]
    
    adx03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title(''), Usage('N'), Position(4)]


class L2320A(Loop):
    
    adx: Annotated[L2320A_ADX, Title(''), Usage('R'), Position(2100), Syntax(['P0304']), Required(True)]


class L2300A(Loop):
    
    rmr: Annotated[L2300A_RMR, Title(''), Usage('R'), Position(1500), Syntax(['P0102', 'P0708']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300A_REF, Title(''), Usage('S'), Position(1700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]
    
    dtm: Annotated[L2300A_DTM, Title(''), Usage('S'), Position(1800), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemL2310A: TypeAlias = Annotated[L2310A, Title(''), Usage('S'), Position(1900), Required(True)]
    l2310a: Annotated[list[ItemL2310A], MinItems(1)]
    ItemL2320A: TypeAlias = Annotated[L2320A, Title(''), Usage('S'), Position(2100), Required(True)]
    l2320a: Annotated[list[ItemL2320A], MinItems(1)]


class L2000A(Loop):
    
    ent: Annotated[L2000A_ENT, Title(''), Usage('R'), Position(100), Syntax(['P020304', 'P050607', 'P0809']), Required(True)]
    ItemL2200A: TypeAlias = Annotated[L2200A, Title(''), Usage('S'), Position(800), Required(True)]
    l2200a: Annotated[list[ItemL2200A], MinItems(1)]
    ItemL2300A: TypeAlias = Annotated[L2300A, Title(''), Usage('R'), Position(1500), Required(True)]
    l2300a: Annotated[list[ItemL2300A], MinItems(1)]


class TABLE2AREA2(Loop):
    ItemL2000A: TypeAlias = Annotated[L2000A, Title(''), Usage('S'), Position(100), Required(True)]
    l2000a: Annotated[list[ItemL2000A], MinItems(1)]


class L2000B_ENT(Segment):
    """"""
    _segment_name = 'ENT'
    
    ent01: Annotated[D_554, Title(''), Usage('R'), Position(1)]
    
    ent02: Annotated[D_98, Title(''), Usage('R'), Position(2), Enumerated(*['2J'])]
    
    ent03: Annotated[D_66, Title(''), Usage('R'), Position(3), Enumerated(*['34', 'EI', 'II'])]
    
    ent04: Annotated[D_67, Title(''), Usage('R'), Position(4)]
    
    ent05: Annotated[D_98, Title(''), Usage('N'), Position(5)]
    
    ent06: Annotated[D_66, Title(''), Usage('N'), Position(6)]
    
    ent07: Annotated[D_67, Title(''), Usage('N'), Position(7)]
    
    ent08: Annotated[D_128, Title(''), Usage('N'), Position(8)]
    
    ent09: Annotated[D_127, Title(''), Usage('N'), Position(9)]


class L2100B_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['DO', 'EY', 'IL', 'QE'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('S'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['34', 'EI', 'N'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100B(Loop):
    
    nm1: Annotated[L2100B_NM1, Title(''), Usage('R'), Position(200), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]


class L2200B_ADX(Segment):
    """"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title(''), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title(''), Usage('R'), Position(2), Enumerated(*['52', '53', '80', '81', '86', 'BJ', 'H1', 'H6', 'RU', 'WO'])]
    
    adx03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title(''), Usage('N'), Position(4)]


class L2200B(Loop):
    
    adx: Annotated[L2200B_ADX, Title(''), Usage('R'), Position(800), Syntax(['P0304']), Required(True)]


class L2300B_RMR(Segment):
    """"""
    _segment_name = 'RMR'
    
    rmr01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['11', '9J', 'AZ', 'B7', 'CT', 'ID', 'IG', 'IK', 'KW'])]
    
    rmr02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    rmr03: Annotated[D_482, Title(''), Usage('N'), Position(3)]
    
    rmr04: Annotated[D_782, Title(''), Usage('R'), Position(4)]
    
    rmr05: Annotated[D_782, Title(''), Usage('S'), Position(5)]
    
    rmr06: Annotated[D_782, Title(''), Usage('N'), Position(6)]
    
    rmr07: Annotated[D_426, Title(''), Usage('N'), Position(7)]
    
    rmr08: Annotated[D_782, Title(''), Usage('N'), Position(8)]


class L2300B_REF04(Composite):
    """"""
    pass


class L2300B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['14', '18', '2F', '38', 'E9', 'LU', 'ZZ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2300B_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['582', 'AAG'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('S'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('S'), Position(5), Enumerated(*['RD8'])]
    
    dtm06: Annotated[D_1251, Title(''), Usage('S'), Position(6)]


class L2320B_ADX(Segment):
    """"""
    _segment_name = 'ADX'
    
    adx01: Annotated[D_782, Title(''), Usage('R'), Position(1)]
    
    adx02: Annotated[D_426, Title(''), Usage('R'), Position(2), Enumerated(*['20', '52', '53', 'AA', 'AX', 'H1', 'H6', 'IA', 'J3'])]
    
    adx03: Annotated[D_128, Title(''), Usage('N'), Position(3)]
    
    adx04: Annotated[D_127, Title(''), Usage('N'), Position(4)]


class L2320B(Loop):
    
    adx: Annotated[L2320B_ADX, Title(''), Usage('R'), Position(2100), Syntax(['P0304']), Required(True)]


class L2300B(Loop):
    
    rmr: Annotated[L2300B_RMR, Title(''), Usage('R'), Position(1500), Syntax(['P0102', 'P0708']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2300B_REF, Title(''), Usage('S'), Position(1700), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]
    
    dtm: Annotated[L2300B_DTM, Title(''), Usage('S'), Position(1800), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemL2320B: TypeAlias = Annotated[L2320B, Title(''), Usage('S'), Position(2100), Required(True)]
    l2320b: Annotated[list[ItemL2320B], MinItems(1)]


class L2000B(Loop):
    
    ent: Annotated[L2000B_ENT, Title(''), Usage('R'), Position(100), Syntax(['P020304', 'P050607', 'P0809']), Required(True)]
    ItemL2100B: TypeAlias = Annotated[L2100B, Title(''), Usage('S'), Position(200), Required(True)]
    l2100b: Annotated[list[ItemL2100B], MinItems(1)]
    ItemL2200B: TypeAlias = Annotated[L2200B, Title(''), Usage('S'), Position(800), Required(True)]
    l2200b: Annotated[list[ItemL2200B], MinItems(1)]
    ItemL2300B: TypeAlias = Annotated[L2300B, Title(''), Usage('R'), Position(1500), Required(True)]
    l2300b: Annotated[list[ItemL2300B], MinItems(1)]


class TABLE2AREA3(Loop):
    ItemL2000B: TypeAlias = Annotated[L2000B, Title(''), Usage('S'), Position(100), Required(True)]
    l2000b: Annotated[list[ItemL2000B], MinItems(1)]


class FOOTER(Loop):
    pass


class ST_LOOP_SE(Segment):
    """"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title(''), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title(''), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title(''), Usage('R'), Position(100), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title(''), Usage('R'), Position(110), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemTable2Area2: TypeAlias = Annotated[TABLE2AREA2, Title(''), Usage('S'), Position(120)]
    table2area2: Annotated[list[ItemTable2Area2], MinItems(1)]
    ItemTable2Area3: TypeAlias = Annotated[TABLE2AREA3, Title(''), Usage('S'), Position(130)]
    table2area3: Annotated[list[ItemTable2Area3], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title(''), Usage('N'), Position(140)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title(''), Usage('R'), Position(500), Required(True)]


class MSG820A1(Message):
    """HIPAA Payment Order/Remittance Advice 005010X218 820A1"""
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title(''), Usage('R'), Position(200), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
