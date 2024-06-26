#!/usr/bin/python3
"""Module for the class named Custom Object"""
import pickle


class CustomObject:
    """class named CustomObject"""
    def __init__(self, name, age, is_student):
        """initializes the person information"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """defines the display of the information"""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """defines the serialization"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error on Serialization:", e)
            return None

    @classmethod
    def deserialize(cls, filename):
        """defines the deserialization"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Error on Deserialization:", e)
            return None
