#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if (chr(i) == 'q' or chr(i) == 'e'):
        continue
    else:
        print("{:s}".format(chr(i)), end="")
