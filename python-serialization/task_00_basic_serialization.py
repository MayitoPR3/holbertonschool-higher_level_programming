#!/usr/bin/python3
"""Module to the Task 0"""
import json


def serialize_and_save_to_file(data, filename):
    """defines the serialize"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """defines the deserialize"""
    with open(filename, 'r') as f:
        info = json.load(f)
    return info
