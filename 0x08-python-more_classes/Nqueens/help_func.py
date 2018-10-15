from Queen import Queen
from Status import Status
from sys import argv

def run(size):
    status = Status(size, [[0 for x in range(size)] for y in range(size)])
    queen = Queen(size)
    i = 1
    check_set = 0
    while True:
        check_set = queen.set_queen(status)
        if check_set == size:
            """print the combination, set queen postion value is y-dir value
            queen number decremented and go back to previous status as normal"""
            status.return_comb()
            status.stat_arr[queen.pos_y][queen.pos_x] = queen.pos_y
            queen.number -= 1
            status.back_status(queen)
        elif check_set > 0:
            queen.move_queen(status)
        else:
            status.back_status(queen)
