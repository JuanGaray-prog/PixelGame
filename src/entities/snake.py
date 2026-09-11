import pygame
from src.utils.constants import CELL_SIZE, CELL_NUMBER

class Snake:
    def __init__(self, start_x: int, start_y: int, sprites: dict, controls: dict):
        self.body = [[start_x * CELL_SIZE, start_y * CELL_SIZE]]
        self.dir = (0, 0)
        self.controls = controls
        self.score = 0
        
        self.sprites = {
            key: pygame.transform.scale(pygame.image.load(path).convert_alpha(), (CELL_SIZE, CELL_SIZE))
            for key, path in sprites.items()
        }

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and event.key in self.controls:
            new_dir = self.controls[event.key]
            if (new_dir[0] * -1, new_dir[1] * -1) != self.dir:
                self.dir = new_dir

    def update(self):
        if self.dir == (0, 0):
            return

        head_x, head_y = self.body[-1]
        grid_x = (head_x // CELL_SIZE) + self.dir[0]
        grid_y = (head_y // CELL_SIZE) + self.dir[1]

        grid_x %= CELL_NUMBER
        grid_y %= CELL_NUMBER

        new_head = [grid_x * CELL_SIZE, grid_y * CELL_SIZE]
        self.body.append(new_head)

        if len(self.body) > self.score + 1:
            self.body.pop(0)

    def _get_vector(self, p1, p2):
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        if dx > CELL_SIZE: dx = -CELL_SIZE
        elif dx < -CELL_SIZE: dx = CELL_SIZE
        if dy > CELL_SIZE: dy = -CELL_SIZE
        elif dy < -CELL_SIZE: dy = CELL_SIZE
        return dx, dy

    def draw(self, surface: pygame.Surface):
        if len(self.body) < 2:
            rect = pygame.Rect(self.body[0][0], self.body[0][1], CELL_SIZE, CELL_SIZE)
            surface.blit(self.sprites['head'], rect)
            return

        for index, block in enumerate(self.body):
            rect = pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE)

            if index == len(self.body) - 1:
                dx, dy = self._get_vector(self.body[index - 1], block)
                angles = {(CELL_SIZE, 0): 90, (-CELL_SIZE, 0): 270, (0, CELL_SIZE): 0, (0, -CELL_SIZE): 180}
                angle = angles.get((dx, dy), 0)
                surface.blit(pygame.transform.rotate(self.sprites['head'], angle), rect)

            elif index == 0:
                dx, dy = self._get_vector(block, self.body[index + 1])
                angles = {(CELL_SIZE, 0): 180, (-CELL_SIZE, 0): 0, (0, CELL_SIZE): 90, (0, -CELL_SIZE): 270}
                angle = angles.get((dx, dy), 0)
                surface.blit(pygame.transform.rotate(self.sprites['tail'], angle), rect)

            else:
                p_prev, p_next = self.body[index - 1], self.body[index + 1]
                dx_p, dy_p = self._get_vector(block, p_prev)
                dx_n, dy_n = self._get_vector(block, p_next)

                if dx_p != 0 and dx_n != 0:
                    surface.blit(self.sprites['body'], rect)
                elif dy_p != 0 and dy_n != 0:
                    surface.blit(pygame.transform.rotate(self.sprites['body'], 90), rect)
                else:
                    corners = {
                        (-CELL_SIZE, -CELL_SIZE): 180,
                        (-CELL_SIZE, CELL_SIZE): 270,
                        (CELL_SIZE, -CELL_SIZE): 90,
                        (CELL_SIZE, CELL_SIZE): 0
                    }
                    angle = corners.get((dx_p or dx_n, dy_n or dy_p), 0)
                    surface.blit(pygame.transform.rotate(self.sprites['corner'], angle), rect)