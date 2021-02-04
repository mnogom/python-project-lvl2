#!/usr/bin/env python3

"""Module for running main script."""

from gendiff.cli import parse
from gendiff.core import generate_diff
from gendiff.format import stylish


def main():
    """Function to start script."""

    first_file, second_file, style = parse()
    difference = generate_diff(first_file, second_file, style)
    print(stylish.view(difference))


if __name__ == "__main__":
    main()
