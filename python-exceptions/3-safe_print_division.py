#!/usr/bin/python3
def safe_print_division(a, b):
    """Print the result of the division of a by b."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
