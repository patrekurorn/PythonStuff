
class WinsAndLosses:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def add_to_wins(self):
        self.wins += 1

    def add_to_losses(self):
        self.losses += 1

    def __str__(self):
        return "Number of wins: {}\nNumber of losses: {}".format(self.wins, self.losses)
