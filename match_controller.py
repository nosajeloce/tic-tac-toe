import random
from match import Match

class MatchController:
    def __init__(self, view):
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
        """
        Method that returns True when slot is a str that has anumerical value between 1 and 9 inclusively.
        To be used in the main file to repeat the input of the slot choice if it keeps being invalid.
        :param slot:Input from the user
        :return: False = invalid input. True = valid number input between 1 and 9 inclusively
        """
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
            print(e)
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