#!/usr/bin/python3


class MyList(list):
    """MyList class inherited from parent class list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
