import numpy as np

ROWS = 6
COLUMNS = 7


class Board:
    array = np.zeros((ROWS, COLUMNS))

    def __init__(self, board=array):
        self.board = board

    def drop_chip(self, board, row, col, chip):
        board[row, col] = chip

    def is_column_available(self, board, col):
        return board[0, col] == 0

    def get_available_row(self, board, col):
        for row in range(ROWS-1, -1, -1):
            if board[row, col] == 0:
                return row

    def check_horiz_win(self, board, chip):
        win = False
        for row in range(ROWS):
            for col in range(COLUMNS-3):
                if board[row, col] == board[row, col+1] == board[row, col+2] == board[row, col+3] == chip:
                    win = True
                    return win

    def check_vertic_win(self, board, chip):
        win = False
        for col in range(COLUMNS):
            for row in range(ROWS-3):
                if board[row, col] == board[row+1, col] == board[row+2, col] == board[row+3, col] == chip:
                    win = True
                    return win

    def check_diag_up(self, board, chip):
        win = False
        for col in range(COLUMNS-3):
            for row in range(ROWS-3):
                if board[row, col] == board[row+1, col+1] == board[row+2, col+2] == board[row+3, col+3] == chip:
                    win = True
                    return True

    def check_diag_down(self, board, chip):
        win = False
        for col in range(COLUMNS-3):
            for row in range(3, ROWS):
                if board[row, col] == board[row-1, col+1] == board[row-2, col+2] == board[row-3, col+3] == chip:
                    win = True
                    return win

    def check_win(self, board, chip):
        return self.check_horiz_win(board, chip) or self.check_vertic_win(board, chip) or self.check_diag_up(board,\
                                        chip) or self.check_diag_down(board, chip)
