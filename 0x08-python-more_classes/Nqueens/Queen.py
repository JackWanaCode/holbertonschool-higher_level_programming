#from Board import Board
#from Status import Status

class Queen:
    def __init__(self, size=0, pos_x=0, pos_y=0, number=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.number = number
        self.size = size

    def set_queen(self, status):
        """locate Queen on Board at empty cell
        return number of queen when success
        otherwise, return 0"""
        for x in range(self.size):
            if status.stat_arr[self.pos_y][x] == 0:
                self.pos_x = x
                status.stat_arr[self.pos_y][x] = -5
                self.number += 1
                return self.number
        return 0

    def move_queen(self, status):
        """move the queen follow queen rules at current rows
        cell value is y-direction of queen"""
        for i in range(self.size):
            if status.stat_arr[self.pos_y][i] == 0:
                status.stat_arr[self.pos_y][i] = self.pos_y + 1
            if status.stat_arr[i][self.pos_x] == 0:
                status.stat_arr[i][self.pos_x] = self.pos_y + 1
            if self.pos_y + i < self.size and self.pos_x + i < self.size:
                if status.stat_arr[self.pos_y + i][self.pos_x + i] == 0:
                    status.stat_arr[self.pos_y + i][self.pos_x + i] = self.pos_y + 1
            if self.pos_y + i < self.size and self.pos_x - i >= 0:
                if status.stat_arr[self.pos_y + i][self.pos_x - i] == 0:
                    status.stat_arr[self.pos_y + i][self.pos_x - i] = self.pos_y + 1
        if self.pos_y + 1 < self.size:
            """y is not the last row, else, no movement"""
            self.pos_y = self.pos_y + 1
        self.pos_x = 0
