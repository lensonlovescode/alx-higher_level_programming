#!/usr/bin/python3
def no_c(my_string):
    my_list = [char for char in my_string if char != 'C' and char != 'c']
    new_string =''.join(my_list)
    return new_string
