#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    best_key = None
    best_value = 0
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    if best_key is None:
        return (None)
    else:
        return (best_key)
