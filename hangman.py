import random
from word_list import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


    lives = 7

    while(len(word_letters) > 0 and lives>0):
        #letters used

        print("\nLives left: " + str(lives))
        print("You have used these letters: ", " ".join(used_letters))

        #current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print("You have already used that letter")
        else:
            print("That is an invalid letter")

    #game ends if either len(word_letters) ==0 0 or lives == 0
    if lives == 0:
        print("\nYou died. The word was", word.upper())
    else:
        print("\nYou have guessed the word ", word.upper(), "!")
        

if __name__ == "__main__":
    hangman()