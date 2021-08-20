import csv
import datetime
import os

class History:
    def __init__(self, word="", win=0, loss=0, difficulty="", score=0):
        self.word = word
        self.win = win
        self.loss = loss
        self.date = datetime.datetime.today()
        self.difficulty = difficulty
        self.score = score
        self.file = "history.csv"

    def add_to_history(self):
        if len(self.word) > 0:
            with open(self.file, "a", encoding="utf-8") as file:
                try:
                    writer = csv.writer(file)
                    writer.writerow([self.word, self.win, self.loss, self.difficulty, self.score, self.date.strftime('%d-%m-%Y')])
                except:
                    return

    def get_history(self):
        history = []
        with open(self.file, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                history.append(row)
        return history

    def display_history(self):
        data = self.get_history()
        print("\n{:<10} {:>12} {:>10} {:>15} {:>6} {:>8}\n{}".format("Word", "Win", "Loss", "Difficulty", "Score", "Date", "-"*72))

        wins = 0
        losses = 0
        high_score = 0

        for row in data:
            win = int(row[1])
            loss = int(row[2])
            print("{:<17} {:>3} {:>9} {:>12} {:>9} {:>17}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
            wins += win
            losses += loss

            score = int(row[4])
            if score > high_score:
                high_score = score
        print("\nTotal wins:\t{}".format(wins))
        print("Total losses:\t{}".format(losses))
        print("HIGH SCORE:\t{}".format(high_score))

    def clear_history(self):
        os.remove(self.file)
        header = "Word,Win,Loss,Difficulty,Score,Date\n"

        with open(self.file, "a+", encoding="utf-8") as file:
            file.write(header)
