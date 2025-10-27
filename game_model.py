class GameModel:
    def __init__(self):
        self.matches = []
        self.scores = {f"X": 0, f"O": 0}

    def add(self, match):
        self.matches.append(match)

    def update_score(self,winner_symbol:str):
        self.scores[winner_symbol] += 1

    def get_scores(self):
        return self.scores