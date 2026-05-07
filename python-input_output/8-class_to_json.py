#!/usr/bin/python3
"""Module for converting a class to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj: The object to convert to a dictionary.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
