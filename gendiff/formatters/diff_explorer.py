"""Module has base functions to parse difference."""


def is_parent(node: dict) -> bool:
    """Predicate to check if node."""

    return "children" in node.keys()


def is_child(node: dict) -> bool:
    """Predicate to check node is child."""

    return not is_parent(node)


def get_name(node: dict) -> str:
    """Get name of node."""

    return node["name"]


def get_old_value(node: dict) -> str:
    """Get old value of node."""

    if is_child(node):
        return node["old_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_new_value(node: dict) -> str:
    """Get new value of node."""

    if is_child(node):
        return node["new_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_status(node: dict) -> str:
    """Get status of node."""

    return node["status"]


def get_children(node: dict) -> list:
    """Get children of node."""

    if is_parent(node):
        return node["children"]
    raise KeyError(f"node '{node}' doesn't have any child.")


def is_complex_value(value) -> bool:
    """Check if value is complex object."""

    return isinstance(value, dict)


def convert_value(value, strong=False) -> str:
    """Convert value to JSON signature.
    With 'strong=True' all strings will be print with (')."""

    python2json = {True: "true",
                   False: "false",
                   None: "null"}

    if isinstance(value, bool) or value is None:
        return python2json[value]
    if isinstance(value, str) and strong:
        return f"'{value}'"
    return f"{value}"
