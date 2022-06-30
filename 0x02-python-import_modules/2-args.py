#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_no = len(sys.argv)
    if arg_no == 0:
        print("{} arguments.".format(arg_no))
    elif arg_no == 1:
        print("{} argument:".format(arg_no))
        print("1: {}".format(sys.argv[0]))
    else:
        print("{} arguments:".format(arg_no))
        for i in sys.argv:
            print("{}: {}".format(i, sys.argv[i]))
