#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i == j or j == 0:
            continue
        elif i < j and i != 8:
            print("{}{}".format(i, j), end=", ")
        elif i == 8 and i < j:
            print("{}{}".format(i, j), end="\n")
