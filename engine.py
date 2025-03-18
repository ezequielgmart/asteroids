import pygame, sys
from settings import *
# from game_objects import ObjectPlayer

# Enfoque simplificado para construir el juego antes de modularizarlo y convertirlo en un motor.
class SpriteSheetRender:
    def __init__(self, image_sheet_path):
        self.sheet = pygame.image.load(image_sheet_path).convert_alpha()

    def render_sprite_from_sheet(self, frame, width, height, scale, colour, rotation_angle):
        # Crear una superficie para almacenar el sprite
        image = pygame.Surface((width, height), pygame.SRCALPHA)

        x = frame * width  # Calcular posición del sprite en la hoja

        # Dibujar la parte seleccionada de la hoja de sprites en la nueva superficie
        image.blit(self.sheet, (0, 0), (x, 0, width, height))

        # Escalar la imagen al tamaño deseado
        image = pygame.transform.scale(image, (width * scale, height * scale))

        # Aplicar rotación
        image = pygame.transform.rotate(image, rotation_angle)

        # Establecer un color transparente
        image.set_colorkey(colour)

        return image
    

class SnakEngine:
    # Clase principal del motor del juego
    def __init__(self, project, game_objs, clock, controllers, screen):
        self.project = project
        pygame.display.set_caption(self.project["name"])
        self.game_objs = game_objs
        self.clock = clock
        self.controllers = controllers
        self.screen = screen

    def run(self):

        running = True

        while running:
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # # Pasar eventos a los objetos relevantes
                # for game_obj in self.game_objs:
                #     if isinstance(game_obj, ObjectPlayer):

                #         # a las acciones que necesiten un evento. Como disparar
                #         game_obj.handle_event(event, self.game_objs)

                # observar evento de presionar cierre app
                self.close_app_event_handler(event)

            self.global_update()

            # Actualizar el estado de los objetos
            for game_obj in self.game_objs:
                game_obj.update(event, self.game_objs)

            # Actualizar pantalla
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def close_app_event_handler(self, event):

        if event.type == pygame.KEYDOWN and event.key == self.controllers["CLOSE_APP_BTN"]:
            sys.exit()
            pygame.quit()

    # eventos que quiera comprobar a nivel global como por ejemplo que una bala choque con 
    def global_update(self):

        self.display_update() 


    def display_update(self):    
        self.screen.fill(self.project["colors"]["black"])  # Limpiar la pantalla



