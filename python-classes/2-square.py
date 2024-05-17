#!/usr/bin/python3
"""This module creates a class Square

Raises:
    TypeError: size must be an integer
    ValueError: size must be >= 0
"""
class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """_summary_

        Args:
            size: size for __size attribute of class instance. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
