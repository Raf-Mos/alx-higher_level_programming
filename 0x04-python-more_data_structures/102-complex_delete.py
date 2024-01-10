#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, v in a_dictionary:
        if v == value:
            del a_dictionary[i]
    return a_dictionary
