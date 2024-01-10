#!/usr/bin/python3

def weight_average(my_list=[]):
        weight = (sum(x * y) / sum(y)) for (x, y) in my_list

    return weight
