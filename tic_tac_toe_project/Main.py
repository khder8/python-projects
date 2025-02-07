from player_Class import player_Class
from Board_class import Board_class
from Menu_class import Menu_class
import os
def clear_screen():
        os.system('cls')
class Main :
    def __init__(self):
        self.palyer=[player_Class(),player_Class()]
        self.board=Board_class()
        self.menu=Menu_class()
        self.current_player_index=0
    
    def start_game(self):
        choice=self.menu.display_mean_menu()
        if choice =='1':
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    
    def play_game(self):
         while True:
            self.paly_turn()
            if self.check_win() or self.check_draw():
                if self.check_win():
                    self.current_player_index=1-self.current_player_index
                    
                    print(f"congrats {self.palyer[self.current_player_index].player_name} you have won the game!")
                if self.check_draw():
                    print("the resutl is Draw ! , no one won the game!")
                choice=self.menu.display_endGame_menu()
                if choice =='1':
                    self.restart_game()
                else:
                    self.quit_game()
                    break




    def restart_game(self):
        self.board.reset_board()

    def check_win(self):
        row_counter=3
        column_counter=1

        for i in range(3):
            if self.board.board[0+row_counter]==self.board.board[1+row_counter] ==self.board.board[2+row_counter]:
                return  True 
            elif self.board.board[0+column_counter]==self.board.board[3+column_counter]==self.board.board[6+column_counter]:
                 return  True 
            elif self.board.board[0]==self.board.board[4] ==self.board.board[8]:
                return True 
            elif self.board.board[3]==self.board.board[4]==self.board.board[6]:
                return True
            i+=1
        return False
                
    def check_draw(self):
        if len([True for item in self.board.board if item.isalpha()])==9:
            return True
        return False
              
    def paly_turn(self):
        self.board.display_board()
        while True :
            #we did not check if the entered value is not a number !
            choice=input(f"please{ self.palyer[self.current_player_index].player_name} choose a number from 1-9 to put your symbol there:")
            if choice  in [f"{x}" for x in range(1,10)]:
             if  self.board.update_board(choice,self.palyer[self.current_player_index].player_symbol):
                 print("your choice is valid")
                 self.board.display_board()
                 self.current_player_index=1-self.current_player_index
                 
                 break
             print("already filled place , plase chooose another one!")
            print("unvalid place,please choose another one!")

            
    def setup_players(self):
        for number,player in enumerate( self.palyer,start=1):
            print(f"Player {number} , enter your details:")
            #x=input("entertx")
            player.choose_name()
            player.choose_symbol()
            clear_screen()
    def quit_game(self):
         print("Thank you for playing!")


main=Main()
main.start_game()





