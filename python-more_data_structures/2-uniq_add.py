#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    unique_integers = set(my_list)
    total = sum(unique_integers)
    return total

def uniq_add1(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    seen = []
    total = 0
    for value in my_list:
        if value not in seen:
            seen.append(value)
            total += value
    return total
