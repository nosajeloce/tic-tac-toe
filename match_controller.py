import random
from match import Match

class MatchController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.match = None

    def start_match(self):
        if not self.match:
            self.match = Match()
        self.view.display_seperator()

    def get_board_state(self):
        board = self.match.board_state
        self.view.display_board_state(board)

    def display_player_with_priority(self):
        self.view.display_player_who_plays_first(self.match.player_with_priority)


