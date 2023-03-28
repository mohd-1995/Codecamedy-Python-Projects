#ask user if they want to generator a password or not
#if yes, ask for a password login
#generate password
#print password

import string
import random

characters = list(string.ascii_letters + string.digits + random(symbol))

def generate_password:
    password_length = int(input("How long do you want your passowrd to be?"))
    password = []

    for i in range(password_length):
        password.append(random.choice(characters))
        random.shuffle(password)

        password = "".join(password)
        print(password)

option = input("do you want to generate a passowrd? (Yes/No)")

if option == "Yes":
    generate_password()
elif option == "No":
    print("program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()









