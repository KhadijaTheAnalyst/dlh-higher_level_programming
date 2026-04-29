#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary."""
    # we can use pop function but we will use del statement instead.
    # a_dictionary.pop(key, None)  # --- IGNORE ---
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
