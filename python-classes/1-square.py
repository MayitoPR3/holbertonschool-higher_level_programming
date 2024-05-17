#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """
    This is the class named Square

    Attributes:
    attr1 (size): means size of square
    """
    def __init__(self, size):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.__size = size
