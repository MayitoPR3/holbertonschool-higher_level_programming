#!/usr/bin/python3

"""
This module is for add integer function
"""


def add_integer(a, b=98):

    """ Function that adds two integers.

    Args:
        a (int): First integer.
        b (int): Second integer, set to zero.

    Returns:
        int: The return value. The sum
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
