import random

class GameBoard(object):
    def __init__(self, dimension=3):
        self.dimension = dimension
        self.cells = []
        self.cell_statuses = {}
        self.special_cells = {}

        for i in range(self.dimension):
            arr = []
            for j in range(self.dimension):
                arr.append('R')
                self.cell_statuses[str(i) + "_" + str(j)] = 0
            self.cells.append(arr)

    def dump_cells(self):
        for i in range(self.dimension):
           for j in range(self.dimension):
               print(i,j, self.cells[i][j], self.cell_statuses[str(i) + "_" + str(j)]) 

    def make_special_cells(self):
        count = random.randint(0, self.dimension * self.dimension)

        while count > 0:
            row = random.randint(0, self.dimension-1)
            col = random.randint(0, self.dimension-1)
            if self.cells[row][col] == "R":
                self.cells[row][col] = 'S'
                count -= 1

    def count_special_cells(self, r, c):
        if self.cells[r][c] == 'S':
            print("Game over!!!")
        else:
            print(self.get_neighbors(r, c))

    def get_neighbors(self, r, c):
        neighbors = []
        if r == self.dimension:
            r_max = r
        else:
            r_max = r + 1

        if r == 0:
            r_min = 0
        else:
            r_min = r - 1
        
        if c == self.dimension:
            c_max = c
        else:
            c_max = c + 1

        if c == 0:
            c_min = 0
        else:
            c_min = c - 1
        
        for i in range(r_min, r_max):
            for j in range(c_min, c_max):
                neighbors.append((i,j))

        return neighbors

def main():
    game_board = GameBoard(5)
    game_board.make_special_cells()
    #game_board.dump_cells()
    game_board.count_special_cells(3, 4)

if __name__ == "__main__":
    main()