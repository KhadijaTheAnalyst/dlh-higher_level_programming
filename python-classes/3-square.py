#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """A class that defines a square."""
    def __init__(self, size=0):
        # Check type first (reject if not int, or if bool)
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")

        # Check value (reject if negative)
        if size < 0:
            raise ValueError("size must be >= 0")

        # Only assign if all checks pass
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
