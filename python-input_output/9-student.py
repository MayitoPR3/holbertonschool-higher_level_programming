#!/usr/bin/python3
"""Module for the class Student"""


class Student:
    """Class for the student dictionary"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        serializable_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                serializable_dict[key] = value
        return serializable_dict
