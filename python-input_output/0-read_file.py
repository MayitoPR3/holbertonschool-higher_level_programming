#!/usr/bin/python3
"""Module that created the defines of read file"""


def read_file(filename=""):
    """defines the reading of file"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
