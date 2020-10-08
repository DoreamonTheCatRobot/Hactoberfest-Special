#A small program that generates a random password with given length.

import string
import random

#The password generator , if you want symbols aswell add string.punctuation with letters and numbers
def passwordgen(input):
    print("Generating a password with "+ str(input) + " characters! ")
    password = []
    letters = string.ascii_letters
    numbers = string.digits
    password_chars = letters + numbers

    for x in range(input):
        password.append(random.choice(password_chars))
    
    print(''.join(password))

def main():
    numberofchars = int(input("How many characters do you want ? Tell me in a number: "))
    passwordgen(numberofchars)

if __name__=="__main__":
    main()