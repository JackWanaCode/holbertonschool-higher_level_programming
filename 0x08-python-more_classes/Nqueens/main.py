from help_func import run
from sys import argv

l = len(argv)
if l != 2:
    print("Usage: nqueens N")
    exit(1)
if type(int(argv[1])) is not int:
    print("N must be a number")
    exit(1)
elif int(argv[1]) < 4:
    print("N must be at least 4")

run(int(argv[1]))

"""
def check_arr(size, arr):
    sm_queen = Queen(size)
    for arr1 in arr:
        array = [[0 for x in range(size)] for y in range(size)]
        for arr2 in arr1:
            sm_queen.pos_x = arr2[1]
            sm_queen.pos_y = arr2[0]
            if array[sm_queen.pos_y][sm_queen.pos_x] == 1:
                return False
            array = sm_queen.move_queen(array)
    return True
"""
