from settings import *
import random
from objects.interactive.bullet_obj_ import BulletObject
from objects.interactive.big_rock_obj_ import BigRockObject
from objects.interactive.mid_rock_obj_ import MidRockObject
from objects.interactive.rock_class import RockClass
from objects.interactive.player_obj_ import ObjectPlayer
from objects.hud.score_text import ScoreTxtObject

class OneLevelHandler:
    def __init__(self):
        self.score = 0
        self.player_lives = 3  # Inicializar con 3 vidas
        self.player_has_loose = False
        self.player_last_colission = None

    def update(self):
        # Detectar colisiones de rocas proyectiles
        self.bullet_collides_with_rock_event(RockClass)

        # Detectar colisiones con jugador
        if self.player_collides_with_rock_event():
            # Si el jugador colisiona y no hay tiempo de colisión previo, registrar el tiempo
            if self.player_last_colission is None:
                self.player_last_colission = pygame.time.get_ticks()

        # Si hay un tiempo de colisión registrado, manejar el respawn
        if self.player_last_colission is not None:
            self.respawn_player()

    def bullet_collides_with_rock_event(self, rockInstance):
        # Llama a la función genérica para colisiones de objetos con rocas
        self.obj_collides_with_rock_event(BulletObject, rockInstance)

    def obj_collides_with_rock_event(self, objInstance, rockInstance):
        # Itera sobre todos los objetos en el juego
        for obj in GAMELOOP.game_objects:
            # Si el objeto es del tipo especificado (proyectil)
            if isinstance(obj, objInstance):
                # Itera sobre todas las rocas en el juego
                for rock in GAMELOOP.game_objects:
                    # Si la roca es del tipo especificado
                    if isinstance(rock, rockInstance):
                        # Si hay colisión entre el objeto y la roca
                        if self.is_colliding(obj, rock):
                            # Eliminar el proyectil y la roca
                            GAMELOOP.remove_obj(obj)
                            GAMELOOP.remove_obj(rock)
                            # Aumentar el puntaje
                            self.add_score_for_big()
                            # Si la roca era grande, crear rocas medianas resultantes
                            if isinstance(rock, BigRockObject):
                                self.create_resulting_mid_rocks(rock.x, rock.y)
                            break  # Salir del bucle interno

    def player_loose_live(self):
        # Reduce las vidas del jugador y muestra el recuento
        self.player_lives -= 1
        print(f"Vidas restantes: {self.player_lives}")

    def add_score_for_big(self):
        # Aumenta el puntaje por destruir una roca grande y actualiza el HUD
        self.score += 10
        self.update_score_hud()

    def add_score_for_mid(self):
        # Aumenta el puntaje por destruir una roca mediana y actualiza el HUD
        self.score += 5
        self.update_score_hud()

    def update_score_hud(self):
        # Actualiza el texto del puntaje en el HUD
        for obj in GAMELOOP.hud:
            if isinstance(obj, ScoreTxtObject):
                obj.text_to_show = str(self.score)

    def player_collides_with_rock_event(self):
        # Itera sobre todos los objetos en el juego
        for obj in GAMELOOP.game_objects:
            # Si el objeto es el jugador
            if isinstance(obj, ObjectPlayer):
                # Itera sobre todas las rocas en el juego
                for rock in GAMELOOP.game_objects:
                    # Si la roca es grande o mediana
                    if isinstance(rock, MidRockObject) or isinstance(rock, BigRockObject):
                        # Si hay colisión entre el jugador y la roca
                        if self.is_colliding(obj, rock):
                            # Eliminar el jugador y la roca
                            GAMELOOP.remove_obj(obj)
                            GAMELOOP.remove_obj(rock)
                            # Aumentar el puntaje
                            self.add_score_for_big()
                            # Si la roca era grande, crear rocas medianas resultantes
                            if isinstance(rock, BigRockObject):
                                self.create_resulting_mid_rocks(rock.x, rock.y)
                            # Reduce las vidas del jugador
                            self.player_loose_live()
                            return True  # Indica que hubo colisión
        return False  # Indica que no hubo colisión

    def is_colliding(self, obj, rock):
        # Verifica si hay colisión entre dos objetos
        return (
            rock.x < obj.x + obj.width and
            rock.x + rock.width > obj.x and
            rock.y < obj.y + obj.height and
            rock.y + rock.height > obj.y
        )

    def respawn_player(self):
        # Maneja el respawn del jugador después de un tiempo
        current_time = pygame.time.get_ticks()
        # Si han pasado 3 segundos desde la colisión
        if current_time - self.player_last_colission > 3000:
            # Si el jugador aún tiene vidas, crea un nuevo jugador
            if self.player_lives > 0:
                GAMELOOP.add_obj(ObjectPlayer(400, 300))
            # Resetea el tiempo de colisión
            self.player_last_colission = None

    def create_new_bigrock(self):
        # Crea una nueva roca grande en una posición aleatoria
        potential_x = [0, 400, 800]
        bigrock = BigRockObject(random.choice(potential_x), -300)
        GAMELOOP.add_obj(bigrock)

    def create_resulting_mid_rocks(self, x, y):
        # Crea dos rocas medianas resultantes de una roca grande destruida
        first_midRock = [-1, -1]
        second_midRock = [1, 1]
        GAMELOOP.add_obj(MidRockObject(x, y, first_midRock[0], first_midRock[1]))
        GAMELOOP.add_obj(MidRockObject(x, y, second_midRock[0], second_midRock[1]))