#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    my_sum = 0
    for x in new_list:
        my_sum += x
    return (my_sum)
