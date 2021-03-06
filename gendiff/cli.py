"""CLI parser."""

import argparse


def parse_args():
    """Parse input parameters.

    :return: file paths and arguments
    """
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument(dest="first_file")
    parser.add_argument(dest="second_file")
    parser.add_argument("-f", "--format",
                        help="set formatters of output",
                        default="stylish")

    args = parser.parse_args()

    return args.first_file, args.second_file, args.format
