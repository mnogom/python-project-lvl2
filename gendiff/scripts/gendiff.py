#!/usr/bin/env python3

"""Module for running main script."""

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    """Function to start script."""

    first_file, second_file, style = parse_args()
    diff = generate_diff(first_file, second_file, formatter=style)
    print(diff)


if __name__ == "__main__":
    main()
