#!/usr/bin/env python3
print("Type message to start encoding:")
user_input =input() #getting message that shall be encoded
enc_mes = ""
chain = ""
found = ""
count = 0
dicti = {1: 'A', 2: 'B'} # initalizing variables & dictionary
if len(user_input) == 0:
    print("Enter at least one letter!") #exit if no message is given
    exit()

for char in user_input: # iterate over every character of the message
    if char not in dicti.values():
        print("At least one character is not in the dictionary! Only 'A' and 'B' are accepted letters!") # exit if next character is not in the alphabet
        exit()
    count+=1
    chain = chain + char
    if chain not in dicti.values():
        dicti[list(dicti)[-1]+1] = chain # add chain to the dictionary, if not included
        if len(chain[:-1]) != 0:
            enc_mes = enc_mes + str(list(dicti.keys())[list(dicti.values()).index(chain[:-1])]) + " " # add the included part of chain (which is chain, just without the last character) to the dictionary
            chain = char # required, as we added chain without the char character

    if count == len(user_input):
        enc_mes = enc_mes + str(list(dicti.keys())[list(dicti.values()).index(chain)]) # add remaining list if last character has already been reached, as it would not be encoded otherwise
print("Encoded Message:", enc_mes) #output encoded message
