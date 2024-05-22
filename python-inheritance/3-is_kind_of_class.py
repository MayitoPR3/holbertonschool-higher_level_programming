#!/usr/bin/python3
"""Definition to check if and object is an instance of the same class"""


def is_kind_of_class(obj, a_class):
    """checks if the object is and instance from the same class a_class"""
    return isinstance(obj, a_class)
