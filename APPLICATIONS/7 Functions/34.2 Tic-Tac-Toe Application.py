import random
import time

# Tic-Tac-Toe Application V-2.0
print("**"*50)

# Welcome message.
print("Welcome To Tic-Tac-Toe Application.")


def draw_board(pieces_pos):
    # print(pieces_pos)
    print("\nTic-Tac-Toe Application\n")
    print("|", pieces_pos[0], "|", pieces_pos[1], "|", pieces_pos[2], "|")
    print("|", pieces_pos[3], "|", pieces_pos[4], "|", pieces_pos[5], "|")
    print("|", pieces_pos[6], "|", pieces_pos[7], "|", pieces_pos[8], "|")


def get_player_input(player_char, pieces_pos):
    while True:
        print("\n--------------- It's your turn ---------------")
        move = int(
            input(f"\n{player_char}: Where would you like to place your piece (1 - 9): "))
            
        # move is available
        if move > 0 and move < 10:
            # If the space on the board does not currently have a piece there
            if pieces_pos[move-1] == "_":
                # if you do not hit return statement this loop becomes false
                return move
            else:
                print("The spot has already been choosen. Please try again.")
        else:
            print("This is not spot on board. Please try again.")

def get_computer_input(player_char, pieces_pos):
    while True:
        move = random.randint(1,9)

        # If the space on the board does not currently have a piece there
        if pieces_pos[move-1] == "_":
            print("\n--------------- It's computer's turn ---------------")
            time.sleep(1)
            return move


def piece_char_on_board(player_char, move, pieces_pos):
    # Put the players move at correct place
    pieces_pos[move-1] = player_char  # Putting x or o

def choice():
    print("\n1.Duel with friend.")
    print("2.Play with computer.")
    while True:
        option=input("\nEnter your option (1/2): ").strip()
        if option=="1" or option=="2":
            break
        else:
            print("Please enter valid option!!")
    return option

def is_winner(pieces_pos, player_char):
    # 8 ways of winning:3H, 3V, 2D
    return (  # return true or false using compound conditional operator
        # 3 type of Horizontal wins
        (pieces_pos[0] == player_char and pieces_pos[1] == player_char and pieces_pos[2] == player_char) or
        (pieces_pos[3] == player_char and pieces_pos[4] == player_char and pieces_pos[5] == player_char) or
        (pieces_pos[6] == player_char and pieces_pos[7] == player_char and pieces_pos[8] == player_char) or

        # 3 type of Verticle wins
        (pieces_pos[0] == player_char and pieces_pos[3] == player_char and pieces_pos[6] == player_char) or
        (pieces_pos[1] == player_char and pieces_pos[4] == player_char and pieces_pos[7] == player_char) or
        (pieces_pos[2] == player_char and pieces_pos[5] == player_char and pieces_pos[8] == player_char) or

        # 2 type of Digonal wins
        (pieces_pos[0] == player_char and pieces_pos[4] == player_char and pieces_pos[8] == player_char) or
        (pieces_pos[6] == player_char and pieces_pos[4] == player_char and pieces_pos[2] == player_char)
    )


def main():
    player_1 = "X"
    player_2 = "O"
    option=choice()

    c_list = ["_"]*9
    # print(c_list)
    n_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # print(n_list)

    draw_board(n_list)
    draw_board(c_list)

    while True:
        # For player 1
        move = get_player_input(player_1, c_list)
        piece_char_on_board(player_1, move, c_list)  # Update board

        draw_board(n_list)
        draw_board(c_list)

        if is_winner(c_list, player_1):
            print("\nCongratulations! Player 1 wins!")
            break
        # If there is a tie
        elif "_" not in c_list:
            print("\nOhh! The game was a tie!")
            break

        if option=="1":
            # For player 2
            move = get_player_input(player_2, c_list) #For manual insertion
            piece_char_on_board(player_2, move, c_list)  # Update board

            draw_board(n_list)
            draw_board(c_list)

            if is_winner(c_list, player_2):
                print("\nCongratulations! Player 2 wins!")
                break
            # There is no need to cheak if it is tie as it is already checked
        else:
            # For player 2 computer
            move = get_computer_input(player_2, c_list) #For auto insertion
            piece_char_on_board(player_2, move, c_list)  # Update board

            draw_board(n_list)
            draw_board(c_list)

            if is_winner(c_list, player_2):
                print("\nCongratulations! Player 2 wins!")
                break
            # There is no need to cheak if it is tie as it is already checked



if __name__ == '__main__':
    main()

# End of programm.
print("\n\nThank you for using the Tic-Tac-Toe Application. Goodbye.\n")
print("**"*50)
