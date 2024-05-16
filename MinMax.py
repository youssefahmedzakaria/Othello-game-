import sys

class MinMax:
    def __init__(self):
        pass

    def minimax_decision(self, moves, board, gameLogic, depth):
        def max_value(board, alpha, beta, depth):
            move = False
            if depth == 0 or board.is_full():
                blackScore, whiteScore = gameLogic.calcScore(board)
                return whiteScore - blackScore
            v = -sys.maxsize
            for i in range(8):
                for j in range(8):
                    if moves.is_valid_move(board, "w", i, j, gameLogic):
                        new_board = board.clone()
                        new_board.make_move("w", i, j)
                        gameLogic.doOutflanking(new_board, "w", i, j)
                        score = min_value(new_board, alpha, beta, depth - 1)
                        v = max(v, score)
                        alpha = max(alpha, v)
                        move = True
                        if v >= beta:
                            return v
            if move == False:
                new_board = board.clone()
                score = min_value(new_board, alpha, beta, depth - 1)
                v = max(v, score)
            return v

        def min_value(board, alpha, beta, depth):
            move = False
            if depth == 0 or board.is_full():
                blackScore, whiteScore = gameLogic.calcScore(board)
                return whiteScore - blackScore
            v = sys.maxsize
            for i in range(8):
                for j in range(8):
                    if moves.is_valid_move(board, "b", i, j, gameLogic):
                        new_board = board.clone()
                        new_board.make_move("b", i, j)
                        gameLogic.doOutflanking(new_board, "b", i, j)
                        score = max_value(new_board, alpha, beta, depth - 1)
                        v = min(v, score)
                        beta = min(beta, v)
                        move = True
                        if v <= alpha:
                            return v
            if move == False:
                new_board = board.clone()
                score = min_value(new_board, alpha, beta, depth - 1)
                v = min(v, score)
            return v

        best_score = -sys.maxsize
        best_move = None
        for i in range(8):
            for j in range(8):
                if moves.is_valid_move(board, "w", i, j, gameLogic):
                    new_board = board.clone()
                    new_board.make_move("w", i, j)
                    gameLogic.doOutflanking(new_board, "w", i, j)
                    score = min_value(new_board, -sys.maxsize, sys.maxsize, depth - 1)
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move