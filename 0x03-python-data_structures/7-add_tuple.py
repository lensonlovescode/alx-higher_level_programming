#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
    if len(tuple_a) != 2:
        tuple_a_one = tuple_a[0] if len(tuple_a == 1) else 0
        tuple_a_two = 0
    else:
       tuple_a_one = tuple_a[0]
       tuple_a_two = tuple_a[1]

    if len(tuple_b) != 2:
        tuple_b_one = tuple_b[0] if len(tuple_b == 1) else 0
        tuple_b_two = 0
    else:
        tuple_b_one = tuple_b[0]
        tuple_b_two = tuple_b[1]
        
    ans1 = tuple_a_one + tuple_b_one
    ans2 = tuple_a_two + tuple_b_two

    my_tuple = (ans1, ans2)
    return my_tuple
