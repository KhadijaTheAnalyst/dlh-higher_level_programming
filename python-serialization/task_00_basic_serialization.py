#!/usr/bin/env python3
"""Module for basic serialization and deserialization of Python objects."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python object and save it to a file.

    Args:
        data: The Python object to serialize.
        filename (str): The name of the file to save to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load a JSON file and deserialize it to a Python object.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
