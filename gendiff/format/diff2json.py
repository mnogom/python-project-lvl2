"""Module to make json representation."""

import json

from gendiff.format.diff_explorer import get_children


def view(diff):
    """Function to render difference between two files in JSON format.

    :param diff: difference between files
    :return: formatted string
    """
    return json.dumps(get_children(diff),
                      indent=2,
                      sort_keys=True)
