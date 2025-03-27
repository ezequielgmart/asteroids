
from settings import *
from engine.text_render_ import TextComponent

"""

Archivo donde se define el objeto interactivo

"""

class ScoreTxtObject():
    def __init__(self, text_to_show, font_family,font_size, color, pixel_position, screen, screen_width, screen_height):
        self.text_to_show = text_to_show
        self.font_family=font_family
        self.font_size=font_size
        self.rgb_color=color
        self.screen = screen
        self.pixel_position = pixel_position
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, text=""):

        TextComponent().render(self.text_to_show,
                               self.font_family,
                               self.font_size, 
                               self.rgb_color, 
                               self.pixel_position, 
                               self.screen, 
                               self.screen_width, 
                               self.screen_height)
    