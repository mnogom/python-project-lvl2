"""Module to find difference between two input trees."""


ADDED = "ADDED"
REMOVED = "REMOVED"
UNCHANGED = "UNCHANGED"
CHANGED = "CHANGED"


def _check_status(node1, node2, key) -> str:
    """Compare sub nodes taken from nodes by key.

    :param node1: node to compare #1
    :param node2: node to compare #2
    :param key: key to get sub node
    :return: status
    """

    if key in node1.keys() and key in node2.keys():
        sub_node1 = node1.get(key)
        sub_node2 = node2.get(key)
        if (isinstance(sub_node1, dict) and isinstance(sub_node2, dict)) or \
                (sub_node1 == sub_node2):
            return UNCHANGED
        return CHANGED
    if key in node1.keys():
        return REMOVED
    if key in node2.keys():
        return ADDED
    raise KeyError(f"Can't understand difference between"
                   f"node1: '{node1}' and node2: '{node2}'")


def get_diff_tree(data1: dict, data2: dict) -> dict:
    """Find difference between two nodes. Works
    with branches (recursive) and for leaves (plain).

    :param data1: node #1
    :param data2: node #2
    :return: difference between two nodes
    """

    def inner(parent_key, node1, node2, status) -> dict:

        if isinstance(node1, dict) and isinstance(node2, dict):
            key_bag = sorted(list({*node1.keys(), *node2.keys()}))

            return {
                "name": parent_key,
                "status": status,
                "children": [
                    inner(key,
                          node1.get(key),
                          node2.get(key),
                          _check_status(node1, node2, key))
                    for key in key_bag
                ]
            }

        return {
            "name": parent_key,
            "status": status,
            "old_value": node1,
            "new_value": node2
        }

    root_name = "root"
    root_status = UNCHANGED
    return inner(root_name, data1, data2, root_status)
