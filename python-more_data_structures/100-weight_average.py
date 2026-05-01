#!/usr/bin/python3
def weight_average(my_list=[]):
    """Calculate the weighted average of all integers tuple in a list."""
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for product, weight in my_list:
        total_score += product * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_score / total_weight
