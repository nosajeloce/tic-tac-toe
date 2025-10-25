class GameModel:
    def __init__(self):
        self.matches = []

    def add(self, match):
        self.matches.append(match)

    def get_all_matches(self):
        return self.matches

    def get_match(self, match_number):
        """
        Method used for spectating previously played matches within a playing session
        Also used for debugging score feature
        Method that returns the match with the specified match_number. Mqtch numbers is 1 for match 1 and
        continues at 2 for match 2 and so on.
        :param match_number: match_number is the nth match a player wish to review
        :return: The desired match (every board state done and printed out sequentially)
        """
        return self.matches[match_number-1]

