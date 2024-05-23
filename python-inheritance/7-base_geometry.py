#!/usr/bin/python3
"""defines a class"""


class BaseGeometry:
    """class named BaseGeometry"""
    def area(self):
        """returns area of rectangle and raise exception"""
        raise Exception("area() is mot implemented")

    def integer_validator(self, name, value):
        """checks if the value is an integer and raises error if not an int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
