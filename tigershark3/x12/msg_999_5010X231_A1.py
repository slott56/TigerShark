"""
999.5010X231.A1
Created 2023-05-19 10:17:36.462416
"""
from .base import *
from .common import *


class ISA_LOOP_ISA(Segment):
    """Interchange Control Header"""
    _segment_name = 'ISA'
    
    isa01: Annotated[I01, Title('Authorization Information Qualifier'), Usage('R'), Position(1), Enumerated(*['00', '01', '02', '03', '04', '05', '06'])]
    
    isa02: Annotated[I02, Title('Authorization Information'), Usage('R'), Position(2)]
    
    isa03: Annotated[I03, Title('Security Information Qualifier'), Usage('R'), Position(3), Enumerated(*['00', '01'])]
    
    isa04: Annotated[I04, Title('Security Information'), Usage('R'), Position(4)]
    
    isa05: Annotated[I05, Title('Interchange ID Qualifier'), Usage('R'), Position(5)]
    
    isa06: Annotated[I06, Title('Interchange Sender ID'), Usage('R'), Position(6)]
    
    isa07: Annotated[I05, Title('Interchange ID Qualifier'), Usage('R'), Position(7)]
    
    isa08: Annotated[I07, Title('Interchange Receiver ID'), Usage('R'), Position(8)]
    
    isa09: Annotated[I08, Title('Interchange Date'), Usage('R'), Position(9)]
    
    isa10: Annotated[I09, Title('Interchange Time'), Usage('R'), Position(10)]
    
    isa11: Annotated[I65, Title('Repetition Separator'), Usage('R'), Position(11)]
    
    isa12: Annotated[I11, Title('Interchange Control Version Number'), Usage('R'), Position(12), Enumerated(*['00501'])]
    
    isa13: Annotated[I12, Title('Interchange Control Number'), Usage('R'), Position(13)]
    
    isa14: Annotated[I13, Title('Acknowledgment Requested'), Usage('R'), Position(14), Enumerated(*['0', '1'])]
    
    isa15: Annotated[I14, Title('Usage Indicator'), Usage('R'), Position(15), Enumerated(*['I', 'P', 'T'])]
    
    isa16: Annotated[I15, Title('Component Element Separator'), Usage('R'), Position(16)]


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    _segment_name = 'GS'
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['FA'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['005010X231A1'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['999'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]
    
    st03: Annotated[D_1705, Title('Implementation Convention Reference'), Usage('R'), Position(3), Enumerated(*['005010X231A1'])]


class HEADER_AK1(Segment):
    """Functional Group Response Header"""
    _segment_name = 'AK1'
    
    ak101: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['BE', 'HB', 'HC', 'HI', 'HN', 'HP', 'HR', 'HS', 'RA'])]
    
    ak102: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(2)]
    
    ak103: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(3)]


class L2000_AK2(Segment):
    """Transaction Set Response Header"""
    _segment_name = 'AK2'
    
    ak201: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['270', '271', '276', '277', '278', '820', '834', '835', '837'])]
    
    ak202: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]
    
    ak203: Annotated[D_1705, Title('Implementation Convention Reference'), Usage('S'), Position(3)]


