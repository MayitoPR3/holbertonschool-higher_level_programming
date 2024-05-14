#!/usr/bin/python3

def no_c(my_string):
    newshow = ""
    for m in my_string:
        if m != "c" and m != "C":
            newshow += m
    return (newshow)
