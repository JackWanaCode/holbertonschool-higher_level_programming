#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        new_list = []
        i = 0
        for num in my_list:
            if i != idx:
                new_list.append(num)
            else:
                new_list.append(element)
            i += 1
        return new_list
    return my_list
