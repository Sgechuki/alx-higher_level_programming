#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    adtn = 0
    arg_no = len(sys.argv)
    if arg_no > 1:
        for i in range(1, arg_no):
            adtn += int(sys.argv[i])
    print("{:d}".format(adtn))
