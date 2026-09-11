import pygame

CELL_SIZE = 40
CELL_NUMBER = 20
SCREEN_SIZE = CELL_SIZE * CELL_NUMBER

BLUE1 = (10, 10, 80)
BLUE2 = (30, 30, 100)
WHITE = (255, 255, 255)

# Mapeo de Teclas por Jugador
P1_CONTROLS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}

P2_CONTROLS = {
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0)
}