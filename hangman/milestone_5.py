import random



#Creating list of fruits:
word_list = ["Strawberry", "Blueberry", "Mangosteen", "Pineapple", "Apple"]
word_list =  [item.lower() for item in word_list]


#Selecting Random Fruit:


#Defining the Hangman Class:

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    #Checks the guess is alphabetical and 1 char. in length:

    def guess_input(self):
        while True:
            guess = input("Please guess a letter: ").lower()
            if  guess in self.list_of_guesses:
                print("You already guessed that")
            elif guess.isalpha() and len(guess) == 1:
                if guess not in self.list_of_guesses:
                    self.list_of_guesses.append(guess)
                return guess
                         
            else:
                print("Invalid guess, please try again")

    #Checking if the guessed letter is in the selected word:
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess {guess} is in the word ")
            for idx, character in enumerate(self.word):
                if character == guess:
                    
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
            
        else:
            print(f"Sorry, {guess} is not in the word")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives remaining")


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You lost!. The word was {game.word}!")
            break
        elif game.num_letters > 0:
            guessed_letter = game.guess_input()
            game.check_guess(guessed_letter)
            print(game.word_guessed)
            print(f"There are {game.num_letters} different letters remaining!")
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations! You won the game")
            break

play_game(word_list)