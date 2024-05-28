#!/usr/bin/python3

def read_file(filename=""):
    """defines the reading of file"""
    with open("my_file_0.txt", encoding="utf-8") as filename:
        print(filename.read())
