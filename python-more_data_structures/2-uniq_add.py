#!/usr/bin/python3
def uniq_add(my_list=[]):
        another_list = []
        for i in my_list:
            if i not in another_list:
                another_list.append(i)
        return sum(another_list)
