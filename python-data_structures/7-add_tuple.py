#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise.

    Args:
        tuple_a (tuple): The first tuple to add.
        tuple_b (tuple): The second tuple to add.

    Returns:
        tuple: A tuple containing the element-wise sum of the input tuples.

    # Ensure both tuples have at least 2 elements by padding 
    with zeros if necessary
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Return the element-wise sum of the first two 
    elements of each tuple
    return (tuple_a[0] + tuple_b[0], 
    tuple_a[1] + tuple_b[1])
    """
    # Ensure both tuples have at least 2 elements by padding with zeros if necessary
    first_a = tuple_a[0] if len(tuple_a) > 0 else 0
    second_a = tuple_a[1] if len(tuple_a) > 1 else 0
    first_b = tuple_b[0] if len(tuple_b) > 0 else 0
    second_b = tuple_b[1] if len(tuple_b) > 1 else 0
    tuple_a = (first_a, second_a)
    tuple_b = (first_b, second_b)

    # Return the element-wise sum of the first two elements of each tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
