"""Plain formatter."""

from gendiff.tree_builder import ADDED, REMOVED, CHANGED, UNCHANGED, NESTED


ROW_TEMP = "Property '{path}' was {action}\n"


def _stringify(value):
    """Convert value to string."""

    if isinstance(value, dict) or \
            isinstance(value, tuple) or \
            isinstance(value, list) or \
            isinstance(value, set):
        return "[complex value]"

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return value


def plain_render(diff):  # noqa: C901
    """Function to render diff in plain format.

    :param diff: difference between files
    :return: formatted string
    """

    def inner(node, parent_name):

        if node["status"] == NESTED:
            return "".join(
                inner(child, parent_name + "." + child["name"])
                for child in node["children"]
            )

        old_value = _stringify(node["old_value"])
        new_value = _stringify(node["new_value"])

        if node["status"] == ADDED:
            action_string = "added with value: {value}".format(value=new_value)
            return ROW_TEMP.format(path=parent_name,
                                   action=action_string)
        if node["status"] == REMOVED:
            action_string = "removed"
            return ROW_TEMP.format(path=parent_name,
                                   action=action_string)
        if node["status"] == CHANGED:
            action_string = ("updated. From {old_value}"
                             " to {new_value}").format(old_value=old_value,
                                                       new_value=new_value)
            return ROW_TEMP.format(path=parent_name,
                                   action=action_string)

        if node["status"] == UNCHANGED:
            return ""

    plain_diff = inner(diff, parent_name=diff["name"])[:-1]
    return "\n".join([row.replace("Property 'root.", "Property '")
                      for row in plain_diff.split("\n")])
