"""Module to find difference between two input trees. Difference is structure of
data (list) if core found difference. Data can be parent (has key 'children') or
child (has keys 'old_value' and 'new_value'). Values (old and new) can be leaf
(value) or branch (dict)."""

from gendiff.gardener_tools import is_branch, has_key


ADDED = "+"
REMOVED = "-"
UNCHANGED = " "
CHANGED = "~"


def _get_keys_bag(branch1, branch2):
    return sorted(list({*branch1.keys(), *branch2.keys()}))


def _check_status(node1, node2, key) -> str:
    """Compare sub nodes taken from nodes by key.

    :param node1: node to compare #1
    :param node2: node to compare #2
    :param key: key to get sub node
    :return: status
    """

    if has_key(key, node1) and has_key(key, node2):
        if is_branch(node1.get(key)) and is_branch(node2.get(key)):
            return UNCHANGED
        if node1.get(key) == node2.get(key):
            return UNCHANGED
        return CHANGED
    if has_key(key, node1):
        return REMOVED
    if has_key(key, node2):
        return ADDED
    raise KeyError(f"Can't understand difference between"
                   f"node1: '{node1}' and node2: '{node2}'")


def grow_diff_tree(data1: dict, data2: dict) -> list:
    """Find difference between two nodes. Works
    with branches (recursive) and for leaves (plain)

    :param data1: node #1
    :param data2: node #2
    :return: difference between two nodes
    """

    def inner(parent_key, node1, node2, status) -> list:

        if is_branch(node1) and is_branch(node2):
            key_bag = _get_keys_bag(node1, node2)

            return [{
                "name": parent_key,
                "status": status,
                "children": [
                    inner(key,
                          node1.get(key),
                          node2.get(key),
                          _check_status(node1, node2, key))
                    for key in key_bag
                ]
            }]

        return [{
            "name": parent_key,
            "status": status,
            "old_value": node1,
            "new_value": node2
        }]

    root_name = "root"
    root_status = UNCHANGED
    return inner(root_name, data1, data2, root_status)
