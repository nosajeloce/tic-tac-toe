


class IntroController:
    def __init__(self, view):
        self.view = view
        self.user_will_play= False

    def get_intro_message(self):
        self.view.get_intro_message()

    def prompt_user_to_play(self):
        return self.view.ask_user_to_play()

    def process_input(self, input):
        """

        :param input: Text inputted by the user.
        :return: A boolean. False = Keep the input loop going until its valid. Only happens if the input is invalid.
        True = the input was valid (Y,y,N or n). This ends the loop that asks the user to input if they want to play or not in the main.py.
        """
        try:
            if input.upper() == "Y":
                self.user_will_play = True
                return True
            elif input.upper() == "N":
                self.user_will_play = False
                return True
            else:
                raise ValueError("Invalid input. Expected 'Y' or 'N'.")
        except ValueError as e:
            print(f"Error: {e}")
            return False #This continues the main loop to give chance for the user to correct their input

    def ask_user_to_play_again(self):
        return self.view.ask_user_to_play_again()