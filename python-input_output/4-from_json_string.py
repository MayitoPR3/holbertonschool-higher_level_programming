#!/usr/bin/python3
"""Module for the function that returns an object
(Python data structure)
represented by a JSON string"""

import json


def from_json_string(my_str):
    """defines the return of an object"""
    return json.loads(my_str)
