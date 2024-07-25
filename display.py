import pygame
from settings import YELLOW, RED, BLACK, POWER_UP_COLOR, POWER_UP_SIZE

def show_score(game_window, score):
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render(f'Score: {score}', True, YELLOW)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10)
    game_window.blit(score_surface, score_rect)

def game_over(game_window, score):
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Your Score: {score}', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (game_window.get_width() / 2, game_window.get_height() / 4)
    game_window.blit(game_over_surface, game_over_rect)

    restart_font = pygame.font.SysFont('times new roman', 30)
    restart_surface = restart_font.render('Press R to Restart or Q to Quit', True, YELLOW)
    restart_rect = restart_surface.get_rect()
    restart_rect.midtop = (game_window.get_width() / 2, game_window.get_height() / 2)
    game_window.blit(restart_surface, restart_rect)

    pygame.display.flip()

def show_menu(game_window):
    game_window.fill(BLACK)
    screen_width, screen_height = game_window.get_size()
    
    # Title
    title_font = pygame.font.SysFont('times new roman', int(screen_height * 0.1))
    title_surface = title_font.render('Simple Snake Game', True, YELLOW)
    title_rect = title_surface.get_rect(center=(screen_width / 2, screen_height * 0.2))
    game_window.blit(title_surface, title_rect)
    
    # Start and Quit options
    option_font = pygame.font.SysFont('times new roman', int(screen_height * 0.05))
    
    start_surface = option_font.render('Press S to Start', True, YELLOW)
    start_rect = start_surface.get_rect(center=(screen_width / 2, screen_height * 0.4))
    game_window.blit(start_surface, start_rect)

    quit_surface = option_font.render('Press Q to Quit', True, YELLOW)
    quit_rect = quit_surface.get_rect(center=(screen_width / 2, screen_height * 0.5))
    game_window.blit(quit_surface, quit_rect)
    
    # Instructions
    instructions_font = pygame.font.SysFont('times new roman', int(screen_height * 0.03))
    
    instructions_surface = instructions_font.render('Instructions:', True, YELLOW)
    instructions_rect = instructions_surface.get_rect(center=(screen_width / 2, screen_height * 0.65))
    game_window.blit(instructions_surface, instructions_rect)

    controls_surface = instructions_font.render('- Use Arrow Keys to Move', True, YELLOW)
    controls_rect = controls_surface.get_rect(center=(screen_width / 2, screen_height * 0.7))
    game_window.blit(controls_surface, controls_rect)
    
    food_surface = instructions_font.render('- Eat the Yellow Fruit to Score', True, YELLOW)
    food_rect = food_surface.get_rect(center=(screen_width / 2, screen_height * 0.75))
    game_window.blit(food_surface, food_rect)
    
    obstacles_surface = instructions_font.render('- Avoid Grey Obstacles', True, YELLOW)
    obstacles_rect = obstacles_surface.get_rect(center=(screen_width / 2, screen_height * 0.8))
    game_window.blit(obstacles_surface, obstacles_rect)
    
    power_up_surface = instructions_font.render('- Collect Power-Ups for Special Abilities:', True, YELLOW)
    power_up_rect = power_up_surface.get_rect(center=(screen_width / 2, screen_height * 0.85))
    game_window.blit(power_up_surface, power_up_rect)

    power_up_1_surface = instructions_font.render('  - Change Snake Color', True, YELLOW)
    power_up_1_rect = power_up_1_surface.get_rect(center=(screen_width / 2, screen_height * 0.9))
    game_window.blit(power_up_1_surface, power_up_1_rect)

    power_up_2_surface = instructions_font.render('  - Become Invulnerable for 10 Seconds', True, YELLOW)
    power_up_2_rect = power_up_2_surface.get_rect(center=(screen_width / 2, screen_height * 0.95))
    game_window.blit(power_up_2_surface, power_up_2_rect)

    pygame.display.flip()

def show_pause(game_window):
    font = pygame.font.SysFont('times new roman', 50)
    pause_surface = font.render('Game Paused', True, YELLOW)
    pause_rect = pause_surface.get_rect()
    pause_rect.midtop = (game_window.get_width() / 2, game_window.get_height() / 4)
    game_window.blit(pause_surface, pause_rect)

    resume_font = pygame.font.SysFont('times new roman', 30)
    resume_surface = resume_font.render('Press P to Resume', True, YELLOW)
    resume_rect = resume_surface.get_rect()
    resume_rect.midtop = (game_window.get_width() / 2, game_window.get_height() / 2)
    game_window.blit(resume_surface, resume_rect)

    pygame.display.flip()
    
def draw_power_up(game_window, position):
    pygame.draw.rect(game_window, POWER_UP_COLOR, pygame.Rect(position[0], position[1], POWER_UP_SIZE, POWER_UP_SIZE))
