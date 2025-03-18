from settings import *
from game_objects import RockObject, ObjectPlayer, BulletObject
from engine import SnakEngine

# todos los objetos con los que el jugador puede interactuar
GAME_OBJS = [ObjectPlayer()]

# print(INSTANCES["interactive_objs"])
for instance in INSTANCES["interactive_objs"]["rocks"]:

    GAME_OBJS.append(RockObject(instance["localization"]['x'],instance["localization"]['y'],instance["representation"]['width'],instance["representation"]['height'], instance["representation"]['sprites_sheet'], instance["representation"]['scale'], instance["representation"]['frame'], PROJECT["colors"]["black"], instance["physics"]['speed']))

class Game(SnakEngine):

    def __init__(self, project, game_objs, clock, controllers, screen):
        super().__init__(project, game_objs, clock, controllers, screen)


if __name__ == "__main__":
    # Instanciar y ejecutar el juego
    app = Game(PROJECT, GAME_OBJS, CLOCK, CONTROLLERS, SCREEN)
    app.run()
