# Wordle Game

This is a simple Wordle game I built using Python, Flask, HTML, CSS, and JavaScript.

The goal of the game is to guess the hidden 5-letter word within 6 tries.

## What I Used

* Python
* Flask
* HTML
* CSS
* JavaScript

## Features

* Guess a 5-letter word
* You get 6 attempts
* Green means the letter is in the correct position
* Yellow means the letter is in the word but in the wrong position
* Gray means the letter is not in the word
* On-screen keyboard
* You can also use your computer keyboard
* New Game button

## How to Run It

### 1. Download the project

Download or clone this repository and open the project folder.

### 2. Install Flask

Open your terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### 3. Run the app

Run:

```bash
python app.py
```

### 4. Open the game

After running the app, open this in your browser:

```text
http://127.0.0.1:5000
```

## How to Play

1. Type a 5-letter word.
2. Press **Enter**.
3. Check the colours of the letters.
4. Use the clues to guess the correct word.
5. You have 6 attempts.

## Project Files

```wordle
├── app.py
├── requirements.txt
├── README.md
├── templates
│   └── index.html
└── static
    ├── script.js
    └── style.css
```

## What I Learned

While building this project, I practiced:

* Python
* Flask
* Working with routes
* HTML and CSS
* JavaScript
* Sending data between the frontend and backend
* Using APIs
* Working with JSON
* Basic game logic



## Author

Built as a personal learning project.
