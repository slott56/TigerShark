"""
Test Field Extraction shown in the README.
"""

from x12 import msg_835_4010_X091_A1
from x12.base import Source, X12Parser
from pathlib import Path

def test_extract() -> None:
    EXAMPLES = Path.cwd() / "tests"  # Should be run in the parent directory
    example = EXAMPLES / "835-example.txt"
    document = Source(example.read_text())
    # Skip some validation rules
    errors_here = [
      "*_N1:n101:Enumerated", "*_N1:n103:Enumerated", "*_REF:ref01:Enumerated",
      "*_NM1:nm101:Enumerated", "*_NM1:nm102:Enumerated", "*_NM1:nm108:Enumerated"
    ]
    parser = X12Parser(msg_835_4010_X091_A1.MSG835, skip_validation=errors_here)
    msg = parser.parse(document)

    # Payee is in N1 in Loop 1000A. L1000A_N1 found in HEADER.ItemL1000A
    # The ISA/GS/ST structure is always similar.
    n1 = msg.isa_loop[0].gs_loop[0].st_loop[0].header[0].l1000a[0].n1
    # print(n1)
    n4 = msg.isa_loop[0].gs_loop[0].st_loop[0].header[0].l1000a[0].n4
    # print(n4)
    ts3 = msg.isa_loop[0].gs_loop[0].st_loop[0].detail[0].l2000[0].ts3
    # print(ts3)

    assert n1.n102 == "UNITED HEALTHCARE INSURANCE COMPANY"
    assert n4.n403 == "553430000"
    assert ts3.ts304 == 2.0
