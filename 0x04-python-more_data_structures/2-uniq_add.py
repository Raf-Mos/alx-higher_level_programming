#!/usr/bin/python3

def uniq_add(my_list=[]):

    new_list = set(my_list)
    uniq_sum = 0
    for x in new_list:
        uniq_sum += x
    return uniq_sum
