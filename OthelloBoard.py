class OthelloBoard:
    def __init__(self):
        self.size = 8
        self.board = [['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', 'w', 'b', '-', '-', '-'],
                      ['-', '-', '-', 'b', 'w', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-', '-', '-']]

    def display(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            print(i, end=" ")
            for j in range(8):
                print(self.board[i][j], end=" ")
        
            print(" ")

    def make_move(self, piece, row, col):
        self.board[row][col] = piece

    def is_full(self):
        for row in self.board:
            for col in row:
                if col == "-":
                    return False
        return True
    
    def outflank(self, piece, x1, y1, x2, y2):
        if x1 == x2:
            for i in range(y1, y2):
                self.board[x1][i] = piece

        if y1 == y2:
            for i in range(x1, x2):
                self.board[i][y1] = piece

    def clone(self):
        clone_board = OthelloBoard()
        clone_board.board = [row[:] for row in self.board]
        return clone_board