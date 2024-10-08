# Tic Tac Toe Game

## Description
This Tic Tac Toe game allows players to compete against each other or against a computer opponent. It features a simple and intuitive interface to play the classic game on a 3x3 board, with options for human vs. human (hot seat) or human vs. computer gameplay.

## Features
- Play against another human or the computer.
- Automatic win detection for rows, columns, and diagonals.
- Handles draws when no moves are left.
- User-friendly input prompts and error handling.

## Installation
To run the game, follow these steps:

 **Clone the repository**:   

   `git clone https://github.com/Tais19991/Python-Projects/edit/main/Tic_Tac_Toe_game`   
   `cd Tic_Tac_Toe_game`

## Usage
Run the game:  
`python main.py`

1. Choose the game mode:

- 1 - for Hot Seat (play with a nearby human).
- 2 - for playing against the computer.

2. Select your symbol (X or O) for the game.
3. Input your move by specifying the row and column (0-2) when prompted.
4. The game continues until a player wins or the game ends in a draw.

## Code Structure
The code is organized into three main classes:

- Board: Manages the game board, including displaying the board, checking for moves, and determining win/draw conditions.
- Player: Represents a player in the game, allowing for manual and automatic moves.
- Game: Controls the flow of the game, player selection, and gameplay mechanics.

## Testing
Unit tests are included to verify the functionality of the Board and Player classes. To run the tests, execute:

`python -m unittest discover`

## License
This project is licensed under the MIT License.
