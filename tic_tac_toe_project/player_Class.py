class player_Class :

    def __init__(self):
        self.player_name= ''
        self.player_symbol=''

    def choose_name (self):
        while True:
          name= input("Enter your name:(letters only!)")
          #x=input("dasda")
          if name.isalpha():
              self.player_name=name
              break
          print("invalid name , plaese enter only letter")

    def choose_symbol(self):
        symbol = input("enter your symbol (only one leter!):")
        while True :
            if symbol.isalpha() and len(symbol)==1:
                self.player_symbol= symbol.upper()
                break
            print("invalid input , please use only one letter")

    
         



        
