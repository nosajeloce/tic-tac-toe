import random
from match import Match

class MatchController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.match = None

    def start_match(self):
        self.match = Match()
        self.view.display_seperator()

    def get_board_state(self):
        self.view.display_board_state(self.match.board_state)

    def display_player_with_priority(self):
        self.view.display_player_who_plays_first(self.match.player_with_priority)

    def prompt_user_slot_choice(self):
        return self.view.ask_for_slot_choice(self.match.get_available_slots())

    def validate_slot_pick(self, slot:str):
        try:
            slot_number = int(slot)
            if slot_number not in range(1, 10):
                raise ValueError
            if self.match.has_slot_available(slot_number):
                return True
            else:
                raise Exception("The slot is already occupied.")
        except ValueError:
            self.view.display_value_error()
            return False
        except Exception as e:
            self.view.display_invalid_input_error(e)
        else:
            return slot_number

    def update_board(self,slot_number:int):
        self.match.update_board_state(slot_number)

    def detect_end_of_game(self):
        return self.match.is_end_of_game()

    def display_final_result(self):
        if self.match.winner:
            self.view.display_one_sided_result(self.match.winner.symbol)
        else: #Its a draw
            self.view.display_draw_result()

    def update_score(self):
        if self.match.has_one_sided_result():
            self.model.update_score(self.match.winner.symbol)

    def display_score(self):
        self.view.display_score(self.model.get_scores())

    def save_match(self):
        self.model.add(self.match)

    def determine_priority(self):
        self.match.determine_priority()