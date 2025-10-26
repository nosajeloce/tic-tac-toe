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

