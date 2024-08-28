Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... class Hangman:
...     def __init__(self, word_list, num_lives=5):
...         # Initialize attributes
...         self.word_list = word_list
...         self.num_lives = num_lives
...         self.word = random.choice(word_list)
...         self.word_guessed = ['_' for _ in self.word]
...         self.num_letters = len(set(self.word))
...         self.list_of_guesses = []
... 
...     def check_guess(self, guess):
...         # Convert the guessed letter to lowercase
...         guess = guess.lower()
...         
...         # Check if the guess is in the word
...         if guess in self.word:
...             print(f"Good guess! {guess} is in the word.")
...             
...             # Replace the corresponding "_" in word_guessed with the guessed letter
...             for index, letter in enumerate(self.word):
...                 if letter == guess:
...                     self.word_guessed[index] = guess
...             
...             # Reduce the number of unique letters left to guess
...             self.num_letters -= 1
...         else:
...             # Reduce the number of lives if the guess is incorrect
...             self.num_lives -= 1
...             print(f"Sorry, {guess} is not in the word.")
...             print(f"You have {self.num_lives} lives left.")
... 
...     def ask_for_input(self):
...         while True:
...             # Ask the user to guess a letter
            guess = input("Guess a letter: ")
            
            # Check if the input is valid
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Call check_guess method and add the guess to list_of_guesses
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

# Testing the implementation

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    game = Hangman(word_list)
