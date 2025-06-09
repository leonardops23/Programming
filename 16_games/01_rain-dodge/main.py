import pygame
from src.config import Config

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((
            Config.WIDTH_SCREEN,
            Config.HEIGHT_SCREEN,
        ))
        self.run = True


    def running(self) -> None:
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
        pygame.quit()

