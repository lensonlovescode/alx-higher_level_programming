#!/usr/bin/python3
def islower(c):
    if c > chr(96) and c < chr(123):
        return True
    elif c > chr(64) and c < chr(91):
        return False
