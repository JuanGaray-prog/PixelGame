import pygame
from src.utils.constants import CELL_SIZE, CELL_NUMBER, BLUE1, BLUE2, WHITE

class GameRenderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.Font(None, 60)

    def draw_grid(self):
        self.screen.fill(BLUE1)
        for row in range(CELL_NUMBER):
            for col in range(CELL_NUMBER):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, BLUE2, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def draw_scores(self, score1: int, score2: int):
        p1_txt = self.font.render(f"P1: {score1}", True, WHITE)
        p2_txt = self.font.render(f"P2: {score2}", True, WHITE)
        self.screen.blit(p1_txt, (10, 10))
        self.screen.blit(p2_txt, (self.screen.get_width() - p2_txt.get_width() - 10, 10))

    def draw_winner(self, winner_img: pygame.Surface, message: str):
        self.screen.blit(winner_img, (0, 0))
        txt = self.font.render(message, True, WHITE)
        rect = txt.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 1.2))
        self.screen.blit(txt, rect)