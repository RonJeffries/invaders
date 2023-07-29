# Invaders Game
import pygame as pygame
from pygame import Rect, KEYDOWN, K_ESCAPE, QUIT, Vector2, Surface


class Game:
    def __init__(self, testing=False):
        self._testing = testing
        alien1 = (0x00, 0x00, 0x39, 0x79, 0x7A, 0x6E, 0xEC, 0xFA, 0xFA, 0xEC, 0x6E, 0x7A, 0x79, 0x39, 0x00, 0x00)
        alien2 = (0x00, 0x00, 0x00, 0x78, 0x1D, 0xBE, 0x6C, 0x3C, 0x3C, 0x3C, 0x6C, 0xBE, 0x1D, 0x78, 0x00, 0x00)
        alien3 = (0x00, 0x00, 0x00, 0x00, 0x19, 0x3A, 0x6D, 0xFA, 0xFA, 0x6D, 0x3A, 0x19, 0x00, 0x00, 0x00, 0x00)
        if not testing:
            pygame.init()
            pygame.display.set_caption("Space Invaders")
            self.delta_time = 0
            self.clock = pygame.time.Clock()
            self.screen = pygame.display.set_mode((256, 256))
            self.alien1 = self.alien_surface(alien1)
            self.alien2 = self.alien_surface(alien2)
            self.alien3 = self.alien_surface(alien3)
            self.alien1 = pygame.transform.scale_by(self.alien1, 8)
            self.alien2 = pygame.transform.scale_by(self.alien2, 8)
            self.alien3 = pygame.transform.scale_by(self.alien3, 8)
        self.player_location = Vector2(128, 128)

    def alien_surface(self, alien1):
        s = Surface((16, 8))
        s.fill("red")
        count = 0
        for byte in alien1:
            for z in range(8):
                bit = byte & 1
                byte = byte >> 1
                x = int(count / 8)
                y = 7 - int(count % 8)
                if bit:
                    s.set_at((x, y), "white")
                count += 1
        return s

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
            dest = (32, 16)
            self.screen.blit(self.alien1, dest)
            dest = (32, 16+80)
            self.screen.blit(self.alien2, dest)
            dest = (32, 16+160)
            self.screen.blit(self.alien3, dest)
            pygame.display.flip()
            self.delta_time = self.clock.tick(60) / 1000
        return "done"
