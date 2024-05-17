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

    @property
    def size(self):
        """
        Property to retrieve size

        Return: the size of the area
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size value

        Args:
            value (_type_): looks for the value

        Raises:
            TypeError: size must be int
            ValueError: size must be >= 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
