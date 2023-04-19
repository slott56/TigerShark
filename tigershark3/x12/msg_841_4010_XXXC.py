"""
841.4010.XXXC
Created 2023-03-25 09:22:30.298789
"""
from .base import *
from . import common


class ISA_LOOP_ISA01(Element):
    """Authorization Information Qualifier"""
    class Schema:
        json = {'title': 'Authorization Information Qualifier',
         'usage': 'R',
         'description': 'xid=ISA01 data_ele=I01',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/I01'}, {'enum': ['00', '03']}]}}
        datatype = common.I01
        codes = ['00', '03']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA02(Element):
    """Authorization Information"""
    class Schema:
        json = {'title': 'Authorization Information',
         'usage': 'R',
         'description': 'xid=ISA02 data_ele=I02',
         'sequence': 2,
         'type': {'$ref': '#/$common/I02'}}
        datatype = common.I02
        min_len = 10
        max_len = 10


class ISA_LOOP_ISA03(Element):
    """Security Information Qualifier"""
    class Schema:
        json = {'title': 'Security Information Qualifier',
         'usage': 'R',
         'description': 'xid=ISA03 data_ele=I03',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/I03'}, {'enum': ['00', '01']}]}}
        datatype = common.I03
        codes = ['00', '01']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA04(Element):
    """Security Information"""
    class Schema:
        json = {'title': 'Security Information',
         'usage': 'R',
         'description': 'xid=ISA04 data_ele=I04',
         'sequence': 4,
         'type': {'$ref': '#/$common/I04'}}
        datatype = common.I04
        min_len = 10
        max_len = 10


class ISA_LOOP_ISA05(Element):
    """Interchange ID Qualifier"""
    class Schema:
        json = {'title': 'Interchange ID Qualifier',
         'usage': 'R',
         'description': 'xid=ISA05 data_ele=I05',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/I05'},
                            {'enum': ['01', '14', '20', '27', '28', '29', '30', '33',
                                      'ZZ']}]}}
        datatype = common.I05
        codes = ['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA06(Element):
    """Interchange Sender ID"""
    class Schema:
        json = {'title': 'Interchange Sender ID',
         'usage': 'R',
         'description': 'xid=ISA06 data_ele=I06',
         'sequence': 6,
         'type': {'$ref': '#/$common/I06'}}
        datatype = common.I06
        min_len = 15
        max_len = 15


class ISA_LOOP_ISA07(Element):
    """Interchange ID Qualifier"""
    class Schema:
        json = {'title': 'Interchange ID Qualifier',
         'usage': 'R',
         'description': 'xid=ISA07 data_ele=I05',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/I05'},
                            {'enum': ['01', '14', '20', '27', '28', '29', '30', '33',
                                      'ZZ']}]}}
        datatype = common.I05
        codes = ['01', '14', '20', '27', '28', '29', '30', '33', 'ZZ']
        min_len = 2
        max_len = 2


class ISA_LOOP_ISA08(Element):
    """Interchange Receiver ID"""
    class Schema:
        json = {'title': 'Interchange Receiver ID',
         'usage': 'R',
         'description': 'xid=ISA08 data_ele=I07',
         'sequence': 8,
         'type': {'$ref': '#/$common/I07'}}
        datatype = common.I07
        min_len = 15
        max_len = 15


class ISA_LOOP_ISA09(Element):
    """Interchange Date"""
    class Schema:
        json = {'title': 'Interchange Date',
         'usage': 'R',
         'description': 'xid=ISA09 data_ele=I08',
         'sequence': 9,
         'type': {'$ref': '#/$common/I08'}}
        datatype = common.I08
        min_len = 6
        max_len = 6


class ISA_LOOP_ISA10(Element):
    """Interchange Time"""
    class Schema:
        json = {'title': 'Interchange Time',
         'usage': 'R',
         'description': 'xid=ISA10 data_ele=I09',
         'sequence': 10,
         'type': {'$ref': '#/$common/I09'}}
        datatype = common.I09
        min_len = 4
        max_len = 4


class ISA_LOOP_ISA11(Element):
    """Interchange Control Standards Identifier"""
    class Schema:
        json = {'title': 'Interchange Control Standards Identifier',
         'usage': 'R',
         'description': 'xid=ISA11 data_ele=I10',
         'sequence': 11,
         'type': {'allOf': [{'$ref': '#/$common/I10'}, {'enum': ['U']}]}}
        datatype = common.I10
        codes = ['U']
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA12(Element):
    """Interchange Control Version Number"""
    class Schema:
        json = {'title': 'Interchange Control Version Number',
         'usage': 'R',
         'description': 'xid=ISA12 data_ele=I11',
         'sequence': 12,
         'type': {'allOf': [{'$ref': '#/$common/I11'}, {'enum': ['00401']}]}}
        datatype = common.I11
        codes = ['00401']
        min_len = 5
        max_len = 5


class ISA_LOOP_ISA13(Element):
    """Interchange Control Number"""
    class Schema:
        json = {'title': 'Interchange Control Number',
         'usage': 'R',
         'description': 'xid=ISA13 data_ele=I12',
         'sequence': 13,
         'type': {'$ref': '#/$common/I12'}}
        datatype = common.I12
        min_len = 9
        max_len = 9


class ISA_LOOP_ISA14(Element):
    """Acknowledgment Requested"""
    class Schema:
        json = {'title': 'Acknowledgment Requested',
         'usage': 'R',
         'description': 'xid=ISA14 data_ele=I13',
         'sequence': 14,
         'type': {'allOf': [{'$ref': '#/$common/I13'}, {'enum': ['0', '1']}]}}
        datatype = common.I13
        codes = ['0', '1']
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA15(Element):
    """Usage Indicator"""
    class Schema:
        json = {'title': 'Usage Indicator',
         'usage': 'R',
         'description': 'xid=ISA15 data_ele=I14',
         'sequence': 15,
         'type': {'allOf': [{'$ref': '#/$common/I14'}, {'enum': ['P', 'T']}]}}
        datatype = common.I14
        codes = ['P', 'T']
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA16(Element):
    """Component Element Separator"""
    class Schema:
        json = {'title': 'Component Element Separator',
         'usage': 'R',
         'description': 'xid=ISA16 data_ele=I15',
         'sequence': 16,
         'type': {'$ref': '#/$common/I15'}}
        datatype = common.I15
        min_len = 1
        max_len = 1


