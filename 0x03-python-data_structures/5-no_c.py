#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    i = 0
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
        i += 1
    return new_str
