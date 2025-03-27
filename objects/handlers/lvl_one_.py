from settings import *

from objects.interactive.bullet_obj_ import BulletObject
from objects.interactive.big_rock_obj_ import BigRockObject
from objects.interactive.mid_rock_obj_ import MidRockObject
from objects.interactive.player_obj_ import ObjectPlayer
from objects.hud.score_text import ScoreTxtObject

import random

"""
    este archivo es para eventos globales del nivel. 
""" 
class OneLevelHandler:
    def __init__(self):  
        
        # score inicial del jugador al comenzar el nivel
        self.score = 0

        # el jugador tiene 3 vidas
        self.player_lives = 3

        # si las vidas llegan a cero el jugador perdio y el jugador pasa el nivel de gameover
        self.player_has_loose = False

    def update(self):

        # Detectar colisiones con proyectiles
        self.bullet_collides_with_rock_event(BigRockObject)
        self.bullet_collides_with_rock_event(MidRockObject)
        self.player_collides_with_rock_event()

    # que pasa con el disparo cuando impacta una roca
    def bullet_collides_with_rock_event(self, rockInstance):

        for obj in GAMELOOP.game_objects:
                    
            if isinstance(obj, BulletObject):

                # Buscar colisiones de rocas con proyectiles
                for rock in GAMELOOP.game_objects:

                    if isinstance(rock, rockInstance):

                        # Pasa obj y rock a is_colliding
                        if self.is_colliding(obj, rock):  

                            # Eliminar proyectil
                            GAMELOOP.remove_obj(obj)  

                            # Eliminar roca
                            GAMELOOP.remove_obj(rock)  

                            # aumentar escore cada vez que rompa una roca grande
                            self.add_score_for_big()

                            # Solo crear dos nuevas mid rocks si un 
                            if isinstance(rock, BigRockObject):
                                
                                self.create_resulting_mid_rocks(rock.x,rock.y)
                            
                            break  # Salir del bucle interno si ya se eliminó la roca

                                
           
    def add_score_for_big(self):
         
         self.score += 10
         self.update_score_hud()

    def add_score_for_mid(self):
         
         self.score += 5
         self.update_score_hud()
         
    def update_score_hud(self):
         
         for obj in GAMELOOP.hud:
              
            if isinstance(obj, ScoreTxtObject):
                 
                 obj.text_to_show = str(self.score)


    # colision de el jugador con las rocas
    def player_collides_with_rock_event(self):
         
         for obj in GAMELOOP.game_objects:
                    
            if isinstance(obj, ObjectPlayer):

                # Buscar colisiones de rocas con el jugador
                for rock in GAMELOOP.game_objects:

                    if isinstance(rock, MidRockObject) or isinstance(rock, BigRockObject):

                        # Pasa obj y rock a is_colliding
                        if self.is_colliding(obj, rock):  

                            # Eliminar obj
                            GAMELOOP.remove_obj(obj)  

                            # Eliminar roca
                            GAMELOOP.remove_obj(rock)  

                            # Solo crear dos nuevas mid rocks si un 
                            if isinstance(rock, BigRockObject):
                                
                                self.create_resulting_mid_rocks(rock.x,rock.y)
                            
                            break  # Salir del bucle interno si ya se eliminó la roca 

    def is_colliding(self, obj, rock):
        # Verifica si hay superposición entre la roca y el objeto (proyectil)
        return (
            rock.x < obj.x + obj.width and
            rock.x + rock.width > obj.x and
            rock.y < obj.y + obj.height and
            rock.y + rock.height > obj.y
        )
    


    # agregar una nueva roca grande para que el jugador nunca se quede sin rocas
    
    def create_new_bigrock(self):
        potential_x = [0,400,800]
        bigrock = BigRockObject(random.choice(potential_x),-300)

        GAMELOOP.add_obj(bigrock)  # agregar roca

        
    def create_resulting_mid_rocks(self, x,y):
        first_midRock = [-1,-1]
        second_midRock = [1,1]

        GAMELOOP.add_obj(MidRockObject(x,y,first_midRock[0], first_midRock[1]))  # agregar roca
        GAMELOOP.add_obj(MidRockObject(x,y,second_midRock[0], second_midRock[1]))  # agregar roca