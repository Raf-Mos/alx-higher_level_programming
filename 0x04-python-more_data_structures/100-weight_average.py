#!/usr/bin/python3

def weight_average(my_list=[]):
    for (x, y) in my_list:
        weight = sum(x * y) / sum(y)

    return weight
