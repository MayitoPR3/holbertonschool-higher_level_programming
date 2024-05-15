#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for m in my_list:
        if m not in new_list:
            new_list.append(m)
        return sum(new_list)