class L2100_IK3(Segment):
    """Error Identification"""
    _segment_name = 'IK3'
    
    ik301: Annotated[D_721, Title('Segment ID Code'), Usage('R'), Position(1)]
    
    ik302: Annotated[D_719, Title('Segment Position in Transaction Set'), Usage('R'), Position(2)]
    
    ik303: Annotated[D_447, Title('Loop Identifier Code'), Usage('S'), Position(3)]
    
    ik304: Annotated[D_620, Title('Segment Syntax Error Code'), Usage('S'), Position(4), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', 'I4', 'I6', 'I7', 'I8', 'I9'])]


class L2100_C998(Composite):
    """Context Identification"""
    
    ctx01_01: Annotated[D_9999, Title('Context Name'), Usage('R'), Position(1), Enumerated(*['SITUATIONAL TRIGGER'])]
    
    ctx01_02: Annotated[D_9998, Title('Context Reference'), Usage('N'), Position(2)]


class L2100_C030(Composite):
    """Position in Segment"""
    
    ctx05_01: Annotated[D_722, Title('Element Position in Segment'), Usage('R'), Position(1)]
    
    ctx05_02: Annotated[D_1528, Title('Component Data Element Position in Composite'), Usage('S'), Position(2)]
    
    ctx05_03: Annotated[D_1686, Title('Repeating Data Element Position'), Usage('S'), Position(3)]


class L2100_C999(Composite):
    """Reference in Segment"""
    
    ctx06_01: Annotated[D_725, Title('Data Element Reference Number'), Usage('R'), Position(1)]
    
    ctx06_02: Annotated[D_725, Title('Data Element Reference Number'), Usage('N'), Position(2)]


class L2100_CTX(Segment):
    """Segment Context"""
    _segment_name = 'CTX'
    ItemC998: TypeAlias = Annotated[L2100_C998, Title('Context Identification'), Usage('R'), Position(1), Required(True)]
    c998: Annotated[list[ItemC998], MaxItems(10)]
    
    ctx02: Annotated[D_721, Title('Segment ID Code'), Usage('R'), Position(2)]
    
    ctx03: Annotated[D_719, Title('Segment Position in Transaction Set'), Usage('R'), Position(3)]
    
    ctx04: Annotated[D_447, Title('Loop Identifier Code'), Usage('S'), Position(4)]
    
    c030: Annotated[L2100_C030, Title('Position in Segment'), Usage('S'), Position(5), Required(True)]
    
    c999: Annotated[L2100_C999, Title('Reference in Segment'), Usage('S'), Position(6), Required(True)]


class L2100_C998(Composite):
    """Context Identification"""
    
    ctx01_01: Annotated[D_9999, Title('Context Name'), Usage('R'), Position(1), Enumerated(*['TRN02', 'NM109', 'PATIENT NAME NM109', 'SUBSCRIBER NAME NM109', 'ENT01', 'SUBSCRIBER NUMBER REF02', 'CLM01'])]
    
    ctx01_02: Annotated[D_9998, Title('Context Reference'), Usage('R'), Position(2)]


class L2100_C030(Composite):
    """Position in Segment"""
    
    ctx05_01: Annotated[D_722, Title('Element Position in Segment'), Usage('R'), Position(1)]
    
    ctx05_02: Annotated[D_1528, Title('Component Data Element Position in Composite'), Usage('S'), Position(2)]
    
    ctx05_03: Annotated[D_1686, Title('Repeating Data Element Position'), Usage('S'), Position(3)]


class L2100_C999(Composite):
    """Reference in Segment"""
    
    ctx06_01: Annotated[D_725, Title('Data Element Reference Number'), Usage('R'), Position(1)]
    
    ctx06_02: Annotated[D_725, Title('Data Element Reference Number'), Usage('N'), Position(2)]


class L2100_CTX(Segment):
    """Business Unit Identifier"""
    _segment_name = 'CTX'
    ItemC998: TypeAlias = Annotated[L2100_C998, Title('Context Identification'), Usage('R'), Position(1), Required(True)]
    c998: Annotated[list[ItemC998], MaxItems(10)]
    
    ctx02: Annotated[D_721, Title('Segment ID Code'), Usage('N'), Position(2)]
    
    ctx03: Annotated[D_719, Title('Segment Position in Transaction Set'), Usage('N'), Position(3)]
    
    ctx04: Annotated[D_447, Title('Loop Identifier Code'), Usage('N'), Position(4)]
    
    c030: Annotated[L2100_C030, Title('Position in Segment'), Usage('S'), Position(5), Required(True)]
    
    c999: Annotated[L2100_C999, Title('Reference in Segment'), Usage('N'), Position(6), Required(True)]


class L2110_C030(Composite):
    """Position in Segment"""
    
    ik401_01: Annotated[D_722, Title('Element Position in Segment'), Usage('R'), Position(1)]
    
    ik401_02: Annotated[D_1528, Title('Component Data Element Position in Composite'), Usage('S'), Position(2)]
    
    ik401_03: Annotated[D_1686, Title('Repeating Data Element Position'), Usage('S'), Position(3)]


class L2110_IK4(Segment):
    """Implementation Data Element Note"""
    _segment_name = 'IK4'
    
    c030: Annotated[L2110_C030, Title('Position in Segment'), Usage('R'), Position(1), Required(True)]
    
    ik402: Annotated[D_725, Title('Data Element Reference Number'), Usage('S'), Position(2)]
    
    ik403: Annotated[D_621, Title('Implementation Data Element Syntax Error Code'), Usage('R'), Position(3), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'I10', 'I11', 'I12', 'I13', 'I6', 'I9'])]
    
    ik404: Annotated[D_724, Title('Copy of Bad Data Element'), Usage('S'), Position(4)]


