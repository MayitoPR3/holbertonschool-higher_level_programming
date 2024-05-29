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

    try:
        the_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        the_list = []

    for arg in sys.argv[1:]:
        the_list.append(arg)

    save_to_json_file(the_list, 'add_item.json')


if __name__ == "__main__":
    main()
