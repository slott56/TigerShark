from tigershark.X12 import message


def pprint(x12_message, level=0, indent=" "):
    """ Pretty print the parsed message.

    :param loop: The `X12.message.X12Message` to print.
    :type loop: `X12.message.X12Message`
    :param level: The current indentation level.
    :type level: int
    :param indent: The character(s) to use for indentation.
    :type indent: String
    """
    if x12_message.parts is not None:
        for segment in x12_message.parts:
            if isinstance(segment, message.X12Segment):
                print("{indent}{name} - {elements}".format(
                    indent=level * indent,
                    name=segment.name,
                    elements=segment.elements))
            else:
                print("{indent}#### {name} ####".format(
                    indent=(level + 1) * indent,
                    name=segment.name))
                pprint(segment, level + 1, indent)
