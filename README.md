# Wordle Game

This is a simple Wordle game I built using Python, Flask, HTML, CSS and JavaScript.

The goal is to guess the hidden word within 6 tries.

## What I Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Features

- Choose a word length from 4 to 8 letters
- 6 attempts for each game
- Green means the letter is in the correct position
- Yellow means the letter is in the word but in the wrong position
- Gray means the letter is not in the word
- On-screen keyboard
- Physical keyboard support
- New Game button
- Each player gets their own game
- Repeated letters are scored using Wordle-style rules

## How to Run It

### 1. Create a virtual environment

In the project folder, run:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 2. Install the requirements

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

### 4. Open the game

Open this in your browser:

```text
http://127.0.0.1:5000
```

## How to Play

1. Choose how many letters you want the word to have.
2. Type a word.
3. Press **Enter**.
4. Use the colours as clues.
5. Try to find the word within 6 attempts.

## Project Files

```text
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates
│   └── index.html
└── static
    ├── script.js
    └── style.css
```

## What I Learned

While building this project, I practiced:

- Python
- Flask routes
- Flask sessions
- HTML and CSS
- JavaScript
- Working with APIs/data from the internet
- Sending data between the frontend and backend
- JSON
- Game logic
- Handling repeated letters


## Note

The game uses the English word list from the `dwyl/english-words` GitHub repository. An internet connection is needed when the app starts so the word list can be loaded.

This is a learning project.
