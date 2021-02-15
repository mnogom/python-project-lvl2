"""Module to make stylish representation."""

from gendiff.gardener_tools import is_leaf, is_branch
from gendiff.constants import ADDED, REMOVED, CHANGED, UNCHANGED
from gendiff.formatters.diff_explorer import get_name, get_status, \
    get_new_value, get_old_value, get_children, \
    is_parsed_child, is_parsed_parent, convert_value

PARENT_TEMP = "{indent}{status} {name}: {{\n{children}\n{indent}  }}"
CHILD_TEMP = "{indent}{status} {name}: {value}"


def _remove_root(string: str) -> str:
    return "\n".join(row[2:] for row in string[6:].split("\n"))


def stylish_view(diff):  # noqa: C901
    """Function to render difference between two files in stylish formatters.

    :param diff: difference between files
    :return: formatted string
    """

    # TODO: Make function more simple [?-1]
    def inner(data, indent_len):

        if is_parsed_parent(data):
            children_string = "\n".join(inner(child, indent_len + 4)
                                        for child in get_children(data))
            parent_string = PARENT_TEMP.format(indent=" " * indent_len,
                                               status=get_status(data),
                                               name=get_name(data),
                                               children=children_string)
            return parent_string

        if is_parsed_child(data):
            status = get_status(data)
            if status == ADDED or status == UNCHANGED:
                value = get_new_value(data)
                value_string = inner(value, indent_len + 4)
                child_string = CHILD_TEMP.format(indent=" " * indent_len,
                                                 status=get_status(data),
                                                 name=get_name(data),
                                                 value=value_string)
                return child_string
            if status == REMOVED:
                value = get_old_value(data)
                value_string = inner(value, indent_len + 4)
                child_string = CHILD_TEMP.format(indent=" " * indent_len,
                                                 status=get_status(data),
                                                 name=get_name(data),
                                                 value=value_string)
                return child_string
            if status == CHANGED:
                old_value = get_old_value(data)
                new_value = get_new_value(data)
                old_value_string = inner(old_value, indent_len + 4)
                new_value_string = inner(new_value, indent_len + 4)
                child_string_1 = CHILD_TEMP.format(indent=" " * indent_len,
                                                   status=REMOVED,
                                                   name=get_name(data),
                                                   value=old_value_string)
                child_string_2 = CHILD_TEMP.format(indent=" " * indent_len,
                                                   status=ADDED,
                                                   name=get_name(data),
                                                   value=new_value_string)
                return "{}\n{}".format(child_string_1,
                                       child_string_2)

            raise KeyError(f"data '{data}' is parsed child but don't"
                           f"understand how to work with it")

        if is_leaf(data):
            value_string = convert_value(data)
            return value_string

        if is_branch(data):
            values_string = "{\n"
            for key, value in data.items():
                value_string = inner(value, indent_len + 4)
                values_string += CHILD_TEMP.format(indent=" " * indent_len,
                                                   status=UNCHANGED,
                                                   name=key,
                                                   value=value_string) + "\n"
            values_string += " " * (indent_len - 2) + "}"
            return values_string

        raise KeyError(f"data '{data}' is not parsed or leaf or branch.")

    return _remove_root(inner(diff, indent_len=0))
