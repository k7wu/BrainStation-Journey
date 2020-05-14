def tictactoe():

    '''
    Tic Tac Toe Game

    '''

    print(
        f'Hello World'
    )

    ### Setting up variables to represent spaces in 3x3 grid

    tictactoe_array = [None, None, None, None,None,None,None,None,None]
    print(tictactoe_array)


    turn_number = 0
    player1_turn = True

    while turn_number < 9:
        if player1_turn:
            player1_position = input(f'Player 1 enter your move: where to place "X"?')
            print(player1_position)
            tictactoe_array[int(player1_position)-1] = 'X'
            print(tictactoe_array)
            player1_turn = False
        else:
            player2_position = input(f'Player 2 enter your move: where to place "O"?')
            print(player2_position)
            tictactoe_array[int(player2_position)-1] = 'O'
            print(tictactoe_array)
            player1_turn = True

        turn_number += 1








tictactoe()
