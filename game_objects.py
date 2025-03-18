from settings import *
import pygame, math, random
from engine import SpriteSheetRender

"""
Archivo donde se definen los objetos que se utilizaran para interactuar en el juego
"""

class BulletObject:
    def __init__(self, player_x,player_y,player_width,player_height, player_rotation_angle):
            
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
    
    def update(self, event,gameObjs):
        # Generar el sprite desde la hoja de sprites
        frame_image = self.renderer.render_sprite_from_sheet(
            self.frame, self.width, self.height, self.scale,
            self.colour, self.rotation_angle
        )

        # Dibujar el sprite en la posición actual del jugador
        SCREEN.blit(frame_image, (self.x, self.y))

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

    def update(self, event, gameObjs):
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

        self.handle_event_shot(event, gameObjs)

    # detectar los eventos de disparos
    def handle_event_shot(self, event, gameObjs):
           
        # if event.type == pygame.KEYDOWN and event.key == CONTROLLERS['SHOOT_BTN']:
        #     if self.can_shoot:
        #         gameObjs.append(BulletObject(self.x,self.y,self.width, self.height, self.rotation_angle))


        #         self.can_shoot = False
        #         print("shotting")

        # if event.type == pygame.KEYUP and event.key == CONTROLLERS['SHOOT_BTN']:
        #     self.can_shoot = True

        #     self.last_shot_time = 0

        # Controlar el movimiento de la nave y rotación
        keys = pygame.key.get_pressed()

        current_time = pygame.time.get_ticks()  # Tiempo actual en milisegundos

        if keys[CONTROLLERS['SHOOT_BTN']]:
            if current_time - self.last_shot_time > 100:  # 300ms entre disparos
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

        # if self.frame == 1:
        #     self.frame = 0       

        self.borders_collition_handler()

        # self.shoot(self.x,self.y)

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

class RockObject:

    def __init__(self, x,y,width,height, sprites_sheet, scale, frame, colour, speed):
            
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

    def update(self, event, gameObjs):
        # Generar el sprite desde la hoja de sprites
        frame_image = self.renderer.render_sprite_from_sheet(
            self.frame, self.width, self.height, self.scale,
            self.colour, rotation_angle =0
        )
        
        self.rocks_movement()
        self.borders_collition_handler()

        # Dibujar el sprite en la posición actual
        SCREEN.blit(frame_image, (self.x, self.y))

        # este rect es simpleemnte para fines de testeo
        pygame.draw.rect(SCREEN, PROJECT["colors"]["blue"], (self.x, self.y, self.width, self.height), 3)


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
