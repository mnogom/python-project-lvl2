"""Module contains main functions to get difference between two files."""

import json
import yaml

from gendiff.node_explorer import is_leaf, is_branch, have_key
from gendiff.constants import ADDED, REMOVED, UNCHANGED, CHANGED


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

    old_value = node1.get(key)
    new_value = node2.get(key)

    if is_branch(old_value) and is_branch(new_value):
        status = UNCHANGED
        return {key: [status, {}, _check_diff(old_value, new_value)]}

    if not have_key(key, node1):
        old_value = None if is_leaf(new_value) else {}
        status = ADDED

    elif not have_key(key, node2):
        new_value = None if is_leaf(old_value) else {}
        status = REMOVED

    elif node1.get(key) == node2.get(key):
        old_value = None
        status = UNCHANGED

    elif is_leaf(node1.get(key)) or is_leaf(node2.get(key)):
        status = CHANGED

    else:
        raise SystemError((f"Don't understand key: {key}, "
                           f"node1: {node1}, node2: {node2}"))

    return {key: [status, old_value, new_value]}


def _check_diff(data1: dict, data2: dict) -> dict:
    difference = {}

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    keys_bag = sorted(list(keys1.union(keys2)))

    for key in keys_bag:
        difference.update(
            _find_diff(key, data1, data2))

    return difference


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
    difference = _check_diff(data1, data2)

    return difference
