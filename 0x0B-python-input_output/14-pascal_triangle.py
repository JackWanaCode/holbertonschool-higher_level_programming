#!/usr/bin/python3


def pascal_triangle(n):
    """make a pascal triangle"""
    lis = []
    for row in range(n):
        for i in range(row + 1):
            if i == 0:
                lis += [[1]]
            elif i == row:
                lis[row] += [1]
            else:
                lis[row] += [lis[row - 1][i - 1] + lis[row - 1][i]]
    return lis
