#!usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an element at a specific index in a list.

    Args:
        my_list (list): A list of integers.
        idx (int): The index of the element to delete.

    Returns:
        list: A new list with the element at the specified index removed.
    """
    def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []
    for index in range(len(my_list)):
        if index != idx:
            new_list.append(my_list[index])

    return new_list

