from Board import Board
#from Status import Status

class Queen:
    def __init__(self, size=0, pos_x=0, pos_y=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

    def move_queen(self, arr):
        """move the queen follow queen rules"""
        array = [sub_arr[:] for sub_arr in arr]
        for i in range(self.size):
            array[self.pos_y][i] = 1
            array[i][self.pos_x] = 1
            if self.pos_y + i < self.size and self.pos_x + i < self.size:
                array[self.pos_y + i][self.pos_x + i] = 1
            if self.pos_y - i >= 0 and self.pos_x - i >= 0:
                array[self.pos_y - i][self.pos_x - i] = 1
            if self.pos_y + i < self.size and self.pos_x - i >= 0:
                array[self.pos_y + i][self.pos_x - i] = 1
            if self.pos_y - i >= 0 and self.pos_x + i < self.size:
                array[self.pos_y - i][self.pos_x + i] = 1
        array[self.pos_y][self.pos_x] = 2
        return array
