from gendiff.core import generate_diff


def test_plain_json():
    """Test for finding difference between two plain JSON files"""

    with open("tests/fixtures/plain_answer.txt", "r") as file:
        assert generate_diff(
            "tests/fixtures/plain_json/file1.json",
            "tests/fixtures/plain_json/file2.json") == file.read()


def test_plain_yaml():
    """Test for finding difference between two plain YAML files"""
    with open("tests/fixtures/plain_answer.txt", "r") as file:
        assert generate_diff(
            "tests/fixtures/plain_yaml/file1.yaml",
            "tests/fixtures/plain_yaml/file2.yaml") == file.read()


def test_recursive_json():
    """Test for finding difference between two recursive JSON files"""

    with open("tests/fixtures/recursive_answer.txt", "r") as file:
        assert generate_diff(
            "tests/fixtures/recursive_json/file1.json",
            "tests/fixtures/recursive_json/file2.json") == file.read()


def test_recursive_yaml():
    """Test for finding difference between two recursive YAML files"""

    with open("tests/fixtures/recursive_answer.txt", "r") as file:
        assert generate_diff(
            "tests/fixtures/recursive_yaml/file1.yaml",
            "tests/fixtures/recursive_yaml/file2.yaml") == file.read()
