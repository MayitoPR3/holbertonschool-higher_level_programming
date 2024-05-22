#!/usr/bin/python3
"""defines a method to check if object is a subclass instance from a class"""


def inherits_from(obj, a_class):
    """checks if object is a subclass instance from a_class"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
