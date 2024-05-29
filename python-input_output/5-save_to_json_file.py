#!/usr/bin/python3
"""Module for the function that writes an Object to a
text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """defines the writing an object to a text file"""
    with open(my_obj, 'r') as file:
        data = json.load(file)

    with open(filename, 'w') as file:
        json.dump(data, file)
