import time
# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():
    # Show the initial game board
    display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:
        # Handle a turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):
    # Get position from player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows_for_x(), check_rows_for_o()
    column_winner = check_columns_for_x(), check_columns_for_o()
    diagonal_winner = check_diagonals_for_x(), check_diagonals_for_o()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows_for_x():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[0] == board[1] == board[2] != "X"
    row_3 = board[3] == board[4] == board[5] != "-"
    row_4 = board[3] == board[4] == board[5] != "X"
    row_5 = board[6] == board[7] == board[8] != "-"
    row_6 = board[6] == board[7] == board[8] != "X"
    # If any row does have a match, flag that there is a win
    row_7 = row_1 and row_2
    row_8 = row_3 and row_4
    row_9 = row_5 and row_6
    if row_7 or row_8 or row_9:
        print("X won the game")
        game_still_going = False
        time.sleep(3)
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
        # Or return None if there was no winner
    else:
        return None

# Check the columns for a win


def check_rows_for_o():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[0] == board[1] == board[2] != "O"
    row_3 = board[3] == board[4] == board[5] != "-"
    row_4 = board[3] == board[4] == board[5] != "O"
    row_5 = board[6] == board[7] == board[8] != "-"
    row_6 = board[6] == board[7] == board[8] != "O"
    # If any row does have a match, flag that there is a win
    row_7 = row_1 and row_2
    row_8 = row_3 and row_4
    row_9 = row_5 and row_6
    if row_7 or row_8 or row_9:
        print("O won the game")
        game_still_going = False
        time.sleep(3)
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
        # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns_for_x():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[0] == board[3] == board[6] == "X"
    column_3 = board[1] == board[4] == board[7] != "-"
    column_4 = board[1] == board[4] == board[7] == "X"
    column_5 = board[2] == board[5] == board[8] != "-"
    column_6 = board[2] == board[5] == board[8] != "X"
    # If any row does have a match, flag that there is a win
    column_7 = column_1 and column_2
    column_8 = column_3 and column_4
    column_9 = column_5 and column_6
    if column_7 or column_8 or column_9:
        print("X Won the game")
        game_still_going = False
        time.sleep(3)
    # Return the winner
    if column_7:
        return board[0]
    elif column_8:
        return board[1]
    elif column_9:
        return board[2]
        # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win


def check_columns_for_o():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[0] == board[3] == board[6] == "O"
    column_3 = board[1] == board[4] == board[7] != "-"
    column_4 = board[1] == board[4] == board[7] == "O"
    column_5 = board[2] == board[5] == board[8] != "-"
    column_6 = board[2] == board[5] == board[8] != "O"
    # If any row does have a match, flag that there is a win
    column_7 = column_1 and column_2
    column_8 = column_3 and column_4
    column_9 = column_5 and column_6
    if column_7 or column_8 or column_9:
        print("O Won the game")
        game_still_going = False
        time.sleep(3)
    # Return the winner
    if column_7:
        return board[0]
    elif column_8:
        return board[1]
    elif column_9:
        return board[2]
        # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals_for_x():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[0] == board[4] == board[8] == "X"
    diagonal_3 = board[2] == board[4] == board[6] != "-"
    diagonal_4 = board[2] == board[4] == board[6] == "X"
    # If any row does have a match, flag that there is a win
    diagonal_5 = (diagonal_1 and diagonal_2)
    diagonal_6 = (diagonal_3 and diagonal_4)
    if diagonal_5:
        print("X won the game")
        game_still_going = False
        time.sleep(3)

    if diagonal_6:
        print("X won the game")
        game_still_going = False
        time.sleep(3)

    # Return the winner
    if diagonal_5:
        return board[0]
    elif diagonal_6:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie


def check_diagonals_for_o():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[0] == board[4] == board[8] == "O"
    diagonal_3 = board[2] == board[4] == board[6] != "-"
    diagonal_4 = board[2] == board[4] == board[6] == "O"
    # If any row does have a match, flag that there is a win
    diagonal_5 = (diagonal_1 and diagonal_2)
    diagonal_6 = (diagonal_3 and diagonal_4)
    if diagonal_5:
        print("O won the game")
        game_still_going = False
        time.sleep(3)

    if diagonal_6:
        print("O won the game")
        game_still_going = False
        time.sleep(3)

    # Return the winner
    if diagonal_5:
        return board[0]
    elif diagonal_6:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        print("The game tied")
        game_still_going = False
        time.sleep(3)
        return True
    # Else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()