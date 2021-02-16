"""Module has base functions to parse difference."""


def is_parent(node: dict) -> bool:
    """Predicate to check if data was parsed and
    has children."""

    return "children" in node.keys()


def is_child(node: dict) -> bool:
    """Predicate to check if data was parsed and
    is children."""

    return not is_parent(node)


def get_name(node: dict) -> str:
    """Get name of node from data."""

    return node["name"]


def get_old_value(node: dict) -> str:
    """Get old value of node from data."""

    if is_child(node):
        return node["old_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_new_value(node: dict) -> str:
    """Get new value of node from data."""

    if is_child(node):
        return node["new_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_status(node: dict) -> str:
    """Get status of node from data."""

    return node["status"]


def get_children(node: dict) -> list:
    """Get children of node from data."""

    if is_parent(node):
        return node["children"]
    raise KeyError(f"node '{node}' doesn't have any child.")


def is_nested_value(value) -> bool:
    """Check if value is nested object"""

    return isinstance(value, dict)


def convert_value(value, strong=False) -> str:
    """Convert value to JSON signature.
    With 'strong=True' all strings will be print with (')"""

    pyth2json = {True: "true",
                 False: "false",
                 None: "null"}

    if isinstance(value, bool) or value is None:
        return pyth2json[value]
    if isinstance(value, str) and strong:
        return f"'{value}'"
    return f"{value}"
