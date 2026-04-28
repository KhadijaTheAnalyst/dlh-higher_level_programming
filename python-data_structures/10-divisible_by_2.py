#!usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all numbers in a list that are divisible by 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of booleans indicating whether each number is divisible by 2.
    """
    result = []
    for value in my_list:
        result.append(value % 2 == 0)
    return result
