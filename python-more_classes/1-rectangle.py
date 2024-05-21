#!/usr/bin/python3
"""
    This module creates an empty class Rectangle
"""


class Rectangle:
    """
    This is the empty class
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation

        Args:
            width Defaults to 0.
            height Defaults to 0.
        """
    @property
    def width(self):
        """
        Property to retrieve the width

        Returns:
            The width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property to set the width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if value != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
