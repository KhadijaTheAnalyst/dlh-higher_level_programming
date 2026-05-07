#!/usr/bin/python3
"""Module containing the append_write function."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and
    return the number of characters written.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
