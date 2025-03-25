
from engine import TextComponent

class GameoverTxtObject(TextComponent): 

    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)


    def update(self, game_objs):
        # text_to_show = "", font_family, font_size, rgb_color
        text = "GAME OVER"
        self.render(text)