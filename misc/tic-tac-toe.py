# Author: Vinay Varma Nadimpalli

#draw board
def print_board(*board):

    print ("   |   |   ")
    print (" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
    print ("   |   |   ")
    print ("-----------")
    print ("   |   |   ")
    print (" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
    print ("   |   |   ")
    print ("-----------")
    print ("   |   |   ")
    print (" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
    print ("   |   |   ")

#choosing markeer
def chooseXO():
    while True:
        p1_marker = input("Player 1 choose your marker x or o : ")
        if (p1_marker not in ['x', 'X', 'o', 'O']):
            print ("Invalid input, select marker again \n")
        else:
            if (p1_marker not in ['x', 'X']):
                print ("Player 1 is assigned o \n")
                print ("Player 2 is assigned x \n")
                p2_marker = 'x'
                break
            else:
                print ("Player 1 is assigned x \n")
                print ("Player 2 is assigned o \n")
                p2_marker = 'o'
                break
    return [p1_marker,p2_marker]

#checking win conditions
def winConditions(player_marker,*board):
    if (board[1] == board[2] == board[3] == player_marker or board[4] == board[5] == board[6] == player_marker or board[7] == board[8] == board[9] == player_marker):
        result = "Win"
    elif (board[1] == board[4] == board[7] == player_marker or board[2] == board[5] == board[8] == player_marker or board[3] == board[6] == board[9] == player_marker):
        result = "Win"
    elif (board[1] == board[5] == board[9] == player_marker or board[3] == board[5] == board[7] == player_marker):
        result = "Win"
    else:
        result = "Draw"
    return result

#main problem
def ticatactoe():
    board = ['','1','2','3','4','5','6','7','8','9']
    print ("Welcome to the game of Tic Tac Toe \n")
    print ("Player 1 goes first \n")
    current_player_flag = "p1"
    marker_counter = 0
    markers = chooseXO()
    print ("Here are the markers \n")
    print ("Player 1: %s \n" %(markers[0]))
    print ("Player 2: %s \n" %(markers[1]))

    while (marker_counter<=9):
        if (current_player_flag == "p1"):
            print_board(*board)
            while True:
                p1_input = input("Player 1, enter a position between 1 and 9 to place your marker: ")
                try:
                    if (board[int(p1_input)] != 'x' and board[int(p1_input)] != 'o'):
                            board[int(p1_input)] = markers[0]
                            break;
                    else:
                        print ("Box is occupied\n")
                except Exception as e:
                    print ("Invalid input\n")
            marker_counter = marker_counter + 1
            if (winConditions(markers[0],*board) == "Win"):
                print_board(*board)
                print ("Player 1 wins \n")
                break
            else:
                current_player_flag = "p2"
        else:
            print_board(*board)
            while True:
                p2_input = input("Player 2, enter a position between 1 and 9 to place your marker: ")
                marker_counter = marker_counter + 1
                try:
                    if (board[int(p2_input)] != 'x' and board[int(p2_input)] != 'o'):
                        board[int(p2_input)] = markers[1]
                        break;
                    else:
                        print ("cannot put in that box\n")
                except Exception as e:
                    print ("Invalid input\n")
            if (winConditions(markers[1],*board) == "Win"):
                print_board(*board)
                print ("Player 2 wins \n")
                break
            else:
                current_player_flag = "p1"
    if (marker_counter>9):
        print_board(*board)
        print ("The game is a draw!!!")

if __name__ == '__main__':
    ticatactoe()
