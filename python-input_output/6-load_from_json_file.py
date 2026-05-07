#!/usr/bin/python3
"""Module containing the load_from_json_file function."""

import json


def load_from_json_file(filename):
    """Create an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        # Read the JSON string from the file and
        # deserialize it to a Python object
        return json.loads(f.read())
