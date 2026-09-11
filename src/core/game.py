import pygame
import random
from src.utils.constants import *
from src.entities.snake import Snake
from src.entities.food import Food
from src.graphics.renderer import GameRenderer

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Snake POO")
        self.clock = pygame.time.Clock()
        self.renderer = GameRenderer(self.screen)
        self.state = "MENU"
        self.tick = 5

        self.food = Food("assets/sprites/environment/Manzana.png")
        self._init_snakes()
        self._load_ui_assets()

    def _init_snakes(self):
        p1_sprites = {
            'head': 'assets/sprites/firstplayer/Head.png', 'body': 'assets/sprites/firstplayer/Body.jpg',
            'corner': 'assets/sprites/firstplayer/Body_curve.png', 'tail': 'assets/sprites/firstplayer/Tail.png'
        }
        p2_sprites = {
            'head': 'assets/sprites/secondplayer/Head_red.png', 'body': 'assets/sprites/secondplayer/Body_red.jpg',
            'corner': 'assets/sprites/secondplayer/Body_curve_red.png', 'tail': 'assets/sprites/secondplayer/Tail_red.png'
        }
        self.player1 = Snake(random.randint(1, 18), random.randint(1, 18), p1_sprites, P1_CONTROLS)
        self.player2 = Snake(random.randint(1, 18), random.randint(1, 18), p2_sprites, P2_CONTROLS)

    def _load_ui_assets(self):
        self.menu_img = pygame.transform.scale(pygame.image.load("assets/sprites/ui/Menu.png"), (SCREEN_SIZE, SCREEN_SIZE))
        self.play_btn = pygame.transform.scale(pygame.image.load("assets/sprites/ui/Play.png"), (CELL_SIZE*10, CELL_SIZE*3))
        self.play_rect = self.play_btn.get_rect(center=(SCREEN_SIZE//2, SCREEN_SIZE//2.5))
        self.winner_img = pygame.transform.scale(pygame.image.load("assets/sprites/ui/Winner.png"), (SCREEN_SIZE, SCREEN_SIZE))

    def run(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                self.player1.handle_input(event)
                self.player2.handle_input(event)
                
                if self.state == "MENU" and event.type == pygame.MOUSEBUTTONUP:
                    if self.play_rect.collidepoint(mouse_pos):
                        self.state = "RUNNING"

            self.update()
            self.render()
            self.clock.tick(self.tick)

        pygame.quit()

    def update(self):
        if self.state == "RUNNING":
            self.player1.update()
            self.player2.update()

            for player in [self.player1, self.player2]:
                if player.body[-1] == self.food.pos:
                    player.score += 1
                    self.tick += 1
                    self.food.randomize()

            if self.player1.score >= 5: self.state = "WIN_P1"
            elif self.player2.score >= 5: self.state = "WIN_P2"

    def render(self):
        if self.state == "MENU":
            self.screen.blit(self.menu_img, (0, 0))
            self.screen.blit(self.play_btn, self.play_rect)
        
        elif self.state == "RUNNING":
            self.renderer.draw_grid()
            self.food.draw(self.screen)
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.renderer.draw_scores(self.player1.score, self.player2.score)

        elif "WIN" in self.state:
            msg = "¡Jugador 1 Gana!" if self.state == "WIN_P1" else "¡Jugador 2 Gana!"
            self.renderer.draw_winner(self.winner_img, msg)

        pygame.display.update()