class ISA_LOOP_ISA(Segment):
    """Interchange Control Header"""
    class Schema:
        json = {'title': 'Interchange Control Header',
         'usage': 'R',
         'description': 'xid=ISA name=Interchange Control Header',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'ISA'},
                        'isa01': {'$ref': '#/$elements/ISA_LOOP_ISA01'},
                        'isa02': {'$ref': '#/$elements/ISA_LOOP_ISA02'},
                        'isa03': {'$ref': '#/$elements/ISA_LOOP_ISA03'},
                        'isa04': {'$ref': '#/$elements/ISA_LOOP_ISA04'},
                        'isa05': {'$ref': '#/$elements/ISA_LOOP_ISA05'},
                        'isa06': {'$ref': '#/$elements/ISA_LOOP_ISA06'},
                        'isa07': {'$ref': '#/$elements/ISA_LOOP_ISA07'},
                        'isa08': {'$ref': '#/$elements/ISA_LOOP_ISA08'},
                        'isa09': {'$ref': '#/$elements/ISA_LOOP_ISA09'},
                        'isa10': {'$ref': '#/$elements/ISA_LOOP_ISA10'},
                        'isa11': {'$ref': '#/$elements/ISA_LOOP_ISA11'},
                        'isa12': {'$ref': '#/$elements/ISA_LOOP_ISA12'},
                        'isa13': {'$ref': '#/$elements/ISA_LOOP_ISA13'},
                        'isa14': {'$ref': '#/$elements/ISA_LOOP_ISA14'},
                        'isa15': {'$ref': '#/$elements/ISA_LOOP_ISA15'},
                        'isa16': {'$ref': '#/$elements/ISA_LOOP_ISA16'}},
         'required': ['isa01', 'isa02', 'isa03', 'isa04', 'isa05', 'isa06', 'isa07',
                      'isa08', 'isa09', 'isa10', 'isa11', 'isa12', 'isa13', 'isa14',
                      'isa15', 'isa16']}
        segment_name = 'ISA'
    isa01: ISA_LOOP_ISA01
    isa02: ISA_LOOP_ISA02
    isa03: ISA_LOOP_ISA03
    isa04: ISA_LOOP_ISA04
    isa05: ISA_LOOP_ISA05
    isa06: ISA_LOOP_ISA06
    isa07: ISA_LOOP_ISA07
    isa08: ISA_LOOP_ISA08
    isa09: ISA_LOOP_ISA09
    isa10: ISA_LOOP_ISA10
    isa11: ISA_LOOP_ISA11
    isa12: ISA_LOOP_ISA12
    isa13: ISA_LOOP_ISA13
    isa14: ISA_LOOP_ISA14
    isa15: ISA_LOOP_ISA15
    isa16: ISA_LOOP_ISA16


