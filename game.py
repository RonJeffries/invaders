# Invaders Game
import pygame as pygame
from pygame import Rect, KEYDOWN, K_ESCAPE, QUIT, Vector2


class Game:
    def __init__(self, testing=False):
        self._testing = testing
        if not testing:
            pygame.init()
            pygame.display.set_caption("Space Invaders")
            self.delta_time = 0
            self.clock = pygame.time.Clock()
            self.screen = pygame.display.set_mode((256, 256))
        self.player_location = Vector2(128, 128)

    def main_loop(self):
        running = not self._testing
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
            self.screen.fill("midnightblue")
            rect = Rect(0, 0, 32, 32)
            rect.center = self.player_location
            pygame.draw.rect(self.screen, "white", rect)
            pygame.draw.line(self.screen, "red", (128, 0), (128, 256))
            pygame.draw.line(self.screen, "red", (0, 128), (256, 128))
            pygame.display.flip()
            self.delta_time = self.clock.tick(60) / 1000
        return "done"
