# Othello Game with AI

This project is an implementation of the classic board game Othello (also known as Reversi) with a graphical user interface and an AI opponent. The game is built using Python and the Tkinter library for the GUI.

## Features

- Full implementation of Othello game rules
- Graphical user interface for easy gameplay
- AI opponent with adjustable difficulty levels (Easy, Medium, Hard)
- Alpha-beta pruning algorithm for efficient AI decision making
- Real-time disc count display
- Option to restart the game

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code.
2. Ensure you have Python installed on your system.
3. No additional libraries need to be installed as the game uses only built-in Python libraries.

## How to Play

1. Run the `othello.py` file
2. The game window will open, showing the Othello board.
3. Black always moves first. Click on a valid move (highlighted in light green) to place your disc.
4. The AI (White) will automatically make its move after you.
5. Continue playing until no more moves are possible.
6. The player with the most discs of their color on the board at the end wins.

## Game Controls

- Click on a valid square to make a move.
- Use the "Difficulty" menu to change the AI's difficulty level.
- Use the "Play Again" option in the menu to restart the game.
- Use the "Exit" option in the menu to close the game.

## AI Difficulty Levels

- Easy: AI looks 1 move ahead
- Medium: AI looks 3 moves ahead
- Hard: AI looks 5 moves ahead

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/khaledsa1ah/Othello/issues) if you want to contribute.

