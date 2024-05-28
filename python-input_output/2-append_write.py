#!/usr/bin/python3
"""Module for the function that appends a string at the end of a text file (UTF8)
 and returns the number of characters added"""


def append_write(filename="", text=""):
    """defines - appends a string at the end of a text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        append_write(filename="")
        return len(text)
