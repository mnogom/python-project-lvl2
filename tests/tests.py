from gendiff.core import generate_diff
from gendiff.format import stylish


def test_plain_json():
    """Test for finding difference between two plain JSON files"""

    with open("tests/fixtures/stylish_format/plain_answer.txt", "r") as file:
        ans = file.read()
        diff = generate_diff(
            "tests/fixtures/stylish_format/plain_json/file1.json",
            "tests/fixtures/stylish_format/plain_json/file2.json")
        assert ans == stylish.view(diff)


def test_plain_yaml():
    """Test for finding difference between two plain YAML files"""
    with open("tests/fixtures/stylish_format/plain_answer.txt", "r") as file:
        ans = file.read()
        diff = generate_diff(
            "tests/fixtures/stylish_format/plain_yaml/file1.yaml",
            "tests/fixtures/stylish_format/plain_yaml/file2.yaml")
        assert ans == stylish.view(diff)


def test_recursive_json():
    """Test for finding difference between two recursive JSON files"""

    with open("tests/fixtures/stylish_format/recursive_answer.txt", "r") as file:
        ans = file.read()
        diff = generate_diff(
            "tests/fixtures/stylish_format/recursive_json/file1.json",
            "tests/fixtures/stylish_format/recursive_json/file2.json")
        assert ans == stylish.view(diff)


def test_recursive_yaml():
    """Test for finding difference between two recursive YAML files"""

    with open("tests/fixtures/stylish_format/recursive_answer.txt", "r") as file:
        ans = file.read()
        diff = generate_diff(
            "tests/fixtures/stylish_format/recursive_yaml/file1.yaml",
            "tests/fixtures/stylish_format/recursive_yaml/file2.yaml")
        assert ans == stylish.view(diff)
