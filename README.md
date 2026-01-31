# Rock, Paper, Scissors Game 🪨📃✂️

A simple command-line implementation of the classic Rock, Paper, Scissors game with support for both single-player and multiplayer modes.

## Features

- **Player vs Machine Mode**: Play against a computer opponent with random selections
- **Player vs Player Mode**: Two players can play against each other with hidden input
- **Hidden Input**: In multiplayer mode, player inputs are hidden from the terminal for fair gameplay
- **Interactive UI**: User-friendly terminal interface with clear instructions

## Requirements

- Python 3.x
- No external dependencies (uses only standard library modules)

## How to Run

```bash
python main.py
```

## Game Rules

- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- If both players select the same option, it's a **tie**

## Game Modes

### 1. Player vs Machine

- Enter your name
- Choose: 1 for Rock, 2 for Paper, 3 for Scissors
- The machine makes a random selection
- Winner is announced

### 2. Player vs Player

- Both players enter their names
- Each player makes their selection (hidden from opponent)
- The selections are not displayed on screen for fair gameplay
- Winner is announced

### 3. Exit

- Close the game

## Technical Details

- Uses the `getpass` module to hide player inputs in multiplayer mode
- Random selection for machine opponent using Python's `random` module
- Simple conditional logic to determine winners

## Future Enhancements

- Score tracking across multiple rounds
- Better input validation
- More detailed game statistics
