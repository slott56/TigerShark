"""
Candidate "main" application to convert Exchange format to JSON and JSON to Exchange format.
"""
import argparse
import importlib
import logging
from pathlib import Path
import sys

from x12.base import Source, Message
# from x12 import msg_834_5010_X220_A1
import x12

logger = logging.getLogger("tigershark3")

def get_options(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", "-f", choices=("json", "exchange", "segments", "python"), default="json")
    parser.add_argument("--output", "-o", type=Path, default=None)
    parser.add_argument("source", nargs=1, type=Path)
    parser.add_argument("--package", "-p", type=str, default="x12", help="Python package with message modules")
    parser.add_argument("--message", "-m", type=str, default="msg_834_5010_X220_A1.MSG834A1", help="message module.class")
    parser.add_argument("--separators", "-s", type=str, default="", help="separators when parsing compressed ISA segments, for example '*:~'")
    parser.add_argument("--debug", "-d", dest="log_level", action='store_const', const=logging.DEBUG, default=logging.INFO)
    options = parser.parse_args(argv)
    module_name, _, cls_name = options.message.partition(".")
    try:
        importlib.import_module(f"{options.package}.{module_name}", package='x12')
        options.message_class = eval(f"{options.package}.{module_name}.{cls_name}")
    except NameError as ex:
        parser.error(f"unknown message class {options.package}.{options.message}")
    if options.separators:
        try:
            options.element_sep, _, options.segment_sep = options.separators
        except ValueError as ex:
            parser.error(f"separators must be three characters, for example '*:~'")
    else:
        options.element_sep = options.segment_sep = ""
    return options

def exchange_to_python(source: Path, message_class: type[Message], element_sep: str = "", segment_sep: str = "") -> None:
    """
    Output is "segments" format, used for unit test output...
    """
    document = Source(source.read_text(), element_sep=element_sep, segment_sep=segment_sep)
    msg = message_class.parse(document)
    if msg:
        print(repr(msg))
    else:
        logger.error("No message parsed from %s as %r", source, message_class)


def exchange_to_segments(source: Path, message_class: type[Message], element_sep: str = "", segment_sep: str = "") -> None:
    """
    Output is "segments" format, used for unit test output...
    """
    document = Source(source.read_text(), element_sep=element_sep, segment_sep=segment_sep)
    msg = message_class.parse(document)
    if msg:
        print(list(msg.segment_iter()))
    else:
        logger.error("No message parsed from %s as %r", source, message_class)

def exchange_to_json(source: Path, message_class: type[Message], element_sep: str = "", segment_sep: str = "") -> None:
    """
    TODO: Output is "json" format.
    """
    document = Source(source.read_text(), element_sep=element_sep, segment_sep=segment_sep)
    msg = message_class.parse(document)
    print(msg.json())

def main(argv: list[str] = sys.argv[1:]) -> None:
    options = get_options(argv)
    logging.getLogger().setLevel(options.log_level)
    # Assume format is "segments" which lists the segments
    # Assume output is not specified (which means stdout)
    logger.info("Loading %r using %r", options.source[0], options.message_class)
    if options.element_sep or options.segment_sep:
        logger.info("  Compressed ISA, separators %r %r", options.element_sep, options.segment_sep)
    if options.format == "segments":
        exchange_to_segments(options.source[0], options.message_class, options.element_sep, options.segment_sep)
    elif options.format == "python":
        exchange_to_python(options.source[0], options.message_class, options.element_sep, options.segment_sep)
    elif options.format == "json":
        exchange_to_json(options.source[0], options.message_class, options.element_sep, options.segment_sep)
    else:
        raise NotImplementedError(f"unsupporeted {options.format}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    message_options = []
    examples = Path.cwd().parent / "tests"

    # message_path = examples / "834-example.txt"
    # message_class = "msg_834_5010_X220_A1.MSG834A1"

    # message_path = examples / "835-example.txt"
    # Failed: message_class = "msg_835_4010_X091_A1.MSG835"  # Unexpected L2100_NM109
    # message_class = "msg_835_5010_X221_A1.MSG835W1"

    # message_path = examples / "835-example-2.txt"
    # message_class = "msg_835_5010_X221_A1.MSG835W1"

    # Some problems with example file and message definitions.
    # message_path = examples / "837I-Examples.txt" # Damanged file
    # message_class = "msg_837Q3_I_5010_X223_A1_v2.MSG837Q3"  # Appears incomplete
    # message_class = "msg_837_5010_X222_A1.MSG837"

    # Multi-transaction files...
    # message_path = examples / "TEST 276 TXNs.txt"
    # message_class = "msg_276_4010_X093_A1.MSG276"
    # message_options = ["-s", "*:~", "-f"]

    # Documentation example.
    # message_path = examples / "271-example.txt"
    # message_class = "msg_271_4010_X092_A1.MSG271"

    # Separators Issues.
    message_path = examples / "TEST 278_13 TXNS.txt"
    message_class = "msg_278_4010_X094_A1.MSG278"

    # Command-line.
    main(["-d", "-m", message_class, "-f", "json"] + message_options + [str(message_path)])
    logging.shutdown()
