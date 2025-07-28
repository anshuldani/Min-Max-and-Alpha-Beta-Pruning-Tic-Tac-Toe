#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:54:35 2024

@author: anshuldani
"""

import random
import sys

# Define the Tic-Tac-Toe game class
class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 tic-tac-toe board
        self.current_winner = None  # To keep track of the winner

    def print_board(self):
        # Prints the board with positions 1-9
        for i, row in enumerate([self.board[i * 3:(i + 1) * 3] for i in range(3)]):
            display_row = [' ' if spot == ' ' else spot for spot in row]
            print(f"| {display_row[0] if display_row[0] != ' ' else i*3+1} | {display_row[1] if display_row[1] != ' ' else i*3+2} | {display_row[2] if display_row[2] != ' ' else i*3+3} |")

    def available_moves(self):
        # Adjust moves for positions 1-9 instead of 0-8
        return [i + 1 for i, spot in enumerate(self.board) if spot == ' ']  

    def empty_squares(self):
        return ' ' in self.board  # Returns if there are any empty spaces left

    def num_empty_squares(self):
        return self.board.count(' ')  # Counting the number of empty spaces

    def make_move(self, square, letter):
        # Adjust for 1-9 numbering (internally subtract 1)
        square -= 1
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False  # If the space is empty, we make a move

    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True

        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Primary diagonal
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Secondary diagonal
            if all([s == letter for s in diagonal2]):
                return True

        return False

expanded_nodes_count = 0

# Minimax Algorithm
def minimax_search(game, maximizing_player):
    global expanded_nodes_count
    expanded_nodes_count += 1
    if game.current_winner == 'X':  # Maximizing player wins
        return {'position': None, 'score': 1 * (game.num_empty_squares() + 1)}
    elif game.current_winner == 'O':  # Minimizing player wins
        return {'position': None, 'score': -1 * (game.num_empty_squares() + 1)}
    elif not game.empty_squares():  # No more moves, it's a tie
        return {'position': None, 'score': 0}

    if maximizing_player:
        best = {'position': None, 'score': -float('inf')}  # Maximizing player (X)
        for possible_move in game.available_moves():
            game.make_move(possible_move, 'X')
            sim_score = minimax_search(game, False)  # Simulate move for minimizing player
            game.board[possible_move - 1] = ' '  # Undo move
            game.current_winner = None  # Reset winner
            sim_score['position'] = possible_move

            if sim_score['score'] > best['score']:
                best = sim_score
        return best
    else:
        best = {'position': None, 'score': float('inf')}  # Minimizing player (O)
        for possible_move in game.available_moves():
            game.make_move(possible_move, 'O')
            sim_score = minimax_search(game, True)  # Simulate move for maximizing player
            game.board[possible_move - 1] = ' '  # Undo move
            game.current_winner = None  # Reset winner
            sim_score['position'] = possible_move

            if sim_score['score'] < best['score']:
                best = sim_score
        return best

# Alpha-Beta Pruning Algorithm
def alpha_beta_search(game, maximizing_player=True):
    global expanded_nodes_count
    expanded_nodes_count += 1

    def max_value(game, alpha, beta):
        global expanded_nodes_count
        expanded_nodes_count += 1  # Increment the count for expanded nodes
        if game.current_winner:
            return 1, None
        if not game.empty_squares():
            return 0, None
        v = -float('inf')
        best_move = None
        for move in sorted(game.available_moves(), key=lambda x: x == 5, reverse=True):  # Center move prioritized
            game.make_move(move, 'X')
            v2, _ = min_value(game, alpha, beta)
            game.board[move - 1] = ' '  # Undo move
            game.current_winner = None
            if v2 > v:
                v, best_move = v2, move
            alpha = max(alpha, v)
            if v >= beta:
                return v, best_move
        return v, best_move

    def min_value(game, alpha, beta):
        global expanded_nodes_count
        expanded_nodes_count += 1  # Increment the count for expanded nodes
        if game.current_winner:
            return -1, None
        if not game.empty_squares():
            return 0, None
        v = float('inf')
        best_move = None
        for move in sorted(game.available_moves(), key=lambda x: x == 5, reverse=True):  # Center move prioritized
            game.make_move(move, 'O')
            v2, _ = max_value(game, alpha, beta)
            game.board[move - 1] = ' '  # Undo move
            game.current_winner = None
            if v2 < v:
                v, best_move = v2, move
            beta = min(beta, v)
            if v <= alpha:
                return v, best_move
        return v, best_move

    if maximizing_player:
        result = max_value(game, -float('inf'), float('inf'))[1]
    else:
        result = min_value(game, -float('inf'), float('inf'))[1]

    return result

# Command Line Prompt Game
def play_game():
    # Step 1: Select Algorithm
    print("Select the algorithm to use:")
    print("1. Minimax")
    print("2. Alpha-Beta Pruning")
    algo_choice = input("Enter 1 or 2: ")

    algorithm = 'Minimax' if algo_choice == '1' else 'Alpha-Beta Pruning'

    # Step 2: Select Starting Player
    print("Who starts the game?")
    print("X: Computer (Maximizing Player)")
    print("O: Human (Minimizing Player)")
    start_player = input("Enter 'X' or 'O': ")

    # Step 3: Select Game Type
    print("Select Game Type:")
    print("1. Human vs Computer")
    print("2. Computer vs Computer")
    game_type = input("Enter 1 or 2: ")

    mode = 'Human vs Computer' if game_type == '1' else 'Computer vs Computer'

    # Step 4: Display name, ID, and solution information based on user input
    print("\nDani, Anshul Kaushalbhai, A20580060 solution:")
    print(f"Algorithm: {algorithm}")
    print(f"First: {start_player}")
    print(f"Mode: {mode}\n")

    # Initialize the game
    game = TicTacToeGame()
    current_player = start_player
    game.print_board()

    while game.empty_squares():
        if current_player == 'X':  # Computer's move (X)
            if algo_choice == '1':  # Minimax
                move = minimax_search(game, maximizing_player=True)['position']
            else:  # Alpha-Beta Pruning
                move = alpha_beta_search(game, maximizing_player=True)

        elif game_type == '1' and current_player == 'O':  # Human's move (O)
            print(f"Available moves: {game.available_moves()}")
            valid_move = False
            while not valid_move:
                move = int(input("Enter your move (1-9) or 0 to exit: "))
                if move == 0:
                    print("Game exited.")
                    return
                if move in game.available_moves():
                    valid_move = True
                else:
                    print("Invalid move! Try again.")
        else:  # Computer's move (O) in case of Computer vs Computer game
            if algo_choice == '1':  # Minimax
                move = minimax_search(game, maximizing_player=False)['position']
            else:  # Alpha-Beta Pruning
                move = alpha_beta_search(game, maximizing_player=False)

        game.make_move(move, current_player)
        game.print_board()

        if game.current_winner:
            print(f'{current_player} wins!')
            print(f'Total number of expanded nodes: {expanded_nodes_count}')
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print("It's a tie!")
    print(f'Total number of expanded nodes: {expanded_nodes_count}')

if __name__ == '__main__':
    play_game()
