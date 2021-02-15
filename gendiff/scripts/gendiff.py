#!/usr/bin/env python3

"""Module for running main script."""

from gendiff.cli import parse_user_input
from gendiff.core import generate_diff


def main():
    """Function to start script."""

    first_file, second_file, style = parse_user_input()
    diff = generate_diff(first_file, second_file, formatter=style)
    print(diff)


if __name__ == "__main__":
    main()
