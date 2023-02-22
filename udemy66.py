def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


test_board = ['#','X','O','X','O','X','O','X','O','X']
# result = display_board(test_board)
# print(result)
#this function display the tic tac toe at start level





def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose 'X' or 'O' ").upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')





def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return((board[7] == board[8] == board[9] == mark ) or
           (board[4] == board[5] == board[6] == mark ) or
           (board[1] == board[2] == board[3] == mark ) or
           (board[7] == board[4] == board[1] == mark ) or
           (board[8] == board[5] == board[2] == mark ) or
           (board[9] == board[6] == board[3] == mark ) or
           (board[7] == board[5] == board[3] == mark ) or
           (board[9] == board[5] == board[1] == mark ))

# result2 = display_board(test_board)
# print(result2)
# result1 = win_check(test_board,'X')
# print(result1)




import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'



def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Enter a value bwt (1-9)'))

    return position


def replay():
    choice = input('Do you want to play again Yes or No')
    return choice == 'Yes'
















#while loop to keep the game running

print('Welcome to the tic tac toe game')

while True:
    #play the  game\\\\



    #set everythingup(board,who'sfirt,choose x,o)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'Will go first')
    play_game = input('Ready to play game? y or n')
    if play_game == 'y':
        gameon = True
    else:
        gameon = False





    #gameplay

    while gameon:
        if turn == 'Player 1':
            #show the Board
            display_board(the_board)

            # choose a position

            position = player_choice(the_board)
            #place the marker on the postion
            place_marker(the_board,player1_marker,position)


            #check if they have won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Yeyyy Player 1 has won !!!!!!")
                gameon = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    gameon = False

                else:
                    turn = 'Player 2'


        else:
            # show the Board
            display_board(the_board)

            # choose a position

            position = player_choice(the_board)
            # place the marker on the postion
            place_marker(the_board, player2_marker, position)

            # check if they have won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Yeyyy Player 2 has won !!!!!!")
                gameon = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    gameon = False

                else:
                    turn = 'Player 1'




    if not replay():
        break

#Break out of the loop

# here we have finished our first game through python




















