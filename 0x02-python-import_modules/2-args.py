#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print("{:d} arguments".format(len(sys.argv) - 1))
    counter = 1
    for i in range(len(sys.argv) - 1):
        print("{:d}: {:s}".format(counter, sys.argv[counter]))
        counter += 1
