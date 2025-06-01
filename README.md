# **Rock, Paper, Scissors**

## Description

This is a simple **Rock, Paper, Scissors** game where the player competes against the computer. The goal is to choose between Rock, Paper, or Scissors and try to beat the opponent. The game keeps score and allows the player to keep playing until they decide to quit.

---

## Features

* **Player's Choice**: The player selects between Rock, Paper, or Scissors.
* **Computer's Choice**: The computer randomly selects between Rock, Paper, or Scissors.
* **Scoreboard**: The game keeps track of the player's and the opponent's victories.
* **Input Validation**: The game validates player input and ensures only valid options are accepted.
* **Restart or Quit**: The player can choose to continue playing or quit at any time.

---

## How to Play

1. **Start the Game**: When the game starts, the player must choose between Rock, Paper, or Scissors by typing the corresponding number:

   * **1** for Rock
   * **2** for Paper
   * **3** for Scissors
2. The computer randomly selects one of the options.
3. The game compares the choices:

   * Rock beats Scissors.
   * Scissors beats Paper.
   * Paper beats Rock.
4. The scoreboard is updated after each round.
5. The player can continue playing or quit at any time.

---

## How to Use

1. Clone or download the code from the repository.
2. Run the Python script.
3. Follow the instructions in the terminal to play.

---

## Example of Use

```bash
* Menu *
1- Start
2- Quit
R: 1

* Score *
You: 0
Opponent: 0

* Choice *
1- Rock
2- Paper
3- Scissors
R: 1

Opponent chose Scissors!
You won!

Type "1" to go back
R: 1

* Menu *
1- Start
2- Quit
R: 2

Program terminated!
```

---

## Requirements

* Python 3.x
* `random` library (included by default in Python)

---

## How to Run the Code

1. **Clone or download the project**:

   ```bash
   git clone https://github.com/jp9141joao/rock-paper-scissors.git
   ```

2. **Run the script**:

   ```bash
   python rock_paper_scissors.py
   ```
