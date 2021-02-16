"""Module to pick instructions for formatter."""

from gendiff.formatters.json import json_view
from gendiff.formatters.plain import plain_view
from gendiff.formatters.stylish import stylish_view


def get_formatted_diff(diff: list, formatter: str) -> str:
    """ Function to render difference between two files in picked format.

    :param diff: difference from gardener
    :param formatter: ['stylish' | 'plain' | 'json']
    :return:
    """

    if formatter == "stylish":
        return stylish_view(diff)
    if formatter == "plain":
        return plain_view(diff)
    if formatter == "json":
        return json_view(diff)

    raise KeyError(f"Don't know formatter '{formatter}'")
