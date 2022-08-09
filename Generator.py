# this is the password generator
# it is the backend for the main file, we are passed in total length we want and then we can get a password from that 

import random
import math
#import string

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

def passwordGenerator(length, array, isAlpha):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if isAlpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)

# alphabet part of the password
passwordGenerator(alphabetLength, alphabet, True)

# numeric password
passwordGenerator(numericsLength, numerics, False)

# special Character password
passwordGenerator(specialcharsLength, specialChars, False)

# suffle the generated password list. TWICE because of more 
random.shuffle(password)  
random.shuffle(password)

# convert List To string since the list is currently not a string
gen_password = ""

for i in password:
    gen_password = gen_password + str(i)
print(gen_password)