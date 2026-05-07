#!/usr/bin/env python3
"""Module for serializing and deserializing data using XML format.

This module provides functions to convert Python dictionaries to XML format
and reconstruct dictionaries from XML files using ElementTree.

Note: XML stores all values as strings, so type conversion may be needed
when deserializing.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file.

    This function takes a Python dictionary and converts it to XML format,
    then saves it to the specified file. Each dictionary key becomes an
    XML element, and its value becomes the element's text content.

    Args:
        dictionary (dict): A Python dictionary to serialize.
        filename (str): The filename where the XML data will be saved.
                       If the file exists, it will be overwritten.

    Returns:
        bool: True if serialization was successful, False otherwise.

    Example:
        >>> data = {"name": "John", "age": 25, "city": "New York"}
        >>> serialize_to_xml(data, "data.xml")
        True

    Note:
        All values are converted to strings when saving to XML.
    """
    try:
        # Step 1: Create the root element (top-level XML tag)
        root = ET.Element("data")

        # Step 2: Iterate through dictionary items
        # For each key-value pair, create a child element
        for key, value in dictionary.items():
            # Create a child element with the key as the tag name
            child = ET.SubElement(root, key)
            # Set the element's text content to the value (converted to string)
            child.text = str(value)

        # Step 3: Create an ElementTree object from the root element
        tree = ET.ElementTree(root)

        # Step 4: Write the tree to the file
        # encoding="utf-8" ensures proper character encoding
        tree.write(filename, encoding="utf-8")

        # Return True to indicate successful serialization
        return True

    except Exception as e:
        # If any error occurs (file permission, invalid path, etc.)
        # catch it and return False
        print(f"Error serializing to XML: {e}")
        return False


def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary.

    This function reads an XML file and reconstructs a Python dictionary
    from it. Each XML element becomes a dictionary key, and the element's
    text content becomes the value.

    Args:
        filename (str): The filename of the XML file to deserialize.

    Returns:
        dict: A Python dictionary reconstructed from the XML file.
              Returns None if deserialization fails.

    Example:
        >>> data = deserialize_from_xml("data.xml")
        >>> print(data)
        {'name': 'John', 'age': '25', 'city': 'New York'}

    Note:
        All values are returned as strings. You may need to convert them
        to the appropriate type (int, float, bool, etc.) manually.

        Example:
        >>> data = deserialize_from_xml("data.xml")
        >>> data['age'] = int(data['age'])  # Convert string to int
    """
    try:
        # Step 1: Parse the XML file
        # ET.parse() reads the file and creates an ElementTree object
        tree = ET.parse(filename)

        # Step 2: Get the root element
        # getroot() returns the top-level element of the XML tree
        root = tree.getroot()

        # Step 3: Create an empty dictionary to store the results
        dictionary = {}

        # Step 4: Iterate through all child elements
        # Each child element represents a key-value pair
        for child in root:
            # child.tag is the element's name (dictionary key)
            # child.text is the element's content (dictionary value)
            dictionary[child.tag] = child.text

        # Return the reconstructed dictionary
        return dictionary

    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: File '{filename}' not found.")
        return None

    except ET.ParseError as e:
        # Handle XML parsing errors (malformed XML)
        print(f"Error parsing XML: {e}")
        return None

    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error deserializing from XML: {e}")
        return None


# Example usage (for testing)
if __name__ == "__main__":
    # Create a sample dictionary
    sample_data = {
        "name": "John Doe",
        "age": 25,
        "city": "New York",
        "is_student": True
    }

    print("Original dictionary:")
    print(sample_data)
    print()

    # Serialize the dictionary to XML
    print("Serializing to XML...")
    success = serialize_to_xml(sample_data, "data.xml")
    if success:
        print("Successfully saved to data.xml")
        print()
    else:
        print("Failed to serialize")
        print()

    # Deserialize the XML file back to a dictionary
    print("Deserializing from XML...")
    loaded_data = deserialize_from_xml("data.xml")
    if loaded_data:
        print("Loaded dictionary:")
        print(loaded_data)
        print()

        # Note: All values are strings now
        print(
            "Note: All values are strings "
            "(type conversion needed for other types)"
            )
        print(f"Age type: {type(loaded_data['age'])}")  # <class 'str'>
