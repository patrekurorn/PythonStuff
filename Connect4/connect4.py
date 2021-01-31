from pprint import pprint

game_board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

RED = 1
YELLOW = 2


def check_if_taken(board, column):
    taken = False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if col == column:
                if row == 0 and board[row][col] != 0:
                    return True
    return taken


def insert(board, chip, column):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if col == column:
                if row <= 4:
                    if board[row][col] == 0 and board[row + 1][col] != 0:
                        board[row][col] = chip
                else:
                    if board[row][col] == 0:
                        board[row][col] = chip


def valid_input():
    while True:
        column = input("Select a column: ")
        try:
            column = int(column)
            if column < 0 or column > 6:
                print("Column has to be from 0 to 6.")
                continue
            else:
                break
        except:
            print("Column has to be an integer.")
    return column


def winner(board):

    # Horizontal --
    for row in range(len(board)):
        for col in range(4):
            if board[row][col] != 0 and board[row][col] == board[row][col+1] and board[row][col+1] == board[row][col+2] and board[row][col+2] == board[row][col+3]:
                return True

    # Vertical |
    for row in range(3):
        for col in range(len(board[0])):
            if board[row][col] != 0 and board[row][col] == board[row+1][col] and board[row+1][col] == board[row+2][col] and board[row+2][col] == board[row+3][col]:
                return True

    # Diagonal \
    for row in range(3):
        for col in range(4):
            if board[row][col] != 0 and board[row][col] == board[row+1][col+1] and board[row+1][col+1] == board[row+2][col+2] and board[row+2][col+2] == board[row+3][col+3]:
                return True

    # Diagonal /
    for row in range(3):
        for col in range(6, 2, -1):
            if board[row][col] != 0 and board[row][col] == board[row+1][col-1] and board[row+1][col-1] == board[row+2][col-2] and board[row+2][col-2] == board[row+3][col-3]:
                return True


def play_game():
    counter = 0

    while True:
        pprint(game_board)
        if counter % 2 == 0:
            chip = RED
        else:
            chip = YELLOW
        column = valid_input()
        if check_if_taken(game_board, column):
            print("This column is full.")
            continue
        insert(game_board, chip, column)
        if winner(game_board):
            print("\nPlayer {} has won!".format(chip))
            pprint(game_board)
            quit()
        counter += 1


play_game()
