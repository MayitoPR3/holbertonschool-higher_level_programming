#!/usr/bin/python3
"""BaseGeometry class Module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Method Raises an Exception"""
        raise Exception("area() is not implemented")

    @staticmethod
    def integer_validator(name, value):
        """Method for validating value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
