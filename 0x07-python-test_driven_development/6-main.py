#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
print(max_integer([5]))
print(max_integer([-4, -9, -5, -3]))
print(max_integer([]))
print(max_integer(["1", "2", "3", "4"]))
print(max_integer("my string that's not a list"))
print(max_integer("67.5"))
