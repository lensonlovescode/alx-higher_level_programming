#!/usr/bin/python3
for no in range(10):
    for nah in range(no + 1, 10):
        if no != nah:
            if no == 8 and nah == 9:
                print("{:d}{:d}".format(no, nah))
            else:
                print("{:d}{:d}".format(no, nah), end=", ")
