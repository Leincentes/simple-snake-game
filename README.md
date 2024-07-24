# Simple Snake Game

## Overview

A simple Snake game implemented in Python using the Pygame library. This game demonstrates basic game development concepts including user input handling, game state management, and rendering graphics.

## Features

- Classic Snake game mechanics
- Scoring system
- Obstacles that increase in number as the player scores more points
- Restart or quit options on game over

## Prerequisites

- Python 3.x
- Pygame library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/snake-game.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd snake-game
    ```

3. **Install dependencies**:
    ```bash
    pip install pygame
    ```

## How to Run

1. **Run the game**:
    ```bash
    python snake_game.py
    ```

2. **Control the Snake**:
    - **UP Arrow**: Move Up
    - **DOWN Arrow**: Move Down
    - **LEFT Arrow**: Move Left
    - **RIGHT Arrow**: Move Right

3. **Game Over**:
    - After a game over, press **R** to restart or **Q** to quit.

## Game Mechanics

- **Objective**: Eat the fruit to score points and grow the snake.
- **Obstacles**: Randomly placed obstacles appear each time a fruit is eaten. The number of obstacles increases every 100 points.
- **Game Over**: The game ends if the snake collides with the walls, itself, or an obstacle.

## Code Structure

- **`snake_game.py`**: Contains the main game logic including game state management, event handling, and rendering.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by classic Snake games.
- Uses Pygame library for game development.

