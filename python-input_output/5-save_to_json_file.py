#!/usr/bin/python3
"""Module to save objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file.

    Args:
        my_obj: The object to serialize.
        filename (str): The filename to save to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        # Serialize the object to a JSON string and write it to the file
        # json.dump(my_obj, f)
        f.write(json.dumps(my_obj))
