class Menu_class:
    def display_mean_menu(self):
        print("welcome to x o game:")
        print("1.start game")
        print("2.quit game")
        choice=input("enter your choice 1 or 2:")

        while True :
            if choice not in ['1','2']:
                print("invalid input , please choose 1 or 2:")
            else:
                return choice
                break
    def display_endGame_menu(self):
        print("the game is over!")
        print("1.restart game")
        print("2.quit game")
        choice=input("enter your choice 1 or 2:")

        while True :
            if choice not in ['1','2']:
                print("invalid input , please choose 1 or 2:")
            else:
                return choice
                


