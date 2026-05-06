#!/usr/bin/python3
"""Module containing the read_file function."""

def read_file(filename=""):
    """Read a text file and print its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
