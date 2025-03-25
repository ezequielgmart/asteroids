# initial_level_.py
from settings import *
import pygame

class InitialLevelHandler():
    def __init__(self, x,y):
        self.x = x
        self.x = y

    def update(self, gameobjs = []):
        keys = pygame.key.get_pressed()
        if keys[CONTROLLERS["CLOSE_APP_BTN"]]:
            GAMELOOP.change_level(LEVELS['lvl_one'])

            

       