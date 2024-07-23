import pygame
import time
import random

# Initialize pygame
pygame.init()

class SnakeGame:
    def __init__(self):
        # Game settings
        self.window_x = 720
        self.window_y = 480
        self.snake_speed = 15
        self.snake_block = 10
        self.initial_obstacle_count = 5
        self.obstacle_increment_score = 100
        
        # Colors
        self.black = pygame.Color(0, 0, 0)
        self.yellow = pygame.Color(255, 255, 0)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.grey = pygame.Color(169, 169, 169)
        
        # Initialize display
        pygame.display.set_caption('Simple Snake')
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
        self.fps = pygame.time.Clock()

    def reset_game(self):
        # Initialize game state
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.fruit_position = [random.randrange(1, (self.window_x // self.snake_block)) * self.snake_block,
                               random.randrange(1, (self.window_y // self.snake_block)) * self.snake_block]
        self.fruit_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.obstacles = self.place_obstacles()

    def place_obstacles(self):
        obstacle_count = self.initial_obstacle_count + (self.score // self.obstacle_increment_score) * 5
        obstacles = []
        for _ in range(obstacle_count):
            pos = [random.randrange(1, (self.window_x // self.snake_block)) * self.snake_block,
                   random.randrange(1, (self.window_y // self.snake_block)) * self.snake_block]
            while pos in self.snake_body or pos == self.fruit_position or pos in obstacles:
                pos = [random.randrange(1, (self.window_x // self.snake_block)) * self.snake_block,
                       random.randrange(1, (self.window_y // self.snake_block)) * self.snake_block]
            obstacles.append(pos)
        return obstacles

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(self.score), True, self.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.window_x / 2, self.window_y / 4)
        self.game_window.blit(game_over_surface, game_over_rect)
        
        restart_font = pygame.font.SysFont('times new roman', 30)
        restart_surface = restart_font.render('Press R to Restart or Q to Quit', True, self.yellow)
        restart_rect = restart_surface.get_rect()
        restart_rect.midtop = (self.window_x / 2, self.window_y / 2)
        self.game_window.blit(restart_surface, restart_rect)
        
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
                        self.reset_game()
                        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    self.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    self.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    self.change_to = 'RIGHT'

        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def update_snake(self):
        if self.direction == 'UP':
            self.snake_position[1] -= self.snake_block
        if self.direction == 'DOWN':
            self.snake_position[1] += self.snake_block
        if self.direction == 'LEFT':
            self.snake_position[0] -= self.snake_block
        if self.direction == 'RIGHT':
            self.snake_position[0] += self.snake_block

        self.snake_body.insert(0, list(self.snake_position))
        if self.snake_position[0] == self.fruit_position[0] and self.snake_position[1] == self.fruit_position[1]:
            self.score += 10
            self.fruit_spawn = False
            self.obstacles = self.place_obstacles()  # Place new obstacles
        else:
            self.snake_body.pop()
        
        if not self.fruit_spawn:
            self.fruit_position = [random.randrange(1, (self.window_x // self.snake_block)) * self.snake_block,
                                   random.randrange(1, (self.window_y // self.snake_block)) * self.snake_block]
        
        self.fruit_spawn = True

    def draw_elements(self):
        self.game_window.fill(self.black)
        for pos in self.snake_body:
            pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], self.snake_block, self.snake_block))
        pygame.draw.rect(self.game_window, self.yellow, pygame.Rect(self.fruit_position[0], self.fruit_position[1], self.snake_block, self.snake_block))
        for obs in self.obstacles:
            pygame.draw.rect(self.game_window, self.grey, pygame.Rect(obs[0], obs[1], self.snake_block, self.snake_block))
        self.show_score(1, self.yellow, 'times new roman', 20)
        pygame.display.update()

    def check_game_over(self):
        if self.snake_position[0] < 0 or self.snake_position[0] > self.window_x - self.snake_block:
            return True
        if self.snake_position[1] < 0 or self.snake_position[1] > self.window_y - self.snake_block:
            return True
        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                return True
        for obs in self.obstacles:
            if self.snake_position[0] == obs[0] and self.snake_position[1] == obs[1]:
                return True
        return False

    def run(self):
        self.reset_game()
        while True:
            self.handle_events()
            self.update_snake()
            if self.check_game_over():
                self.game_over()
            self.draw_elements()
            self.fps.tick(self.snake_speed)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()