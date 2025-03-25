import pygame

from engine.gameloop_ import GameloopHandler

# PG = pygame

PROJECT = {
    "name": 'ASTEROIDS',
    "width": 800,
    "height": 600,
    "colors":{
        "black":(0,0,0),
        "red":(250,0,0),
        "green":(0,250,0),
        "blue":(0,0,250),
        "white":(250,250,250)
    }
}

FRAMES = {"rocks":{
    "big": {"x": 0, "y": 0, "width": 183, "height": 132},
    "medium": {"x": 0, "y": 132, "width": 146, "height": 120},
    "small": {"x": 0, "y": 252, "width": 79, "height": 80},
    "mini": {"x": 0, "y": 332, "width": 43, "height": 54},
}
}
# Objetos que puedo utilizar para construir los niveles 
INSTANCES = {
    "player":{
    "representation":{
        "sprites_sheet":"./sheets/player_sheet.png",
        "frame":0,
        "width":92,
        "height":82,
        "scale":1,

    }},
    "bullet":{
    "representation":{
        "sprites_sheet":"./sheets/player.png",
        "frame":4,
        "width":20,
        "height":20,
        "scale":1,

    }},
    "bigrock":{
    "representation":{
        "sprites_sheet":"./sheets/rocks_sheet.png",
        "frame_x": 0, 
        "frame_y": 0,
        "width":183,
        "height":132,
        "scale":1,

    }},
    "midrock":{
    "representation":{
        "sprites_sheet":"./sheets/rocks_sheet.png",
        "frame_x": 0, 
        "frame_y": 252,
        "width":146,
        "height":120,
        "scale":1,

    }
    
}


}
pygame.init()

SCREEN = pygame.display.set_mode((PROJECT["width"], PROJECT["height"]))
CLOCK = pygame.time.Clock()


# Controller settings 
CONTROLLERS = {
"UP_BTN":pygame.K_w,
        "ALT_UP_BTN":pygame.K_UP,
        "R_BTN":pygame.K_d,
        "ALT_R_BTN":pygame.K_RIGHT,
        "L_BTN":pygame.K_a,
        "ALT_L_BTN":pygame.K_LEFT,
        "SHOOT_BTN":pygame.K_SPACE, 
        "START_GAME_BTN":pygame.K_b,
        "CLOSE_APP_BTN":pygame.K_ESCAPE} 


LEVELS = {
    "initial":"./levels/initial.json",
    "lvl_one":"./levels/lvl_one.json"
}

GAMELOOP = GameloopHandler(SCREEN,PROJECT['width'],PROJECT['height'])