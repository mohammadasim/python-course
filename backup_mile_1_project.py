def play_game():
    play_game = True
    while play_game == True:
        board = ['']*10
        display_board(board)
        player1_marker,player2_marker = player_input()
        player = choose_first()
        print(player + ' goes first ')
        game_over = False
        print('Game starting')
        if not game_over:
            print('inside the while loop')
            if player == 'Player 1':
                print(player + ' playing')
                player_move = player_choice(board)
                place_marker(board,player1_marker,player_move)
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
                    print(player + ' playing')
                    player_move = player_choice(board)
                    place_marker(board,player2_marker,player_move)
                    if win_check(board,player2_marker):
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