let currentRow = 0;
let currentGuess = "";
let gameOver = false;


function addLetter(letter) {
    if (gameOver) return;

    if (currentGuess.length < 5) {
        currentGuess += letter.toLowerCase();
        updateBoard();
    }
}


function removeLetter() {
    if (gameOver) return;

    currentGuess = currentGuess.slice(0, -1);
    updateBoard();
}


function updateBoard() {
    for (let i = 0; i < 5; i++) {
        const tile = document.getElementById(
            `tile-${currentRow}-${i}`
        );

        tile.textContent = currentGuess[i] || "";
    }
}


async function submitGuess() {
    if (gameOver) return;

    if (currentGuess.length !== 5) {
        showMessage("Enter a 5-letter word.");
        return;
    }

    const response = await fetch("/guess", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            guess: currentGuess
        })
    });

    const data = await response.json();

    if (!response.ok) {
        showMessage(data.error);
        return;
    }

    for (let i = 0; i < 5; i++) {
        const tile = document.getElementById(
            `tile-${currentRow}-${i}`
        );

        tile.classList.add(data.result[i]);
    }

    if (data.won) {
        showMessage("🎉 You won!");
        gameOver = true;
        return;
    }

    currentRow++;
    currentGuess = "";

    if (currentRow >= 6) {
        showMessage("Game over! The answer was " + data.answer);
        gameOver = true;
    }
}


function showMessage(message) {
    document.getElementById("message").textContent = message;
}


async function newGame() {
    await fetch("/new-game", {
        method: "POST"
    });

    currentRow = 0;
    currentGuess = "";
    gameOver = false;

    document.getElementById("message").textContent = "";

    for (let row = 0; row < 6; row++) {
        for (let col = 0; col < 5; col++) {
            const tile = document.getElementById(
                `tile-${row}-${col}`
            );

            tile.textContent = "";
            tile.className = "tile";
        }
    }
}


document.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        submitGuess();
    }

    else if (event.key === "Backspace") {
        removeLetter();
    }

    else if (/^[a-zA-Z]$/.test(event.key)) {
        addLetter(event.key.toUpperCase());
    }

});