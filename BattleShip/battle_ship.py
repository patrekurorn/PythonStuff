from pprint import pprint
import random as rand

board1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

available_ships = {
    0: [1, 1],
    1: [1, 1, 1],
    2: [1, 1, 1, 1],
    3: [1, 1, 1, 1],
    4: [1, 1, 1, 1, 1]
}
TOTAL_HITS = 18

used_rows = []
used_ships = []


def get_row():
    while True:
        my_row = rand.randint(0, 9)
        if my_row not in used_rows:
            used_rows.append(my_row)
            break
    return my_row


def get_ship():
    while True:
        my_ship = rand.randint(0, 4)
        if my_ship not in used_ships:
            used_ships.append(my_ship)
            break
    return my_ship


def get_addition(ship):
    max_value = 10 - len(available_ships[ship])
    addition = rand.randint(0, max_value)
    return addition


def place_ships(board, ships):
    counter = 0
    while True:
        if counter == len(ships):
            break
        my_row = get_row()
        my_ship = get_ship()
        addition = get_addition(my_ship)
        for i in range(10):
            if i <= len(ships[my_ship]) - 1:
                board[my_row][i + addition] = 1
        counter += 1


def is_sunken(board, row):
    for i in board[row]:
        if i == 1:
            return False
    return True


def hit_or_miss(guess, board):
    for row in range(10):
        for col in range(10):
            if guess[0] == row and guess[1] == col:
                if board[row][col] == 2:
                    print("You have already hit here!")
                    return False
                if board[row][col] == 1:
                    print("Hit!")
                    board[row][col] = 2
                    if is_sunken(board, row):
                        print("You have sunken a ship!")
                    return True
                elif board[row][col] == 0:
                    print("Miss")
                    return False


def convert_guess():
    valid = False
    while valid is False:
        guess_row = input("Guess the row: ")
        if guess_row == "i win":
            pprint(board1)
            quit()
        try:
            guess_row = int(guess_row)
            if guess_row < 0 or guess_row > 9:
                print("Guess has to be from 0 to 9.")
                continue
            else:
                valid = True
        except:
            print("Guess has to be an integer.")

    valid = False
    while valid is False:
        guess_col = input("Guess the column: ")
        try:
            guess_col = int(guess_col)
            if guess_col < 0 or guess_col > 9:
                print("Guess has to be from 0 to 9.")
                continue
            else:
                valid = True
        except:
            print("Guess has to be an integer.")
    guess = [guess_row, guess_col]
    return guess


def play_game():
    print("Welcome to Battle Ship.\n"
          "The rules are:\n"
          "There are 5 ships:\n"
          "\t 1x small ship (2 hits)\n"
          "\t 1x medium ship (3 hits)\n"
          "\t 2x lagre ships (4 hits)\n"
          "\t 1x x-large ship (5 hits)\n"
          "All the ships lie horizontally on the board.\n")
    nr_of_hits = 0
    place_ships(board1, available_ships)
    while True:
        guess = convert_guess()
        hit = hit_or_miss(guess, board1)
        if hit is True:
            nr_of_hits += 1
        print()
        if nr_of_hits == TOTAL_HITS:
            print("You won!")
            pprint(board1)
            quit()


play_game()
