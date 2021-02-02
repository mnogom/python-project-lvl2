#!/usr/bin/env python3

"""Module for running main script."""

from gendiff.cli import parse
from gendiff.core import generate_diff


def main():
    """Function to start script."""

    first_file, second_file, style = parse()
    generate_diff(first_file, second_file, style)


if __name__ == "__main__":
    main()


"""
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""