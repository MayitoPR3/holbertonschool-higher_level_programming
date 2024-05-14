#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for m in range(len(new_list)):
        if new_list[m] % 2 == 0:
            new_list[m] = True
        else:
            new_list[m] = False
    return new_list
