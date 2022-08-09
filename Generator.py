# this is the password generator
# it is the backend for the main file, we are passed in total length we want and then we can get a password from that 

import random
import string
import math

# let's take the password to only be 10 characters long 

alphabet = "abcdefghijklmnopqrstuvwxyz"
numerics = "0123456789"
specialChars = "@#$%&*"

print('This will be your alphanumeric password length')
passwordLength = int(input("Enter Password Length: "))

print(passwordLength)

alphabetLength = passwordLength//2
numericsLength = math.ceil(passwordLength*30/100)
specialcharsLength = passwordLength-(alphabetLength+numericsLength)

password = [] #new list has to be created to store the password

# we need to generate ranodm parts of each

def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)

