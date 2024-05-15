#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    may = 0
    for i in new:
        may += i
    return may