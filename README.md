# Number Guessing Game

A simple command-line number guessing game built with Python. The computer picks a random number between 1 and 1000, and you try to guess it. After each guess you get a hint telling you whether your guess was too high or too low.

## Features

- Random number between 1 and 1000 every game
- "Too Low" / "Too High" hints after each guess
- Counts how many attempts you take
- Input validation (handles non-number entries)

## Requirements

- Python 3.6 or higher
No external libraries are needed.

## How to Run

1. Clone the repository:
   
   git clone https://github.com/shashwat207gupta-cpu/Guess-The-Number.git
   cd Guess-The-Number

3. Run the game:

   python main.py
   
## How to Play

1. The game picks a secret number between 1 and 1000.
2. Type your guess and press Enter.
3. Follow the hints and keep guessing until you find the number.
4. Try to win in as few attempts as possible!

## Example

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 1000.
Guess the number: 500
Too High
Guess the number: 250
Too Low
Guess the number: 375
Correct! You guessed it in 3 attempts.

## Project Structure

├── main.py
└── README.md

## Future Improvements

- Play again option
- Difficulty levels (easy, medium, hard)
- Limited number of attempts
- High score tracking
