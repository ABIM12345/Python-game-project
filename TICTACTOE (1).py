#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This is an 'X' and 'O' game played by two players


# In[ ]:


#First step is creating the board of the game, inother for display


# In[2]:


def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('______________________________________________')


# In[ ]:


# second step, testinhg the board to see how it looks


# In[3]:


test_board = [str(x) for x in range(0,10)]
display_board(test_board)


# In[ ]:


#In the Input function, players will be able to answer questions if they want to play the game, and if they choose X or O


# In[4]:


def player_input():
    player1_marker = input("do you want to play the game? ")
    if player1_marker == "yes": input('Choose between X and O')
    
    while player1_marker.upper() not in ['X', 'O']:            #while loop to continously ask
        player1_marker = input('Not accepted, Choose between X and O:')

    if player1_marker.upper() == 'X':
        print('player 1 is X')
        print('player 2 is O')
        return ('X', 'O')
    else:
        print('player 1 is O')
        print('player 2 is X')
        return ('O', 'X')


# In[5]:


player_input()


# In[6]:


def place_marker(board, marker, position):
    new_board = board    #new_board needed so that board can be changed when player chooses a position
    new_board[position] = marker    #position in list, in place of the numbers
    return new_board


# In[7]:


place_marker(test_board,'O',7)
display_board(test_board)


# In[8]:


#This is the win_check function, to check if any player has won the game
def win_check(board, mark):
    won_top_horizontal = board[1] == mark and board[2] == mark and board[3] == mark      #If board1,2,3 are X or O. Either Won!
    won_middle_horizontal = board[4] == mark and board[5] == mark and board[6] == mark
    won_bottom_horizontal = board[7] == mark and board[8] == mark and board[9] == mark
    won_left_vertical = board[1] == mark and board[4] == mark and board[7] == mark
    won_middle_vertical = board[2] == mark and board[5] == mark and board[8] == mark
    won_right_vertical = board[3] == mark and board[6] == mark and board[9] == mark
    won_diagonal_one = board[1] == mark and board[5] == mark and board[9] == mark
    won_diagonal_two = board[3] == mark and board[5] == mark and board[7] == mark

    has_won = won_top_horizontal or won_middle_horizontal or won_bottom_horizontal or won_left_vertical or won_middle_vertical or won_right_vertical or won_diagonal_one or won_diagonal_two 

    return has_won


# In[9]:


win_check(test_board,'O')


# In[10]:


# space board check is to know the available space on the board
def space_check(board, position):
    if board[position] not in ['X', 'O']:
        return True
    else:
        return False


# In[11]:


space_check(test_board, 8)


# In[12]:


def full_board_check(board):            
    # this is to check if board is full, that is if there is no more space for any player to play
    is_full = True
    for position, marker in enumerate(test_board):
        if position == 0:
            continue
        else:
            if marker in ['X', 'O']:
                is_full = True
            else:
                is_full = False
                break
    return is_full


# In[13]:


full_board_check(test_board)


# In[14]:


#step 8
def player_choice(board):
    choice = int(input('What position do you want to play on:'))
    is_free = space_check(board, choice)
    
    if is_free:
        print('position', choice, 'is free to play on')
        return choice
    else:
        print('position', choice, 'already has a marker')


# In[15]:


player_choice(test_board)


# In[16]:


def replay():
    response = input('Do you want to play again Y/N?')
    if response.upper() == 'Y':
        return True
    else:
        return False


# In[17]:


replay()


# # using the while loops and functions created to run the game.

# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [str(x) for x in range(0,10)]

    # Player choose markers
    player1_marker, player2_marker = player_input()


    #start the game
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
        print('Game has begun')
    else:
        game_on = False

    turn = 'Player 1'
    while game_on:
        if turn == 'Player 1':
            print('Player 1s turn')
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            print('Player 2s turn')
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
                
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:




