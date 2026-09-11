import random
import pygame
from src.utils.constants import CELL_SIZE, CELL_NUMBER

class Food:
    def __init__(self, image_path: str):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.pos = [0, 0]
        self.randomize()

    def randomize(self):
        self.pos = [
            random.randint(1, CELL_NUMBER - 1) * CELL_SIZE,
            random.randint(1, CELL_NUMBER - 1) * CELL_SIZE
        ]

    def draw(self, surface: pygame.Surface):
        rect = self.image.get_rect(topleft=self.pos)
        surface.blit(self.image, rect)