class L2110_C998(Composite):
    """Context Identification"""
    
    ctx01_01: Annotated[D_9999, Title('Context Name'), Usage('R'), Position(1), Enumerated(*['SITUATIONAL TRIGGER'])]
    
    ctx01_02: Annotated[D_9998, Title('Context Reference'), Usage('N'), Position(2)]


class L2110_C030(Composite):
    """Position in Segment"""
    
    ctx05_01: Annotated[D_722, Title('Element Position in Segment'), Usage('R'), Position(1)]
    
    ctx05_02: Annotated[D_1528, Title('Component Data Element Position in Composite'), Usage('S'), Position(2)]
    
    ctx05_03: Annotated[D_1686, Title('Repeating Data Element Position'), Usage('S'), Position(3)]


class L2110_C999(Composite):
    """Reference in Segment"""
    
    ctx06_01: Annotated[D_725, Title('Data Element Reference Number'), Usage('R'), Position(1)]
    
    ctx06_02: Annotated[D_725, Title('Data Element Reference Number'), Usage('N'), Position(2)]


class L2110_CTX(Segment):
    """Element Context"""
    _segment_name = 'CTX'
    ItemC998: TypeAlias = Annotated[L2110_C998, Title('Context Identification'), Usage('R'), Position(1), Required(True)]
    c998: Annotated[list[ItemC998], MaxItems(10)]
    
    ctx02: Annotated[D_721, Title('Segment ID Code'), Usage('R'), Position(2)]
    
    ctx03: Annotated[D_719, Title('Segment Position in Transaction Set'), Usage('R'), Position(3)]
    
    ctx04: Annotated[D_447, Title('Loop Identifier Code'), Usage('S'), Position(4)]
    
    c030: Annotated[L2110_C030, Title('Position in Segment'), Usage('S'), Position(5), Required(True)]
    
    c999: Annotated[L2110_C999, Title('Reference in Segment'), Usage('S'), Position(6), Required(True)]


class L2110(Loop):
    
    ik4: Annotated[L2110_IK4, Title('Implementation Data Element Note'), Usage('S'), Position(600), Required(True)]
    ItemCtx: TypeAlias = Annotated[L2110_CTX, Title('Element Context'), Usage('S'), Position(700), Required(True)]
    ctx: Annotated[list[ItemCtx], MaxItems(10)]


class L2100(Loop):
    
    ik3: Annotated[L2100_IK3, Title('Error Identification'), Usage('R'), Position(400), Required(True)]
    ItemCtx: TypeAlias = Annotated[L2100_CTX, Title('Segment Context'), Usage('S'), Position(500), Required(True)]
    ctx: Annotated[list[ItemCtx], MaxItems(9)]
    
    ctx: Annotated[L2100_CTX, Title('Business Unit Identifier'), Usage('S'), Position(500), Required(True)]
    ItemL2110: TypeAlias = Annotated[L2110, Title('AK2/IK3/IK4 Implementation Data Element Note'), Usage('S'), Position(600)]
    l2110: Annotated[list[ItemL2110], MinItems(1)]


