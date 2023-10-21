#Importing Modules:
import random

#Creating list of fruits
word_list = ["Strawberry", "Blueberry", "Mangosteen", "Pineapple", "Apple"]
print(word_list)

#Selecting Random Fruit

word = random.choice(word_list)
print(word)

#Taking single letter guess:

guess = input("Please enter single letter guess: ")
if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")


