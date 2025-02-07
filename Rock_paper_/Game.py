import Player
import Menu

class Game:
    
    def __init__(self):
        self.players=[Player.player(),Player.player()]
        self.menu=Menu.Menu()
        self.current_player=0

    

    def start_game(self):
            choice=self.menu.main_menu()
            if choice ==1:
                self.Player_names()
                self.play_game()
            else:
                self.quit_game()

    def play_game(self):
       
        while True:
            self.play_turn()
            self.check_result()
            if self.check_winner():
                print(f"{self.check_winner()} Won the game !!!")
                if self.menu.end_menu():
                     self.restart_game()
                else:
                     self.quit_game()
                     return




    def Player_names(self):
        for num ,player in enumerate(self.players):
                    print(f"player{ num+1}:",end=" ")
                    player.choose_name()
   
   
    def play_turn(self):
         for player in self.players:
            player.make_choice()
            self.current_player=1-self.current_player
    
    def check_result(self):
         win_options={('r','p'):'p',('r','s'):'r',('p','s'):'r'}
         p0=self.players[0]
         p1=self.players[1]


        #check the draw status:
         if p0.choice==p1.choice:
              print(f"Its a DRAW, both players choosed{p0.choice}")
              return
        #check the win status:
         for option in win_options:
              if  p0.choice in option and p1.choice in option:
                    if p0.choice==win_options[option]:
                         print(f"{p0.name} has won !!!")
                         p0.change_score()
                    else:
                         print(f"{p1.name} has won !!!")
                         p1.change_score()
         print(f"The score now is: {p0.name}:{p0.score} - {p1.name}:{p1.score}   ")
    
    def check_winner(self):
         for player in self.players:
              if player.score==3:
                   return player.name
              
    def quit_game(self):
         print("thank you for playing")
    
    def restart_game(self):
         for player in self.players:
              player.score=0
                
         
                         
                   
        

G=Game()
G.start_game()