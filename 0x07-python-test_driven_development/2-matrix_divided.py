#!/usr/bin/python3

"""Calculate sum of two integers
Args:
a: The first parameter
b: The second parameter
Returns: sum of 2 parameters"""


def check_matrix(matrix):
    """Check the matrix if its rows have same size
    and check element must be integer or float type
    """
    temp = 0
    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        if temp == 0:
            temp = len(row)
        elif temp != len(row):
            raise TypeError("Each row of the matrix must have the same size")


def matrix_divided(matrix, div):
    """Return new matrix that each elements will be
    devided by given dive
    """
    try:
        check_matrix(matrix)
    except Exception as e:
        raise e
    if div == 0:
        raise ZeroDivisionError("division by Zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    else:
        return [[round(x / div, 2) for x in row] for row in matrix]
