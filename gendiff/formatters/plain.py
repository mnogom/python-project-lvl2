"""Module to make plain representation."""

from gendiff.tree_builder import ADDED, REMOVED, CHANGED, UNCHANGED


ROW_TEMP = "Property '{path}' was {action}\n"
ADDED_TEMP = "added with value: {value}"
REMOVED_TEMP = "removed"
CHANGED_TEMP = "updated. From {old_value} to {new_value}"
NESTED_TEMP = "[complex value]"


def _value_to_string(value):
    """Get converted to string value."""

    if isinstance(value, dict):
        return NESTED_TEMP

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain_view(diff):  # noqa: C901
    """Function to render difference between two files in plain formatters.

    :param diff: difference between files
    :return: formatted string
    """

    def inner(data, parent_name):

        if "children" in data.keys():
            return "".join(
                inner(child, parent_name + "." + child["name"])
                for child in data["children"]
            )
        status = data["status"]
        old_value = _value_to_string(data["old_value"])
        new_value = _value_to_string(data["new_value"])

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

        if status == UNCHANGED:
            return ""

    plain_diff = inner(diff, parent_name=diff["name"])[:-1]
    return "\n".join([row.replace("Property 'root.", "Property '")
                      for row in plain_diff.split("\n")])