class L2000_IK5(Segment):
    """Transaction Set Response Trailer"""
    _segment_name = 'IK5'
    
    ik501: Annotated[D_717, Title('Transaction Set Acknowledgment Code'), Usage('R'), Position(1), Enumerated(*['A', 'E', 'M', 'R', 'W', 'X'])]
    
    ik502: Annotated[D_618, Title('Implementation Transaction Set Syntax Error Code'), Usage('S'), Position(2), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '23', '24', '25', '26', '27', 'I5', 'I6'])]
    
    ik503: Annotated[D_618, Title('Implementation Transaction Set Syntax Error Code'), Usage('S'), Position(3), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '23', '24', '25', '26', '27', 'I5', 'I6'])]
    
    ik504: Annotated[D_618, Title('Implementation Transaction Set Syntax Error Code'), Usage('S'), Position(4), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '23', '24', '25', '26', '27', 'I5', 'I6'])]
    
    ik505: Annotated[D_618, Title('Implementation Transaction Set Syntax Error Code'), Usage('S'), Position(5), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '23', '24', '25', '26', '27', 'I5', 'I6'])]
    
    ik506: Annotated[D_618, Title('Implementation Transaction Set Syntax Error Code'), Usage('S'), Position(6), Enumerated(*['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '16', '17', '18', '19', '23', '24', '25', '26', '27', 'I5', 'I6'])]


class L2000(Loop):
    
    ak2: Annotated[L2000_AK2, Title('Transaction Set Response Header'), Usage('R'), Position(300), Required(True)]
    ItemL2100: TypeAlias = Annotated[L2100, Title('AK2/IK3 Error Identification'), Usage('S'), Position(400), Required(True)]
    l2100: Annotated[list[ItemL2100], MinItems(1)]
    
    ik5: Annotated[L2000_IK5, Title('Transaction Set Response Trailer'), Usage('R'), Position(800), Required(True)]


class HEADER_AK9(Segment):
    """Functional Group Response Trailer"""
    _segment_name = 'AK9'
    
    ak901: Annotated[D_715, Title('Functional Group Acknowledge Code'), Usage('R'), Position(1), Enumerated(*['A', 'E', 'M', 'P', 'R', 'W', 'X'])]
    
    ak902: Annotated[D_97, Title('Number of Transaction Sets Included'), Usage('R'), Position(2)]
    
    ak903: Annotated[D_123, Title('Number of Received Transaction Sets'), Usage('R'), Position(3)]
    
    ak904: Annotated[D_2, Title('Number of Accepted Transaction Sets'), Usage('R'), Position(4)]
    
    ak905: Annotated[D_716, Title('Functional Group Syntax Error Code'), Usage('S'), Position(5), Enumerated(*['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26'])]
    
    ak906: Annotated[D_716, Title('Functional Group Syntax Error Code'), Usage('S'), Position(6), Enumerated(*['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26'])]
    
    ak907: Annotated[D_716, Title('Functional Group Syntax Error Code'), Usage('S'), Position(7), Enumerated(*['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26'])]
    
    ak908: Annotated[D_716, Title('Functional Group Syntax Error Code'), Usage('S'), Position(8), Enumerated(*['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26'])]
    
    ak909: Annotated[D_716, Title('Functional Group Syntax Error Code'), Usage('S'), Position(9), Enumerated(*['1', '2', '3', '4', '5', '6', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26'])]


class HEADER(Loop):
    
    ak1: Annotated[HEADER_AK1, Title('Functional Group Response Header'), Usage('R'), Position(200), Required(True)]
    ItemL2000: TypeAlias = Annotated[L2000, Title('Transaction Set Response Header'), Usage('S'), Position(300), Required(True)]
    l2000: Annotated[list[ItemL2000], MinItems(1)]
    
    ak9: Annotated[HEADER_AK9, Title('Functional Group Response Trailer'), Usage('R'), Position(900), Required(True)]


class DETAIL(Loop):
    pass


class FOOTER(Loop):
    pass


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Number of Included Segments'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(50), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Table 1 - Header'), Usage('R'), Position(100), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('N'), Position(200)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('N'), Position(300)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(800), Required(True)]


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


class MSG999(Message):
    """HIPAA Implementation Acknowledgment 999"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(10), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
