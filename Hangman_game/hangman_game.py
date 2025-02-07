import maskpass


# The word to guess is represented by a row of dashes 
# representing each letter or number of the word

# If the guessing player suggests a letter which occurs in the word, 
# the other player writes it in all its correct positions

#If the suggested letter does not occur in the word,
# the other player adds (or alternatively, removes) one element of a hanged stick figure as a tally mark.
# and print out the wrong letter to use later as a reference

#the game ends once the word is guessed,
# or if the stick figure is complete — signifying that all guesses have been used.



# A varible to store the word that should be gussed
word_to_guess=""
# number of tries which represnts the six body segments in the game
souls=6
#the hidden word which represents the  word
dashes_word=[]
#the letters which are guessed worng to use as a reference
wrong_letters=[]


def start_game():
   choose_word()
   while True:
        display_info()
        guess=make_guess()
        
        check_guess(guess)
        if check_win() or check_loose():
            print("you won the game!") if check_win() else print("you lost the game!")
            display_info()
            break       

# choose_word function allow one of the 2 players to enter the word that should be gussed
#only letters are premitted
def choose_word():
    
    while True:
        global word_to_guess
        global dashes_word
        word_to_guess=maskpass.askpass(prompt="please enter the word that should be gussed (no numbers or symbols just letters) :",mask='-')
        if word_to_guess.isalpha():
            
            print("Nice on✅")
            dashes_word=['-' for l in word_to_guess]
            return
        print("unvalid word, please follow the instructions!")


def make_guess():
    while True:
        guess=input("enter your guess (one letter please): ")
        
        if guess.isalpha():
            return guess
        print("unvalid input, please follow the instructions!")


def check_guess(guess):
    
    global souls
    if guess in word_to_guess:
        print("right guess✅")
        for index ,letter in enumerate(word_to_guess):
            if guess ==letter:
                dashes_word[index]=guess
        return
        
    print("wrong guess❌")
    wrong_letters.append(guess)
    souls-=1

      
def check_win():
    if ''.join(dashes_word).isalpha():
        return True
    return False

def check_loose():
    if souls==0:
        return True
    return False


def display_info():
    info=f"""your souls: {souls}
             the word : {dashes_word}
             wrong letter : {wrong_letters} 
"""
    print(info)




start_game()


        

