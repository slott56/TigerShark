"""
830.4010.PS
Created 2023-05-19 10:17:35.948584
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
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['PS'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_29, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_30, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['830'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class HEADER_BFR(Segment):
    """Planning Schedule"""
    _segment_name = 'BFR'
    
    bfr01: Annotated[D_353, Title('Transaction Purpose Code'), Usage('R'), Position(1), Enumerated(*['05'])]
    
    bfr02: Annotated[D_127, Title('Forecast Order Number'), Usage('S'), Position(2)]
    
    bfr03: Annotated[D_328, Title('Release Number'), Usage('R'), Position(3)]
    
    bfr04: Annotated[D_675, Title('Schedule Type Qualifier'), Usage('R'), Position(4), Enumerated(*['DL', 'SH'])]
    
    bfr05: Annotated[D_676, Title('Schedule Quantity Qualifier'), Usage('R'), Position(5), Enumerated(*['C', 'A'])]
    
    bfr06: Annotated[D_373, Title('Horizon Start Date'), Usage('R'), Position(6)]
    
    bfr07: Annotated[D_373, Title('Horizon End Date'), Usage('R'), Position(7)]
    
    bfr08: Annotated[D_373, Title('Generation Date'), Usage('R'), Position(8)]
    
    bfr09: Annotated[D_373, Title('Fordcast Updated Date'), Usage('S'), Position(9)]
    
    bfr10: Annotated[D_367, Title('Contract Number'), Usage('S'), Position(10)]
    
    bfr11: Annotated[D_324, Title('Purchase Order Number'), Usage('S'), Position(11)]


class N1_LOOP_N1(Segment):
    """Payer Identification"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['SU', 'ST', 'MI', 'SF'])]
    
    n102: Annotated[D_93, Title('Payer Name'), Usage('S'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('S'), Position(3), Enumerated(*['1', '92'])]
    
    n104: Annotated[D_67, Title('Payer Identifier'), Usage('S'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class N1_LOOP_PER(Segment):
    """Administrative Communications Information"""
    _segment_name = 'PER'
    
    per01: Annotated[D_366, Title('ContactFunction Code'), Usage('R'), Position(1), Enumerated(*['EX'])]
    
    per02: Annotated[D_93, Title('ContactFunction Code'), Usage('S'), Position(2)]
    
    per03: Annotated[D_365, Title('ContactFunction Code'), Usage('S'), Position(3)]
    
    per04: Annotated[D_364, Title('ContactFunction Code'), Usage('S'), Position(4)]


class N1_LOOP(Loop):
    ItemN1: TypeAlias = Annotated[N1_LOOP_N1, Title('Payer Identification'), Usage('R'), Position(230), Syntax(['R0203', 'P0304']), Required(True)]
    n1: Annotated[list[ItemN1], MaxItems(3)]
    ItemPer: TypeAlias = Annotated[N1_LOOP_PER, Title('Administrative Communications Information'), Usage('S'), Position(280), Syntax(['P0304']), Required(True)]
    per: Annotated[list[ItemPer], MaxItems(3)]


class HEADER(Loop):
    
    bfr: Annotated[HEADER_BFR, Title('Planning Schedule'), Usage('R'), Position(10), Syntax(['R0203']), Required(True)]
    ItemN1_Loop: TypeAlias = Annotated[N1_LOOP, Title('Supplier'), Usage('R'), Position(230), Required(True)]
    n1_loop: Annotated[list[ItemN1_Loop], MinItems(200)]


class LIN_LOOP_LIN(Segment):
    """Item Identification"""
    _segment_name = 'LIN'
    
    lin01: Annotated[D_350, Title('Assigned Identification'), Usage('N'), Position(1)]
    
    lin02: Annotated[D_235, Title('Buyer Part Number'), Usage('R'), Position(2), Enumerated(*['BP'])]
    
    lin03: Annotated[D_234, Title('Product/Service Id'), Usage('S'), Position(3)]
    
    lin04: Annotated[D_235, Title('Product/Service Id Qualifier'), Usage('S'), Position(4), Enumerated(*['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY', 'VP'])]
    
    lin05: Annotated[D_234, Title('Product/Service Id'), Usage('S'), Position(5)]
    
    lin06: Annotated[D_235, Title('Product/Service Id Qualifier'), Usage('S'), Position(6), Enumerated(*['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY', 'VP'])]
    
    lin07: Annotated[D_234, Title('Product/Service Id'), Usage('S'), Position(7)]
    
    lin08: Annotated[D_235, Title('Product/Service Id Qualifier'), Usage('S'), Position(8), Enumerated(*['CR', 'DR', 'EC', 'ON', 'PL', 'PO', 'RN', 'RY', 'VP'])]


class LIN_LOOP_UIT(Segment):
    """Unit Detail"""
    _segment_name = 'UIT'
    
    uit01: Annotated[D_355, Title('Composite Unit of Measure'), Usage('R'), Position(1)]


class LIN_LOOP_PID(Segment):
    """Product/Item Description"""
    _segment_name = 'PID'
    
    pid01: Annotated[D_349, Title('Item Descripton Type'), Usage('R'), Position(1), Enumerated(*['F'])]
    
    pid02: Annotated[D_750, Title('Product/Process Characteristic Code'), Usage('S'), Position(2)]
    
    pid03: Annotated[D_559, Title('Product/Process Characteristic Code'), Usage('S'), Position(3)]
    
    pid04: Annotated[D_751, Title('Product/Process Characteristic Code'), Usage('S'), Position(4)]
    
    pid05: Annotated[D_352, Title('Product/Process Characteristic Code'), Usage('S'), Position(5)]


class LIN_LOOP_ATH(Segment):
    """Resource Authorization"""
    _segment_name = 'ATH'
    
    ath01: Annotated[D_672, Title('Resource Authorization Code'), Usage('R'), Position(1), Enumerated(*['FI', 'MT', 'PQ'])]
    
    ath02: Annotated[D_373, Title('Resource Authorization Date'), Usage('S'), Position(2)]
    
    ath03: Annotated[D_380, Title('Quantity'), Usage('S'), Position(3)]
    
    ath04: Annotated[D_380, Title('Quantity'), Usage('N'), Position(4)]
    
    ath05: Annotated[D_373, Title('Cumulative Start Date'), Usage('S'), Position(5)]


class FST_LOOP_FST(Segment):
    """Forecast Schedule"""
    _segment_name = 'FST'
    
    fst01: Annotated[D_380, Title('Quantity'), Usage('R'), Position(1)]
    
    fst02: Annotated[D_680, Title('Forecast Qualifier'), Usage('R'), Position(2), Enumerated(*['A', 'C', 'D', 'B', 'Z'])]
    
    fst03: Annotated[D_681, Title('Forecast Timing Qualifier'), Usage('R'), Position(3), Enumerated(*['F', 'M', 'W', 'D', 'Z'])]
    
    fst04: Annotated[D_373, Title('Forecast Schedule Date'), Usage('R'), Position(4)]


class FST_LOOP(Loop):
    ItemFst: TypeAlias = Annotated[FST_LOOP_FST, Title('Forecast Schedule'), Usage('R'), Position(410), Syntax(['P0607', 'P0809']), Required(True)]
    fst: Annotated[list[ItemFst], MaxItems(1000)]


class SHP_LOOP_SHP(Segment):
    """Shipped/Received Information"""
    _segment_name = 'SHP'
    
    shp01: Annotated[D_673, Title('Quantity Qualifier'), Usage('R'), Position(1), Enumerated(*['01', '02'])]
    
    shp02: Annotated[D_380, Title('Quantity'), Usage('R'), Position(2)]
    
    shp03: Annotated[D_374, Title('Date/Time Qualifier'), Usage('R'), Position(3), Enumerated(*['011', '050', '051'])]
    
    shp04: Annotated[D_373, Title('Date'), Usage('S'), Position(4)]


class SHP_LOOP_REF(Segment):
    """Reference Identification"""
    _segment_name = 'REF'
    
    ref01: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(1), Enumerated(*['SI'])]
    
    ref02: Annotated[D_127, Title('Reference Identification'), Usage('R'), Position(2)]


class SHP_LOOP(Loop):
    ItemShp: TypeAlias = Annotated[SHP_LOOP_SHP, Title('Shipped/Received Information'), Usage('R'), Position(470), Syntax(['C0102', 'L030405', 'C0403']), Required(True)]
    shp: Annotated[list[ItemShp], MaxItems(99)]
    
    ref: Annotated[SHP_LOOP_REF, Title('Reference Identification'), Usage('S'), Position(480), Syntax(['R0203']), Required(True)]


class LIN_LOOP(Loop):
    ItemLin: TypeAlias = Annotated[LIN_LOOP_LIN, Title('Item Identification'), Usage('R'), Position(10), Syntax(['P0405']), Required(True)]
    lin: Annotated[list[ItemLin], MinItems(1)]
    
    uit: Annotated[LIN_LOOP_UIT, Title('Unit Detail'), Usage('R'), Position(20), Syntax(['C0302']), Required(True)]
    ItemPid: TypeAlias = Annotated[LIN_LOOP_PID, Title('Product/Item Description'), Usage('S'), Position(30), Required(True)]
    pid: Annotated[list[ItemPid], MaxItems(1000)]
    ItemAth: TypeAlias = Annotated[LIN_LOOP_ATH, Title('Resource Authorization'), Usage('S'), Position(230), Syntax(['R0203', 'C0305', 'C0405']), Required(True)]
    ath: Annotated[list[ItemAth], MaxItems(20)]
    ItemFst_Loop: TypeAlias = Annotated[FST_LOOP, Title('Forecast'), Usage('R'), Position(410), Required(True)]
    fst_loop: Annotated[list[ItemFst_Loop], MinItems(1)]
    ItemShp_Loop: TypeAlias = Annotated[SHP_LOOP, Title('Ship/RecInfo'), Usage('R'), Position(470), Required(True)]
    shp_loop: Annotated[list[ItemShp_Loop], MinItems(1)]


class DETAIL(Loop):
    ItemLin_Loop: TypeAlias = Annotated[LIN_LOOP, Title('Line Item'), Usage('R'), Position(10), Required(True)]
    lin_loop: Annotated[list[ItemLin_Loop], MinItems(1)]


class FOOTER_CTT(Segment):
    """Transaction Totals"""
    _segment_name = 'CTT'
    
    ctt01: Annotated[D_354, Title('Number of Line Items'), Usage('R'), Position(1)]
    
    ctt02: Annotated[D_347, Title('Hash Total'), Usage('S'), Position(2)]


class FOOTER(Loop):
    
    ctt: Annotated[FOOTER_CTT, Title('Transaction Totals'), Usage('S'), Position(10), Syntax(['P0304']), Required(True)]


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(10), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Table 1 - Header'), Usage('R'), Position(10), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('R'), Position(10), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('R'), Position(10)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(20), Required(True)]


class GS_LOOP_GE(Segment):
    """Functional Group Trailer"""
    _segment_name = 'GE'
    
    ge01: Annotated[D_97, Title('Number of Transaction Sets Included'), Usage('R'), Position(1)]
    
    ge02: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(2)]


class GS_LOOP(Loop):
    
    gs: Annotated[GS_LOOP_GS, Title('Functional Group Header'), Usage('R'), Position(20), Required(True)]
    ItemSt_Loop: TypeAlias = Annotated[ST_LOOP, Title('Transaction Set Header'), Usage('R'), Position(20), Required(True)]
    st_loop: Annotated[list[ItemSt_Loop], MinItems(1)]
    
    ge: Annotated[GS_LOOP_GE, Title('Functional Group Trailer'), Usage('R'), Position(30), Required(True)]


class ISA_LOOP_IEA(Segment):
    """Interchange Control Trailer"""
    _segment_name = 'IEA'
    
    iea01: Annotated[I16, Title('Number of Included Functional Groups'), Usage('R'), Position(1)]
    
    iea02: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(2)]


class ISA_LOOP(Loop):
    
    isa: Annotated[ISA_LOOP_ISA, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    ItemGs_Loop: TypeAlias = Annotated[GS_LOOP, Title('Functional Group Header'), Usage('R'), Position(20), Required(True)]
    gs_loop: Annotated[list[ItemGs_Loop], MinItems(1)]
    
    iea: Annotated[ISA_LOOP_IEA, Title('Interchange Control Trailer'), Usage('R'), Position(40), Required(True)]


class MSG830(Message):
    """Forecast with Release capability - 830"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
