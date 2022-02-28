#Hangman v1.0
#this is a simple hangman program to play against the computer
#Currently, the word is not shown completely when the final letter is guessed

import random
import string
from words import words

def getValidWord(words):
    word = random.choice(words) #randomly chooses a word from 'words' file
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) #letters in the word, saved as set
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() #what the user has guessed

    #getting user input
    while len(wordLetters) > 0:
        #letters used
        print("\nYou've guessed these letters: ", ' '.join(sorted(usedLetters)))
    
        #showing user the word
        word_list = [letter if letter in usedLetters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
    
        userLetter = input("Guess a letter already: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
        elif userLetter in usedLetters:
            print("You literally already guessed that...")

        else:
            print("You literally can't use that letter...")
    print("\n", word)
    print("CONGRATS!!!")
    
    
hangman()
