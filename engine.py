import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class CustomComponent:
    def __init__(self, game_object):
        self.game_object = game_object

    def update(self):
        pass

class GameObject:
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def update(self):
        for component in self.components:
            component.update()
            
# Debe haber una clase encargada de mostrar graficos en pantalla            
class Render():
    
    def __init__(self):
        self.texture = 0
    
    def render_level_background(self, param_bg_img):
        
        bg_img = pygame.image.load(param_bg_img)
        bg_data = pygame.image.tostring(bg_img, "RGB", 1)

        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, bg_img.get_width(), bg_img.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, bg_data)
    
    def render_background(self):
            
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(-1, -1)
        glTexCoord2f(1, 0)
        glVertex2f(1, -1)
        glTexCoord2f(1, 1)
        glVertex2f(1, 1)
        glTexCoord2f(0, 1)
        glVertex2f(-1, 1)
        glEnd()

        glDisable(GL_TEXTURE_2D)
        
class LevelHandler:
    def __init__(self, level_json_file, screen, clock):
        self.level_config = level_json_file  # Archivo JSON de configuración del nivel
        self.screen = screen  # Pantalla del juego
        self.clock = clock  # Reloj del juego
        self.texture = None

        self.start()

    def start(self):
        """
        Métodos que se ejecutan al iniciar el nivel.
        Ejemplo: renderizar el fondo del nivel.
        """
        print(self.level_config['name'])
       
        Render().render_level_background(self.level_config['background']['bg_img'])
        
    def render_background(self):
       pass

    def update(self):
        """
        Métodos que se ejecutan en cada frame del nivel.
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Render().render_background()

        for interactiveObj in self.level_config['interactiveObjs']:
            interactiveObj.update()

        self.update_screen_frame()

    def update_screen_frame(self):
        """
        Actualiza la pantalla y controla la velocidad del juego.
        """
        pygame.display.flip()
        self.clock.tick(60)

    def change_level(self, new_level):
        """
        Cambia al nuevo nivel y reinicia.
        """
        self.level_config = new_level
        self.start()

class InputEventsHandler:
    def __init__(self):
        self.input_handler = pygame

class GameLoop:
    def __init__(self, screen, clock):
        self.level = None  # Nivel actual del juego
        self.screen = screen  # Pantalla del juego
        self.clock = clock  # Reloj del juego

    def run(self):
        if self.level is not None:
            self.level.update()

    def load_level(self, level_config_file):
        """
        Carga un nivel desde un archivo de configuración.
        """
        self.level = LevelHandler(level_config_file, self.screen, self.clock)

    def change_level(self, new_level_config_file):
        """
        Cambia a un nuevo nivel.
        """
        self.load_level(new_level_config_file)

class GameEngine:
    def __init__(self, project_name, screen, clock):
        pygame.display.set_caption(project_name)  # Establece el título de la ventana del juego
        self.screen = screen  # Pantalla del juego
        self.clock = clock  # Reloj del juego

        glClearColor(0.1, 0.2, 0.2, 1)  # Color de fondo de OpenGL

        self.game_loop = GameLoop(self.screen, self.clock)  # Instancia del bucle principal del juego

    def run_game(self, initial_level):
        """
        Método principal para ejecutar el juego.
        """
        self.game_loop.load_level(initial_level)  # Carga el nivel inicial

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.game_loop.run()

        pygame.quit()
