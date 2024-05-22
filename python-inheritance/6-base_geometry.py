#!/usr/bin/python3
"""class with an unimplemented area method"""


class BaseGeometry:
    """class named BaseGeometry"""
    def area(self):
        """returns the area of the rectangle"""
        raise Exception("area() is not implemented")
