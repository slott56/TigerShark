"""
835.5010.X221.A1.v2
Created 2023-05-19 10:17:36.002838
"""
from .base import *
from .common import *


class ST_LOOP_ST(Segment):
    """"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title(''), Usage('R'), Position(1), Enumerated(*['835'])]
    
    st02: Annotated[D_329, Title(''), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title(''), Usage('N'), Position(3), Enumerated(*['005010X221A1'])]


class HEADER_BPR(Segment):
    """"""
    _segment_name = 'BPR'
    
    bpr01: Annotated[D_305, Title(''), Usage('R'), Position(1), Enumerated(*['C', 'D', 'H', 'I', 'P', 'U', 'X'])]
    
    bpr02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    bpr03: Annotated[D_478, Title(''), Usage('R'), Position(3), Enumerated(*['C', 'D'])]
    
    bpr04: Annotated[D_591, Title(''), Usage('R'), Position(4), Enumerated(*['ACH', 'BOP', 'CHK', 'FWT', 'NON'])]
    
    bpr05: Annotated[D_812, Title(''), Usage('S'), Position(5), Enumerated(*['CCP', 'CTX'])]
    
    bpr06: Annotated[D_506, Title(''), Usage('S'), Position(6), Enumerated(*['01', '04'])]
    
    bpr07: Annotated[D_507, Title(''), Usage('S'), Position(7)]
    
    bpr08: Annotated[D_569, Title(''), Usage('S'), Position(8), Enumerated(*['DA'])]
    
    bpr09: Annotated[D_508, Title(''), Usage('S'), Position(9)]
    
    bpr10: Annotated[D_509, Title(''), Usage('S'), Position(10)]
    
    bpr11: Annotated[D_510, Title(''), Usage('S'), Position(11)]
    
    bpr12: Annotated[D_506, Title(''), Usage('S'), Position(12), Enumerated(*['01', '04'])]
    
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
    
    trn01: Annotated[D_481, Title(''), Usage('R'), Position(1), Enumerated(*['1'])]
    
    trn02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    trn03: Annotated[D_509, Title(''), Usage('R'), Position(3)]
    
    trn04: Annotated[D_127, Title(''), Usage('S'), Position(4)]


class HEADER_CUR(Segment):
    """"""
    _segment_name = 'CUR'
    
    cur01: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PR'])]
    
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
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['EV'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class HEADER_REF04(Composite):
    """"""
    pass


class HEADER_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['F2'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class HEADER_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['405'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class L1000A_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    n102: Annotated[D_93, Title(''), Usage('R'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('S'), Position(3), Enumerated(*['XV'])]
    
    n104: Annotated[D_67, Title(''), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


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


class L1000A_REF04(Composite):
    """"""
    pass


class L1000A_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['2U', 'EO', 'HI', 'NF'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L1000A_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['CX'])]
    
    per02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('S'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EX'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L1000A_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['BL'])]
    
    per02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('S'), Position(3), Enumerated(*['EM', 'TE', 'UR'])]
    
    per04: Annotated[D_364, Title(''), Usage('S'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE', 'UR'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EM', 'EX', 'FX', 'UR'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L1000A_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['IC'])]
    
    per02: Annotated[D_93, Title(''), Usage('N'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['UR'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('N'), Position(5)]
    
    per06: Annotated[D_364, Title(''), Usage('N'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('N'), Position(7)]
    
    per08: Annotated[D_364, Title(''), Usage('N'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L1000A(Loop):
    
    n1: Annotated[L1000A_N1, Title(''), Usage('R'), Position(800), Syntax(['R0203', 'P0304']), Required(True)]
    
    n3: Annotated[L1000A_N3, Title(''), Usage('R'), Position(1000), Required(True)]
    
    n4: Annotated[L1000A_N4, Title(''), Usage('R'), Position(1100), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L1000A_REF, Title(''), Usage('S'), Position(1200), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(4)]
    
    per: Annotated[L1000A_PER, Title(''), Usage('S'), Position(1300), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    ItemPer: TypeAlias = Annotated[L1000A_PER, Title(''), Usage('R'), Position(1300), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MinItems(1)]
    
    per: Annotated[L1000A_PER, Title(''), Usage('S'), Position(1300), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]


class L1000B_N1(Segment):
    """"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PE'])]
    
    n102: Annotated[D_93, Title(''), Usage('R'), Position(2)]
    
    n103: Annotated[D_66, Title(''), Usage('R'), Position(3), Enumerated(*['FI', 'XV', 'XX'])]
    
    n104: Annotated[D_67, Title(''), Usage('R'), Position(4)]
    
    n105: Annotated[D_706, Title(''), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title(''), Usage('N'), Position(6)]


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


