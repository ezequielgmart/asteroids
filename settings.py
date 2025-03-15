from engine import GameLoop

import pygame

project = {
    "name": 'ASTEROIDS',
    "width": 800,
    "height": 600
}

WINDOW_WIDTH = project["width"]
WINDOW_HEIGHT = project["height"]

pygame.init()

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()

GAME_LOOP = GameLoop(SCREEN, CLOCK)

# Controller settings 

# up
UP_BTN = pygame.K_w 
ALT_UP_BTN = pygame.K_UP

# right 
R_BTN = pygame.K_d 
ALT_R_BTN = pygame.K_RIGHT


# left
L_BTN = pygame.K_a 
ALT_L_BTN = pygame.K_LEFT

# shoot
SHOOT_BTN = pygame.K_SPACE

# start game
START_GAME_BTN = pygame.K_b


