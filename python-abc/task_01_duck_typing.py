#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Class named Shape"""
    @abstractmethod
    def area(self):
        """Defines the area of the class Shape"""

    @abstractmethod
    def perimeter(self):
        """Defines the perimeter of the class Shape"""


class Circle(Shape):
    """Class named Circle with parent class Shape"""
    def __init__(self, radius):
        """Initialized the radius"""
        if radius < 0:
            raise ValueError("radius must be non negative")
        self.radius = radius

    def area(self):
        """defines the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """defines the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """class named Rectangle with parent class Shape"""
    def __init__(self, width, height):
        """initializes the width and height"""
        self.width = width
        self.height = height

    def area(self):
        """defines the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """defines the area of the perimeter"""
        return (self.width + self.height) * 2


def shape_info(shape):
    """defines the shape information"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
