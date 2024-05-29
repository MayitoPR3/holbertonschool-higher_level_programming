#!/usr/bin/python3
"""Module for the script that adds all arguments to a
Python list, and then save them to a file"""
import json


def save_to_json_file(my_obj, filename):
    """defines the writing an object to a text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """defines the function that creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        my_object = json.load(file)
    return my_object


def main():
    import sys

    the_list = load_from_json_file('add_item.json')

    save_to_json_file(the_list, 'add_item.json')
