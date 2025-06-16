import random
from ..config import Config

class Start:
    def __init__(self):
        """
        
        """
        self.x = random.randint(0, Config.WIDTH_SCREEN)
        self.y = random.randint(0, Config.HEIGHT_SCREEN)
        self.size = random.randint(1, 3)
        self.alpha = random.randint(50, 255)
        self.alpha_speed = random.randint(1, 3)
        self.alpha_direction = random.choice([-1, 1])

    def update(self):
        """
        
        """
        self.alpha += self.alpha_speed * self.alpha_direction
        if self.alpha <= 50 or self.alpha >= 255:
            self.alpha_direction *= -1

    def draw(self):
        """
        
        """
        pass
