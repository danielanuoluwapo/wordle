import random
import urllib.request
import json

def load_api_words(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


def load_dictionary(url):
    with urllib.request.urlopen(url) as response:
        words = response.read().decode("utf-8").splitlines()
        return [word.lower() for word in words if len(word) == 5]

def is_valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    feedback = ""

    for i in range(5):
        if guess[i] == word[i]:
            feedback += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                feedback += "\033[33m" + guess[i]
            else:
                feedback += "\033[0m" + guess[i]

    return feedback + "\033[0m"

def wordle(guesses, answers):
    print("Welcome to Wordle! Get 6 chances to guess a 5-letter word.")
    secret_word = random.choice(answers)

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue
        if guess == secret_word:
            print("Congratulations! You guessed the word: ", secret_word)
            break

        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

    if attempts > max_attempts:
        print("Game over. The secret word was: ", secret_word)
    

guesses = load_dictionary("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt")
answers = load_api_words("https://random-word-api.herokuapp.com/word?length=5")

wordle(guesses, answers)

                          