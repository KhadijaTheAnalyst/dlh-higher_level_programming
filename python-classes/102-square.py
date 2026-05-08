#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """A class that defines a square by size and calculates its area."""
    def __init__(self, size=0):
        # Let the setter do the validation and assignment
        self.size = size

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
        # Check type first (reject if not int or float, or if bool)
        if not isinstance(size, (int, float)) or isinstance(size, bool):
            raise TypeError("size must be a number")

        # Check value (reject if negative)
        if size < 0:
            raise ValueError("size must be >= 0")
        # Only assign if all checks pass
        self.__size = size

    def __lt__(self, other):
        """Compare two squares based on their area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare two squares based on their area."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Compare two squares based on their area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares based on their area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare two squares based on their area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare two squares based on their area."""
        return self.area() >= other.area()
