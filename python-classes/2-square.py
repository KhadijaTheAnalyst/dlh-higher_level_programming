#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """A class that defines a square."""
    def __init__(self, size = 0):
        # Step 1: CHECK THE TYPE FIRST (before assigning)
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")

        # Step 2: THEN check if it's negative
        if size < 0:
            raise ValueError("size must be >= 0")

        # Step 3: ONLY NOW assign it (after all validation passes)
        self.__size = size
