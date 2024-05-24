#!/usr/bin/python3

class CountedIterator:
    """Class named CountedIterator"""
    def __init__(self, iterable):
        """initialized iterable"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """defines next iterator"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        """defines get count"""
        return self.count
