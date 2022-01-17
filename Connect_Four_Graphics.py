from Player import Player
from random import choice
from Board import *
from time import sleep
import pygame
from pygame.locals import *
import sys
import math

color_dict = {'red': (255, 0, 0), 'yellow': (255, 255, 0)}


def draw_board(board: 'np.array', player1: 'Player', player2: 'Player'):
    for col in range(COLUMNS):
        for row in range(ROWS):
            pygame.draw.rect(screen, (0, 0, 100), (col*WINDOW_SIZE, (row+1)*WINDOW_SIZE, WINDOW_SIZE, WINDOW_SIZE))

            if board[row, col] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (int(col*WINDOW_SIZE + WINDOW_SIZE/2),
                    int(row*WINDOW_SIZE + WINDOW_SIZE + WINDOW_SIZE/2)), int(WINDOW_SIZE/2 - 5))
            elif board[row, col] == 1:
                pygame.draw.circle(screen, color_dict[player1.color_chosen], (int(col * WINDOW_SIZE + WINDOW_SIZE / 2),
                    int(row * WINDOW_SIZE + WINDOW_SIZE + WINDOW_SIZE / 2)), int(WINDOW_SIZE / 2 - 5))
            else:
                pygame.draw.circle(screen, color_dict[player2.color_chosen], (int(col * WINDOW_SIZE + WINDOW_SIZE / 2),
                    int(row * WINDOW_SIZE + WINDOW_SIZE + WINDOW_SIZE / 2)), int(WINDOW_SIZE / 2 - 5))
    pygame.display.update()


print("Welcome to Connect 4".center(125, "-"))
print("You need a friend to play this game :)".center(125, " "))

available_colors = ["red", "yellow"]
name_one = input("Please enter the name of the first player:")
name_two = input("Please enter the name of the second player:")
print()

color_one = choice(available_colors)
color_two = available_colors[0] if available_colors[0] is not color_one else available_colors[1]

player_one = Player(name_one, color_one)
player_two = Player(name_two, color_two)

print(player_one)
print(player_two)

game = Board()
game_board = game.board
# sleep(3)
print("\nGame is starting...")
# sleep(3)
print(game_board)

turn = 1
game_over = False
winner = Player("", "")

pygame.init()

WINDOW_SIZE = 100
size = (COLUMNS * WINDOW_SIZE, (ROWS+1) * WINDOW_SIZE)

screen = pygame.display.set_mode(size)
draw_board(game_board, player_one, player_two)

pygame.display.update()

winning_font = pygame.font.SysFont("monospace", 30)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            if turn == 1:
                x_pos = event.pos[0]
                col = x_pos//WINDOW_SIZE

                if game.is_column_available(game_board, col):
                    row_num = game.get_available_row(game_board, col)

                    game.drop_chip(game_board, row_num, col, 1)

                    if game.check_win(game_board, 1):
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

                    if game.check_win(game_board, 2):
                        label = winning_font.render("Congratulations {0}!, you won!".format(player_one.name), 1,
                                                    color_dict[player_one.color_chosen])
                        screen.blit(label, (50, 10))
                        game_over = True
                turn -= 1

            print(game_board)
            draw_board(game_board, player_one, player_two)


if game_over:
    pygame.time.wait(5000)
