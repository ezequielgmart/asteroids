from settings import *
import pygame
from engine.render_sprites_sheet_ import MultipleSpriteSheetRender


"""

Archivo donde se define el objeto interactivo

en este caso este es un modelo para hacer varias rocas pero de diferentes tipos que tienen el mismo comportamiento

"""
class RockClass:

    def __init__(self, x,y, velocity_x, velocity_y, renderer, colour, frame_x, frame_y, width, height,scale):
        
        # Representation
        self.renderer = MultipleSpriteSheetRender(renderer)  # Instancia del render de sprites
        self.colour = colour  # Fondo transparente en sprites
        self.frame_x = frame_x 
        self.frame_y = frame_y
        
        self.width = width # Ancho del sprite
        self.height = height # Altura del sprite
        
        # Factor de escalado del sprite
        self.scale = scale

        # localization
        self.x = x
        self.y = y
        
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        # Fisicas
        # determinar el punto inicial desde donde sera disparado el proyectil para definir su trayectoria
        
        # self.speed = random.random()
        # self.acceleration_x = random.random()
        

    def start(self):
        pass 

    def update(self):
        # Actualizar posición y renderizar
        frame_image = self.renderer.render_sprite_from_sheet(
            self.frame_x, self.frame_y, self.width, self.height, self.scale, self.colour, rotation_angle=0
        )

        # movimiento de las rocas de manera aleatoria
        self.rocks_movement()
        self.borders_collition_handler()
        SCREEN.blit(frame_image, (self.x, self.y))
        # pygame.draw.rect(SCREEN, PROJECT["colors"]["blue"], (self.x, self.y, self.width, self.height), 3)


    # logica para que los asteroides se muevan por si solos. 
    def rocks_movement(self):
            
        # quiero que el movimiento sea aleatorio.     
        self.x += self.velocity_x
        self.y += self.velocity_y

    # comportamiento del juego cuando el objeto pase los borders de la pantalla. 
    def borders_collition_handler(self):    
            
            if self.x > PROJECT["width"] + 10 :
                self.x = 0
            elif self.x < 0:
                self.x = PROJECT["width"] 
            elif self.y > PROJECT["height"] +10:
                self.y =0
            elif self.y < 0:
                self.y = PROJECT["height"]   
