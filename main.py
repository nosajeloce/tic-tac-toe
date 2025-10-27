from intro_controller import IntroController
from intro_view import IntroView
from match_view import MatchView
from match_controller import MatchController
from game_model import GameModel

def main():
    #Instanciate model object, views and controllers
    #Model
    model = GameModel()

    #Views
    intro_view = IntroView()
    match_view = MatchView()

    #Controllers
    intro_controller = IntroController(intro_view)
    match_controller = MatchController(model, match_view)

    #Welcome message, developer name, HOW-TO-PLAY, how to win
    intro_controller.get_intro_message()

    #Input to start the game or end the program
    while True:
        #Ask if the player wants to play
        response = intro_controller.prompt_user_to_play()

        if intro_controller.process_input(response): #Checks if the input is valid. If the script enters this if statement, then the input is valid
            if intro_controller.user_will_play: #If the user responded Yes (Y,y)
                break
            else: #If the user responded (N,n) -> terminate the program
                return #Since this is inside a function, the main(), it should terminate the program.

    continue_playing = "Y"
    while continue_playing == "Y":
        #Instantiate a Match object
        match_controller.start_match()

        while True: #while True = match is pending
            # Set who gets to pick a slot
            match_controller.determine_priority()

            #Print out who gets to pick a slot
            match_controller.display_player_with_priority()

            #Print the board and the pieces on the board
            match_controller.get_board_state()

            #Get the choice from the player who can pick
            slot_choice = match_controller.prompt_user_slot_choice()

            #Validate the input
            while not match_controller.validate_slot_pick(slot_choice):
                slot_choice = match_controller.prompt_user_slot_choice()

            #To access the match.Match.board_state content, we need this variable to be an int to access the dictionary content:
            #the keys of the dictionary are integer keys from 1 to 9
            slot_choice = int(slot_choice)

            #Update board state
            match_controller.update_board(slot_choice)

            #Check if the player who played just end the game with a victory or a draw
            match_is_ending = match_controller.detect_end_of_game()
            if match_is_ending: #if True = the match will end
                match_controller.get_board_state()
                match_controller.display_final_result()

                #Update and display scoreboard for playing session
                match_controller.update_score()
                match_controller.display_score()

                #Save the match to keep track of the score
                match_controller.save_match()
                break

        continue_playing = intro_controller.ask_user_to_play_again().upper()



if __name__ == "__main__":
    main()