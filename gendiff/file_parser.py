"""File parser."""

import json

import yaml


def parse(data: bytes, extension: str) -> dict:
    """Parse JSON or YAML data and returns dictionary.

    :param data: data from file
    :param extension:
    :return: dictionary from data
    """

    if extension == ".json":
        return json.loads(data)
    if extension in (".yaml", ".yml"):
        return yaml.safe_load(data)

    raise TypeError(f"Unknown extension: {extension}")
