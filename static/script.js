let currentRow = 0;
let currentGuess = "";
let gameOver = false;


// Add a letter to the current guess
function addLetter(letter) {
    if (gameOver) return;

    if (currentGuess.length < 5) {
        currentGuess += letter.toLowerCase();
        updateBoard();
    }
}


// Remove the last letter
function removeLetter() {
    if (gameOver) return;

    currentGuess = currentGuess.slice(0, -1);
    updateBoard();
}


// Show the current guess on the board
function updateBoard() {
    for (let i = 0; i < 5; i++) {
        const tile = document.getElementById(
            `tile-${currentRow}-${i}`
        );

        if (tile) {
            tile.textContent = currentGuess[i]
                ? currentGuess[i].toUpperCase()
                : "";
        }
    }
}


// Submit the guess
async function submitGuess() {
    if (gameOver) return;

    // Make sure the guess has 5 letters
    if (currentGuess.length !== 5) {
        showMessage("Enter a 5-letter word.");
        return;
    }

    // Save the guess before changing anything
    const guessToSubmit = currentGuess;

    try {
        const response = await fetch("/guess", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                guess: guessToSubmit
            })
        });

        const data = await response.json();

        // Invalid guess
        if (!response.ok) {
            showMessage(data.error);
            return;
        }

        // Add the correct colours to the submitted row
        for (let i = 0; i < 5; i++) {
            const tile = document.getElementById(
                `tile-${currentRow}-${i}`
            );

            if (tile) {
                tile.textContent =
                    guessToSubmit[i].toUpperCase();

                tile.classList.add(data.result[i]);
            }
        }

        // Player won
        if (data.won) {
            showMessage("🎉 You won!");
            gameOver = true;
            return;
        }

        // Move to the next row
        currentRow++;

        // Clear the current guess
        currentGuess = "";

        // Player used all 6 guesses
        if (data.game_over) {
            showMessage(
                "Game over! The answer was " + data.answer
            );

            gameOver = true;
        }

    } catch (error) {
        showMessage("Something went wrong. Please try again.");
        console.error(error);
    }
}


// Display a message above the board
function showMessage(message) {
    document.getElementById("message").textContent = message;
}


// Start a completely new game
async function newGame() {
    try {
        const response = await fetch("/new-game", {
            method: "POST"
        });

        if (response.ok) {
            // Reload the page to completely reset the board
            window.location.reload();
        } else {
            showMessage("Could not start a new game.");
        }

    } catch (error) {
        showMessage("Could not start a new game.");
        console.error(error);
    }
}


// Physical keyboard support
document.addEventListener("keydown", function(event) {

    // Enter
    if (event.key === "Enter") {
        submitGuess();
    }

    // Backspace
    else if (event.key === "Backspace") {
        removeLetter();
    }

    // Letters A-Z
    else if (/^[a-zA-Z]$/.test(event.key)) {
        addLetter(event.key.toUpperCase());
    }
});