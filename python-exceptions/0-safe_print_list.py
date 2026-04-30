#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list."""
    """
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print()
            return i
    """
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        i += 1
    print()
    return i
