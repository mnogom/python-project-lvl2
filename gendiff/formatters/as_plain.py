"""Module to make plain representation."""

from gendiff.constants import ADDED, REMOVED, CHANGED
from gendiff.gardener_tools import is_branch
from gendiff.formatters.diff_explorer import get_name, get_status, \
    get_new_value, get_old_value, get_children, \
    is_parsed_child, is_parsed_parent, convert_value

ROW_TEMP = "Property '{path}' was {action}\n"
ADDED_TEMP = "added with value: {value}"
REMOVED_TEMP = "removed"
CHANGED_TEMP = "updated. From {old_value} to {new_value}"
BRANCH_TEMP = "[complex value]"


def _remove_root(string: str) -> str:
    """Remove root key from input string."""

    return "\n".join([row.replace("Property 'root.",
                                  "Property '") for row in string.split("\n")])


def _setup_value(value):
    """Replace value with 'BRANCH_TEMP' if value is branch."""
    return BRANCH_TEMP if is_branch(value) \
        else convert_value(value, strong=True)


def plain_view(diff):  # noqa: C901
    """Function to render difference between two files in plain formatters.

    :param diff: difference between files
    :return: formatted string
    """

    # TODO: Make function more simple [?-2]
    def inner(data, parent_name):

        if is_parsed_parent(data):
            return "".join(
                inner(child, parent_name + "." + get_name(child))
                for child in get_children(data)
            )

        if is_parsed_child(data):

            status = get_status(data)
            old_value = _setup_value(get_old_value(data))
            new_value = _setup_value(get_new_value(data))

            if status == ADDED:
                action_string = ADDED_TEMP.format(value=new_value)
                return ROW_TEMP.format(path=parent_name,
                                       action=action_string)
            if status == REMOVED:
                action_string = REMOVED_TEMP
                return ROW_TEMP.format(path=parent_name,
                                       action=action_string)
            if status == CHANGED:
                action_string = CHANGED_TEMP.format(old_value=old_value,
                                                    new_value=new_value)
                return ROW_TEMP.format(path=parent_name,
                                       action=action_string)

        return ""

    return _remove_root(inner(diff, parent_name=get_name(diff))[:-1])