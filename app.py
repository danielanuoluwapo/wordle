from flask import Flask, render_template, request, jsonify, session
import random
import urllib.request
import json

app = Flask(__name__)

# Needed for sessions
app.secret_key = "wordle-secret-key"


# Get a random 5-letter word from the Random Word API
def get_secret_word():
    url = "https://random-word-api.herokuapp.com/word?length=5"

    with urllib.request.urlopen(url) as response:
        words = json.loads(response.read())

    return words[0].lower()


# Load the dictionary from GitHub
def load_dictionary():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

    with urllib.request.urlopen(url) as response:
        words = response.read().decode("utf-8").splitlines()

    return {
        word.lower()
        for word in words
        if len(word) == 5 and word.isalpha()
    }


guesses = load_dictionary()


# Start a new game
def new_game():
    secret_word = get_secret_word()

    # Make sure the API word is accepted by our dictionary
    while secret_word not in guesses:
        secret_word = get_secret_word()

    session["secret_word"] = secret_word
    session["attempts"] = 0


@app.route("/")
def home():
    if "secret_word" not in session:
        new_game()

    if "attempts" not in session:
        session["attempts"] = 0

    return render_template("index.html")


# Check the letters in a guess
def evaluate_guess(guess, word):
    result = ["absent"] * 5

    # Keep track of letters that haven't been matched
    remaining_letters = list(word)

    # First check for correct letters
    for i in range(5):
        if guess[i] == word[i]:
            result[i] = "correct"
            remaining_letters[i] = None

    # Then check for letters in the wrong position
    for i in range(5):
        if result[i] == "correct":
            continue

        if guess[i] in remaining_letters:
            result[i] = "present"

            # Remove the matched letter
            # so it can't be counted twice
            index = remaining_letters.index(guess[i])
            remaining_letters[index] = None

    return result


@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    guess = data.get("guess", "").lower()

    secret_word = session["secret_word"]
    attempts = session["attempts"]

    # Check the guess is exactly 5 letters
    if len(guess) != 5:
        return jsonify({
            "error": "Guess must be 5 letters."
        }), 400

    # Check the guess is a valid English word
    if guess not in guesses:
        return jsonify({
            "error": "Not a valid word."
        }), 400

    # Don't allow more than 6 guesses
    if attempts >= 6:
        return jsonify({
            "error": "Game over."
        }), 400

    # Check the guess
    result = evaluate_guess(guess, secret_word)

    # Increase attempts
    attempts += 1
    session["attempts"] = attempts

    # Check if the player won
    won = guess == secret_word

    # Game ends if they win or use all 6 guesses
    game_over = won or attempts >= 6

    response = {
        "guess": guess,
        "result": result,
        "won": won,
        "game_over": game_over
    }

    # Only reveal the answer when the game is actually over
    if game_over:
        response["answer"] = secret_word

    return jsonify(response)


# Start a new game
@app.route("/new-game", methods=["POST"])
def start_new_game():
    new_game()

    return jsonify({
        "message": "New game started!"
    })


if __name__ == "__main__":
    app.run(debug=True)