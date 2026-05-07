#!/usr/bin/python3
"""Module for the Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to
            include in the dictionary.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        # hasattr(object, "attribute_name")
        # is used to check if the object has the specified attribute.

        # getattr(object, "attribute_name") is used to retrieve
        # the value of the specified attribute from the object.
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
