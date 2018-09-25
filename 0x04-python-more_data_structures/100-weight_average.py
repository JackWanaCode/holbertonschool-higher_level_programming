#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    denumerator = 0
    for t in my_list:
        numerator += t[0] * t[1]
        denumerator += t[1]
    return numerator / denumerator if denumerator != 0 else 0
