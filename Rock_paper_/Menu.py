class Menu:
    
    def main_menu(self):
        enternce_message="""
        welcom to the Rock, Paper , Scissors Game!
        please choose an option:
         1-start the game
         2-quit the game
         your choice: """
        while True:
            enterance_choice=input(enternce_message)
            if enterance_choice not in ['1','2']:
                print("invalid choice! please follow the instructions!")
            else:
                return True if enterance_choice=='1' else  False
    

    def end_menu(self):
        quit_mesaage="""please choose an option:
         1-restart the game
         2-quit the game
         your choice:"""
        
        while True:
            end_choice=input(quit_mesaage)
            if end_choice not in ['1','2']:
                print("invalid choice! please follow the instructions!")
            else:
                return True if end_choice=='1' else  False







