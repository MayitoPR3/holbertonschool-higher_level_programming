#!/usr/bin/python3
"""
This is the module to create the class Rectangle
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    """This is the Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property to set the width"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns: the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for _ in range(self.height):
            rectangle += "#" * self.width + "\n"
        return rectangle.strip()

    def __repr__(self):
        """Returns: a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints: the message Bye rectangle...
        (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
