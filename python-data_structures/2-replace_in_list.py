#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to replace.
        element: The new element to insert at the specified index.

    Returns:
        The modified list, or the original list if the index is out of bounds.
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    
    my_list[idx] = element
    return my_list
