import random


#generate a random number between 1 and 10
number_to_guess=random.randint(1,10)
#define the user number of tries
number_of_tries=3

while True:

    if number_of_tries==0:
        print("you run out of tries!")
        break
    # the user input
    user_guess=int(input(f"guess the number which is between 1 and 10 (you have {number_of_tries} tries!):  "))
    

    if user_guess>number_to_guess:
        print("Too High!")
    elif user_guess<number_to_guess:
        print("Too Low")
    else:
        print("Correct! Nice Guess!")
        break
    number_of_tries-=1


