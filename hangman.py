# assignment: programming assignment 1
# author: Aryan Sahni
# date: 04/17/2023
# file: hangman.py is a program that runs methods import_dictionary and get_options
# input: The code prompts the user to choose the game settings and after that the letters of the word that is to be guessed.
# output: The code outputs a certain lettered word chosen by the user which is to be guessed. With each correct guess of letter, the letter is revealed, and soon the word is revealed.
from random import choice, random, randint

dictionary_file = "dictionary_short.txt"

def import_dictionary(filename):
    dictionary = {Lenlist: [] for Lenlist in range(1, 13)}
    try:
        f = open(filename, "r")
        max_size = 12
        for line in f:
            word = line.strip()
            word_length = len(word)
            if word_length > 0:
                if word_length < max_size:
                    dictionary[word_length].append(word)
                else:
                    dictionary[max_size].append(word)

        return dictionary
    except Exception as e:
        print(e)


def print_dictionary(dictionary):
    pass



def get_game_options():
    try:
        size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]: \n"))
        print(f"The word size is set to {size}.")
        if size > 12 or size < 3:
            size = randint(3, 12)
            print(f'A dictionary word of {size} letters will be chosen')

    except:
        print("A dictionary word of any size will be chosen.")
        size = randint(3, 12)
    try:

        lives = int(input("Please choose a number of lives [1 - 10, default 5]: \n"))
        if lives > 10 or lives < 1:
            lives = randint(1, 10)
        print(f'You have {lives} lives.')
    except:
        print("You have 5 lives.")
        lives = 5
    return (size, lives)


def uppercase(letter):
    return letter.capitalize()


def lowercase(letter):
    return letter.lower()


def print_status(lives_remaining, letters_used, word, num_lives):
    lives_status = ''
    for i in range(num_lives - lives_remaining):
        lives_status += 'X'
    for i in range(lives_remaining):
        lives_status += 'O'
    print('Letters chosen:', end=' ')
    formatted_letters_used = list(map(uppercase, letters_used))
    print(*formatted_letters_used, sep=', ')
    letters_status = ''
    for letter in word.lower():
        if letter in list(map(lowercase, letters_used)) or letter == '-':
            letters_status += letter.capitalize()
        else:
            letters_status += '__'
        letters_status += ' '

    print('{} lives: {} {}'.format(letters_status, lives_remaining, lives_status))




if __name__ == '__main__':

    dictionary = import_dictionary(dictionary_file)


    print('Welcome to the Hangman Game!')

    play = True
    while play:

        word_size, num_lives = get_game_options()


        possible_words = dictionary[word_size]
        word = choice(possible_words)
        display_word = word

        word.replace('-', '.')
        letters_chosen = []
        lives_remaining = num_lives
        print_status(lives_remaining, letters_chosen, display_word, num_lives)

        while lives_remaining > 0:

            guess = ''

            while len(guess) != 1 or not guess.isalpha() or guess in letters_chosen:
                print('Please choose a new letter >')
                guess = input()


                if guess is not None:
                    if guess in letters_chosen:
                        print('You have already chosen this letter.')

            if guess not in word:
                lives_remaining -= 1
                print('You guessed wrong, you lost one life.')
            else:
                print('You guessed right!')
            letters_chosen.append(guess)

            print_status(lives_remaining, letters_chosen, word, num_lives)
            if all(guessed in list(map(lowercase, letters_chosen)) for guessed in word.replace('-', '').lower()):
                print('Congratulations!!! You won! The word is {}!'.format(word.upper()))
                print('Would you like to play again [Y/N]?')
                break

        if lives_remaining == 0:
            print('You lost! The word is {}!'.format(word.upper()))
            print('Would you like to play again [Y/N]?')


        play_input = input()

        play = play_input == 'Y' or play_input == 'y'


    print('Goodbye!')
