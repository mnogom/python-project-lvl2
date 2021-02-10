"""Module has base functions to parse difference. Difference is structure
of data (list) if core found difference in input dictionaries and another
type if there are no difference."""

from gendiff.constants import PYTH2JSON


def _is_parsed_data(data) -> bool:
    """Predicate to check does 'core' find difference for current node."""

    return isinstance(data, list)


def get_node(data: list) -> dict:
    """Get node from data. If data is list - returns
    first (the only one) element (node)."""

    if _is_parsed_data(data):
        return data[0]
    raise KeyError(f"data '{data}' hasn't node.")


def is_parsed_parent(data):
    """Predicate to check if data was parsed and
    has children."""

    if _is_parsed_data(data):
        node = get_node(data)
        if "children" in node.keys():
            return True
    return False


def is_parsed_child(data):
    """Predicate to check if data was parsed and
    is children."""

    if _is_parsed_data(data):
        node = get_node(data)
        if "children" not in node.keys():
            return True
    return False


def get_name(data) -> str:
    """Get name of node from data."""

    node = get_node(data)
    return node["name"]


def get_old_value(data) -> str:
    """Get old value of node from data."""

    node = get_node(data)
    if is_parsed_child(data):
        return node["old_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_new_value(data) -> str:
    """Get new value of node from data."""

    node = get_node(data)
    if is_parsed_child(data):
        return node["new_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_status(data: list) -> str:
    """Get status of node from data."""

    node = get_node(data)
    return node["status"]


def get_children(data) -> list:
    """Get children of node from data."""

    node = get_node(data)
    if is_parsed_parent(data):
        return node["children"]
    raise KeyError(f"node '{node}' doesn't have any child.")


def convert_value(value, strong=False):
    """Convert value to JSON signature. So:
    1. False -> false; 2. True -> true; 3. None -> null.
    With 'strong=True' all strings will be print with (')"""

    if isinstance(value, bool) or value is None:
        return PYTH2JSON[value]
    if isinstance(value, str) and strong:
        return f"'{value}'"
    return f"{value}"
