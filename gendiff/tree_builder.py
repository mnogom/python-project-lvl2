"""Module to find difference between two input trees."""


ADDED = "ADDED"
REMOVED = "REMOVED"
UNCHANGED = "UNCHANGED"
CHANGED = "CHANGED"


def get_diff_tree(data1: dict, data2: dict) -> dict:  # noqa: C901
    """Find difference between two nodes. Works
    with branches (recursive) and for leaves (plain).

    :param data1: node #1
    :param data2: node #2
    :return: difference between two nodes
    """

    def inner(key, node1, node2, parent_node1=None, parent_node2=None) -> dict:

        if isinstance(node1, dict) and isinstance(node2, dict):
            key_bag = sorted(list({*node1.keys(), *node2.keys()}))

            return {
                "name": key,
                "status": UNCHANGED,
                "children": [
                    inner(key,
                          node1.get(key),
                          node2.get(key),
                          node1,
                          node2)
                    for key in key_bag
                ]
            }

        if key not in parent_node1.keys():
            return {
                "name": key,
                "status": ADDED,
                "old_value": node1,
                "new_value": node2
            }

        if key not in parent_node2.keys():
            return {
                "name": key,
                "status": REMOVED,
                "old_value": node1,
                "new_value": node2
            }

        if parent_node1.get(key) == parent_node2.get(key):
            return {
                "name": key,
                "status": UNCHANGED,
                "old_value": node1,
                "new_value": node2
            }

        if parent_node1.get(key) != parent_node2.get(key):
            return {
                "name": key,
                "status": CHANGED,
                "old_value": node1,
                "new_value": node2
            }

    root_name = "root"
    return inner(root_name, data1, data2)
