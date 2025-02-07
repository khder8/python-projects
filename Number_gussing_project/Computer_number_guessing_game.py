import random

def main(higest_number):
    
    lowest_number=1
    feedback=" "
    computer_guess=random.randint(lowest_number,higest_number)
    

    while feedback!='c':
        computer_guess=random.randint(lowest_number,higest_number)

        feedback= input(f"{computer_guess}, 'h' too high , 'l' too low ,'c' correct:")
        
        if feedback=='h':
            higest_number=computer_guess-1
        elif feedback =='l':
            lowest_number=computer_guess+1
    print("well done !! correct answer!")
            
main(20)
        


