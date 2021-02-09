"""Module contains main functions to get difference between two files."""

import json
import yaml

from gendiff.node_explorer import is_branch, has_key
from gendiff.constants import ADDED, REMOVED, UNCHANGED, CHANGED

from pprint import pprint


def _read_file(file_path: str) -> dict:
    """Read json or yaml file and returns dictionary.

    :param file_path: *.json/*.yaml file path
    :return: dictionary from json file
    """

    with open(file_path, "rb") as file:
        if file_path.lower().endswith(".json"):
            return json.load(file)

        if file_path.lower().endswith(".yaml"):
            return yaml.load(file, Loader=yaml.SafeLoader)

        raise TypeError((f"Don't know what to do with "
                         f"'{file_path.split('.')[-1]}' file"))


# def _check_diff(key, node1, node2):
#     """Find difference between two nodes."""
#
#     old_value = node1.get(key)
#     new_value = node2.get(key)
#
#     if is_branch(old_value) and is_branch(new_value):
#         status = UNCHANGED
#         return {key: [status, {}, _check_diff(old_value, new_value)]}
#
#     if not have_key(key, node1):
#         old_value = None if is_leaf(new_value) else {}
#         status = ADDED
#
#     elif not have_key(key, node2):
#         new_value = None if is_leaf(old_value) else {}
#         status = REMOVED
#
#     elif node1.get(key) == node2.get(key):
#         old_value = None
#         status = UNCHANGED
#
#     elif is_leaf(node1.get(key)) or is_leaf(node2.get(key)):
#         status = CHANGED
#
#     else:
#         raise SystemError((f"Don't understand key: {key}, "
#                            f"node1: {node1}, node2: {node2}"))
#
#     return {key: [status, old_value, new_value]}


# def _find_diff(node1: dict, node2: dict) -> dict:
#     difference = {}
#
#     keys1 = set(node1.keys())
#     keys2 = set(node2.keys())
#     keys_bag = sorted(list(keys1.union(keys2)))
#
#     for key in keys_bag:
#         difference.update(
#             _check_diff(key, node1, node2))
#
#     return difference


def _check_status(node1, node2, key):
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


def _find_diff(data1, data2):

    def inner(parent_key, node1, node2, status) -> list:

        if is_branch(node1) and is_branch(node2):
            keys1 = set(node1.keys())
            keys2 = set(node2.keys())
            key_bag = sorted(list(keys1.union(keys2)))

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

    return inner("root", data1, data2, UNCHANGED)


def generate_diff(file_path1: str, file_path2: str, style="stylish"):
    """Get difference between two json files.
    '+' - key, value added
    '-' - key, value removed
    '- ... / + ...' - value updated for key

    :param style:
    :param file_path1: json file #1
    :param file_path2: json file #2
    :return: string with difference
    """

    data1 = _read_file(file_path1)
    data2 = _read_file(file_path2)
    diff = _find_diff(data1, data2)

    return diff


if __name__ == '__main__':
    difference = generate_diff("tests/fixtures/recursive_json/file1.json",
                               "tests/fixtures/recursive_json/file2.json")
    pprint(difference)
    print("-" * 30)
    difference = generate_diff("tests/fixtures/plain_json/file1.json",
                               "tests/fixtures/plain_json/file2.json",)
    pprint(difference)
    print("-" * 30)
    print(f"count: {len(difference)}")
