"""Module to make stylish representation."""

from gendiff.gardener_tools import is_leaf, is_branch
from gendiff.gardener import ADDED, REMOVED, CHANGED, UNCHANGED
from gendiff.formatters.diff_explorer import get_name, get_status, \
    get_new_value, get_old_value, get_children, \
    is_child, is_parent, convert_value, is_nested_value

PARENT_TEMP = "{indent}{status} {name}: {{\n{children}\n{indent}  }}"
CHILD_TEMP = "{indent}{status} {name}: {value}"


def _remove_root(string: str) -> str:
    return "\n".join(row[2:] for row in string[6:].split("\n"))


def _setup_value(value, indent_len=0) -> str:
    if is_nested_value(value):
        nested_value_string = "{\n"
        for key, value in value.items():
            value_string = _setup_value(value, indent_len + 4)
            nested_value_string += CHILD_TEMP.format(indent=" " * indent_len,
                                                     status=UNCHANGED,
                                                     name=key,
                                                     value=value_string) + "\n"
        return nested_value_string + " " * (indent_len - 2) + "}"
    return convert_value(value)


def stylish_view(diff):  # noqa: C901
    """Function to render difference between two files in stylish formatters.

    :param diff: difference between files
    :return: formatted string
    """

    def inner(node, indent_len):

        if is_parent(node):
            children_string = "\n".join(inner(child, indent_len + 4)
                                        for child in get_children(node))
            parent_string = PARENT_TEMP.format(indent=" " * indent_len,
                                               status=get_status(node),
                                               name=get_name(node),
                                               children=children_string)
            return parent_string

        if is_child(node):
            status = get_status(node)
            if status == ADDED or status == UNCHANGED:
                value = get_new_value(node)
                value_string = _setup_value(value, indent_len + 4)
                child_string = CHILD_TEMP.format(indent=" " * indent_len,
                                                 status=get_status(node),
                                                 name=get_name(node),
                                                 value=value_string)
                return child_string
            if status == REMOVED:
                value = get_old_value(node)
                value_string = _setup_value(value, indent_len + 4)
                child_string = CHILD_TEMP.format(indent=" " * indent_len,
                                                 status=get_status(node),
                                                 name=get_name(node),
                                                 value=value_string)
                return child_string
            if status == CHANGED:
                old_value = get_old_value(node)
                new_value = get_new_value(node)
                old_value_string = _setup_value(old_value, indent_len + 4)
                new_value_string = _setup_value(new_value, indent_len + 4)
                child_string_1 = CHILD_TEMP.format(indent=" " * indent_len,
                                                   status=REMOVED,
                                                   name=get_name(node),
                                                   value=old_value_string)
                child_string_2 = CHILD_TEMP.format(indent=" " * indent_len,
                                                   status=ADDED,
                                                   name=get_name(node),
                                                   value=new_value_string)
                return "{}\n{}".format(child_string_1,
                                       child_string_2)

            raise KeyError(f"node '{node}' is parsed child but don't"
                           f"understand how to work with it")

        raise KeyError(f"node '{node}' is not parsed or leaf or branch.")

    return _remove_root(inner(diff, indent_len=0))
