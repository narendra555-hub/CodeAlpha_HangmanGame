
# CodeAlpha: Hangman Game (Task 1)

A clean, text-based terminal implementation of the classic Hangman word-guessing game built using Python. This project was developed as part of the CodeAlpha Python Programming Internship.

## 🚀 Features
- **Randomized Gameplay**: Selects a random secret word from a predefined list for every new game round.
- **Visual Game State**: Tracks and prints your current correct guesses, hidden characters, and remaining attempt counters in real-time.
- **Input Sanitization**: Includes robust validation logic to filter out numbers, multi-character strings, or duplicate inputs.
- **Strict Attempt Limits**: Adheres to a maximum threshold of 6 incorrect guesses before triggering a game-over condition.

## 🛠️ Key Concepts Used
- `random` module for item selection.
- Control flow statements (`while`, `if-elif-else`).
- Complex data structures (`lists`, `sets` for tracked elements).
- Pure text-based console Input/Output optimization.

## 📦 How to Run
1. Ensure you have Python 3 installed on your machine.
2. Clone this repository or download the script file.
3. Open your terminal, navigate to the folder, and run:
   ```bash
   python hangman.py
   ```
