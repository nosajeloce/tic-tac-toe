class MatchView:
    def __init__(self):
        pass

    def display_player_who_plays_first(self,player):
        print(f"It's player {player.symbol}'s turn to choose a slot")

    def ask_for_slot_choice(self,options:tuple):
        return input(f"Enter your slot choice {options}: ")

    def display_board_state(self,mapping_of_choices:dict):
        print(f"Here's the current board state:"
              f"\n                    {mapping_of_choices[7]} | {mapping_of_choices[8]} | {mapping_of_choices[9]}"
              "\n                    ---------"
              f"\n                    {mapping_of_choices[4]} | {mapping_of_choices[5]} | {mapping_of_choices[6]}"
              "\n                    ---------"
              f"\n                    {mapping_of_choices[1]} | {mapping_of_choices[2]} | {mapping_of_choices[3]}")

    def display_seperator(self):
        print("====================== GAME HAS STARTED ! =========================")

    def display_value_error(self):
        print("Error: Expected a number between 1 and 9. ")

    def display_one_sided_result(self, player_symbol:str):
        print(f"Player {player_symbol} has won!")

    def display_draw_result(self):
        print("It's a draw!")