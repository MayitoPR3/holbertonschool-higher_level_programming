#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        Reverseorder = reversed(my_list)
        for m in Reverseorder:
            print("{:d}".format(m))