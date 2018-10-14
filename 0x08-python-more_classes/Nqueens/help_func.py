from Queen import Queen
from Board import Board
from Status import Status
from sys import argv

def run(size):
    board = Board(size, [])
    status = Status(size, [[0 for x in range(size)] for y in range(size)])
    queen = Queen(size)
    i = 1
    comb_arr = []
    count = 0
    check_set = 0
    check_back = 1
    while True:
        check_set = queen.set_queen(status)
        if check_set == size:
            count += 1
            print(status.return_comb(), count)
            status.stat_arr[queen.pos_y][queen.pos_x] = queen.pos_y
            queen.number -= 1
            status.back_status(queen)
        elif check_set > 0:
            queen.move_queen(status)
        else:
            status.back_status(queen)
