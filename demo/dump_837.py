"""
Dump the 837-bug-sample.txt message
"""
from pathlib import Path
from x12 import msg_837_5010_X222_A1
from x12.base import Source, X12Parser, asdict
import json
import logging

def main():
    EXAMPLES = Path.cwd()
    example = EXAMPLES / "837-bug-sample.txt"
    document = Source(example.read_text(), segment_sep="~", element_sep="*", array_sep="^")
    # Skip these validation rules
    errors_here = [
        "*_N1:n101:Enumerated", "*_N1:n103:Enumerated", "*_REF:ref01:Enumerated",
        "*_NM1:nm101:Enumerated", "*_NM1:nm102:Enumerated", "*_NM1:nm108:Enumerated",

        # Special cases to read a message for whih we DO NOT have a proper definition.
        "*_ISA:isa11:Enumerated",
        "*_GS:gs08:Enumerated",
        "*_CLM:clm05_01:MaxLen",
        "*_CLM:clm06:MinLen",
        "*_DTP:dtp01:Enumerated",
        "*_DTP:dtp02:Enumerated",
    ]
    parser = X12Parser(msg_837_5010_X222_A1.MSG837, skip_validation=errors_here)
    msg = parser.parse(document)

    for segment in msg.segment_iter():
        print(segment)

    print(json.dumps(asdict(msg), indent=2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("x12.base.Segment").setLevel(logging.DEBUG)

    main()

    logging.shutdown()
