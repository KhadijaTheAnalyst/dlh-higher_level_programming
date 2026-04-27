#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list like in C.

    Args:
        my_list (list): The list to search through.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index, or None if the index is out of bounds.
    """
    """if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None"""
    if idx < 0:
            return None
    if idx >= len(my_list):
            return None
    else:
            return my_list[idx]
