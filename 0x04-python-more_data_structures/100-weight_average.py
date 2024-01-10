#!/usr/bin/python3

def weight_average(my_list=[]):
    sum_1 = 0
    sum_2 = 0
    for (x, y) in my_list:
        sum_1 += x * y
        sum_2 += y
    weight = sum_1 / sum_2
    return weight
