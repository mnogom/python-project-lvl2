"""Module to parse input file."""

import json

import yaml


def parse_file(file: bytes, extension: str) -> dict:
    """Read json or yml file and returns dictionary.

    :param file: *.json/*.yml file path
    :param extension:
    :return: dictionary from json file
    """

    if extension == "json":
        return json.loads(file)
    if extension in ("yaml", "yml"):
        return yaml.safe_load(file)

    raise TypeError((f"Don't know what to do with "
                     f"'{extension}' file"))
