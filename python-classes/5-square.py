#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """A class that defines a square by size and calculates its area."""
    def __init__(self, size=0):
        # Let the setter do the validation and assignment
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square with validation."""
        # Check type first (reject if not int, or if bool)
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")

        # Check value (reject if negative)
        if size < 0:
            raise ValueError("size must be >= 0")
        # Only assign if all checks pass
        self.__size = size

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
