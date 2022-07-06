#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    w_adtn = 0
    sum_prdct = 0
    for tup in my_list:
        sum_prdct += (tup[0] * tup[1])
        w_adtn = w_adtn + tup[1]
    return float(sum_prdct) / w_adtn
