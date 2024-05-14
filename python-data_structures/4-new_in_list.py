#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    Replace_list = my_list[:]
    if idx >= 0 and idx < len(my_list):
        Replace_list[idx] = element
    return Replace_list
