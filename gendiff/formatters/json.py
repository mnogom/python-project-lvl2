"""Module to make json representation."""

import json


def json_view(diff):
    """Function to render difference between two files in JSON formatters.

    :param diff: difference between files
    :return: formatted string
    """
    return json.dumps(diff["children"],
                      indent=2,
                      sort_keys=True)
