
# Importing the numpy library
import numpy as np

# Defining constants used in building the game board
ROWS = 6
COLUMNS = 7

"""
This module contains Board class
Attributes:
    board: numpy 2-D array with 6 x 7 dimensions
"""


class Board:

    # Creating the array
    array = np.zeros((ROWS, COLUMNS))

    # Creating the constructor
    def __init__(self, board=array):
        self.board = board

    # A method that defines the function
    def drop_chip(self, board:'np.array', row: 'int', col: 'int', chip: 'int'):
        board[row, col] = chip

    # A method that checks if a column is available
    def is_column_available(self, board: 'np.array', col: 'int'):
        return board[0, col] == 0

    # A method that determines where the location of the of the chip in the column will be
    def get_available_row(self, board: 'np.array', col: 'int'):
        for row in range(ROWS-1, -1, -1):
            if board[row, col] == 0:
                return row

    # A method to check if the players won by aligning the chips horizontally
    def check_horiz_win(self, board: 'np.array', chip: 'int'):
        win = False
        for row in range(ROWS):
            for col in range(COLUMNS-3):
                if board[row, col] == board[row, col+1] == board[row, col+2] == board[row, col+3] == chip:
                    win = True
                    return win

    # A method to check if the player won by aligning the chips vertically
    def check_vertic_win(self, board: 'np.array', chip: 'int'):
        win = False
        for col in range(COLUMNS):
            for row in range(ROWS-3):
                if board[row, col] == board[row+1, col] == board[row+2, col] == board[row+3, col] == chip:
                    win = True
                    return win

    # A method that check if the player won by aligning the chips in a positive diagonal
    def check_diag_up(self, board: 'np.array', chip: 'int'):
        win = False
        for col in range(COLUMNS-3):
            for row in range(ROWS-3):
                if board[row, col] == board[row+1, col+1] == board[row+2, col+2] == board[row+3, col+3] == chip:
                    win = True
                    return True

    # A method that checks if the player won by aligning the chips in a negative diagonal
    def check_diag_down(self, board: 'np.array', chip: 'int'):
        win = False
        for col in range(COLUMNS-3):
            for row in range(3, ROWS):
                if board[row, col] == board[row-1, col+1] == board[row-2, col+2] == board[row-3, col+3] == chip:
                    win = True
                    return win

    # A method that checks if the player won by checking the previous four cases
    def check_win(self, board: 'np.array', chip: 'int'):
        return self.check_horiz_win(board, chip) or self.check_vertic_win(board, chip) or self.check_diag_up(board,\
                                        chip) or self.check_diag_down(board, chip)
