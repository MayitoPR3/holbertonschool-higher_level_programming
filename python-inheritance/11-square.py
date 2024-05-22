#!/usr/bin/python3
"""class named Rectangle that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class named Square inherited from Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns representation of the Square class"""
        return "[{}] {}/{}".format("Square", self.__size, self.__size)
