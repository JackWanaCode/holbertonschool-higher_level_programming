#!/usr/bin/python3
def remove_char_at(string, n):
    i = 0
    new_str = ""
    for c in string:
        if i != n:
            new_str += c
        i += 1
    return new_str
