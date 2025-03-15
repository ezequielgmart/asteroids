import pygame
import math
from settings import * 
from engine import GameEngine, SpritesSheetRender, Render

class BulletManager():

    def __init__(self, x,y):
        
        self.sheet_path = 'sheets/player.png'
        self.speed = 10
        self.direction = 0
        self.x = x
        self.y = y
        self.frame = 4
        self.width = 20
        self.height = 20
        self.frame = 4
        self.scale = 1
        self.colour = (0,0,0)
        self.rotation_angle = 0

    def start(self):
        pass
    
    def update(self):
        
        sprite_renderer = SpritesSheetRender(self.sheet_path)
        frame_image = sprite_renderer.render_sprite_from_sheet(self.frame, self.width, self.height, self.scale, self.colour, self.rotation_angle)
        Render().render_obj(frame_image, SCREEN, self.x, self.y)   

        self.x += self.speed 
        self.y -= self.speed 

    
# Clase encargada de la interactividad del jugador
class PlayerManager:
    def __init__(self):
        self.sheet_path = 'sheets/player.png'
        self.x = int(WINDOW_WIDTH/2)
        self.y = int(WINDOW_HEIGHT/2)
        self.speed = 0
        self.rotation_angle = 15
        self.colour = (0, 0, 0)
        self.frame = 1
        self.width = 20
        self.height = 20
        self.scale = 2
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.1
        self.friction = 0.98  # Coeficiente de fricción

        self.bullets = []

    def start(self):
        pass

    def update(self):
        sprite_renderer = SpritesSheetRender(self.sheet_path)
        frame_image = sprite_renderer.render_sprite_from_sheet(self.frame, self.width, self.height, self.scale, self.colour, self.rotation_angle)
        Render().render_obj(frame_image, SCREEN, self.x, self.y)

       # funcion para controlar el movimiento.  
        self.asteroids_movement()    

            
    # funcion para controlar la nave y que tenga un movimiento que simule el juego origiginal asteroids
    def asteroids_movement(self):
        # Controlar el movimiento de la nave y rotación
        keys = pygame.key.get_pressed()

        if keys[UP_BTN]:
            # Aumentar la velocidad en la dirección de la inclinación
            self.velocity_x += self.acceleration * math.cos(math.radians(self.rotation_angle))
            self.velocity_y -= self.acceleration * math.sin(math.radians(self.rotation_angle))
        

        if keys[L_BTN]:
            self.rotation_angle += 3
        if keys[R_BTN]:
            self.rotation_angle -= 3

        # Aplicar la fricción
        self.velocity_x *= self.friction
        self.velocity_y *= self.friction

        # Actualizar la posición basada en la velocidad
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.borders_collition_handler()

        self.shoot(self.x,self.y)

    # funcion cuando el jugador dispare
    def shoot(self, x,y):

        keys = pygame.key.get_pressed()
        
        if keys[SHOOT_BTN]:

            bullet = BulletManager(x,y)
            bullet.start()
            self.bullets.append(bullet)

        for bullet in self.bullets: 

            bullet.update()

    # comportamiento del juego cuando el jugador pase los borders de la pantalla. 
    def borders_collition_handler(self):    
        
        if self.x > 800:

            self.x = 0
        elif self.x < 0:
            self.x = 800
        elif self.y > 600:
            self.y =0
        elif self.y < 0:
            self.y = 600             
        

class LevelOneManagerLevel:
    def __init__(self):
        print("Initial Screen")

        
    def update(self):
        keys = pygame.key.get_pressed()
        # if keys[START_GAME_BTN]:
        #     print("Cambiar")
        #     GAME_LOOP.change_level(initial_screen)
        

class LevelTwoManagerLevel:
    def __init__(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[START_GAME_BTN]:
            print("Cambiar")
            GAME_LOOP.change_level(initial_screen)

# initial_screen = {
#     "name": "InitialScreen",
#     "background": {
#         "bg_img": "../assets/images/start_game.jpg"
#     },
#     "tiles": [],
#     "interactiveObjs": [LevelOneManagerLevel()],
#     "HUD": []
# }

# level_one = {
#     "name": "LevelOne",
#     "background": {
#         "bg_img": "../assets/images/final_game.jpg"
#     },
#     "tiles": [],
#     "interactiveObjs": [LevelTwoManagerLevel(),PlayerManager()],
#     "HUD": []
# }

initial_screen = {
    "name": "LevelOne",
    "background": {
        "bg_img": "../assets/images/black-background.png"
    },
    "tiles": [],
    "interactiveObjs": [LevelTwoManagerLevel(),PlayerManager()],
    "HUD": []
}

class Game(GameEngine):
    def __init__(self, project_name, screen, clock):
        super().__init__(project_name, screen, clock)

    def run_game(self, initial_level):
        GAME_LOOP.load_level(initial_level)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            GAME_LOOP.run()

if __name__ == '__main__':
    try:
        game = Game(project["name"], SCREEN, CLOCK)
        game.run_game(initial_screen)
    except Exception as e:
        print(e)