class GS_LOOP_GS01(Element):
    """Functional Identifier Code"""
    class Schema:
        json = {'title': 'Functional Identifier Code',
         'usage': 'R',
         'description': 'xid=GS01 data_ele=479',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/479'}, {'enum': ['SP']}]}}
        datatype = common.D_479
        codes = ['SP']
        min_len = 2
        max_len = 2


class GS_LOOP_GS02(Element):
    """Application Sender's Code"""
    class Schema:
        json = {'title': "Application Sender's Code",
         'usage': 'R',
         'description': 'xid=GS02 data_ele=142',
         'sequence': 2,
         'type': {'$ref': '#/$common/142'}}
        datatype = common.D_142
        min_len = 2
        max_len = 15


class GS_LOOP_GS03(Element):
    """Application Receiver's Code"""
    class Schema:
        json = {'title': "Application Receiver's Code",
         'usage': 'R',
         'description': 'xid=GS03 data_ele=124',
         'sequence': 3,
         'type': {'$ref': '#/$common/124'}}
        datatype = common.D_124
        min_len = 2
        max_len = 15


class GS_LOOP_GS04(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'R',
         'description': 'xid=GS04 data_ele=373',
         'sequence': 4,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class GS_LOOP_GS05(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'R',
         'description': 'xid=GS05 data_ele=337',
         'sequence': 5,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class GS_LOOP_GS06(Element):
    """Group Control Number"""
    class Schema:
        json = {'title': 'Group Control Number',
         'usage': 'R',
         'description': 'xid=GS06 data_ele=28',
         'sequence': 6,
         'type': {'$ref': '#/$common/28'}}
        datatype = common.D_28
        min_len = 1
        max_len = 9


class GS_LOOP_GS07(Element):
    """Responsible Agency Code"""
    class Schema:
        json = {'title': 'Responsible Agency Code',
         'usage': 'R',
         'description': 'xid=GS07 data_ele=455',
         'sequence': 7,
         'type': {'allOf': [{'$ref': '#/$common/455'}, {'enum': ['X']}]}}
        datatype = common.D_455
        codes = ['X']
        min_len = 1
        max_len = 2


class GS_LOOP_GS08(Element):
    """Version / Release / Industry Identifier Code"""
    class Schema:
        json = {'title': 'Version / Release / Industry Identifier Code',
         'usage': 'R',
         'description': 'xid=GS08 data_ele=480',
         'sequence': 8,
         'type': {'allOf': [{'$ref': '#/$common/480'}, {'enum': ['004010XXXC']}]}}
        datatype = common.D_480
        codes = ['004010XXXC']
        min_len = 1
        max_len = 12


class GS_LOOP_GS(Segment):
    """Functional Group Header"""
    class Schema:
        json = {'title': 'Functional Group Header',
         'usage': 'R',
         'description': 'xid=GS name=Functional Group Header',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'GS'},
                        'gs01': {'$ref': '#/$elements/GS_LOOP_GS01'},
                        'gs02': {'$ref': '#/$elements/GS_LOOP_GS02'},
                        'gs03': {'$ref': '#/$elements/GS_LOOP_GS03'},
                        'gs04': {'$ref': '#/$elements/GS_LOOP_GS04'},
                        'gs05': {'$ref': '#/$elements/GS_LOOP_GS05'},
                        'gs06': {'$ref': '#/$elements/GS_LOOP_GS06'},
                        'gs07': {'$ref': '#/$elements/GS_LOOP_GS07'},
                        'gs08': {'$ref': '#/$elements/GS_LOOP_GS08'}},
         'required': ['gs01', 'gs02', 'gs03', 'gs04', 'gs05', 'gs06', 'gs07', 'gs08']}
        segment_name = 'GS'
    gs01: GS_LOOP_GS01
    gs02: GS_LOOP_GS02
    gs03: GS_LOOP_GS03
    gs04: GS_LOOP_GS04
    gs05: GS_LOOP_GS05
    gs06: GS_LOOP_GS06
    gs07: GS_LOOP_GS07
    gs08: GS_LOOP_GS08


class ST_LOOP_ST01(Element):
    """Transaction Set Identifier Code"""
    class Schema:
        json = {'title': 'Transaction Set Identifier Code',
         'usage': 'R',
         'description': 'xid=ST01 data_ele=143',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/143'}, {'enum': ['841']}]}}
        datatype = common.D_143
        codes = ['841']
        min_len = 3
        max_len = 3


class ST_LOOP_ST02(Element):
    """Transaction Set Control Number"""
    class Schema:
        json = {'title': 'Transaction Set Control Number',
         'usage': 'R',
         'description': 'xid=ST02 data_ele=329',
         'sequence': 2,
         'type': {'$ref': '#/$common/329'}}
        datatype = common.D_329
        min_len = 4
        max_len = 9


class ST_LOOP_ST(Segment):
    """Transaction Set Header"""
    class Schema:
        json = {'title': 'Transaction Set Header',
         'usage': 'R',
         'description': 'xid=ST name=Transaction Set Header',
         'position': 5,
         'type': 'object',
         'properties': {'xid': {'literal': 'ST'},
                        'st01': {'$ref': '#/$elements/ST_LOOP_ST01'},
                        'st02': {'$ref': '#/$elements/ST_LOOP_ST02'}},
         'required': ['st01', 'st02']}
        segment_name = 'ST'
    st01: ST_LOOP_ST01
    st02: ST_LOOP_ST02


class L1000_SPI01(Element):
    """Security Level Code"""
    class Schema:
        json = {'title': 'Security Level Code',
         'usage': 'R',
         'description': 'xid=SPI01 data_ele=786',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/786'}, {'enum': ['00']}]}}
        datatype = common.D_786
        codes = ['00']
        min_len = 2
        max_len = 2


class L1000_SPI02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'N',
         'description': 'xid=SPI02 data_ele=128',
         'sequence': 2,
         'type': {'$ref': '#/$common/128'}}
        datatype = common.D_128
        min_len = 2
        max_len = 3


class L1000_SPI03(Element):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'N',
         'description': 'xid=SPI03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L1000_SPI04(Element):
    """Entity Title"""
    class Schema:
        json = {'title': 'Entity Title',
         'usage': 'R',
         'description': 'xid=SPI04 data_ele=790',
         'sequence': 4,
         'type': {'$ref': '#/$common/790'}}
        datatype = common.D_790


class L1000_SPI05(Element):
    """Entity Purpose"""
    class Schema:
        json = {'title': 'Entity Purpose',
         'usage': 'R',
         'description': 'xid=SPI05 data_ele=791',
         'sequence': 5,
         'type': {'$ref': '#/$common/791'}}
        datatype = common.D_791


class L1000_SPI06(Element):
    """Entity Status Code"""
    class Schema:
        json = {'title': 'Entity Status Code',
         'usage': 'N',
         'description': 'xid=SPI06 data_ele=792',
         'sequence': 6,
         'type': {'$ref': '#/$common/792'}}
        datatype = common.D_792


class L1000_SPI07(Element):
    """Transaction Set Purpose Code"""
    class Schema:
        json = {'title': 'Transaction Set Purpose Code',
         'usage': 'N',
         'description': 'xid=SPI07 data_ele=353',
         'sequence': 7,
         'type': {'$ref': '#/$common/353'}}
        datatype = common.D_353
        min_len = 2
        max_len = 2


class L1000_SPI08(Element):
    """Report Type Code"""
    class Schema:
        json = {'title': 'Report Type Code',
         'usage': 'N',
         'description': 'xid=SPI08 data_ele=755',
         'sequence': 8,
         'type': {'$ref': '#/$common/755'}}
        datatype = common.D_755
        min_len = 2
        max_len = 2


class L1000_SPI09(Element):
    """Security Level Code"""
    class Schema:
        json = {'title': 'Security Level Code',
         'usage': 'N',
         'description': 'xid=SPI09 data_ele=786',
         'sequence': 9,
         'type': {'$ref': '#/$common/786'}}
        datatype = common.D_786
        min_len = 2
        max_len = 2


class L1000_SPI10(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=SPI10 data_ele=559',
         'sequence': 10,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L1000_SPI11(Element):
    """Source Subqualifier"""
    class Schema:
        json = {'title': 'Source Subqualifier',
         'usage': 'N',
         'description': 'xid=SPI11 data_ele=822',
         'sequence': 11,
         'type': {'$ref': '#/$common/822'}}
        datatype = common.D_822
        min_len = 1
        max_len = 15


class L1000_SPI12(Element):
    """Assigned Number"""
    class Schema:
        json = {'title': 'Assigned Number',
         'usage': 'N',
         'description': 'xid=SPI12 data_ele=554',
         'sequence': 12,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L1000_SPI13(Element):
    """Certification Type Code"""
    class Schema:
        json = {'title': 'Certification Type Code',
         'usage': 'N',
         'description': 'xid=SPI13 data_ele=1322',
         'sequence': 13,
         'type': {'$ref': '#/$common/1322'}}
        datatype = common.D_1322
        min_len = 1
        max_len = 1


class L1000_SPI14(Element):
    """Proposal Data Detail Identifier Code"""
    class Schema:
        json = {'title': 'Proposal Data Detail Identifier Code',
         'usage': 'N',
         'description': 'xid=SPI14 data_ele=1401',
         'sequence': 14,
         'type': {'$ref': '#/$common/1401'}}
        datatype = common.D_1401


class L1000_SPI15(Element):
    """Heirarchal Structure Code"""
    class Schema:
        json = {'title': 'Heirarchal Structure Code',
         'usage': 'N',
         'description': 'xid=SPI15 data_ele=1005',
         'sequence': 15,
         'type': {'$ref': '#/$common/1005'}}
        datatype = common.D_1005
        min_len = 4
        max_len = 4


class L1000_SPI(Segment):
    """Code List"""
    class Schema:
        json = {'title': 'Code List',
         'usage': 'R',
         'description': 'xid=SPI name=Code List',
         'position': 20,
         'syntax': ['P0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'SPI'},
                        'spi01': {'$ref': '#/$elements/L1000_SPI01'},
                        'spi04': {'$ref': '#/$elements/L1000_SPI04'},
                        'spi05': {'$ref': '#/$elements/L1000_SPI05'}},
         'required': ['spi01', 'spi04', 'spi05']}
        segment_name = 'SPI'
    spi01: L1000_SPI01
    spi04: L1000_SPI04
    spi05: L1000_SPI05


class L1000_RDT01(Element):
    """Revision Level Code"""
    class Schema:
        json = {'title': 'Revision Level Code',
         'usage': 'N',
         'description': 'xid=RDT01 data_ele=795',
         'sequence': 1,
         'type': {'$ref': '#/$common/795'}}
        datatype = common.D_795


class L1000_RDT02(Element):
    """Revision Value"""
    class Schema:
        json = {'title': 'Revision Value',
         'usage': 'N',
         'description': 'xid=RDT02 data_ele=796',
         'sequence': 2,
         'type': {'$ref': '#/$common/796'}}
        datatype = common.D_796


class L1000_RDT03(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'R',
         'description': 'xid=RDT03 data_ele=374',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['171']}]}}
        datatype = common.D_374
        codes = ['171']
        min_len = 3
        max_len = 3


class L1000_RDT04(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'R',
         'description': 'xid=RDT04 data_ele=373',
         'sequence': 4,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L1000_RDT05(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=RDT05 data_ele=337',
         'sequence': 5,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L1000_RDT06(Element):
    """Time Code"""
    class Schema:
        json = {'title': 'Time Code',
         'usage': 'N',
         'description': 'xid=RDT06 data_ele=623',
         'sequence': 6,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L1000_RDT(Segment):
    """Release Date"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Release Date',
                   'usage': 'R',
                   'description': 'xid=RDT name=Release Date',
                   'position': 30,
                   'syntax': ['C0102', 'L030405', 'C0605'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'RDT'},
                                  'rdt03': {'$ref': '#/$elements/L1000_RDT03'},
                                  'rdt04': {'$ref': '#/$elements/L1000_RDT04'}},
                   'required': ['rdt03', 'rdt04']}}
        segment_name = 'RDT'
    rdt03: L1000_RDT03
    rdt04: L1000_RDT04


class L1000_RDT01(Element):
    """Revision Level Code"""
    class Schema:
        json = {'title': 'Revision Level Code',
         'usage': 'N',
         'description': 'xid=RDT01 data_ele=795',
         'sequence': 1,
         'type': {'$ref': '#/$common/795'}}
        datatype = common.D_795


class L1000_RDT02(Element):
    """Revision Value"""
    class Schema:
        json = {'title': 'Revision Value',
         'usage': 'N',
         'description': 'xid=RDT02 data_ele=796',
         'sequence': 2,
         'type': {'$ref': '#/$common/796'}}
        datatype = common.D_796


class L1000_RDT03(Element):
    """Date/Time Qualifier"""
    class Schema:
        json = {'title': 'Date/Time Qualifier',
         'usage': 'R',
         'description': 'xid=RDT03 data_ele=374',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/374'}, {'enum': ['007']}]}}
        datatype = common.D_374
        codes = ['007']
        min_len = 3
        max_len = 3


class L1000_RDT04(Element):
    """Date"""
    class Schema:
        json = {'title': 'Date',
         'usage': 'R',
         'description': 'xid=RDT04 data_ele=373',
         'sequence': 4,
         'type': {'$ref': '#/$common/373'}}
        datatype = common.D_373
        min_len = 8
        max_len = 8


class L1000_RDT05(Element):
    """Time"""
    class Schema:
        json = {'title': 'Time',
         'usage': 'N',
         'description': 'xid=RDT05 data_ele=337',
         'sequence': 5,
         'type': {'$ref': '#/$common/337'}}
        datatype = common.D_337
        min_len = 4
        max_len = 8


class L1000_RDT06(Element):
    """Time Code"""
    class Schema:
        json = {'title': 'Time Code',
         'usage': 'N',
         'description': 'xid=RDT06 data_ele=623',
         'sequence': 6,
         'type': {'$ref': '#/$common/623'}}
        datatype = common.D_623
        min_len = 2
        max_len = 2


class L1000_RDT(Segment):
    """Effective Date"""
    class Schema:
        json = {'title': 'Effective Date',
         'usage': 'S',
         'description': 'xid=RDT name=Effective Date',
         'position': 30,
         'syntax': ['C0102', 'L030405', 'C0605'],
         'type': 'object',
         'properties': {'xid': {'literal': 'RDT'},
                        'rdt03': {'$ref': '#/$elements/L1000_RDT03'},
                        'rdt04': {'$ref': '#/$elements/L1000_RDT04'}},
         'required': ['rdt03', 'rdt04']}
        segment_name = 'RDT'
    rdt03: L1000_RDT03
    rdt04: L1000_RDT04


class L1100_N101(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'R',
         'description': 'xid=N101 data_ele=98',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/98'}, {'enum': ['0F']}]}}
        datatype = common.D_98
        codes = ['0F']
        min_len = 2
        max_len = 3


class L1100_N102(Element):
    """Name"""
    class Schema:
        json = {'title': 'Name',
         'usage': 'R',
         'description': 'xid=N102 data_ele=93',
         'sequence': 2,
         'type': {'$ref': '#/$common/93'}}
        datatype = common.D_93
        min_len = 1
        max_len = 60


class L1100_N103(Element):
    """Identification Code Qualifier"""
    class Schema:
        json = {'title': 'Identification Code Qualifier',
         'usage': 'N',
         'description': 'xid=N103 data_ele=66',
         'sequence': 3,
         'type': {'$ref': '#/$common/66'}}
        datatype = common.D_66
        min_len = 1
        max_len = 2


class L1100_N104(Element):
    """Identification Code"""
    class Schema:
        json = {'title': 'Identification Code',
         'usage': 'N',
         'description': 'xid=N104 data_ele=67',
         'sequence': 4,
         'type': {'$ref': '#/$common/67'}}
        datatype = common.D_67
        min_len = 2
        max_len = 80


class L1100_N105(Element):
    """Entity Relationship Code"""
    class Schema:
        json = {'title': 'Entity Relationship Code',
         'usage': 'N',
         'description': 'xid=N105 data_ele=706',
         'sequence': 5,
         'type': {'$ref': '#/$common/706'}}
        datatype = common.D_706
        min_len = 2
        max_len = 2


class L1100_N106(Element):
    """Entity Identifier Code"""
    class Schema:
        json = {'title': 'Entity Identifier Code',
         'usage': 'N',
         'description': 'xid=N106 data_ele=98',
         'sequence': 6,
         'type': {'$ref': '#/$common/98'}}
        datatype = common.D_98
        min_len = 2
        max_len = 3


class L1100_N1(Segment):
    """Code List Source"""
    class Schema:
        json = {'title': 'Code List Source',
         'usage': 'S',
         'description': 'xid=N1 name=Code List Source',
         'position': 120,
         'syntax': ['R0203', 'P0304'],
         'type': 'object',
         'properties': {'xid': {'literal': 'N1'},
                        'n101': {'$ref': '#/$elements/L1100_N101'},
                        'n102': {'$ref': '#/$elements/L1100_N102'}},
         'required': ['n101', 'n102']}
        segment_name = 'N1'
    n101: L1100_N101
    n102: L1100_N102


class L1100(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Code List Source',
                   'usage': 'R',
                   'description': 'xid=1100 name=Code List Source type=None',
                   'position': 40,
                   'type': 'object',
                   'properties': {'n1': {'$ref': '#/$segments/L1100_N1'}}}}
    n1: L1100_N1 | None


class L1000(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Code List',
                   'usage': 'R',
                   'description': 'xid=1000 name=Code List type=None',
                   'position': 10,
                   'type': 'object',
                   'properties': {'spi': {'$ref': '#/$segments/L1000_SPI'},
                                  'rdt': {'$ref': '#/$segments/L1000_RDT'},
                                  'l1100': {'$ref': '#/$segments/L1100'}},
                   'required': ['spi', 'rdt', 'l1100']}}
    spi: L1000_SPI
    rdt: list[L1000_RDT]
    rdt: L1000_RDT
    l1100: list[L1100]


class HEADER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 1 - Header',
                   'usage': 'R',
                   'description': 'xid=HEADER name=Table 1 - Header type=wrapper',
                   'position': 10,
                   'type': 'object',
                   'properties': {'l1000': {'$ref': '#/$segments/L1000'}},
                   'required': ['l1000']},
         'maxItems': 1}
    l1000: list[L1000]


class L2000_HL01(Element):
    """Hierarchical ID Number"""
    class Schema:
        json = {'title': 'Hierarchical ID Number',
         'usage': 'R',
         'description': 'xid=HL01 data_ele=628',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/628'}, {'enum': ['1']}]}}
        datatype = common.D_628
        codes = ['1']
        min_len = 1
        max_len = 12


class L2000_HL02(Element):
    """Hierarchical Parent ID Number"""
    class Schema:
        json = {'title': 'Hierarchical Parent ID Number',
         'usage': 'N',
         'description': 'xid=HL02 data_ele=734',
         'sequence': 2,
         'type': {'$ref': '#/$common/734'}}
        datatype = common.D_734
        min_len = 1
        max_len = 12


class L2000_HL03(Element):
    """Hierarchical Level Code"""
    class Schema:
        json = {'title': 'Hierarchical Level Code',
         'usage': 'R',
         'description': 'xid=HL03 data_ele=735',
         'sequence': 3,
         'type': {'allOf': [{'$ref': '#/$common/735'}, {'enum': ['I']}]}}
        datatype = common.D_735
        codes = ['I']
        min_len = 1
        max_len = 2


class L2000_HL04(Element):
    """Hierarchical Child Code"""
    class Schema:
        json = {'title': 'Hierarchical Child Code',
         'usage': 'N',
         'description': 'xid=HL04 data_ele=736',
         'sequence': 4,
         'type': {'$ref': '#/$common/736'}}
        datatype = common.D_736
        min_len = 1
        max_len = 1


class L2000_HL(Segment):
    """Code List Header"""
    class Schema:
        json = {'title': 'Code List Header',
         'usage': 'R',
         'description': 'xid=HL name=Code List Header',
         'position': 10,
         'type': 'object',
         'properties': {'xid': {'literal': 'HL'},
                        'hl01': {'$ref': '#/$elements/L2000_HL01'},
                        'hl03': {'$ref': '#/$elements/L2000_HL03'}},
         'required': ['hl01', 'hl03']}
        segment_name = 'HL'
    hl01: L2000_HL01
    hl03: L2000_HL03


class L2100_SPI01(Element):
    """Security Level Code"""
    class Schema:
        json = {'title': 'Security Level Code',
         'usage': 'R',
         'description': 'xid=SPI01 data_ele=786',
         'sequence': 1,
         'type': {'allOf': [{'$ref': '#/$common/786'}, {'enum': ['00']}]}}
        datatype = common.D_786
        codes = ['00']
        min_len = 2
        max_len = 2


class L2100_SPI02(Element):
    """Reference Identification Qualifier"""
    class Schema:
        json = {'title': 'Reference Identification Qualifier',
         'usage': 'R',
         'description': 'xid=SPI02 data_ele=128',
         'sequence': 2,
         'type': {'allOf': [{'$ref': '#/$common/128'}, {'enum': ['ZZ']}]}}
        datatype = common.D_128
        codes = ['ZZ']
        min_len = 2
        max_len = 3


class L2100_SPI03(Element):
    """Reference Identification"""
    class Schema:
        json = {'title': 'Reference Identification',
         'usage': 'R',
         'description': 'xid=SPI03 data_ele=127',
         'sequence': 3,
         'type': {'$ref': '#/$common/127'}}
        datatype = common.D_127
        min_len = 1
        max_len = 50


class L2100_SPI04(Element):
    """Entity Title"""
    class Schema:
        json = {'title': 'Entity Title',
         'usage': 'R',
         'description': 'xid=SPI04 data_ele=790',
         'sequence': 4,
         'type': {'$ref': '#/$common/790'}}
        datatype = common.D_790


class L2100_SPI05(Element):
    """Entity Purpose"""
    class Schema:
        json = {'title': 'Entity Purpose',
         'usage': 'N',
         'description': 'xid=SPI05 data_ele=791',
         'sequence': 5,
         'type': {'$ref': '#/$common/791'}}
        datatype = common.D_791


class L2100_SPI06(Element):
    """Entity Status Code"""
    class Schema:
        json = {'title': 'Entity Status Code',
         'usage': 'N',
         'description': 'xid=SPI06 data_ele=792',
         'sequence': 6,
         'type': {'$ref': '#/$common/792'}}
        datatype = common.D_792


class L2100_SPI07(Element):
    """Transaction Set Purpose Code"""
    class Schema:
        json = {'title': 'Transaction Set Purpose Code',
         'usage': 'N',
         'description': 'xid=SPI07 data_ele=353',
         'sequence': 7,
         'type': {'$ref': '#/$common/353'}}
        datatype = common.D_353
        min_len = 2
        max_len = 2


class L2100_SPI08(Element):
    """Report Type Code"""
    class Schema:
        json = {'title': 'Report Type Code',
         'usage': 'N',
         'description': 'xid=SPI08 data_ele=755',
         'sequence': 8,
         'type': {'$ref': '#/$common/755'}}
        datatype = common.D_755
        min_len = 2
        max_len = 2


class L2100_SPI09(Element):
    """Security Level Code"""
    class Schema:
        json = {'title': 'Security Level Code',
         'usage': 'N',
         'description': 'xid=SPI09 data_ele=786',
         'sequence': 9,
         'type': {'$ref': '#/$common/786'}}
        datatype = common.D_786
        min_len = 2
        max_len = 2


class L2100_SPI10(Element):
    """Agency Qualifier Code"""
    class Schema:
        json = {'title': 'Agency Qualifier Code',
         'usage': 'N',
         'description': 'xid=SPI10 data_ele=559',
         'sequence': 10,
         'type': {'$ref': '#/$common/559'}}
        datatype = common.D_559
        min_len = 2
        max_len = 2


class L2100_SPI11(Element):
    """Source Subqualifier"""
    class Schema:
        json = {'title': 'Source Subqualifier',
         'usage': 'N',
         'description': 'xid=SPI11 data_ele=822',
         'sequence': 11,
         'type': {'$ref': '#/$common/822'}}
        datatype = common.D_822
        min_len = 1
        max_len = 15


class L2100_SPI12(Element):
    """Assigned Number"""
    class Schema:
        json = {'title': 'Assigned Number',
         'usage': 'N',
         'description': 'xid=SPI12 data_ele=554',
         'sequence': 12,
         'type': {'$ref': '#/$common/554'}}
        datatype = common.D_554
        min_len = 1
        max_len = 6


class L2100_SPI13(Element):
    """Certification Type Code"""
    class Schema:
        json = {'title': 'Certification Type Code',
         'usage': 'N',
         'description': 'xid=SPI13 data_ele=1322',
         'sequence': 13,
         'type': {'$ref': '#/$common/1322'}}
        datatype = common.D_1322
        min_len = 1
        max_len = 1


class L2100_SPI14(Element):
    """Proposal Data Detail Identifier Code"""
    class Schema:
        json = {'title': 'Proposal Data Detail Identifier Code',
         'usage': 'N',
         'description': 'xid=SPI14 data_ele=1401',
         'sequence': 14,
         'type': {'$ref': '#/$common/1401'}}
        datatype = common.D_1401


class L2100_SPI15(Element):
    """Heirarchal Structure Code"""
    class Schema:
        json = {'title': 'Heirarchal Structure Code',
         'usage': 'N',
         'description': 'xid=SPI15 data_ele=1005',
         'sequence': 15,
         'type': {'$ref': '#/$common/1005'}}
        datatype = common.D_1005
        min_len = 4
        max_len = 4


class L2100_SPI(Segment):
    """Code List Value and Definition"""
    class Schema:
        json = {'title': 'Code List Value and Definition',
         'usage': 'R',
         'description': 'xid=SPI name=Code List Value and Definition',
         'position': 20,
         'syntax': ['P0203'],
         'type': 'object',
         'properties': {'xid': {'literal': 'SPI'},
                        'spi01': {'$ref': '#/$elements/L2100_SPI01'},
                        'spi02': {'$ref': '#/$elements/L2100_SPI02'},
                        'spi03': {'$ref': '#/$elements/L2100_SPI03'},
                        'spi04': {'$ref': '#/$elements/L2100_SPI04'}},
         'required': ['spi01', 'spi02', 'spi03', 'spi04']}
        segment_name = 'SPI'
    spi01: L2100_SPI01
    spi02: L2100_SPI02
    spi03: L2100_SPI03
    spi04: L2100_SPI04


class L2100_MSG01(Element):
    """Free-Form Text Message"""
    class Schema:
        json = {'title': 'Free-Form Text Message',
         'usage': 'R',
         'description': 'xid=MSG01 data_ele=933',
         'sequence': 1,
         'type': {'$ref': '#/$common/933'}}
        datatype = common.D_933
        min_len = 1
        max_len = 264


class L2100_MSG02(Element):
    """Printer Carriage Control Code"""
    class Schema:
        json = {'title': 'Printer Carriage Control Code',
         'usage': 'N',
         'description': 'xid=MSG02 data_ele=934',
         'sequence': 2,
         'type': {'$ref': '#/$common/934'}}
        datatype = common.D_934
        min_len = 2
        max_len = 2


class L2100_MSG03(Element):
    """Number"""
    class Schema:
        json = {'title': 'Number',
         'usage': 'N',
         'description': 'xid=MSG03 data_ele=1470',
         'sequence': 3,
         'type': {'$ref': '#/$common/1470'}}
        datatype = common.D_1470
        min_len = 1
        max_len = 9


class L2100_MSG(Segment):
    """Additional Text"""
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Additional Text',
                   'usage': 'S',
                   'description': 'xid=MSG name=Additional Text',
                   'position': 50,
                   'syntax': ['C0302'],
                   'type': 'object',
                   'properties': {'xid': {'literal': 'MSG'},
                                  'msg01': {'$ref': '#/$elements/L2100_MSG01'}},
                   'required': ['msg01']}}
        segment_name = 'MSG'
    msg01: L2100_MSG01


class L2100(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Code List Value and Definition',
                   'usage': 'R',
                   'description': 'xid=2100 name=Code List Value and Definition '
                                  'type=None',
                   'position': 10,
                   'type': 'object',
                   'properties': {'spi': {'$ref': '#/$segments/L2100_SPI'},
                                  'msg': {'$ref': '#/$segments/L2100_MSG'}},
                   'required': ['spi']}}
    spi: L2100_SPI
    msg: list[L2100_MSG] | None


class L2000(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Code List Header',
                   'usage': 'R',
                   'description': 'xid=2000 name=Code List Header type=None',
                   'position': 10,
                   'type': 'object',
                   'properties': {'hl': {'$ref': '#/$segments/L2000_HL'},
                                  'l2100': {'$ref': '#/$segments/L2100'}},
                   'required': ['hl', 'l2100']}}
    hl: L2000_HL
    l2100: list[L2100]


class DETAIL(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 2 - Detail',
                   'usage': 'S',
                   'description': 'xid=DETAIL name=Table 2 - Detail type=wrapper',
                   'position': 20,
                   'type': 'object',
                   'properties': {'l2000': {'$ref': '#/$segments/L2000'}},
                   'required': ['l2000']}}
    l2000: list[L2000]


class FOOTER(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Table 3 - Footer',
                   'usage': 'N',
                   'description': 'xid=FOOTER name=Table 3 - Footer type=wrapper',
                   'position': 30},
         'maxItems': 1}


class ST_LOOP_SE01(Element):
    """Transaction Segment Count"""
    class Schema:
        json = {'title': 'Transaction Segment Count',
         'usage': 'R',
         'description': 'xid=SE01 data_ele=96',
         'sequence': 1,
         'type': {'$ref': '#/$common/96'}}
        datatype = common.D_96
        min_len = 1
        max_len = 10


class ST_LOOP_SE02(Element):
    """Transaction Set Control Number"""
    class Schema:
        json = {'title': 'Transaction Set Control Number',
         'usage': 'R',
         'description': 'xid=SE02 data_ele=329',
         'sequence': 2,
         'type': {'$ref': '#/$common/329'}}
        datatype = common.D_329
        min_len = 4
        max_len = 9


class ST_LOOP_SE(Segment):
    """Transaction Set Trailer"""
    class Schema:
        json = {'title': 'Transaction Set Trailer',
         'usage': 'R',
         'description': 'xid=SE name=Transaction Set Trailer',
         'position': 210,
         'type': 'object',
         'properties': {'xid': {'literal': 'SE'},
                        'se01': {'$ref': '#/$elements/ST_LOOP_SE01'},
                        'se02': {'$ref': '#/$elements/ST_LOOP_SE02'}},
         'required': ['se01', 'se02']}
        segment_name = 'SE'
    se01: ST_LOOP_SE01
    se02: ST_LOOP_SE02


class ST_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Transaction Set Header',
                   'usage': 'R',
                   'description': 'xid=ST_LOOP name=Transaction Set Header '
                                  'type=explicit',
                   'position': 20,
                   'type': 'object',
                   'properties': {'st': {'$ref': '#/$segments/ST_LOOP_ST'},
                                  'header': {'$ref': '#/$segments/HEADER'},
                                  'detail': {'$ref': '#/$segments/DETAIL'},
                                  'se': {'$ref': '#/$segments/ST_LOOP_SE'}},
                   'required': ['st', 'header', 'se']}}
    st: ST_LOOP_ST
    header: list[HEADER]
    detail: list[DETAIL] | None
    se: ST_LOOP_SE


class GS_LOOP_GE01(Element):
    """Number of Transaction Sets Included"""
    class Schema:
        json = {'title': 'Number of Transaction Sets Included',
         'usage': 'R',
         'description': 'xid=GE01 data_ele=97',
         'sequence': 1,
         'type': {'$ref': '#/$common/97'}}
        datatype = common.D_97
        min_len = 1
        max_len = 6


class GS_LOOP_GE02(Element):
    """Group Control Number"""
    class Schema:
        json = {'title': 'Group Control Number',
         'usage': 'R',
         'description': 'xid=GE02 data_ele=28',
         'sequence': 2,
         'type': {'$ref': '#/$common/28'}}
        datatype = common.D_28
        min_len = 1
        max_len = 9


class GS_LOOP_GE(Segment):
    """Functional Group Trailer"""
    class Schema:
        json = {'title': 'Functional Group Trailer',
         'usage': 'R',
         'description': 'xid=GE name=Functional Group Trailer',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'GE'},
                        'ge01': {'$ref': '#/$elements/GS_LOOP_GE01'},
                        'ge02': {'$ref': '#/$elements/GS_LOOP_GE02'}},
         'required': ['ge01', 'ge02']}
        segment_name = 'GE'
    ge01: GS_LOOP_GE01
    ge02: GS_LOOP_GE02


class GS_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Functional Group Header',
                   'usage': 'R',
                   'description': 'xid=GS_LOOP name=Functional Group Header '
                                  'type=explicit',
                   'position': 20,
                   'type': 'object',
                   'properties': {'gs': {'$ref': '#/$segments/GS_LOOP_GS'},
                                  'st_loop': {'$ref': '#/$segments/ST_LOOP'},
                                  'ge': {'$ref': '#/$segments/GS_LOOP_GE'}},
                   'required': ['gs', 'st_loop', 'ge']}}
    gs: GS_LOOP_GS
    st_loop: list[ST_LOOP]
    ge: GS_LOOP_GE


class ISA_LOOP_TA101(Element):
    """Interchange Control Number"""
    class Schema:
        json = {'title': 'Interchange Control Number',
         'usage': 'R',
         'description': 'xid=TA101 data_ele=I12',
         'sequence': 1,
         'type': {'$ref': '#/$common/I12'}}
        datatype = common.I12
        min_len = 9
        max_len = 9


class ISA_LOOP_TA102(Element):
    """Interchange Date"""
    class Schema:
        json = {'title': 'Interchange Date',
         'usage': 'R',
         'description': 'xid=TA102 data_ele=I08',
         'sequence': 2,
         'type': {'$ref': '#/$common/I08'}}
        datatype = common.I08
        min_len = 6
        max_len = 6


class ISA_LOOP_TA103(Element):
    """Interchange Time"""
    class Schema:
        json = {'title': 'Interchange Time',
         'usage': 'R',
         'description': 'xid=TA103 data_ele=I09',
         'sequence': 3,
         'type': {'$ref': '#/$common/I09'}}
        datatype = common.I09
        min_len = 4
        max_len = 4


class ISA_LOOP_TA104(Element):
    """Interchange Acknowledgement Code"""
    class Schema:
        json = {'title': 'Interchange Acknowledgement Code',
         'usage': 'R',
         'description': 'xid=TA104 data_ele=I17',
         'sequence': 4,
         'type': {'allOf': [{'$ref': '#/$common/I17'}, {'enum': ['A', 'E', 'R']}]}}
        datatype = common.I17
        codes = ['A', 'E', 'R']
        min_len = 1
        max_len = 1


class ISA_LOOP_TA105(Element):
    """Interchange Note Code"""
    class Schema:
        json = {'title': 'Interchange Note Code',
         'usage': 'R',
         'description': 'xid=TA105 data_ele=I18',
         'sequence': 5,
         'type': {'allOf': [{'$ref': '#/$common/I18'},
                            {'enum': ['000', '001', '002', '003', '004', '005', '006',
                                      '007', '008', '009', '010', '011', '012', '013',
                                      '014', '015', '016', '017', '018', '019', '020',
                                      '021', '022', '023', '024', '025', '026', '027',
                                      '028', '029', '030', '031']}]}}
        datatype = common.I18
        codes = ['000', '001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031']
        min_len = 3
        max_len = 3


class ISA_LOOP_TA1(Segment):
    """Interchange Acknowledgement"""
    class Schema:
        json = {'title': 'Interchange Acknowledgement',
         'usage': 'S',
         'description': 'xid=TA1 name=Interchange Acknowledgement',
         'position': 20,
         'type': 'object',
         'properties': {'xid': {'literal': 'TA1'},
                        'ta101': {'$ref': '#/$elements/ISA_LOOP_TA101'},
                        'ta102': {'$ref': '#/$elements/ISA_LOOP_TA102'},
                        'ta103': {'$ref': '#/$elements/ISA_LOOP_TA103'},
                        'ta104': {'$ref': '#/$elements/ISA_LOOP_TA104'},
                        'ta105': {'$ref': '#/$elements/ISA_LOOP_TA105'}},
         'required': ['ta101', 'ta102', 'ta103', 'ta104', 'ta105']}
        segment_name = 'TA1'
    ta101: ISA_LOOP_TA101
    ta102: ISA_LOOP_TA102
    ta103: ISA_LOOP_TA103
    ta104: ISA_LOOP_TA104
    ta105: ISA_LOOP_TA105


class ISA_LOOP_IEA01(Element):
    """Number of Included Functional Groups"""
    class Schema:
        json = {'title': 'Number of Included Functional Groups',
         'usage': 'R',
         'description': 'xid=IEA01 data_ele=I16',
         'sequence': 1,
         'type': {'$ref': '#/$common/I16'}}
        datatype = common.I16
        min_len = 1
        max_len = 5


class ISA_LOOP_IEA02(Element):
    """Interchange Control Number"""
    class Schema:
        json = {'title': 'Interchange Control Number',
         'usage': 'R',
         'description': 'xid=IEA02 data_ele=I12',
         'sequence': 2,
         'type': {'$ref': '#/$common/I12'}}
        datatype = common.I12
        min_len = 9
        max_len = 9


class ISA_LOOP_IEA(Segment):
    """Interchange Control Trailer"""
    class Schema:
        json = {'title': 'Interchange Control Trailer',
         'usage': 'R',
         'description': 'xid=IEA name=Interchange Control Trailer',
         'position': 30,
         'type': 'object',
         'properties': {'xid': {'literal': 'IEA'},
                        'iea01': {'$ref': '#/$elements/ISA_LOOP_IEA01'},
                        'iea02': {'$ref': '#/$elements/ISA_LOOP_IEA02'}},
         'required': ['iea01', 'iea02']}
        segment_name = 'IEA'
    iea01: ISA_LOOP_IEA01
    iea02: ISA_LOOP_IEA02


class ISA_LOOP(Loop):
    class Schema:
        json = {'type': 'array',
         'items': {'title': 'Interchange Control Header',
                   'usage': 'R',
                   'description': 'xid=ISA_LOOP name=Interchange Control Header '
                                  'type=explicit',
                   'position': 1,
                   'type': 'object',
                   'properties': {'isa': {'$ref': '#/$segments/ISA_LOOP_ISA'},
                                  'gs_loop': {'$ref': '#/$segments/GS_LOOP'},
                                  'ta1': {'$ref': '#/$segments/ISA_LOOP_TA1'},
                                  'iea': {'$ref': '#/$segments/ISA_LOOP_IEA'}},
                   'required': ['isa', 'gs_loop', 'iea']}}
    isa: ISA_LOOP_ISA
    gs_loop: list[GS_LOOP]
    ta1: ISA_LOOP_TA1 | None
    iea: ISA_LOOP_IEA


class MSG841(Message):
    """HIPAA Related Code Lists"""
    class Schema:
        json = {'title': 'HIPAA Related Code Lists',
         'description': 'xid=841 name=HIPAA Related Code Lists',
         'type': 'object',
         'properties': {'isa_loop': {'$ref': '#/$loops/ISA_LOOP'}},
         'required': ['isa_loop']}
    isa_loop: list[ISA_LOOP]
