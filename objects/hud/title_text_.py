
from settings import *
from engine.text_render_ import TextComponent

"""

Archivo donde se define el objeto interactivo

"""

class TitleTxtObject(TextComponent):
    def __init__(self, text_to_show,font_family,font_size, color, pixel_position, screen, screen_width, screen_height):
        super().__init__(text_to_show,font_family,font_size, color, pixel_position, screen, screen_width, screen_height)

    