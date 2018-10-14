
class Board:

    def __init__(self, size=0, array=0, next_arr=None):
        self.size = size
        self.array = array
        self.next_arr = None

    def set_queen(self, queen, array, len):
        """locate Queen on Board at empty cell"""
        # for y in range(self.size):
        if array is not None:
            new_arr = [sub_arr[:] for sub_arr in array]
            for x in range(self.size):
                if new_arr[len - 1][x] == 0:
                    queen.pos_x = x
                    queen.pos_y = len - 1
                    new_arr[len - 1][x] = 2
                    return new_arr
        queen.pos_x = -1

    def next_queen(self, array, len):
        """move the Queen to next empty cell on board"""
        if array is not None:
            new_arr = [sub_arr[:] for sub_arr in array]
        empty_arr = [[0 for x in range(self.size)] for y in range(self.size)]
        # print(len)
        for i in range(self.size - 1):
            if len == 2:
                empty_arr[0][i] = 1
                if array[0][i] == 2:
                    # print("HEEEEEEEERREERERER", empty_arr)
                    return empty_arr
            elif new_arr[len - 1][i] == 0:
                # print("check")
                new_arr[len - 1][i] = 1
                return new_arr
        return 0
