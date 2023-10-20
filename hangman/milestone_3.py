import random

#Checks the guess is alphabetical and 1 char. in length:
def guess_input():
    while True:
        guess = input("Please guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            return guess
            
        else:
            print("Invalid guess, please try again")

guessed_letter = guess_input().lower()

#Creating list of fruits:
word_list = ["Strawberry", "Blueberry", "Mangosteen", "Pineapple", "Apple"]
word_list =  [item.lower() for item in word_list]

#Selecting Random Fruit:
word = random.choice(word_list)

#Checking if the guessed letter is in the selected word:

def check_guess(guessed_letter):
    if guessed_letter in word:
        print(f"Good guess {guessed_letter} is in the word ")
    else:
        print(f"Sorry, {guessed_letter} is not in the word")

check_guess(guessed_letter)
