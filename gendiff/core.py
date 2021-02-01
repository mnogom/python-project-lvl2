"""Module contains main functions to get difference between two files."""

import json
import yaml

from gendiff.view import dict2str
from gendiff.node_explorer import is_leaf, is_branch, have_key

ADDED = "+"
REMOVED = "-"
UNCHANGED = " "
KEY_TEMP = "{} {}"


def _read_file(file_path: str) -> dict:
    """Read json or yaml file and returns dictionary.

    :param file_path: *.json/*.yaml file path
    :return: dictionary from json file
    """

    with open(file_path, "rb") as file:
        if file_path.lower().endswith(".json"):
            return json.load(file)

        elif file_path.lower().endswith(".yaml"):
            return yaml.load(file, Loader=yaml.SafeLoader)

        else:
            raise TypeError((f"Don't know what to do with "
                             f"'*.{file_path.split('.')[-1]}' file"))


def _find_diff(key, node1, node2):
    """Find difference between two nodes."""

    if not have_key(key, node1):
        new_key = KEY_TEMP.format(ADDED, key)
        new_value = node2.get(key)
        return {new_key: new_value}

    if not have_key(key, node2):
        new_key = KEY_TEMP.format(REMOVED, key)
        new_value = node1.get(key)
        return {new_key: new_value}

    if node1.get(key) == node2.get(key):
        new_key = KEY_TEMP.format(UNCHANGED, key)
        new_value = node1.get(key)
        return {new_key: new_value}

    if is_leaf(node1.get(key)) or is_leaf(node2.get(key)):
        new_key1 = KEY_TEMP.format(REMOVED, key)
        new_key2 = KEY_TEMP.format(ADDED, key)
        new_value1 = node1.get(key)
        new_value2 = node2.get(key)
        return {new_key1: new_value1,
                new_key2: new_value2}

    new_key = KEY_TEMP.format(UNCHANGED, key)
    return {new_key: _check_diff(node1.get(key), node2.get(key))}


def _check_diff(data1: dict, data2: dict) -> dict:
    difference = {}

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    keys_bag = sorted(list(keys1.union(keys2)))

    for key in keys_bag:

        sub_node1 = data1.get(key)
        sub_node2 = data2.get(key)

        if is_leaf(data1.get(key)) or is_leaf(data2.get(key)):
            difference.update(
                _find_diff(key, data1, data2))

        elif is_branch(sub_node1) and is_branch(sub_node2):
            difference.update(
                _find_diff(key, data1, data2)
            )

    return difference


def generate_diff(file_path1: str, file_path2: str):
    """Get difference between two json files.
    '+' - key, value added
    '-' - key, value removed
    '- ... / + ...' - value updated for key

    :param file_path1: json file #1
    :param file_path2: json file #2
    :return: string with difference
    """

    data1 = _read_file(file_path1)
    data2 = _read_file(file_path2)
    difference = _check_diff(data1, data2)

    print(dict2str(difference, UNCHANGED))
    return dict2str(difference, UNCHANGED)
