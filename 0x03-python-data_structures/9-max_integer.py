def max_integer(my_list=[]):
    max = my_list[0] if my_list else None
    for num in my_list:
        if max < num:
            max = num
    return max
