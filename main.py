from game_model import GameModel
from intro_controller import IntroController
from intro_view import IntroView
from match_view import MatchView
from match_controller import MatchController

def main():
    #Instanciate Model object, views and controllers
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

    match_controller.start_match()

    #To put all this in a loop
    match_controller.match.determine_priority()
    match_controller.display_player_with_priority()
    match_controller.get_board_state()




if __name__ == "__main__":
    main()