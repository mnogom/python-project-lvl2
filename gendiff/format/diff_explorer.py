"""Module has base functions to parse difference."""

from gendiff.constants import PYTH2JSON


def convert_value(value):
    """Convert value to JSON signature. Working for
    1. False -> false; 2. True -> true; 3. None -> null."""

    return PYTH2JSON.get(value, str(value))


def get_name(data) -> str:
    """Get name of node

    :param data: node
    :return:
    """

    node = get_node(data)
    return node["name"]


def get_old_value(data) -> str:
    """Get old value of node.

    :param data: node
    :return: old value in Python or JSON format
    """

    node = get_node(data)
    if is_parsed_child(data):
        return node["old_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_new_value(data) -> str:
    """Get new value of node.

    :param data: node
    :return: new value in Python or JSON format
    """

    node = get_node(data)
    if is_parsed_child(data):
        return node["new_value"]
    raise KeyError(f"node '{node}' is Parent. So it hasn't any values.")


def get_status(data: list) -> str:
    """Get status of node.

    :param data: node
    :return: status of changes for node
    """

    node = get_node(data)
    return node["status"]


def get_children(data) -> list:
    """Get children of node.

    :param data: parent node
    :return: list of children
    """

    node = get_node(data)
    try:
        return node["children"]
    except KeyError:
        raise KeyError(f"node '{node}' doesn't have any child.")


def _is_parsed_data(data) -> bool:
    """Predicate to check does 'core' find difference for current node."""

    return isinstance(data, list)


def get_node(data: list) -> dict:
    if _is_parsed_data(data):
        return data[0]
    raise KeyError(f"data '{data}' hasn't node.")


def is_parsed_parent(data):
    if _is_parsed_data(data):
        node = get_node(data)
        if "children" in node.keys():
            return True
    return False


def is_parsed_child(data):
    if _is_parsed_data(data):
        node = get_node(data)
        if "children" not in node.keys():
            return True
    return False
