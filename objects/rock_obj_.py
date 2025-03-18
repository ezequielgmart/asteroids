from settings import *
import pygame, random
from engine import SpriteSheetRender
from objects.bullet_obj_ import BulletObject

"""

Archivo donde se define el objeto interactivo

"""
class RockObject:

    def __init__(self, x,y,width,height, sprites_sheet, scale, frame, colour, speed = 0):
            
        # Representation
        self.frame = frame
        self.scale = scale
        self.colour = colour  # Fondo transparente en sprites
        self.renderer = SpriteSheetRender(sprites_sheet)  # Instancia del render de sprites
        self.width =  width
        self.height = height

        # localization
        self.x = x
        self.y = y
        
        # Fisicas
        # determinar el punto inicial desde donde sera disparado el proyectil para definir su trayectoria
        
        self.speed = random.random()
        self.acceleration_x = random.random()
        self.acceleration_y = random.random()

    def start(self):
        pass 

    def update(self, gameObjs):
        # Actualizar posición y renderizar
        frame_image = self.renderer.render_sprite_from_sheet(
            self.frame, self.width, self.height, self.scale, self.colour, rotation_angle=0
        )

        # movimiento de las rocas de manera aleatoria
        self.rocks_movement()
        self.borders_collition_handler()
        SCREEN.blit(frame_image, (self.x, self.y))
        pygame.draw.rect(SCREEN, PROJECT["colors"]["blue"], (self.x, self.y, self.width, self.height), 3)

        # Detectar colisiones con proyectiles
        for obj in gameObjs:
            if isinstance(obj, BulletObject):
                if self.is_colliding(obj):
                    gameObjs.remove(obj)  # Eliminar proyectil
                    gameObjs.remove(self)  # Eliminar roca
                    print("¡Colisión detectada!")
                    break  # Salir del bucle si ya se eliminó la roca

    def is_colliding(self, obj):
        # Verifica si hay superposición entre la roca y el objeto (proyectil)
        return (
            self.x < obj.x + obj.width and
            self.x + self.width > obj.x and
            self.y < obj.y + obj.height and
            self.y + self.height > obj.y
        )


        # logica para que los asteroides se muevan por si solos. 
    def rocks_movement(self):


        # quiero que el movimiento sea aleatorio.     
            self.x += self.acceleration_x
            self.y += self.acceleration_y

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
