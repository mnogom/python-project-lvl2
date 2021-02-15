"""Module contains main functions to get difference between two files."""

from gendiff.formatters import get_formatted_diff
from gendiff.file_parser import parse_file
from gendiff.gardener import find_diff


def generate_diff(file_path1: str, file_path2: str, formatter="stylish"):
    """Get difference between two json files and returns formatted string.

    :param formatter: ['stylish' | 'plain' | 'json']
    :param file_path1: json file #1
    :param file_path2: json file #2
    :return: string with difference
    """

    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = find_diff(data1, data2)
    formatted_diff = get_formatted_diff(diff, formatter)
    return formatted_diff
