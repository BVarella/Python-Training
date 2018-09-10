import random

def display_board(board):
    print (board[7] + "|" + board[8] + "|" + board[9])
    print (board[4] + "|" + board[5] + "|" + board[6])
    print (board[1] + "|" + board[2] + "|" + board[3])

def player_input():
    marker = ' '
    while (marker != "X") and (marker != "O"):
        marker = input("Player 1, please pick a marker 'X' or 'O'").upper()

    player1_marker = marker

    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"

    return (player1_marker, player2_marker)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark))

def choose_first():
    if random.randint(1,2) == 1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return (board[position] == " ")

def full_board_check(board):
    for i in range (1, 10):
        if (space_check(board,i)):
            return False
    return True

def player_choice(board):
    position = int(input('Please enter a number'))
    if space_check(board, position):
        return position


def replay():
    choice = (input('Would you like to play again? [y] or [n]'))
    if choice == "y":
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:

    board = [" "]*10
    play1, play2 = player_input()
    turn = choose_first()
    print(turn + "goes first!")

    while True:
        if turn == "Player 1":
        #Player 1 Turn
            display_board(board)
            pos = player_choice(board)
            place_marker(board, play1, pos)

            if win_check(board, play1):
                display_board(board)
                print("Congrats Player 1 :)")
                break
            else:
                if full_board_check(board):
                    display_board(board)
                    print ("Draw!")
                    break
                else:
                    turn = "Player 2"
        # Player2's turn.
        else:
            display_board(board)
            pos = player_choice(board)
            place_marker(board, play2, pos)

            if win_check(board, play2):
                display_board(board)
                print("Congrats Player 2 :)")
                break
            else:
                if full_board_check(board):
                    display_board(board)
                    print ("Draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
