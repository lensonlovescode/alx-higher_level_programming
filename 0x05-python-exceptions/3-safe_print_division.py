#!/usr/bin/python3
def safe_print_division(a, b):
    results = None
    try:
        results = a / b
    except ZeroDivisionError:
        results = None
    finally:
        print("Inside results: {}".format(results))
    return (results)
