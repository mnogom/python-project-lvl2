"""Module to make stylish representation."""

from gendiff.tree_builder import ADDED, REMOVED, CHANGED, UNCHANGED


ADDED_MARKER = "+"
REMOVED_MARKER = "-"
UNCHANGED_MARKER = " "

PARENT_TEMP = "{indent}{status} {name}: {{\n{children}\n{indent}  }}"
CHILD_TEMP = "{indent}{status} {name}: {value}"


def _value_to_string(value, indent_len=0) -> str:
    """Get converted to string value."""

    if isinstance(value, dict):
        complex_value_string = "{\n"
        for key, value in value.items():
            value_string = _value_to_string(value, indent_len + 4)
            complex_value_string += CHILD_TEMP.format(
                indent=" " * indent_len,
                status=UNCHANGED_MARKER,
                name=key,
                value=value_string) + "\n"
        return complex_value_string + " " * (indent_len - 2) + "}"

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def stylish_view(diff):  # noqa: C901
    """Function to render difference between two files in stylish formatters.

    :param diff: difference between files
    :return: formatted string
    """

    def inner(node, indent_len=0):

        if "children" in node.keys():
            children_string = "\n".join(inner(child, indent_len + 4)
                                        for child in node["children"])
            parent_string = PARENT_TEMP.format(
                indent=" " * indent_len,
                status=UNCHANGED_MARKER,
                name=node["name"],
                children=children_string)
            return parent_string

        if node["status"] == UNCHANGED:
            value = node["new_value"]
            value_string = _value_to_string(value, indent_len + 4)
            child_string = CHILD_TEMP.format(
                indent=" " * indent_len,
                status=UNCHANGED_MARKER,
                name=node["name"],
                value=value_string)
            return child_string

        if node["status"] == ADDED:
            value = node["new_value"]
            value_string = _value_to_string(value, indent_len + 4)
            child_string = CHILD_TEMP.format(
                indent=" " * indent_len,
                status=ADDED_MARKER,
                name=node["name"],
                value=value_string)
            return child_string

        if node["status"] == REMOVED:
            value = node["old_value"]
            value_string = _value_to_string(value, indent_len + 4)
            child_string = CHILD_TEMP.format(
                indent=" " * indent_len,
                status=REMOVED_MARKER,
                name=node["name"],
                value=value_string)
            return child_string

        if node["status"] == CHANGED:
            old_value = node["old_value"]
            new_value = node["new_value"]
            old_value_string = _value_to_string(old_value, indent_len + 4)
            new_value_string = _value_to_string(new_value, indent_len + 4)
            child_string_1 = CHILD_TEMP.format(
                indent=" " * indent_len,
                status=REMOVED_MARKER,
                name=node["name"],
                value=old_value_string)
            child_string_2 = CHILD_TEMP.format(
                indent=" " * indent_len,
                status=ADDED_MARKER,
                name=node["name"],
                value=new_value_string)
            return "{}\n{}".format(child_string_1,
                                   child_string_2)

    stylish_diff = inner(diff)
    return "\n".join(row[2:] for row in stylish_diff[6:].split("\n"))
