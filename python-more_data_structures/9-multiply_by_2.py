#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Return a new dictionary with all values multiplied by 2.
    """
    we can use dict comprehension but we will use a for loop instead.
    new_dict={key: value * 2 for key, value in a_dictionary.items()}
    for each key, value → create key: value*2 in new_dict
    --- IGNORE ---
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
