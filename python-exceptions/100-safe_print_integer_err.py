#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Print an integer with "{:d}".format().

    Args:
        value: The value to be printed

    Returns:
        If value has been correctly printed - True.
        Otherwise - False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
