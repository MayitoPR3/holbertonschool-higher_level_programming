#!/usr/bin/python3
"""The module creates a class Square"""


class Square:
    """
    This is the class named Square

    Attributes:
    attr1 (size): means size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area based on size of square

        Returns: an int which is the value
        of the area
        """
        return self.__size * self.__size
