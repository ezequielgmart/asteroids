from settings import *
import pygame, math
from engine.render_sprites_sheet_ import SpriteSheetRender

"""

Archivo donde se define el objeto interactivo

"""
class BulletObject:
    def __init__(self, player_x,player_y,player_width,player_height, player_rotation_angle):
            
            self.engine = None  # Inicializa el atributo engine
            # Representation
            self.frame = INSTANCES["bullet"]["representation"]["frame"]
            self.scale = INSTANCES["bullet"]["representation"]["scale"]
            self.colour = PROJECT["colors"]["black"]  # Fondo transparente en sprites
            self.rotation_angle = player_rotation_angle
            self.renderer = SpriteSheetRender(INSTANCES["bullet"]["representation"]["sprites_sheet"])  # Instancia del render de sprites
            self.width =  INSTANCES["bullet"]["representation"]["width"]
            self.height = INSTANCES["bullet"]["representation"]["height"]
            
            # Fisicas
            # determinar el punto inicial desde donde sera disparado el proyectil para definir su trayectoria
            
            self.speed = 5
            self.set_bullet_origin(player_x,player_y,player_width,player_height,self.rotation_angle)

    def start(self):
        pass
    
    def update(self):
        # Generar el sprite desde la hoja de sprites
        frame_image = self.renderer.render_sprite_from_sheet(
            self.frame, self.width, self.height, self.scale,
            self.colour, self.rotation_angle
        )

        # Dibujar el sprite en la posición actual del jugador
        SCREEN.blit(frame_image, (self.x, self.y))

        # self.borders_collition_handler()
        pygame.draw.rect(SCREEN, PROJECT["colors"]["green"], (self.x, self.y, self.width, self.height), 3)

        # Actualizar la posición del proyectil
        self.x += self.velocity_x
        self.y += self.velocity_y
    
    def set_bullet_origin(self, player_x, player_y, player_width, player_height, player_angle):
    # Calcular el centro del sprite del jugador como punto inicial del proyectil
        self.x = player_x + player_width / 2
        self.y = player_y + player_height / 2

        # Convertir el ángulo a radianes (para cálculos trigonométricos)
        self.angle = math.radians(player_angle)

        # Ajustar el origen del proyectil para salir desde el "frente" del sprite según el ángulo
        offset_distance = player_width / 2  # Distancia desde el centro hacia el borde del sprite
        self.x += offset_distance * math.cos(self.angle)
        self.y -= offset_distance * math.sin(self.angle)

        # Calcular la velocidad inicial basada en la dirección de rotación
        self.velocity_x = math.cos(self.angle) * self.speed
        self.velocity_y = -math.sin(self.angle) * self.speed
