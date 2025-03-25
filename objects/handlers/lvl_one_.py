from settings import *
from objects.interactive.bullet_obj_ import BulletObject
from objects.interactive.rock_class import RockClass
from objects.interactive.big_rock_obj_ import BigRockObject
from objects.interactive.mid_rock_obj_ import MidRockObject
import random
"""
    este archivo es para eventos globales del nivel. 
""" 
class OneLevelHandler:
    def __init__(self):  # Recibe GAMELOOP como argumento
        pass

    def update(self):

        # Detectar colisiones con proyectiles
        self.bullet_collides_with_rock_event(BigRockObject)
        self.bullet_collides_with_midrock(MidRockObject)

    # def rocks_collides_with_ship(self):
         

    def bullet_collides_with_rock_event(self, rockInstance):

        for obj in GAMELOOP.game_objects:
                    
                    if isinstance(obj, BulletObject):

                        # Buscar colisiones con BigRockObject

                        for rock in GAMELOOP.game_objects:

                            if isinstance(rock, rockInstance):

                                # Pasa obj y rock a is_colliding
                                if self.is_colliding(obj, rock):  

                                    # Eliminar proyectil
                                    GAMELOOP.remove_obj(obj)  

                                    # Eliminar roca
                                    GAMELOOP.remove_obj(rock)  

                                    self.create_resulting_mid_rocks(rock.x,rock.y)
                                    
                                    break  # Salir del bucle interno si ya se eliminó la roca
                                

    # Buscar colisiones con MidRockObject
    def bullet_collides_with_midrock(self, rockInstance):                        
    
       for obj in GAMELOOP.game_objects:
                    
                    if isinstance(obj, BulletObject):

                        # Buscar colisiones con BigRockObject

                        for rock in GAMELOOP.game_objects:

                            if isinstance(rock, rockInstance):

                                # Pasa obj y rock a is_colliding
                                if self.is_colliding(obj, rock):  

                                    # Eliminar proyectil
                                    GAMELOOP.remove_obj(obj)  

                                    # Eliminar roca
                                    GAMELOOP.remove_obj(rock)  
                                    
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