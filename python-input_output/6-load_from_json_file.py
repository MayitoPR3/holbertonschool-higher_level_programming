#!/usr/bin/python3
"""Module for the function that
creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """defines the function that creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        my_object = json.load(file)
    return my_object
