"""Module to run tests."""

import os

import pytest

from gendiff import generate_diff

MAIN_PATH = os.path.join("tests", "fixtures")
INPUT_PATH = "input"
OUTPUT_PATH = "output"

PLAIN_STRUCTURE = "plain"
RECURSIVE_STRUCTURE = "recursive"
JSON_FORMAT = "json"
YML_FORMAT = "yml"
PLAIN_FORMATTER = "plain"
JSON_FORMATTER = "json"
STYLISH_FORMATTER = "stylish"
DEFAULT_FORMATTER = None

STYLISH_OUT = "stylish"
PLAIN_OUT = "plain"
JSON_OUT = "json"


def _get_input_data(input_structure, input_format):
    paths = []
    for index in [1, 2]:
        paths.append(
            os.path.join(MAIN_PATH,
                         INPUT_PATH,
                         f"{input_structure}_{input_format}",
                         f"file{index}.{input_format}")
        )
    return paths


def _get_result(input_structure, output_style):
    extension = "json" if output_style == JSON_FORMATTER else "txt"
    path = os.path.join(MAIN_PATH,
                        OUTPUT_PATH,
                        output_style,
                        f"{input_structure}_result.{extension}")
    with open(path, "r") as file:
        return file.read()


@pytest.mark.parametrize("input_structure, input_format, formatter, output_style",
                         [(PLAIN_STRUCTURE, JSON_FORMAT, DEFAULT_FORMATTER, STYLISH_OUT),
                          (PLAIN_STRUCTURE, YML_FORMAT, DEFAULT_FORMATTER, STYLISH_OUT),
                          (RECURSIVE_STRUCTURE, JSON_FORMAT, DEFAULT_FORMATTER, STYLISH_OUT),
                          (RECURSIVE_STRUCTURE, YML_FORMAT, DEFAULT_FORMATTER, STYLISH_OUT),
                          (PLAIN_STRUCTURE, JSON_FORMAT, STYLISH_FORMATTER, STYLISH_OUT),
                          (PLAIN_STRUCTURE, YML_FORMAT, STYLISH_FORMATTER, STYLISH_OUT),
                          (RECURSIVE_STRUCTURE, JSON_FORMAT, STYLISH_FORMATTER, STYLISH_OUT),
                          (RECURSIVE_STRUCTURE, YML_FORMAT, STYLISH_FORMATTER, STYLISH_OUT),
                          (PLAIN_STRUCTURE, JSON_FORMAT, PLAIN_FORMATTER, PLAIN_OUT),
                          (PLAIN_STRUCTURE, YML_FORMAT, PLAIN_FORMATTER, PLAIN_OUT),
                          (RECURSIVE_STRUCTURE, JSON_FORMAT, PLAIN_FORMATTER, PLAIN_OUT),
                          (RECURSIVE_STRUCTURE, YML_FORMAT, PLAIN_FORMATTER, PLAIN_OUT),
                          (PLAIN_STRUCTURE, JSON_FORMAT, JSON_FORMATTER, JSON_OUT),
                          (PLAIN_STRUCTURE, YML_FORMAT, JSON_FORMATTER, JSON_OUT),
                          (RECURSIVE_STRUCTURE, JSON_FORMAT, JSON_FORMATTER, JSON_OUT),
                          (RECURSIVE_STRUCTURE, YML_FORMAT, JSON_FORMATTER, JSON_OUT)])
def test_diff(input_structure, input_format, formatter, output_style):
    file1, file2 = _get_input_data(input_structure, input_format)
    result = _get_result(input_structure, output_style)

    if formatter == DEFAULT_FORMATTER:
        assert generate_diff(file1, file2) == result
    else:
        assert generate_diff(file1, file2, formatter) == result
