
# Importing the needed libraries and modules
from Player import Player
from random import choice
from Board import *


# A method that validates the column inputted by the player
def validate_input_col(column: 'str', player: 'str'):
    valid_column = False
    while not valid_column:
        if not column.isnumeric():
            column = input("{0}, please select a column between 0 and 6, not a character:".format(player.name))
        elif int(column) not in range(7):
            column = input("{0}, please select a column between 0 and 6, no other numbers:".format(player.name))
        else:
            valid_column = True

    return column


"""
This is where the Connect 4 Game program starts
"""

print("Welcome to Connect 4".center(125, "-"))
print("You need a friend to play this game :)".center(125, " "))

# A list of the available chip colors
available_colors = ["red", "yellow"]

# Reading the names of the players and validating them
name_one = input("Please enter the name of the first player:")
while not name_one.isalpha():
    name_one = input("Please enter the first player's name again and make sure it only has alphabetic characters:")

name_two = input("Please enter the name of the second player:")
while not name_two.isalpha():
    name_two = input("Please enter the second player's name again and make sure it only has alphabetic characters:")
print()


# Setting the chip colors of the players randomly
color_one = choice(available_colors)
color_two = available_colors[0] if available_colors[0] is not color_one else available_colors[1]

# Creating student objects and printing them
player_one = Player(name_one, color_one)
player_two = Player(name_two, color_two)

print(player_one)
print(player_two)

# Creating the Board object and assigning the board to a variable
game = Board()
game_board = game.board

print("\nGame is starting...")

print(game_board)

# Defining necessary variables
turn = 1
game_over = False
winner = Player("", "")

# Starting the game
while not game_over:

    # This condition applies when it is the turn of the first player
    if turn == 1:

        # Reading the number of the column where the first player wants to place their chip
        col = input("It is {0}'s turn, please select a column between 0 and 6:".format(player_one.name))

        # Validating the number of the column
        validate_input_col(col, player_one)
        col = int(col)

        # Validating that the chip is in an available column
        correct_placement = False
        while not correct_placement:

            # Placing the chip in the column and in the proper row
            if game.is_column_available(game_board, col):
                row_num = game.get_available_row(game_board, col)
                game.drop_chip(game_board, row_num, col, 1)
                correct_placement = True

                # Checking if the first player won after each turn
                if game.check_win(game_board, 1):
                    winner = player_one
                    game_over = True

            # Asking the player to enter another valid column
            else:
                print("\nWarning! This column is not available, please choose a different column")
                col = input("Please input another column, {0}:".format(player_one.name))
                col = int(validate_input_col(col, player_one))

        # Switching the turn to the second player
        turn += 1

    # This applies when it is the second player's turn
    else:

        # Reading the number of the column where the second player wants to place their chip
        col = input("It is {0}'s turn, please select a column between 0 and 6:".format(player_two.name))

        # Validating the number of the column
        validate_input_col(col, player_two)
        col = int(col)
        correct_placement = False

        # Validating that the chip is in an available column
        while not correct_placement:

            # Placing the chip in the column and in the proper row
            if game.is_column_available(game_board, col):
                row_num = game.get_available_row(game_board, col)
                game.drop_chip(game_board, row_num, col, 2)
                correct_placement = True

                # Checking if the first player won after each turn
                if game.check_win(game_board, 2):
                    winner = player_two
                    game_over = True

            # Asking the player to enter another valid column
            else:
                print("\nWarning! This column is not available, please choose a different column")
                col = input("Please input another column, {0}:".format(player_two.name))
                col = int(validate_input_col(col, player_two))

        # Switching the turn to the first player
        turn -= 1

    print("".center(125, "_"))
    print(game_board)

# Printing the result and the name of the winner
print("".center(125, "_"))
print("Congratulations {0}!, you win!!!\n".format(winner.name))
print(game_board)
