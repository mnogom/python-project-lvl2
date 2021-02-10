from gendiff.core import generate_diff


# -- Stylish tests --


def test_plain_json2stylish():
    """Test for finding difference between
    two plain JSON files in stylish format."""

    with open("tests/fixtures/outputs/stylish/plain_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/plain_json/file1.json",
            "tests/fixtures/inputs/plain_json/file2.json",
            formatter="stylish")


def test_plain_yml2stylish():
    """Test for finding difference between
    two plain YML files in stylish format."""

    with open("tests/fixtures/outputs/stylish/plain_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/plain_yml/file1.yml",
            "tests/fixtures/inputs/plain_yml/file2.yml",
            formatter="stylish")


def test_recursive_json2stylish():
    """Test for finding difference between
    two recursive JSON files in stylish format."""

    with open("tests/fixtures/outputs/stylish/rec_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/recursive_json/file1.json",
            "tests/fixtures/inputs/recursive_json/file2.json",
            formatter="stylish")


def test_recursive_yml2stylish():
    """Test for finding difference between
    two recursive YML files in stylish format."""

    with open("tests/fixtures/outputs/stylish/rec_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/recursive_yml/file1.yml",
            "tests/fixtures/inputs/recursive_yml/file2.yml",
            formatter="stylish")


# -- Plain tests --


def test_plain_json2plain():
    """Test for finding difference between
    two plain JSON files in plain format."""

    with open("tests/fixtures/outputs/plain/plain_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/plain_json/file1.json",
            "tests/fixtures/inputs/plain_json/file2.json",
            formatter="plain")


def test_plain_yml2plain():
    """Test for finding difference between
    two plain YML files in plain format."""

    with open("tests/fixtures/outputs/plain/plain_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/plain_yml/file1.yml",
            "tests/fixtures/inputs/plain_yml/file2.yml",
            formatter="plain")


def test_recursive_json2plain():
    """Test for finding difference between
    two recursive JSON files in plain format."""

    with open("tests/fixtures/outputs/plain/rec_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/recursive_json/file1.json",
            "tests/fixtures/inputs/recursive_json/file2.json",
            formatter="plain")


def test_recursive_yml2plain():
    """Test for finding difference between
    two recursive YML files in plain format."""

    with open("tests/fixtures/outputs/plain/rec_answer.txt", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/recursive_yml/file1.yml",
            "tests/fixtures/inputs/recursive_yml/file2.yml",
            formatter="plain")


# -- Stylish tests --


def test_plain_json2json():
    """Test for finding difference between
    two plain JSON files in plain format."""

    with open("tests/fixtures/outputs/json/plain_answer.json", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/plain_json/file1.json",
            "tests/fixtures/inputs/plain_json/file2.json",
            formatter="json")


def test_plain_yml2json():
    """Test for finding difference between
    two plain YML files in plain format."""

    with open("tests/fixtures/outputs/json/plain_answer.json", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/plain_yml/file1.yml",
            "tests/fixtures/inputs/plain_yml/file2.yml",
            formatter="json")


def test_recursive_json2json():
    """Test for finding difference between
    two recursive JSON files in plain format."""

    with open("tests/fixtures/outputs/json/rec_answer.json", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/recursive_json/file1.json",
            "tests/fixtures/inputs/recursive_json/file2.json",
            formatter="json")


def test_recursive_yml2json():
    """Test for finding difference between
    two recursive YML files in plain format."""

    with open("tests/fixtures/outputs/json/rec_answer.json", "r") as file:
        ans = file.read()
        assert ans == generate_diff(
            "tests/fixtures/inputs/recursive_yml/file1.yml",
            "tests/fixtures/inputs/recursive_yml/file2.yml",
            formatter="json")
