#!/usr/bin/python3

import sys

if __name__ == "__main__":
    av = len(argv) - 1
    if av == 0:
        print("0 arguments.")
    else:
        print("{:d} {}".format(length, "arguments:"))
        for i in range(1, av + 1):
            print("{}: {}".format(i, sys.argv[i]))
