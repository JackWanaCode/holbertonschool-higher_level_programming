class Status:
    def __init__(self, size, stat_arr=[], stat_comb = []):
        self.stat_arr = stat_arr
        self.stat_comb = stat_comb
        self.size = size

    def return_comb(self):
        """create a combination of Queen location"""
        comb = []
        for y in range(self.size):
            for x in range(self.size):
                if self.stat_arr[y][x] == -5:
                    comb += [[y, x]]
        if len(comb) == self.size:
            #self.stat_comb += [comb]
            self.stat_comb += [str(comb)]

    def print_graphic(self, col):
        """print combination as shown on chess board
        uncomment line 15, 49 and comment out line 16, 48 to print
        """
        lis = []
        l = len(self.stat_comb)
        rows = l // col if l % col == 0 else l // col + 1
        r = 0
        for row in range(rows):
            r = row * col + col if row * col + col < l else l
            print("-" * ((self.size * 2 + 5) * col - 4))
            for y in range(self.size):
                for i in range(row * col, r):
                    lis = ["| " * self.stat_comb[i][y][1]] + ["|Q"] + ["| " * (self.size - self.stat_comb[i][y][1] - 1)] + ["|"]
                    if i != col - 1:
                        lis += ["    "]
                    print("".join(lis), end='')
                print("")
            print("-" * ((self.size * 2 + 5) * col - 4))

    def back_status(self, queen):
        """the function will go back previous status
        and set that time queen position to y-direction value"""
        for y in reversed(range(self.size)):
            for x in reversed(range(self.size)):
                if self.stat_arr[y][x] >= queen.pos_y:
                    self.stat_arr[y][x] = 0
                if self.stat_arr[y][x] == -5:
                    if y == 0 and x == self.size - 1:
                        """when no more combination, the program will be exit"""
                        print("\n".join(self.stat_comb))
                        #self.print_graphic(6)
                        exit()
                    else:
                        self.stat_arr[y][x] = queen.pos_y
                        queen.pos_y = y
                        queen.pos_x = x
                        queen.number -= 1
                        return
