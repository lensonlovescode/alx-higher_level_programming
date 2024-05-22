#!/usr/bin/python3
for no in range(100):
    if no != 99:
        print("{:d}, ".format(no), end="")
    else:
        print("{:d}".format(no))
