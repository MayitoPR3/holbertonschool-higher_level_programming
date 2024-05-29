#!/usr/bin/python3
"""Module for the function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """defines the return of the dictionary description"""
    serializable_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
    return serializable_dict
