#!/usr/bin/python3

def read_file(filename=""):
    """defines the reading of file"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
