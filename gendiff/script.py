#!/usr/bin/env python3

from gendiff.cli import parse
from gendiff.core import generate_diff


def main():
    first_file, second_file, format = parse()
    generate_diff(first_file, second_file)


if __name__ == "__main__":
    main()
