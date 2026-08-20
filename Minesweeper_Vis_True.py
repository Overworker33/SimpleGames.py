import random
import pygame as py

#Minesweeper

mines = 5
cell_size = 20
length = 5
height = 5
mode = 0

board = []

def _fresh_board():
    global board
    board = []
    for i in range(0, length):
        board.append([])
        for j in range(0, height):
            board[i].append(0)

_fresh_board()


print(board)