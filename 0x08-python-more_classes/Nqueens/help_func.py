from Queen import Queen
from Board import Board
from Status import Status
from sys import argv

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


def run(size):
    """hand moving for queen to empty cell and go back to previous case
    when no more empty cell"""
    arr = [[0 for x in range(size)] for y in range(size)]
    board = Board(size, [])
    status = Status(size, [[[0 for x in range(size)] for y in range(size)]])
    queen = Queen(size)
    i = 1
    comb_arr = []
    count = 0
    while count < 300:
        count += 1
        # print("arr bf set", arr)
        arr = board.set_queen(queen, arr, len(status.stat_arr))
        if queen.pos_x != -1:
            arr = [sub_arr[:] for sub_arr in queen.move_queen(arr)]
            status.stat_arr.append(arr)
            if len(status.stat_arr) == size + 1:
                """ print the list combination when have
                N queens located on chess board """
                print("combine",status.return_comb())
                arr = [sub_arr[:] for sub_arr in status.stat_arr[1]]
                arr = status.stat_arr[1]
                status.stat_arr = status.stat_arr[:2]
                print("here arr", arr)
                arr = board.next_queen(arr, len(status.stat_arr))
                print("here arr", arr)
                if arr == 0:
                    print("no more combine")
                    exit()
                status.stat_arr.pop()
                print(status.stat_arr)
                print(arr)


        elif queen.pos_x == -1:
            """ go back to previouse status when no more
            cell for Queen moving """
            if len(status.stat_arr) > 1:
                # print("status bf pop", status.stat_arr)
                status.stat_arr.pop()
                # print("status af pop", status.stat_arr)
                arr = [sub_arr[:] for sub_arr in status.stat_arr[-1]]
        #
                arr = board.next_queen(arr, len(status.stat_arr))
                if len(status.stat_arr) == 2:
                    status.stat_arr.pop()
                # print("checkherer", len(status.stat_arr), arr)
                if len(status.stat_arr) == 1 and arr == 0:
                    print("No more combine", count)
                    return
        #         elif arr == 0:
        #             arr = status.stat_arr[-1]
        # print(status.stat_arr)
        # if len(status.stat_arr) == 2:
        #     print(status.stat_arr)
