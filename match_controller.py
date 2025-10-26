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

    def prompt_user_slot_choice(self):
        return self.view.ask_for_slot_choice()

    def validate_slot_pick(self, slot:str):
        """
        Method that returns the slot number when slot is a str that has anumerical value between 1 and 9 inclusively.
        To be used in the main file to repeat the input of the slot choice if it keeps being invalid.
        :param slot:Input from the user
        :return: False = invalid input. slot_number = valid number input between 1 and 9 inclusively
        """
        try:
            slot_number = int(slot)
            if slot_number not in range(1, 10):
                raise ValueError
        except ValueError:
            self.view.display_value_error()
            return False
        else:
            return slot_number

    def update_board(self,slot_number:int):
        self.match.update_board_state(slot_number)