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
        if item in self:
            print(f"Removed {item} from the list")
        else:
            print(f"{item} is not in the list")
        super().remove(item)

    def pop(self, index=None):
        """defines the override method of list pop"""
        if index is None:
            index = len(self) - 1
        popped_item = self[index]
        print(f"Popped {popped_item} from the list.")
        return super().pop(index)
