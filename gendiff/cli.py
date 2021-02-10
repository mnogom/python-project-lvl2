"""Module create console interface"""

import argparse


def parse():
    """Parse input parameters

    :return: file paths and arguments
    """
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument(dest="first_file")
    parser.add_argument(dest="second_file")
    parser.add_argument("-f", "--format", dest="FORMAT",
                        help="set format of output",
                        default="stylish")

    args = parser.parse_args()

    return args.first_file, args.second_file, args.FORMAT
