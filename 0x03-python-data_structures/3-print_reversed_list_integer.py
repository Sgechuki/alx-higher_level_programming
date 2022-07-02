#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    ind = -1
    while i < len(my_list):
        print("{:d}".format(my_list[ind]))
        i = i + 1
        ind = (-1 - 1)
