#!/usr/bin/python3
"""Module for the class Student"""


class Student:
    """Class for the student dictionary"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            attrs = self.__dict__.keys()

        serializable_dict = {}
        for attr in attrs:
            if isinstance(attr, str) and hasattr(self, attr):
                serializable_dict[attr] = getattr(self, attr)
        return serializable_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
