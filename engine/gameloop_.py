import json, importlib

class GameloopHandler():
    def __init__(self, screen, screen_width, screen_height):
        self.current_level = {}
        self.level_transiction = False
        self.game_objects = []  # Store instantiated game objects
        self.hud = []  # Store instantiated HUD objects

        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

    def load_level(self, level):
        try:
            with open(level, "r") as file:

                if self.level_transiction:
                    return 0
                else:
                    datos = json.load(file)
                    self.current_level = datos
                    self.init_hud()  # Call initialize_level_game_objs
                    self.initialize_level_game_objs()  # Call initialize_level_game_objs
                    self.level_transiction = True
                
                

        except FileNotFoundError:
            print(f"Error: No se encontró el file '{level}'.")
            return None
        except json.JSONDecodeError:
            print(f"Error: El file '{level}' no es un JSON válido.")
            return None
        
    def init_hud(self):
        self.hud = []  # Clear previous game objects
        for hud in self.current_level['hud_objs']:

            module_name = hud['code_path']
            class_name = hud['obj_name_for_instance']
            data_for_instance = hud.get('data_for_instance', {}) 
             # Default to empty dict
            try:
                module = importlib.import_module(module_name)
                class_ = getattr(module, class_name)
                instance = class_(data_for_instance['text'], 
                                  data_for_instance['font_family'], 
                                  data_for_instance['font_size'], 
                                  data_for_instance['color'], 
                                  data_for_instance['pixel_position'], 
                                  self.screen, 
                                  self.screen_width, 
                                  self.screen_height)

                self.hud.append(instance)  # Add instance to list

            except ImportError:
                print(f"Error: No se pudo importar el módulo '{module_name}'.")
            except AttributeError:
                print(f"Error: No se encontró la clase '{class_name}' en el módulo '{module_name}'.")
            except TypeError as e:
                print(f"Error: No se pudo instanciar la clase '{class_name}': {e}")

    def initialize_level_game_objs(self):
        self.game_objects = []  # Clear previous game objects
        for game_obj in self.current_level['game_objs']:

            module_name = game_obj['code_path']
            class_name = game_obj['obj_name_for_instance']
            data_for_instance = game_obj.get('data_for_instance', {}) 
             # Default to empty dict
            try:
                module = importlib.import_module(module_name)
                class_ = getattr(module, class_name)
                instance = class_(**data_for_instance)
                self.game_objects.append(instance)  # Add instance to list
            except ImportError:
                print(f"Error: No se pudo importar el módulo '{module_name}'.")
            except AttributeError:
                print(f"Error: No se encontró la clase '{class_name}' en el módulo '{module_name}'.")
            except TypeError as e:
                print(f"Error: No se pudo instanciar la clase '{class_name}': {e}")

    def change_level(self, level):
        self.level_transiction = False
        self.load_level(level)

    def update(self):

        for object in self.game_objects:

            object.update()

        
        for object in self.hud:

            object.update()    

    # esta funcion agrega un nuevo objeto a los objetos y se puede utilizar desde afuera. 
    def add_obj(self, obj):

        self.game_objects.append(obj)

    # esta funcion remueva un objeto y se puede utilizar desde afuera. 
    def remove_obj(self, obj):

        self.game_objects.remove(obj)