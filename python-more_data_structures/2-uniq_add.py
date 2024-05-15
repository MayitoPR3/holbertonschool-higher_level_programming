#!/usr/bin/python3
def uniq_add(my_list=[]):
        Makelist = []
        for m in my_list:
            if m not in Makelist:
                Makelist.append(m)
                return sum(Makelist)
