#!/usr/bin/python3


class VerboseList(list):
    """Class named VerboseList that extends the Python list class"""
    def append(self, item):
        """defines the override method of list append"""
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, iterable):
        """defines the override method of list extend"""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items")

    def remove(self, item):
        """defines the override method of list remove"""
        super().remove(item)
        print(f"Removed {item} from the list")

    def pop(self, index=None):
        """defines the override method of list pop"""
        if index is not None:
            item = self[index]
            print(f"Popped {item} from the list.")
        else:
            item = self[-1]
            print(f"Popped {item} from the list.")
        super().pop(index)
