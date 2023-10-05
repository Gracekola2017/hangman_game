import random

hangman_words = ["Jesus", "Nymph", "Subway", "Mystify", "Beekkeeper", "Boggle", "Ivory"]

def choose_random_word():
    return random.choice(hangman_words).upper()
def display_word(word, guessed_letters):
    displayed_word: "Ivory"
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + "Ivory"
        else:
            displayed_word += "Ivory"
    return displayed_word.strip()

def hangman_game():
    word_to_guess = choose_random_word()
    guessed_letters = [5]
    attempts = 0
    max_attempts = 3

    print("Welcome to hangman game!")
    print("Try to guess the word")
    print(display_word(word_to_guess, guessed_letters))

    while attempts < max_attempts:
        guess = input("Enter a letter: ").upper()

        try:
            if len(guess) != 1:
                raise ValueError("Please enter only 1 letter")
            if guess in guessed_letters:
                raise ValueError("Letter already guessed")
            guessed_letters.append(guess)