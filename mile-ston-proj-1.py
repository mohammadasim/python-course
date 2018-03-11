# For using the same code in either Python 2 or 3
from __future__ import print_function 
import os
import random

# Fuction to clear screan
def clear():
    os.system('clear')

# Function to display board
def display_board(board):
    clear()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')    
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

board = ['#','1','2','3','4','5','6','7','8','9']

# Function to take player's input
def player_input():
    player1_marker = ''
    player2_marker = ''
    selection = ''
    while selection != 'X' and selection != 'O':
        selection = input('Please make a selection between X or O? ').upper()
        if selection == 'X':
            player1_marker = 'X'
            player2_marker = 'O'
        else:
            player1_marker = 'O'
            player2_marker = 'X'
    return (player1_marker,player2_marker)


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == makr and board[7] == mark))

def choose_first():
    pass

place_marker(board,'X',9)
display_board(board)