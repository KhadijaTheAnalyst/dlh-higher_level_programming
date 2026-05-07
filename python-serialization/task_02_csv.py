#!/usr/bin/env python3
"""Module for converting CSV to JSON."""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save it to a file.
    Args:
        csv_filename (str): The name of the CSV file to convert.
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        # Open CSV file
        with open(csv_filename, "r", encoding="utf-8") as f:
            # Use DictReader to convert rows
            reader = csv.DictReader(f)
            # Collect all rows into a list
            data = list(reader)

        # Write to JSON file
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

        return True
    except Exception:
        return False
