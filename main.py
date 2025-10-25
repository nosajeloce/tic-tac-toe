from game_model import GameModel
from intro_controller import IntroController
from intro_view import IntroView


def main():
    #Instanciate Model object, views and controllers
    #Model
    model = GameModel()

    #Views
    intro_view = IntroView()

    #Controllers
    intro_controller = IntroController(model,intro_view)

    #Welcome message, developer name, HOW-TO-PLAY, how to win
    intro_controller.get_intro_message()

    #Input to start the game or end the program
    while True:
        #Ask if the player wants to play
        response = intro_controller.prompt_user_to_play()

        if intro_controller.process_input(response): #Checks if the input is valid. If the script enters this if statement, then the input is valid
            if intro_controller.user_will_play: #If the user responded Yes (Y,y)
                print("Y")
                break
            else: #If the user responded (N,n) -> terminate the program
                print("N")
                return #Since this is inside a function, the main(), it should terminate the program.




if __name__ == "__main__":
    main()