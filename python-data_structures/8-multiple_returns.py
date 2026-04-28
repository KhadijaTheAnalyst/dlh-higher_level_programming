#!/usr/bin/python3
def multiple_returns(sentence):
    """Return the length of a string and its first character.

    Args:
        sentence (str): The string to analyze.

    Returns:
        tuple: A tuple containing the length of the string
        and its first character.

    A value is treated as FALSE in conditions if it is:
    "" → empty string
    0 → zero
    None
    [] → empty list
    {} → empty dict
    """
    length = len(sentence)
    if not sentence:
        return (0, None)
    return (length, sentence[0])
