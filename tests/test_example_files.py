"""
Test the example .txt files

The 837I-Examples.txt appears damaged.
There's no SE,GE, or IEA segments at the end of the first message.
We do not use it as a test case.

"""

from pathlib import Path
from typing import TextIO
from pprint import pprint

from pytest import fixture, mark

from x12.base import Source
from x12 import msg_271_4010_X092_A1
from x12 import msg_834_5010_X220_A1
from x12 import msg_834_5010_X220_A1_v2
from x12 import msg_835_5010_X221_A1
from x12 import msg_837_4010_X098_A1
# from x12 import msg_837_4010_X097_A1  # Error -- undefined common attribute C035
# from x12 import msg_837_4010_X096_A1  # Error
from x12 import msg_837_5010_X222_A1
from x12 import msg_837Q3_I_5010_X223_A1_v2  # Not usable, missing ISA, GS, etc., starts with ST.
from x12 import msg_276_4010_X093_A1
from x12 import msg_278_4010_X094_A1


EXAMPLES = Path.cwd() / "tests"  # Should be run in the parent directory

def test_271_dependent_benefits() -> None:
    example = EXAMPLES / "271-dependent-benefits.txt"
    document = Source(example.read_text())
    msg = msg_271_4010_X092_A1.MSG271.parse(document)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl.hl01)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl.hl03)
    # print(msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000a[0].hl.hl04)
    # print(list(msg.segment_iter()))
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '10864          ',
            '101006', '0931', 'U', '00401', '000000418', '1', 'P', '^'],
        ['GS', 'HB', 'ZIRMED', '10864', '20120830', '0931', '410', 'X', '004010X092A1'],
        ['ST', '271', '0001'],
        ['BHT', '0022', '11', '140', '20121001', '090231', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'COMMERCIAL SAMPLE', '', '', '', '', 'PI', '44444', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
        ['HL', '3', '2', '22', '1'],
        ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
        ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
        ['NM1', 'IL', '1', 'DOE', 'JOHN', 'P', '', '', 'MI', '111111111', None, None],
        ['REF', '6P', '11111', 'ACME MEDICAL, INC'],
        ['HL', '4', '3', '23', '0'],
        ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
        ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
        ['NM1', '03', '1', 'DOE', 'JANE', None, None, None, None, None, None, None],
        ['REF', '18', '1234567', None],
        ['N3', '3333 SOMEWHERE ST', None],
        ['N4', 'ANYWHERE', 'LA', '71104', None, None, None],
        ['DMG', 'D8', '19370305', 'F', None, None, None, None, None, None],
        ['DTP', '346', 'D8', '20110801'],
        ['DTP', '472', 'D8', '20120928'],
        ['DTP', '307', 'D8', '20110801'],
        ['EB', 'L', 'FAM', '30', 'PS', None, None, None, None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['MSG', 'PCP SELECTION NOT REQUIRED', None, None],
        ['EB', 'W', None, None, None, None, None, None, None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['LS', '2120'],
        ['NM1', 'PR', '2', 'Aetna', None, None, None, None, None, None, None, None],
        ['N3', 'PO Box 14079', None],
        ['N4', 'Lexington', 'KY', '40512', None, None, None],
        ['LE', '2120'],
        ['EB', '1', 'FAM', '30', 'PS', 'Aetna Choice POS II', None, None, None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['EB', 'C', 'FAM', '30', None, '', '23', '600', None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['DTP', '307', 'D8', '20120101'],
        ['MSG', 'Med Dent', None, None],
        ['MSG', 'LAB OP DIR ACC', None, None],
        ['MSG', 'OP LAB', None, None],
        ['EB', 'C', 'FAM', '30', None, '', '29', '186.89', None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['MSG', 'Med Dent', None, None],
        ['EB', 'C', 'FAM', '30', None, '', '23', '600', None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['DTP', '307', 'D8', '20120101'],
        ['MSG', 'PAP SMEAR', None, None],
        ['EB', 'C', 'IND', '30', None, '', '23', '200', None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['DTP', '307', 'D8', '20120101'],
        ['MSG', 'Med Dent', None, None],
        ['MSG', 'LAB OP DIR ACC', None, None],
        ['MSG', 'OP LAB', None, None],
        ['EB', 'C', 'IND', '30', None, '', '29', '78.8', None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['MSG', 'Med Dent', None, None],
        ['EB', 'C', 'IND', '30', None, '', '23', '200', None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['DTP', '307', 'D8', '20120101'],
        ['MSG', 'PAP SMEAR', None, None],
        ['EB', 'G', 'IND', '30', None, '', None, '1000', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', None, '', '29', '1000', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', None, '', None, '3000', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', None, '', '29', '3000', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', '1', 'FAM', '5', None, 'Aetna Choice POS II', None, None, None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['EB', 'A', 'FAM', '5', None, '', None, None, '0', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'LAB OP DIR ACC', None, None],
        ['MSG', 'OP LAB', None, None],
        ['MSG', 'PAP SMEAR', None, None],
        ['EB', 'F', 'FAM', '5', None, '', None, None, None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'PAP SMEAR /Plan Ded Waived', None, None],
        ['EB', 'B', 'FAM', '5', None, '', None, '0', None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['MSG', 'LAB OP DIR ACC', None, None],
        ['MSG', 'OP LAB', None, None],
        ['MSG', 'PAP SMEAR', None, None],
        ['EB', 'F', 'FAM', '5', None, None, None, None, None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['MSG', 'Plan Requires PreCert', None, None],
        ['EB', 'F', 'FAM', '5', None, '', '32', None, None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['MSG', 'Unlimited Lifetime Benefits', None, None],
        ['EB', 'F', 'FAM', '5', None, None, None, None, None, None, None, None, None,
         [None, None, None, None, None, None, None]],
        ['MSG', 'Self Funded', None, None],
        ['MSG', 'Plan includes NAP', None, None],
        ['EB', 'A', 'FAM', '5', None, '', None, None, '0.3', None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['MSG', 'LAB OP DIR ACC', None, None],
        ['MSG', 'COINS APPLIES TO OUT OF POCKET', None, None],
        ['MSG', 'OP LAB', None, None],
        ['MSG', 'PAP SMEAR', None, None],
        ['SE', '79', '0001'],
        ['GE', '1', '931'],
        ['IEA', '1', '000090132']
    ]
    assert list(msg.segment_iter()) == expected

def test_271_example() -> None:
    example = EXAMPLES / "271-example.txt"
    document = Source(example.read_text())
    msg = msg_271_4010_X092_A1.MSG271.parse(document)
    # print(list(msg.segment_iter()))
    expected = [['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '12345          ', '120605', '2324', 'U', '00401', '000050033', '1', 'P', '^'],
        ['GS', 'HB', 'ZIRMED', '12345', '20120605', '2324', '50025', 'X', '004010X092A1'],
        ['ST', '271', '0001'],
        ['BHT', '0022', '11', '11111', '20120605', '232423', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'Health Net Inc', '', '', '', '', 'PI', '10385', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', 'DR. ACULA', '', '', '', '', 'XX', '1111111111', None, None],
        ['HL', '3', '2', '22', '0'],
        ['TRN', '1', '222222222', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '2', '333333333', '9ZIRMEDCOM', 'ELI ID'],
        ['TRN', '1', '4444444444', '9MEDDATACO', None],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'R11111111', None, None],
        ['AAA', 'N', None, '72', 'C'],
        ['AAA', 'N', None, '73', 'C'],
        ['AAA', 'N', None, '73', 'C'],
        ['AAA', 'N', None, '58', 'C'],
        ['DTP', '291', 'D8', '20120408'],
        ['SE', '17', '0001'],
        ['GE', '1', '50025'],
        ['IEA', '1', '000050033']]
    assert list(msg.segment_iter()) == expected


def test_271_example_2() -> None:
    example = EXAMPLES / "271-example-2.txt"
    document = Source(example.read_text())
    msg = msg_271_4010_X092_A1.MSG271.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '10864          ', '101006', '0931', 'U', '00401', '000000418', '1', 'P', '^'],
        ['GS', 'HB', 'ZIRMED', '10864', '20120830', '0931', '410', 'X', '004010X092A1'],
        ['ST', '271', '0001'],
        ['BHT', '0022', '11', '140', '20120830', '093122', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'COMMERCIAL SAMPLE', '', '', '', '', 'PI', '44444', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
        ['HL', '3', '2', '22', '0'],
        ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
        ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
        ['NM1', 'IL', '1', 'DOE', 'JANET', '', '', '', 'MI', '111111111', None, None],
        ['REF', '6P', '00000', None],
        ['N3', '3333 SOMEWHERE ST', None],
        ['N4', 'ANYWHERE', 'LA', '71104', None, None, None],
        ['DMG', 'D8', '19370305', 'F', None, None, None, None, None, None],
        ['INS', 'Y', '18', '001', '25', None, None, None, None, None, None, None, '', None, '', None, None, '1'],
        ['DTP', '307', 'D8', '20050201'],
        ['EB', '1', None, '30', 'C1', 'MANAGED INDEMNITY', None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['LS', '2120'],
        ['NM1', 'PR', '2', 'UNITEDHEALTHCARE', None, None, None, None, None, None, None, None],
        ['N3', 'P.O. BOX 740800', 'P.O. BOX 740800'],
        ['N4', 'ATLANTA', 'GA', '303740800', None, None, None],
        ['LE', '2120'],
        ['EB', 'G', 'FAM', '30', 'C1', '', None, '3000', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', 'C1', '', '24', '3025.9', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', 'C1', '', '29', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'FAM', '30', None, '', None, '236', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'FAM', '30', None, '', '24', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'FAM', '30', None, '', '29', '236', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', 'C1', '', None, '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', 'C1', '', '24', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', 'C1', '', '29', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'FAM', '30', None, '', None, '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'FAM', '30', None, '', '24', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'FAM', '30', None, '', '29', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', 'C1', '', None, '1500', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', 'C1', '', '24', '1500', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', 'C1', '', '29', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'IND', '30', None, '', None, '118', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'IND', '30', None, '', '24', '118', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'IND', '30', None, '', '29', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', 'C1', '', None, '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', 'C1', '', '24', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', 'C1', '', '29', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'IND', '30', None, '', None, '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'IND', '30', None, '', '24', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'C', 'IND', '30', None, '', '29', '0', None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'I', None, '35', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'I', None, '92', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'I', None, '91', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'I', None, '88', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', '1', None, 'AE', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', 'AE', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', 'AE', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, 'AL', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', 'AL', None, '', '27', None, '1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', 'AL', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, 'A4', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', 'A4', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', 'A4', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, 'A6', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', 'A6', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', 'A6', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, 'A7', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', 'A7', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', 'A7', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, 'A8', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', 'A8', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', 'A8', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '1', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '1', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '1', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '2', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '2', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '2', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '4', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '4', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '4', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '5', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '5', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '5', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '7', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '7', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '7', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '9', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '9', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '9', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '12', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '12', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '12', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '13', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '13', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '13', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '47', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '47', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '47', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '48', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '48', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '48', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '50', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '50', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '50', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '52', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '52', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '52', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '53', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '53', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '53', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '60', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '60', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '60', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '68', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '68', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '68', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '81', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '81', None, '', '27', None, '0.1', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '81', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '86', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '86', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '86', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '96', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'A', 'IND', '96', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', 'IND', '96', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', '1', None, '98', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['MSG', 'OFFICE VISIT', None, None],
        ['EB', 'A', 'IND', '98', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'OFFICE VISIT', None, None],
        ['EB', 'B', 'IND', '98', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'OFFICE VISIT', None, None],
        ['EB', '1', None, '98', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['MSG', 'PRIMARY CARE PHYSICIAN', None, None],
        ['EB', 'A', 'IND', '98', None, '', '27', None, '0.2', None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'PRIMARY CARE PHYSICIAN', None, None],
        ['EB', 'B', 'IND', '98', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'PRIMARY CARE PHYSICIAN', None, None],
        ['EB', 'R', None, '30', None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['LS', '2120'],
        ['NM1', 'PR', '2', 'MEDICARE', None, None, None, None, None, None, None, None],
        ['LE', '2120'],
        ['EB', 'X', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['LS', '2120'],
        ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
        ['LE', '2120'],
        ['SE', '144', '0001'],
        ['GE', '1', '410'],
        ['IEA', '1', '000000418'],
        ]
    assert list(msg.segment_iter()) == expected

def test_271_dependent_rejection() -> None:
    example = EXAMPLES / "271-example-dependent-rejection.txt"
    document = Source(example.read_text())
    msg = msg_271_4010_X092_A1.MSG271.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '12345          ', '120629', '1745', 'U', '00401', '000059247', '1', 'P', '^'],
        ['GS', 'HB', 'ZIRMED', '12345', '20120629', '1745', '59239', 'X', '004010X092A1'],
        ['ST', '271', '0001'],
        ['BHT', '0022', '11', '58446', '20120629', '174529', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'ANTHEM BLUE CROSS', '', '', '', '', 'PI', '10319', None, None],
        ['PER', 'IC', 'BLUECARD ELIGIBILITY', 'TE', '8006762583', None, None, None, None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', 'DR. SPACEMAN', '', '', '', '', 'XX', '1111111111', None, None],
        ['HL', '3', '2', '22', '1'],
        ['TRN', '1', '222222222', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '2', '333333333', '9ZIRMEDCOM', 'ELI ID'],
        ['TRN', '1', '4444444444', '9MEDDATACO', None],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'R11111111', None, None],
        ['AAA', 'Y', None, '72', 'N'],
        ['HL', '4', '3', '23', '0'],
        ['TRN', '1', '222222222', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '2', '333333333', '9ZIRMEDCOM', 'ELI ID'],
        ['TRN', '1', '4444444444', '9MEDDATACO', None],
        ['NM1', '03', '1', 'DOE', 'JANE', None, None, None, None, None, None, None],
        ['DMG', 'D8', '19810810', None, None, None, None, None, None, None],
        ['SE', '20', '0001'],
        ['GE', '1', '59239'],
        ['IEA', '1', '000059247'],
    ]
    assert list(msg.segment_iter()) == expected

def test_271_related_entity() -> None:
    example = EXAMPLES / "271-related-entity.txt"
    document = Source(example.read_text())
    msg = msg_271_4010_X092_A1.MSG271.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'ZIRMED         ', 'ZZ', '10864          ', '120927', '1403', 'U', '00401', '000089573', '1', 'P', '^'],
        ['GS', 'HB', 'ZIRMED', '10864', '20120927', '1403', '89565', 'X', '004010X092A1'],
        ['ST', '271', '0001'],
        ['BHT', '0022', '11', '11111', '20120927', '140333', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'COMMERCIAL SAMPLE', '', '', '', '', 'PI', '44444', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', '', '', '', '', '', 'XX', '1234567890', None, None],
        ['HL', '3', '2', '22', '1'],
        ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
        ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
        ['NM1', 'IL', '1', 'DOE', 'JOHN', 'P', '', '', 'MI', '111111111', None, None],
        ['REF', '3H', '0GEU', None],
        ['INS', 'Y', '18', '001', '25', None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['HL', '4', '3', '23', '0'],
        ['TRN', '2', '51813246', '9ZIRMEDCOM', None],
        ['TRN', '1', '53637360', '9ZIRMEDCOM', 'ELR ID'],
        ['TRN', '1', '51893570', '9ZIRMEDCOM', 'ELI ID'],
        ['NM1', '03', '1', 'DOE', 'JANE', None, None, None, None, None, None, None],
        ['REF', '6P', '55555G', 'CEDARS-SINAI HEALTH SYSTEM'],
        ['REF', 'IF', 'HVU', None],
        ['DMG', 'D8', '19370305', 'F', None, None, None, None, None, None],
        ['DTP', '291', 'RD8', '20120101-99991231'],
        ['EB', '1', 'ESP', '30', 'HM', 'HMO CEDARS SINAI ONLY', None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['EB', 'G', 'FAM', '30', None, '', '23', '1000', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'TWO PARTY COPAY MAXIMUM', None, None],
        ['EB', 'G', 'FAM', '30', None, '', '29', '870', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'TWO PARTY COPAY MAXIMUM', None, None],
        ['EB', 'G', 'FAM', '30', None, '', '23', '1500', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'COPAY MAXIMUM', None, None],
        ['EB', 'G', 'FAM', '30', None, '', '29', '1370', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'G', 'IND', '30', None, '', '23', '500', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'SINGLE PARTY COPAY MAXIMUM', None, None],
        ['EB', 'G', 'IND', '30', None, '', '29', '460', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['EB', 'B', None, '5', None, '', '26', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'FETAL GENETIC', None, None],
        ['EB', 'B', None, '5', None, '', '27', '0', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'BLOOD LEAD SCREENING', None, None],
        ['MSG', 'MAMMOGRAPHY', None, None],
        ['MSG', 'PAP/CERVICAL CANCER SCREEN', None, None],
        ['MSG', 'PROSTATE SCREEN', None, None],
        ['EB', 'B', None, '5', None, '', '27', '20', None, None, None, None, 'Y', [None, None, None, None, None, None, None]],
        ['MSG', 'ALLERGY TESTING', None, None],
        ['MSG', 'MAMMOGRAM ROUTINE COPAY', None, None],
        ['EB', 'I', None, '5', None, '', None, None, None, None, None, None, 'N', [None, None, None, None, None, None, None]],
        ['EB', 'N', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['DTP', '295', 'RD8', '20110701-99991231'],
        ['LS', '2120'],
        ['N3', '123 RELATED ST # 1', None],
        ['N4', 'ANYTOWN', 'CA', '902101234', None, None, None],
        ['PER', 'IC', '', 'TE', '8005554160', None, None, None, None, None],
        ['LE', '2120'],
        ['EB', 'L', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['DTP', '295', 'RD8', '20110701-99991231'],
        ['LS', '2120'],
        ['NM1', '36', '2', 'EMPLOYER', None, None, None, None, None, None, None, None],
        ['N3', '123 RELATED ST # 2', None],
        ['N4', 'ANYTOWN', 'WA', '98101', None, None, None],
        ['PER', 'IC', '', 'TE', '2065551234', None, None, None, None, None],
        ['LE', '2120'],
        ['EB', 'P', None, None, None, None, None, None, None, None, None, None, None, [None, None, None, None, None, None, None]],
        ['MSG', 'UNLESS OTHERWISE REQUIRED BY STATE LAW, THIS NOTICE IS NOT A GUARANTEE OF PAYMENT. BENEFITS ARE SUBJECT TO ALL CONTRACT LIMITATIONS AND THE MEMBERS ELIGIBILITY STATUS ON THE DATE OF SERVICE. FOR ANY QUESTIONS PLEASE CALL PHONE NUMBER ON BACK OF MEMBERS CARD.', None, None],
        ['SE', '77', '0001'],
        ['GE', '1', '89565'],
        ['IEA', '1', '000089573'],
    ]
    assert list(msg.segment_iter()) == expected


def test_834_example() -> None:
    example = EXAMPLES / "834-example.txt"
    document = Source(example.read_text())
    msg = msg_834_5010_X220_A1.MSG834A1.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'D00XXX         ', 'ZZ', '00AA           ', '070305', '1832', '^', '00501', '676048320', '0', 'P', '\\'],
        ['GS', 'BE', 'D00XXX', '00AA', '20150305', '1832', '260007982', 'X', '005010X220A1'],
        ['ST', '834', '0001', '005010X220A1'],
        ['BGN', '00', '88880070301  00', '20150305', '181245', None, '', None, '4', None],
        ['DTP', '007', 'D8', '20150301'],
        ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
        ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
        ['INS', 'Y', '18', '030', 'XN', 'A', ['C   ', None, None, None], None, 'FT', None, None, None, None, None, None, None, None, None],
        ['REF', '0F', '00389999', None],
        ['REF', '1L', '000003409999', None],
        ['REF', '3H', 'K129999A', None],
        ['DTP', '356', 'D8', '20150301'],
        ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
        ['N3', '777 ELM ST', None],
        ['N4', 'ALLEGAN', 'MI', '49010', None, 'CY', '03', None],
        ['DMG', 'D8', '19670330', 'M', None, [['O', None, None]], None, None, None, None, None, None],
        ['LUI', None, '', 'ESSPANISH', None, None],
        ['HD', '030', None, 'AK', '064703', 'IND', None, None, None, None, None, None],
        ['DTP', '348', 'D8', '20150301'],
        ['AMT', 'P3', '45.34', None],
        ['REF', '17', 'E  1F', None],
        ['SE', '20', '0001'],
        ['GE', '1', '260007982'],
        ['IEA', '1', '676048320'],
    ]
    assert list(msg.segment_iter()) == expected


def test_834_example_2() -> None:
    example = EXAMPLES / "834-example-2.txt"
    document = Source(example.read_text())
    msg = msg_834_5010_X220_A1.MSG834A1.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'D00XXX         ', 'ZZ', '00AA           ', '070305', '1832', 'U', '00501', '000701336', '0', 'P', ':'],
        ['GS', 'BE', 'D00XXX', '00AA', '20070305', '1832', '13360001', 'X', '005010X220A1'],
        ['ST', '834', '0001', '005010X220A1'],
        ['BGN', '00', '88880070301  00', '20070305', '181245', None, '', None, '4', None],
        ['DTP', '007', 'D8', '20070301'],
        ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
        ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
        ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], None, 'FT', None, None, None, None, None, None, None, None, None],
        ['REF', '0F', '00389999', None],
        ['REF', '1L', '000003409999', None],
        ['REF', '3H', 'K129999A', None],
        ['DTP', '356', 'D8', '20070301'],
        ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
        ['N3', '777 ELM ST', None],
        ['N4', 'ALLEGAN', 'MI', '49010', None, 'CY', '03', None],
        ['DMG', 'D8', '19670330', 'M', None, [['O', None, None]], None, None, None, None, None, None],
        ['LUI', None, '', 'ESSPANISH', None, None],
        ['HD', '030', None, 'AK', '064703', 'IND', None, None, None, None, None, None],
        ['DTP', '348', 'D8', '20070301'],
        ['AMT', 'P3', '45.34', None],
        ['REF', '17', 'E  1F', None],
        ['SE', '20', '0001'],
        ['ST', '834', '0002', '005010X220A1'],
        ['BGN', '00', '88880070301  00', '20070305', '181245', None, '', None, '4', None],
        ['DTP', '007', 'D8', '20070301'],
        ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
        ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
        ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], None, 'FT', None, None, None, None, None, None, None, None, None],
        ['REF', '0F', '00389999', None],
        ['REF', '1L', '000003409999', None],
        ['REF', '3H', 'K129999A', None],
        ['DTP', '356', 'D8', '20070301'],
        ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
        ['N3', '777 ELM ST', None],
        ['N4', 'ALLEGAN', 'MI', '49010', None, 'CY', '03', None],
        ['DMG', 'D8', '19670330', 'M', None, [['O', None, None]], None, None, None, None, None, None],
        ['LUI', None, '', 'ESSPANISH', None, None],
        ['HD', '030', None, 'AK', '064703', 'IND', None, None, None, None, None, None],
        ['DTP', '348', 'D8', '20070301'],
        ['AMT', 'P3', '45.34', None],
        ['REF', '17', 'E  1F', None],
        ['SE', '20', '0002'],
        ['ST', '834', '0003', '005010X220A1'],
        ['BGN', '00', '88880070301  00', '20070305', '181245', None, '', None, '4', None],
        ['DTP', '007', 'D8', '20070301'],
        ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
        ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
        ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], None, 'FT', None, None, None, None, None, None, None, None, None],
        ['REF', '0F', '00389999', None],
        ['REF', '1L', '000003409999', None],
        ['REF', '3H', 'K129999A', None],
        ['DTP', '356', 'D8', '20070301'],
        ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
        ['N3', '777 ELM ST', None],
        ['N4', 'ALLEGAN', 'MI', '49010', None, 'CY', '03', None],
        ['DMG', 'D8', '19670330', 'M', None, [['O', None, None]], None, None, None, None, None, None],
        ['LUI', None, '', 'ESSPANISH', None, None],
        ['HD', '030', None, 'AK', '064703', 'IND', None, None, None, None, None, None],
        ['DTP', '348', 'D8', '20070301'],
        ['AMT', 'P3', '45.34', None],
        ['REF', '17', 'E  1F', None],
        ['SE', '20', '0003'],
        ['ST', '834', '0004', '005010X220A1'],
        ['BGN', '00', '88880070301  00', '20070305', '181245', None, '', None, '4', None],
        ['DTP', '007', 'D8', '20070301'],
        ['N1', 'P5', 'PAYER 1', 'FI', '999999999', None, None],
        ['N1', 'IN', 'KCMHSAS', 'FI', '999999999', None, None],
        ['INS', 'Y', '18', '030', 'XN', 'A', ['C', None, None, None], None, 'FT', None, None, None, None, None, None, None, None, None],
        ['REF', '0F', '00389999', None],
        ['REF', '1L', '000003409999', None],
        ['REF', '3H', 'K129999A', None],
        ['DTP', '356', 'D8', '20070301'],
        ['NM1', 'IL', '1', 'DOE', 'JOHN', 'A', '', '', '34', '999999999', None, None, None],
        ['N3', '777 ELM ST', None],
        ['N4', 'ALLEGAN', 'MI', '49010', None, 'CY', '03', None],
        ['DMG', 'D8', '19670330', 'M', None, [['O', None, None]], None, None, None, None, None, None],
        ['LUI', None, '', 'ESSPANISH', None, None],
        ['HD', '030', None, 'AK', '064703', 'IND', None, None, None, None, None, None],
        ['DTP', '348', 'D8', '20070301'],
        ['AMT', 'P3', '45.34', None],
        ['REF', '17', 'E  1F', None],
        ['SE', '20', '0004'],
        ['GE', '4', '13360001'],
        ['IEA', '1', '000701336'],
    ]
    assert list(msg.segment_iter()) == expected

def test_835_example() -> None:
    example = EXAMPLES / "835-example.txt"
    document = Source(example.read_text())
    msg = msg_835_5010_X221_A1.MSG835W1.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'MYCLEARINGHOUSE', 'ZZ', 'RECVCODE       ', '120323', '1938', 'U', '00401', '000015442', '1', 'P', '^'],
        ['GS', 'HP', 'MYCLEARINGHOUSE', 'RECVCODE', '20120323', '1938', '15555', 'X', '004010X091A1'],
        ['ST', '835', '0001', None],
        ['BPR', 'I', '12345.67', 'C', 'ACH', 'CCP', '01', '999999999', 'DA', '1234567890', '1111111111', '000011111', '01', '222222222', 'DA', '3333333333', '20120322', None, None, None, None, None],
        ['TRN', '1', '1QG11111111', '1111111111', '000011111'],
        ['DTM', '405', '20120319', None, None, None, None],
        ['N1', 'PR', 'UNITED HEALTHCARE INSURANCE COMPANY', 'XV', '87726', None, None],
        ['N3', '9900 BREN ROAD', None],
        ['N4', 'MINNETONKA', 'MN', '553430000', None, None, None, None],
        ['REF', '2U', '87726', None],
        ['PER', 'CX', 'ATLANTA SERVICE CENTER', 'TE', '8778423210', None, None, None, None, None],
        ['N1', 'PE', 'MY CLINIC', 'XX', '1333333333', None, None],
        ['N3', '123 HEALTHCARE STREET', None],
        ['N4', 'SAN FRANCISCO', 'CA', '94109', None, None, None, None],
        ['REF', 'TJ', '777777777', None],
        ['LX', '1'],
        ['TS3', '1333333333', '81', '20121231', '2', '23456.78', '12345.67', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['CLP', '001-DDDDDDDDDD', '1', '200.02', '200.02', None, '13', '1234567890 0987654321', '81', None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'DOE', 'JOHN', None, None, None, None, None, None, None, None],
        ['NM1', 'IL', '1', 'DOE', 'JANE', '', '', '', 'MI', '123111111', None, None, None],
        ['NM1', '74', '1', 'DOE', 'JANE', 'D', None, None, None, None, None, None, None],
        ['NM1', '82', '2', 'MY CLINIC', '', '', '', '', 'XX', '1333333333', None, None, None],
        ['REF', 'CE', 'CHOYC+', None],
        ['REF', '1L', '5G5G5G', None],
        ['DTM', '232', '20120222', None, None, None, None],
        ['AMT', 'AU', '200.02', None],
        ['SVC', ['HC', '88888', None, None, None, None, None, None], '200.02', '200.02', '', '1', [None, None, None, None, None, None, None, None], None],
        ['DTM', '472', '20120222', None, None, None, None],
        ['REF', '6R', '251111111111', None],
        ['AMT', 'B6', '200.02', None],
        ['CLP', '001-SSSSSSSSSS', '1', '23276.56', '12000.65', '145', '14', '2234567890 0987654322', '81', None, None, None, None, None, None],
        ['CAS', 'PR', '1', '145', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'SMITH', 'JOHN', None, None, None, None, None, None, None, None],
        ['NM1', 'IL', '1', 'SMITH', 'JANE', '', '', '', 'MI', '123222222', None, None, None],
        ['NM1', '74', '1', 'SMITH', 'JANE', 'A', None, None, None, None, None, None, None],
        ['REF', 'CE', 'CHOYC', None],
        ['REF', '1L', '717171', None],
        ['DTM', '050', '20120303', None, None, None, None],
        ['DTM', '232', '20120223', None, None, None, None],
        ['AMT', 'AU', '12145.65', None],
        ['SVC', ['HC', '88888', None, None, None, None, None, None], '23276.56', '12145.65', '', '1', [None, None, None, None, None, None, None, None], None],
        ['DTM', '472', '20120221', None, None, None, None],
        ['CAS', 'CO', '45', '11130.91', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['REF', '6R', '252222222222', None],
        ['AMT', 'B6', '12145.65', None],
        ['LQ', 'HE', 'N220'],
        ['LQ', 'HE', 'M68'],
        ['PLB', '743238060', '20121231', ['WO', '12104411559120820 001GAL295513'], '-361.19', [None, None], None, [None, None], None, [None, None], None, [None, None], None, [None, None], None],
        ['SE', '43', '0001'],
        ['GE', '1', '15555'],
        ['IEA', '1', '000015442'],
    ]
    assert list(msg.segment_iter()) == expected

def test_835_example_2() -> None:
    example = EXAMPLES / "835-example-2.txt"
    document = Source(example.read_text())
    msg = msg_835_5010_X221_A1.MSG835W1.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', 'MYCLEARINGHOUSE', 'ZZ', 'RECVCODE       ', '120323', '1938', 'U', '00401', '000015442', '1', 'P', '^'],
        ['GS', 'HP', 'MYCLEARINGHOUSE', 'RECVCODE', '20120323', '1938', '15555', 'X', '004010X091A1'],
        ['ST', '835', '0001', None],
        ['BPR', 'I', '12345.67', 'C', 'ACH', 'CCP', '01', '999999999', 'DA', '1234567890', '1111111111', '000011111', '01', '222222222', 'DA', '3333333333', '20120322', None, None, None, None, None],
        ['TRN', '1', '1QG11111111', '1111111111', '000011111'],
        ['DTM', '405', '20120319', None, None, None, None],
        ['N1', 'PR', 'UNITED HEALTHCARE INSURANCE COMPANY', 'XV', '87726', None, None],
        ['N3', '9900 BREN ROAD', None],
        ['N4', 'MINNETONKA', 'MN', '553430000', None, None, None, None],
        ['REF', '2U', '87726', None],
        ['PER', 'CX', 'ATLANTA SERVICE CENTER', 'TE', '8778423210', None, None, None, None, None],
        ['N1', 'PE', 'MY CLINIC', 'XX', '1333333333', None, None],
        ['N3', '123 HEALTHCARE STREET', None],
        ['N4', 'SAN FRANCISCO', 'CA', '94109', None, None, None, None],
        ['REF', 'TJ', '777777777', None],
        ['LX', '1'],
        ['TS3', '1333333333', '81', '20121231', '1', '200.02', '200.02', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['CLP', '001-DDDDDDDDDD', '1', '200.02', '200.02', None, '13', '1234567890 0987654321', '81', None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'DOE', 'JOHN', None, None, None, None, None, None, None, None],
        ['NM1', 'IL', '1', 'DOE', 'JANE', '', '', '', 'MI', '123111111', None, None, None],
        ['NM1', '74', '1', 'DOE', 'JANE', 'D', None, None, None, None, None, None, None],
        ['NM1', '82', '2', 'MY CLINIC', '', '', '', '', 'XX', '1333333333', None, None, None],
        ['REF', 'CE', 'CHOYC+', None],
        ['REF', '1L', '5G5G5G', None],
        ['DTM', '232', '20120222', None, None, None, None],
        ['AMT', 'AU', '200.02', None],
        ['SVC', ['HC', '88888', None, None, None, None, None, None], '200.02', '200.02', '', '1', [None, None, None, None, None, None, None, None], None],
        ['DTM', '472', '20120222', None, None, None, None],
        ['REF', '6R', '251111111111', None],
        ['AMT', 'B6', '200.02', None],
        ['SE', '28', '0001'],
        ['ST', '835', '0002', None],
        ['BPR', 'I', '12000.65', 'C', 'ACH', 'CCP', '01', '999999990', 'DA', '1234567891', '1111111112', '000011112', '01', '222222223', 'DA', '3333333334', '20120322', None, None, None, None, None],
        ['TRN', '1', '1QG11111112', '1111111112', '000011112'],
        ['DTM', '405', '20120319', None, None, None, None],
        ['N1', 'PR', 'ACME, INC. A WHOLLY OWNED SUBSIDIARY OF UNITED HEALTHCARE INSURANCE COMPANY', 'XV', '87726', None, None],
        ['N3', '123 MAIN STREET', None],
        ['N4', 'ANYTOWN', 'CA', '940660000', None, None, None, None],
        ['REF', '2U', '87726', None],
        ['N1', 'PE', 'MY CLINIC', 'XX', '1333333333', None, None],
        ['N3', '123 HEALTHCARE STREET', None],
        ['N4', 'SAN FRANCISCO', 'CA', '94109', None, None, None, None],
        ['REF', 'TJ', '777777777', None],
        ['LX', '1'],
        ['TS3', '1333333333', '81', '20121231', '1', '23276.56', '12000.65', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['CLP', '001-SSSSSSSSST', '1', '23276.56', '12000.65', '145', '14', '2234567891 1987654322', '81', None, None, None, None, None, None],
        ['CAS', 'PR', '1', '145', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'SMITH', 'JOHN', None, None, None, None, None, None, None, None],
        ['NM1', 'IL', '1', 'SMITH', 'JANE', '', '', '', 'MI', '123222222', None, None, None],
        ['NM1', '74', '1', 'SMITH', 'JANE', 'A', None, None, None, None, None, None, None],
        ['REF', 'CE', 'CHOYC', None],
        ['REF', '1L', '717171', None],
        ['DTM', '050', '20120303', None, None, None, None],
        ['DTM', '232', '20120223', None, None, None, None],
        ['AMT', 'AU', '12145.65', None],
        ['SVC', ['HC', '88888', None, None, None, None, None, None], '23276.56', '12145.65', '', '1', [None, None, None, None, None, None, None, None], None],
        ['DTM', '472', '20120221', None, None, None, None],
        ['CAS', 'CO', '45', '11130.91', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['REF', '6R', '252222222222', None],
        ['AMT', 'B6', '12145.65', None],
        ['SE', '28', '0002'],
        ['GE', '1', '15555'],
        ['IEA', '1', '000015442'],
    ]
    assert list(msg.segment_iter()) == expected

def test_837_example() -> None:
    """File with a 'compressed' ISA header."""
    example = EXAMPLES / "837-example.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    msg = msg_837_5010_X222_A1.MSG837.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '          ', '00', '          ', 'ZZ', '123456789      ', '30', '41-1674742     ', '060209', '0826', 'U', '00401', '000000002', '0', 'P', ':'],
        ['GS', 'HC', '123456789', '41-1674742', '20060209', '0826', '2', 'X', '004010X098A1'],
        ['ST', '837', '0001', None],
        ['BHT', '0019', '00', '180', '20060209', '0826', 'CH'],
        ['REF', '87', '004010X098A1', None],
        ['NM1', '41', '2', 'Brisbane Schools', '', '', '', '', '46', '567891234', None, None, None],
        ['PER', 'IC', 'Some Contact', 'TE', '5551231234', None, None, None, None, None],
        ['NM1', '40', '2', 'MN Department of Human Services', '', '', '', '', '46', '41-1674742', None, None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', '85', '2', 'Brisbane Schools', '', '', '', '', '24', '12-3456789', None, None, None],
        ['N3', '101 Brisbane Lane', None],
        ['N4', 'Brisbane', 'MN', '561641234', None, None, None, None],
        ['REF', '1D', '123456789', None],
        ['HL', '2', '1', '22', '0'],
        ['SBR', 'S', '18', '', '', None, None, None, None, 'MC'],
        ['NM1', 'IL', '1', 'Student', 'Some', '', '', '', 'MI', '12345678', None, None, None],
        ['N3', '109 Plum Street', None],
        ['N4', 'Somewherein', 'MN.', '56123', None, None, None, None],
        ['DMG', 'D8', '19950505', 'M', None, None, None, None, None, None, None],
        ['NM1', 'PR', '2', 'MN Department of Human Services', '', '', '', '', 'PI', '41-1674742', None, None, None],
        ['CLM', '0777-0777-12345678', '32.73', None, None, ['03', None, '1'], 'Y', 'A', 'Y', 'Y', 'C', [None, None, None, None, None], None, None, None, None, None, None, None, None, None],
        ['LX', '1'],
        ['SV1', ['HC', 'T1018', 'U1', None, None, None, None, None], '10.63', 'UN', '1', None, None, [None, None, None, None], None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['DTP', '472', 'D8', '20060102'],
        ['LX', '2'],
        ['SV1', ['HC', 'T1018', 'U8', None, None, None, None, None], '22.1', 'UN', '10', None, None, [None, None, None, None], None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ['DTP', '472', 'D8', '20060102'],
        ['SE', '26', '0001'],
        ['GE', '1', '2'],
        ['IEA', '1', '000000002'],
    ]
    assert list(msg.segment_iter()) == expected

def test_837I_patient_notsubscriber() -> None:
    """File with a 'compressed' ISA header."""
    example = EXAMPLES / "837I-Patient-NotSubscriber.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    msg = msg_837_5010_X222_A1.MSG837.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '00        ', '00', '00        ', 'ZZ', 'GENERAL HOSP   ', 'ZZ', 'WI911234567    ', '020122', '1100', 'U', '00401', '000000001', '0', 'T', ':'],
        ['GS', 'HC', '91-7777666', '91-1234567', '20020122', '1100', '1', 'X', '004010X096A1'],
        ['ST', '837', '0001', None],
        ['BHT', '0019', '00', '0001', '20020122', '1100', 'CH'],
        ['REF', '87', '004010X096A1', None],
        ['NM1', '41', '2', 'GENERAL HOSP', '', '', '', '', '46', '91-7777666', None, None, None],
        ['PER', 'IC', 'SUSAN', 'TE', '2064551111', None, None, None, None, None],
        ['NM1', '40', '2', ' WORLDWIDE INSUR', '', '', '', '', '46', '91-1234567', None, None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', '85', '2', 'GENERAL HOSP', '', '', '', '', '24', '91-7777666', None, None, None],
        ['N3', '404 2ND AVE', None],
        ['N4', 'SEATTLE', 'WA', '98112', None, None, None, None],
        ['HL', '2', '1', '22', '1'],
        ['SBR', 'P', None, '', 'CSI INC', None, None, None, None, 'CI'],
        ['NM1', 'IL', '1', 'FLINTSTONE', 'FRED', '', '', '', 'MI', 'WW2020-01', None, None, None],
        ['N3', '666 BEDROCK LN', None],
        ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None, None],
        ['NM1', 'PR', '2', ' WORLDWIDE INSUR', '', '', '', '', 'PI', '91-1234567', None, None, None],
        ['N3', '2020 1ST AVE', None],
        ['N4', 'SEATTLE', 'WA', '98112', None, None, None, None],
        ['HL', '3', '2', '23', '0'],
        ['PAT', '19', None, None, None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'FLINSTONE', 'PEBBLES', '', '', '', 'MI', 'WW2020-03', None, None, None],
        ['N3', '666 BEDROCK LN', None],
        ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None, None],
        ['DMG', 'D8', '19721201', 'F', None, None, None, None, None, None, None],
        ['CLM', 'FF555672020', '974', None, None, ['13', 'A', '1'], 'Y', 'A', 'Y', 'A', None, [None, None, None, None, None], None, None, None, None, None, None, 'Y', None, None],
        ['DTP', '434', 'D8', '20011101'],
    ]
    assert list(msg.segment_iter()) == expected


def test_837I_patient_notsubscriber2() -> None:
    """File with a 'compressed' ISA header."""
    example = EXAMPLES / "837I-Patient-NotSubscriber2.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    msg = msg_837_5010_X222_A1.MSG837.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '00        ', '00', '00        ', 'ZZ', 'GENERAL HOSP   ', 'ZZ', 'WHS915779491   ', '020122', '1100', 'U', '00401', '000000001', '0', 'T', ':'],
        ['GS', 'HC', '91-7777666', '91-5779491', '20020122', '1100', '1', 'X', '004010X096A1'],
        ['ST', '837', '0001', None],
        ['BHT', '0019', '00', '0001', '20020122', '1100', 'CH'],
        ['REF', '87', '004010X096A1', None],
        ['NM1', '41', '2', 'GENERAL HOSP', '', '', '', '', '46', '917777666', None, None, None],
        ['PER', 'IC', 'SUSAN', 'TE', '2064551111', None, None, None, None, None],
        ['NM1', '40', '2', ' WASHINGTON HEALTH SERVICES', '', '', '', '', '46', '915779491', None, None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', '85', '2', 'GENERAL HOSP', '', '', '', '', '24', '917777666', None, None, None],
        ['N3', '404 2ND AVE', None],
        ['N4', 'SEATTLE', 'WA', '98112', None, None, None, None],
        ['HL', '2', '1', '22', '1'],
        ['SBR', 'S', None, '', 'CSI INC', None, None, None, None, 'CI'],
        ['NM1', 'IL', '1', 'FLINTSTONE', 'WILMA', '', '', '', 'MI', 'WF55550', None, None, None],
        ['N3', '666 BEDROCK LN', None],
        ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None, None],
        ['NM1', 'PR', '2', ' WASHINGTON HEALTH SERVICES', '', '', '', '', 'PI', '915779491', None, None, None],
        ['N3', '234 2ND AVE', None],
        ['N4', 'SEATTLE', 'WA', '98112', None, None, None, None],
        ['HL', '3', '2', '23', '0'],
        ['PAT', '17', None, None, None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'FLINSTONE', 'PEBBLES', '', '', '', 'MI', 'WF5555002', None, None, None],
        ['N3', '666 BEDROCK LN', None],
        ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None, None],
        ['DMG', 'D8', '19721201', 'F', None, None, None, None, None, None, None],
        ['CLM', 'FF559872032', '3712', None, None, ['11', 'A', '1'], 'Y', 'A', 'Y', 'A', None, [None, None, None, None, None], None, None, None, None, None, None, 'Y', None, None],
        ['DTP', '096', 'TM', '1700'],
        ['DTP', '434', 'RD8', '20011115-20011117'],
        ['DTP', '435', 'DT', '200111151500'],
    ]
    assert list(msg.segment_iter()) == expected

def test_837I_patient_subscriber() -> None:
    """File with a 'compressed' ISA header."""
    example = EXAMPLES / "837I-Patient-Subscriber.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    msg = msg_837_5010_X222_A1.MSG837.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '00', '00        ', '00', '00        ', 'ZZ', 'CRU1234        ', 'ZZ', 'WI911234567    ', '020122', '1100', 'U', '00401', '000000001', '0', 'T', ':'],
        ['GS', 'HC', '91-1257070', '91-1234567', '20020122', '1100', '1', 'X', '004010X096A1'],
        ['ST', '837', '0001', None],
        ['BHT', '0019', '00', '0001', '20020122', '1100', 'CH'],
        ['REF', '87', '004010X096A1', None],
        ['NM1', '41', '2', 'CLAIMS R US', '', '', '', '', '46', '911257070', None, None, None],
        ['PER', 'IC', 'CONTACT NAME', 'TE', '555-546-1234', None, None, None, None, None],
        ['NM1', '40', '2', ' WORLDWIDE INSUR', '', '', '', '', '46', '911234567', None, None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', '85', '2', 'GENERAL HOSP', '', '', '', '', '24', '917777666', None, None, None],
        ['N3', '404 2ND AVE', None],
        ['N4', 'SEATTLE', 'WA', '98112', None, None, None, None],
        ['REF', 'G2', 'XYZ', None],
        ['HL', '2', '1', '22', '0'],
        ['SBR', 'P', '18', '', 'CSI INC', None, None, None, None, 'CI'],
        ['NM1', 'IL', '1', 'FLINTSTONE', 'FRED', '', '', '', 'MI', 'WW2020-01', None, None, None],
        ['N3', '666 BEDROCK LN', None],
        ['N4', 'QUARRYVILLE', 'WA', '98666', None, None, None, None],
        ['DMG', 'D8', '19501101', 'M', None, None, None, None, None, None, None],
        ['NM1', 'PR', '2', ' WORLDWIDE INSUR', '', '', '', '', 'PI', '911234567', None, None, None],
        ['N3', '2020 1ST AVE', None],
        ['N4', 'SEATTLE', 'WA', '98112', None, None, None, None],
        ['CLM', 'FF555202020', '2750', None, None, ['11', 'A', '1'], 'Y', 'A', 'Y', 'Y', None, [None, None, None, None, None], None, None, None, None, None, None, 'Y', None, None],
        ['DTP', '096', 'TM', '0900'],
        ['DTP', '434', 'RD8', '20011205-20011207'],
        ['DTP', '435', 'DT', '200112051000'],
    ]
    assert list(msg.segment_iter()) == expected

@mark.skip("The 837I-Examples.txt file appears damaged")
def test_837I_examples() -> None:
    example = EXAMPLES / "837I-Examples.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    msg = msg_837_5010_X222_A1.MSG837.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        # ISA...ESA, ISA...ESA for two messages of this class.
    ]
    assert list(msg.segment_iter()) == expected

def test_276_txns() -> None:
    """
    Transaction set, Multiple messages in a single file.
    File with a 'compressed' ISA header.
    """
    example = EXAMPLES / "TEST 276 TXNs.txt"
    document = Source(example.read_text(), element_sep="*", array_sep=":", segment_sep="~")
    msg = msg_276_4010_X093_A1.MSG276.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '03', 'mdycha1   ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0904', 'U', '00401', '000246742', '0', 'T', ':'],
        ['GS', 'HR', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0904', '245842', 'X', '004010X093A1'],
        ['ST', '276', '246742'],
        ['BHT', '0010', '13', '', '20071015', None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '41', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'FI', '830382654', None, None],
        ['HL', '3', '2', '19', '1'],
        ['NM1', '1P', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'SV', '000000042000', None, None],
        ['HL', '4', '3', '22', '0'],
        ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'YJP88091836301', None, None],
        ['TRN', '1', 'GZCSMXKRDR', None, None],
        ['AMT', 'T3', '0', None],
        ['DTP', '232', 'RD8', '20070919-20070921'],
        ['SE', '15', '246742'],
        ['GE', '1', '245842'],
        ['IEA', '1', '000246742'],

        ['ISA', '03', 'mdycha1   ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0905', 'U', '00401', '000246785', '0', 'T', ':'],
        ['GS', 'HR', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0905', '245885', 'X', '004010X093A1'],
        ['ST', '276', '246785'],
        ['BHT', '0010', '13', '', '20071015', None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '41', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'FI', '830382654', None, None],
        ['HL', '3', '2', '19', '1'],
        ['NM1', '1P', '2', 'ERIE COUNTY MEDICAL CENTER', '', '', '', '', 'SV', '000000042000', None, None],
        ['HL', '4', '3', '22', '0'],
        ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'YJP88101119801', None, None],
        ['TRN', '1', 'MVFWVYEJJD', None, None],
        ['AMT', 'T3', '0', None],
        ['DTP', '232', 'RD8', '20070919-20070922'],
        ['SE', '15', '246785'],
        ['GE', '1', '245885'],
        ['IEA', '1', '000246785'],

        ['ISA', '03', 'lhammond1 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', '071015', '0909', 'U', '00401', '000032685', '0', 'T', ':'],
        ['GS', 'HR', '0000000Eliginet', 'BlueShield of N', '20071015', '0909', '31785', 'X', '004010X093A1'],
        ['ST', '276', '32685'],
        ['BHT', '0010', '13', '', '20071015', None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '41', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'FI', '141338413', None, None],
        ['HL', '3', '2', '19', '1'],
        ['NM1', '1P', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'SV', '000400010000', None, None],
        ['HL', '4', '3', '22', '0'],
        ['DMG', 'D8', '19740201', 'U', None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'ZWP88005432001', None, None],
        ['TRN', '1', 'COPROCKESA', None, None],
        ['AMT', 'T3', '0', None],
        ['DTP', '232', 'RD8', '20070815-20070815'],
        ['SE', '15', '32685'],
        ['GE', '1', '31785'],
        ['IEA', '1', '000032685'],

        ['ISA', '03', 'lhammond1 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', '071015', '0911', 'U', '00401', '000032694', '0', 'T', ':'],
        ['GS', 'HR', '0000000Eliginet', 'BlueShield of N', '20071015', '0911', '31794', 'X', '004010X093A1'],
        ['ST', '276', '32694'],
        ['BHT', '0010', '13', '', '20071015', None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '41', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'FI', '141338413', None, None],
        ['HL', '3', '2', '19', '1'],
        ['NM1', '1P', '2', 'GLENS FALLS HOSPITAL', '', '', '', '', 'SV', '000400010000', None, None],
        ['HL', '4', '3', '22', '0'],
        ['DMG', 'D8', '19990705', 'U', None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'ZWX88065356704', None, None],
        ['TRN', '1', 'UGXSOJFCFD', None, None],
        ['AMT', 'T3', '0', None],
        ['DTP', '232', 'RD8', '20070725-20070725'],
        ['SE', '15', '32694'],
        ['GE', '1', '31794'],
        ['IEA', '1', '000032694'],

        ['ISA', '03', 'mormond   ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0926', 'U', '00401', '000247238', '0', 'T', ':'],
        ['GS', 'HR', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0926', '246338', 'X', '004010X093A1'],
        ['ST', '276', '247238'],
        ['BHT', '0010', '13', '', '20071015', None, None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'PR', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '41', '2', "MOUNT ST MARY'S HOSPITAL", '', '', '', '', 'FI', '161523353', None, None],
        ['HL', '3', '2', '19', '1'],
        ['NM1', '1P', '2', "MOUNT ST MARY'S HOSPITAL", '', '', '', '', 'SV', '000000022000', None, None],
        ['HL', '4', '3', '22', '0'],
        ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
        ['NM1', 'QC', '1', 'lastname', 'firstname', '', '', '', 'MI', 'yjw99000745701', None, None],
        ['TRN', '1', 'GGEEMIMLEV', None, None],
        ['AMT', 'T3', '0', None],
        ['DTP', '232', 'RD8', '20070827-20070830'],
        ['SE', '15', '247238'],
        ['GE', '1', '246338'],
        ['IEA', '1', '000247238'],
    ]
    assert list(msg.segment_iter()) == expected


def test_278_13_txns() -> None:
    """
    Transaction set, Multiple messages in a single file.
    File with a 'compressed' ISA header.
    """
    example = EXAMPLES / "TEST 278_13 TXNS.txt"
    document = Source(example.read_text())
    # document = Source(example.read_text(), element_sep="*", segment_sep="~")
    msg = msg_278_4010_X094_A1.MSG278.parse(document)
    # print("[")
    # for s in msg.segment_iter():
    #     print(f"    {s},")
    # print("]")
    expected = [
        ['ISA', '03', 'gjohnson2 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0903', 'U', '00401', '000242835', '0', 'P', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0903', '241935', 'X', '004010X094A1'],
        ['ST', '278', '242835'],
        ['BHT', '0078', '13', 'GXEDWLXQYKII', '20071015', '0903', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '1', 'SHEIKH', 'ZIA', '', '', '', '24', '161590688', None, None],
        ['REF', 'ZH', '000524454008', None],
        ['N3', '4039 ROUTE 219', 'SUITE 102'],
        ['N4', 'SALAMANCA', 'NY', '14779', None, None, None],
        ['HL', '3', '2', '22', '1'],
        ['HI', ['BF', '706.1', None, None, None, None, None]],
        ['NM1', 'IL', '1', 'burton', 'amanda', '', '', '', 'MI', 'yjw88034076701', None, None],
        ['DMG', 'D8', '19900815', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', '19', '1'],
        ['NM1', 'SJ', '1', 'JAREMKO', 'WILLIAM', '', '', '', '24', '161482964', None, None],
        ['REF', 'ZH', '000511127003', None],
        ['N3', '2646 WEST STATE STREET', 'SUITE 405'],
        ['N4', 'OLEAN', 'NY', '147600000', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'SC', 'I', None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20080415'],
        ['HSD', 'VS', '30', None, None, None, None, None, None],
        ['SE', '24', '242835'],
        ['GE', '1', '241935'],
        ['IEA', '1', '000242835'],

        ['ISA', '03', 'jrandazzo ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0903', 'U', '00401', '000242836', '0', 'P', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0903', '241936', 'X', '004010X094A1'],
        ['ST', '278', '242836'],
        ['BHT', '0078', '13', 'KLTVJTDDRYEM', '20071015', '0903', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '1', 'PERNA', 'ANTHONY', '', '', '', '24', '161260886', None, None],
        ['REF', 'ZH', '000500338001', None],
        ['N3', '41 DELAWARE ROAD', None],
        ['N4', 'KENMORE', 'NY', '142172742', None, None, None],
        ['HL', '3', '2', '22', '1'],
        ['HI', ['BF', '599.7', None, None, None, None, None]],
        ['NM1', 'IL', '1', 'farrugia', 'brenda', '', '', '', 'MI', '88027756201', None, None],
        ['DMG', 'D8', '19391111', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', '19', '1'],
        ['NM1', 'SJ', '1', 'GRECO', 'JOSEPH', '', '', '', '24', '161511795', None, None],
        ['REF', 'ZH', '000507772005', None],
        ['N3', '55 SPINDRIFT DRIVE', 'SUITE 240'],
        ['N4', 'WILLIAMSVILLE', 'NY', '14221', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'SC', 'I', None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20080415'],
        ['HSD', 'VS', '10', None, None, None, None, None, None],
        ['SE', '24', '242836'],
        ['GE', '1', '241936'],
        ['IEA', '1', '000242836'],

        ['ISA', '03', 'dnoone    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', '071015', '0903', 'U', '00401', '000032674', '0', 'P', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BlueShield of N', '20071015', '0903', '31774', 'X', '004010X094A1'],
        ['ST', '278', '32674'],
        ['BHT', '0078', '13', 'ENLENGSDPMTQ', '20071015', '0903', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '1', 'VACEK', 'JAMES', '', '', '', '24', '141338465', None, None],
        ['REF', 'ZH', '000401141002', None],
        ['N3', '99 EAST STATE STREET', None],
        ['N4', 'GLOVERSVILLE', 'NY', None, None, None, None],
        ['HL', '3', '2', '22', '1'],
        ['HI', ['BF', '366.19', None, None, None, None, None]],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', '88003509901', None, None],
        ['DMG', 'D8', '19221209', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', '19', '1'],
        ['NM1', 'SJ', '1', 'MAIRS', 'MICHAEL', '', '', '', '24', '141786068', None, None],
        ['REF', 'ZH', '000407032001', None],
        ['N3', '185 SECOND AVENUE', None],
        ['N4', 'GLOVERSVILLE', 'NY', '12078', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'SC', 'I', None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20080415'],
        ['HSD', 'VS', '20', None, None, None, None, None, None],
        ['SE', '24', '32674'],
        ['GE', '1', '31774'],
        ['IEA', '1', '000032674'],

        ['ISA', '03', 'gjohnson2 ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0904', 'U', '00401', '000242839', '0', 'P', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0904', '241939', 'X', '004010X094A1'],
        ['ST', '278', '242839'],
        ['BHT', '0078', '13', 'WHBMBBXDSPML', '20071015', '0904', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '1', 'SHEIKH', 'ZIA', '', '', '', '24', '161590688', None, None],
        ['REF', 'ZH', '000524454008', None],
        ['N3', '4039 ROUTE 219', 'SUITE 102'],
        ['N4', 'SALAMANCA', 'NY', '14779', None, None, None],
        ['HL', '3', '2', '22', '1'],
        ['HI', ['BF', '706.1', None, None, None, None, None]],
        ['NM1', 'IL', '1', 'burton', 'amanda', '', '', '', 'MI', 'yjw88034076701', None, None],
        ['DMG', 'D8', '19900815', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', '19', '1'],
        ['NM1', 'SJ', '1', 'JAREMKO', 'WILLIAM', '', '', '', '24', '161482964', None, None],
        ['REF', 'ZH', '000511127003', None],
        ['N3', '2646 WEST STATE STREET', 'SUITE 405'],
        ['N4', 'OLEAN', 'NY', '147600000', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'SC', 'I', None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20080415'],
        ['HSD', 'VS', '30', None, None, None, None, None, None],
        ['SE', '24', '242839'],
        ['GE', '1', '241939'],
        ['IEA', '1', '000242839'],

        ['ISA', '03', 'tmason    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BlueShield of N', '071015', '0905', 'U', '00401', '000032679', '0', 'P', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BlueShield of N', '20071015', '0905', '31779', 'X', '004010X094A1'],
        ['ST', '278', '32679'],
        ['BHT', '0078', '13', 'EOCMUPJPJCEO', '20071015', '0905', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUESHIELD OF NORTHEASTERN NEW YORK', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '1', 'MAZZEI', 'RENATA', '', '', '', '24', '141338428', None, None],
        ['REF', 'ZH', '000404963001', None],
        ['N3', '460 SARATOGA ROAD', None],
        ['N4', 'SCOTIA', 'NY', '12302', None, None, None],
        ['HL', '3', '2', '22', '1'],
        ['HI', ['BF', 'V65.8', None, None, None, None, None]],
        ['NM1', 'IL', '1', 'whitney', 'james', '', '', '', 'MI', '88059250301', None, None],
        ['DMG', 'D8', '19701002', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', '19', '1'],
        ['NM1', 'SJ', '1', 'NYDEGGER', 'RUDY', '', '', '', '24', '141787916', None, None],
        ['REF', 'ZH', '000471951001', None],
        ['N3', '1201 NOTT STREET', 'SUITE 103'],
        ['N4', 'SCHENECTADY', 'NY', '123082589', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'SC', 'I', None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20080415'],
        ['HSD', 'VS', '6', None, None, None, None, None, None],
        ['SE', '24', '32679'],
        ['GE', '1', '31779'],
        ['IEA', '1', '000032679'],
    ]
    assert list(msg.segment_iter()) == expected


def test_278_28_txns_soa_example() -> None:
    """
    Transaction set, Multiple messages in a single file.
    File with a 'compressed' ISA header.
    """
    example = EXAMPLES / "TEST 278_28 TXNS_SOA.txt"
    document = Source(example.read_text())
    # document = Source(example.read_text(), element_sep="*", segment_sep="~")
    msg = msg_278_4010_X094_A1.MSG278.parse(document)
    print("[")
    for s in msg.segment_iter():
        print(f"    {s},")
    print("]")
    expected = [
        ['ISA', '03', 'jking3    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0905', 'U', '00401', '000246767', '0', 'T', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0905', '245867', 'X', '004010X059'],
        ['ST', '278', '246767'],
        ['BHT', '0083', '28', 'XPMPDTETJDHS', '20071015', '0905', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '1', 'SHAH', 'SIDDHARTHA', '', '', '', '24', '161569074', None, None],
        ['REF', 'ZH', '000511391004', None],
        ['HL', '3', '2', '22', '1'],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJE88000251501', None, None],
        ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', 'PA', '1'],
        ['NM1', 'DN', '1', 'SHAH', 'SIDDHARTHA', '', '', '', '24', '161569074', None, None],
        ['REF', 'ZH', '000511391004', None],
        ['N3', '60 MAPLE ROAD', None],
        ['N4', 'WILLIAMSVILLE', 'NY', '142212918', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'SC', None, None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20071113'],
        ['SE', '20', '246767'],
        ['GE', '1', '245867'],
        ['IEA', '1', '000246767'],

        ['ISA', '03', 'bjary     ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0905', 'U', '00401', '000242872', '0', 'T', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0905', '241972', 'X', '004010X059'],
        ['ST', '278', '242872'],
        ['BHT', '0083', '28', 'JVQWCOPYJBYW', '20071015', '0905', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '1', 'SANSANO JR', 'MICHAEL', '', '', '', '24', '161505558', None, None],
        ['REF', 'ZH', '000511031001', None],
        ['HL', '3', '2', '22', '1'],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJE88001567901', None, None],
        ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', 'PA', '1'],
        ['NM1', 'DN', '1', 'SANSANO JR', 'MICHAEL', '', '', '', '24', '161505558', None, None],
        ['REF', 'ZH', '000511031001', None],
        ['N3', '515 ABBOTT ROAD', 'SUITE 206'],
        ['N4', 'BUFFALO', 'NY', '14220', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'SC', None, None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071012-20071110'],
        ['SE', '20', '242872'],
        ['GE', '1', '241972'],
        ['IEA', '1', '000242872'],

        ['ISA', '03', 'HEALTHNOW ', '00', 'HEALTHNOW ', 'ZZ', 'KALEIDAHEALTH01', 'ZZ', 'KaleidaHealth01', '071015', '0905', 'U', '00401', '905310466', '0', 'T', ':'],
        ['GS', 'HI', '2000002', 'BLUECROSS BLUES', '20071015', '0905', '905310467', 'X', '004010X059'],
        ['ST', '278', '905310467'],
        ['BHT', '0083', '28', '278R2   6370177   3CWW585', '20071015', '0905', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', '', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', '', '', '', '', '', '24', '161533232', None, None],
        ['REF', 'ZH', '000000001000', None],
        ['HL', '3', '2', '22', '1'],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJP88045401902', None, None],
        ['HL', '4', '3', 'SS', '0'],
        ['TRN', '1', 'CWW585', '9999999999', '6370177'],
        ['UM', 'AR', None, None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20071114'],
        ['SE', '14', '905310467'],
        ['GE', '1', '905310467'],
        ['IEA', '1', '905310466'],

        ['ISA', '03', 'cww585    ', '01', '0000000000', 'ZZ', '0000000Eliginet', 'ZZ', 'BLUECROSS BLUES', '071015', '0905', 'U', '00401', '000246782', '0', 'T', ':'],
        ['GS', 'HI', '0000000Eliginet', 'BLUECROSS BLUES', '20071015', '0905', '245882', 'X', '004010X059'],
        ['ST', '278', '246782'],
        ['BHT', '0083', '28', 'JNPLOLKXXOBO', '20071015', '0905', None],
        ['HL', '1', '', '20', '1'],
        ['NM1', 'X3', '2', 'BLUECROSS BLUESHIELD OF WESTERN NEW', '', '', '', '', 'PI', '55204', None, None],
        ['HL', '2', '1', '21', '1'],
        ['NM1', '1P', '2', 'BUFFALO GENERAL HOSPITAL', '', '', '', '', '24', '161533232', None, None],
        ['REF', 'ZH', '000000001000', None],
        ['HL', '3', '2', '22', '1'],
        ['NM1', 'IL', '1', '', '', '', '', '', 'MI', 'YJP88045401902', None, None],
        ['DMG', 'D8', '19010101', 'U', None, None, None, None, None, None],
        ['HL', '4', '3', 'PA', '1'],
        ['NM1', 'DN', '2', 'BUFFALO GENERAL HOSPITAL', '', '', '', '', '24', '161533232', None, None],
        ['REF', 'ZH', '000000001000', None],
        ['N3', '100 HIGH STREET', None],
        ['N4', 'BUFFALO', 'NY', '14203', None, None, None],
        ['HL', '5', '4', 'SS', '0'],
        ['TRN', '1', '1', '9999955204', None],
        ['UM', 'AR', None, None, ['', None, None], [None, None, None, None, None], None, None, None, 'Y', None],
        ['DTP', '472', 'RD8', '20071015-20071113'],
        ['SE', '20', '246782'],
        ['GE', '1', '245882'],
        ['IEA', '1', '000246782'],
    ]
    assert list(msg.segment_iter()) == expected
