#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if ord(i) in range(97, 123):
            string = string + chr(ord(i) - 32)
        else:
            string = string + i
    print("{}".format(string))
