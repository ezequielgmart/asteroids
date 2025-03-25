from settings import *
# import pygame, random
# from objects.interactive.bullet_obj_ import BulletObject
from objects.interactive.rock_class import RockClass
"""

Archivo donde se define el objeto interactivo

"""


class MidRockObject(RockClass):
    def __init__(self, x, y, velocity_x, velocity_y):
        renderer = INSTANCES["midrock"]["representation"]["sprites_sheet"]
        colour = PROJECT["colors"]["black"]
        # frame = INSTANCES["midrock"]["representation"]["frame"]
        width = INSTANCES["midrock"]["representation"]["width"]
        height = INSTANCES["midrock"]["representation"]["height"]
        scale = INSTANCES["midrock"]["representation"]["scale"]

        frame_x = INSTANCES["midrock"]["representation"]["frame_x"]
        frame_y = INSTANCES["midrock"]["representation"]["frame_y"]

        velocity_x = velocity_x
        velocity_y = velocity_y
        super().__init__(x, y, velocity_x, velocity_y, renderer, colour, frame_x, frame_y ,width, height, scale)  # Corrección aquí
        
