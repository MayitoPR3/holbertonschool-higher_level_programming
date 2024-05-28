#!/usr/bin/python3
"""unction that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """defines the function to write a string to text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return len(text)
