import pygame

# clase especializada del motor que se encarga de tomar una parte de un sprite_sheet y convertirlo en una imagen con capacidad de rotacion
class SpriteSheetRender:
    def __init__(self, image_sheet_path):
        self.sheet = pygame.image.load(image_sheet_path).convert_alpha()

    def render_sprite_from_sheet(self, frame, width, height, scale, colour, rotation_angle):
        # Crear una superficie para almacenar el sprite
        image = pygame.Surface((width, height), pygame.SRCALPHA)

        x = frame * width  # Calcular posición del sprite en la hoja

        # Dibujar la parte seleccionada de la hoja de sprites en la nueva superficie
        image.blit(self.sheet, (0, 0), (x, 0, width, height))

        # Escalar la imagen al tamaño deseado
        image = pygame.transform.scale(image, (width * scale, height * scale))

        # Aplicar rotación
        image = pygame.transform.rotate(image, rotation_angle)

        # Establecer un color transparente
        image.set_colorkey(colour)

        return image

"""
        Renderiza un sprite individual desde la hoja de sprites.

        Args:
            frame_x (int): Coordenada X del frame en la hoja de sprites.
            frame_y (int): Coordenada Y del frame en la hoja de sprites.
            width (int): Ancho del sprite.
            height (int): Alto del sprite.
            scale (float): Factor de escala del sprite.
            colour (tuple): Color clave para la transparencia (o None para sin transparencia).
            rotation_angle (float): Ángulo de rotación del sprite.

        Returns:
            pygame.Surface: Superficie que contiene el sprite renderizado.
        """

class MultipleSpriteSheetRender:

    
    # class SpriteSheetRender:
    def __init__(self, image_sheet_path):
        self.sheet = pygame.image.load(image_sheet_path).convert_alpha()

    def render_sprite_from_sheet(self, frame_x, frame_y, width, height, scale, colour, rotation_angle):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (frame_x, frame_y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image = pygame.transform.rotate(image, rotation_angle)
        image.set_colorkey(colour)
        return image

# Solo renderiza una imagen    
class SingleSpriteRender:
    def __init__(self, image_path):
        # Cargar la imagen directamente
        self.image = pygame.image.load(image_path).convert_alpha()

    def render_sprite(self, scale=1, colour=None, rotation_angle=0):
        # Escalar la imagen al tamaño deseado
        image = pygame.transform.scale(self.image, (
            int(self.image.get_width() * scale), 
            int(self.image.get_height() * scale)
        ))

        # Aplicar rotación si es necesario
        if rotation_angle != 0:
            image = pygame.transform.rotate(image, rotation_angle)

        # Establecer un color transparente si se especifica
        if colour:
            image.set_colorkey(colour)

        return image
