#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) < 123 and ord(letter) > 96:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("\n", end="")
