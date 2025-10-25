class IntroView:
    def __init__(self):
        pass

    def get_intro_message(self):
        intro_message = ""
        intro_message += """            ╔╦╗╦╔═╗  ╔╦╗╔═╗╔═╗  ╔╦╗╔═╗╔═╗
             ║ ║║     ║ ╠═╣║     ║ ║ ║║╣ 
             ╩ ╩╚═╝   ╩ ╩ ╩╚═╝   ╩ ╚═╝╚═╝\n"""
        intro_message += "             Welcome to CLI Tic Tac Toe!\n"
        intro_message += "            Made by Jason Nguyen (nosajeloce)\n"
        intro_message += "      =============== HOW TO PLAY ===============\n"
        intro_message += "-Requires two people to play.\n"
        intro_message += "-Pick a number 1-9 to mark a slot when it's your turn: \n\n"
        intro_message += """                    1 | 2 | 3
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9
        \n"""
        intro_message += "-First to make a line on the board with three slots wins!"
        print(intro_message)

    def ask_user_to_play(self):
        return input("Do you and your opponent want to play? [Y/N] ")
