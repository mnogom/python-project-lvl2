"""Module has base functions to parse difference."""


def _is_parsed_data(data) -> bool:
    """Predicate to check does 'core' find difference for current node."""

    return isinstance(data, list)


def unpack_node(data: list) -> dict:
    """Get node from data. If data is list - returns
    first (the only one) element (node)."""

    if _is_parsed_data(data):
        return data[0]
    raise KeyError(f"data '{data}' hasn't node.")


def is_parsed_parent(data: list) -> bool:
    """Predicate to check if data was parsed and
    has children."""

    if _is_parsed_data(data):
        node = unpack_node(data)
        if "children" in node.keys():
            return True
    return False


def is_parsed_child(data: list) -> bool:
    """Predicate to check if data was parsed and
    is children."""

    if _is_parsed_data(data):
        node = unpack_node(data)
        if "children" not in node.keys():
            return True
    return False


def get_name(data: list) -> str:
    """Get name of node from data."""

    node = unpack_node(data)
    return node["name"]


def get_old_value(data: list) -> str:
    """Get old value of node from data."""

    node = unpack_node(data)
    if is_parsed_child(data):
        return node["old_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_new_value(data: list) -> str:
    """Get new value of node from data."""

    node = unpack_node(data)
    if is_parsed_child(data):
        return node["new_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_status(data: list) -> str:
    """Get status of node from data."""

    node = unpack_node(data)
    return node["status"]


def get_children(data: list) -> list:
    """Get children of node from data."""

    node = unpack_node(data)
    if is_parsed_parent(data):
        return node["children"]
    raise KeyError(f"node '{node}' doesn't have any child.")


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
