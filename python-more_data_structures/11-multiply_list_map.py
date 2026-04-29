#!/usr/bin/python3
def multiply_map_list(my_list=[], number=0):
    """Return a list with all values multiplied by a number."""
    # we can use list comprehension but we will use map function instead.
    # new_list = [x * number for x in my_list]  # --- IGNORE ---
    new_list = list(map(lambda x: x * number, my_list))
    return new_list
