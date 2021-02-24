"""Module contains main functions to get difference between two files."""

from os.path import splitext

from gendiff.format_picker import get_formatted_diff
from gendiff.file_parser import parse_file
from gendiff.tree_builder import get_diff_tree


def _get_extension(file_path: str) -> str:
    return splitext(file_path)[-1].lower()


def _read_file(file_path: str) -> (bytes, str):
    extension = _get_extension(file_path)
    with open(file_path, "rb") as file:
        return file.read(), extension


def generate_diff(file_path1: str, file_path2: str, formatter="stylish"):
    """Get difference between two json files and returns formatted string.

    :param formatter: ['stylish' | 'plain' | 'json']
    :param file_path1: json file #1
    :param file_path2: json file #2
    :return: string with difference
    """

    file1, extension1 = _read_file(file_path1)
    file2, extension2 = _read_file(file_path2)
    data1 = parse_file(file1, extension1)
    data2 = parse_file(file2, extension2)
    diff = get_diff_tree(data1, data2)
    formatted_diff = get_formatted_diff(diff, formatter)
    return formatted_diff
