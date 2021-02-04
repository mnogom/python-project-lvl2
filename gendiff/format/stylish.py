"""Module to create several representation."""

from gendiff.node_explorer import is_leaf, is_branch
from gendiff.constants import ADDED, REMOVED, CHANGED, UNCHANGED, \
    DICTIONARY


def _convert_value(value):
    """Check json signature of True/False/None"""

    if is_leaf(value):
        return DICTIONARY.get(value, str(value))
    return value


def _get_status(pack):
    """Get status of node."""

    return pack[0] if isinstance(pack, list) else UNCHANGED


def _get_old_value(pack):
    """Get old value of node."""

    return pack[1] if isinstance(pack, list) else pack


def _get_new_value(pack):
    """Get new value of node."""

    return pack[2] if isinstance(pack, list) else pack


def _get_string(indent, status, key, value=None):
    """Make stylish string"""

    if is_leaf(value):
        string = "{}{} {}: {}".format(" " * indent,
                                      status,
                                      key,
                                      _convert_value(value))
        return string.rstrip(" ") + "\n"

    elif is_branch(value):
        string = ""
        string += "{}{} {}: ".format(" " * indent,
                                     status,
                                     key)
        string += _difference2stylish(value, indent + 4)
        return string

    else:
        raise TypeError(f"Value '{value}' is not branch or leaf.")


def _difference2stylish(data: dict, indent=2):

    output = "{\n"

    for key, sub_node in data.items():

        status = _get_status(sub_node)

        if status == CHANGED:
            value = _get_old_value(sub_node)
            output += _get_string(indent, REMOVED, key, value)
            value = _get_new_value(sub_node)
            output += _get_string(indent, ADDED, key, value)
        elif status == ADDED or status == UNCHANGED:
            value = _get_new_value(sub_node)
            output += _get_string(indent, status, key, value)
        elif status == REMOVED:
            value = _get_old_value(sub_node)
            output += _get_string(indent, status, key, value)
        else:
            raise KeyError(f"status: '{status}' is undefined")

    output += " " * (indent - 2) + "}\n"
    return output


def view(data: dict) -> str:
    """Present difference in format."""

    return _difference2stylish(data)[:-1]
