# Famous Snake Game

Welcome to the **Famous Snake Game**, a classic game implemented in Python as part of a project for a Udemy course! The goal is simple: control the snake, eat the food, and grow longer. The game keeps track of the highest score, so challenge yourself to beat it every time you play!

## Table of Contents

- [Game Features](#game-features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [File Overview](#file-overview)
- [Contributing](#contributing)
- [License](#license)

## Game Features

- Classic snake game mechanics
- Option to choose from three difficulty levels: Easy, Medium and Hard
- Keeps track of the player's highest score
- Randomly positioned food for the snake to eat
- Snake grows longer with each food item consumed
- Game over screen when the snake collides with itself or the boundaries
- Written using Python's Turtle graphics module for simplicity

## Technologies
This project is implemented with the following technologies:

- **Python 3**: The core programming language used for development.
- **Turtle Module**: A standard Python library used for creating graphics and simple animations, ideal for games like this.
- **Text File (data.txt)**: Used for persisting data, such as the high score, across game sessions.


## Installation

### Prerequisites

Ensure you have **Python 3.x** installed on your machine. You will also need the `turtle` module, which is a standard Python library.

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/Famous-Snake-Game.git
    cd Famous-Snake-Game
    ```

2. Run the game:

    ```bash
    python main.py
    ```

## How to Play

1. **Control the Snake**: 
   - Use the **arrow keys** on your keyboard to navigate the snake.
   - The snake will move in the direction of the arrow keys (up, down, left, right).

2. **Goal**:
   - Eat the food that randomly appears on the screen.
   - The more food you eat, the longer the snake becomes.

3. **Game Over**:
   - The game ends when the snake runs into the screen boundary or collides with itself.

4. **Score**:
   - Try to beat the highest score, which is saved and displayed during gameplay.

## File Overview

- **main.py**: The main script that runs the game, initializes the screen, and handles game flow.
- **body.py**: Contains the `Body` class, which represents the snake itself, handling its movement and collision logic.
- **food.py**: Contains the `Food` class, which randomly generates food for the snake to eat.
- **scoreboard.py**: Contains the `Scoreboard` class, which displays the current score and keeps track of the high score.
- **data.txt**: A simple text file where the highest score is stored.

## Contributing

Feel free to fork the repository, submit issues, and create pull requests if you'd like to contribute to this project. Any suggestions or improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgement
This project is a part of the course "100 Days of Code: The Complete Python Pro Bootcamp", taught by Dr. Angela Yu on Udemy.

## Author
- [mdgolamfardin](https://github.com/mdgolamfardin)
