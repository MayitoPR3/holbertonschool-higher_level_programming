#!/usr/bin/python3
class Rectangle:
    """This is the Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return (self.width + self.height) * 2

    @property
    def width(self):
        """Property to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property to set the width"""
        if isinstance(value, int) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property to set the height"""
        if isinstance(value, int) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
