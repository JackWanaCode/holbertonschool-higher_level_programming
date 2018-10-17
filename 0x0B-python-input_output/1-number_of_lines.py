#!/usr/bin/python3
def number_of_lines(filename=""):
    ct = 0
    with open(filename, 'r') as f:
        for line in f:
            ct += 1
    return ct
