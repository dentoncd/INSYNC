# INSYNC

A two-player command-line guessing game written in Python. Players take turns choosing a spectrum-based category, receiving a hidden target from **1–20**, giving a clue, and seeing how closely the other player can place that clue on the spectrum.

The game combines randomization, clue-giving, and proximity-based scoring into a simple terminal experience inspired by the hit game "Wavelength".

## Features

* Two-player turn-based gameplay
* 45+ built-in category spectrums
* Random target generation from 1–20
* Animated wheel-spinning effect in the terminal
* Category reshuffling before each turn
* Custom clue words or phrases
* Proximity-based scoring
* Automatic score tracking
* First player to **10 points** wins
* No third-party Python packages required

## How to Play

Each turn follows the same basic sequence:

1. A random spectrum is displayed, such as `Slow <----> Fast`.
2. The active player can accept the category or shuffle for another one.
3. The game generates a hidden target between **1 and 20**.
4. The active player enters a clue intended to help the other player estimate the target's position on the spectrum.
5. The screen is cleared so the guessing player cannot see the target.
6. The guessing player enters a number from **1 to 20**.
7. Points are awarded based on how close the guess is to the target.
8. Players switch roles and continue until someone reaches **10 points**.

### Category Controls

| Input | Action                           |
| ----- | -------------------------------- |
| `,`   | Shuffle to a new random category |
| `/`   | Select the current category      |

## Scoring

| Distance from Target | Points |
| -------------------- | -----: |
| Exact guess          |      3 |
| 1 away               |      2 |
| 2 away               |      1 |
| 3+ away              |      0 |

The first player to reach **10 points** wins the game.

## Getting Started

### Requirements

* Python 3
* A terminal or command prompt

The project uses only Python's standard library, so no additional packages need to be installed.

### Installation

Clone the repository:

```bash
git clone https://github.com/dentoncd/INSYNC
cd INSYNC
```

### Run the Game

```bash
python main.py
```

If your system uses `python3` instead of `python`, run:

```bash
python3 main.py
```

## Example Gameplay

```text
Current topic: Slow <----> Fast
Player 1, please choose your category ('/' to select, ',' to shuffle):
/

Selected topic: Slow <----> Fast
Spinning the Wheel: 14/20

Please enter a hint word/phrase: Cheetah

Player 2, the topic is Slow <----> Fast | Hint: Cheetah
Please enter a number (1-20): 15
```

The game then compares the guess with the hidden target, awards points, displays the current score, and begins the next player's turn.

## Project Structure

```text
INSYNC/
├── main.py       # Main game logic and gameplay loop
├── test.py       # Small test for the random wheel animation
├── ideas.txt     # Original gameplay notes and project ideas
└── README.md     # Project documentation
```

## Concepts Demonstrated

This project demonstrates several core Python programming concepts:

* Variables and game state
* Lists and nested lists
* Loops and conditionals
* User input and validation
* Random number generation
* Terminal output formatting
* Score tracking
* Turn-based program flow

## Possible Improvements

Future versions could include:

* Stronger validation for guesses outside the 1–20 range
* A larger and customizable category library
* Refactored turn logic to reduce repeated code
* Configurable winning scores
* Single-player or team game modes
* A graphical or web-based interface
* Saved game statistics

## Repository

GitHub: [dentoncd/INSYNC](https://github.com/dentoncd/INSYNC)
