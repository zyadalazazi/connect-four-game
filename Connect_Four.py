from Player import Player
from random import choice
from Board import *
from time import sleep
import pygame
import sys

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


while not game_over:

    if turn == 1:
        col = int(input("It is {0}'s turn, please select a column between 0 and 6:".format(player_one.name)))
        if game.is_column_available(game_board, col):
            row_num = game.get_available_row(game_board, col)
            # print("ROW is ",row_num, " COL is ",col)
            game.drop_chip(game_board, row_num, col, 1)

            if game.check_win(game_board, 1):
                winner = player_one
                game_over = True
        turn += 1

    else:
        col = int(input("It is {0}'s turn, please select a column between 0 and 6:".format(player_two.name)))
        if game.is_column_available(game_board, col):
            row_num = game.get_available_row(game_board, col)
            # print("ROW is ", row_num, " COL is ",col)
            game.drop_chip(game_board, row_num, col, 2)

            if game.check_win(game_board, 2):
                winner = player_two
                game_over = True
        turn -= 1

    print("".center(125, "_"))
    print("Congratulations {0}!, you win!!!\n".format(winner.name))
    print(game_board)
