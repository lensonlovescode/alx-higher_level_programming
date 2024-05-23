#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) < 123 and ord(letter) > 96:
            upper = ord(letter) - 32
            print("{}".format(chr(upper)), end="")
        else:
            print("{}".format(letter), end="")
    print("\n")
