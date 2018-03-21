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
    print(board[7] + '  | ' + board[8] + ' | ' + board[9])
    print('---------')    
    print(board[4] + '  | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + '  | ' + board[2] + ' | ' + board[3])

board = ['#','X','Y','X','Y','X','Y','7','8','9']

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
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] != 'X' and board[position] != 'Y'


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    # Board if Full we return True        
    return True

def player_choice(board):
    player_choice = 0
    while not player_choice in range(1,10) and not space_check(board, player_choice):
        player_choice = input('What position would you like to choose (1:9 ? ')
    return player_choice

def replay():
    choice = input("Play agian? Enter Yes or No")
    return choice == 'Yes'

def play_game():
    play_game = True
    while play_game == True:
        board = ['']*10
        display_board(board)
        player1_marker,player2_marker = player_input()
        player = choose_first()
        print(player + ' goes first ')
        game_over = False
        while not game_over:
            if player == 'Player 1':
                player_input = player_choice(board)
                place_marker(board,player1_marker,player_input)
                if win_check(board,player1_marker):
                    print(player + ' won!')
                    game_over = True
                    break
                elif full_board_check(board):
                    print('Its a draw!')
                    game_over = True
                    break
                else:
                    player == 'Player 2'
                    player_input = player_choice(board)
                    place_marker(board,player1_marker,player_input)
                    if win_check(board,player1_marker):
                        print(player + ' won!')
                        game_over = True
                        break
                    elif full_board_check(board):
                        print('Its a draw!')
                        game_over = True
                        break
                    else:
                        player == 'Player 1'
        rematch = replay()
        if not rematch:
            play_game = False
            break

player1_marker,player2_marker = player_input()
print('These are the markers ' + player1_marker,player2_marker)
play_game()