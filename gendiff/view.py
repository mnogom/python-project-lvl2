"""Module to create several representation."""

from gendiff.node_explorer import is_leaf

DICTIONARY = {True: "true",
              False: "false",
              None: "null"}
INDENT = 2


def _check_signature(value):
    """Check json signature of True/False/None"""

    if is_leaf(value):
        return DICTIONARY.get(value, str(value))
    return value


def _partition_status_key(status_key, unchached_marker):
    """Partition key_status to key and status"""

    if status_key[0] in "+- ":
        return status_key[0], status_key[2:]
    return unchached_marker, status_key


# def dict2str(data: dict) -> str:
#     """Convert dictionary to formatted string
#
#     :param data: input data in dict format
#     :return: formatted string
#     """
#
#     return json.dumps(data,
#                       indent=2,
#                       separators=("", ": ")).replace("\"", "")


def dict2str(data: dict, unchached_marker=" ") -> str:
    """Convert dictionary to formatted string.

    :param data: input data in dict format
    :return: formatted string
    """

    def inner(new_data, new_indent):
        output = "{\n"
        for status_key, value in new_data.items():

            status, key = _partition_status_key(status_key,
                                                unchached_marker)
            signature_value = _check_signature(value)

            if is_leaf(value):
                output += "{}{} {}:{}".format(
                    " " * new_indent,
                    status, key,
                    " " + signature_value)
                output = output.rstrip(" ") + "\n"

            else:
                output += "{}{} {}: ".format(
                    " " * new_indent,
                    status, key
                )
                output += inner(new_data[status_key], new_indent + INDENT + 2)
        output += " " * (new_indent - INDENT) + "}\n"

        return output
    return inner(data, INDENT)[:-1]
