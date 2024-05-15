#!/usr/bin/python3
def search_replace(my_list, search, replace):
        return [replace if m == search else m for m in my_list]