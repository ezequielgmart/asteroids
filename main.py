from settings import *
from engine.snake_engine_ import SnakEngine

class Game(SnakEngine):
    def __init__(self, project, gameloop,clock, controllers, screen):
        super().__init__(project, gameloop,clock, controllers, screen)

if __name__ == "__main__":
    app = Game(PROJECT, GAMELOOP, CLOCK, CONTROLLERS, SCREEN)
    app.run(LEVELS["initial"])