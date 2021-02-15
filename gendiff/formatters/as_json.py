"""Module to make json representation."""

import json

from gendiff.formatters.diff_explorer import get_children


def json_view(diff):
    """Function to render difference between two files in JSON formatters.

    :param diff: difference between files
    :return: formatted string
    """
    return json.dumps(get_children(diff),
                      indent=2,
                      sort_keys=True)
