#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_key = []
    for k, v in a_dictionary.items():
        if v == value:
            del_key += [k]
    for k in del_key:
        a_dictionary.pop(k)
    return a_dictionary