class L1000B_REF04(Composite):
    """"""
    pass


class L1000B_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', 'D3', 'PQ', 'TJ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L1000B_RDM04(Composite):
    """"""
    pass


class L1000B_RDM05(Composite):
    """"""
    pass


class L1000B_RDM(Segment):
    """"""
    _segment_name = 'RDM'
    
    rdm01: Annotated[D_756, Title(''), Usage('R'), Position(1), Enumerated(*['BM', 'EM', 'FT', 'OL'])]
    
    rdm02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    rdm03: Annotated[D_364, Title(''), Usage('S'), Position(3)]


class L1000B(Loop):
    
    n1: Annotated[L1000B_N1, Title(''), Usage('R'), Position(800), Syntax(['R0203', 'P0304']), Required(True)]
    
    n3: Annotated[L1000B_N3, Title(''), Usage('S'), Position(1000), Required(True)]
    
    n4: Annotated[L1000B_N4, Title(''), Usage('S'), Position(1100), Syntax(['E0207', 'C0605', 'C0704']), Required(True)]
    ItemRef: TypeAlias = Annotated[L1000B_REF, Title(''), Usage('S'), Position(1200), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MinItems(1)]
    
    rdm: Annotated[L1000B_RDM, Title(''), Usage('S'), Position(1400), Required(True)]


