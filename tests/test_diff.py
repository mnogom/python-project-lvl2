"""Module to run tests."""

import os
import json

import pytest

from gendiff import generate_diff

MAIN_PATH = os.path.join("tests", "fixtures")
INPUT_PATH = "input"
OUTPUT_PATH = "output"

PLAIN = "plain"
RECURSIVE = "recursive"
JSON = "json"
YML = "yml"
STYLISH = "stylish"


def _get_input_data(input_structure, input_format):
    paths = [os.path.join(MAIN_PATH,
                          INPUT_PATH,
                          f"{input_structure}_{input_format}",
                          f"file{index}.{input_format}")
             for index in [1, 2]]
    return paths


def _get_result(input_structure, output_style):
    extension = ".json" if output_style == JSON else ".txt"
    path = os.path.join(MAIN_PATH,
                        OUTPUT_PATH,
                        output_style,
                        f"{input_structure}_result{extension}")
    with open(path, "r") as file:
        return file.read()


@pytest.mark.parametrize("in_structure, in_format, formatter, out_style",
                         [(PLAIN, JSON, None, STYLISH),
                          (PLAIN, YML, None, STYLISH),
                          (RECURSIVE, JSON, None, STYLISH),
                          (RECURSIVE, YML, None, STYLISH),
                          (PLAIN, JSON, STYLISH, STYLISH),
                          (PLAIN, YML, STYLISH, STYLISH),
                          (RECURSIVE, JSON, STYLISH, STYLISH),
                          (RECURSIVE, YML, STYLISH, STYLISH),
                          (PLAIN, JSON, PLAIN, PLAIN),
                          (PLAIN, YML, PLAIN, PLAIN),
                          (RECURSIVE, JSON, PLAIN, PLAIN),
                          (RECURSIVE, YML, PLAIN, PLAIN),
                          (PLAIN, JSON, JSON, JSON),
                          (PLAIN, YML, JSON, JSON),
                          (RECURSIVE, JSON, JSON, JSON),
                          (RECURSIVE, YML, JSON, JSON)])
def test_diff(in_structure, in_format, formatter, out_style):
    """Tests for function 'generate_diff'. For JSON-Formatter function
    works with dictionaries and with strings otherwise"""

    file1, file2 = _get_input_data(in_structure, in_format)
    result = _get_result(in_structure, out_style)

    if formatter is None:
        assert generate_diff(file1, file2) == result
    elif formatter == JSON:
        assert json.loads(generate_diff(file1,
                                        file2,
                                        formatter)) == json.loads(result)
    else:
        assert generate_diff(file1, file2, formatter) == result
