#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """A class that defines a square by size and position."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with size and position.

        Args:
            size: The size of the square (default 0)
            position: The position of the square as tuple (default (0, 0))
        """
        self.size = size
        self.position = position

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
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the character # at the specified position."""
        if self.__size == 0:
            print()
            return

        # Print empty lines for vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
