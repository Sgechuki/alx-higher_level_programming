#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_no = len(sys.argv)
    if arg_no == 1:
        print("{} arguments.".format(arg_no - 1))
    elif arg_no == 2:
        print("{} argument:".format(arg_no - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arg_no - 1))
        for i in range(1, arg_no):
            print("{}: {}".format(i, sys.argv[i]))
