import pygame
from engine import GameEngine, GameLoop

project = {
    "name": 'ASTEROIDS',
    "width": 800,
    "height": 600
}

pygame.init()

SCREEN = pygame.display.set_mode((project["width"], project["height"]), pygame.OPENGL | pygame.DOUBLEBUF)
CLOCK = pygame.time.Clock()

GAME_LOOP = GameLoop(SCREEN, CLOCK)

class LevelOneManagerLevel:
    def __init__(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            print("Cambiar")
            GAME_LOOP.change_level(level_one)
        print("Initial Screen")

class LevelTwoManagerLevel:
    def __init__(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            print("Cambiar")
            GAME_LOOP.change_level(initial_screen)
        print("First level")

initial_screen = {
    "name": "InitialScreen",
    "background": {
        "bg_img": "C://Users//jerem//OneDrive//Documentos//pywebview//project//sprites//start_game.jpg"
    },
    "tiles": [],
    "interactiveObjs": [LevelOneManagerLevel()],
    "HUD": []
}

level_one = {
    "name": "LevelOne",
    "background": {
        "bg_img": "C://Users//jerem//OneDrive//Documentos//pywebview//project//sprites//final_game.jpg"
    },
    "tiles": [],
    "interactiveObjs": [LevelTwoManagerLevel()],
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
