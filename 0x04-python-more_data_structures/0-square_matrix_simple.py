#!/usr/bin/python3
def square_list_num(l=[]):
    return list(map(lambda x: (x * x), l))


def square_matrix_simple(matrix=[]):
    return list(map(square_list_num, matrix))
