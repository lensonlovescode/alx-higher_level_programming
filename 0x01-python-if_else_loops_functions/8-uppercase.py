#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) < 123 and ord(letter) > 96:
            upper = ord(letter) - 32
            print(f"{chr(upper)}", end="")
        else:
            print(f"{letter}", end="")
