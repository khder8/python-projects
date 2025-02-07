import string
import random


#generting a string which contains all the english letters in lower case
letters=string.ascii_lowercase
#generting a string which contains all the digits 0>>9
numbers=string.digits
#generting a string which contains special characters
spec_Chars=string.punctuation

def password_generator():
    
    # ask the user to input the length of the password
    password_lenght=int(input("how long the password is?"))
    # the list which will contain the password
    password_list=[]


    # the number of the elements of each category in the password
    number_of_letters= int (0.5 * password_lenght)
    number_of_digits= int(0.3 * password_lenght)
    number_of_special_chars= password_lenght-(number_of_digits+number_of_letters)


    info=[{number_of_letters:letters},{number_of_digits:numbers},{number_of_special_chars:spec_Chars}]

    # genereting the passowrd
    
    for item in info:
        for lenght in item:
            for i in range(lenght):
                index=random.randint(0,len(item[lenght])-1)
                char=item[lenght][index]
                choice=random.randint(0,1)
                if char.isalpha():
                    if choice==1:
                        char.upper()
                password_list.append(char)
                random.shuffle(password_list)

    
    # converting the list into string
    
    password=""
    
    for item in password_list:
        password+=item
    print(password)
            

password_generator()








