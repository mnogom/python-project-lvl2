"""JSON formatter."""

import json


def json_render(diff):
    """Dump diff to JSON.

    :param diff: difference between files
    :return: JSON data
    """
    return json.dumps(diff["children"],
                      indent=2)
