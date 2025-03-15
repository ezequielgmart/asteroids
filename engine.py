import pygame

# Clase para definir componentes personalizados que se pueden agregar a un GameObject
class CustomComponent:
    def __init__(self, game_object):
        self.game_object = game_object

    def update(self):
        pass

# Clase para definir un objeto del juego
class GameObject:
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def update(self):
        for component in self.components:
            component.update()


# Clase para encargarse del renderizado del fondo del nivel
class Render:
    
    def __init__(self):
        self.bg_img = None
    
    # Cargar y almacenar la imagen de fondo del nivel
    def render_level_background(self, param_bg_img):
        self.bg_img = pygame.image.load(param_bg_img)
        
    # Renderizar la imagen de fondo en la pantalla
    def render_background(self, screen):
        screen.blit(self.bg_img, (0, 0))

    # Metodo para mostrar un objeto encima del background. 
    def render_obj(self, obj, screen, x, y):    
        
        screen.blit(obj, (x,y))


class SpritesSheetRender:
    def __init__(self, image_sheet_path):
        self.sheet = pygame.image.load(image_sheet_path).convert_alpha()

    def render_sprite_from_sheet(self, frame, width, height, scale, colour, rotation_angle):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        x = frame * width
        
        # Dibujar la parte seleccionada de la hoja de sprites en el surface
        image.blit(self.sheet, (0, 0), (x, 0, width, height))

        # Escalar la imagen al tamaño deseado
        image = pygame.transform.scale(image, (width * scale, height * scale))

        # Aplicar la rotación
        image = pygame.transform.rotate(image, rotation_angle)

        # Agregar transparencia
        image.set_colorkey(colour)

        return image
    

# Clase para manejar los niveles del juego
class LevelHandler:
    def __init__(self, level_json_file, screen, clock):
        self.level_config = level_json_file
        self.screen = screen
        self.clock = clock
        self.render = Render()
        
        # self.sprites_sheet_full = pygame.image.load('assets\\sheets\\asteroids_ss.png').convert_alpha()  
        self.start()

    def start(self):
        print(self.level_config['name'])
        self.render.render_level_background(self.level_config['background']['bg_img'])
        
        
    def render_background(self):
        self.render.render_background(self.screen)

    def update(self):
        self.screen.fill((0, 0, 0))  # Limpiar la pantalla con color negro
        self.render_background()

        # Actualizar todos los objetos interactivos del nivel
        for interactiveObj in self.level_config['interactiveObjs']:
            interactiveObj.update()

        self.update_screen_frame()

    def update_screen_frame(self):
        pygame.display.flip()  # Actualizar la pantalla
        self.clock.tick(60)  # Controlar la velocidad del juego a 60 FPS

    def change_level(self, new_level):
        self.level_config = new_level
        self.start()

# Clase para manejar eventos de entrada
class InputEventsHandler:
    def __init__(self):
        self.input_handler = pygame

# Clase para manejar el bucle principal del juego
class GameLoop:
    def __init__(self, screen, clock):
        self.level = None
        self.screen = screen
        self.clock = clock

    def run(self):
        if self.level is not None:
            self.level.update()

    def load_level(self, level_config_file):
        self.level = LevelHandler(level_config_file, self.screen, self.clock)

    def change_level(self, new_level_config_file):
        self.load_level(new_level_config_file)

# Clase principal del motor del juego
class GameEngine:
    def __init__(self, project_name, screen, clock):
        pygame.display.set_caption(project_name)
        self.screen = screen
        self.clock = clock
        self.game_loop = GameLoop(self.screen, self.clock)

    def run_game(self, initial_level):
        self.game_loop.load_level(initial_level)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.game_loop.run()

        pygame.quit()

# # Ejemplo de uso
# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((200, 600))
#     clock = pygame.time.Clock()
    #  level_config = {
#         'name': 'Nivel 1',
#         'background': {'bg_img': 'ruta/a/imagen_de_fondo.png'},
#         'interactiveObjs': []
#     }

#     engine = GameEngine("Mi Proyecto", screen, clock)
#     engine.run_game(level_config)
