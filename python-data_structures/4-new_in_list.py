#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without
    modifying the original list (like in C).

    Args:
        my_list (list): The list to copy and modify.
        idx (int): The index of the element to replace.
        element: The new element to insert at the specified index.

    Returns:
    A new list with the specified element replaced, or the original
    list if the index is out of bounds.
    """
    if idx < 0:
        return my_list[:]
    if idx >= len(my_list):
        return my_list[:]

    new_list = my_list[:]
    new_list[idx] = element

    return new_list
