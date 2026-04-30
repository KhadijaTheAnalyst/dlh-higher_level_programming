#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    if not a_dictionary:
        return None
    """"we can use max function with key argument but we will use a for loop instead."""
    # best_key = max(a_dictionary, key=a_dictionary.get)
    best_key = None
    best_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    return best_key
