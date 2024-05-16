class Moves:
    def __init__(self):
        pass

    def is_valid_move(self, board, color, row, col, gameLogic):
        if board.board[row][col] != "-":
            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        for dir_row, dir_col in directions:
            new_row, new_col = row + dir_row, col + dir_col
            if 0 <= new_row < 8 and 0 <= new_col < 8 and board.board[new_row][new_col] != "-":
                if board.board[new_row][new_col] != color and gameLogic.checkForOutflanking(board, color, row, col):
                    return True

        return False

    def hasValidMove(self, color, board, gameLogic):
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(board, color, i, j, gameLogic):
                    return True
                        
        return False
    
    def getAllMoves(self, color, board, gameLogic):
        temp_board = board.clone()

        for i in range(8):
            for j in range(8):
                if self.is_valid_move(board, color, i, j, gameLogic):
                    temp_board.board[i][j] = '+'

        return temp_board