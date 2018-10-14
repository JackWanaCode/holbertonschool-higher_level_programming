from Board import Board

class Status:
    def __init__(self, size, stat_arr=[]):
        self.stat_arr = stat_arr
        self.size = size

    def reset_arr(self):
        """reset the arr to arr of 0"""
        l = len(self.stat_arr)
        while l > 1:
            self.stat_arr.pop()
            l -= 1

    def return_comb(self):
        """create a combination of Queen location"""
        comb = []
        for y in range(self.size):
            for x in range(self.size):
                if self.stat_arr[-1][y][x] == 2:
                    comb += [[y, x]]
        return comb
