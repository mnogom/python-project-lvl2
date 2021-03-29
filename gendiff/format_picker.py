"""Format picker."""

from gendiff.formatters.json import json_render
from gendiff.formatters.plain import plain_render
from gendiff.formatters.stylish import stylish_render


def render_diff(diff: dict, format: str) -> str:
    """Render difference between two files in picked format.

    :param diff: difference between two files
    :param format: ['stylish' | 'plain' | 'json']
    :return:
    """

    if format == "stylish":
        return stylish_render(diff)
    if format == "plain":
        return plain_render(diff)
    if format == "json":
        return json_render(diff)

    raise KeyError(f"Unknown format '{format}'")
