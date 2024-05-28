#!/usr/bin/python3
import sys
if __name__ == '__main__':
    num_args = len(sys.argv)
    if num_args == 0:
        print("{} arguments.".format(len(sys.argv) - 1))
    counter = 1
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
        print("{:d}: {:s}".format(counter, sys.argv[counter]))
        counter += 1
