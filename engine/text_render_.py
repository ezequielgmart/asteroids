import pygame 

class TextComponent:
    def __init__(self):

        pygame.font.init()

        # self.text = text_to_show
        # self.font_family=font_family
        # self.font_size=font_size
        # self.rgb_color=color
        # self.screen = screen
        # self.pixel_position = pixel_position
        # self.width = screen_width
        # self.height = screen_height

        # text_to_show="SNAKE ENGINE", font_family='Arial', font_size=75, rgb_color=(250, 250, 250), position="CENTER", pixel_position=None

    def render(self, text_to_show,font_family,font_size, color, pixel_position, screen, screen_width, screen_height):
        font = pygame.font.SysFont(font_family, font_size)
        text_surface = font.render(text_to_show, False, color)
        text_rect = text_surface.get_rect()

        if pixel_position:
            text_rect.topleft = pixel_position
        elif pixel_position == "CENTER":
            text_rect.center = (screen_width // 2, screen_height // 2)
        elif isinstance(pixel_position, list) and len(pixel_position) == 2:
            text_rect.topleft = pixel_position
        else:
            text_rect.topleft = (0, 0)

        screen.blit(text_surface, text_rect)