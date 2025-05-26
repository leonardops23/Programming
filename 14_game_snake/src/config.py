from enum import Enum, auto


class ConfigGame:
    """
    
    """
    TITLE = "SnakeGame"
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 10 # frames por la velociadad de la serpiente

    # Configuracion de la serpiente
    CELL_SIZE = 20 # tama_o de segmento de la serpierte
    GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE # ancho de la cuadrícula
    GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE # alto de la cuadrícula

    # Colores (RGB)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GRAY = (100, 100, 100)
    DARK_GREEN = (0, 150, 0)

class Direction:
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
