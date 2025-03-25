from settings import *
# import pygame, random
# from objects.interactive.bullet_obj_ import BulletObject
from objects.interactive.rock_class import RockClass
"""

Archivo donde se define el objeto interactivo

"""


class BigRockObject(RockClass):
    def __init__(self, x, y):
        renderer = INSTANCES["bigrock"]["representation"]["sprites_sheet"]
        colour = PROJECT["colors"]["black"]
        # frame = INSTANCES["bigrock"]["representation"]["frame"]
        width = INSTANCES["bigrock"]["representation"]["width"]
        height = INSTANCES["bigrock"]["representation"]["height"]
        scale = INSTANCES["bigrock"]["representation"]["scale"]

        frame_x = INSTANCES["bigrock"]["representation"]["frame_x"]
        frame_y = INSTANCES["bigrock"]["representation"]["frame_y"]

        
        velocity_x = 0
        velocity_y = 0.5

        super().__init__(x, y, velocity_x, velocity_y, renderer, colour, frame_x, frame_y ,width, height, scale)  # Corrección aquí
        
