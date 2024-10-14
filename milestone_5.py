import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already guessed {guess}. Try a different letter.")
            else:
                self.list_of_guesses.append(guess)
                if guess in self.word:
                    print(f"Good guess! {guess} is in the word.")
                    for i, letter in enumerate(self.word):
                        if letter == guess:
                            self.word_guessed[i] = guess
                    self.num_letters -= 1
                else:
                    self.num_lives -= 1
                    print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")
                print(f"Current word: {' '.join(self.word_guessed)}")
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'orange', 'grape', 'mango']
    play_game(word_list)
