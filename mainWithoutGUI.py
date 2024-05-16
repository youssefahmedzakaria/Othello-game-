import random
import sys
import time
from GameLogic import GameLogic
from OthelloBoard import OthelloBoard
from Player import Player
from Moves import Moves
from MinMax import MinMax

print("Welcome to Othello!")
print("You are white, and the computer is black.")
print("To make a move, enter the x and y coordinates of the square you want to place your piece in.")
print("The x and y coordinates should be between 0 and 7.")

# difficulity level
print("difficulity level")
print("1. Easy")
print("2. Medium")
print("3. Hard")
difficulty = int(input("Enter the difficulity level: "))
print(" ")
if difficulty == 1:
    difficulty = 1
elif difficulty == 2:
    difficulty = 3
else:
    difficulty = 5

board = OthelloBoard()
gameLogic = GameLogic()
player = Player("b", 30)
computer = Player("w", 30)
moves = Moves()
minmax = MinMax()

def update_score():
    blackScore, whiteScore = gameLogic.calcScore(board)
    print("\nComputer Disks: " + str(computer.getPieceNumber()) + " | Player Disks: " + str(
        player.getPieceNumber()) + "\n Black score is " + str(blackScore) + " | White score is " + str(whiteScore) + "\n")

def check_end_game():
    if board.is_full() or player.getPieceNumber() == 0 or computer.getPieceNumber() == 0 or (
            (not moves.hasValidMove(player.getColor(), board, gameLogic)) and (
            not moves.hasValidMove(computer.getColor(), board, gameLogic))):
        blackScore, whiteScore = gameLogic.calcScore(board)
        winner = gameLogic.checkForWinner()
        message = f"{winner}\nBlack score is {blackScore} | White score is {whiteScore}\n\n"
        print(message)
        sys.exit()

def player_move():
    while True:
        row = int(input("Enter x: "))
        col = int(input("Enter y: "))
        print(" ")
        if moves.is_valid_move(board, player.getColor(), row, col, gameLogic):
            break
        else:
            print("Invalid move. Please try again.")

    board.make_move(player.getColor(), row, col)
    player.updatePieceNum()
    gameLogic.doOutflanking(board, player.getColor(), row, col)
    board.display()
    update_score()
    check_end_game()

def computer_move():
    best_score, best_move = minmax.minimax_decision(moves, board, gameLogic, difficulty)
    if best_move:
        row, col = best_move
        board.make_move(computer.getColor(), row, col)
        computer.updatePieceNum()
        gameLogic.doOutflanking(board, computer.getColor(), row, col)
        valid_moves_board = moves.getAllMoves(player.getColor(), board, gameLogic)
        valid_moves_board.display()
        update_score()
    else:
        print("No valid move for computer")
        return

    check_end_game()

    if not moves.hasValidMove(player.getColor(), board, gameLogic):
        print("No valid move for player")
        time.sleep(2)
        computer_move()

def main():
    valid_moves_board = moves.getAllMoves(player.getColor(), board, gameLogic)
    valid_moves_board.display()
    while True:
        player_move()
        print("******************************************")
        time.sleep(2)
        computer_move()

if __name__ == "__main__":
    main()