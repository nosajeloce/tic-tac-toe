import random
from player import Player

class Match:
    def __init__(self):
        self.player_x = Player("X")
        self.player_o = Player("O")
        self.player_with_priority = None
        self.board_state = {slot_number:" " for slot_number in range(1,10)} # Attribute that represents the board with slots (filled or empty, filled = "X" or "O" and empty = " " (space))
        self.winner = None


    def determine_priority(self):
        """
        Priority means who has the priority to pick a slot on the board.
        This method determines which player has pick priority
        :return: The Player object that has pick priority
        """
        if not self.player_with_priority:
            #The game will assign pick priority randomly if no one has pick priority.
            self.player_with_priority = random.choice([self.player_x,self.player_o])

        else: #This else branch implies that one of the players have pick priority. All we need to do, is to alternate pick priority to the other player
            if self.player_with_priority == self.player_x:
                self.player_with_priority = self.player_o
            else:
                self.player_with_priority = self.player_x

    def update_board_state(self,slot_number:int):
        self.board_state[slot_number] = self.player_with_priority.symbol

    def is_end_of_game(self):
        """
        :return: if this method returns True, then the game will end. Otherwise (match still going), return False
        """
        if self.has_one_sided_result() or self.end_in_a_draw():
            return True
        #If nobody won and it's not a draw (execution gets to this point), then keep the game going
        return False

    def end_in_a_draw(self):
        #Check if it's a draw. Draw = Board is full and nobody wins
        contents_of_board = list(self.board_state.values())
        if " " not in contents_of_board:
            return True
        return False

    def has_one_sided_result(self):
        #Check whether the new placement just make the player who made that placement win
        current_players_symbol = self.player_with_priority.symbol
        list_combinations_to_victory = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]

        chosen_slot_placements = []
        for slot_number,slot_content in self.board_state.items():
            if  slot_content == current_players_symbol:
                chosen_slot_placements.append(slot_number)

        counter_to_victory = 0 #If this counter variable gets to 3, meaning that the slot placements are in one of the sets-
        #in list_combinations_to_victory, return True, the player that played won.
        for combination_slots_to_victory in list_combinations_to_victory:
            for chosen_slot_placement in chosen_slot_placements:
                if chosen_slot_placement in combination_slots_to_victory:
                    counter_to_victory += 1

                if counter_to_victory == 3:
                    self.winner = self.player_with_priority
                    return True
            counter_to_victory = 0

        return False

    def has_slot_available(self,slot_number):
        """
        Method that checks if a slot is available for getting picked
        :param slot_number: integer corresponding to the slot choice
        :return: boolean. True when the slot is empty, false if the slot has content that is not space (" ")
        """
        if self.board_state[slot_number] == " ":
            return True
        return False

    def get_available_slots(self):
        slots = []

        for slot_number in self.board_state.keys():
            if self.has_slot_available(slot_number):
                slots.append(slot_number)

        return slots

