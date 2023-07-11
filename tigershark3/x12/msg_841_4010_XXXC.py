"""
841.4010.XXXC
Created 2023-05-19 10:17:36.452937
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
    
    gs01: Annotated[D_479, Title('Functional Identifier Code'), Usage('R'), Position(1), Enumerated(*['SP'])]
    
    gs02: Annotated[D_142, Title("Application Sender's Code"), Usage('R'), Position(2)]
    
    gs03: Annotated[D_124, Title("Application Receiver's Code"), Usage('R'), Position(3)]
    
    gs04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    gs05: Annotated[D_337, Title('Time'), Usage('R'), Position(5)]
    
    gs06: Annotated[D_28, Title('Group Control Number'), Usage('R'), Position(6)]
    
    gs07: Annotated[D_455, Title('Responsible Agency Code'), Usage('R'), Position(7), Enumerated(*['X'])]
    
    gs08: Annotated[D_480, Title('Version / Release / Industry Identifier Code'), Usage('R'), Position(8), Enumerated(*['004010XXXC'])]


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    _segment_name = 'ST'
    
    st01: Annotated[D_143, Title('Transaction Set Identifier Code'), Usage('R'), Position(1), Enumerated(*['841'])]
    
    st02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class L1000_SPI(Segment):
    """Code List"""
    _segment_name = 'SPI'
    
    spi01: Annotated[D_786, Title('Security Level Code'), Usage('R'), Position(1), Enumerated(*['00'])]
    
    spi02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('N'), Position(2)]
    
    spi03: Annotated[D_127, Title('Reference Identification'), Usage('N'), Position(3)]
    
    spi04: Annotated[D_790, Title('Entity Title'), Usage('R'), Position(4)]
    
    spi05: Annotated[D_791, Title('Entity Purpose'), Usage('R'), Position(5)]
    
    spi06: Annotated[D_792, Title('Entity Status Code'), Usage('N'), Position(6)]
    
    spi07: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('N'), Position(7)]
    
    spi08: Annotated[D_755, Title('Report Type Code'), Usage('N'), Position(8)]
    
    spi09: Annotated[D_786, Title('Security Level Code'), Usage('N'), Position(9)]
    
    spi10: Annotated[D_559, Title('Agency Qualifier Code'), Usage('N'), Position(10)]
    
    spi11: Annotated[D_822, Title('Source Subqualifier'), Usage('N'), Position(11)]
    
    spi12: Annotated[D_554, Title('Assigned Number'), Usage('N'), Position(12)]
    
    spi13: Annotated[D_1322, Title('Certification Type Code'), Usage('N'), Position(13)]
    
    spi14: Annotated[D_1401, Title('Proposal Data Detail Identifier Code'), Usage('N'), Position(14)]
    
    spi15: Annotated[D_1005, Title('Heirarchal Structure Code'), Usage('N'), Position(15)]


class L1000_RDT(Segment):
    """Release Date"""
    _segment_name = 'RDT'
    
    rdt01: Annotated[D_795, Title('Revision Level Code'), Usage('N'), Position(1)]
    
    rdt02: Annotated[D_796, Title('Revision Value'), Usage('N'), Position(2)]
    
    rdt03: Annotated[D_374, Title('Date/Time Qualifier'), Usage('R'), Position(3), Enumerated(*['171'])]
    
    rdt04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    rdt05: Annotated[D_337, Title('Time'), Usage('N'), Position(5)]
    
    rdt06: Annotated[D_623, Title('Time Code'), Usage('N'), Position(6)]


class L1000_RDT(Segment):
    """Effective Date"""
    _segment_name = 'RDT'
    
    rdt01: Annotated[D_795, Title('Revision Level Code'), Usage('N'), Position(1)]
    
    rdt02: Annotated[D_796, Title('Revision Value'), Usage('N'), Position(2)]
    
    rdt03: Annotated[D_374, Title('Date/Time Qualifier'), Usage('R'), Position(3), Enumerated(*['007'])]
    
    rdt04: Annotated[D_373, Title('Date'), Usage('R'), Position(4)]
    
    rdt05: Annotated[D_337, Title('Time'), Usage('N'), Position(5)]
    
    rdt06: Annotated[D_623, Title('Time Code'), Usage('N'), Position(6)]


class L1100_N1(Segment):
    """Code List Source"""
    _segment_name = 'N1'
    
    n101: Annotated[D_98, Title('Entity Identifier Code'), Usage('R'), Position(1), Enumerated(*['0F'])]
    
    n102: Annotated[D_93, Title('Name'), Usage('R'), Position(2)]
    
    n103: Annotated[D_66, Title('Identification Code Qualifier'), Usage('N'), Position(3)]
    
    n104: Annotated[D_67, Title('Identification Code'), Usage('N'), Position(4)]
    
    n105: Annotated[D_706, Title('Entity Relationship Code'), Usage('N'), Position(5)]
    
    n106: Annotated[D_98, Title('Entity Identifier Code'), Usage('N'), Position(6)]


class L1100(Loop):
    
    n1: Annotated[L1100_N1, Title('Code List Source'), Usage('S'), Position(120), Syntax(['R0203', 'P0304']), Required(True)]


class L1000(Loop):
    
    spi: Annotated[L1000_SPI, Title('Code List'), Usage('R'), Position(20), Syntax(['P0203']), Required(True)]
    ItemRdt: TypeAlias = Annotated[L1000_RDT, Title('Release Date'), Usage('R'), Position(30), Syntax(['C0102', 'L030405', 'C0605']), Required(True)]
    rdt: Annotated[list[ItemRdt], MinItems(1)]
    
    rdt: Annotated[L1000_RDT, Title('Effective Date'), Usage('S'), Position(30), Syntax(['C0102', 'L030405', 'C0605']), Required(True)]
    ItemL1100: TypeAlias = Annotated[L1100, Title('Code List Source'), Usage('R'), Position(40)]
    l1100: Annotated[list[ItemL1100], MinItems(1)]


class HEADER(Loop):
    ItemL1000: TypeAlias = Annotated[L1000, Title('Code List'), Usage('R'), Position(10), Required(True)]
    l1000: Annotated[list[ItemL1000], MinItems(1)]


class L2000_HL(Segment):
    """Code List Header"""
    _segment_name = 'HL'
    
    hl01: Annotated[D_628, Title('Hierarchical ID Number'), Usage('R'), Position(1), Enumerated(*['1'])]
    
    hl02: Annotated[D_734, Title('Hierarchical Parent ID Number'), Usage('N'), Position(2)]
    
    hl03: Annotated[D_735, Title('Hierarchical Level Code'), Usage('R'), Position(3), Enumerated(*['I'])]
    
    hl04: Annotated[D_736, Title('Hierarchical Child Code'), Usage('N'), Position(4)]


class L2100_SPI(Segment):
    """Code List Value and Definition"""
    _segment_name = 'SPI'
    
    spi01: Annotated[D_786, Title('Security Level Code'), Usage('R'), Position(1), Enumerated(*['00'])]
    
    spi02: Annotated[D_128, Title('Reference Identification Qualifier'), Usage('R'), Position(2), Enumerated(*['ZZ'])]
    
    spi03: Annotated[D_127, Title('Reference Identification'), Usage('R'), Position(3)]
    
    spi04: Annotated[D_790, Title('Entity Title'), Usage('R'), Position(4)]
    
    spi05: Annotated[D_791, Title('Entity Purpose'), Usage('N'), Position(5)]
    
    spi06: Annotated[D_792, Title('Entity Status Code'), Usage('N'), Position(6)]
    
    spi07: Annotated[D_353, Title('Transaction Set Purpose Code'), Usage('N'), Position(7)]
    
    spi08: Annotated[D_755, Title('Report Type Code'), Usage('N'), Position(8)]
    
    spi09: Annotated[D_786, Title('Security Level Code'), Usage('N'), Position(9)]
    
    spi10: Annotated[D_559, Title('Agency Qualifier Code'), Usage('N'), Position(10)]
    
    spi11: Annotated[D_822, Title('Source Subqualifier'), Usage('N'), Position(11)]
    
    spi12: Annotated[D_554, Title('Assigned Number'), Usage('N'), Position(12)]
    
    spi13: Annotated[D_1322, Title('Certification Type Code'), Usage('N'), Position(13)]
    
    spi14: Annotated[D_1401, Title('Proposal Data Detail Identifier Code'), Usage('N'), Position(14)]
    
    spi15: Annotated[D_1005, Title('Heirarchal Structure Code'), Usage('N'), Position(15)]


class L2100_MSG(Segment):
    """Additional Text"""
    _segment_name = 'MSG'
    
    msg01: Annotated[D_933, Title('Free-Form Text Message'), Usage('R'), Position(1)]
    
    msg02: Annotated[D_934, Title('Printer Carriage Control Code'), Usage('N'), Position(2)]
    
    msg03: Annotated[D_1470, Title('Number'), Usage('N'), Position(3)]


class L2100(Loop):
    
    spi: Annotated[L2100_SPI, Title('Code List Value and Definition'), Usage('R'), Position(20), Syntax(['P0203']), Required(True)]
    ItemMsg: TypeAlias = Annotated[L2100_MSG, Title('Additional Text'), Usage('S'), Position(50), Syntax(['C0302']), Required(True)]
    msg: Annotated[list[ItemMsg], MinItems(1)]


class L2000(Loop):
    
    hl: Annotated[L2000_HL, Title('Code List Header'), Usage('R'), Position(10), Required(True)]
    ItemL2100: TypeAlias = Annotated[L2100, Title('Code List Value and Definition'), Usage('R'), Position(10), Required(True)]
    l2100: Annotated[list[ItemL2100], MinItems(1)]


class DETAIL(Loop):
    ItemL2000: TypeAlias = Annotated[L2000, Title('Code List Header'), Usage('R'), Position(10), Required(True)]
    l2000: Annotated[list[ItemL2000], MinItems(1)]


class FOOTER(Loop):
    pass


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    _segment_name = 'SE'
    
    se01: Annotated[D_96, Title('Transaction Segment Count'), Usage('R'), Position(1)]
    
    se02: Annotated[D_329, Title('Transaction Set Control Number'), Usage('R'), Position(2)]


class ST_LOOP(Loop):
    
    st: Annotated[ST_LOOP_ST, Title('Transaction Set Header'), Usage('R'), Position(5), Required(True)]
    ItemHeader: TypeAlias = Annotated[HEADER, Title('Table 1 - Header'), Usage('R'), Position(10), Required(True)]
    header: Annotated[list[ItemHeader], MinItems(1)]
    ItemDetail: TypeAlias = Annotated[DETAIL, Title('Table 2 - Detail'), Usage('S'), Position(20), Required(True)]
    detail: Annotated[list[ItemDetail], MinItems(1)]
    ItemFooter: TypeAlias = Annotated[FOOTER, Title('Table 3 - Footer'), Usage('N'), Position(30)]
    footer: Annotated[list[ItemFooter], MinItems(1)]
    
    se: Annotated[ST_LOOP_SE, Title('Transaction Set Trailer'), Usage('R'), Position(210), Required(True)]


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


class MSG841(Message):
    """HIPAA Related Code Lists"""
    ItemIsa_Loop: TypeAlias = Annotated[ISA_LOOP, Title('Interchange Control Header'), Usage('R'), Position(1), Required(True)]
    isa_loop: Annotated[list[ItemIsa_Loop], MinItems(1)]