class HEADER(Loop):
    
    bpr: Annotated[HEADER_BPR, Title(''), Usage('R'), Position(200), Syntax(['P0607', 'C0809', 'P1213', 'C1415', 'P1819', 'C2021']), Required(True)]
    
    trn: Annotated[HEADER_TRN, Title(''), Usage('R'), Position(400), Required(True)]
    
    cur: Annotated[HEADER_CUR, Title(''), Usage('S'), Position(500), Syntax(['C0807', 'C0907', 'L101112', 'C1110', 'C1210', 'L131415', 'C1413', 'C1513', 'L161718', 'C1716', 'C1816', 'L192021', 'C2019', 'C2119']), Required(True)]
    
    ref: Annotated[HEADER_REF, Title(''), Usage('S'), Position(600), Syntax(['R0203']), Required(True)]
    
    ref: Annotated[HEADER_REF, Title(''), Usage('S'), Position(600), Syntax(['R0203']), Required(True)]
    
    dtm: Annotated[HEADER_DTM, Title(''), Usage('S'), Position(700), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemL1000A: TypeAlias = Annotated[L1000A, Title(''), Usage('R'), Position(800), Required(True)]
    l1000a: Annotated[list[ItemL1000A], MinItems(1)]
    ItemL1000B: TypeAlias = Annotated[L1000B, Title(''), Usage('R'), Position(1400), Required(True)]
    l1000b: Annotated[list[ItemL1000B], MinItems(1)]


class L2000_LX(Segment):
    """"""
    _segment_name = 'LX'
    
    lx01: Annotated[D_554, Title(''), Usage('R'), Position(1)]


class L2000_TS3(Segment):
    """"""
    _segment_name = 'TS3'
    
    ts301: Annotated[D_127, Title(''), Usage('R'), Position(1)]
    
    ts302: Annotated[D_1331, Title(''), Usage('R'), Position(2)]
    
    ts303: Annotated[D_373, Title(''), Usage('R'), Position(3)]
    
    ts304: Annotated[D_380, Title(''), Usage('R'), Position(4)]
    
    ts305: Annotated[D_782, Title(''), Usage('R'), Position(5)]
    
    ts306: Annotated[D_782, Title(''), Usage('N'), Position(6)]
    
    ts307: Annotated[D_782, Title(''), Usage('N'), Position(7)]
    
    ts308: Annotated[D_782, Title(''), Usage('N'), Position(8)]
    
    ts309: Annotated[D_782, Title(''), Usage('N'), Position(9)]
    
    ts310: Annotated[D_782, Title(''), Usage('N'), Position(10)]
    
    ts311: Annotated[D_782, Title(''), Usage('N'), Position(11)]
    
    ts312: Annotated[D_782, Title(''), Usage('N'), Position(12)]
    
    ts313: Annotated[D_782, Title(''), Usage('S'), Position(13)]
    
    ts314: Annotated[D_782, Title(''), Usage('N'), Position(14)]
    
    ts315: Annotated[D_782, Title(''), Usage('S'), Position(15)]
    
    ts316: Annotated[D_782, Title(''), Usage('N'), Position(16)]
    
    ts317: Annotated[D_782, Title(''), Usage('S'), Position(17)]
    
    ts318: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    ts319: Annotated[D_782, Title(''), Usage('N'), Position(19)]
    
    ts320: Annotated[D_782, Title(''), Usage('S'), Position(20)]
    
    ts321: Annotated[D_782, Title(''), Usage('S'), Position(21)]
    
    ts322: Annotated[D_782, Title(''), Usage('S'), Position(22)]
    
    ts323: Annotated[D_380, Title(''), Usage('S'), Position(23)]
    
    ts324: Annotated[D_782, Title(''), Usage('S'), Position(24)]


class L2000_TS2(Segment):
    """"""
    _segment_name = 'TS2'
    
    ts201: Annotated[D_782, Title(''), Usage('S'), Position(1)]
    
    ts202: Annotated[D_782, Title(''), Usage('S'), Position(2)]
    
    ts203: Annotated[D_782, Title(''), Usage('S'), Position(3)]
    
    ts204: Annotated[D_782, Title(''), Usage('S'), Position(4)]
    
    ts205: Annotated[D_782, Title(''), Usage('S'), Position(5)]
    
    ts206: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    ts207: Annotated[D_380, Title(''), Usage('S'), Position(7)]
    
    ts208: Annotated[D_782, Title(''), Usage('S'), Position(8)]
    
    ts209: Annotated[D_782, Title(''), Usage('S'), Position(9)]
    
    ts210: Annotated[D_380, Title(''), Usage('S'), Position(10)]
    
    ts211: Annotated[D_380, Title(''), Usage('S'), Position(11)]
    
    ts212: Annotated[D_380, Title(''), Usage('S'), Position(12)]
    
    ts213: Annotated[D_380, Title(''), Usage('S'), Position(13)]
    
    ts214: Annotated[D_380, Title(''), Usage('S'), Position(14)]
    
    ts215: Annotated[D_782, Title(''), Usage('S'), Position(15)]
    
    ts216: Annotated[D_380, Title(''), Usage('S'), Position(16)]
    
    ts217: Annotated[D_782, Title(''), Usage('S'), Position(17)]
    
    ts218: Annotated[D_782, Title(''), Usage('S'), Position(18)]
    
    ts219: Annotated[D_782, Title(''), Usage('S'), Position(19)]


class L2100_CLP(Segment):
    """"""
    _segment_name = 'CLP'
    
    clp01: Annotated[D_1028, Title(''), Usage('R'), Position(1)]
    
    clp02: Annotated[D_1029, Title(''), Usage('R'), Position(2), Enumerated(*['1', '19', '2', '20', '21', '22', '23', '25', '3', '4'])]
    
    clp03: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    clp04: Annotated[D_782, Title(''), Usage('R'), Position(4)]
    
    clp05: Annotated[D_782, Title(''), Usage('S'), Position(5)]
    
    clp06: Annotated[D_1032, Title(''), Usage('R'), Position(6), Enumerated(*['12', '13', '14', '15', '16', '17', 'AM', 'CH', 'DS', 'HM', 'LM', 'MA', 'MB', 'MC', 'OF', 'TV', 'VA', 'WC', 'ZZ'])]
    
    clp07: Annotated[D_127, Title(''), Usage('R'), Position(7)]
    
    clp08: Annotated[D_1331, Title(''), Usage('S'), Position(8)]
    
    clp09: Annotated[D_1325, Title(''), Usage('S'), Position(9)]
    
    clp10: Annotated[D_1352, Title(''), Usage('N'), Position(10)]
    
    clp11: Annotated[D_1354, Title(''), Usage('S'), Position(11)]
    
    clp12: Annotated[D_380, Title(''), Usage('S'), Position(12)]
    
    clp13: Annotated[D_954, Title(''), Usage('S'), Position(13)]
    
    clp14: Annotated[D_1073, Title(''), Usage('N'), Position(14)]


class L2100_CAS(Segment):
    """"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title(''), Usage('R'), Position(1), Enumerated(*['CO', 'OA', 'PI', 'PR'])]
    
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


class L2100_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['QC'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['34', 'HN', 'II', 'MI', 'MR'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['IL'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['FI', 'II', 'MI'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['74'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['C'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['82'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['BD', 'BS', 'FI', 'MC', 'PC', 'SL', 'UP', 'XX'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['TT'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['AD', 'FI', 'NI', 'PI', 'PP', 'XV'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['PR'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('R'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('N'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('N'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('N'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('R'), Position(8), Enumerated(*['AD', 'FI', 'NI', 'PI', 'PP', 'XV'])]
    
    nm109: Annotated[D_67, Title(''), Usage('R'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100_NM1(Segment):
    """"""
    _segment_name = 'NM1'
    
    nm101: Annotated[D_98, Title(''), Usage('R'), Position(1), Enumerated(*['GB'])]
    
    nm102: Annotated[D_1065, Title(''), Usage('R'), Position(2), Enumerated(*['1', '2'])]
    
    nm103: Annotated[D_1035, Title(''), Usage('S'), Position(3)]
    
    nm104: Annotated[D_1036, Title(''), Usage('S'), Position(4)]
    
    nm105: Annotated[D_1037, Title(''), Usage('S'), Position(5)]
    
    nm106: Annotated[D_1038, Title(''), Usage('N'), Position(6)]
    
    nm107: Annotated[D_1039, Title(''), Usage('S'), Position(7)]
    
    nm108: Annotated[D_66, Title(''), Usage('S'), Position(8), Enumerated(*['FI', 'II', 'MI'])]
    
    nm109: Annotated[D_67, Title(''), Usage('S'), Position(9)]
    
    nm110: Annotated[D_706, Title(''), Usage('N'), Position(10)]
    
    nm111: Annotated[D_98, Title(''), Usage('N'), Position(11)]
    
    nm112: Annotated[D_1035, Title(''), Usage('N'), Position(12)]


class L2100_MIA(Segment):
    """"""
    _segment_name = 'MIA'
    
    mia01: Annotated[D_380, Title(''), Usage('R'), Position(1)]
    
    mia02: Annotated[D_782, Title(''), Usage('S'), Position(2)]
    
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


class L2100_MOA(Segment):
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


class L2100_REF04(Composite):
    """"""
    pass


class L2100_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['1L', '1W', '28', '6P', '9A', '9C', 'BB', 'CE', 'EA', 'F8', 'G1', 'G3', 'IG', 'SY'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2100_REF04(Composite):
    """"""
    pass


class L2100_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'D3', 'G2', 'LU'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2100_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['232', '233'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class L2100_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['036'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class L2100_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['050'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class L2100_PER(Segment):
    """"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title(''), Usage('R'), Position(1), Enumerated(*['CX'])]
    
    per02: Annotated[D_93, Title(''), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title(''), Usage('R'), Position(3), Enumerated(*['EM', 'FX', 'TE'])]
    
    per04: Annotated[D_364, Title(''), Usage('R'), Position(4)]
    
    per05: Annotated[D_365, Title(''), Usage('S'), Position(5), Enumerated(*['EM', 'EX', 'FX', 'TE'])]
    
    per06: Annotated[D_364, Title(''), Usage('S'), Position(6)]
    
    per07: Annotated[D_365, Title(''), Usage('S'), Position(7), Enumerated(*['EX'])]
    
    per08: Annotated[D_364, Title(''), Usage('S'), Position(8)]
    
    per09: Annotated[D_443, Title(''), Usage('N'), Position(9)]


class L2100_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['AU', 'D8', 'DY', 'F5', 'I', 'NL', 'T', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2100_QTY03(Composite):
    """"""
    pass


class L2100_QTY(Segment):
    """"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title(''), Usage('R'), Position(1), Enumerated(*['CA', 'CD', 'LA', 'LE', 'NE', 'NR', 'OU', 'PS', 'VS', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO'])]
    
    qty02: Annotated[D_380, Title(''), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title(''), Usage('N'), Position(4)]


class L2110_SVC01(Composite):
    """"""
    
    svc01_01: Annotated[D_235, Title(''), Usage('R'), Position(1), Enumerated(*['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'N6', 'NU', 'UI', 'WK'])]
    
    svc01_02: Annotated[D_234, Title(''), Usage('R'), Position(2)]
    
    svc01_03: Annotated[D_1339, Title(''), Usage('S'), Position(3)]
    
    svc01_04: Annotated[D_1339, Title(''), Usage('S'), Position(4)]
    
    svc01_05: Annotated[D_1339, Title(''), Usage('S'), Position(5)]
    
    svc01_06: Annotated[D_1339, Title(''), Usage('S'), Position(6)]
    
    svc01_07: Annotated[D_352, Title(''), Usage('N'), Position(7)]
    
    svc01_08: Annotated[D_234, Title(''), Usage('N'), Position(8)]


class L2110_SVC06(Composite):
    """"""
    
    svc06_01: Annotated[D_235, Title(''), Usage('R'), Position(1), Enumerated(*['AD', 'ER', 'HC', 'HP', 'IV', 'N4', 'NU', 'WK'])]
    
    svc06_02: Annotated[D_234, Title(''), Usage('R'), Position(2)]
    
    svc06_03: Annotated[D_1339, Title(''), Usage('S'), Position(3)]
    
    svc06_04: Annotated[D_1339, Title(''), Usage('S'), Position(4)]
    
    svc06_05: Annotated[D_1339, Title(''), Usage('S'), Position(5)]
    
    svc06_06: Annotated[D_1339, Title(''), Usage('S'), Position(6)]
    
    svc06_07: Annotated[D_352, Title(''), Usage('S'), Position(7)]
    
    svc06_08: Annotated[D_234, Title(''), Usage('N'), Position(8)]


class L2110_SVC(Segment):
    """"""
    _segment_name = 'SVC'
    
    svc01: Annotated[L2110_SVC01, Title(''), Usage('R'), Position(1), Required(True)]
    
    svc02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    svc03: Annotated[D_782, Title(''), Usage('R'), Position(3)]
    
    svc04: Annotated[D_234, Title(''), Usage('S'), Position(4)]
    
    svc05: Annotated[D_380, Title(''), Usage('S'), Position(5)]
    
    svc06: Annotated[L2110_SVC06, Title(''), Usage('S'), Position(6), Required(True)]
    
    svc07: Annotated[D_380, Title(''), Usage('S'), Position(7)]


class L2110_DTM(Segment):
    """"""
    _segment_name = 'DTM'
    
    dtm01: Annotated[D_374, Title(''), Usage('R'), Position(1), Enumerated(*['150', '151', '472'])]
    
    dtm02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    dtm03: Annotated[D_337, Title(''), Usage('N'), Position(3)]
    
    dtm04: Annotated[D_623, Title(''), Usage('N'), Position(4)]
    
    dtm05: Annotated[D_1250, Title(''), Usage('N'), Position(5)]
    
    dtm06: Annotated[D_1251, Title(''), Usage('N'), Position(6)]


class L2110_CAS(Segment):
    """"""
    _segment_name = 'CAS'
    
    cas01: Annotated[D_1033, Title(''), Usage('R'), Position(1), Enumerated(*['CO', 'OA', 'PI', 'PR'])]
    
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


class L2110_REF04(Composite):
    """"""
    pass


class L2110_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['1S', 'APC', 'BB', 'E9', 'G1', 'G3', 'LU', 'RB'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2110_REF04(Composite):
    """"""
    pass


class L2110_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['6R'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2110_REF04(Composite):
    """"""
    pass


class L2110_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0B', '1A', '1B', '1C', '1D', '1G', '1H', '1J', 'D3', 'G2', 'HPI', 'SY', 'TJ'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2110_REF04(Composite):
    """"""
    pass


class L2110_REF(Segment):
    """"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title(''), Usage('R'), Position(1), Enumerated(*['0K'])]
    
    ref02: Annotated[D_127, Title(''), Usage('R'), Position(2)]
    
    ref03: Annotated[D_352, Title(''), Usage('N'), Position(3)]


class L2110_AMT(Segment):
    """"""
    _segment_name = 'AMT'
    
    amt01: Annotated[D_522, Title(''), Usage('R'), Position(1), Enumerated(*['B6', 'KH', 'T', 'T2', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO'])]
    
    amt02: Annotated[D_782, Title(''), Usage('R'), Position(2)]
    
    amt03: Annotated[D_478, Title(''), Usage('N'), Position(3)]


class L2110_QTY03(Composite):
    """"""
    pass


class L2110_QTY(Segment):
    """"""
    _segment_name = 'QTY'
    
    qty01: Annotated[D_673, Title(''), Usage('R'), Position(1), Enumerated(*['ZK', 'ZL', 'ZM', 'ZN', 'ZO'])]
    
    qty02: Annotated[D_380, Title(''), Usage('R'), Position(2)]
    
    qty04: Annotated[D_61, Title(''), Usage('N'), Position(4)]


class L2110_LQ(Segment):
    """"""
    _segment_name = 'LQ'
    
    lq01: Annotated[D_1270, Title(''), Usage('R'), Position(1), Enumerated(*['HE', 'RX'])]
    
    lq02: Annotated[D_1271, Title(''), Usage('R'), Position(2)]


class L2110(Loop):
    
    svc: Annotated[L2110_SVC, Title(''), Usage('R'), Position(700), Required(True)]
    ItemDtm: TypeAlias = Annotated[L2110_DTM, Title(''), Usage('S'), Position(800), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    dtm: Annotated[list[ItemDtm], MaxItems(2)]
    ItemCas: TypeAlias = Annotated[L2110_CAS, Title(''), Usage('S'), Position(900), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    ItemRef: TypeAlias = Annotated[L2110_REF, Title(''), Usage('S'), Position(1000), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(8)]
    
    ref: Annotated[L2110_REF, Title(''), Usage('S'), Position(1000), Syntax(['R0203']), Required(True)]
    ItemRef: TypeAlias = Annotated[L2110_REF, Title(''), Usage('S'), Position(1000), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(10)]
    ItemRef: TypeAlias = Annotated[L2110_REF, Title(''), Usage('S'), Position(1000), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    ItemAmt: TypeAlias = Annotated[L2110_AMT, Title(''), Usage('S'), Position(1100), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(9)]
    ItemQty: TypeAlias = Annotated[L2110_QTY, Title(''), Usage('S'), Position(1200), Syntax(['E0204', 'R0204']), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(6)]
    ItemLq: TypeAlias = Annotated[L2110_LQ, Title(''), Usage('S'), Position(1300), Syntax(['C0102']), Required(True)]
    lq: Annotated[list[ItemLq], MaxItems(99)]


class L2100(Loop):
    
    clp: Annotated[L2100_CLP, Title(''), Usage('R'), Position(100), Required(True)]
    ItemCas: TypeAlias = Annotated[L2100_CAS, Title(''), Usage('S'), Position(200), Syntax(['L050607', 'C0605', 'C0705', 'L080910', 'C0908', 'C1008', 'L111213', 'C1211', 'C1311', 'L141516', 'C1514', 'C1614', 'L171819', 'C1817', 'C1917']), Required(True)]
    cas: Annotated[list[ItemCas], MaxItems(99)]
    
    nm1: Annotated[L2100_NM1, Title(''), Usage('R'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title(''), Usage('S'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title(''), Usage('S'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title(''), Usage('S'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title(''), Usage('S'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title(''), Usage('S'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    nm1: Annotated[L2100_NM1, Title(''), Usage('S'), Position(300), Syntax(['P0809', 'C1110', 'C1203']), Required(True)]
    
    mia: Annotated[L2100_MIA, Title(''), Usage('S'), Position(330), Required(True)]
    
    moa: Annotated[L2100_MOA, Title(''), Usage('S'), Position(350)]
    ItemRef: TypeAlias = Annotated[L2100_REF, Title(''), Usage('S'), Position(400), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(5)]
    ItemRef: TypeAlias = Annotated[L2100_REF, Title(''), Usage('S'), Position(400), Syntax(['R0203']), Required(True)]
    ref: Annotated[list[ItemRef], MaxItems(10)]
    ItemDtm: TypeAlias = Annotated[L2100_DTM, Title(''), Usage('S'), Position(500), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    dtm: Annotated[list[ItemDtm], MaxItems(2)]
    
    dtm: Annotated[L2100_DTM, Title(''), Usage('S'), Position(500), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    
    dtm: Annotated[L2100_DTM, Title(''), Usage('S'), Position(500), Syntax(['R020305', 'C0403', 'P0506']), Required(True)]
    ItemPer: TypeAlias = Annotated[L2100_PER, Title(''), Usage('S'), Position(600), Syntax(['P0304', 'P0506', 'P0708']), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(2)]
    ItemAmt: TypeAlias = Annotated[L2100_AMT, Title(''), Usage('S'), Position(620), Required(True)]
    amt: Annotated[list[ItemAmt], MaxItems(13)]
    ItemQty: TypeAlias = Annotated[L2100_QTY, Title(''), Usage('S'), Position(640), Syntax(['E0204', 'R0204']), Required(True)]
    qty: Annotated[list[ItemQty], MaxItems(14)]
    ItemL2110: TypeAlias = Annotated[L2110, Title(''), Usage('S'), Position(700), Required(True)]
    l2110: Annotated[list[ItemL2110], MinItems(999)]


class L2000(Loop):
    
    lx: Annotated[L2000_LX, Title(''), Usage('R'), Position(30), Required(True)]
    
    ts3: Annotated[L2000_TS3, Title(''), Usage('S'), Position(50), Required(True)]
    
    ts2: Annotated[L2000_TS2, Title(''), Usage('S'), Position(70)]
    ItemL2100: TypeAlias = Annotated[L2100, Title(''), Usage('R'), Position(100), Required(True)]
    l2100: Annotated[list[ItemL2100], MinItems(1)]


class DETAIL(Loop):
    ItemL2000: TypeAlias = Annotated[L2000, Title(''), Usage('S'), Position(30), Required(True)]
    l2000: Annotated[list[ItemL2000], MinItems(1)]


class FOOTER_PLB03(Composite):
    """"""
    
    plb03_01: Annotated[D_426, Title(''), Usage('R'), Position(1), Enumerated(*['50', '51', '72', '90', 'AH', 'AM', 'AP', 'B2', 'B3', 'BD', 'BN', 'C5', 'CR', 'CS', 'CT', 'CV', 'CW', 'DM', 'E3', 'FB', 'FC', 'GO', 'HM', 'IP', 'IR', 'IS', 'J1', 'L3', 'L6', 'LE', 'LS', 'OA', 'OB', 'PI', 'PL', 'RA', 'RE', 'SL', 'TL', 'WO', 'WU'])]
    
    plb03_02: Annotated[D_127, Title(''), Usage('S'), Position(2)]


class FOOTER_PLB05(Composite):
    """"""
    
    plb05_01: Annotated[D_426, Title(''), Usage('R'), Position(1)]
    
    plb05_02: Annotated[D_127, Title(''), Usage('S'), Position(2)]


class FOOTER_PLB07(Composite):
    """"""
    
    plb07_01: Annotated[D_426, Title(''), Usage('R'), Position(1)]
    
    plb07_02: Annotated[D_127, Title(''), Usage('S'), Position(2)]


class FOOTER_PLB09(Composite):
    """"""
    
    plb09_01: Annotated[D_426, Title(''), Usage('R'), Position(1)]
    
    plb09_02: Annotated[D_127, Title(''), Usage('S'), Position(2)]


class FOOTER_PLB11(Composite):
    """"""
    
    plb11_01: Annotated[D_426, Title(''), Usage('R'), Position(1)]
    
    plb11_02: Annotated[D_127, Title(''), Usage('S'), Position(2)]


class FOOTER_PLB13(Composite):
    """"""
    
    plb13_01: Annotated[D_426, Title(''), Usage('R'), Position(1)]
    
    plb13_02: Annotated[D_127, Title(''), Usage('S'), Position(2)]


class FOOTER_PLB(Segment):
    """"""
    _segment_name = 'PLB'
    
    plb01: Annotated[D_127, Title(''), Usage('R'), Position(1)]
    
    plb02: Annotated[D_373, Title(''), Usage('R'), Position(2)]
    
    plb03: Annotated[FOOTER_PLB03, Title(''), Usage('R'), Position(3), Required(True)]
    
    plb04: Annotated[D_782, Title(''), Usage('R'), Position(4)]
    
    plb05: Annotated[FOOTER_PLB05, Title(''), Usage('S'), Position(5), Required(True)]
    
    plb06: Annotated[D_782, Title(''), Usage('S'), Position(6)]
    
    plb07: Annotated[FOOTER_PLB07, Title(''), Usage('S'), Position(7), Required(True)]
    
    plb08: Annotated[D_782, Title(''), Usage('S'), Position(8)]
    
    plb09: Annotated[FOOTER_PLB09, Title(''), Usage('S'), Position(9), Required(True)]
    
    plb10: Annotated[D_782, Title(''), Usage('S'), Position(10)]
    
    plb11: Annotated[FOOTER_PLB11, Title(''), Usage('S'), Position(11), Required(True)]
    
    plb12: Annotated[D_782, Title(''), Usage('S'), Position(12)]
    
    plb13: Annotated[FOOTER_PLB13, Title(''), Usage('S'), Position(13), Required(True)]
    
    plb14: Annotated[D_782, Title(''), Usage('S'), Position(14)]


class FOOTER(Loop):
    ItemPlb: TypeAlias = Annotated[FOOTER_PLB, Title(''), Usage('S'), Position(100), Syntax(['P0506', 'P0708', 'P0910', 'P1112', 'P1314']), Required(True)]
    plb: Annotated[list[ItemPlb], MinItems(1)]


class ST_LOOP_SE(Segment):
    """"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title(''), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title(''), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title(''), Usage('R'), Position(100), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title(''), Usage('R'), Position(110), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title(''), Usage('S'), Position(120)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title(''), Usage('R'), Position(130)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title(''), Usage('R'), Position(200), Required(True)]


class MSG835W1(Message):
    """HIPAA Health Care Claim Payment/Advice 005010X221A1 835W1"""
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title(''), Usage('R'), Position(200), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
