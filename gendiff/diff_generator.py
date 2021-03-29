"""Diff generator."""

from os.path import splitext

from gendiff.format_picker import render_diff
from gendiff.file_parser import parse
from gendiff.tree_builder import build_tree


def _read_file(file_path: str) -> (bytes, str):
    extension = splitext(file_path)[-1].lower()
    with open(file_path, "rb") as file:
        return file.read(), extension


def generate_diff(file_path1: str, file_path2: str, format="stylish"):
    """Get difference between two files (JSON or YAML) and returns
    stylised difference.

    :param format: ['stylish' | 'plain' | 'json']
    :param file_path1: file #1
    :param file_path2: file #2
    :return: stylised difference
    """

    file1, extension1 = _read_file(file_path1)
    file2, extension2 = _read_file(file_path2)
    data1 = parse(file1, extension1)
    data2 = parse(file2, extension2)
    diff = build_tree(data1, data2)
    formatted_diff = render_diff(diff, format)
    return formatted_diff
