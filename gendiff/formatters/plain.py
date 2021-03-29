"""Plain formatter."""

from gendiff.tree_builder import ADDED, REMOVED, CHANGED, UNCHANGED


ROW_TEMP = "Property '{path}' was {action}\n"


def _stringify(value):
    """Convert value to string."""

    if isinstance(value, dict):
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

    def inner(data, parent_name):

        if "children" in data.keys():
            return "".join(
                inner(child, parent_name + "." + child["name"])
                for child in data["children"]
            )
        status = data["status"]
        old_value = _stringify(data["old_value"])
        new_value = _stringify(data["new_value"])

        if status == ADDED:
            action_string = "added with value: {value}".format(value=new_value)
            return ROW_TEMP.format(path=parent_name,
                                   action=action_string)
        if status == REMOVED:
            action_string = "removed"
            return ROW_TEMP.format(path=parent_name,
                                   action=action_string)
        if status == CHANGED:
            action_string = ("updated. From {old_value}"
                             " to {new_value}").format(old_value=old_value,
                                                       new_value=new_value)
            return ROW_TEMP.format(path=parent_name,
                                   action=action_string)

        if status == UNCHANGED:
            return ""

    plain_diff = inner(diff, parent_name=diff["name"])[:-1]
    return "\n".join([row.replace("Property 'root.", "Property '")
                      for row in plain_diff.split("\n")])
