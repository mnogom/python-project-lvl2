"""Module to create several representation."""

from gendiff.node_explorer import is_leaf
from gendiff.constants import ADDED, REMOVED, UNCHANGED, DICTIONARY,\
    INDENT, ADDED_TEXT, REMOVED_TEXT, CHANGED_TEXT


def _convert_signature(value):
    """Check json signature of True/False/None"""

    if is_leaf(value):
        return DICTIONARY.get(value, str(value))
    return value


def _partition_status_key(status_key):
    """Partition key_status to key and status"""

    if status_key[0] in (ADDED, REMOVED, UNCHANGED):
        return status_key[0], status_key[2:]
    return UNCHANGED, status_key


def _is_updated(key, data):
    pass


def _is_removed(key, data):
    pass


def _is_added(key, data):
    pass


def _is_unchanged(key, data):
    pass


def _difference2stylish(data: dict) -> str:
    """Convert difference to stylish string.

    :param data: input data in dict format
    :return: formatted string
    """

    def inner(new_data, new_indent):
        output = "{\n"
        for status_key, value in new_data.items():

            status, key = _partition_status_key(status_key)
            signature = _convert_signature(value)

            if is_leaf(value):
                output += "{}{} {}:{}".format(
                    " " * new_indent,
                    status, key,
                    " " + signature)
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


def _difference2plain(data: dict) -> str:
    """Convert difference to plain string.

    :param data:
    :return:
    """
    output = ""

    for status_key, value in data.items():

        status, key = _partition_status_key(status_key)
        signature = _convert_signature(value)

        if is_leaf(data.get(key)):

            if f"+ {key}" in data.keys() and f"- {key}" in data.keys() and status == REMOVED:
                output += CHANGED_TEXT.format(
                    key,
                    _convert_signature(data.get(f"- {key}")),
                    _convert_signature(data.get(f"+ {key}")))

            elif f"+ {key}" in data.keys() and f"- {key}" in data.keys() and status == ADDED:
                output += ""

            elif status == ADDED:
                output += ADDED_TEXT.format(key, signature)

            elif status == REMOVED:
                output += REMOVED_TEXT.format(key)

    return output


def present_difference(data: dict, style: str) -> str:
    if style == "stylish":
        return _difference2stylish(data)
    if style == "plain":
        return _difference2plain(data)
    else:
        raise KeyError(f"Don't know style '{style}'")

