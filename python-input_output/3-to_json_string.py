#!/usr/bin/python3
"""Module containing the to_json_string function."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
