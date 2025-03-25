import pygame, sys

"""

En este documento estaran todos los componentes del motor. 

"""
        
# Clase principal del motor del juego
class SnakEngine:
    
    # def __init__(self, project, game_objs, clock, controllers, screen):
    def __init__(self, project, gameloop, clock, controllers, screen):
        self.project = project
        pygame.display.set_caption(self.project["name"])
        # self.game_objs = game_objs
        self.clock = clock
        self.controllers = controllers
        self.screen = screen

        self.gameloop = gameloop
        

    def run(self,lvl_initial):

        """

            Modificar SnakEngine.run para pasar self a load_level:

            Pasa self (la instancia de SnakEngine) a load_level.

        """
        
        

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            
            self.display_update()

            self.gameloop.load_level(lvl_initial)  # Pasa self
            self.gameloop.update()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def close_app_event_handler(self, event):

        if event.type == pygame.KEYDOWN and event.key == self.controllers["CLOSE_APP_BTN"]:
            sys.exit()
            pygame.quit()

    def display_update(self):    
        self.screen.fill(self.project["colors"]["black"])  # Limpiar la pantalla



