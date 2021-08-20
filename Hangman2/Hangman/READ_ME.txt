
Welcome to my Python Hangman game!

The rules of the game are simple:
    1. First you select the difficulty of the game.
    2. You can either guess a single letter or the whole word.
        a. If your guess is either not a single letter or not the same length as the word
            you will get an error message.
        b. If you guess the same letter more than once, you get an error message.
    3. If you run out of guesses you lose.
    4. If you guess the wrong word you automatically lose.
    5. The guesses you have left each round only decrease if you guess incorrectly.
    6. You win by either guessing the whole word correctly or by guessing all the letters.

Scoring system:
    You get a score for each word you guess.
    The score is calculated as such:
        1. The number of times you have guessed is deducted from 20.
        2. That number is then multiplied by the length of the word.
            Formula = (20 - num_guesses) * len(word)
    If you lose you get a 0.

History:
    Each time you play a round, that round gets added to the 'history.csv' file where
    you can see:
        1. The word you were guessing.
        2. Whether you won or lost.
        3. The difficulty.
        4. Your score.
        5. The date when the round was played.
        6. Total wins and losses.
        7. The high score.

Word bank:
    All the words in the game are stored in a text file ('words.txt').
    Each round a single word is randomly selected from the bank for the user to guess.
    At the end of the game you can choose to add words to the word bank:
        1. The word can't be longer than 15 letters.
        2. There cannot be numbers or symbols in the word.
        3. Only single words are allowed.
        4. You can't add the same word twice.

You start the game by running the 'hangman.py' file.
