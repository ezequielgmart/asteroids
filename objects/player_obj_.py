from settings import *
import pygame, math
from engine import SpriteSheetRender
from objects.bullet_obj_ import BulletObject

"""

Archivo donde se define el objeto interactivo

"""
class ObjectPlayer:
    # Clase que representa al jugador
    def __init__(self):

        # Representation
        self.renderer = SpriteSheetRender(INSTANCES["player"]["representation"]["sprites_sheet"])  # Instancia del render de sprites
        self.colour = PROJECT["colors"]["black"]  # Fondo transparente en sprites
        self.frame = INSTANCES["player"]["representation"]["frame"]  # Fotograma actual del sprite
        
        self.width = INSTANCES["player"]["representation"]["width"]  # Ancho del sprite
        self.height = INSTANCES["player"]["representation"]["height"]  # Altura del sprite
        
        # Factor de escalado del sprite
        self.scale = INSTANCES["player"]["representation"]["scale"]  

        # localization
        self.x = INSTANCES["player"]["localization"]["x"]  
        self.y = INSTANCES["player"]["localization"]["y"]  

        # variables para Fisicas 
        self.rotation_angle = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.1
        self.friction = 0.98  # Coeficiente de fricción
        self.last_shot_time = 0

        # Bandera para controlar disparos
        self.can_shoot = True

    def update(self, gameObjs):
        # Generar el sprite desde la hoja de sprites
        frame_image = self.renderer.render_sprite_from_sheet(
            self.frame, self.width, self.height, self.scale,
            self.colour, self.rotation_angle
        )

        # Dibujar el sprite en la posición actual del jugador
        SCREEN.blit(frame_image, (self.x, self.y))

        # este rect es simpleemnte para fines de testeo
        pygame.draw.rect(SCREEN, PROJECT["colors"]["blue"], (self.x, self.y, self.width, self.height), 3)

        # funcion para controlar el movimiento.  
        self.asteroids_movement()    

        self.handle_event_shot(gameObjs)

    # detectar los eventos de disparos
    def handle_event_shot(self, gameObjs):
           
        # Controlar el movimiento de la nave y rotación
        keys = pygame.key.get_pressed()

        current_time = pygame.time.get_ticks()  # Tiempo actual en milisegundos

        if keys[CONTROLLERS['SHOOT_BTN']]:
            if current_time - self.last_shot_time > 100:  # 100ms entre disparos
                gameObjs.append(BulletObject(self.x, self.y, self.width, self.height, self.rotation_angle))
                # self.can_shoot = False
                self.last_shot_time = current_time
        
            
    # funcion para controlar la nave y que tenga un movimiento que simule el juego origiginal asteroids
    def asteroids_movement(self):
        # Controlar el movimiento de la nave y rotación
        keys = pygame.key.get_pressed()

        if keys[CONTROLLERS["UP_BTN"]] or keys[CONTROLLERS["ALT_UP_BTN"]]:
            # Aumentar la velocidad en la dirección de la inclinación
            self.velocity_x += self.acceleration * math.cos(math.radians(self.rotation_angle))
            self.velocity_y -= self.acceleration * math.sin(math.radians(self.rotation_angle))
            
            self.frame = 1
        else: 
            self.frame = 0

        if keys[CONTROLLERS["L_BTN"]] or keys[CONTROLLERS["ALT_L_BTN"]]:
            self.rotation_angle += 3
        if keys[CONTROLLERS["R_BTN"]] or keys[CONTROLLERS["ALT_R_BTN"]]:
            self.rotation_angle -= 3

        # Aplicar la fricción
        self.velocity_x *= self.friction
        self.velocity_y *= self.friction

        # Actualizar la posición basada en la velocidad
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.borders_collition_handler()

    # comportamiento del juego cuando el jugador pase los borders de la pantalla. 
    def borders_collition_handler(self):    
        
        if self.x > PROJECT["width"] + 10 :
            self.x = 0
        elif self.x < 0:
            self.x = PROJECT["width"] 
        elif self.y > PROJECT["height"] +10:
            self.y =0
        elif self.y < 0:
            self.y = PROJECT["height"]    