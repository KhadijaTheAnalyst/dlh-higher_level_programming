#!/usr/bin/env python3
"""Module for pickling custom objects.

This module provides a CustomObject class that can be serialized
and deserialized using pickle.
"""


import pickle


class CustomObject:
    """A custom object that can be serialized and
    deserialized using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name,
        age, and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Is Student: {self.is_student}"
        )

    def serialize(self, filename):
        """Serialize object to file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file using pickle."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except Exception as e:
            return None
