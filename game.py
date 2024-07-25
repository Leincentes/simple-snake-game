import pygame
import sys
from settings import *
from utils import random_position, generate_power_up_position, should_spawn_power_up
from display import show_score, game_over, show_menu, show_pause, draw_power_up

class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Simple Snake')
        self.game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
        self.fps = pygame.time.Clock()
        self.in_menu = True
        self.paused = False
        self.power_up_active = False
        self.power_up_start_time = 0
        self.last_power_up_spawn_time = pygame.time.get_ticks()
        self.power_up_spawn_requested = False
        self.reset_game()

    def reset_game(self):
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.fruit_position = random_position()
        self.fruit_spawn = True
        self.power_up_position = None
        self.power_up_spawn = False
        self.power_up_spawn_requested = False
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.obstacles = self.place_obstacles()
        self.snake_color = GREEN

    def place_obstacles(self):
        obstacle_count = INITIAL_OBSTACLE_COUNT + (self.score // OBSTACLE_INCREMENT_SCORE) * 5
        obstacles = []
        for _ in range(obstacle_count):
            pos = random_position()
            while pos in self.snake_body or pos == self.fruit_position or pos in obstacles:
                pos = random_position()
            obstacles.append(pos)
        return obstacles

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.in_menu:
                    if event.key == pygame.K_s:
                        self.in_menu = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                elif self.paused:
                    if event.key == pygame.K_p:
                        self.paused = False
                else:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.change_to = 'RIGHT'
                    if event.key == pygame.K_p:
                        self.paused = True
        if not self.in_menu and not self.paused:
            self.direction = self.change_to

    def update_snake(self):
        if self.direction == 'UP':
            self.snake_position[1] -= SNAKE_BLOCK
        if self.direction == 'DOWN':
            self.snake_position[1] += SNAKE_BLOCK
        if self.direction == 'LEFT':
            self.snake_position[0] -= SNAKE_BLOCK
        if self.direction == 'RIGHT':
            self.snake_position[0] += SNAKE_BLOCK

        self.snake_body.insert(0, list(self.snake_position))
        if self.snake_position == self.fruit_position:
            self.score += 10
            self.fruit_spawn = False
            self.obstacles = self.place_obstacles()
            self.power_up_spawn_requested = True  # Request to spawn a power-up
        else:
            self.snake_body.pop()

        if not self.fruit_spawn:
            self.fruit_position = random_position()
        self.fruit_spawn = True

        # Check if snake collects the power-up
        if self.power_up_position and self.snake_position == self.power_up_position:
            self.power_up_active = True
            self.power_up_start_time = pygame.time.get_ticks()
            self.power_up_spawn = False
            self.snake_color = POWER_UP_COLOR  # Change snake color when power-up is active

        # Deactivate power-up after duration
        if self.power_up_active and (pygame.time.get_ticks() - self.power_up_start_time > POWER_UP_DURATION):
            self.power_up_active = False
            self.snake_color = GREEN  # Reset snake color to default
            self.last_power_up_spawn_time = pygame.time.get_ticks()  # Update spawn time after power-up ends

        # Respawn power-up randomly if requested
        if self.power_up_spawn_requested and should_spawn_power_up(self.last_power_up_spawn_time):
            self.power_up_position = generate_power_up_position(self.snake_body, self.fruit_position, self.obstacles, self.power_up_position)
            self.power_up_spawn = True
            self.power_up_spawn_requested = False

    def draw_elements(self):
        self.game_window.fill(BLACK)
        for pos in self.snake_body:
            pygame.draw.rect(self.game_window, self.snake_color, pygame.Rect(pos[0], pos[1], SNAKE_BLOCK, SNAKE_BLOCK))
        pygame.draw.rect(self.game_window, YELLOW, pygame.Rect(self.fruit_position[0], self.fruit_position[1], SNAKE_BLOCK, SNAKE_BLOCK))
        if self.power_up_spawn:
            draw_power_up(self.game_window, self.power_up_position)
        for obs in self.obstacles:
            pygame.draw.rect(self.game_window, GREY, pygame.Rect(obs[0], obs[1], SNAKE_BLOCK, SNAKE_BLOCK))
        show_score(self.game_window, self.score)
        pygame.display.update()

    def check_game_over(self):
        if self.snake_position[0] < 0 or self.snake_position[0] >= WINDOW_X:
            return True
        if self.snake_position[1] < 0 or self.snake_position[1] >= WINDOW_Y:
            return True
        if self.snake_position in self.snake_body[1:]:
            return True
        if not self.power_up_active and self.snake_position in self.obstacles:
            return True
        return False

    def run(self):
        while True:
            self.handle_events()
            if self.in_menu:
                show_menu(self.game_window)
            elif self.paused:
                show_pause(self.game_window)
            else:
                self.update_snake()
                if self.check_game_over():
                    game_over(self.game_window, self.score)
                    self.wait_for_restart_or_quit()
                self.draw_elements()
                self.fps.tick(SNAKE_SPEED)

    def wait_for_restart_or_quit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        self.reset_game()
                        return
