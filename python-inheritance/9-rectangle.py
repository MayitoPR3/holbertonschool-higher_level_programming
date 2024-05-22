#!/usr/bin/python3
"""class named Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class named Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area  of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns representation of the Rectangle class"""
        return "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
