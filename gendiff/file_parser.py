"""Module to parse input file."""

import json

import yaml


def _get_extension(file_path: str) -> str:
    return file_path.split(".")[-1].lower()


def parse_file(file_path: str) -> dict:
    """Read json or yml file and returns dictionary.

    :param file_path: *.json/*.yml file path
    :return: dictionary from json file
    """

    with open(file_path, "rb") as file:
        file_extension = _get_extension(file_path)
        if file_extension == "json":
            return json.load(file)

        if file_extension in ("yaml", "yml"):
            return yaml.load(file, Loader=yaml.SafeLoader)

        raise TypeError((f"Don't know what to do with "
                         f"'{file_extension}' file"))
