import os

class Config:
    WIDTH_SCREEN = 900
    HEIGHT_SCREEN = 600
    FPS = 60

    CAPTION = 'Rain Dodge🚀'

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # ===== JOIN =-===
    ASSETS_DIRS = os.path.join(BASE_DIR, 'assets')

    # =====
    IMG_BG = os.path.join(ASSETS_DIRS, 'bg.jpg')
