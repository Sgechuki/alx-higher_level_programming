#!/usr/bin/python3
def uniq_add(my_list=[]):
    adtn = 0
    for i in set(my_list):
        adtn += i
    return adtn
