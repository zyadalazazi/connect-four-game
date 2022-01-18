
# Importing the needed modules and libraries
from Player import Player
from random import choice
from Board import *
import pygame
import sys


# Defining the dictionary of available colors and their matching RGB representations
color_dict = {'red': (255, 0, 0), 'yellow': (255, 255, 0)}


# This function draws the main window of the game
def draw_board(board: 'np.array', player1: 'Player', player2: 'Player'):
    for col in range(COLUMNS):
        for row in range(ROWS):

            # This command draws main window
            pygame.draw.rect(screen, (0, 0, 100), (col*WINDOW_SIZE, (row+1)*WINDOW_SIZE, WINDOW_SIZE, WINDOW_SIZE))

            # This draws the empty black circles of the board
            if board[row, col] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (int(col*WINDOW_SIZE + WINDOW_SIZE/2),
                                    int(row*WINDOW_SIZE + WINDOW_SIZE + WINDOW_SIZE/2)), int(WINDOW_SIZE/2 - 5))

            # This draws the chips of the first player
            elif board[row, col] == 1:
                pygame.draw.circle(screen, color_dict[player1.color_chosen], (int(col * WINDOW_SIZE + WINDOW_SIZE / 2),
                                    int(row * WINDOW_SIZE + WINDOW_SIZE + WINDOW_SIZE / 2)), int(WINDOW_SIZE / 2 - 5))

            # This draws the chips of the second player
            else:
                pygame.draw.circle(screen, color_dict[player2.color_chosen], (int(col * WINDOW_SIZE + WINDOW_SIZE / 2),
                    int(row * WINDOW_SIZE + WINDOW_SIZE + WINDOW_SIZE / 2)), int(WINDOW_SIZE / 2 - 5))
    pygame.display.update()


"""
This is where the Connect 4 Game program starts
"""

print("Welcome to Connect 4".center(125, "-"))
print("You need a friend to play this game :)".center(125, " "))

# A list of the available chip colors
available_colors = list(color_dict.keys())

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

# Initiating pygame
pygame.init()
WINDOW_SIZE = 100
size = (COLUMNS * WINDOW_SIZE, (ROWS+1) * WINDOW_SIZE)

screen = pygame.display.set_mode(size)
draw_board(game_board, player_one, player_two)

pygame.display.update()

# Defining the font for displaying the winner
winning_font = pygame.font.SysFont("monospace", 30)

while not game_over:

    # Looping through the events of pygame to define the functionality of each event we need
    for event in pygame.event.get():

        # Exiting the game when clicking on the 'x' button
        if event.type == pygame.QUIT:
            sys.exit()

        # Putting chips into the board based on the horizontal location of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 1:
                x_pos = event.pos[0]
                col = x_pos // WINDOW_SIZE

                if game.is_column_available(game_board, col):
                    row_num = game.get_available_row(game_board, col)
                    game.drop_chip(game_board, row_num, col, 1)

                    if game.check_win(game_board, 1):

                        # Informing the first player of his win
                        label = winning_font.render("Congratulations {0}!, you won!".format(player_one.name), 1,
                                                    color_dict[player_one.color_chosen])
                        screen.blit(label, (50, 10))
                        game_over = True
                turn += 1

            else:
                x_pos = event.pos[0]
                col = x_pos // WINDOW_SIZE

                if game.is_column_available(game_board, col):
                    row_num = game.get_available_row(game_board, col)
                    game.drop_chip(game_board, row_num, col, 2)

                    # Informing the second player of his win
                    if game.check_win(game_board, 2):
                        label = winning_font.render("Congratulations {0}!, you won!".format(player_two.name), 1,
                                                    color_dict[player_two.color_chosen])
                        screen.blit(label, (50, 10))
                        game_over = True
                turn -= 1

            print(game_board)
            draw_board(game_board, player_one, player_two)


# Make the game wait for 5 seconds after it is done
if game_over:
    pygame.time.wait(5000)
