#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    av = len(argv) - 1
    if av == 0:
        print("{}".format("0 arguments."))
    elif av == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(av, "arguments:"))
        for i in range(1, av + 1):
            print("{:d}: {}".format(i, argv[i]))
