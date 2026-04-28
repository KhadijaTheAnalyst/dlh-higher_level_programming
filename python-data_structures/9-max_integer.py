#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        int: The biggest integer in the list.
    """
    if not my_list:
        return None

    max_value = my_list[0]
    for value in my_list:
        if value > max_value:
            max_value = value

    return max_value
