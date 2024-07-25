# Simple Snake Game

## Overview

A simple Snake game implemented in Python using the Pygame library. This game demonstrates basic game development concepts including user input handling, game state management, and rendering graphics.

## Features

- Classic Snake game mechanics with power-ups
- Scoring system
- Obstacles that increase in number as the player scores more points
- Power-ups that grant temporary invulnerability and the ability to destroy obstacles
- Restart or quit options on game over
- Responsive display with a menu, pause functionality, and detailed instructions

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
    - **P**: Pause/Resume the game
    - **Q**: Quit the game

3. **Game Over**:
    - After a game over, press **R** to restart or **Q** to quit.

4. **Power-ups**:
    - Power-ups appear randomly and grant temporary invulnerability, allowing the snake to destroy obstacles.
    - The snake's color changes when a power-up is active.

## Game Mechanics

- **Objective**: Eat the fruit to score points and grow the snake.
- **Obstacles**: Randomly placed obstacles appear. The number of obstacles increases every 100 points.
- **Power-ups**: Spawn randomly and provide temporary invulnerability, changing the snake’s color and allowing it to destroy obstacles.
- **Game Over**: The game ends if the snake collides with the walls, itself, or an obstacle (unless invulnerable).

## Code Structure

- **`snake_game.py`**: Contains the main game logic including game state management, event handling, rendering, and power-up mechanics.
- **`settings.py`**: Contains configuration settings such as colors, sizes, and game parameters.
- **`utils.py`**: Includes utility functions for random position generation and power-up spawning.
- **`display.py`**: Manages rendering of game elements, menus, and UI components.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by classic Snake games.
- Uses Pygame library for game development.
