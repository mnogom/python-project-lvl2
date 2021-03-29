#!/usr/bin/env python3

"""Entry point."""

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    """Parse arguments, run gendiff and print result."""

    first_file, second_file, format = parse_args()
    diff = generate_diff(first_file, second_file, format=format)
    print(diff)


if __name__ == "__main__":
    main()
