#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxi = my_list[0]
        for val in my_list:
            if val > maxi:
                maxi = val
        return maxi
    else:
        return None
