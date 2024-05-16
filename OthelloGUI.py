from tkinter import messagebox
from GameLogic import GameLogic
from OthelloBoard import OthelloBoard
from MinMax import MinMax
from Player import Player
from Moves import Moves
import tkinter as tk
import sys


player = Player("b", 30)
computer = Player("w", 30)
board = OthelloBoard()
gameLogic = GameLogic()
minMax = MinMax()
moves = Moves()


class OthelloGUI:
    def __init__(self, master, difficulty):
        self.difficulty = difficulty

        self.master = master
        self.master.title("Othello")
        self.master.geometry("500x560")
        self.board_canvas = tk.Canvas(self.master, bg="#009067", width=500, height=500)
        self.board_canvas.pack()
        self.winner_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.winner_label.pack()
        self.draw_board()
        self.board_canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        square_size = 500 // 8
        for i in range(8):
            for j in range(8):
                x1, y1 = i * square_size, j * square_size
                x2, y2 = x1 + square_size, y1 + square_size
                self.board_canvas.create_rectangle(x1, y1, x2, y2, fill="#009067")

        self.draw_pieces(square_size, moves.getAllMoves(player.getColor(), board, gameLogic))

    def draw_pieces(self, square_size, temp_board):
        for i in range(8):
            for j in range(8):
                x1, y1 = i * square_size, j * square_size
                x2, y2 = x1 + square_size, y1 + square_size
                if temp_board.board[j][i] == 'w':
                    self.board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill='white')
                elif temp_board.board[j][i] == 'b':
                    self.board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill='black')
                elif temp_board.board[j][i] == '+':
                    self.board_canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5)

    def check_end_game(self):
        if board.is_full() or player.getPieceNumber() == 0 or computer.getPieceNumber() == 0 or ((not moves.hasValidMove(player.getColor(), board, gameLogic)) and (not moves.hasValidMove(computer.getColor(), board, gameLogic))):
            blackScore, whiteScore = gameLogic.calcScore(board)
            winner = gameLogic.checkForWinner()
            message = f"{winner}\nBlack score is {blackScore} | White score is {whiteScore}"
            messagebox.showinfo("Game Over", message)
            sys.exit()

    def update_score(self):
        blackScore, whiteScore = gameLogic.calcScore(board)
        self.winner_label.config(text="Computer Disks: " + str(computer.getPieceNumber()) + " | Player Disks: " + str(player.getPieceNumber()) + "\n Black score is " + str(blackScore) + " | White score is " + str(whiteScore))

    def computer_move(self):
        best_score, best_move = minMax.minimax_decision(moves, board, gameLogic, self.difficulty)
        if best_move:
            row, col = best_move
            board.make_move(computer.getColor(), row, col)
            computer.updatePieceNum()
            gameLogic.doOutflanking(board, computer.getColor(), row, col)
            self.update_score()
            self.draw_board()
        else:
            self.winner_label.config(text= "No valid move for computer")
            return

        self.check_end_game()

        if not moves.hasValidMove(player.getColor(), board, gameLogic):
            self.winner_label.config(text= "No valid move for player")
            self.master.after(1000, self.computer_move)

    def player_move(self, row, col):
        board.make_move(player.getColor(), row, col)
        player.updatePieceNum()
        gameLogic.doOutflanking(board, player.getColor(), row, col)
        self.update_score()
        self.draw_board()
        self.check_end_game()

    def on_click(self, event):
        square_size = 500 // 8
        col = event.x // square_size
        row = event.y // square_size

        if moves.is_valid_move(board, player.getColor(), row, col, gameLogic):
            self.player_move(row, col)
            
            self.master.after(1000, self.computer_move)