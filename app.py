from flask import Flask, render_template, request, jsonify
import random
import urllib.request
import json

app = Flask(__name__)

# Get a random 5-letter word from the API
def get_secret_word():
    url = "https://random-word-api.herokuapp.com/word?length=5"

    with urllib.request.urlopen(url) as response:
        words = json.loads(response.read())

    return words[0].lower()


# Load valid guesses from your GitHub dictionary
def load_dictionary():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

    with urllib.request.urlopen(url) as response:
        words = response.read().decode("utf-8").splitlines()

    return {
        word.lower()
        for word in words
        if len(word) == 5
    }


guesses = load_dictionary()
secret_word = get_secret_word()


def evaluate_guess(guess, word):
    result = []

    for i in range(5):
        if guess[i] == word[i]:
            result.append("correct")
        elif guess[i] in word:
            result.append("present")
        else:
            result.append("absent")

    return result


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():
    global secret_word

    data = request.get_json()
    guess = data.get("guess", "").lower()

    if len(guess) != 5:
        return jsonify({
            "error": "Guess must be 5 letters."
        }), 400

    if guess not in guesses:
        return jsonify({
            "error": "Not a valid word."
        }), 400

    result = evaluate_guess(guess, secret_word)

    won = guess == secret_word

    return jsonify({
    "guess": guess,
    "result": result,
    "won": won,
    "answer": secret_word
})


@app.route("/new-game", methods=["POST"])
def new_game():
    global secret_word

    secret_word = get_secret_word()

    return jsonify({
        "message": "New game started!"
    })


if __name__ == "__main__":
    app.run(debug=True)