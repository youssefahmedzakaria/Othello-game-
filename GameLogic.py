class GameLogic:
    whiteScore = 0
    blackScore = 0
    def __init__(self):
        pass

    def calcScore(self, board):
        self.blackScore = 0
        self.whiteScore = 0
        for row in board.board:
            for col in row:
                if col == "b":
                    self.blackScore += 1
                elif col == "w":
                    self.whiteScore += 1
        return self.blackScore, self.whiteScore
        
    def checkForWinner(self):
        if self.blackScore > self.whiteScore:
            return "Black WINS!"
        elif self.whiteScore > self.blackScore:
            return "White WINS!"
        else:
            return "Draw!"
        
    def doOutflanking(self, board, player, row, col):
        # check outflanking vertical down
        for i in range(row+1,8):
            if board.board[i][col] == '-':
                break
            if board.board[i][col] == player:
                board.outflank(player, row, col, i, col)
                break
        
        # check outflanking vertical up
        for i in range(row-1, -1, -1):
            if board.board[i][col] == '-':
                break
            if board.board[i][col] == player:
                board.outflank(player, i, col, row, col)
                break

        # check outflanking horizontal right
        for i in range(col+1, 8):
            if board.board[row][i] == '-':
                break
            if board.board[row][i] == player:
                board.outflank(player, row, col, row, i)
                break
        
        # check outflanking horizontal left
        for i in range(col-1, -1, -1):
            if board.board[row][i] == '-':
                break
            if board.board[row][i] == player:
                board.outflank(player, row, i, row, col)
                break

    def checkForOutflanking(self, board, player, row, col):
        flag = False
        whitePassed = False
        # check outflanking vertical down
        for i in range(row+1,8):
            if board.board[i][col] == '-':
                break
            if board.board[i][col] != player and board.board[i][col] != '-':
                whitePassed = True
            if board.board[i][col] == player:
                if whitePassed:
                    flag = True
                else: 
                    break

        whitePassed = False

        # check outflanking vertical up
        for i in range(row-1, -1, -1):
            if board.board[i][col] == '-':
                break
            if board.board[i][col] != player and board.board[i][col] != '-':
                whitePassed = True
            if board.board[i][col] == player:
                if whitePassed:
                    flag = True
                else:
                    break

        whitePassed = False

        # check outflanking horizontal right
        for i in range(col+1, 8):
            if board.board[row][i] == '-':
                break
            if board.board[row][i] != player and board.board[row][i] != '-':
                whitePassed = True
            if board.board[row][i] == player:
                if whitePassed:
                    flag = True
                else:
                    break
        
        whitePassed = False

        # check outflanking horizontal left
        for i in range(col-1, -1, -1):
            if board.board[row][i] == '-':
                break
            if board.board[row][i] != player and board.board[row][i] != '-':
                whitePassed = True
            if board.board[row][i] == player:
                if whitePassed:
                    flag = True
                else:
                    break
            
        return flag