#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print("{} arguments".format(len(sys.argv)))
    counter = 1
    for i in range(len(sys.argv) - 1):
        print("{}: {}".format(counter, sys.argv[counter]))
        counter += 1
