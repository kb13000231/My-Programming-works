import random
from words import words
import string


def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def play_hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and you have used these letters: "
              + ' '.join(sorted(used_letters)))
        word_list = [
            letter if letter in used_letters else '-' for letter in word
            ]
        print('Current word: ' + ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f'Letter {user_letter} is not in the word')
        elif user_letter in used_letters:
            print("You just guessed that letter!")

        else:
            print('You typed in an invalid character')
    if lives == 0:
        return f"Sorry you were unable to guess the word {word} correctly\n"
    else:
        return f"Congratulations you've guessed the word {word} correctly\n"


print(play_hangman())
