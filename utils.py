import random, pygame
from settings import WINDOW_X, WINDOW_Y, SNAKE_BLOCK, POWER_UP_SPAWN_INTERVAL

def random_position():
    return [
        random.randrange(1, (WINDOW_X // SNAKE_BLOCK)) * SNAKE_BLOCK,
        random.randrange(1, (WINDOW_Y // SNAKE_BLOCK)) * SNAKE_BLOCK
    ]

def generate_power_up_position(snake_body, fruit_position, obstacles, power_up_position):
    pos = random_position()
    while pos in snake_body or pos == fruit_position or pos in obstacles or pos == power_up_position:
        pos = random_position()
    return pos

def should_spawn_power_up(last_spawn_time):
    return pygame.time.get_ticks() - last_spawn_time > POWER_UP_SPAWN_INTERVAL
