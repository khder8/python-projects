import maskpass
class player :

    #player class constructor 
    def __init__(self):
        self.name=" "
        self.choice=" "
        self.score=0

    def choose_name(self):
       
        while True:
            name_choice=input("please enter your name (only letters please): ")
            if name_choice.isalpha():
                self.name=name_choice
                print("the name was saved successfuly✅")
                break
            print("invalied name!❌")
        

    
    def make_choice(self):
        
        while True:
            game_choice=maskpass.askpass(prompt=f"please {self.name} enter your choice r>>(rock), p>>(paper), s>>(Scissors):",mask='*')
            if game_choice in['r','p','s']:
                print("Good choice!,its saved!✅")
                self.choice=game_choice
                return
            print("unvalid choice please follow the instruction!❌")
        

    def change_score(self):
        self.score+=1


