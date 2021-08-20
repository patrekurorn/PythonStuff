import random
from wins_and_losses import WinsAndLosses
from history import History

WORDS_FILE = "words.txt"
EASY = 1
MEDIUM = 2
HARD = 3

wins_and_losses = WinsAndLosses()

def get_word():
    with open(WORDS_FILE, "r") as file:
        lines = [line.rstrip('\n') for line in file]

    my_word = random.choice(lines)
    return my_word.upper()

def one_letter_guess(my_word, temp, guess):
    correct_guess = False

    for x in range(len(my_word)):
        if guess == my_word[x]:
            temp[x] = guess
            correct_guess = True

    for i in range(len(temp)):
        print(temp[i], end=" ")
    print()

    return correct_guess

def whole_word_guess(my_word, guess):
    correct_guess = False
    if guess == my_word:
        correct_guess = True
    return correct_guess

def check_guess(my_word, guess):
    error_msg = "Invalid guess. You can only guess a single letter or the whole word"
    if len(guess) > len(my_word):
        print(error_msg)
        return False
    elif 1 < len(guess) < len(my_word):
        print(error_msg)
        return False
    elif guess.isalpha() is False:
        print(error_msg)
        return False
    else:
        return True

def get_number_of_guesses():
    while True:
        print("\n1. 20 guesses (EASY)\n"
              "2. 10 guesses (MEDIUM)\n"
              "3. 5 guesses (HARD)")
        num_guesses = input("Please select the difficulty (1, 2 or 3): ")

        try:
            num_guesses = int(num_guesses)
            if num_guesses > 3 or num_guesses < 1:
                print("\nPlease input 1, 2 or 3.")
            else:
                if num_guesses == EASY:
                    return 20
                elif num_guesses == MEDIUM:
                    return 10
                elif num_guesses == HARD:
                    return 5
        except ValueError:
            print("\nPlease input an integer.")

def get_word_list(word):
    word_list = []
    for letter in word:
        word_list.append(letter)
    return word_list

def continue_or_not():
    while True:
        choice = input("\nDo you want to continue (Y/N)? ").upper()
        if choice == "Y" or choice == "N":
            return choice
        else:
            print("Please input Y or N.")

def winner(word):
    print("\nYOU WON!\nThe word was {}".format(word))

def loser_ran_out_of_guesses(word):
    print("\nYou Lost. You have no more guesses.")
    print("The word was {}".format(word))

def loser_guessed_wrong_word(word):
    print("\nYou Lost. You guessed the wrong word.")
    print("The word was {}".format(word))

def get_score(num_guesses, word):
    score = (20 - num_guesses) * len(word)
    return score

def play_hangman():
    word = get_word()
    word_list = get_word_list(word)
    word_set = set(word_list)

    temp = ["-" for x in word_list]

    correct_guesses = []
    wrong_guesses = []

    max_guesses = get_number_of_guesses()
    num_guesses = 0

    if max_guesses == 20:
        difficulty = "EASY"
    elif max_guesses == 10:
        difficulty = "MEDIUM"
    else:
        difficulty = "HARD"

    print("\nThe word is {} letters long.".format(len(word_list)))
    print("- " * len(word))

    while True:
        guesses_left = max_guesses - num_guesses
        print("\nYou have {} guesses left.".format(guesses_left))

        guess = input("Enter a guess: ").upper()
        if check_guess(word_list, guess):
            if guess in wrong_guesses or guess in correct_guesses:
                print("\nYou have already guessed '{}'".format(guess))
                one_letter_guess(word_list, temp, guess)
                continue

            if len(guess) == len(word):
                if whole_word_guess(word, guess):
                    winner(word)
                    wins_and_losses.add_to_wins()
                    score = get_score(num_guesses, word)
                    history = History(word, 1, 0, difficulty, score)
                    history.add_to_history()
                    print("Score:", score)
                    break
                else:
                    loser_guessed_wrong_word(word)
                    wins_and_losses.add_to_losses()
                    history = History(word, 0, 1, difficulty, 0)
                    history.add_to_history()
                    print("Score: 0")
                    break

            if one_letter_guess(word_list, temp, guess):
                correct_guesses.append(guess)
                print("\n'{}' is in the word!".format(guess))
            else:
                wrong_guesses.append(guess)
                print("\n'{}' is not in the word :(".format(guess))
                num_guesses += 1

        if num_guesses == max_guesses:
            loser_ran_out_of_guesses(word)
            wins_and_losses.add_to_losses()
            history = History(word, 0, 1, difficulty, 0)
            history.add_to_history()
            print("Score: 0")
            break

        if len(correct_guesses) == len(word_set):
            winner(word)
            wins_and_losses.add_to_wins()
            score = get_score(num_guesses, word)
            history = History(word, 1, 0, difficulty, score)
            history.add_to_history()
            print("Score:", score)
            break

    choice = continue_or_not()
    if choice == "Y":
        play_hangman()
    elif choice == "N":
        print("Thank you for playing.\n")

def display_history():
    history = History()
    history.display_history()

def clear_history():
    choice = input("Would you like to clear your game history (Y/N)? ").upper()
    if choice == "Y":
        history = History()
        history.clear_history()
        print("Game history successfully cleared.")
        history.display_history()
    else:
        return

def add_word_to_bank():
    new_word = input("\nEnter 'q' to go to MAIN MENU\nEnter a new word to add to the word bank: ").lower().strip()
    if new_word == "q":
        return
    elif new_word.isalpha():
        if len(new_word) > 15:
            print("Word is too long.")
            add_word_to_bank()
        else:
            with open(WORDS_FILE) as f:
                for word in f:
                    if new_word == word.strip():
                        print("'{}' is already in the bank.".format(new_word))
                        add_word_to_bank()

            with open(WORDS_FILE, "a") as file:
                file.write("\n{}".format(new_word))
                print("'{}' has been added to the word bank.".format(new_word))
                add_word_to_bank()
    else:
        print("Please enter a single word which only contains letters.")
        add_word_to_bank()

def _add_word_to_bank():
    while True:
        already_in_bank = False
        new_word = input("\nEnter 'q' to go to MAIN MENU\nEnter a new word to add to the word bank: ").lower().strip()
        if new_word == "q":
            break
        elif new_word.isalpha() and len(new_word) < 15:
            with open(WORDS_FILE) as f:
                for word in f:
                    if new_word == word.strip():
                        print("'{}' is already in the bank.".format(new_word))
                        already_in_bank = True

            if already_in_bank is True:
                continue

            with open(WORDS_FILE, "a") as file:
                file.write("\n{}".format(new_word))
                print("'{}' has been added to the word bank.".format(new_word))
        else:
            print("Please enter a single word which only contains letters and is 15 letters or shorter.")

def main_menu():
    error_msg = "Please enter 1, 2, 3 or 4."
    while True:
        print("\nMAIN MENU\n"
              "1. Play Hangman\n"
              "2. Game History\n"
              "3. Add to word bank\n"
              "4. Quit\n")

        choice = input("Enter 1, 2, 3 or 4: ")
        try:
            choice = int(choice)
            if choice == 1:
                play_hangman()
                print(wins_and_losses)
            elif choice == 2:
                display_history()
                clear_history()
            elif choice == 3:
                _add_word_to_bank()
            elif choice == 4:
                quit()
            else:
                print(error_msg)
                main_menu()
        except ValueError:
            print(error_msg)
            main_menu()


if __name__ == "__main__":
    main_menu()
