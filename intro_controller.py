from intro_view import IntroView


class IntroController:
    def __init__(self, model, view:IntroView):
        self.model = model
        self.view = view
        self.user_will_play: bool = False

    def get_intro_message(self):
        self.view.get_intro_message()

    def prompt_user_to_play(self):
        return input("Do you and your opponent want to play? [Y/N] ")

    def process_input(self, input):
        """

        :param input: Text. If it's Y or y, return True. Otherwise, return False
        :return: A boolean. False = Keep the input loop going until its valid. Only happens if the input is invalid.
        True = the input was valid (Y,y,N or n). This ends the loop that requires the user to input if they want to play or not.
        """
        try:
            if input.upper() == "Y":
                self.user_will_play = True
                return True
            elif input.upper() == "N":
                return True
            else:
                raise ValueError("Invalid input. Expected 'Y' or 'N'.")
        except ValueError as e:
            print(f"Error: {e}")
            return False #This continues the main loop to give chance for the user to correct their input

