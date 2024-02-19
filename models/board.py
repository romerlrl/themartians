import random

class Board:
    board = [[]]
    empty_cells = []
    notable_cells = {}

    def init_by_randomness(self, rows: int = 8, cols: int = 8, goals: int = 4, seed: int = None):
        if seed is not None:
            random.seed(seed)
        self.board = [["EE" for i in range(rows)] for j in range(cols)]
        self.empty_cells = random.sample([(i, j) for i in range(rows) for j in range(cols)], cols * rows)
        self.notable_cells = {}
        BASE = self.empty_cells.pop()
        self.board[BASE[0]][BASE[1]] = "BB"
        self.notable_cells['BB'] = BASE
        for i in range(goals):
            g1, g2 = self.empty_cells.pop()
            self.board[g1][g2] = f"G{chr(49+i)}"
            self.notable_cells[f"G{chr(49+i)}"] = (g1, g2)

    def init_with_matrix(self, matrix: list):
        print("MATRIX", matrix, type(matrix))
        self.board = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                cell = matrix[i][j]
                if cell == "EE":
                    self.empty_cells.append((i, j))
                else:
                    self.notable_cells[cell] = ((i, j))
        random.sample(self.empty_cells, len(self.empty_cells))







