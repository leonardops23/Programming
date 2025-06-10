import pygame
from config import Config

class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(Config.CAPTION)
        self.screen = pygame.display.set_mode((
            Config.WIDTH_SCREEN,
            Config.HEIGHT_SCREEN,
        ))
        self.bg = pygame.image.load(Config.IMG_BG)
        self.bg = pygame.transform.scale(self.bg, (Config.WIDTH_SCREEN, Config.HEIGHT_SCREEN))
        self.run = True

    def running(self) -> None:
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            
            # Draw background
            self.screen.blit(self.bg, (0, 0))
            pygame.display.flip()

        pygame.quit()
