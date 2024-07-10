# PIG Game!

## Introduction

The Python PIG Game is a simple and fun dice game where players roll a dice and accumulate points to reach a maximum score. Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

 - If the player rolls a 1, they score nothing and it becomes the next
   player's turn.
 - If the player rolls any other number, it is added to their turn total
   and the player's turn continues.
 - If a player chooses to hold, their turn total (the sum of the dice
   rolls) is added to their score, and it becomes the next player's
   turn.

The first player to accumulate 20 or more points wins the game. The game can be played by 2 to 4 players.

## Game Rules

 - **Starting the Game**: The game starts by asking for the number of
   players (between 2 and 4). Each player starts with a score of 0.
 - **Game Play**: Players take turns rolling a dice. After each roll:
	 - If a player rolls a 1, their score for that round resets to 0, and their turn ends.
	 - If a player rolls a number between 2 and 6, the number is added to their score for that round. The player then decides whether to roll again or hold. If they hold, their round score is added to their total score.
	 - Ending the Game: The game ends when a player's total score reaches or exceeds 20 points. The game can also end if a player chooses to quit by entering 'q' during their turn.

## System Requirements

 - Python 3.6 or higher

## Getting Started

To play the game, follow these steps:

 1. Clone this repository or download the game file.
    ```bash
    git clone https://github.com/yourusername/python-pig-game.git
    ```
2. Navigate to the directory containing the game.
	```bash
	cd python-pig-game
	```
3. Run the game using Python.
	```bash
	python pig_game.py
	```
Enjoy playing the game with your friends!

## Contributions

Contributions are welcome! Please fork the repository and open a pull request with your improvements or submit an issue if you find bugs or have suggestions.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.