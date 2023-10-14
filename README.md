# Rock, Paper, Scissors Game

Welcome to the Rock, Paper, Scissors (RPS) game!
This simple text-based game allows you to play the classic RPS game against a computer.

## Installation

Before you start playing, make sure you have the necessary dependencies installed.
You can install them using the provided `requirements.txt` file. To do so, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage

To play the game, you need to provide a set of arguments through the command-line interface. You must pass an odd number of unique moves (choices) that are used in the game. The game will ensure the moves are valid, and if they are not, it will display an informative error message.

Here's an example of how to start the game with valid arguments:

```bash
python main.py Rock Paper Scissors
```

In this example, we've provided three valid moves: "Rock," "Paper," and "Scissors."

The game will then generate a cryptographically secure random key with a length of at least 256 bits.
It will make its own move, calculate the HMAC of its move with the generated key, and show the HMAC to you.

After this, you will receive a menu that allows you to make your move.
The menu will display options like "1 - Rock," "2 - Paper," and so on.
You can choose by entering the number associated with your choice.

The game will determine the winner, show the computer's move, and display the original key.

Please make sure to provide a valid set of moves when starting the game, and enjoy playing Rock, Paper, Scissors securely!

## Additional Classic Menu
If you want to start the game with the additional classic menu, you can do so by providing the -cmenu argument at the end of your command. For example:

```bash
python main.py Rock Paper Scissors -cmenu
```

### Enjoy the game and have fun playing Rock, Paper, Scissors!

## License
This project is licensed under the MIT License. See the LICENSE file for details.