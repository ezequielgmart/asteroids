import pygame 

class TextComponent:
    def __init__(self, text_to_show,font_family,font_size, color, pixel_position, screen, screen_width, screen_height):

        pygame.font.init()

        self.text = text_to_show
        self.font_family=font_family
        self.font_size=font_size
        self.rgb_color=color
        self.screen = screen
        self.pixel_position = pixel_position
        self.width = screen_width
        self.height = screen_height

        # text_to_show="SNAKE ENGINE", font_family='Arial', font_size=75, rgb_color=(250, 250, 250), position="CENTER", pixel_position=None

    def render(self):
        font = pygame.font.SysFont(self.font_family, self.font_size)
        text_surface = font.render(self.text, False, self.rgb_color)
        text_rect = text_surface.get_rect()

        if self.pixel_position:
            text_rect.topleft = self.pixel_position
        elif self.pixel_position == "CENTER":
            text_rect.center = (self.width // 2, self.height // 2)
        elif isinstance(self.pixel_position, list) and len(self.pixel_position) == 2:
            text_rect.topleft = self.pixel_position
        else:
            text_rect.topleft = (0, 0)

        self.screen.blit(text_surface, text_rect)