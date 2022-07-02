#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        maxi = 0
        for val in my_list:
            if val > maxi:
                maxi = val
        return maxi
