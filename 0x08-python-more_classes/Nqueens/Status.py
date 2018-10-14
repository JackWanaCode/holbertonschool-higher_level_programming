#from Board import Board

class Status:
    def __init__(self, size, stat_arr=[]):
        self.stat_arr = stat_arr
        self.size = size

    def check_N(self):
        """reset the arr to arr of 0"""
        count = 0
        for y in range(self.size):
            for x in range(self.size):
                if self.array[y][x] == -5:
                    count += 1

    def return_comb(self):
        """create a combination of Queen location"""
        comb = []
        for y in range(self.size):
            for x in range(self.size):
                if self.stat_arr[y][x] == -5:
                    comb += [[y, x]]
        return comb

    def back_status(self, queen):
        for y in reversed(range(self.size)):
            for x in reversed(range(self.size)):
                if self.stat_arr[y][x] >= queen.pos_y:
                    self.stat_arr[y][x] = 0
                if self.stat_arr[y][x] == -5:
                    if y == 0 and x == self.size - 1:
                        print("no more combination")
                        exit()
                    else:
                        self.stat_arr[y][x] = queen.pos_y
                        queen.pos_y = y
                        queen.pos_x = x
                        queen.number -= 1
                        return
