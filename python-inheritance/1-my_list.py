#!/usr/bin/python3

"""This is THE MyList module"""


class MyList(list):
    """MyList class inherited from parent class list"""

    def print_sorted(self):
        """prints sorted list"""

        sorting = self.copy()
        sorting.sort()
        print(sorting)
